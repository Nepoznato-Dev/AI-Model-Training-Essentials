# Chapter 2: Cloud Deployment

## 🎯 What You'll Learn in This Chapter

By the end of this chapter, you will:
- Understand cloud computing fundamentals for AI workloads
- Deploy your containerized models to AWS, GCP, or Azure
- Configure auto-scaling to handle traffic spikes
- Set up load balancers for high availability
- Implement blue-green deployments for zero-downtime updates

**Time to complete:** 4-5 hours  
**Difficulty:** Intermediate (requires Chapter 1 knowledge)

---

## Part 1: Why Cloud? The Scaling Challenge

### The Problem: Growth Hurts (Without Planning) 😰

Remember our chatbot from Chapter 1? Let's see what happens when it goes viral:

```
Day 1: 100 users/day → Your laptop handles it fine ✅
Day 7: 1,000 users/day → Getting slow, but works ⚠️
Day 14: 10,000 users/day → Crashes during peak hours 💥
Day 21: 100,000 users/day → Company loses $50,000 in sales 💸
```

**What went wrong?**
- Single point of failure (your laptop)
- No automatic scaling
- No backup if hardware fails
- Limited by your machine's resources

### The Solution: Cloud Computing ☁️

Cloud providers give you:
- **Unlimited scale**: Add more servers in minutes
- **Pay-per-use**: Only pay for what you consume
- **Global reach**: Deploy close to your users worldwide
- **Built-in redundancy**: Automatic backups and failover
- **Managed services**: Focus on AI, not hardware

### Real-World Story: Startup Success with Cloud

**Case Study: ImageAI Scales to Millions**

A computer vision startup built an amazing image classifier. When featured on Product Hunt:

```
Before Cloud Launch:
- 2 servers on laptop
- Max capacity: 500 requests/minute
- Downtime during updates: 10 minutes
- Monthly cost: $0 (but limited)

After Cloud Migration:
- Auto-scales from 2 to 100 servers
- Max capacity: 50,000 requests/minute
- Zero downtime updates
- Monthly cost: $2,500 (scales with revenue)
```

**Result:** Handled 100x traffic spike without breaking! 🚀

---

## Part 2: Cloud Provider Comparison

### The Big Three: AWS vs GCP vs Azure

| Feature | AWS | Google Cloud (GCP) | Azure |
|---------|-----|-------------------|-------|
| **Market Share** | 32% (Leader) | 10% | 23% |
| **AI/ML Tools** | SageMaker | Vertex AI | Azure ML |
| **Kubernetes** | EKS | GKE (Original!) | AKS |
| **Free Tier** | 12 months, limited | $300 credit for 90 days | $200 credit for 30 days |
| **Pricing** | Complex, granular | Simple, per-second | Enterprise-friendly |
| **Best For** | Everything, mature | AI/ML, Kubernetes | Microsoft ecosystem |

### Which Should You Choose?

#### Choose AWS if:
- ✅ You want the most mature platform
- ✅ Need the widest range of services
- ✅ Building enterprise applications
- ✅ Want largest community and documentation

#### Choose GCP if:
- ✅ AI/ML is your primary focus
- ✅ Love Kubernetes (Google created it!)
- ✅ Want simpler pricing
- ✅ Need best data analytics tools

#### Choose Azure if:
- ✅ Your company uses Microsoft tools
- ✅ Need hybrid cloud (on-prem + cloud)
- ✅ Enterprise compliance required
- ✅ Already have Microsoft licenses

> 💡 **Our Recommendation**: Start with **GCP** for AI projects (best ML tools, easiest Kubernetes). But all three work great!

---

## Part 3: Setting Up Your Cloud Account

### Step 1: Create Your Account

#### Google Cloud Platform (GCP)

```bash
# 1. Go to https://cloud.google.com
# 2. Click "Get started for free"
# 3. Sign up with Google account
# 4. Add billing info (required, but won't charge without permission)
# 5. Claim $300 free credit

# Install gcloud CLI
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
gcloud init
```

#### Amazon Web Services (AWS)

```bash
# 1. Go to https://aws.amazon.com
# 2. Click "Create an AWS Account"
# 3. Enter email, password, contact info
# 4. Add payment method
# 5. Verify identity (phone call)

# Install AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws configure
```

#### Microsoft Azure

```bash
# 1. Go to https://azure.microsoft.com
# 2. Click "Start free"
# 3. Sign in with Microsoft account
# 4. Add payment verification
# 5. Claim $200 credit

# Install Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az login
```

