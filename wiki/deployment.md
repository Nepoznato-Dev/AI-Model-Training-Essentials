# Deployment

## Overview

Guide to deploying machine learning models to production environments. The examples below are intentionally educational; provider SDKs and framework APIs should be checked against the versions used by your project before production deployment.

---

## Deployment Strategies

### 1. Batch Inference

Process data in batches on a schedule.

**Use Cases:**
- Daily recommendations
- Weekly forecasting
- Offline processing

**Implementation:**
```python
from datetime import datetime, timezone
import pandas as pd


def batch_predict(model):
    data = load_new_data()
    predictions = model.predict(data)
    results = pd.DataFrame({
        "timestamp": datetime.now(timezone.utc),
        "input_id": data.id,
        "prediction": predictions,
    })
    results.to_csv(f"predictions/{datetime.now(timezone.utc):%Y%m%d}.csv", index=False)
```

### 2. Real-time API

Serve predictions via REST or gRPC API.

**FastAPI Example:**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch
import time

app = FastAPI()
model = load_model()  # Define this for your model/artifact format.
model.eval()

class InputData(BaseModel):
    features: list[float]

class PredictionResponse(BaseModel):
    prediction: int
    confidence: float
    latency_ms: float

@app.post("/predict", response_model=PredictionResponse)
async def predict(input_data: InputData):
    start = time.perf_counter()
    try:
        with torch.inference_mode():
            tensor = torch.tensor([input_data.features])
            output = model(tensor)
            probs = torch.softmax(output, dim=-1)
            confidence, pred = torch.max(probs, dim=-1)

        return PredictionResponse(
            prediction=pred.item(),
            confidence=confidence.item(),
            latency_ms=(time.perf_counter() - start) * 1000,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
```

> Do not return raw exception strings from production APIs unless they are intentionally sanitized. Avoid loading arbitrary untrusted model files.

### 3. Streaming Inference

Process data streams in real-time.

**Use Cases:**
- IoT sensor data
- Clickstream analysis
- Real-time monitoring

**Kafka Consumer Example:**
```python
from kafka import KafkaConsumer, KafkaProducer
import json

consumer = KafkaConsumer(
    "input-topic",
    bootstrap_servers=["localhost:9092"],
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)
producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)

for message in consumer:
    data = message.value
    prediction = model.predict([data["features"]])
    producer.send(
        "output-topic",
        {
            "input_id": data["id"],
            "prediction": prediction.tolist(),
        },
    )
```

---

## Containerization

### Docker Setup

**Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

> For a production image, pin dependencies and use a dedicated non-root runtime user. If `curl` is undesirable, replace the health check with a tool already present in the image or an application-level check.

**docker-compose.yml:**
```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      MODEL_PATH: /app/models/model.pt
    volumes:
      - ./models:/app/models:ro
    restart: unless-stopped

  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
```

### Building and Running

```bash
docker build -t my-model-api:latest .
docker run -p 8000:8000 -d my-model-api:latest
docker compose up -d
docker compose logs -f api
```

---

## Cloud Deployment

Cloud SDKs change frequently. Treat these snippets as provider-specific patterns, not copy-paste production code. Pin and verify the SDK/framework versions in your own environment before deployment.

### AWS SageMaker

```python
import sagemaker
from sagemaker.pytorch import PyTorchModel

pytorch_model = PyTorchModel(
    model_data="s3://bucket/model.tar.gz",
    role="arn:aws:iam::account:role/sagemaker-role",
    entry_point="inference.py",
    # Set these to versions supported by the SageMaker SDK/runtime you pin.
    framework_version="<verified-pytorch-version>",
    py_version="py3<verified-version>",
)

predictor = pytorch_model.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large",
)
```

### Google Cloud

```python
from google.cloud import aiplatform

aiplatform.init(project="my-project", location="us-central1")

# Verify the serving image and SDK API against the versions pinned by your project.
model = aiplatform.Model.upload(
    display_name="my-model",
    artifact_uri="gs://bucket/model",
    serving_container_image_uri="<verified-serving-image>",
)

