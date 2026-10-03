# Chapter 4: Advanced Patterns

## 🎯 What You'll Learn in This Chapter

By the end of this chapter, you will:
- Deploy AI systems across multiple regions for global scale
- Implement advanced security patterns for enterprise AI
- Optimize costs at scale (50%+ savings)
- Build disaster recovery and business continuity plans
- Master advanced deployment patterns (canary, A/B testing, shadow mode)
- Understand compliance requirements (GDPR, HIPAA, SOC2)

**Time to complete:** 6-8 hours  
**Difficulty:** Advanced (requires Chapters 1-3 knowledge)

---

## Part 1: Multi-Region Deployment

### Why Multi-Region?

```
Single Region Risks:
┌─────────────────────────────────────┐
│         us-east-1 (N. Virginia)     │
│                                     │
│  ☁️ All users depend on this region │
│                                     │
│  Risk: If us-east-1 goes down...    │
│  → 100% of users affected           │
│  → $1M/hour revenue loss            │
│  → Brand damage                     │
└─────────────────────────────────────┘

Multi-Region Solution:
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  us-east-1   │  │  eu-west-1   │  │  ap-northeast│
│  (Primary)   │  │  (Backup)    │  │  (Backup)    │
│              │  │              │  │              │
│  Active      │  │  Warm        │  │  Warm        │
│  100% load   │  │  standby     │  │  standby     │
└──────────────┘  └──────────────┘  └──────────────┘
       ↓                 ↓                 ↓
   Users in US      Users in EU      Users in Asia
   
Benefits:
✓ 99.99% availability
✓ Lower latency (serve from closest region)
✓ Disaster recovery
✓ Compliance (data residency)
```

### Deployment Strategies

#### Strategy 1: Active-Passive (Warm Standby)

```
┌─────────────────┐
│   Primary       │◄── All traffic normally
│   (us-east-1)   │
│   Active        │
└────────┬────────┘
         │
         │ Failover (if primary fails)
         ▼
┌─────────────────┐
│   Secondary     │◄── Receives traffic on failure
│   (eu-west-1)   │
│   Passive       │
└─────────────────┘

Pros: Simple, cost-effective
Cons: Higher failover time (5-10 min)
Best for: Most applications
```

#### Strategy 2: Active-Active

```
┌─────────────────┐      ┌─────────────────┐
│   us-east-1     │◄────►│   eu-west-1     │
│   Active        │ Sync │   Active        │
│   50% traffic   │      │   50% traffic   │
└─────────────────┘      └─────────────────┘
       ↓                        ↓
   US Users                EU Users

Pros: Zero failover time, better resource utilization
Cons: Complex data synchronization, higher cost
Best for: Critical applications requiring zero downtime
```

#### Strategy 3: Regional Sharding

```
┌─────────────────┐
│   us-east-1     │←── US customers
│   (US data)     │
└─────────────────┘

┌─────────────────┐
│   eu-west-1     │←── EU customers (GDPR compliance)
│   (EU data)     │
└─────────────────┘

┌─────────────────┐
│   ap-southeast-1│←── APAC customers
│   (APAC data)   │
└─────────────────┘

Pros: Data residency compliance, lowest latency
Cons: Complex routing, data silos
Best for: Global enterprises with compliance needs
```

### Implementation: Multi-Region with Kubernetes

#### Step 1: Create Clusters in Multiple Regions

```bash
# GCP: Create clusters in 3 regions
gcloud container clusters create us-cluster \
  --region us-central1 \
  --num-nodes=3

gcloud container clusters create eu-cluster \
  --region europe-west1 \
  --num-nodes=2

gcloud container clusters create asia-cluster \
  --region asia-northeast1 \
  --num-nodes=2
```

#### Step 2: Set Up Global Load Balancer

```yaml
# Global ingress configuration
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: global-ingress
  annotations:
    kubernetes.io/ingress.global-static-ip-name: "ai-app-ip"
    networking.gke.io/managed-certificates: "ai-cert"
spec:
  rules:
  - host: api.myaiapp.com
    http:
      paths:
      - path: /*
        pathType: ImplementationSpecific
        backend:
          service:
            name: ai-service
            port:
              number: 80
```