### Step 2: Set Up Budget Alerts (CRITICAL!)

Never skip this step! Prevent surprise bills:

#### GCP Budget Setup
```bash
# Create budget alert at $50
gcloud billing budgets create \
  --billing-account=YOUR_BILLING_ACCOUNT \
  --display-name="Learning Budget" \
  --budget-amount=50USD \
  --threshold-rule=percent=50 \
  --threshold-rule=percent=90 \
  --email-recipients=your-email@example.com
```

#### AWS Budget Setup
```bash
# Using AWS Console (easier):
# 1. Go to Billing Dashboard
# 2. Click "Budgets"
# 3. Create budget: $50/month
# 4. Set alerts at 50%, 80%, 100%
# 5. Add your email
```

> ⚠️ **WARNING**: Always set budget alerts before deploying anything!

---

## Part 4: Deploying to Managed Kubernetes

### Why Managed Kubernetes?

From Chapter 1, you used Minikube (local Kubernetes). Now let's go production:

| Feature | Minikube (Local) | Managed Kubernetes (Cloud) |
|---------|------------------|---------------------------|
| **Purpose** | Development/Learning | Production |
| **Availability** | Only on your machine | 99.9%+ uptime SLA |
| **Scaling** | Limited by your hardware | Auto-scales infinitely |
| **Management** | You manage everything | Cloud manages control plane |
| **Cost** | Free | ~$70/month + node costs |

### Deploying to Google Kubernetes Engine (GKE)

#### Step 1: Enable GKE API
```bash
gcloud services enable container.googleapis.com
```

#### Step 2: Create a GKE Cluster
```bash
gcloud container clusters create ai-cluster \
  --zone us-central1-a \
  --num-nodes=3 \
  --machine-type=e2-standard-4 \
  --enable-autoscaling \
  --min-nodes=2 \
  --max-nodes=10
```

**What this creates:**
- 3 nodes to start (can scale 2-10 automatically)
- e2-standard-4 machines (4 vCPU, 16GB RAM each)
- Located in us-central1 (Iowa, USA)
- Estimated cost: ~$200/month at minimum scale

#### Step 3: Configure kubectl
```bash
gcloud container clusters get-credentials ai-cluster --zone us-central1-a
kubectl cluster-info
```

#### Step 4: Deploy Your Model
```bash
# Use the same deployment.yaml from Chapter 1
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# Check status
kubectl get pods
kubectl get services
```

#### Step 5: Get Your Public IP
```bash
kubectl get service ai-model-service

# Output:
# NAME                 TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)
# ai-model-service     LoadBalancer   10.0.0.1      35.232.100.50   80:32000/TCP

# Your model is now live at: http://35.232.100.50
curl http://35.232.100.50/predict \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"text": "This is amazing!"}'
```

### Deploying to Amazon EKS

#### Step 1: Install eksctl
```bash
# Download eksctl
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
sudo mv /tmp/eksctl /usr/local/bin
eksctl version
```

#### Step 2: Create EKS Cluster
```bash
eksctl create cluster \
  --name ai-cluster \
  --region us-east-1 \
  --nodegroup-name standard-nodes \
  --node-type t3.medium \
  --nodes 3 \
  --nodes-min 2 \
  --nodes-max 10 \
  --managed
```

#### Step 3: Deploy Your Application
```bash
# Same kubectl commands as GKE!
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### Deploying to Azure AKS

#### Step 1: Create Resource Group
```bash
az group create --name ai-resource-group --location eastus
```

#### Step 2: Create AKS Cluster
```bash
az aks create \
  --resource-group ai-resource-group \
  --name ai-cluster \
  --node-count 3 \
  --enable-managed-identity \
  --node-vm-size Standard_DS2_v2 \
  --enable-cluster-autoscaler \
  --min-count 2 \
  --max-count 10
```

#### Step 3: Connect and Deploy
```bash
az aks get-credentials --resource-group ai-resource-group --name ai-cluster
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

---

## Part 5: Auto-Scaling Configuration

### What is Auto-Scaling?

Auto-scaling automatically adds or removes resources based on demand:

```
Traffic Pattern Throughout Day:

     ▲
     │         ┌───┐
Users│    ┌────┘   └────┐
     │ ┌──┘             └──┐
     │└─┘                  └─
     └──────────────────────────► Time
       Night  Morning  Afternoon Evening

Without Auto-Scaling:
- Provision for peak (wasteful at night)
- OR under-provision (crash during peak)

With Auto-Scaling:
- Automatically adjusts to match demand
- Pay only for what you use
- Never crash from overload
```

