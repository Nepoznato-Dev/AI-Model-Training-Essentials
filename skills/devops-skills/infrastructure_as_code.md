# Infrastructure as Code

## Overview

Infrastructure as Code (IaC) is the practice of managing and provisioning infrastructure through machine-readable definition files, rather than physical hardware configuration or interactive configuration tools. IaC enables version control, automation, consistency, and repeatability in infrastructure management.

This skill covers declarative and imperative approaches to infrastructure automation, state management, and best practices for treating infrastructure with the same rigor as application code.

## Core Competencies

- **Declarative vs Imperative**: Understanding when to use each approach
- **State Management**: Tracking infrastructure state and handling drift
- **Module Development**: Creating reusable infrastructure components
- **Secret Management**: Securely handling credentials in IaC workflows
- **Policy as Code**: Enforcing compliance and governance rules
- **Testing Infrastructure**: Validating infrastructure before deployment
- **Multi-Environment Management**: Handling dev, staging, production configurations
- **Cost Estimation**: Predicting infrastructure costs from code

## When to Use

IaC is essential when:
- ✅ Managing complex, multi-resource infrastructure
- ✅ Needing reproducible environments (dev, staging, production)
- ✅ Requiring audit trails for infrastructure changes
- ✅ Implementing disaster recovery strategies
- ✅ Scaling infrastructure dynamically
- ✅ Enforcing security and compliance policies
- ✅ Collaborating on infrastructure changes

**Not ideal for:**
- ❌ One-time experimental setups
- ❌ Environments requiring frequent manual intervention
- ❌ Legacy systems without API support

## IaC Approaches

### Declarative Approach

Define the desired end state; the tool determines how to achieve it.

```hcl
# Terraform example
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.medium"
  
  tags = {
    Name = "web-server"
  }
}
```

**Pros:**
- Simpler to understand desired state
- Tool handles dependency ordering
- Easier to reason about final configuration

**Cons:**
- Less control over execution order
- May not support complex logic
- Debugging can be challenging

### Imperative Approach

Define step-by-step instructions to reach the desired state.

```yaml
# Ansible playbook example
- name: Configure web server
  hosts: webservers
  tasks:
    - name: Install nginx
      apt:
        name: nginx
        state: present
    
    - name: Start nginx service
      service:
        name: nginx
        state: started
        enabled: true
```

**Pros:**
- Full control over execution flow
- Better for complex procedural logic
- Easier debugging of individual steps

**Cons:**
- More verbose
- Must manage dependencies manually
- Harder to determine final state

## IaC Tools Comparison

| Tool | Language | Type | Best For | State Management |
|------|----------|------|----------|------------------|
| **Terraform** | HCL | Declarative | Multi-cloud provisioning | Remote state (S3, Azure Blob, etc.) |
| **Pulumi** | TypeScript, Python, Go | Declarative | Developers wanting general-purpose languages | Cloud-managed state |
| **AWS CDK** | TypeScript, Python, Java | Imperative | AWS-native infrastructure | CloudFormation stacks |
| **CloudFormation** | YAML/JSON | Declarative | AWS-only environments | Stack-based |
| **Ansible** | YAML | Imperative | Configuration management | Agentless, no state file |
| **Chef** | Ruby | Imperative | Complex configuration workflows | Chef Server |
| **Puppet** | DSL | Declarative | Large enterprise infrastructure | PuppetDB |

## Practical Templates

### Terraform Module Structure

```
modules/
├── vpc/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── versions.tf
├── eks/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── versions.tf
└── rds/
    ├── main.tf
    ├── variables.tf
    ├── outputs.tf
    └── versions.tf

environments/
├── dev/
│   └── main.tf
├── staging/
│   └── main.tf
└── production/
    └── main.tf
```

### Terraform Module Template

