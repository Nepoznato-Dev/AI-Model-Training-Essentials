# Chapter 1: Infrastructure Fundamentals

## 🎯 What You'll Learn in This Chapter

By the end of this chapter, you will:
- Understand what infrastructure means for AI systems
- Know the difference between containers and virtual machines
- Build your first Docker container for an AI model
- Deploy to local Kubernetes
- Troubleshoot common infrastructure issues

**Time to complete:** 3-4 hours  
**Difficulty:** Beginner-friendly (no prior infrastructure experience needed!)

---

## Part 1: What is Infrastructure? (And Why Should You Care?)

### The Restaurant Analogy 🍽️

Imagine you're a brilliant chef (that's your AI model). You can cook amazing dishes (make predictions). But to serve customers, you need:

| Kitchen Element | AI Infrastructure Equivalent |
|-----------------|------------------------------|
| Restaurant building | Servers/Cloud |
| Waiters taking orders | APIs |
| Kitchen equipment | Compute resources (CPU/GPU) |
| Recipe storage | Model registry |
| Health inspectors | Monitoring systems |
| Backup generator | Redundancy/Failover |
| Multiple kitchen stations | Scaling/Replicas |

**Without infrastructure**, your amazing AI model is like a chef cooking in their home kitchen—great for family, but can't serve thousands of customers!

### Real-World Story: When Infrastructure Fails

**Case Study: Chatbot Black Friday Disaster**

A startup built an amazing shopping assistant chatbot. On their website launch day:

```
Day 1 (Testing): 50 users → Works perfectly! ✅
Day 2 (Soft launch): 500 users → A bit slow, but okay ⚠️
Day 3 (Black Friday): 50,000 users → CRASH! 💥
```