#### Step 3: Configure DNS-Based Routing

```yaml
# Using Cloud DNS with geo-routing
# Route based on user location

us-central:
  target: us-cluster
  match:
    - North America

europe-west:
  target: eu-cluster
  match:
    - Europe

asia-northeast:
  target: asia-cluster
  match:
    - Asia Pacific
```

#### Step 4: Data Synchronization

```python
# Cross-region data replication
from kafka import KafkaProducer
import json

class CrossRegionReplicator:
    def __init__(self, regions):
        self.producers = {
            region: KafkaProducer(
                bootstrap_servers=f'{region}.kafka.myaiapp.com:9092',
                value_serializer=lambda v: json.dumps(v).encode('utf-8')
            )
            for region in regions
        }
    
    def replicate(self, data):
        """Replicate data to all regions"""
        for region, producer in self.producers.items():
            producer.send('model-updates', value=data)
            print(f"Replicated to {region}")
```

### Global Traffic Management

#### Using AWS Route53

```python
import boto3

route53 = boto3.client('route53')

# Create health checks
us_health_check = route53.create_health_check(
    CallerReference='us-east-1-health',
    HealthCheckConfig={
        'IPAddress': 'us-load-balancer.amazonaws.com',
        'Port': 80,
        'Type': 'HTTP',
        'ResourcePath': '/health',
        'RequestInterval': 30,
        'FailureThreshold': 3
    }
)

eu_health_check = route53.create_health_check(
    CallerReference='eu-west-1-health',
    HealthCheckConfig={
        'IPAddress': 'eu-load-balancer.amazonaws.com',
        'Port': 80,
        'Type': 'HTTP',
        'ResourcePath': '/health',
        'RequestInterval': 30,
        'FailureThreshold': 3
    }
)

# Create routing policy
route53.change_resource_record_sets(
    HostedZoneId='Z123456',
    ChangeBatch={
        'Changes': [{
            'Action': 'CREATE',
            'ResourceRecordSet': {
                'Name': 'api.myaiapp.com',
                'Type': 'A',
                'SetIdentifier': 'us-east-1',
                'GeoLocation': {'CountryCode': 'US'},
                'AliasTarget': {
                    'HostedZoneId': 'Z123456',
                    'DNSName': 'us-load-balancer.amazonaws.com',
                    'EvaluateTargetHealth': True
                }
            }
        }]
    }
)
```

---

## Part 2: Advanced Security Patterns

### Security Layers for AI Systems

```
┌─────────────────────────────────────────────────────┐
│              Security Defense in Depth               │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Layer 7: Application Security                       │
│  - Input validation                                  │
│  - Authentication/Authorization                      │
│  - Rate limiting                                     │
│                                                      │
│  Layer 6: Model Security                             │
│  - Adversarial robustness                            │
│  - Model encryption                                  │
│  - Access control                                    │
│                                                      │
│  Layer 5: Data Security                              │
│  - Encryption at rest                                │
│  - Encryption in transit                             │
│  - Data masking                                      │
│                                                      │
│  Layer 4: Network Security                           │
│  - VPC isolation                                     │
│  - Firewall rules                                    │
│  - DDoS protection                                   │
│                                                      │
│  Layer 3: Infrastructure Security                    │
│  - IAM policies                                      │
│  - Secrets management                                │
│  - Audit logging                                     │
│                                                      │
└─────────────────────────────────────────────────────┘
```

### 1. Input Validation & Sanitization

