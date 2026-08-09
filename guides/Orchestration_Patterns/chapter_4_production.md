# Chapter 4: Production Systems

## 🎯 Learning Objectives

By the end of this chapter, you will:
- Evaluate and choose orchestration frameworks (Airflow, Prefect, Temporal)
- Deploy orchestration systems to cloud infrastructure
- Implement security best practices
- Design comprehensive testing strategies
- Migrate from custom implementations to frameworks
- Learn from real-world case studies

---

## 4.1 Choosing an Orchestration Framework

### When to Build vs. Buy

**Build Custom When:**
- ✅ Learning/research purposes
- ✅ Very specific requirements not met by existing tools
- ✅ Minimal dependencies needed
- ✅ Full control required

**Use Framework When:**
- ✅ Production deployment
- ✅ Need battle-tested reliability
- ✅ Team collaboration required
- ✅ Want community support and plugins

### Framework Comparison

| Feature | Apache Airflow | Prefect | Temporal | Custom Engine |
|---------|---------------|---------|----------|---------------|
| **Learning Curve** | Steep | Moderate | Moderate | Easy (initially) |
| **Scalability** | Excellent | Excellent | Excellent | Limited |
| **UI/Dashboard** | Rich | Modern | Good | None |
| **Python-Native** | Yes | Yes | SDK | Yes |
| **Dynamic Workflows** | Limited | Excellent | Excellent | Depends |
| **Retry Logic** | Basic | Advanced | Advanced | Custom |
| **State Management** | Database | Hybrid | Event Sourcing | Custom |
| **Community Size** | Large | Growing | Growing | None |
| **Cloud Managed** | Yes (MWAA, etc.) | Yes (Prefect Cloud) | Yes (Temporal Cloud) | No |

### Framework Deep Dives

#### Apache Airflow

**Best for:** Traditional ETL, data pipelines, scheduled batch jobs

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'email_on_failure': True,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'customer_onboarding',
    default_args=default_args,
    description='Onboard new customers',
    schedule_interval='@daily',
    catchup=False,
)

def validate_customer(**context):
    # Your logic here
    return {'valid': True}

def create_account(**context):
    # Your logic here
    return {'account_id': 'ACC_123'}

validate_task = PythonOperator(
    task_id='validate_customer',
    python_callable=validate_customer,
    dag=dag,
)

create_task = PythonOperator(
    task_id='create_account',
    python_callable=create_account,
    dag=dag,
)

validate_task >> create_task  # Define dependency
```

**Pros:**
- Mature ecosystem with many providers
- Rich UI for monitoring
- Strong scheduling capabilities
- Large community

**Cons:**
- Heavy resource usage
- Complex setup
- Dynamic workflows are awkward
- DAGs must be defined upfront

#### Prefect

**Best for:** Modern data stacks, dynamic workflows, hybrid cloud/on-prem

```python
from prefect import flow, task
from prefect.task_runners import ConcurrentTaskRunner

@task(retries=3, retry_delay_seconds=60)
def validate_customer(customer_id: str):
    # Your logic here
    return {'valid': True}

@task
def create_account(validation_result: dict):
    # Your logic here
    return {'account_id': 'ACC_123'}

@flow(task_runner=ConcurrentTaskRunner())
def customer_onboarding(customer_id: str):
    validation = validate_customer(customer_id)
    account = create_account(validation)
    return account

# Run locally
if __name__ == "__main__":
    customer_onboarding("CUST_123")

# Or deploy to Prefect Cloud
# prefect deploy
```

**Pros:**
- Python-native, feels natural
- Excellent dynamic workflow support
- Hybrid execution (cloud or local)
- Modern UI
- Easy to get started

**Cons:**
- Newer than Airflow (smaller ecosystem)
- Some advanced features require paid tier

#### Temporal

**Best for:** Long-running workflows, microservices orchestration, event-driven systems

```python
from temporalio import activity, workflow
from temporalio.client import Client
from temporalio.worker import Worker
from dataclasses import dataclass
from typing import List

@dataclass
class OnboardingInput:
    customer_id: str

@dataclass
class OnboardingResult:
    account_id: str
    status: str

@activity.defn
async def validate_customer(input: OnboardingInput) -> dict:
    # Your logic here (can be async!)
    return {'valid': True}