```hcl
# modules/vpc/main.tf
terraform {
  required_version = ">= 1.5.0"
  
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Variables
variable "environment" {
  description = "Environment name (dev, staging, production)"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "enable_nat_gateway" {
  description = "Whether to create NAT gateways"
  type        = bool
  default     = true
}

variable "tags" {
  description = "Additional tags to apply"
  type        = map(string)
  default     = {}
}

# VPC Resource
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = merge(var.tags, {
    Name        = "${var.environment}-vpc"
    Environment = var.environment
    ManagedBy   = "Terraform"
  })
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  
  tags = merge(var.tags, {
    Name = "${var.environment}-igw"
  })
}

# Public Subnets
resource "aws_subnet" "public" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  map_public_ip_on_launch = true
  
  tags = merge(var.tags, {
    Name = "${var.environment}-public-${count.index + 1}"
    Type = "Public"
  })
}

# Private Subnets
resource "aws_subnet" "private" {
  count             = 2
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(var.vpc_cidr, 8, count.index + 10)
  availability_zone = data.aws_availability_zones.available.names[count.index]
  
  tags = merge(var.tags, {
    Name = "${var.environment}-private-${count.index + 1}"
    Type = "Private"
  })
}

# Route Table for Public Subnets
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
  
  tags = merge(var.tags, {
    Name = "${var.environment}-public-rt"
  })
}

# Outputs
output "vpc_id" {
  description = "The ID of the VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "List of public subnet IDs"
  value       = aws_subnet.public[*].id
}

output "private_subnet_ids" {
  description = "List of private subnet IDs"
  value       = aws_subnet.private[*].id
}

output "vpc_cidr" {
  description = "The CIDR block of the VPC"
  value       = aws_vpc.main.cidr_block
}
```

### Pulumi Infrastructure Template

```typescript
// index.ts
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const config = new pulumi.Config();
const environment = config.get("environment") || "dev";
const instanceType = config.get("instanceType") || "t3.medium";

// Create a VPC
const vpc = new aws.ec2.Vpc(`${environment}-vpc`, {
    cidrBlock: "10.0.0.0/16",
    enableDnsHostnames: true,
    enableDnsSupport: true,
    tags: {
        Name: `${environment}-vpc`,
        Environment: environment,
        ManagedBy: "Pulumi"
    }
});

// Create an Internet Gateway
const igw = new aws.ec2.InternetGateway(`${environment}-igw`, {
    vpcId: vpc.id,
    tags: {
        Name: `${environment}-igw`
    }
});

// Create public subnet
const publicSubnet = new aws.ec2.Subnet(`${environment}-public`, {
    vpcId: vpc.id,
    cidrBlock: "10.0.1.0/24",
    availabilityZone: "us-east-1a",
    mapPublicIpOnLaunch: true,
    tags: {
        Name: `${environment}-public-subnet`
    }
});

// Create route table
const routeTable = new aws.ec2.RouteTable(`${environment}-rt`, {
    vpcId: vpc.id,
    routes: [{
        cidrBlock: "0.0.0.0/0",
        gatewayId: igw.id
    }],
    tags: {
        Name: `${environment}-route-table`
    }
});

// Associate route table with subnet
const routeTableAssociation = new aws.ec2.RouteTableAssociation(`${environment}-rt-assoc`, {
    subnetId: publicSubnet.id,
    routeTableId: routeTable.id
});

// Create security group
const sg = new aws.ec2.SecurityGroup(`${environment}-sg`, {
    vpcId: vpc.id,
    description: "Allow HTTP and SSH access",
    ingress: [
        {
            protocol: "tcp",
            fromPort: 80,
            toPort: 80,
            cidrBlocks: ["0.0.0.0/0"]
        },
        {
            protocol: "tcp",
            fromPort: 22,
            toPort: 22,
            cidrBlocks: ["10.0.0.0/16"]
        }
    ],
    egress: [{
        protocol: "-1",
        fromPort: 0,
        toPort: 0,
        cidrBlocks: ["0.0.0.0/0"]
    }],
    tags: {
        Name: `${environment}-security-group`
    }
});

// Launch EC2 instance
const instance = new aws.ec2.Instance(`${environment}-web`, {
    instanceType: instanceType,
    subnetId: publicSubnet.id,
    vpcSecurityGroupIds: [sg.id],
    ami: "ami-0c55b159cbfafe1f0",
    tags: {
        Name: `${environment}-web-server`,
        Environment: environment
    },
    userData: `#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello from ${environment}</h1>" > /var/www/html/index.html`
});