```python
from pydantic import BaseModel, validator, Field
import re

class PredictionRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=1000)
    user_id: str
    
    @validator('text')
    def validate_text(cls, v):
        # Remove potential injection attacks
        v = re.sub(r'[<>\"\'&]', '', v)
        
        # Check for malicious patterns
        if re.search(r'(script|eval|exec)', v, re.IGNORECASE):
            raise ValueError('Potentially malicious input detected')
        
        return v.strip()
    
    @validator('user_id')
    def validate_user_id(cls, v):
        if not re.match(r'^[a-zA-Z0-9_-]+$', v):
            raise ValueError('Invalid user ID format')
        return v

# Usage
try:
    request = PredictionRequest(text="Hello!", user_id="user123")
except ValidationError as e:
    logger.warning(f"Invalid input: {e}")
    raise HTTPException(status_code=400, detail=str(e))
```

### 2. Authentication & Authorization

#### OAuth2 + JWT Implementation

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt
from datetime import datetime, timedelta

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=30))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return user_id
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/predict")
async def predict(request: PredictionRequest, 
                  current_user: str = Depends(get_current_user)):
    # User is authenticated, proceed with prediction
    return model.predict(request.text)
```

### 3. Rate Limiting

```python
from slowapi import SlowApi, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

app = FastAPI()
slowapi = SlowApi(key_func=get_remote_address)
app.state.limiter = slowapi
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/predict")
@_rate_limit_exceeded_handler
@slowapi.limit("100/minute")  # 100 requests per minute per IP
async def predict(request: PredictionRequest):
    return model.predict(request.text)

# Different limits for different endpoints
@app.post("/batch-predict")
@slowapi.limit("10/minute")  # Stricter limit for batch operations
async def batch_predict(requests: List[PredictionRequest]):
    return [model.predict(r.text) for r in requests]
```

### 4. Model Encryption

```python
from cryptography.fernet import Fernet
import pickle

class EncryptedModel:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)
    
    def save_encrypted(self, model, path):
        """Save model in encrypted form"""
        model_bytes = pickle.dumps(model)
        encrypted = self.cipher.encrypt(model_bytes)
        with open(path, 'wb') as f:
            f.write(encrypted)
    
    def load_encrypted(self, path):
        """Load and decrypt model"""
        with open(path, 'rb') as f:
            encrypted = f.read()
        decrypted = self.cipher.decrypt(encrypted)
        return pickle.loads(decrypted)

# Usage
model_wrapper = EncryptedModel()
model_wrapper.save_encrypted(model, 'encrypted_model.enc')

# Later, load securely
model = model_wrapper.load_encrypted('encrypted_model.enc')
```

### 5. Secrets Management

#### Using HashiCorp Vault

```python
import hvac

client = hvac.Client(url='http://vault:8200', token='my-token')

# Read secrets
db_credentials = client.secrets.kv.v2.read_secret_version(
    path='database/creds'
)

db_username = db_credentials['data']['data']['username']
db_password = db_credentials['data']['data']['password']

# Use in application
connection_string = f"postgresql://{db_username}:{db_password}@db:5432/mydb"
```

#### Kubernetes Secrets with External Secrets Operator

```yaml
# external-secret.yaml
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: model-api-key
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: vault-backend
    kind: ClusterSecretStore
  target:
    name: model-api-key-secret
  data:
  - secretKey: api-key
    remoteRef:
      key: ai-model/credentials
      property: api-key
```

---

## Part 3: Cost Optimization at Scale

### Advanced Cost Optimization Strategies

#### 1. Spot Instance Orchestration

```python
import boto3
from botocore.exceptions import ClientError

class SpotInstanceManager:
    def __init__(self):
        self.ec2 = boto3.client('ec2')
    
    def request_spot_instances(self, instance_type, max_price, count=5):
        """Request spot instances with fallback to on-demand"""
        try:
            response = self.ec2.request_spot_instances(
                SpotPrice=max_price,
                InstanceCount=count,
                LaunchSpecification={
                    'ImageId': 'ami-12345678',
                    'InstanceType': instance_type,
                }
            )
            return response['SpotInstanceRequests']
        except ClientError as e:
            # Fallback to on-demand
            print(f"Spot request failed: {e}")
            return self.request_on_demand(instance_type, count)
    
    def request_on_demand(self, instance_type, count):
        """Fallback to on-demand instances"""
        response = self.ec2.run_instances(
            ImageId='ami-12345678',
            InstanceType=instance_type,
            MinCount=count,
            MaxCount=count,
            InstanceInitiatedShutdownBehavior='terminate'
        )
        return response['Instances']