### Horizontal Pod Autoscaler (HPA)

HPA scales the number of pod replicas based on CPU/memory usage:

```yaml
# hpa.yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ai-model-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ai-model-deployment
  minReplicas: 2          # Never go below 2
  maxReplicas: 50         # Scale up to 50 if needed
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70  # Scale when CPU > 70%
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80  # Scale when memory > 80%
```

**Apply HPA:**
```bash
kubectl apply -f hpa.yaml

# Watch it in action
kubectl get hpa --watch
```

### Cluster Autoscaler

While HPA adds more pods, Cluster Autoscaler adds more nodes:

```yaml
# Already enabled with --enable-cluster-autoscaler flag
# But you can customize:

annotations:
  cluster-autoscaler.kubernetes.io/scale-down-disabled: "false"
  cluster-autoscaler.kubernetes.io/scale-down-delay-after-add: "10m"
  cluster-autoscaler.kubernetes.io/scale-down-unneeded-time: "10m"
```

### Custom Metrics Scaling (Advanced)

Scale based on custom metrics like queue length or request latency:

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ai-model-custom-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ai-model-deployment
  minReplicas: 2
  maxReplicas: 100
  metrics:
  - type: Pods
    pods:
      metric:
        name: requests_per_second
      target:
        type: AverageValue
        averageValue: 100  # Scale to maintain 100 req/sec per pod
```

---

## Part 6: Load Balancing

### What is a Load Balancer?

A load balancer distributes incoming traffic across multiple pods:

```
                    ┌─────────────┐
                    │   Users     │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Load      │
                    │  Balancer   │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
         ┌─────────┐ ┌─────────┐ ┌─────────┐
         │  Pod 1  │ │  Pod 2  │ │  Pod 3  │
         │ (Busy)  │ │ (Idle)  │ │(Medium) │
         └─────────┘ └─────────┘ └─────────┘
         
Load Balancer sends:
- 40% traffic to Pod 1
- 30% traffic to Pod 2
- 30% traffic to Pod 3

Result: No single pod gets overwhelmed!
```

### Kubernetes Service Types

#### 1. ClusterIP (Internal Only)
```yaml
apiVersion: v1
kind: Service
metadata:
  name: internal-service
spec:
  type: ClusterIP  # Default
  selector:
    app: ai-model
  ports:
  - port: 80
    targetPort: 5000
```
**Use case:** Internal communication between services

#### 2. NodePort (Direct Node Access)
```yaml
apiVersion: v1
kind: Service
metadata:
  name: nodeport-service
spec:
  type: NodePort
  selector:
    app: ai-model
  ports:
  - port: 80
    targetPort: 5000
    nodePort: 30007  # Exposed on every node
```
**Use case:** Development/testing, not production

#### 3. LoadBalancer (Cloud Load Balancer)
```yaml
apiVersion: v1
kind: Service
metadata:
  name: ai-model-service
spec:
  type: LoadBalancer
  selector:
    app: ai-model
  ports:
  - protocol: TCP
    port: 80
    targetPort: 5000
```
**Use case:** Production internet-facing services

#### 4. Ingress (Advanced Routing)
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ai-ingress
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  rules:
  - host: api.myaiapp.com
    http:
      paths:
      - path: /predict
        pathType: Prefix
        backend:
          service:
            name: ai-model-service
            port:
              number: 80
      - path: /health
        pathType: Prefix
        backend:
          service:
            name: health-service
            port:
              number: 80
```
**Use case:** Multiple services, SSL termination, path-based routing

---

## Part 7: Blue-Green Deployments

### The Problem: Downtime During Updates

Traditional deployment:
```
1. Stop old version (v1.0) ❌ DOWNTIME STARTS
2. Deploy new version (v1.1)
3. Start new version ✅ DOWNTIME ENDS

Total downtime: 2-5 minutes
Lost revenue: $10,000 (for high-traffic app)
```

### The Solution: Blue-Green Deployment

