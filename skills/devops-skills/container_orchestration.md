# Container Orchestration

## Overview

Container orchestration automates the deployment, management, scaling, and networking of containers. It provides the infrastructure needed to run containerized applications at scale with high availability, automatic healing, and efficient resource utilization.

This skill covers Kubernetes fundamentals, deployment patterns, service mesh architecture, and operational best practices for running production-grade container workloads.

## Core Competencies

- **Kubernetes Architecture**: Understanding control plane and worker nodes
- **Workload Management**: Deployments, StatefulSets, DaemonSets, Jobs
- **Service Discovery**: Services, Ingress, DNS resolution
- **Storage Management**: PersistentVolumes, PersistentVolumeClaims, StorageClasses
- **Configuration Management**: ConfigMaps, Secrets, environment variables
- **Scaling Strategies**: Horizontal Pod Autoscaler, Vertical Pod Autoscaler, Cluster Autoscaler
- **Security**: RBAC, Network Policies, Pod Security Standards
- **Observability**: Logging, monitoring, tracing in containerized environments
- **Helm Charts**: Package management for Kubernetes applications

## When to Use

Container orchestration is essential when:
- ✅ Running microservices architectures
- ✅ Needing automatic scaling based on demand
- ✅ Requiring high availability and self-healing
- ✅ Managing complex multi-container applications
- ✅ Implementing CI/CD pipelines for containerized apps
- ✅ Running stateful applications with persistent storage
- ✅ Multi-cloud or hybrid cloud deployments

**Not ideal for:**
- ❌ Simple single-container applications
- ❌ Applications requiring low-level OS access
- ❌ Teams without Kubernetes expertise
- ❌ Short-lived batch jobs (consider serverless)

## Kubernetes Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Control Plane                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │   API    │  │ Scheduler│  │Controller│  │   etcd   │    │
│  │  Server  │  │          │  │ Manager  │  │          │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
└─────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
     ┌────────▼────────┐     ▼      ┌────────▼────────┐
     │   Worker Node 1  │            │   Worker Node 2  │
     │  ┌────────────┐  │            │  ┌────────────┐  │
     │  │  kubelet   │  │            │  │  kubelet   │  │
     │  ├────────────┤  │            │  ├────────────┤  │
     │  │ kube-proxy │  │            │  │ kube-proxy │  │
     │  ├────────────┤  │            │  ├────────────┤  │
     │  │ Container  │  │            │  │ Container  │  │
     │  │  Runtime   │  │            │  │  Runtime   │  │
     │  ├────────────┤  │            │  ├────────────┤  │
     │  │    Pods    │  │            │  │    Pods    │  │
     │  └────────────┘  │            │  └────────────┘  │
     └─────────────────┘            └─────────────────┘
```

### Control Plane Components

| Component | Purpose |
|-----------|---------|
| **API Server** | Frontend for Kubernetes control plane, handles all REST operations |
| **etcd** | Distributed key-value store for cluster data |
| **Scheduler** | Assigns pods to nodes based on resource requirements |
| **Controller Manager** | Runs controller processes (node, replication, endpoints, etc.) |

### Worker Node Components

| Component | Purpose |
|-----------|---------|
| **kubelet** | Agent that ensures containers are running in pods |
| **kube-proxy** | Network proxy maintaining network rules on nodes |
| **Container Runtime** | Software responsible for running containers (containerd, CRI-O) |

## Workload Types

### Deployment (Stateless Applications)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web-app
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  template:
    metadata:
      labels:
        app: web-app
        version: v1.2.0
    spec:
      containers:
      - name: web-app
        image: myregistry/web-app:v1.2.0
        ports:
        - containerPort: 8080
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
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

### StatefulSet (Stateful Applications)

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: database
spec:
  serviceName: database
  replicas: 3
  selector:
    matchLabels:
      app: database
  template:
    metadata:
      labels:
        app: database
    spec:
      containers:
      - name: postgres
        image: postgres:15
        ports:
        - containerPort: 5432
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
        env:
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: password
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: gp3
      resources:
        requests:
          storage: 100Gi
```

