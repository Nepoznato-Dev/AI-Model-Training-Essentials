# Security

## Overview

Security best practices for AI/ML systems, covering model security, application security, and compliance.

---

## Threat Modeling

### STRIDE Framework for ML

| Threat | Description | ML-Specific Examples |
|--------|-------------|---------------------|
| **Spoofing** | Impersonating legitimate users/entities | API key theft, credential stuffing |
| **Tampering** | Modifying data or models | Training data poisoning, model weight manipulation |
| **Repudiation** | Denying actions occurred | Lack of audit logs for predictions |
| **Information Disclosure** | Exposing sensitive data | Model inversion attacks, training data leakage |
| **Denial of Service** | Disrupting service availability | Adversarial examples causing resource exhaustion |
| **Elevation of Privilege** | Gaining unauthorized access | Exploiting vulnerabilities to access model internals |

### AI-Specific Threats

```python
# Threat: Model Inversion Attack
# Attacker reconstructs training data from model outputs

def defend_against_inversion():
    """
    Defenses:
    1. Limit prediction confidence output
    2. Add differential privacy
    3. Rate limit queries per user
    4. Monitor for suspicious query patterns
    """
    pass

# Threat: Membership Inference
# Attacker determines if specific data was in training set

def defend_against_membership_inference():
    """
    Defenses:
    1. Regularization during training
    2. Differential privacy
    3. Limit model confidence
    4. Ensemble methods
    """
    pass

# Threat: Model Stealing
# Attacker creates substitute model via queries

def defend_against_model_stealing():
    """
    Defenses:
    1. Rate limiting
    2. Query watermarking
    3. Reduce prediction precision
    4. Legal agreements (ToS)
    5. Monitor for systematic queries
    """
    pass
```

---

## Adversarial Robustness

### Adversarial Attacks

```python
import torch

# Fast Gradient Sign Method (FGSM)
def fgsm_attack(model, input_tensor, label, epsilon=0.01):
    """Generate adversarial example using FGSM"""
    input_tensor.requires_grad = True
    output = model(input_tensor)
    loss = torch.nn.functional.cross_entropy(output, label)
    
    loss.backward()
    gradient = input_tensor.grad.detach()
    sign_gradient = torch.sign(gradient)
    
    adversarial_input = input_tensor + epsilon * sign_gradient
    return adversarial_input.clamp(0, 1)

# Projected Gradient Descent (PGD)
def pgd_attack(model, input_tensor, label, epsilon=0.01, steps=10, alpha=0.001):
    """Generate adversarial example using iterative PGD"""
    adv_input = input_tensor.clone().detach()
    
    for _ in range(steps):
        adv_input.requires_grad = True
        output = model(adv_input)
        loss = torch.nn.functional.cross_entropy(output, label)
        
        loss.backward()
        gradient = adv_input.grad.detach()
        
        with torch.no_grad():
            adv_input = adv_input + alpha * torch.sign(gradient)
            # Project back to epsilon ball
            diff = adv_input - input_tensor
            diff = torch.clamp(diff, -epsilon, epsilon)
            adv_input = torch.clamp(input_tensor + diff, 0, 1)
    
    return adv_input
```

### Defenses

```python
# Adversarial Training
def adversarial_training_step(model, inputs, labels, epsilon=0.01):
    """Train with adversarial examples"""
    model.train()
    
    # Generate adversarial examples
    adv_inputs = fgsm_attack(model, inputs, labels, epsilon)
    
    # Train on both clean and adversarial examples
    clean_outputs = model(inputs)
    adv_outputs = model(adv_inputs)
    
    clean_loss = torch.nn.functional.cross_entropy(clean_outputs, labels)
    adv_loss = torch.nn.functional.cross_entropy(adv_outputs, labels)
    
    total_loss = 0.5 * clean_loss + 0.5 * adv_loss
    total_loss.backward()
    
    return total_loss.item()

# Randomized Smoothing
class RandomizedSmoothing(torch.nn.Module):
    def __init__(self, base_model, sigma=0.1, num_samples=100):
        super().__init__()
        self.base_model = base_model
        self.sigma = sigma
        self.num_samples = num_samples
    
    def forward(self, x):
        # Add Gaussian noise and average predictions
        predictions = []
        for _ in range(self.num_samples):
            noisy_x = x + torch.randn_like(x) * self.sigma
            pred = self.base_model(noisy_x)
            predictions.append(pred)
        
        return torch.stack(predictions).mean(dim=0)

# Input Transformation
def jpeg_compression_defense(input_tensor, quality=75):
    """Apply JPEG compression as defense"""
    from PIL import Image
    import io
    
    # Convert tensor to PIL image
    img = transforms.ToPILImage()(input_tensor.squeeze())
    
    # Compress and decompress
    buffer = io.BytesIO()
    img.save(buffer, format='JPEG', quality=quality)
    buffer.seek(0)
    img_restored = Image.open(buffer)
    
    # Convert back to tensor
    return transforms.ToTensor()(img_restored)
```

---

## Secure Deployment

### Authentication & Authorization

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

app = FastAPI()
security = HTTPBearer()