// Export outputs
export const vpcId = vpc.id;
export const instanceId = instance.id;
export const publicIp = instance.publicIp;
export const publicDns = instance.publicDns;
```

### Ansible Playbook Template

```yaml
# playbooks/webserver.yml
---
- name: Configure Web Servers
  hosts: webservers
  become: true
  vars:
    nginx_packages:
      - nginx
      - nginx-common
    nginx_service_state: started
    nginx_service_enabled: true
    firewall_allowed_tcp_ports:
      - 80
      - 443
  
  pre_tasks:
    - name: Update apt cache
      apt:
        update_cache: yes
        cache_valid_time: 3600
      when: ansible_os_family == "Debian"
  
  tasks:
    - name: Install nginx
      apt:
        name: "{{ nginx_packages }}"
        state: present
      notify: restart nginx
    
    - name: Start nginx service
      service:
        name: nginx
        state: "{{ nginx_service_state }}"
        enabled: "{{ nginx_service_enabled }}"
    
    - name: Configure firewall
      ufw:
        rule: allow
        port: "{{ item }}"
        proto: tcp
      loop: "{{ firewall_allowed_tcp_ports }}"
    
    - name: Deploy website content
      template:
        src: templates/index.html.j2
        dest: /var/www/html/index.html
        owner: www-data
        group: www-data
        mode: '0644'
    
    - name: Create custom nginx config
      template:
        src: templates/nginx.conf.j2
        dest: /etc/nginx/sites-available/default
        owner: root
        group: root
        mode: '0644'
      notify: restart nginx
  
  handlers:
    - name: restart nginx
      service:
        name: nginx
        state: restarted

# inventory/hosts.ini
[webservers]
web1.example.com ansible_user=ubuntu
web2.example.com ansible_user=ubuntu

[webservers:vars]
ansible_python_interpreter=/usr/bin/python3
```

### Policy as Code with Open Policy Agent (OPA)

```rego
# policies/terraform.rego
package terraform

# Deny creation of unencrypted S3 buckets
deny[msg] {
    input.resource_type == "aws_s3_bucket"
    not input.values.server_side_encryption_configuration
    msg := sprintf("S3 bucket '%s' must have encryption enabled", [input.name])
}

# Require all EC2 instances to use approved AMIs
deny[msg] {
    input.resource_type == "aws_instance"
    not starts_with(input.values.ami, "ami-0c55b159cbfafe1f0")
    msg := sprintf("EC2 instance '%s' must use approved AMI", [input.name])
}

# Deny security groups with unrestricted SSH access
deny[msg] {
    input.resource_type == "aws_security_group"
    ingress := input.values.ingress[_]
    ingress.from_port <= 22
    ingress.to_port >= 22
    ingress.cidr_blocks[_] == "0.0.0.0/0"
    msg := sprintf("Security group '%s' allows unrestricted SSH access", [input.name])
}

# Require tags on all resources
deny[msg] {
    input.resource_type != "aws_iam_policy_attachment"
    not input.values.tags.Environment
    msg := sprintf("Resource '%s' must have Environment tag", [input.name])
}

# Enforce instance type restrictions
deny[msg] {
    input.resource_type == "aws_instance"
    not re_match("^t3\\.(micro|small|medium|large)$", input.values.instance_type)
    msg := sprintf("EC2 instance '%s' uses disallowed instance type: %s", 
                   [input.name, input.values.instance_type])
}
```

## Common Pitfalls

### 🚫 State File Mismanagement

**Problem:** Storing state files locally or in version control.

**Solution:**
```hcl
# ✅ Use remote state backend
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "production/infrastructure.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-locks"
  }
}
```

### 🚫 Hard-Coded Values

**Problem:** Embedding environment-specific values directly in code.

**Solution:**
```hcl
# ❌ Bad
resource "aws_instance" "web" {
  instance_type = "t3.large"  # Hard-coded
}

# ✅ Good
variable "instance_type" {
  type    = string
  default = "t3.medium"
}

resource "aws_instance" "web" {
  instance_type = var.instance_type
}
```

### 🚫 No Module Versioning

**Problem:** Using modules without version constraints.

**Solution:**
```hcl
# ❌ Bad
module "vpc" {
  source = "github.com/company/terraform-aws-vpc"
}