# Usage
spot_manager = SpotInstanceManager()
instances = spot_manager.request_spot_instances(
    instance_type='p3.2xlarge',
    max_price='2.50',  # Max $2.50/hour
    count=5
)
```

#### 2. Intelligent Auto-Scaling

```python
import numpy as np
from sklearn.ensemble import RandomForestRegressor

class PredictiveScaler:
    def __init__(self):
        self.model = RandomForestRegressor()
        self.historical_data = []
    
    def train(self, timestamps, traffic, optimal_replicas):
        """Train model on historical patterns"""
        features = self.extract_features(timestamps, traffic)
        self.model.fit(features, optimal_replicas)
    
    def predict_optimal_replicas(self, future_timestamps):
        """Predict optimal replica count"""
        features = self.extract_features_from_timestamps(future_timestamps)
        predictions = self.model.predict(features)
        return np.round(predictions).astype(int)
    
    def extract_features(self, timestamps, traffic):
        """Extract time-based features"""
        features = []
        for ts, t in zip(timestamps, traffic):
            features.append([
                ts.hour,
                ts.dayofweek,
                ts.month,
                t,  # lag features
                np.mean(traffic[max(0, len(traffic)-24):])  # rolling mean
            ])
        return np.array(features)

# Usage
scaler = PredictiveScaler()
scaler.train(timestamps, traffic, optimal_replicas)

# Schedule scaling based on predictions
future_hours = pd.date_range(start='now', periods=24, freq='H')
predicted_replicas = scaler.predict_optimal_replicas(future_hours)

for hour, replicas in zip(future_hours, predicted_replicas):
    schedule.every().day.at(hour.strftime('%H:%00')).do(
        scale_deployment, replicas=replicas
    )
```

#### 3. Model Compression for Cost Savings

```python
import torch
import torch.nn as nn
from torch.quantization import quantize_dynamic

class ModelCompressor:
    def __init__(self, model):
        self.model = model
    
    def quantize(self):
        """Apply dynamic quantization (reduces model size by 4x)"""
        quantized_model = quantize_dynamic(
            self.model,
            {nn.Linear, nn.Conv2d},
            dtype=torch.qint8
        )
        return quantized_model
    
    def prune(self, amount=0.5):
        """Prune 50% of weights"""
        from torch.nn.utils import prune
        
        for module in self.model.modules():
            if isinstance(module, nn.Linear):
                prune.l1_unstructured(module, name='weight', amount=amount)
        
        return self.model
    
    def knowledge_distillation(self, teacher_model, student_model, data_loader):
        """Train small student model to mimic large teacher"""
        optimizer = torch.optim.Adam(student_model.parameters(), lr=0.001)
        criterion = nn.KLDivLoss()
        
        student_model.train()
        teacher_model.eval()
        
        for batch in data_loader:
            inputs, labels = batch
            
            # Get teacher predictions
            with torch.no_grad():
                teacher_outputs = teacher_model(inputs)
            
            # Train student
            student_outputs = student_model(inputs)
            loss = criterion(
                torch.log_softmax(student_outputs, dim=1),
                torch.softmax(teacher_outputs, dim=1)
            )
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        
        return student_model

# Usage
compressor = ModelCompressor(large_model)

# Option 1: Quantization
quantized_model = compressor.quantize()
# Size: 500MB → 125MB, Speed: 2x faster

# Option 2: Pruning
pruned_model = compressor.prune(amount=0.5)
# Size: 500MB → 250MB, Minimal accuracy loss

