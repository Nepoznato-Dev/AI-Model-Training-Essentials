# Security

## Overview

Security best practices for AI/ML systems, covering model security, application security, and compliance.

> **Security note:** The examples below are educational patterns, not complete production security controls. Secrets, keys, model artifacts, and user data require environment-specific threat modeling and operational controls.

---

## Threat Modeling

### STRIDE Framework for ML

| Threat | Description | ML-Specific Examples |
|--------|-------------|---------------------|
| **Spoofing** | Impersonating legitimate users/entities | API key theft, credential stuffing |
| **Tampering** | Modifying data or models | Training-data poisoning, artifact manipulation |
| **Repudiation** | Denying actions occurred | Missing or incomplete audit logs |
| **Information Disclosure** | Exposing sensitive data | Model inversion, membership inference, prompt/data leakage |
| **Denial of Service** | Disrupting availability | Expensive inference, adversarial resource exhaustion |
| **Elevation of Privilege** | Gaining unauthorized access | Tool abuse, sandbox escape, compromised credentials |

For agentic systems, also model prompt injection, indirect prompt injection, unsafe tool use, excessive agency, malicious retrieved documents, and secret exfiltration.

---

## Adversarial Robustness

### FGSM

Use `torch.autograd.grad` so the attack does not accidentally accumulate gradients in model parameters.

```python
import torch
import torch.nn.functional as F


def fgsm_attack(model, input_tensor, label, epsilon=0.01):
    """Generate an FGSM adversarial example."""
    was_training = model.training
    model.eval()
    x = input_tensor.detach().clone().requires_grad_(True)

    output = model(x)
    loss = F.cross_entropy(output, label)
    gradient = torch.autograd.grad(loss, x)[0]

    adversarial = (x + epsilon * gradient.sign()).clamp(0, 1).detach()
    model.train(was_training)
    return adversarial
```

### PGD

```python
import torch
import torch.nn.functional as F


def pgd_attack(model, input_tensor, label, epsilon=0.01, steps=10, alpha=0.001):
    """Generate an L-infinity PGD adversarial example."""
    original = input_tensor.detach()
    adv = original.clone()
    was_training = model.training
    model.eval()

    for _ in range(steps):
        x = adv.detach().requires_grad_(True)
        output = model(x)
        loss = F.cross_entropy(output, label)
        gradient = torch.autograd.grad(loss, x)[0]

        with torch.no_grad():
            adv = adv + alpha * gradient.sign()
            delta = torch.clamp(adv - original, -epsilon, epsilon)
            adv = (original + delta).clamp(0, 1)

    model.train(was_training)
    return adv.detach()
```

### Adversarial training step

The optimizer must be supplied by the caller and stepped explicitly. The attack itself should not silently modify optimizer/model gradients.

```python
def adversarial_training_step(model, optimizer, inputs, labels, epsilon=0.01):
    model.train()
    adv_inputs = fgsm_attack(model, inputs, labels, epsilon)

    optimizer.zero_grad(set_to_none=True)
    clean_outputs = model(inputs)
    adv_outputs = model(adv_inputs)

    clean_loss = F.cross_entropy(clean_outputs, labels)
    adv_loss = F.cross_entropy(adv_outputs, labels)
    total_loss = 0.5 * clean_loss + 0.5 * adv_loss
    total_loss.backward()
    optimizer.step()

    return total_loss.item()
```

### Randomized smoothing

Averaging noisy predictions is useful as a robustness technique, but it is **not by itself a certified randomized-smoothing implementation**. Certified smoothing requires class-count statistics and an explicit confidence/abstention procedure.

```python
def noisy_prediction_average(model, x, sigma=0.1, num_samples=100):
    predictions = []
    with torch.no_grad():
        for _ in range(num_samples):
            noisy_x = x + torch.randn_like(x) * sigma
            predictions.append(model(noisy_x))
    return torch.stack(predictions).mean(dim=0)
```

### JPEG transformation

```python
def jpeg_compression_defense(input_tensor, quality=75):
    """Apply JPEG round-trip to a single image tensor."""
    from PIL import Image
    import io
    from torchvision import transforms

    image = transforms.ToPILImage()(input_tensor.detach().cpu().squeeze())
    buffer = io.BytesIO()
    image.save(buffer, format="JPEG", quality=quality)
    buffer.seek(0)
    restored = Image.open(buffer).convert("RGB")
    return transforms.ToTensor()(restored)
```

---

## Secure Deployment