@activity.defn
async def create_account(validation: dict) -> dict:
    # Your logic here
    return {'account_id': 'ACC_123'}

@workflow.defn
class CustomerOnboardingWorkflow:
    @workflow.run
    async def run(self, input: OnboardingInput) -> OnboardingResult:
        validation = await workflow.execute_activity(
            validate_customer,
            input,
            start_to_close_timeout=timedelta(seconds=30),
            retry_policy={
                'initial_interval': timedelta(seconds=1),
                'maximum_attempts': 3,
            }
        )
        
        account = await workflow.execute_activity(
            create_account,
            validation,
            start_to_close_timeout=timedelta(seconds=60)
        )
        
        return OnboardingResult(
            account_id=account['account_id'],
            status='completed'
        )

# Start worker
async def main():
    client = await Client.connect('localhost:7233')
    
    worker = Worker(
        client,
        task_queue='onboarding-queue',
        workflows=[CustomerOnboardingWorkflow],
        activities=[validate_customer, create_account],
    )
    
    await worker.run()

# Run workflow
# result = await client.execute_workflow(...)
```

**Pros:**
- Built-in durability (event sourcing)
- Language agnostic (Go, Java, Python, TypeScript)
- Excellent for long-running workflows
- Automatic state persistence
- Powerful query capabilities

**Cons:**
- Requires separate server infrastructure
- Steeper learning curve
- More boilerplate code

### Decision Framework

**Choose Airflow if:**
- You have traditional ETL/data pipeline needs
- Your team already knows Airflow
- You need extensive scheduler features
- You want managed service options (MWAA, Cloud Composer)

**Choose Prefect if:**
- You want Python-native experience
- You need dynamic workflows
- You prefer modern tooling
- You want easy hybrid deployment

**Choose Temporal if:**
- You need long-running workflows (hours/days/weeks)
- You're orchestrating microservices
- You need language interoperability
- Durability is critical

**Stick with Custom if:**
- You're learning/experimenting
- Your needs are very simple
- You need complete control
- You can't add external dependencies

---

## 4.2 Deploying to Cloud Infrastructure

### Deployment Options

#### Option 1: Managed Services (Easiest)

**AWS Managed Workflows for Apache Airflow (MWAA)**

```yaml
# CloudFormation template snippet
Resources:
  MyMWAAEnvironment:
    Type: AWS::MWAA::Environment
    Properties:
      Name: my-airflow-env
      ExecutionRoleArn: !GetAtt AirflowExecutionRole.Arn
      DagS3Path: dags
      SourceBucketArn: !GetAtt DagBucket.Arn
      NetworkConfiguration:
        SecurityGroupIds:
          - !Ref MWaaSg
        SubnetIds:
          - !Ref PrivateSubnet1
          - !Ref PrivateSubnet2
      WebserverAccessMode: PUBLIC_ONLY
```

**Prefect Cloud**

```bash
# Deploy your flow
prefect deploy --flow customer_onboarding

# Configure work pool
prefect work-pool create my-k8s-pool --type kubernetes

# Run on your infrastructure
prefect agent start --pool my-k8s-pool
```

**Temporal Cloud**

```bash
# Create namespace
temporal operator namespace create my-namespace

# Deploy worker to your infrastructure
# Workers connect to Temporal Cloud endpoint
export TEMPORAL_ADDRESS=my-account.temporal-cloud.com:7233
export TEMPORAL_NAMESPACE=my-namespace
```

#### Option 2: Self-Hosted on Kubernetes

**Airflow on Kubernetes (Helm Chart)**

```yaml
# values.yaml
executor: "KubernetesExecutor"
webserver:
  replicas: 2
  resources:
    requests:
      cpu: 500m
      memory: 512Mi
scheduler:
  replicas: 2
  resources:
    requests:
      cpu: 1000m
      memory: 1Gi
workers:
  replicas: 5
  resources:
    requests:
      cpu: 500m
      memory: 1Gi
redis:
  enabled: true
postgresql:
  enabled: true
```

```bash
# Install
helm repo add apache-airflow https://airflow.apache.org
helm install airflow apache-airflow/airflow -f values.yaml
```

**Prefect on Kubernetes**

```yaml
# prefect-agent.yaml
apiVersion: prefect.io/v1
kind: PrefectAgent
metadata:
  name: my-agent