### DaemonSet (Node-Level Services)

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: log-collector
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: log-collector
  template:
    metadata:
      labels:
        app: log-collector
    spec:
      containers:
      - name: fluent-bit
        image: fluent/fluent-bit:latest
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
```

### Job and CronJob (Batch Processing)

```yaml
# One-time Job
apiVersion: batch/v1
kind: Job
metadata:
  name: data-migration
spec:
  completions: 1
  parallelism: 1
  backoffLimit: 3
  template:
    spec:
      containers:
      - name: migration
        image: myregistry/migration-tool:v1.0
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: db-secret
              key: url
      restartPolicy: Never

---
# Scheduled CronJob
apiVersion: batch/v1
kind: CronJob
metadata:
  name: daily-backup
spec:
  schedule: "0 2 * * *"  # Every day at 2 AM
  concurrencyPolicy: Forbid
  successfulJobsHistoryLimit: 3
  failedJobsHistoryLimit: 1
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: backup
            image: myregistry/backup-tool:v1.0
            args:
            - --full-backup
            - --retention=7
          restartPolicy: OnFailure
```

## Service Discovery and Networking

### Service Types

```yaml
# ClusterIP (default - internal only)
apiVersion: v1
kind: Service
metadata:
  name: backend-service
spec:
  type: ClusterIP
  selector:
    app: backend
  ports:
  - port: 80
    targetPort: 8080

---
# NodePort (expose on node IP)
apiVersion: v1
kind: Service
metadata:
  name: debug-service
spec:
  type: NodePort
  selector:
    app: debug-app
  ports:
  - port: 80
    targetPort: 8080
    nodePort: 30080

---
# LoadBalancer (cloud provider LB)
apiVersion: v1
kind: Service
metadata:
  name: public-service
spec:
  type: LoadBalancer
  selector:
    app: public-app
  ports:
  - port: 443
    targetPort: 8443

---
# Headless Service (for StatefulSets)
apiVersion: v1
kind: Service
metadata:
  name: database-headless
spec:
  clusterIP: None
  selector:
    app: database
  ports:
  - port: 5432
```

### Ingress Controller

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - app.example.com
    secretName: app-tls-secret
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 80
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web-service
            port:
              number: 80
```

## Scaling Strategies

### Horizontal Pod Autoscaler (HPA)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: web-app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-app
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

### Vertical Pod Autoscaler (VPA)

```yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: web-app-vpa
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: web-app
  updatePolicy:
    updateMode: Auto
  resourcePolicy:
    containerPolicies:
    - containerName: '*'
      controlledResources: ["cpu", "memory"]
      minAllowed:
        cpu: 100m
        memory: 128Mi
      maxAllowed:
        cpu: 2
        memory: 2Gi
```

## Configuration Management

### ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  config.yaml: |
    server:
      port: 8080
      timeout: 30s
    database:
      max_connections: 100
      pool_size: 20
    logging:
      level: info
      format: json
  
  FEATURE_FLAGS: "new-ui,dark-mode,beta-api"
  
---
# Usage in Pod
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
spec:
  containers:
  - name: app
    image: myapp:latest
    envFrom:
    - configMapRef:
        name: app-config
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
  volumes:
  - name: config-volume
    configMap:
      name: app-config
```

### Secrets

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-credentials
type: Opaque
stringData:
  username: admin
  password: SuperSecretPassword123!
  connection-string: "postgresql://admin:password@db:5432/mydb"

---
# Usage in Pod
apiVersion: v1
kind: Pod
metadata:
  name: app-with-secrets
spec:
  containers:
  - name: app
    image: myapp:latest
    env:
    - name: DB_USERNAME
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: username
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: password
    volumeMounts:
    - name: secret-volume
      mountPath: /etc/secrets
      readOnly: true
  volumes:
  - name: secret-volume
    secret:
      secretName: db-credentials
```