```
Phase 1: Both Versions Running
┌─────────────┐      ┌─────────────┐
│   Blue      │      │   Green     │
│   (v1.0)    │      │   (v1.1)    │
│   ACTIVE    │      │   IDLE      │
└──────┬──────┘      └─────────────┘
       │
       ▼
   All Traffic

Phase 2: Test Green with Small Traffic
┌─────────────┐      ┌─────────────┐
│   Blue      │      │   Green     │
│   (v1.0)    │      │   (v1.1)    │
│   95%       │◄─────│   5%        │
└─────────────┘      └─────────────┘

Phase 3: Gradual Shift
┌─────────────┐      ┌─────────────┐
│   Blue      │      │   Green     │
│   (v1.0)    │      │   (v1.1)    │
│   50%       │◄─────│   50%       │
└─────────────┘      └─────────────┘

Phase 4: Complete Switch
┌─────────────┐      ┌─────────────┐
│   Blue      │      │   Green     │
│   (v1.0)    │      │   (v1.1)    │
│   IDLE      │      │   ACTIVE    │
└─────────────┘      └──────┬──────┘
                            │
                        All Traffic

Result: ZERO DOWNTIME! 🎉
```

### Implementing Blue-Green with Kubernetes

#### Step 1: Create Two Deployments
```yaml
# blue-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-model-blue
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-model
      version: blue
  template:
    metadata:
      labels:
        app: ai-model
        version: blue
    spec:
      containers:
      - name: model
        image: my-ai-app:v1.0
        ports:
        - containerPort: 5000
```

```yaml
# green-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-model-green
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-model
      version: green
  template:
    metadata:
      labels:
        app: ai-model
        version: green
    spec:
      containers:
      - name: model
        image: my-ai-app:v1.1
        ports:
        - containerPort: 5000
```

#### Step 2: Create Service with Selector
```yaml
# service.yaml
apiVersion: v1
kind: Service
metadata:
  name: ai-model-service
spec:
  type: LoadBalancer
  selector:
    app: ai-model
    version: blue  # Initially points to blue
  ports:
  - port: 80
    targetPort: 5000
```

#### Step 3: Deploy Blue First
```bash
kubectl apply -f blue-deployment.yaml
kubectl apply -f service.yaml

# Verify blue is working
kubectl get pods -l version=blue
```

#### Step 4: Deploy Green
```bash
kubectl apply -f green-deployment.yaml

# Green pods start but receive no traffic
kubectl get pods -l version=green
```

#### Step 5: Shift Traffic to Green
```bash
# Update service selector
kubectl patch service ai-model-service -p '{"spec":{"selector":{"version":"green"}}}'

# Watch traffic shift
kubectl get service ai-model-service
```

#### Step 6: Monitor and Rollback if Needed
```bash
# If something goes wrong, rollback instantly:
kubectl patch service ai-model-service -p '{"spec":{"selector":{"version":"blue"}}}'

# Once confident, delete blue deployment
kubectl delete -f blue-deployment.yaml

# Rename green to blue for next cycle
```

### Canary Deployments (Gradual Rollout)

Even safer than blue-green:

```yaml
# Using Istio for canary deployment
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: ai-model-vs
spec:
  hosts:
  - ai-model.example.com
  http:
  - route:
    - destination:
        host: ai-model-blue
        subset: v1
      weight: 90  # 90% to blue
    - destination:
        host: ai-model-green
        subset: v2
      weight: 10  # 10% to green
```

**Progressive rollout:**
```
Time    Blue    Green
T0      100%    0%
T+5min  90%     10%
T+10min 75%     25%
T+15min 50%     50%
T+20min 25%     75%
T+25min 0%      100%  ✅ Complete!
```

---

## Part 8: Cost Optimization Strategies

### Understanding Cloud Pricing

#### Compute Costs (Biggest Expense)

| Instance Type | vCPU | RAM | Price/Hour | Price/Month (730h) |
|--------------|------|-----|------------|-------------------|
| t3.small (AWS) | 2 | 2GB | $0.0208 | ~$15 |
| e2-standard-2 (GCP) | 2 | 8GB | $0.0678 | ~$49 |
| Standard_DS2_v2 (Azure) | 2 | 7GB | $0.096 | ~$70 |
| p3.2xlarge (GPU) | 8 | 61GB | $3.06 | ~$2,234 |

#### Storage Costs
- SSD: $0.10-0.17 per GB/month
- HDD: $0.04-0.06 per GB/month
- Object Storage (S3/GCS): $0.02-0.026 per GB/month

#### Network Costs
- Data transfer IN: Usually free
- Data transfer OUT: $0.09-0.12 per GB
- Cross-region: $0.02-0.10 per GB

### 10 Cost Optimization Tips

#### 1. Right-Size Your Instances
```bash
# Monitor actual usage
kubectl top nodes
kubectl top pods

# If using only 30% of CPU, downsize!
# Before: e2-standard-8 ($195/month)
# After: e2-standard-4 ($97/month)
# Savings: $98/month per node
```