endpoint = aiplatform.Endpoint.create(display_name="my-endpoint")
endpoint.deploy(
    model=model,
    deployed_model_display_name="my-model-v1",
    machine_type="n1-standard-4",
)
```

### Azure Machine Learning

Use the current Azure ML SDK/API for new deployments. The former `azureml.core`/ACI/AKS examples in older tutorials are version-sensitive and should not be copied into a new project without verification.

---

## Performance Optimization

### Model Optimization

```python
# TorchScript and ONNX APIs are version-sensitive; verify them against your
# installed PyTorch/ONNX stack before using these examples in production.
scripted_model = torch.jit.script(model)
scripted_model.save("model-scripted.pt")

dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(
    model,
    dummy_input,
    "model.onnx",
    input_names=["input"],
    output_names=["output"],
    dynamic_axes={"input": {0: "batch_size"}, "output": {0: "batch_size"}},
)
```

### Caching

```python
from functools import lru_cache
import json
import redis

@lru_cache(maxsize=1000)
def cached_predict(feature_tuple):
    features = list(feature_tuple)
    return model.predict([features])

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

def predict_with_cache(features):
    # Prefer a stable serialization over Python's process-randomized hash().
    key = "pred:" + json.dumps(features, separators=(",", ":"), sort_keys=True)
    cached = redis_client.get(key)
    if cached is not None:
        return json.loads(cached)

    result = model.predict([features])
    redis_client.setex(key, 3600, json.dumps(result.tolist()))
    return result
```

### Batching

```python
import asyncio
from collections import deque

class BatchPredictor:
    def __init__(self, model, batch_size=32, max_wait=0.1):
        self.model = model
        self.batch_size = batch_size
        self.max_wait = max_wait
        self.queue = deque()
        self.futures = deque()
        self._timer_scheduled = False
        self._lock = asyncio.Lock()

    async def predict(self, features):
        loop = asyncio.get_running_loop()
        future = loop.create_future()
        async with self._lock:
            self.queue.append(features)
            self.futures.append(future)
            if len(self.queue) >= self.batch_size:
                await self._process_batch()
            elif not self._timer_scheduled:
                self._timer_scheduled = True
                loop.call_later(
                    self.max_wait,
                    lambda: asyncio.create_task(self._flush_after_timeout()),
                )
        return await future

    async def _flush_after_timeout(self):
        async with self._lock:
            self._timer_scheduled = False
            if self.queue:
                await self._process_batch()

    async def _process_batch(self):
        if not self.queue:
            return

        batch = list(self.queue)[: self.batch_size]
        futures = list(self.futures)[: len(batch)]
        for _ in range(len(batch)):
            self.queue.popleft()
            self.futures.popleft()

        try:
            predictions = self.model.predict(batch)
            for future, pred in zip(futures, predictions):
                if not future.done():
                    future.set_result(pred)
        except Exception as exc:
            for future in futures:
                if not future.done():
                    future.set_exception(exc)
```

The example above fixes the missing `_try_process_batch` path and also propagates model errors to waiting callers instead of leaving futures unresolved.

---

## CI/CD for ML

Use pinned action versions and separate build/deploy credentials in real CI. Do not place registry or cluster credentials directly in workflow source.

```yaml
name: ML Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest tests/

  deploy:
    needs: test
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build image
        run: docker build -t registry/image:${{ github.sha }} .
      # Authenticate using GitHub Actions secrets/OIDC and push only after auth.
      - name: Push image
        run: docker push registry/image:${{ github.sha }}
      # Configure kubectl using a short-lived identity before deploying.
      - name: Deploy
        run: kubectl set image deployment/my-app my-app=registry/image:${{ github.sha }}
```

---

## Monitoring & Rollback

### Health Checks

```python
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "model_version": model_version,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

@app.get("/ready")
async def readiness_check():
    try:
        test_input = torch.randn(1, *input_shape)
        with torch.inference_mode():
            model(test_input)
        return {"status": "ready"}
    except Exception as exc:
        raise HTTPException(status_code=503, detail="Model is not ready") from exc
```

Keep liveness and readiness separate: liveness should normally answer whether the process is alive, while readiness should answer whether it can serve traffic.

### Rollback Strategy

```bash
kubectl rollout undo deployment/my-app
kubectl rollout undo deployment/my-app --to-revision=2
kubectl rollout status deployment/my-app
```

---

## Related Resources

- [Architecture Patterns](architecture_patterns.md)
- [Monitoring Guide](monitoring.md)
- [API Reference](references/api_reference.md)
- [Troubleshooting Guide](references/troubleshooting.md)