spec:
  apiKeySecret: prefect-api-key
  workPool: my-k8s-pool
  deploymentSpec:
    replicas: 3
    resources:
      requests:
        cpu: 250m
        memory: 256Mi
```

#### Option 3: Serverless

**AWS Lambda + Step Functions**

```python
# Lambda function
import json

def lambda_handler(event, context):
    # Your workflow step logic
    return {
        'statusCode': 200,
        'body': json.dumps({'result': 'success'})
    }
```

```yaml
# Step Functions definition (ASL)
{
  "Comment": "Customer Onboarding",
  "StartAt": "ValidateCustomer",
  "States": {
    "ValidateCustomer": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:validate",
      "Next": "CreateAccount",
      "Retry": [{
        "ErrorEquals": ["States.ALL"],
        "IntervalSeconds": 1,
        "MaxAttempts": 3
      }]
    },
    "CreateAccount": {
      "Type": "Task",
      "Resource": "arn:aws:lambda:region:account:function:create",
      "End": true
    }
  }
}
```

### Infrastructure as Code Examples

**Terraform for Airflow on AWS**

```hcl
resource "aws_mwaa_environment" "example" {
  name               = "my-airflow"
  execution_role_arn = aws_iam_role.airflow_execution.arn
  dag_s3_path        = "dags"
  source_bucket_arn  = aws_s3_bucket.dags.arn
  
  network_configuration {
    security_group_ids = [aws_security_group.mwaa.id]
    subnet_ids         = aws_subnet.private[*].id
  }
  
  webserver_access_mode = "PUBLIC_ONLY"
  
  schedulers = 2
  max_workers = 10
  
  tags = {
    Environment = "production"
  }
}
```

---

## 4.3 Security Best Practices

### Principle of Least Privilege

**Bad:** Give workers full admin access
```python
# DON'T DO THIS
os.environ["AWS_ACCESS_KEY_ID"] = "AKIAIOSFODNN7EXAMPLE"
os.environ["AWS_SECRET_ACCESS_KEY"] = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
```

**Good:** Use IAM roles with minimal permissions
```yaml
# Kubernetes service account with IAM role
apiVersion: v1
kind: ServiceAccount
metadata:
  name: workflow-worker
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789:role/workflow-role
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: workflow-role
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["get", "list"]  # Only what's needed
```

### Secrets Management

**Using HashiCorp Vault**

```python
import hvac

client = hvac.Client(
    url='https://vault.example.com',
    token=os.getenv('VAULT_TOKEN')
)

# Read secret
secret = client.secrets.kv.v2.read_secret_version(
    path='workflow/database'
)
db_password = secret['data']['data']['password']

# Don't log secrets!
# logger.info(f"Password: {db_password}")  # BAD!
logger.info("Database connection established")  # GOOD
```

**Using AWS Secrets Manager**

```python
import boto3
import json

def get_secret(secret_name):
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response['SecretString'])

# Usage
db_creds = get_secret('prod/workflow/db')
```

### Network Security

**VPC Configuration for Airflow**

```yaml
# Ensure Airflow runs in private subnets
network_configuration:
  security_group_ids:
    - sg-workflow-workers
  subnet_ids:
    - subnet-private-1
    - subnet-private-2

# Security group rules
# Inbound: Only from load balancer
# Outbound: Only to specific services (RDS, ElastiCache, etc.)
```

### Input Validation

```python
from pydantic import BaseModel, validator

class WorkflowInput(BaseModel):
    customer_id: str
    email: str
    
    @validator('customer_id')
    def validate_customer_id(cls, v):
        if not v.startswith('CUST_'):
            raise ValueError('Invalid customer ID format')
        if len(v) > 50:
            raise ValueError('Customer ID too long')
        return v
    
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v.lower()

# Usage in workflow
@task
def process_input(raw_input: dict):
    validated = WorkflowInput(**raw_input)
    # Now safe to use
    return validated
```

---

## 4.4 Testing Strategies

### Unit Testing Workflow Steps

```python
import pytest
from unittest.mock import Mock, patch