## Security Best Practices

### Pod Security Standards

```yaml
# Restricted Pod Security
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
  labels:
    pod-security.kubernetes.io/enforce: restricted
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    runAsGroup: 1000
    fsGroup: 1000
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: app
    image: myapp:latest
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
    resources:
      limits:
        memory: "512Mi"
        cpu: "500m"
```

### Network Policies

```yaml
# Default deny all ingress traffic
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: production
spec:
  podSelector: {}
  policyTypes:
  - Ingress

---
# Allow specific traffic
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-api-traffic
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: api
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    - namespaceSelector:
        matchLabels:
          name: monitoring
    ports:
    - protocol: TCP
      port: 8080
```

### RBAC Configuration

```yaml
# ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-service-account
  namespace: production

---
# Role
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: production
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log"]
  verbs: ["get", "list", "watch"]

---
# RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: production
subjects:
- kind: ServiceAccount
  name: app-service-account
  namespace: production
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

## Helm Chart Structure

```
my-chart/
├── Chart.yaml
├── values.yaml
├── values-dev.yaml
├── values-prod.yaml
├── charts/
├── templates/
│   ├── _helpers.tpl
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   ├── hpa.yaml
│   └── tests/
│       └── test-connection.yaml
└── README.md
```

### Example Chart.yaml

```yaml
apiVersion: v2
name: my-application
description: A Helm chart for deploying my application
type: application
version: 1.0.0
appVersion: "2.0.0"
keywords:
  - web
  - api
  - kubernetes
maintainers:
  - name: DevOps Team
    email: devops@example.com
dependencies:
  - name: postgresql
    version: "~> 12.0"
    repository: "https://charts.bitnami.com/bitnami"
    condition: postgresql.enabled
```

## Common Pitfalls

### 🚫 Resource Misconfiguration

**Problem:** Not setting resource requests and limits.

**Solution:**
```yaml
resources:
  requests:
    memory: "256Mi"
    cpu: "250m"
  limits:
    memory: "512Mi"
    cpu: "500m"
```

### 🚫 Missing Health Checks

**Problem:** No liveness or readiness probes.

**Solution:**
```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 30
  periodSeconds: 10
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 5
```

### 🚫 Running as Root

**Problem:** Containers running as root user.

**Solution:**
```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
```

### 🚫 No Pod Disruption Budgets

**Problem:** All pods can be evicted simultaneously during maintenance.

**Solution:**
```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: app-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: web-app
```

### 🚫 Ignoring Namespace Isolation

**Problem:** All workloads in default namespace.

**Solution:**
```bash
# Create dedicated namespaces
kubectl create namespace production
kubectl create namespace staging
kubectl create namespace monitoring
```

## Best Practices

### ✅ Do

- Always set resource requests and limits
- Implement health checks (liveness, readiness, startup)
- Use namespaces for environment isolation
- Apply Pod Security Standards
- Use Network Policies for traffic control
- Store sensitive data in Secrets (encrypted at rest)
- Use ConfigMaps for non-sensitive configuration
- Implement Pod Disruption Budgets
- Use labels consistently for organization
- Enable audit logging
- Regularly rotate credentials and certificates
- Use Helm or GitOps for deployments
- Monitor resource usage and adjust limits

### ❌ Don't

- Run containers as root
- Hard-code secrets in manifests
- Skip resource limits
- Ignore security updates
- Use latest tags in production
- Deploy without health checks
- Mix different environments in same namespace
- Grant excessive RBAC permissions
- Forget to set up log aggregation
- Neglect backup strategies for stateful apps

## Tools & Resources

### Kubernetes Distributions

| Distribution | Best For |
|--------------|----------|
| **EKS** | AWS-native workloads |
| **GKE** | Google Cloud users |
| **AKS** | Azure deployments |
| **Rancher** | Multi-cluster management |
| **OpenShift** | Enterprise features |
| **Kind/K3s** | Local development |

### Monitoring & Observability

| Tool | Purpose |
|------|---------|
| **Prometheus** | Metrics collection |
| **Grafana** | Visualization |
| **Jaeger** | Distributed tracing |
| **ELK Stack** | Log aggregation |
| **Loki** | Lightweight logging |

### Package Management

| Tool | Purpose |
|------|---------|
| **Helm** | Kubernetes package manager |
| **Kustomize** | Configuration customization |
| **Carvel** | Supply chain tools |

### GitOps

| Tool | Description |
|------|-------------|
| **ArgoCD** | Declarative GitOps CD |
| **Flux** | Continuous delivery |
| **Jenkins X** | Cloud-native CI/CD |

### Security

| Tool | Purpose |
|------|---------|
| **Trivy** | Vulnerability scanner |
| **Falco** | Runtime security |
| **OPA/Gatekeeper** | Policy enforcement |
| **Kyverno** | Kubernetes policy engine |

## Examples

### Example 1: Complete Microservice Deployment

```yaml
# Full microservice stack with all components
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
  namespace: production
  labels:
    app: order-service
    team: commerce