# Option 3: Knowledge Distillation
small_model = SmallModel()
distilled_model = compressor.knowledge_distillation(
    large_model, small_model, train_loader
)
# Size: 500MB → 50MB, 10x smaller!
```

#### 4. Multi-Cloud Cost Arbitrage

```python
class MultiCloudCostOptimizer:
    def __init__(self):
        self.providers = {
            'aws': self.get_aws_price(),
            'gcp': self.get_gcp_price(),
            'azure': self.get_azure_price()
        }
    
    def get_aws_price(self):
        # Query AWS Pricing API
        return 2.50  # $/hour for p3.2xlarge
    
    def get_gcp_price(self):
        return 2.20  # $/hour for n1-standard-8
    
    def get_azure_price(self):
        return 2.40  # $/hour for Standard_NC6
    
    def find_cheapest_provider(self, required_capacity):
        """Find cheapest provider for workload"""
        costs = {}
        for provider, price in self.providers.items():
            costs[provider] = price * required_capacity
        
        cheapest = min(costs, key=costs.get)
        return cheapest, costs[cheapest]
    
    def distribute_workload(self, total_workload):
        """Distribute workload across providers for cost optimization"""
        distribution = {}
        remaining = total_workload
        
        # Sort by price
        sorted_providers = sorted(self.providers.items(), key=lambda x: x[1])
        
        for provider, price in sorted_providers:
            # Allocate up to 50% to each provider for redundancy
            allocation = min(remaining, total_workload * 0.5)
            distribution[provider] = allocation
            remaining -= allocation
            
            if remaining <= 0:
                break
        
        return distribution

# Usage
optimizer = MultiCloudCostOptimizer()
distribution = optimizer.distribute_workload(total_workload=100)

print(f"Distribution: {distribution}")
# Output: {'gcp': 50, 'azure': 50}
# Savings: ~$300/month compared to single provider
```

---

## Part 4: Disaster Recovery & Business Continuity

### RTO and RPO Definitions

```
RTO (Recovery Time Objective):
Maximum acceptable downtime
Example: "System must be back online within 1 hour"

RPO (Recovery Point Objective):
Maximum acceptable data loss
Example: "Can lose at most 5 minutes of data"

┌──────────────────────────────────────────────┐
│                                              │
│  ◄────── RPO ──────► ◄─────── RTO ─────────►│
│                                              │
│  Last      Disaster      Recovery            │
│  Backup    Occurs        Complete            │
│     │          │             │               │
│     ▼          ▼             ▼               │
│  ─────┼──────────┼─────────────┼────────────►│
│       │          │             │             Time
│       │◄────────►│             │
│       Data Loss  │             │
│                  │             │
│                  ◄────────────►│
│                  Downtime      │
│                                              │
└──────────────────────────────────────────────┘
```

### Backup Strategies

#### 1. Model Checkpoint Backup

```python
import boto3
from datetime import datetime