SECRET_KEY = "your-secret-key"  # Use environment variable!
ALGORITHM = "HS256"

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """Verify JWT token"""
    try:
        payload = jwt.decode(
            credentials.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

@app.post("/predict")
async def predict(payload: dict = Depends(verify_token)):
    # User is authenticated, proceed with prediction
    user_id = payload.get("sub")
    # ... prediction logic
```

### Rate Limiting

```python
from slowapi import SlowAPISlow, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

app = FastAPI()
limiter = SlowAPISlow(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/predict")
@limiter.limit("100/minute")  # 100 requests per minute per IP
async def predict(request: Request):
    # ... prediction logic
```

### Input Validation

```python
from pydantic import BaseModel, validator, Field
import numpy as np

class PredictionInput(BaseModel):
    features: list[float] = Field(..., min_items=10, max_items=1000)
    
    @validator('features')
    def validate_features(cls, v):
        # Check for NaN values
        if any(np.isnan(x) for x in v):
            raise ValueError("Features cannot contain NaN values")
        
        # Check for reasonable ranges
        if any(abs(x) > 1e6 for x in v):
            raise ValueError("Feature values out of expected range")
        
        return v

class PredictionOutput(BaseModel):
    prediction: int
    confidence: float = Field(..., ge=0, le=1)
    
    class Config:
        schema_extra = {
            "example": {
                "prediction": 1,
                "confidence": 0.95
            }
        }
```

---

## Data Protection

### Encryption at Rest

```python
from cryptography.fernet import Fernet
import pickle

class EncryptedModelStorage:
    def __init__(self, key: bytes = None):
        if key is None:
            key = Fernet.generate_key()
        self.cipher = Fernet(key)
        self.key = key  # Store securely!
    
    def save_model(self, model, path: str):
        """Save encrypted model"""
        # Serialize model
        model_bytes = pickle.dumps(model)
        
        # Encrypt
        encrypted = self.cipher.encrypt(model_bytes)
        
        # Save
        with open(path, 'wb') as f:
            f.write(encrypted)
    
    def load_model(self, path: str):
        """Load and decrypt model"""
        with open(path, 'rb') as f:
            encrypted = f.read()
        
        # Decrypt
        decrypted = self.cipher.decrypt(encrypted)
        
        # Deserialize
        return pickle.loads(decrypted)
```

### Secure Secrets Management

```python
# ❌ Wrong: Hardcoded secrets
SECRET_KEY = "super-secret-key-123"
DATABASE_URL = "postgresql://user:password@localhost/db"

# ✅ Correct: Environment variables
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

SECRET_KEY = os.environ.get("SECRET_KEY")
DATABASE_URL = os.environ.get("DATABASE_URL")

# Or use a secrets manager
import boto3

secrets_client = boto3.client('secretsmanager')
response = secrets_client.get_secret_value(SecretId='my-app-secrets')
secrets = json.loads(response['SecretString'])
```

---

## Compliance & Governance

### Model Cards

```markdown
# Model Card: Fraud Detection Model

## Model Details
- **Developer**: AI Team
- **Version**: 2.1.0
- **Date**: 2024-01-15
- **License**: Proprietary

## Intended Use
- Detecting fraudulent transactions in e-commerce
- Not intended for medical or legal decisions

## Training Data
- **Source**: Internal transaction logs (2020-2023)
- **Size**: 10M transactions
- **Preprocessing**: Normalized, balanced with SMOTE

## Evaluation Data
- **Test Set**: Hold-out 20% of data
- **Metrics**: 
  - Accuracy: 98.5%
  - Precision: 94.2%
  - Recall: 96.8%
  - F1 Score: 95.5%

## Limitations
- Performance may degrade on new fraud patterns
- Requires retraining quarterly
- Not validated for international transactions

## Ethical Considerations
- Regular bias audits conducted
- False positives reviewed by human analysts
- Appeals process available for flagged transactions
```

### Audit Logging

```python
import logging
import json
from datetime import datetime

audit_logger = logging.getLogger('audit')
audit_logger.setLevel(logging.INFO)

# Separate file handler for audit logs
handler = logging.FileHandler('audit.log')
handler.setFormatter(logging.Formatter('%(message)s'))
audit_logger.addHandler(handler)

def log_model_access(user_id: str, model_id: str, action: str, details: dict):
    """Log model access for audit trail"""
    audit_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": "model_access",
        "user_id": user_id,
        "model_id": model_id,
        "action": action,
        "details": details,
        "ip_address": get_client_ip(),
        "user_agent": get_user_agent()
    }
    audit_logger.info(json.dumps(audit_entry))

# Usage
log_model_access(
    user_id="user123",
    model_id="fraud-detection-v2",
    action="predict",
    details={"request_id": "req-456", "latency_ms": 45}
)
```

---

## Security Checklist

### Development
- [ ] Threat modeling completed
- [ ] Security requirements defined
- [ ] Input validation implemented
- [ ] Error messages don't leak information
- [ ] Dependencies scanned for vulnerabilities

### Deployment
- [ ] HTTPS/TLS enabled
- [ ] Authentication required
- [ ] Rate limiting configured
- [ ] Secrets managed securely
- [ ] Network segmentation in place

### Operations
- [ ] Audit logging enabled
- [ ] Monitoring for anomalies
- [ ] Incident response plan ready
- [ ] Regular security assessments
- [ ] Patch management process

### Compliance
- [ ] Data privacy requirements met
- [ ] Model documentation complete
- [ ] Bias assessment conducted
- [ ] Access controls documented
- [ ] Retention policies defined

---

## Related Resources

- [Architecture Patterns](architecture_patterns.md)
- [Deployment Guide](deployment.md)
- [Best Practices Checklist](references/checklist.md)
- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