# ✅ Good
module "vpc" {
  source  = "company/vpc/aws"
  version = "~> 2.0"
}
```

### 🚫 Ignoring Drift Detection

**Problem:** Not detecting manual changes to infrastructure.

**Solution:**
```bash
# Regularly run terraform plan to detect drift
terraform plan -out=tfplan
terraform show tfplan

# Use automated drift detection in CI/CD
```

### 🚫 Overly Complex Modules

**Problem:** Creating monolithic modules that do too much.

**Solution:**
- Keep modules focused on single responsibility
- Limit module inputs to < 10 variables
- Document module usage clearly
- Test modules independently

## Best Practices

### ✅ Do

- Store state remotely with locking enabled
- Use version control for all IaC code
- Implement code review for infrastructure changes
- Write tests for infrastructure code
- Use modules for reusability
- Tag all resources consistently
- Implement policy as code for compliance
- Document infrastructure architecture
- Use workspaces or directories for environments
- Automate validation in CI/CD pipelines
- Plan before applying changes
- Enable drift detection

### ❌ Don't

- Commit state files to version control
- Hard-code sensitive values (use secrets management)
- Manually modify infrastructure created by IaC
- Skip testing infrastructure changes
- Use latest version tags for modules
- Ignore plan output before applying
- Mix multiple environments in same state
- Create overly permissive IAM policies
- Forget to clean up unused resources

## Tools & Resources

### IaC Tools

| Category | Tools |
|----------|-------|
| **Provisioning** | Terraform, Pulumi, CloudFormation, ARM Templates |
| **Configuration** | Ansible, Chef, Puppet, SaltStack |
| **Container** | Kubernetes manifests, Helm, Kustomize |
| **Policy** | OPA/Conftest, Sentinel, Checkov |
| **Testing** | Terratest, Kitchen-Terraform, InSpec |
| **Cost Estimation** | Infracost, Terraform Cost Estimator |

### Supporting Tools

| Purpose | Tools |
|---------|-------|
| **State Management** | Terraform Cloud, Spacelift, Atlantis |
| **Secret Management** | HashiCorp Vault, AWS Secrets Manager, Azure Key Vault |
| **Linting** | Tflint, Checkov, Terrascan |
| **Documentation** | terraform-docs, tfdoc |
| **Visualization** | terraform-graph, infraviz |
| **CI/CD Integration** | GitHub Actions, GitLab CI, Jenkins, CircleCI |

### Learning Resources

- 📚 ["Terraform: Up & Running" by Yevgeniy Brikman](https://www.terraformupandrunning.com/)
- 📚 ["Infrastructure as Code" by Kief Morris](https://www.oreilly.com/library/view/infrastructure-as-code/9781491924334/)
- 🎥 [HashiCorp Learn](https://learn.hashicorp.com/terraform)
- 🏛️ [Pulumi Learning Path](https://www.pulumi.com/learn/)
- 📖 [Open Policy Agent Documentation](https://www.openpolicyagent.org/docs/)

## Examples

### Example 1: Multi-Tier Application Infrastructure

```hcl
# Production EKS cluster with RDS and ElastiCache
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"
  
  name = "production-vpc"
  cidr = "10.0.0.0/16"
  
  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
  
  enable_nat_gateway = true
  single_nat_gateway = false
  
  tags = {
    Environment = "production"
  }
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"
  
  cluster_name    = "production-cluster"
  cluster_version = "1.28"
  
  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.private_subnets
  
  eks_managed_node_groups = {
    primary = {
      min_size     = 3
      max_size     = 10
      desired_size = 3
      
      instance_types = ["t3.medium"]
      capacity_type  = "ON_DEMAND"
    }
  }
  
  tags = {
    Environment = "production"
  }
}

module "rds" {
  source  = "terraform-aws-modules/rds/aws"
  version = "~> 6.0"
  
  identifier = "production-db"
  
  engine            = "postgres"
  engine_version    = "15"
  instance_class    = "db.t3.medium"
  allocated_storage = 100
  
  db_name  = "appdb"
  username = "dbadmin"
  password = var.db_password
  