#### 2. Use Spot/Preemptible Instances
```yaml
# GCP Preemptible Nodes (70% cheaper!)
gcloud container node-pools create spot-pool \
  --cluster=ai-cluster \
  --preemptible \
  --num-nodes=5 \
  --machine-type=e2-standard-4

# AWS Spot Instances
# Azure Spot VMs
```

**Warning:** Can be terminated anytime! Use for stateless workloads.

#### 3. Auto-Scaling Policies
```yaml
# Aggressive scale-down
spec:
  minReplicas: 2
  maxReplicas: 50
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300  # Wait 5 min before scaling down
      policies:
      - type: Percent
        value: 50  # Scale down 50% at a time
        periodSeconds: 60
```

#### 4. Schedule-Based Scaling
```python
# Scale based on predictable traffic patterns
import schedule

def scale_for_business_hours():
    kubectl("scale deployment ai-model --replicas=10")

def scale_for_night():
    kubectl("scale deployment ai-model --replicas=2")

schedule.every().day.at("09:00").do(scale_for_business_hours)
schedule.every().day.at("18:00").do(scale_for_night)
```

#### 5. Multi-Cloud Strategy
```
Primary Cloud (AWS): 80% traffic
Backup Cloud (GCP): 20% traffic (warm standby)

Benefits:
- Negotiate better rates
- Avoid vendor lock-in
- Better disaster recovery
```

#### 6. Use Managed Services Wisely
```
Self-Managed Kubernetes:
- Cheaper (~$200/month)
- More work (you manage everything)

Managed Kubernetes (GKE/EKS/AKS):
- More expensive (~$300/month)
- Less work (cloud manages control plane)

Decision: For production, managed is worth the extra cost!
```

#### 7. Implement Resource Quotas
```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: compute-quota
spec:
  hard:
    requests.cpu: "10"
    requests.memory: 20Gi
    limits.cpu: "20"
    limits.memory: 40Gi
    pods: "50"
```

#### 8. Clean Up Unused Resources
```bash
# Find unused load balancers
kubectl get services | grep Pending

# Delete old deployments
kubectl get deployments --sort-by=.metadata.creationTimestamp

# Remove unused container images
gcloud container images list-tags my-image
gcloud container images delete my-image:old-tag
```

#### 9. Use Commitment Discounts
```
AWS Reserved Instances: Up to 72% discount
GCP Committed Use: Up to 57% discount
Azure Reserved VMs: Up to 72% discount

Requirement: 1 or 3 year commitment
Best for: Stable, predictable workloads
```

#### 10. Monitor and Alert
```yaml
# Set up billing alerts
gcloud billing budgets create \
  --billing-account=ACCOUNT_ID \
  --display-name="Monthly Budget" \
  --budget-amount=1000USD \
  --threshold-rule=percent=50,notification_channels=EMAIL \
  --threshold-rule=percent=80,notification_channels=EMAIL,SMS \
  --threshold-rule=percent=100,notification_channels=EMAIL,SMS,PAGERDUTY
```

### Cost Monitoring Dashboard

```python
# Example: Daily cost tracking script
from google.cloud import billing_budgets_v1

def get_daily_costs():
    # Query billing API
    # Send report to Slack/Email
    pass

# Run daily
schedule.every().day.at("08:00").do(get_daily_costs)
```

---

## Part 9: Security Best Practices

### 1. Network Security

#### Private Clusters
```bash
# GCP Private Cluster
gcloud container clusters create private-cluster \
  --enable-private-nodes \
  --enable-private-endpoint \
  --master-ipv4-cidr=172.16.0.0/28 \
  --network=default \
  --subnetwork=default
```

#### Network Policies
```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-all-ingress
spec:
  podSelector: {}
  policyTypes:
  - Ingress
```

### 2. Authentication & Authorization

#### RBAC (Role-Based Access Control)
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  namespace: default
  name: pod-reader
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "watch", "list"]
```

### 3. Secrets Management
```yaml
# NEVER store secrets in code!
# Use Kubernetes Secrets:
kubectl create secret generic db-credentials \
  --from-literal=username=admin \
  --from-literal=password='super-secret'

# Use in deployment:
env:
- name: DB_PASSWORD
  valueFrom:
    secretKeyRef:
      name: db-credentials
      key: password
```

### 4. Image Security
```bash
# Scan images for vulnerabilities
gcloud artifacts docker images scan my-image:v1