spec:
  replicas: 3
  selector:
    matchLabels:
      app: order-service
  template:
    metadata:
      labels:
        app: order-service
        version: v1.5.0
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
    spec:
      serviceAccountName: order-service-sa
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
      containers:
      - name: order-service
        image: registry.example.com/order-service:v1.5.0
        imagePullPolicy: Always
        ports:
        - containerPort: 8080
          name: http
        - containerPort: 9090
          name: metrics
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "1000m"
        env:
        - name: SPRING_PROFILES_ACTIVE
          value: "production"
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: order-db-secret
              key: url
        - name: REDIS_HOST
          valueFrom:
            configMapKeyRef:
              name: order-config
              key: redis-host
        livenessProbe:
          httpGet:
            path: /actuator/health/liveness
            port: 8080
          initialDelaySeconds: 60
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /actuator/health/readiness
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 5
        volumeMounts:
        - name: tmp
          mountPath: /tmp
      volumes:
      - name: tmp
        emptyDir: {}
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
                  - order-service
              topologyKey: kubernetes.io/hostname
---
apiVersion: v1
kind: Service
metadata:
  name: order-service
  namespace: production
  labels:
    app: order-service
spec:
  type: ClusterIP
  ports:
  - port: 80
    targetPort: 8080
    name: http
  - port: 9090
    targetPort: 9090
    name: metrics
  selector:
    app: order-service
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: order-service-hpa
  namespace: production
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: order-service
  minReplicas: 3
  maxReplicas: 15
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
```

## Success Indicators

### Proficiency Levels

- **Beginner:** Can deploy simple applications using kubectl and basic YAML
- **Intermediate:** Manages multi-service applications with Helm, implements autoscaling
- **Advanced:** Designs secure, production-ready clusters with proper observability
- **Expert:** Architects multi-cluster setups, implements GitOps, optimizes costs

### Quality Metrics

- Pod uptime > 99.9%
- Mean time to recovery < 5 minutes
- Zero security vulnerabilities in base images
- Resource utilization > 60%
- Deployment frequency > daily
- Change failure rate < 5%

## Related Skills

- [CI/CD](ci_cd.md) - Continuous integration and deployment
- [Infrastructure as Code](infrastructure_as_code.md) - IaC for cluster provisioning
- [Monitoring & Observability](monitoring_observability.md) - Cluster and application monitoring
- [Security Skills](../security-skills/) - Container and cluster security
- [Cloud Infrastructure](cloud_infrastructure.md) - Managed Kubernetes services

## Version Information

---
version: 1.0.0
last_updated: 2024-01-15
reviewed_by: DevOps Team
next_review: 2024-07-15
---