  vpc_security_group_ids = [aws_security_group.rds.id]
  db_subnet_group_name   = aws_db_subnet_group.rds.name
  
  multi_az               = true
  storage_encrypted      = true
  deletion_protection    = true
  skip_final_snapshot    = false
  final_snapshot_identifier = "production-db-final-snapshot"
  
  backup_retention_period = 30
  backup_window          = "03:00-04:00"
  maintenance_window     = "Mon:04:00-Mon:05:00"
  
  tags = {
    Environment = "production"
  }
}

module "elasticache" {
  source  = "terraform-aws-modules/elasticache/aws"
  version = "~> 2.0"
  
  cluster_id = "production-cache"
  
  engine          = "redis"
  engine_version  = "7.0"
  node_type       = "cache.t3.medium"
  num_cache_nodes = 3
  
  subnet_ids   = module.vpc.private_subnets
  security_group_ids = [aws_security_group.cache.id]
  
  automatic_failover_enabled = true
  multi_az_enabled          = true
  
  snapshot_retention_limit = 7
  
  tags = {
    Environment = "production"
  }
}
```

### Example 2: GitOps Workflow with Terraform Cloud

```yaml
# .github/workflows/terraform.yml
name: Terraform Cloud Run

on:
  push:
    branches: [main]
    paths:
      - 'infrastructure/**'
  pull_request:
    branches: [main]
    paths:
      - 'infrastructure/**'

env:
  TF_CLOUD_ORGANIZATION: my-org
  TF_CLOUD_HOSTNAME: app.terraform.io
  TF_WORKSPACE_PREFIX: myapp-

jobs:
  terraform-plan:
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request'
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.6.0
      
      - name: Terraform Init
        run: terraform init
        working-directory: infrastructure
        env:
          CLOUD_API_TOKEN: ${{ secrets.TF_CLOUD_API_TOKEN }}
      
      - name: Terraform Format Check
        run: terraform fmt -check -recursive
        working-directory: infrastructure
      
      - name: Terraform Validate
        run: terraform validate
        working-directory: infrastructure
      
      - name: Terraform Plan
        run: terraform plan -out=tfplan
        working-directory: infrastructure
        env:
          CLOUD_API_TOKEN: ${{ secrets.TF_CLOUD_API_TOKEN }}
      
      - name: Comment Plan on PR
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const plan = fs.readFileSync('infrastructure/tfplan', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## Terraform Plan\n\n\`\`\`\n${plan}\n\`\`\``
            })

  terraform-apply:
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    environment: production
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Terraform
        uses: hashicorp/setup-terraform@v3
        with:
          terraform_version: 1.6.0
      
      - name: Terraform Init
        run: terraform init
        working-directory: infrastructure
        env:
          CLOUD_API_TOKEN: ${{ secrets.TF_CLOUD_API_TOKEN }}
      
      - name: Terraform Apply
        run: terraform apply -auto-approve
        working-directory: infrastructure
        env:
          CLOUD_API_TOKEN: ${{ secrets.TF_CLOUD_API_TOKEN }}
```

## Success Indicators

### Proficiency Metrics

- **Beginner:** Can provision basic resources using existing modules
- **Intermediate:** Creates reusable modules and manages state effectively
- **Advanced:** Designs multi-account/multi-region architectures with policy enforcement
- **Expert:** Implements GitOps workflows and mentors others on IaC best practices

### Quality Indicators

- Zero manual infrastructure changes
- All resources tagged and documented
- Automated testing for infrastructure code
- Policy compliance rate > 95%
- Drift detection and remediation < 1 hour
- Infrastructure deployment time reduced by > 50%

## Related Skills

- [CI/CD](../devops-skills/ci_cd.md) - Pipeline automation for infrastructure
- [Container Orchestration](container_orchestration.md) - Managing containerized workloads
- [Cloud Infrastructure](cloud_infrastructure.md) - Cloud provider-specific knowledge
- [Monitoring & Observability](monitoring_observability.md) - Infrastructure monitoring
- [Security Skills](../security-skills/) - Securing infrastructure

## Version Information

---
version: 1.0.0
last_updated: 2024-01-15
reviewed_by: DevOps Team
next_review: 2024-07-15
---