### Authentication

Never put a real secret in source code. Use a secret manager or environment variable and restrict accepted JWT algorithms/claims according to the deployment's identity provider.

```python
import os
import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

app = FastAPI()
security = HTTPBearer()
SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = "HS256"


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        return jwt.decode(
            credentials.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
    except jwt.ExpiredSignatureError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired") from exc
    except jwt.InvalidTokenError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc
```

### Rate limiting

The previous example used a nonexistent `SlowAPISlow` class. SlowAPI uses `Limiter`, and the decorated route must receive the request object.

```python
from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/predict")
@limiter.limit("100/minute")
async def predict(request: Request):
    return {"status": "ok"}
```

### Input validation (Pydantic v2)

```python
from pydantic import BaseModel, ConfigDict, Field, field_validator
import math

class PredictionInput(BaseModel):
    features: list[float] = Field(..., min_length=10, max_length=1000)

    @field_validator("features")
    @classmethod
    def validate_features(cls, values):
        if any(not math.isfinite(x) for x in values):
            raise ValueError("Features must contain only finite numbers")
        if any(abs(x) > 1e6 for x in values):
            raise ValueError("Feature values out of expected range")
        return values

class PredictionOutput(BaseModel):
    model_config = ConfigDict(
        json_schema_extra={
            "example": {"prediction": 1, "confidence": 0.95}
        }
    )
    prediction: int
    confidence: float = Field(..., ge=0, le=1)
```

---

## Data Protection

Prefer safe, explicit model artifact formats over arbitrary pickle deserialization. Encryption does not make untrusted pickle data safe.

```python
from cryptography.fernet import Fernet

class EncryptedBytesStorage:
    def __init__(self, key: bytes):
        self.cipher = Fernet(key)

    def save(self, data: bytes, path: str):
        with open(path, "wb") as handle:
            handle.write(self.cipher.encrypt(data))

    def load(self, path: str) -> bytes:
        with open(path, "rb") as handle:
            return self.cipher.decrypt(handle.read())
```

Generate/store the key outside the model artifact, preferably using a dedicated secrets-management system. Do not silently generate an ephemeral key that is lost when the process exits.

For PyTorch models, prefer a `state_dict`/`safetensors` workflow and load only artifacts you trust. Do not treat encrypted pickle as a general-purpose secure model format.

---

## Secure Secrets Management

```python
import os

SECRET_KEY = os.environ["SECRET_KEY"]
DATABASE_URL = os.environ["DATABASE_URL"]
```

For production systems, use the platform's secrets manager instead of committing `.env` files or secrets to source control.

---

## Audit Logging

Use timezone-aware UTC timestamps and explicitly pass request metadata into the logging function rather than relying on undefined helper functions.

```python
import json
import logging
from datetime import datetime, timezone

logger = logging.getLogger("audit")


def log_model_access(*, user_id, model_id, action, details, ip_address=None, user_agent=None):
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": "model_access",
        "user_id": user_id,
        "model_id": model_id,
        "action": action,
        "details": details,
        "ip_address": ip_address,
        "user_agent": user_agent,
    }
    logger.info(json.dumps(entry, separators=(",", ":")))
```

Define retention, access control, redaction, rotation, and tamper-resistance requirements separately for production deployments.

---

## Security Checklist

### Development
- [ ] Threat modeling completed
- [ ] Security requirements defined
- [ ] Input validation implemented
- [ ] Error messages don't leak sensitive information
- [ ] Dependencies scanned for vulnerabilities
- [ ] Model/data artifacts have provenance and integrity checks

### Agentic Systems
- [ ] Tools use least privilege
- [ ] Shell/filesystem/network access is allowlisted
- [ ] Destructive actions require appropriate confirmation
- [ ] Retrieved content is treated as untrusted input
- [ ] Secrets are isolated from model/tool context
- [ ] Tool calls are audited

### Deployment
- [ ] HTTPS/TLS enabled
- [ ] Authentication and authorization required
- [ ] Rate limiting configured
- [ ] Secrets managed securely
- [ ] Network segmentation in place

### Operations
- [ ] Audit logging enabled
- [ ] Monitoring for anomalies
- [ ] Incident response plan ready
- [ ] Regular security assessments
- [ ] Patch management process defined

---

## Related Resources

- [Architecture Patterns](architecture_patterns.md)
- [Deployment Guide](deployment.md)
- [Best Practices Checklist](references/checklist.md)
- [OWASP Top 10 for LLMs](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