class ModelBackupManager:
    def __init__(self, s3_bucket):
        self.s3 = boto3.client('s3')
        self.bucket = s3_bucket
    
    def backup_model(self, model_path, metadata=None):
        """Backup model to S3 with versioning"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        key = f"models/backups/{timestamp}/model.pth"
        
        self.s3.upload_file(model_path, self.bucket, key)
        
        # Save metadata
        if metadata:
            metadata_key = f"models/backups/{timestamp}/metadata.json"
            self.s3.put_object(
                Bucket=self.bucket,
                Key=metadata_key,
                Body=json.dumps(metadata)
            )
        
        print(f"Backup created: s3://{self.bucket}/{key}")
        return key
    
    def restore_model(self, backup_key, local_path):
        """Restore model from backup"""
        self.s3.download_file(self.bucket, backup_key, local_path)
        print(f"Model restored from: {backup_key}")
    
    def list_backups(self, prefix='models/backups/'):
        """List available backups"""
        response = self.s3.list_objects_v2(
            Bucket=self.bucket,
            Prefix=prefix
        )
        return [obj['Key'] for obj in response.get('Contents', [])]

# Usage
backup_manager = ModelBackupManager('my-model-backups')

# Automated daily backup
backup_key = backup_manager.backup_model(
    'model.pth',
    metadata={
        'version': '1.2.3',
        'accuracy': 0.95,
        'trained_on': '2026-01-15'
    }
)
```

#### 2. Database Backup with Point-in-Time Recovery

```sql
-- PostgreSQL continuous archiving
-- postgresql.conf

wal_level = replica
archive_mode = on
archive_command = 'aws s3 cp %p s3://my-bucket/wal/%f'
archive_timeout = 300  -- Force archive every 5 minutes

-- Create base backup
pg_basebackup -D /backups/base -Ft -z -P -X stream

-- Restore to specific point in time
-- recovery.conf
restore_command = 'aws s3 cp s3://my-bucket/wal/%f %p'
recovery_target_time = '2026-01-15 14:30:00'
```

### Disaster Recovery Plan

```markdown
# Disaster Recovery Runbook

## Scenario: Primary Region Failure (us-east-1)

### Immediate Actions (First 5 minutes)

1. **Detect Outage**
   ```bash
   # Check health endpoint
   curl https://us-east-1.api.myaiapp.com/health
   
   # Check CloudWatch alarms
   aws cloudwatch describe-alarms --state-value ALARM
   ```

2. **Declare Disaster**
   - Notify incident commander
   - Start war room (Zoom/Slack channel)
   - Begin incident timeline documentation

3. **Activate DR Site**
   ```bash
   # Update DNS to point to eu-west-1
   aws route53 change-resource-record-sets \
     --hosted-zone-id Z123456 \
     --change-batch file://failover-dns.json
   
   # Verify traffic shift
   kubectl config use-context eu-cluster
   kubectl get pods
   ```

### Short-term Actions (5-30 minutes)

4. **Verify Service Restoration**
   ```bash
   # Run health checks
   ./scripts/run-health-checks.sh eu-west-1
   
   # Monitor error rates
   grafana-cli dashboard get 1234
   ```

5. **Notify Stakeholders**
   - Send status update to customers
   - Update status page
   - Brief executive team

### Medium-term Actions (30 minutes - 2 hours)

6. **Assess Data Loss**
   ```sql
   -- Check last successful replication
   SELECT pg_last_wal_receive_lsn(), pg_last_wal_replay_lsn();
   
   -- Compare with RPO
   -- If data loss > RPO, initiate data recovery
   ```

7. **Scale DR Site**
   ```bash
   # Increase capacity to handle full load
   kubectl scale deployment ai-model --replicas=10
   ```

### Long-term Actions (2+ hours)

8. **Root Cause Analysis**
   - Document what happened
   - Identify root cause
   - Create action items

9. **Plan Failback**
   - Wait for primary region recovery
   - Test thoroughly
   - Schedule maintenance window
   - Execute controlled failback

10. **Post-Mortem**
    - Conduct blameless post-mortem
    - Document lessons learned
    - Update runbooks
    - Implement preventive measures
```

---

## Part 5: Advanced Deployment Patterns

### 1. Canary Deployments with Metrics-Based Rollout

```yaml
# Flagger canary deployment
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: ai-model
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ai-model
  progressDeadlineSeconds: 60
  service:
    port: 80
    targetPort: 5000
  analysis:
    interval: 1m
    threshold: 10
    maxWeight: 50
    stepWeight: 10
    metrics:
    - name: request-success-rate
      thresholdRange:
        min: 99
      interval: 1m
    - name: request-duration
      thresholdRange:
        max: 500
      interval: 1m
    webhooks:
    - name: integration-tests
      type: pre-rollout
      url: http://test-runner/tests
      timeout: 2m
```

### 2. A/B Testing Framework

```python
from enum import Enum
import hashlib

class ModelVariant(Enum):
    CONTROL = "v1.0"
    VARIANT_A = "v1.1-improved-accuracy"
    VARIANT_B = "v1.2-faster-inference"

class ABTestingRouter:
    def __init__(self):
        self.weights = {
            ModelVariant.CONTROL: 0.60,
            ModelVariant.VARIANT_A: 0.20,
            ModelVariant.VARIANT_B: 0.20
        }
    
    def get_variant(self, user_id: str) -> ModelVariant:
        """Deterministically assign variant based on user ID"""
        hash_value = int(hashlib.md5(user_id.encode()).hexdigest(), 16)
        normalized = (hash_value % 100) / 100.0
        
        cumulative = 0
        for variant, weight in self.weights.items():
            cumulative += weight
            if normalized < cumulative:
                return variant
        
        return ModelVariant.CONTROL
    
    def log_assignment(self, user_id: str, variant: ModelVariant):
        """Log assignment for analysis"""
        analytics.track(
            event='model_ab_test',
            properties={
                'user_id': user_id,
                'variant': variant.value,
                'timestamp': datetime.now().isoformat()
            }
        )

# Usage
router = ABTestingRouter()

@app.post('/predict')
async def predict(request: PredictionRequest):
    variant = router.get_variant(request.user_id)
    router.log_assignment(request.user_id, variant)
    
    # Load appropriate model
    model = load_model(variant.value)
    prediction = model.predict(request.text)
    
    return {
        'prediction': prediction,
        'variant': variant.value
    }
```

### 3. Shadow Mode Deployment

```python
import asyncio
import time

class ShadowModeDeployer:
    def __init__(self, production_model, shadow_model):
        self.prod_model = production_model
        self.shadow_model = shadow_model
        self.metrics_collector = MetricsCollector()
    
    async def predict(self, input_data):
        """Run both models, return prod result, compare silently"""
        start_time = time.time()
        
        # Production model (always used)
        prod_result = await self.prod_model.predict(input_data)
        prod_latency = time.time() - start_time
        
        # Shadow model (runs in parallel, result discarded)
        try:
            shadow_task = asyncio.create_task(
                self.shadow_model.predict(input_data)
            )
            shadow_result = await asyncio.wait_for(
                shadow_task, timeout=1.0
            )
            shadow_latency = time.time() - start_time
            
            # Compare results
            agreement = self.compare_results(prod_result, shadow_result)
            
            # Log metrics
            self.metrics_collector.record({
                'timestamp': time.time(),
                'agreement': agreement,
                'prod_latency': prod_latency,
                'shadow_latency': shadow_latency,
                'prod_result': prod_result,
                'shadow_result': shadow_result
            })
            
        except Exception as e:
            logger.error(f"Shadow model failed: {e}")
        
        return prod_result
    
    def compare_results(self, prod, shadow):
        """Compare model outputs"""
        if isinstance(prod, (int, float)) and isinstance(shadow, (int, float)):
            return abs(prod - shadow) < 0.01
        elif isinstance(prod, str) and isinstance(shadow, str):
            return prod == shadow
        else:
            return False

# Usage
deployer = ShadowModeDeployer(prod_model, new_model)

@app.post('/predict')
async def predict(request: PredictionRequest):
    result = await deployer.predict(request.text)
    return {'prediction': result}

# After monitoring for 1 week:
metrics = deployer.metrics_collector.get_summary()
if metrics['agreement_rate'] > 0.99:
    print("✅ Shadow model ready for promotion!")
    promote_to_production(new_model)
```

---

## Part 6: Compliance & Governance

### GDPR Compliance Checklist

```markdown
## GDPR Requirements for AI Systems

### 1. Right to Explanation
- [ ] Document model decision logic
- [ ] Provide human-readable explanations
- [ ] Maintain audit trails

### 2. Right to Erasure ("Right to be Forgotten")
- [ ] Implement data deletion pipeline
- [ ] Remove user data from training sets
- [ ] Delete model predictions linked to user

### 3. Data Minimization
- [ ] Collect only necessary data
- [ ] Anonymize where possible
- [ ] Regular data purging

### 4. Consent Management
- [ ] Track user consent
- [ ] Honor consent withdrawal
- [ ] Document consent timestamps

### 5. Data Portability
- [ ] Export user data in standard format
- [ ] Provide API for data access
- [ ] Complete within 30 days
```

### HIPAA Compliance for Healthcare AI

```python
class HIPAACompliantHandler:
    def __init__(self):
        self.audit_logger = AuditLogger()
        self.encryption_key = load_encryption_key()
    
    def process_phi(self, patient_data):
        """Process Protected Health Information"""
        # 1. Log access (required for audit)
        self.audit_logger.log(
            event='phi_access',
            user=current_user,
            patient_id=patient_data['id'],
            timestamp=datetime.now(),
            purpose='model_prediction'
        )
        
        # 2. Encrypt data in transit
        encrypted_data = self.encrypt(patient_data)
        
        # 3. Process with minimum necessary principle
        minimal_data = self.extract_minimum_necessary(patient_data)
        prediction = model.predict(minimal_data)
        
        # 4. Encrypt data at rest
        self.store_encrypted(prediction)
        
        # 5. Automatic logout after 15 minutes
        schedule_logout(current_user, minutes=15)
        
        return prediction
    
    def encrypt(self, data):
        """Encrypt PHI using AES-256"""
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.encryption_key), modes.CFB(iv))
        encryptor = cipher.encryptor()
        return iv + encryptor.update(json.dumps(data).encode()) + encryptor.finalize()
```

### SOC2 Type II Controls

```markdown
## SOC2 Controls for AI Infrastructure

### Security
- [ ] Access control (MFA, RBAC)
- [ ] Encryption (TLS 1.3, AES-256)
- [ ] Network segmentation
- [ ] Intrusion detection
- [ ] Regular penetration testing

### Availability
- [ ] 99.9% uptime SLA
- [ ] Disaster recovery plan
- [ ] Regular backup testing
- [ ] Capacity planning
- [ ] Incident response procedures

### Processing Integrity
- [ ] Input validation
- [ ] Error handling
- [ ] Data quality checks
- [ ] Model validation
- [ ] Output verification

### Confidentiality
- [ ] NDA agreements
- [ ] Data classification
- [ ] Access logging
- [ ] Secure disposal
- [ ] Third-party audits

### Privacy
- [ ] Privacy policy
- [ ] Consent management
- [ ] Data subject rights
- [ ] Retention policies
- [ ] Breach notification
```

---

## Part 7: Capstone Project

### Build a Production-Ready Multi-Region AI System

**Requirements:**

1. **Infrastructure**
   - Deploy to 3 regions (US, EU, Asia)
   - Global load balancing
   - Auto-scaling (2-50 replicas)
   - 99.9% uptime SLA

2. **Security**
   - OAuth2 authentication
   - Rate limiting (100 req/min)
   - Input validation
   - Encrypted model storage
   - Audit logging

3. **MLOps**
   - CI/CD pipeline
   - Model registry
   - Automated testing
   - Monitoring dashboards
   - Alerting system

4. **Cost Optimization**
   - Use spot instances (70% of capacity)
   - Model quantization
   - Predictive auto-scaling
   - Target: 40% cost reduction

5. **Disaster Recovery**
   - RTO < 1 hour
   - RPO < 5 minutes
   - Automated failover
   - Regular DR drills

6. **Compliance**
   - GDPR compliant
   - Data residency enforcement
   - User data export/deletion
   - Audit trail retention (7 years)

**Deliverables:**

1. Terraform infrastructure code
2. Kubernetes manifests
3. CI/CD pipeline configuration
4. Monitoring dashboards
5. Runbooks (deployment, DR, troubleshooting)
6. Security documentation
7. Cost analysis report

---

## Self-Assessment Checklist

- [ ] Design multi-region architecture
- [ ] Implement global load balancing
- [ ] Apply security best practices
- [ ] Optimize costs by 40%+
- [ ] Build disaster recovery plan
- [ ] Implement canary deployments
- [ ] Set up A/B testing framework
- [ ] Ensure GDPR/HIPAA compliance
- [ ] Complete capstone project

**Congratulations! You've mastered Infrastructure Layers!** 🏆

---

*You now have the skills to deploy AI systems at global scale with enterprise-grade reliability, security, and efficiency!*

*Next steps:*
- *Get certified: CKA (Kubernetes), AWS Solutions Architect*
- *Contribute to open source MLOps tools*
- *Share your knowledge with the community*
- *Build something amazing!* 🚀