**What went wrong?**
- No auto-scaling (couldn't handle traffic spikes)
- No load balancing (one server got all requests)
- No monitoring (didn't know it was failing until users complained)
- No backup (single point of failure)

**Lesson:** Great models need great infrastructure!

---

## Part 2: Containers vs Virtual Machines

### The Problem: "It Works on My Machine!" 😅

Have you ever heard this?

```python
# Developer's laptop
$ python app.py
>>> Works perfectly!

# Production server
$ python app.py
>>> Error: ModuleNotFoundError: No module named 'torch'
>>> Error: CUDA version mismatch
>>> Error: Python 3.8 required, found 3.6
```

**Why does this happen?**
- Different Python versions
- Different library versions
- Different operating systems
- Missing system dependencies

### Solution 1: Virtual Machines (VMs)

**What is a VM?**
A VM is like having a complete computer inside your computer.

```
┌─────────────────────────────────────┐
│         Physical Server             │
│  ┌───────────┐  ┌───────────┐       │
│  │    VM 1   │  │    VM 2   │       │
│  │ ┌───────┐ │  │ ┌───────┐ │       │
│  │ │ Guest │ │  │ │ Guest │ │       │
│  │ │  OS   │ │  │ │  OS   │ │       │
│  │ │(Linux)│ │  │ │(Windows)│      │
│  │ └───────┘ │  │ └───────┘ │       │
│  │  App +    │  │  App +    │       │
│  │  Libs     │  │  Libs     │       │
│  └───────────┘  └───────────┘       │
│         Hypervisor                  │
└─────────────────────────────────────┘
```

**Pros:**
- Complete isolation
- Can run different operating systems
- Mature technology

**Cons:**
- **Heavy!** Each VM needs full OS (2-10 GB)
- **Slow to start** (minutes)
- **Wastes resources** (each VM runs unused OS services)

### Solution 2: Containers (Docker) 🐳

**What is a Container?**
A container shares the host OS kernel but packages your app with its dependencies.

**Pros:**
- **Lightweight!** (100-500 MB vs 2-10 GB)
- **Fast startup** (seconds vs minutes)
- **Efficient** (share OS kernel)
- **Portable** (runs same everywhere)

**Cons:**
- Less isolation than VMs (share kernel)
- All containers must use same OS kernel

### Visual Comparison

| Feature | Virtual Machine | Container |
|---------|----------------|-----------|
| Size | 2-10 GB | 100-500 MB |
| Startup Time | Minutes | Seconds |
| Performance | Good (some overhead) | Near-native |
| Isolation | Complete | Process-level |
| Best For | Different OS needs | Same OS, multiple apps |

**For AI deployment, containers win!** 🏆

---

## Part 3: Docker Deep Dive

### What is Docker?

Docker is the most popular container platform. Think of it as:
- **Shipping container** for software
- Packages your app + all dependencies
- Runs identically everywhere

### Key Docker Concepts

#### 1. Dockerfile (The Recipe)

A Dockerfile is like a recipe that tells Docker how to build your image.

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
```

#### 2. Image (The Packaged App)

An image is a snapshot of your application with all dependencies.

```bash
# Build an image from Dockerfile
docker build -t my-ai-app .

# List images
docker images
```

#### 3. Container (The Running Instance)

A container is a running instance of an image.

```bash
# Run a container
docker run -p 5000:5000 my-ai-app

# List running containers
docker ps

# Stop a container
docker stop <container_id>
```

### Hands-On: Build Your First AI Container

Let's containerize a simple text classification model!

#### Step 1: Create the Application

Create a file called `app.py`:

```python
from flask import Flask, request, jsonify
import torch
import torch.nn as nn

app = Flask(__name__)

class TextClassifier(nn.Module):
    def __init__(self, vocab_size=10000, embed_dim=128, num_classes=2):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.fc = nn.Linear(embed_dim, num_classes)
    
    def forward(self, x):
        embedded = self.embedding(x)
        pooled = embedded.mean(dim=1)
        return self.fc(pooled)

model = TextClassifier()
model.eval()

vocab = {"hello": 1, "world": 2, "good": 3, "bad": 4, "great": 5}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('text', '')
    words = text.lower().split()
    indices = [vocab.get(word, 0) for word in words]
    
    if not indices:
        return jsonify({'error': 'No valid words'}), 400
    
    input_tensor = torch.tensor([indices], dtype=torch.long)
    
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.softmax(output, dim=1)
        prediction = torch.argmax(probabilities, dim=1).item()
    
    labels = {0: 'negative', 1: 'positive'}
    
    return jsonify({
        'text': text,
        'prediction': labels[prediction],
        'confidence': probabilities[0][prediction].item()
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

#### Step 2: Create Requirements File

Create `requirements.txt`:

```txt
flask==2.3.0
torch==2.0.0
gunicorn==20.1.0
```

#### Step 3: Create Dockerfile

```dockerfile
FROM python:3.9-slim
WORKDIR /app
RUN apt-get update && apt-get install -y gcc && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
RUN adduser --disabled-password --gecos '' appuser
USER appuser
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
```

#### Step 4: Build and Run

```bash
# Build the Docker image
docker build -t text-classifier:v1 .

# Run the container
docker run -d -p 5000:5000 --name classifier text-classifier:v1

# Test it!
curl http://localhost:5000/health
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "This is great"}'
```

🎉 **Congratulations!** You just containerized your first AI model!

---

## Part 4: Docker Best Practices for AI

### 1. Multi-Stage Builds (Smaller Images)

```dockerfile
# Stage 1: Build stage
FROM python:3.9-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip wheel --no-cache-dir --wheel-dir /wheels -r requirements.txt

# Stage 2: Runtime stage (much smaller!)
FROM python:3.9-slim
WORKDIR /app
COPY --from=builder /wheels /wheels
RUN pip install --no-cache-dir /wheels/*
COPY app.py .
EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

**Result:** 5.2 GB → 1.8 GB (65% smaller!)

### 2. Layer Caching (Faster Builds)

```dockerfile
# Good: Copy requirements first for caching
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
```

### 3. Security Best Practices

```dockerfile
# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser
WORKDIR /home/appuser
COPY --chown=appuser:appuser . .
USER appuser
```

### 4. GPU Support

```dockerfile
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04
RUN apt-get update && apt-get install -y python3 python3-pip
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python3", "app.py"]
```

Run with: `docker run --gpus all -p 5000:5000 my-gpu-app`

---

## Part 5: Kubernetes Basics

### What is Kubernetes?

If Docker is a single musician, Kubernetes is the conductor of an orchestra.

### Key Kubernetes Concepts

#### 1. Pod (Smallest Unit)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: ai-model-pod
spec:
  containers:
  - name: model-container
    image: text-classifier:v1
    ports:
    - containerPort: 5000
```

#### 2. Deployment (Manages Pods)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-model-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-model
  template:
    metadata:
      labels:
        app: ai-model
    spec:
      containers:
      - name: model-container
        image: text-classifier:v1
        ports:
        - containerPort: 5000
```

#### 3. Service (Network Access)

```yaml
apiVersion: v1
kind: Service
metadata:
  name: ai-model-service
spec:
  selector:
    app: ai-model
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
  type: LoadBalancer
```

### Hands-On: Deploy to Local Kubernetes

```bash
# Install Minikube
brew install minikube  # macOS
minikube start --memory=4096 --cpus=2

# Point Docker to Minikube
eval $(minikube docker-env)

# Build image
docker build -t text-classifier:v1 .

# Apply configs
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Check status
kubectl get pods
kubectl get services

# Access your model
minikube service ai-model-service --url
```

---

## Part 6: Troubleshooting Guide

### Common Docker Errors

#### Error 1: "Cannot connect to Docker daemon"

```bash
sudo systemctl start docker
sudo usermod -aG docker $USER  # Then log out and back in
```

#### Error 2: "Port already in use"

```bash
lsof -i :5000  # Find process
kill -9 <PID>  # Kill it
# OR use different port: docker run -p 5001:5000
```

#### Error 3: "Image not found"

```bash
docker images | grep my-app
docker build -t my-app .
```

### Common Kubernetes Errors

#### Error 1: "CrashLoopBackOff"

```bash
kubectl logs <pod-name>
kubectl describe pod <pod-name>
```

#### Error 2: "ImagePullBackOff"

```bash
kubectl describe pod <pod-name>
docker pull <image-name>:<tag>
```

#### Error 3: "Pending" State

```bash
kubectl describe pod <pod-name>
kubectl top nodes
```

---

## Part 7: Glossary

| Term | Definition |
|------|------------|
| **Container** | Lightweight package with app + dependencies |
| **Docker** | Most popular container platform |
| **Dockerfile** | Instructions to build Docker image |
| **Image** | Read-only template for containers |
| **Kubernetes (K8s)** | Container orchestration platform |
| **Pod** | Smallest unit in Kubernetes |
| **Deployment** | Manages pod replicas |
| **Service** | Exposes applications |
| **kubectl** | Kubernetes command-line tool |
| **Minikube** | Local Kubernetes for development |

---

## Part 8: Exercises

### Exercise 1: Beginner - Containerize Hello World

Create a Docker container for a Flask "Hello World" app.

### Exercise 2: Intermediate - Add Health Checks

Add `/health` and `/ready` endpoints to the text classifier.

### Exercise 3: Advanced - Multi-Container Setup

Use Docker Compose to orchestrate model + Redis cache.

---

## Self-Assessment Checklist

- [ ] Explain difference between containers and VMs
- [ ] Write a basic Dockerfile
- [ ] Build and run a Docker container
- [ ] Troubleshoot common Docker errors
- [ ] Explain what Kubernetes does
- [ ] Deploy to local Kubernetes

**Ready for Chapter 2!** 🚀
