# Deployment

## Overview

Guide to deploying machine learning models to production environments.

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
from datetime import datetime
import pandas as pd

def batch_predict():
    # Load new data
    data = load_new_data()
    
    # Predict
    predictions = model.predict(data)
    
    # Store results
    results = pd.DataFrame({
        'timestamp': datetime.now(),
        'input_id': data.id,
        'prediction': predictions
    })
    results.to_csv(f'predictions/{datetime.now():%Y%m%d}.csv')
```

### 2. Real-time API

Serve predictions via REST or gRPC API.

**Use Cases:**
- User-facing features
- Fraud detection
- Real-time recommendations

**FastAPI Example:**
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import torch

app = FastAPI()
model = torch.load('model.pt', map_location='cpu', weights_only=True)
model.eval()

class InputData(BaseModel):
    features: list[float]

class PredictionResponse(BaseModel):
    prediction: int
    confidence: float
    latency_ms: float

@app.post("/predict", response_model=PredictionResponse)
async def predict(input_data: InputData):
    import time
    start = time.time()
    
    try:
        with torch.no_grad():
            tensor = torch.tensor([input_data.features])
            output = model(tensor)
            probs = torch.softmax(output, dim=-1)
            confidence, pred = torch.max(probs, dim=-1)
        
        return PredictionResponse(
            prediction=pred.item(),
            confidence=confidence.item(),
            latency_ms=(time.time() - start) * 1000
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

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
    'input-topic',
    bootstrap_servers=['localhost:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

for message in consumer:
    data = message.value
    prediction = model.predict([data['features']])
    
    # Send to output topic
    producer.send('output-topic', {
        'input_id': data['id'],
        'prediction': prediction.tolist()
    })
```

---

## Containerization

### Docker Setup

**Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies (curl needed for healthcheck)
RUN apt-get update && apt-get install -y \
    gcc \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - MODEL_PATH=/app/models/model.pt
    volumes:
      - ./models:/app/models
    restart: unless-stopped
    
  redis:
    image: redis:alpine
    ports:
      - "6379:6379"
```

### Building and Running

```bash
# Build image
docker build -t my-model-api:latest .

# Run container
docker run -p 8000:8000 -d my-model-api:latest

# With docker-compose
docker-compose up -d

# Check logs
docker-compose logs -f api
```

---

## Cloud Deployment

### AWS SageMaker

```python
import sagemaker
from sagemaker.pytorch import PyTorchModel

# Create model
pytorch_model = PyTorchModel(
    model_data='s3://bucket/model.tar.gz',
    role='arn:aws:iam::account:role/sagemaker-role',
    entry_point='inference.py',
    framework_version='1.9.0',
    py_version='py38'
)

# Deploy
predictor = pytorch_model.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large'
)

# Invoke
response = predictor.predict({
    'instances': [[1.0, 2.0, 3.0]]
})
```

### Google Cloud AI Platform

```python
from google.cloud import aiplatform

aiplatform.init(project='my-project', location='us-central1')

# Deploy model
endpoint = aiplatform.Endpoint.create(display_name='my-endpoint')

model = aiplatform.Model.upload(
    display_name='my-model',
    artifact_uri='gs://bucket/model',
    serving_container_image_uri='gcr.io/project/my-image'
)

endpoint.deploy(
    model=model,
    deployed_model_display_name='my-model-v1',
    machine_type='n1-standard-4'
)

# Predict
response = endpoint.predict(instances=[[1.0, 2.0, 3.0]])
```

### Azure ML (SDK v2)

> **Note**: Azure ML SDK v1 (`azureml-core`) was deprecated in June 2026. Use SDK v2 (`azure-ai-ml`).

```python
from azure.ai.ml import MLClient, command
from azure.ai.ml.entities import Model, ManagedOnlineEndpoint, ManagedOnlineDeployment
from azure.identity import DefaultAzureCredential

# Connect to Azure ML workspace
credential = DefaultAzureCredential()
ml_client = MLClient(credential, subscription_id, resource_group, workspace_name)

# Register model
model = Model(
    name='my-model',
    path='./model.pt',
    type='custom_model'
)
registered_model = ml_client.models.create_or_update(model)

# Create online endpoint
endpoint = ManagedOnlineEndpoint(
    name='my-endpoint',
    auth_mode='key'
)
ml_client.begin_create_or_update(endpoint).result()