# Use trusted base images
FROM python:3.9-slim  # Official, maintained
# NOT: FROM random-user/custom-image
```

---

## Part 10: Troubleshooting Guide

### Common Cloud Deployment Errors

#### Error 1: "Insufficient Quota"
```bash
# Check quota
gcloud compute regions describe us-central1

# Request quota increase
gcloud compute regions add-resource-policies
```

#### Error 2: "ImagePullBackOff"
```bash
# Check if image exists
docker pull my-registry/my-image:v1

# Ensure proper authentication
kubectl create secret docker-registry regcred \
  --docker-server=my-registry.io \
  --docker-username=user \
  --docker-password=pass

# Reference in deployment:
imagePullSecrets:
- name: regcred
```

#### Error 3: "LoadBalancer Pending"
```bash
# Check cloud provider quotas
# May take 2-5 minutes to provision
kubectl get service --watch

# If still pending after 10 minutes:
kubectl describe service ai-model-service
```

#### Error 4: "Node Not Ready"
```bash
kubectl get nodes
kubectl describe node <node-name>

# Check node logs
kubectl logs -n kube-system <system-pod>
```

### Cost Troubleshooting

#### Problem: Bill Higher Than Expected
```bash
# 1. Check Billing Dashboard
# 2. Identify top spending services
# 3. Look for orphaned resources:
kubectl get all --all-namespaces
gcloud compute addresses list  # Unattached IPs cost money!
gcloud compute disks list     # Unattached disks cost money!

# 4. Set up budget alerts immediately
```

---

## Part 11: Glossary

| Term | Definition |
|------|------------|
| **Auto-Scaling** | Automatically adjusting resources based on demand |
| **Blue-Green Deployment** | Zero-downtime deployment strategy |
| **Canary Deployment** | Gradual rollout to subset of users |
| **Cluster** | Group of nodes running Kubernetes |
| **EKS** | Elastic Kubernetes Service (AWS) |
| **GKE** | Google Kubernetes Engine |
| **HPA** | Horizontal Pod Autoscaler |
| **Ingress** | Manages external access to services |
| **Load Balancer** | Distributes traffic across multiple instances |
| **Managed Kubernetes** | Cloud provider manages control plane |
| **Node** | Worker machine running containers |
| **Pod** | Smallest deployable unit in Kubernetes |
| **RBAC** | Role-Based Access Control |
| **Service** | Abstract way to expose applications |
| **Spot Instances** | Discounted, interruptible cloud instances |

---

## Part 12: Exercises

### Exercise 1: Beginner - Deploy to Cloud
Deploy your Chapter 1 model to GKE/EKS/AKS.

**Checklist:**
- [ ] Create cloud account
- [ ] Set up budget alerts
- [ ] Create Kubernetes cluster
- [ ] Deploy your model
- [ ] Access via public IP

### Exercise 2: Intermediate - Auto-Scaling
Configure HPA for your deployment.

**Steps:**
1. Deploy HPA configuration
2. Generate load using `hey` or `ab` tool
3. Watch pods scale up
4. Stop load, watch pods scale down
5. Document scaling behavior

### Exercise 3: Advanced - Blue-Green Deployment
Implement zero-downtime deployment.

**Steps:**
1. Deploy v1.0 (blue)
2. Deploy v1.1 (green)
3. Shift traffic gradually
4. Monitor for errors
5. Rollback if needed
6. Document lessons learned

### Exercise 4: Expert - Cost Optimization
Reduce your cloud bill by 40%.

**Strategies to try:**
- Right-size instances
- Use preemptible/spot instances
- Implement aggressive auto-scaling
- Schedule-based scaling
- Clean up unused resources

---

## Self-Assessment Checklist

- [ ] Explain benefits of cloud vs on-premise
- [ ] Compare AWS, GCP, and Azure for AI workloads
- [ ] Set up cloud account with budget alerts
- [ ] Deploy to managed Kubernetes
- [ ] Configure horizontal pod autoscaler
- [ ] Set up load balancer
- [ ] Implement blue-green deployment
- [ ] Apply cost optimization strategies
- [ ] Follow security best practices
- [ ] Troubleshoot common deployment issues

**Ready for Chapter 3!** 🚀

---

*Estimated Cloud Costs for Learning:*
- *Minimum: $0 (free tier)*
- *Typical: $50-100/month*
- *Production-like: $200-500/month*

*Always set budget alerts before deploying!*
