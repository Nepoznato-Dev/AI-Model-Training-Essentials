# Authentication and Authorization for AI Systems

Implementing secure access control in AI/ML applications.

## Overview

Authentication (AuthN) verifies **who** a user is, while Authorization (AuthZ) determines **what** they can do. Both are critical for protecting AI systems.

## Authentication Methods

### API Key Authentication
Simple token-based authentication for service-to-service communication.

```python
# Example: API Key validation
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

@app.get("/inference")
async def inference(x_api_key: str = Header(...)):
    if not validate_api_key(x_api_key):
        raise HTTPException(status_code=401, detail="Invalid API key")
    return {"result": "model output"}
```

**Best Practices**:
- Use HTTPS only
- Rotate keys regularly (every 90 days)
- Store keys in environment variables or secret managers
- Implement rate limiting per key
- Never log API keys

### JWT (JSON Web Tokens)
Stateless authentication suitable for user-facing applications.

```python
import jwt
from datetime import datetime, timedelta

def create_token(user_id: str) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=1),
        "iat": datetime.utcnow()
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        raise Exception("Token expired")
    except jwt.InvalidTokenError:
        raise Exception("Invalid token")
```

**Best Practices**:
- Use short expiration times (15 min - 1 hour)
- Implement refresh tokens for long sessions
- Include minimal claims in payload
- Validate issuer and audience
- Use RS256 for distributed systems

### OAuth 2.0 / OpenID Connect
Industry-standard protocol for authorization and authentication.

**Flows for AI Applications**:
- **Client Credentials**: Service-to-service (M2M)
- **Authorization Code**: User-facing web apps
- **Device Flow**: CLI tools and IoT devices

```python
# Example: OAuth2 with FastAPI
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    user = await get_current_user(token)
    return {"user": user}
```

### Multi-Factor Authentication (MFA)
Add extra security layer for sensitive operations.

**MFA Methods**:
- TOTP (Time-based One-Time Password)
- SMS codes (less secure)
- Email verification
- Hardware tokens (YubiKey)
- Biometric authentication

```python
import pyotp

def generate_totp_secret():
    return pyotp.random_base32()

def verify_totp(secret: str, code: str) -> bool:
    totp = pyotp.TOTP(secret)
    return totp.verify(code)
```

## Authorization Models

### Role-Based Access Control (RBAC)
Permissions assigned to roles, users assigned to roles.

```python
ROLES = {
    "admin": ["read", "write", "delete", "manage_users"],
    "developer": ["read", "write", "deploy"],
    "analyst": ["read", "query"],
    "viewer": ["read"]
}

def check_permission(user_role: str, required_permission: str) -> bool:
    return required_permission in ROLES.get(user_role, [])
```

**Common Roles for AI Systems**:
- **Admin**: Full system access
- **ML Engineer**: Model training and deployment
- **Data Scientist**: Data access and experimentation
- **Analyst**: Query and visualization only
- **Viewer**: Read-only access to dashboards

### Attribute-Based Access Control (ABAC)
Fine-grained access based on attributes.

```python
def can_access_model(user: dict, model: dict) -> bool:
    conditions = [
        user["department"] == model["owner_department"],
        user["clearance_level"] >= model["required_clearance"],
        datetime.now() <= user["access_expiry"]
    ]
    return all(conditions)
```

**Attributes Considered**:
- User attributes (role, department, clearance)
- Resource attributes (sensitivity, owner, classification)
- Environmental attributes (time, location, device)
- Action attributes (read, write, delete, train)

### Policy-Based Access Control
Dynamic policies using rule engines.

```python
# Example using Rego (Open Policy Agent)
# policy.rego
package authz

default allow = false

allow {
    input.user.role == "admin"
}

allow {
    input.action == "read"
    input.user.department == input.resource.department
}
```

## AI-Specific Authorization Concerns

### Model Access Control
Control who can:
- Query specific models
- Access model outputs
- View model metadata
- Retrain or fine-tune
- Deploy to production

```python
class ModelAccessController:
    def __init__(self):
        self.model_permissions = {}
    
    def grant_access(self, user_id: str, model_id: str, permissions: list):
        key = f"{user_id}:{model_id}"
        self.model_permissions[key] = permissions
    
    def can_query(self, user_id: str, model_id: str) -> bool:
        key = f"{user_id}:{model_id}"
        return "query" in self.model_permissions.get(key, [])
    
    def can_train(self, user_id: str, model_id: str) -> bool:
        key = f"{user_id}:{model_id}"
        return "train" in self.model_permissions.get(key, [])
```