# Deploy model
deployment = ManagedOnlineDeployment(
    name='blue',
    endpoint_name=endpoint.name,
    model=registered_model,
    code_configuration={'code_directory': './scoring'},
    instance_type='Standard_DS2_v2',
    instance_count=1
)
ml_client.begin_create_or_update(deployment).result()

# Predict
response = ml_client.online_endpoints.invoke(
    endpoint_name=endpoint.name,
    request_file='sample_input.json'
)
```

---

## Performance Optimization

### Model Optimization

```python
# TorchScript compilation
scripted_model = torch.jit.script(model)
scripted_model.save('model-scripted.pt')

# ONNX export
dummy_input = torch.randn(1, 3, 224, 224)
torch.onnx.export(
    model,
    dummy_input,
    'model.onnx',
    input_names=['input'],
    output_names=['output'],
    dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}
)

# TensorRT optimization (NVIDIA GPUs)
import torch_tensorrt
trt_model = torch_tensorrt.compile(
    model,
    inputs=[torch_tensorrt.Input((1, 3, 224, 224))],
    enabled_precisions={torch.float16}
)
```

### Caching

```python
from functools import lru_cache
import redis

# In-memory cache
@lru_cache(maxsize=1000)
def cached_predict(feature_tuple):
    features = list(feature_tuple)
    return model.predict([features])

# Redis cache
redis_client = redis.Redis(host='localhost', port=6379)

def predict_with_cache(features):
    key = f"pred:{hash(tuple(features))}"
    cached = redis_client.get(key)
    
    if cached:
        return json.loads(cached)
    
    result = model.predict([features])
    redis_client.setex(key, 3600, json.dumps(result))  # Cache for 1 hour
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
        
    async def predict(self, features):
        loop = asyncio.get_running_loop()
        future = loop.create_future()
        self.queue.append(features)
        self.futures.append(future)
        
        if len(self.queue) >= self.batch_size:
            await self._process_batch()
        else:
            asyncio.call_later(self.max_wait, lambda: asyncio.ensure_future(self._process_batch()))
        
        return await future
    
    async def _process_batch(self):
        if not self.queue:
            return
            
        batch = list(self.queue)[:self.batch_size]
        futures = list(self.futures)[:len(batch)]
        
        # Remove processed items
        for _ in range(len(batch)):
            self.queue.popleft()
            self.futures.popleft()
        
        # Predict
        predictions = self.model.predict(batch)
        
        # Resolve futures
        for future, pred in zip(futures, predictions):
            future.set_result(pred)
```

---

## CI/CD for ML

### GitHub Actions

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
      
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r requirements.txt
      
      - name: Run tests
        run: pytest tests/
      
      - name: Lint
        run: flake8 .
  
  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Log in to container registry
        uses: docker/login-action@v3
        with:
          registry: ${{ secrets.REGISTRY_URL }}
          username: ${{ secrets.REGISTRY_USERNAME }}
          password: ${{ secrets.REGISTRY_PASSWORD }}
      
      - name: Build and push Docker image
        run: |
          docker build -t ${{ secrets.REGISTRY_URL }}/image:${{ github.sha }} .
          docker push ${{ secrets.REGISTRY_URL }}/image:${{ github.sha }}
      
      - name: Deploy to production
        run: |
          kubectl set image deployment/my-app my-app=${{ secrets.REGISTRY_URL }}/image:${{ github.sha }}
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
        "timestamp": datetime.now().isoformat()
    }

@app.get("/ready")
async def readiness_check():
    # Test model can make predictions
    try:
        test_input = torch.randn(1, *input_shape)
        with torch.no_grad():
            model(test_input)
        return {"status": "ready"}
    except Exception as e:
        raise HTTPException(status_code=503, detail=str(e))
```

### Rollback Strategy

```bash
# Kubernetes rollback
kubectl rollout undo deployment/my-app

# Or rollback to specific revision
kubectl rollout undo deployment/my-app --to-revision=2

# Verify rollback
kubectl rollout status deployment/my-app
```

---

## Related Resources

- [Architecture Patterns](architecture_patterns.md)
- [Monitoring Guide](monitoring.md)
- [API Reference](references/api_reference.md)
- [Troubleshooting Guide](references/troubleshooting.md)