# Test a single task
def test_validate_customer_valid():
    from my_workflows.tasks import validate_customer
    
    result = validate_customer({'customer_id': 'CUST_123'})
    
    assert result['valid'] is True
    assert 'customer_id' in result

def test_validate_customer_invalid():
    from my_workflows.tasks import validate_customer
    
    with pytest.raises(ValueError):
        validate_customer({'customer_id': 'INVALID'})

# Test with mocked dependencies
@patch('my_workflows.tasks.requests.get')
def test_create_account_with_mock(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {'account_id': 'ACC_123'}
    mock_response.status_code = 200
    mock_get.return_value = mock_response
    
    from my_workflows.tasks import create_account
    
    result = create_account({'validated': True})
    
    assert result['account_id'] == 'ACC_123'
    mock_get.assert_called_once()
```

### Integration Testing Workflows

```python
import pytest
from prefect.testing.utilities import prefect_test_harness

@pytest.fixture
def prefect_client():
    with prefect_test_harness():
        yield

def test_customer_onboarding_flow(prefect_client):
    from my_workflows.flows import customer_onboarding
    
    result = customer_onboarding.fn(customer_id='CUST_TEST_123')
    
    assert result['status'] == 'completed'
    assert 'account_id' in result
```

### End-to-End Testing

```python
import pytest
from playwright.sync_api import sync_playwright

def test_workflow_via_ui():
    """Test workflow through the UI"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Login
        page.goto('http://localhost:8080/login')
        page.fill('#username', 'testuser')
        page.fill('#password', 'testpass')
        page.click('button[type="submit"]')
        
        # Trigger workflow
        page.goto('http://localhost:8080/dags/customer_onboarding/trigger')
        page.click('button#trigger')
        
        # Wait for completion
        page.wait_for_selector('.status-success', timeout=30000)
        
        # Verify results
        status = page.text_content('.workflow-status')
        assert 'Success' in status
        
        browser.close()
```

### Chaos Testing

```python
import random
import pytest
from unittest.mock import patch

def inject_random_failures():
    """Randomly fail steps to test resilience"""
    if random.random() < 0.3:  # 30% failure rate
        raise Exception("Chaos monkey!")

def test_workflow_with_chaos():
    from my_workflows.flows import customer_onboarding
    
    # Inject failures
    with patch('my_workflows.tasks.validate_customer', side_effect=inject_random_failures):
        # Should still succeed due to retries
        result = customer_onboarding.fn(customer_id='CUST_123')
        
        assert result['status'] == 'completed'
```

---

## 4.5 Migration from Custom to Framework

### Migration Strategy

**Phase 1: Parallel Run (Weeks 1-2)**
- Run custom and framework side-by-side
- Compare outputs
- Validate correctness

**Phase 2: Shadow Mode (Weeks 3-4)**
- Framework processes real traffic
- Results logged but not used
- Monitor for issues

**Phase 3: Gradual Cutover (Weeks 5-6)**
- Route 10% traffic to framework
- Increase to 50%, then 100%
- Keep custom as fallback

**Phase 4: Decommission (Week 7)**
- Remove custom implementation
- Clean up resources
- Document lessons learned

### Migration Example: Custom → Prefect

**Before (Custom)**

```python
# custom_workflow.py
class CustomWorkflow:
    def __init__(self):
        self.steps = []
    
    def add_step(self, name, func, deps=None):
        self.steps.append({
            'name': name,
            'func': func,
            'deps': deps or []
        })
    
    def run(self, context):
        results = {}
        for step in self.steps:
            # Check dependencies
            if not all(d in results for d in step['deps']):
                continue
            
            result = step['func'](context)
            results[step['name']] = result
        
        return results
```

**After (Prefect)**

```python
# prefect_workflow.py
from prefect import flow, task

@task(retries=3)
def validate_customer(customer_id: str):
    # Same logic as before
    pass

@task
def create_account(validation: dict):
    # Same logic as before
    pass

@flow
def customer_onboarding(customer_id: str):
    # Clear, declarative workflow
    validation = validate_customer(customer_id)
    account = create_account(validation)
    return account
```

**Migration Script**

```python
# migrate.py
"""
One-time script to migrate historical data
"""
from custom_engine import CustomWorkflow
from prefect_client import PrefectClient

def migrate_workflows():
    # Export from custom system
    old_workflows = export_custom_workflows()
    
    # Import to Prefect
    for wf in old_workflows:
        PrefectClient.create_flow_run(
            flow_name=wf['name'],
            parameters=wf['parameters'],
            state_history=wf['history']
        )
    
    print(f"Migrated {len(old_workflows)} workflows")

if __name__ == '__main__':
    migrate_workflows()
```

---

## 4.6 Real-World Case Studies

### Case Study 1: E-commerce Order Processing

**Company:** Major online retailer  
**Challenge:** Process 100K+ orders/hour with complex validation  
**Solution:** Temporal for durable orchestration  

**Architecture:**
```
Order Placed → Validate → Inventory Check → Payment → Ship → Notify
                 ↓           ↓              ↓         ↓       ↓
              Retry x3   Retry x2      Retry x5   Retry x3  Fire & Forget
```

**Results:**
- 99.99% order success rate
- 40% reduction in failed orders
- Automatic recovery from payment gateway outages
- Full audit trail for compliance

### Case Study 2: Data Pipeline Modernization

**Company:** Financial services firm  
**Challenge:** Migrate 500+ Airflow DAGs to modern stack  
**Solution:** Prefect 2.0 with hybrid execution  

**Approach:**
1. Automated DAG conversion tool
2. Parallel run for validation
3. Phased migration by business unit
4. Training program for data engineers

**Results:**
- 60% reduction in pipeline failures
- 3x faster development cycle
- Self-service workflow creation
- $500K/year infrastructure savings

### Case Study 3: ML Training Orchestration

**Company:** AI startup  
**Challenge:** Coordinate distributed training across 100+ GPUs  
**Solution:** Custom engine with Ray integration  

**Key Features:**
- Dynamic resource allocation
- Fault-tolerant checkpointing
- Multi-tenant isolation
- Cost optimization (spot instances)

**Results:**
- 80% GPU utilization (up from 45%)
- 50% reduction in training costs
- Zero lost training runs
- Scaled to 1000+ concurrent experiments

---

## 📚 Glossary

| Term | Definition |
|------|------------|
| **Managed Service** | Cloud provider handles infrastructure management |
| **Infrastructure as Code** | Define infrastructure in configuration files |
| **Chaos Testing** | Intentionally inject failures to test resilience |
| **Shadow Mode** | Run new system alongside old without affecting users |
| **IAM Role** | Identity and Access Management permission set |
| **VPC** | Virtual Private Cloud (isolated network) |
| **Service Account** | Identity for applications (not humans) |
| **Event Sourcing** | Store state as sequence of events |

---

## 🎓 Exercises

### Exercise 1: Deploy to Cloud

Deploy your workflow engine to a cloud platform:
- AWS MWAA, Google Cloud Composer, or Azure Airflow
- OR Prefect Cloud with local agent
- OR Temporal Cloud with self-hosted worker

Document your deployment process.

### Exercise 2: Implement Security Controls

Add to your workflow:
- Secrets management (Vault or cloud secrets manager)
- Input validation with Pydantic
- Network isolation (VPC/private subnets)
- Audit logging

### Exercise 3: Migration Project

Migrate a custom workflow to a framework:
1. Choose Airflow, Prefect, or Temporal
2. Rewrite the workflow
3. Set up parallel testing
4. Document lessons learned

---

## 🔍 Self-Assessment Checklist

- [ ] Compare and contrast major orchestration frameworks
- [ ] Choose appropriate framework for given requirements
- [ ] Deploy workflow system to cloud infrastructure
- [ ] Implement security best practices
- [ ] Write comprehensive tests (unit, integration, e2e)
- [ ] Plan and execute migration from custom to framework
- [ ] Learn from real-world case studies
- [ ] Understand trade-offs in architectural decisions

---

## 🎉 Congratulations!

You've completed the Orchestration Patterns Guide! 

You now have the skills to:
- Build workflow engines from scratch
- Apply design patterns effectively
- Scale to production workloads
- Deploy securely to cloud infrastructure
- Choose the right tools for your needs

**What's next?**
- Contribute to open-source orchestration projects
- Share your knowledge with others
- Keep learning about distributed systems
- Build something amazing!

🚀 Happy orchestrating!
