---
# Metadata
title: "DevOps & CI/CD"
description: "Practices for combining software development and IT operations to shorten the development lifecycle with continuous integration and deployment automation."
category: "DevOps Skills"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-01-15"
    author: "AI Model Training Team"
    changes: "Initial skill creation"

# Review
created: "2026-01-15"
last_modified: "2026-01-15"
review_date: "2026-07-15"
reviewed_by: "DevOps Skills Team"
next_review: "2027-01-15"

# Classification
tags: [ci-cd, continuous-integration, continuous-deployment, automation, devops]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "40 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# DevOps & CI/CD

## Overview

DevOps (Development and Operations) is a set of practices that combines software development and IT operations to shorten the development lifecycle and deliver high-quality software continuously. CI/CD (Continuous Integration/Continuous Deployment) is the core automation pipeline that enables frequent, reliable releases.

This skill covers infrastructure automation, pipeline design, deployment strategies, and operational excellence for modern software delivery.

## Core Competencies

- **CI/CD Pipeline Design**: Building automated build, test, and deployment workflows
- **Infrastructure as Code (IaC)**: Managing infrastructure through version-controlled code
- **Container Orchestration**: Deploying and managing containerized applications
- **Monitoring & Observability**: Tracking system health and performance
- **Deployment Strategies**: Implementing safe release patterns (blue-green, canary, rolling)
- **Secret Management**: Securely handling credentials and sensitive data
- **Incident Response**: Responding to and recovering from production issues
- **Cost Optimization**: Managing cloud resources efficiently

## When to Use

DevOps practices are essential when:
- ✅ Releasing software frequently (daily or multiple times per day)
- ✅ Managing complex distributed systems
- ✅ Operating cloud-native applications
- ✅ Needing rapid rollback capabilities
- ✅ Scaling infrastructure dynamically
- ✅ Ensuring compliance and audit trails
- ✅ Reducing manual deployment errors

**Not ideal for:**
- ❌ One-off projects with no maintenance needs
- ❌ Teams without operational responsibilities
- ❌ Highly regulated environments requiring manual approvals at every step (though DevOps can still help)

## The CI/CD Pipeline Flow

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│   Commit    │ →  │     Build    │ →  │    Test     │ →  │   Deploy     │ →  │   Monitor   │
│  (Push to   │    │  (Compile,   │    │  (Unit,     │    │  (Staging,   │    │  (Logs,     │
│   Git)      │    │   Package)   │    │ Integration)│    │ Production)  │    │  Metrics)   │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘    └─────────────┘
       ↓                  ↓                   ↓                  ↓                  ↓
  Trigger            Artifacts           Quality Gate        Release          Feedback Loop