### Data Access Control
Protect training data and sensitive inputs.

**Considerations**:
- PII (Personally Identifiable Information) handling
- Data residency requirements
- Purpose limitation enforcement
- Audit trails for data access

### Rate Limiting and Quotas
Prevent abuse and manage resource usage.

```python
from collections import defaultdict
import time

class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window = window_seconds
        self.requests = defaultdict(list)
    
    def is_allowed(self, user_id: str) -> bool:
        now = time.time()
        # Clean old requests
        self.requests[user_id] = [
            t for t in self.requests[user_id] 
            if now - t < self.window
        ]
        # Check limit
        if len(self.requests[user_id]) >= self.max_requests:
            return False
        self.requests[user_id].append(now)
        return True
```

## Implementation Best Practices

### 1. Defense in Depth
Layer multiple security controls:
```
User → WAF → Auth Gateway → Rate Limiter → Application → Database
       ↓      ↓           ↓             ↓            ↓
     Log    Log         Log           Log          Log
```

### 2. Principle of Least Privilege
Grant minimum necessary permissions:
```python
# ❌ Bad: Overly permissive
@app.delete("/models/{model_id}")
async def delete_model(model_id: str, user: User = Depends(get_current_user)):
    # Any authenticated user can delete

# ✅ Good: Restricted by role
@app.delete("/models/{model_id}")
async def delete_model(
    model_id: str, 
    user: User = Depends(require_role("admin"))
):
    # Only admins can delete
```

### 3. Secure Session Management
```python
from secrets import token_urlsafe

def create_session(user_id: str) -> str:
    session_id = token_urlsafe(32)
    redis.setex(
        f"session:{session_id}",
        SESSION_TIMEOUT,
        user_id
    )
    return session_id

def invalidate_session(session_id: str):
    redis.delete(f"session:{session_id}")
```

### 4. Audit Logging
Log all authentication and authorization events:
```python
import logging
from datetime import datetime

security_logger = logging.getLogger("security")

def log_auth_event(event_type: str, user_id: str, details: dict):
    security_logger.info({
        "timestamp": datetime.utcnow().isoformat(),
        "event": event_type,
        "user_id": user_id,
        "details": details,
        "ip_address": get_client_ip(),
        "user_agent": get_user_agent()
    })

# Usage examples
log_auth_event("login_success", user.id, {"method": "jwt"})
log_auth_event("access_denied", user.id, {"resource": model_id, "action": "delete"})
log_auth_event("permission_change", admin.id, {"target_user": user.id, "new_role": "admin"})
```

## Common Vulnerabilities to Avoid

### 1. Broken Authentication
- ❌ Weak password policies
- ❌ No account lockout after failed attempts
- ❌ Session fixation vulnerabilities
- ✅ Use established libraries (not custom crypto)
- ✅ Implement account lockout
- ✅ Regenerate session IDs after login

### 2. Insecure Direct Object References
```python
# ❌ Vulnerable: User can access any model by ID
@app.get("/models/{model_id}")
async def get_model(model_id: str):
    return db.models[model_id]

# ✅ Secure: Check ownership/permissions
@app.get("/models/{model_id}")
async def get_model(model_id: str, user: User = Depends(get_current_user)):
    model = db.models.get(model_id)
    if not model or not user.can_access(model):
        raise HTTPException(status_code=403)
    return model
```

### 3. Missing Function-Level Access Control
- Verify permissions for every endpoint
- Don't rely on UI hiding features
- Test APIs directly (bypass frontend)

## Tools and Libraries

### Python Libraries
- `PyJWT` - JWT encoding/decoding
- `python-jose` - JWT and JWS/JWE
- `pyotp` - TOTP generation/validation
- `passlib` - Password hashing
- `fastapi-security` - Security utilities for FastAPI
- `authlib` - OAuth client/server

### Infrastructure
- **Auth0** - Managed authentication service
- **Okta** - Enterprise identity management
- **Keycloak** - Open-source IAM
- **AWS Cognito** - AWS user pools
- **Ory Stack** - Open-source auth tools

## Compliance Requirements

### GDPR
- Right to access personal data
- Right to erasure ("right to be forgotten")
- Data portability
- Consent management

### HIPAA
- Unique user identification
- Emergency access procedures
- Automatic logoff
- Encryption and decryption

### SOC 2
- Access control policies
- User access reviews
- Termination procedures
- Vendor access management

---

**Related Documents**:
- [Secure Coding](secure_coding.md)
- [Threat Modeling](threat_modeling.md)

**Next Steps**: Implement authentication and authorization for your AI application following the patterns above.