```

### Pipeline Stages

| Stage | Purpose | Key Activities |
|-------|---------|----------------|
| **Source** | Code integration | Git hooks, branch policies, code review |
| **Build** | Compilation & packaging | Dependency resolution, artifact creation |
| **Test** | Quality validation | Unit, integration, security, performance tests |
| **Deploy** | Release to environments | Provisioning, configuration, rollout |
| **Monitor** | Operational visibility | Logging, metrics, alerting, tracing |

## Infrastructure as Code Tools

### Configuration Management

| Tool | Language | Best For |
|------|----------|----------|
| **Ansible** | YAML | Agentless configuration, simple setups |
| **Puppet** | DSL | Large-scale enterprise infrastructure |
| **Chef** | Ruby | Complex configuration workflows |
| **SaltStack** | Python/YAML | High-speed remote execution |

### Infrastructure Provisioning

| Tool | Strengths | Cloud Support |
|------|-----------|---------------|
| **Terraform** | Multi-cloud, state management | AWS, Azure, GCP, 100+ providers |
| **Pulumi** | General-purpose languages | Multi-cloud with TypeScript, Python, Go |
| **AWS CDK** | AWS-native, programmatic | AWS only |
| **CloudFormation** | AWS-native, mature | AWS only |

### Container Orchestration

| Platform | Use Case | Complexity |
|----------|----------|------------|
| **Kubernetes** | Production-grade orchestration | High |
| **Docker Swarm** | Simple container clustering | Low |
| **Amazon ECS** | AWS-managed containers | Medium |
| **Google Cloud Run** | Serverless containers | Low |

## Practical Templates

### GitHub Actions CI/CD Pipeline

```yaml
# .github/workflows/ci-cd.yml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run linter
        run: npm run lint
      
      - name: Check formatting
        run: npm run format:check

  test:
    runs-on: ubuntu-latest
    needs: lint
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run unit tests
        run: npm run test:unit -- --coverage
      
      - name: Upload coverage
        uses: codecov/codecov-action@v4
        with:
          file: ./coverage/lcov.info

  build:
    runs-on: ubuntu-latest
    needs: test
    permissions:
      contents: read
      packages: write
    outputs:
      image_tag: ${{ steps.meta.outputs.tags }}
    steps:
      - uses: actions/checkout@v4
      
      - name: Log in to Container Registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=ref,event=branch
            type=sha,prefix=
            type=semver,pattern={{version}}
      
      - name: Build and push Docker image
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max

  deploy-staging:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/develop'
    environment: staging
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup kubectl
        uses: azure/setup-kubectl@v3
        with:
          version: 'v1.28.0'
      
      - name: Configure kubeconfig
        run: |
          echo "${{ secrets.KUBE_CONFIG }}" | base64 -d > kubeconfig
          export KUBECONFIG=kubeconfig
      
      - name: Deploy to staging
        run: |
          kubectl set image deployment/app \
            app=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }} \
            -n staging
      
      - name: Verify deployment
        run: |
          kubectl rollout status deployment/app -n staging --timeout=300s

  deploy-production:
    runs-on: ubuntu-latest
    needs: [build, deploy-staging]
    if: github.ref == 'refs/heads/main'
    environment: production
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup kubectl
        uses: azure/setup-kubectl@v3
        with:
          version: 'v1.28.0'
      
      - name: Configure kubeconfig
        run: |
          echo "${{ secrets.KUBE_CONFIG }}" | base64 -d > kubeconfig
          export KUBECONFIG=kubeconfig
      
      - name: Deploy to production (Blue-Green)
        run: |
          # Deploy to green slot
          kubectl set image deployment/app-green \
            app=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }} \
            -n production
          
          # Wait for green to be ready
          kubectl rollout status deployment/app-green -n production --timeout=300s
          
          # Switch traffic to green
          kubectl patch service/app -n production -p '{"spec":{"selector":{"slot":"green"}}}'
          
          # Delete old blue deployment
          kubectl delete deployment/app-blue -n production || true
          
          # Rename green to blue for next deployment
          kubectl label deployment/app-green slot=blue -n production --overwrite

  notify:
    runs-on: ubuntu-latest
    needs: [deploy-production]
    if: always()
    steps:
      - name: Notify Slack
        uses: slackapi/slack-github-action@v1.24.0
        with:
          payload: |
            {
              "text": "Deployment ${{ needs.deploy-production.result }}",
              "blocks": [
                {
                  "type": "section",
                  "text": {
                    "type": "mrkdwn",
                    "text": "*Deployment Status*: ${{ needs.deploy-production.result }}\n*Commit*: ${{ github.sha }}\n*Environment*: Production"
                  }
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

### Terraform Infrastructure Template

```hcl
# main.tf
terraform {
  required_version = ">= 1.5.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "production/infrastructure.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}

provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Environment = var.environment
      ManagedBy   = "Terraform"
      Project     = var.project_name
    }
  }
}

# Variables
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Environment name"
  type        = string
}

variable "project_name" {
  description = "Project name"
  type        = string
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.medium"
}

# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "${var.project_name}-vpc"
  }
}

# Public Subnets
resource "aws_subnet" "public" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  map_public_ip_on_launch = true
  
  tags = {
    Name = "${var.project_name}-public-${count.index + 1}"
    Type = "Public"
  }
}

# Private Subnets
resource "aws_subnet" "private" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 8, count.index + 10)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  tags = {
    Name = "${var.project_name}-private-${count.index + 1}"
    Type = "Private"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  
  tags = {
    Name = "${var.project_name}-igw"
  }
}

# EKS Cluster
resource "aws_eks_cluster" "main" {
  name     = "${var.project_name}-cluster"
  role_arn = aws_iam_role.eks_cluster.arn
  version  = "1.28"
  
  vpc_config {
    subnet_ids         = aws_subnet.private[*].id
    endpoint_private_access = true
    endpoint_public_access  = false
  }
  
  enabled_cluster_log_types = ["api", "audit", "authenticator"]
  
  tags = {
    Name = "${var.project_name}-eks"
  }
}

# EKS Node Group
resource "aws_eks_node_group" "main" {
  cluster_name    = aws_eks_cluster.main.name
  node_group_name = "${var.project_name}-nodes"
  node_role_arn   = aws_iam_role.eks_nodes.arn
  subnet_ids      = aws_subnet.private[*].ids
  
  instance_types = [var.instance_type]
  
  scaling_config {
    desired_size = 3
    max_size     = 10
    min_size     = 2
  }
  
  update_config {
    max_unavailable = 1
  }
  
  depends_on = [aws_eks_cluster.main]
}

# Application Load Balancer
resource "aws_lb" "app" {
  name               = "${var.project_name}-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.alb.id]
  subnets            = aws_subnet.public[*].id
  
  enable_deletion_protection = true
  
  tags = {
    Name = "${var.project_name}-alb"
  }
}

# Outputs
output "vpc_id" {
  value = aws_vpc.main.id
}

output "eks_cluster_endpoint" {
  value = aws_eks_cluster.main.endpoint
}

output "alb_dns_name" {
  value = aws_lb.app.dns_name
}
```

### Kubernetes Deployment Manifest

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
  namespace: production
  labels:
    app: myapp
    version: v1.0.0
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
        version: v1.0.0
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
    spec:
      serviceAccountName: app-service-account
      containers:
        - name: app
          image: ghcr.io/org/myapp:v1.0.0
          imagePullPolicy: Always
          ports:
            - name: http
              containerPort: 8080
              protocol: TCP
          env:
            - name: NODE_ENV
              value: "production"
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: app-secrets
                  key: database-url
            - name: API_KEY
              valueFrom:
                secretKeyRef:
                  name: app-secrets
                  key: api-key
          resources:
            requests:
              memory: "256Mi"
              cpu: "250m"
            limits:
              memory: "512Mi"
              cpu: "500m"
          livenessProbe:
            httpGet:
              path: /health
              port: http
            initialDelaySeconds: 30
            periodSeconds: 10
            timeoutSeconds: 5
            failureThreshold: 3
          readinessProbe:
            httpGet:
              path: /ready
              port: http
            initialDelaySeconds: 5
            periodSeconds: 5
            timeoutSeconds: 3
            failureThreshold: 3
          volumeMounts:
            - name: config
              mountPath: /app/config
              readOnly: true
      volumes:
        - name: config
          configMap:
            name: app-config
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchExpressions:
                    - key: app
                      operator: In
                      values:
                        - myapp
                topologyKey: kubernetes.io/hostname
---
apiVersion: v1
kind: Service
metadata:
  name: app
  namespace: production
  labels:
    app: myapp
spec:
  type: ClusterIP
  ports:
    - port: 80
      targetPort: http
      protocol: TCP
      name: http
  selector:
    app: myapp
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app
  minReplicas: 3
  maxReplicas: 20
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
    - type: Resource
      resource:
        name: memory
        target:
          type: Utilization
          averageUtilization: 80
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 10
          periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
        - type: Percent
          value: 100
          periodSeconds: 15
        - type: Pods
          value: 4
          periodSeconds: 15
      selectPolicy: Max
```

## Common Pitfalls

### 🚫 Anti-Patterns to Avoid

1. **Manual Steps in Pipeline**
   ```yaml
   # ❌ Bad: Manual intervention required
   - name: Deploy manually
     run: echo "Please deploy manually"
   
   # ✅ Good: Fully automated
   - name: Deploy automatically
     run: ./deploy.sh
   ```

2. **Hard-Coded Secrets**
   ```yaml
   # ❌ Bad: Secrets in code
   env:
     DATABASE_PASSWORD: "supersecret123"
   
   # ✅ Good: Using secrets management
   env:
     DATABASE_PASSWORD: ${{ secrets.DB_PASSWORD }}
   ```

3. **No Rollback Strategy**
   ```yaml
   # ❌ Bad: Deploy without rollback plan
   - name: Deploy
     run: kubectl apply -f deployment.yaml
   
   # ✅ Good: Deploy with rollback capability
   - name: Deploy with rollback
     run: |
       kubectl rollout status deployment/app --timeout=300s || \
       kubectl rollout undo deployment/app
   ```

4. **Testing Only in Production**
   ```yaml
   # ❌ Bad: No staging environment
   jobs:
     deploy:
       - name: Deploy to production
         run: ./deploy-prod.sh
   
   # ✅ Good: Multi-environment pipeline
   jobs:
     deploy-staging:
       - name: Deploy to staging
         run: ./deploy-staging.sh
     deploy-production:
       needs: deploy-staging
       - name: Deploy to production
         run: ./deploy-prod.sh
   ```

5. **Ignoring Pipeline Performance**
   ```yaml
   # ❌ Bad: Sequential slow jobs
   jobs:
     lint:
       runs-on: ubuntu-latest
     test:
       needs: lint
       runs-on: ubuntu-latest
     build:
       needs: test
       runs-on: ubuntu-latest
   
   # ✅ Good: Parallel where possible
   jobs:
     lint:
       runs-on: ubuntu-latest
     test:
       runs-on: ubuntu-latest
     build:
       needs: [lint, test]
       runs-on: ubuntu-latest
   ```

6. **No Monitoring or Alerting**
   ```yaml
   # ❌ Bad: Deploy and forget
   - name: Deploy
     run: ./deploy.sh
   
   # ✅ Good: Deploy with verification
   - name: Deploy
     run: ./deploy.sh
   - name: Verify health
     run: ./verify-health.sh
   - name: Notify on failure
     if: failure()
     run: ./notify-team.sh
   ```

## Best Practices

### ✅ Recommended Approaches

1. **Everything as Code**
   - Infrastructure as Code (IaC)
   - Configuration as Code
   - Policy as Code
   - Documentation as Code

2. **Immutable Infrastructure**
   - Never modify running instances
   - Replace instead of update
   - Version all artifacts
   - Use golden images

3. **Progressive Delivery**
   - Start with canary deployments
   - Gradually increase traffic
   - Monitor metrics closely
   - Automate rollback on failures

4. **Security First**
   - Scan containers for vulnerabilities
   - Use least privilege principles
   - Rotate secrets regularly
   - Audit all access

5. **Observability**
   - Implement structured logging
   - Collect meaningful metrics
   - Set up distributed tracing
   - Create actionable alerts

6. **Disaster Recovery**
   - Regular backup testing
   - Document recovery procedures
   - Practice failover scenarios
   - Maintain runbooks

7. **Cost Optimization**
   - Right-size resources
   - Use spot instances where appropriate
   - Implement auto-scaling
   - Monitor and alert on costs

8. **Documentation**
   - Maintain up-to-date runbooks
   - Document architecture decisions
   - Keep incident post-mortems
   - Version control everything

## Tools & Resources

### CI/CD Platforms

| Platform | Type | Best For |
|----------|------|----------|
| **GitHub Actions** | Cloud/Self-hosted | GitHub repositories |
| **GitLab CI** | Cloud/Self-hosted | GitLab users |
| **Jenkins** | Self-hosted | Custom workflows |
| **CircleCI** | Cloud | Fast builds |
| **Azure DevOps** | Cloud | Microsoft ecosystem |
| **ArgoCD** | Kubernetes | GitOps deployments |

### Infrastructure Tools

| Category | Tools |
|----------|-------|
| **IaC** | Terraform, Pulumi, CloudFormation |
| **Configuration** | Ansible, Puppet, Chef |
| **Containers** | Docker, Podman, containerd |
| **Orchestration** | Kubernetes, Nomad, ECS |
| **Service Mesh** | Istio, Linkerd, Consul |

### Monitoring & Observability

| Purpose | Tools |
|---------|-------|
| **Metrics** | Prometheus, Datadog, New Relic |
| **Logging** | ELK Stack, Loki, Splunk |
| **Tracing** | Jaeger, Zipkin, Honeycomb |
| **Alerting** | PagerDuty, Opsgenie, Alertmanager |
| **Dashboards** | Grafana, Kibana |

### Security Tools

| Category | Tools |
|----------|-------|
| **Secret Management** | HashiCorp Vault, AWS Secrets Manager |
| **Container Scanning** | Trivy, Snyk, Clair |
| **Policy Enforcement** | OPA, Kyverno |
| **Network Security** | Calico, Cilium |

### Learning Resources

- 📚 ["The Phoenix Project" by Gene Kim](https://itrevolution.com/book/the-phoenix-project/)
- 📚 ["Site Reliability Engineering" by Google](https://sre.google/books/)
- 📚 ["Accelerate" by Nicole Forsgren](https://www.amazon.com/Accelerate-Software-Performing-Technology-Organizations/dp/1942788339)
- 🎥 [Kelsey Hightower's Kubernetes Tutorials](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- 📖 [DevOps Roadmap](https://roadmap.sh/devops)
- 🏛️ [CNCF Landscape](https://landscape.cncf.io/)

## Examples

### Example 1: Blue-Green Deployment

```bash
#!/bin/bash
# blue-green-deploy.sh

NAMESPACE="production"
DEPLOYMENT_NAME="app"
NEW_VERSION=$1
CURRENT_SLOT=$(kubectl get svc $DEPLOYMENT_NAME -n $NAMESPACE -o jsonpath='{.spec.selector.slot}')
NEW_SLOT=$([ "$CURRENT_SLOT" == "blue" ] && echo "green" || echo "blue")

echo "Current slot: $CURRENT_SLOT"
echo "Deploying to: $NEW_SLOT"

# Deploy new version to inactive slot
kubectl set image deployment/$DEPLOYMENT_NAME-$NEW_SLOT \
  app=registry.example.com/app:$NEW_VERSION \
  -n $NAMESPACE

# Wait for rollout
kubectl rollout status deployment/$DEPLOYMENT_NAME-$NEW_SLOT -n $NAMESPACE --timeout=300s

if [ $? -eq 0 ]; then
  # Switch traffic
  kubectl patch svc $DEPLOYMENT_NAME -n $NAMESPACE \
    -p "{\"spec\":{\"selector\":{\"slot\":\"$NEW_SLOT\"}}}"
  
  echo "Traffic switched to $NEW_SLOT"
  
  # Delete old deployment
  kubectl delete deployment/$DEPLOYMENT_NAME-$CURRENT_SLOT -n $NAMESPACE || true
  
  # Rename new deployment for next cycle
  kubectl label deployment/$DEPLOYMENT_NAME-$NEW_SLOT slot=$CURRENT_SLOT -n $NAMESPACE --overwrite
else
  echo "Deployment failed, rolling back"
  kubectl rollout undo deployment/$DEPLOYMENT_NAME-$NEW_SLOT -n $NAMESPACE
  exit 1
fi
```

### Example 2: Canary Deployment with Istio

```yaml
# canary-release.yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: app-canary
  namespace: production
spec:
  hosts:
    - app.example.com
  http:
    - route:
        - destination:
            host: app-blue
            port:
              number: 80
            subset: stable
          weight: 90
        - destination:
            host: app-green
            port:
              number: 80
            subset: canary
          weight: 10
---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: app-destination
  namespace: production
spec:
  host: app
  subsets:
    - name: stable
      labels:
        version: stable
    - name: canary
      labels:
        version: canary
```

### Example 3: Automated Rollback Script

```python
#!/usr/bin/env python3
# auto-rollback.py

import subprocess
import sys
import time

def check_health(endpoint):
    """Check if the application is healthy"""
    try:
        result = subprocess.run(
            ['curl', '-sf', endpoint],
            capture_output=True,
            timeout=10
        )
        return result.returncode == 0
    except subprocess.TimeoutExpired:
        return False

def get_previous_version(namespace, deployment):
    """Get the previous deployment revision"""
    result = subprocess.run(
        ['kubectl', 'rollout', 'history', f'deployment/{deployment}', 
         '-n', namespace],
        capture_output=True,
        text=True
    )
    
    lines = result.stdout.strip().split('\n')
    if len(lines) >= 3:
        # Parse the second-to-last revision
        parts = lines[1].strip().split()
        return parts[0].split(':')[1]
    
    return None

def rollback(namespace, deployment):
    """Perform rollback to previous version"""
    print(f"Rolling back {deployment} in {namespace}...")
    
    result = subprocess.run(
        ['kubectl', 'rollout', 'undo', f'deployment/{deployment}', 
         '-n', namespace],
        capture_output=True,
        text=True
    )
    
    if result.returncode == 0:
        print("Rollback initiated successfully")
        
        # Wait for rollback to complete
        wait_result = subprocess.run(
            ['kubectl', 'rollout', 'status', f'deployment/{deployment}',
             '-n', namespace, '--timeout=300s'],
            capture_output=True,
            text=True
        )
        
        return wait_result.returncode == 0
    
    print(f"Rollback failed: {result.stderr}")
    return False

def main():
    namespace = sys.argv[1] if len(sys.argv) > 1 else 'production'
    deployment = sys.argv[2] if len(sys.argv) > 2 else 'app'
    health_endpoint = sys.argv[3] if len(sys.argv) > 3 else 'http://localhost:8080/health'
    
    max_retries = 3
    retry_interval = 30  # seconds
    
    for attempt in range(max_retries):
        print(f"Health check attempt {attempt + 1}/{max_retries}")
        
        if check_health(health_endpoint):
            print("Application is healthy!")
            sys.exit(0)
        
        print(f"Health check failed, waiting {retry_interval}s...")
        time.sleep(retry_interval)
    
    print("All health checks failed, initiating rollback...")
    
    if rollback(namespace, deployment):
        print("Rollback completed successfully")
        sys.exit(0)
    else:
        print("Rollback failed, manual intervention required!")
        sys.exit(1)

if __name__ == '__main__':
    main()
```

## Success Indicators

You've mastered DevOps & CI/CD when you can:

- ✅ Design and implement end-to-end CI/CD pipelines
- ✅ Manage infrastructure entirely through code
- ✅ Deploy applications with zero downtime
- ✅ Implement effective monitoring and alerting
- ✅ Respond to incidents quickly and effectively
- ✅ Optimize cloud costs without sacrificing performance
- ✅ Maintain high availability (>99.9% uptime)
- ✅ Enable frequent deployments (multiple times per day)
- ✅ Reduce mean time to recovery (MTTR) to minutes
- ✅ Mentor teams on DevOps best practices

## Related Skills

- [Test Automation](../testing-skills/test_automation.md) - Automated testing in pipelines
- [System Architecture](../designing-skills/system_architecture.md) - Designing for deployability
- [Planning](../behavior-skills/planning.md) - Planning releases and rollouts
- [Code Review](../collaboration-skills/code_review.md) - Reviewing infrastructure code

## Version Information

---
version: 1.0.0
last_updated: 2026-01-15
reviewed_by: DevOps Skills Team
next_review: 2026-07-15
---
