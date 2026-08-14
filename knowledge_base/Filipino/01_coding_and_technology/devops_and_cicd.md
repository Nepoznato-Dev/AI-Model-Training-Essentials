<!--
---
# Metadata
title: "DevOps and CI/CD"
description: "CI/CD pipelines, Docker, Kubernetes, Terraform, GitOps"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [devops, cicd, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# DevOps at CI/CD
Ang DevOps ay ang kumbinasyon ng kultural na pilosopiya, kasanayan, at tool na nagbibigay-daan sa mga team na makapaghatid ng software nang mas mabilis at mas maaasahan. Sinisira nito ang pader sa pagitan ng mga developer (na gustong magpadala ng mga pagbabago) at mga operasyon (na gustong magkaroon ng katatagan). CI/CD — Continuous Integration at Continuous Delivery — ay ang automation backbone na ginagawang posible.
---

## CI/CD Pipelines
### Ano Ang Talagang Ibig Sabihin ng CI/CD
| Termino | Ano ang Ginagawa Nito |
|------|-------------|
| **Patuloy na Pagsasama (CI)** | Ang mga developer ay madalas na pinagsama ang code; ang bawat pagsasama ay nagti-trigger ng mga awtomatikong build at pagsubok |
| **Patuloy na Paghahatid (CD)** | Palaging nasa deployable na estado ang code; ang pagpapalabas sa produksyon ay isang manu-manong desisyon |
| **Patuloy na Deployment** | Bawat pagbabagong pumasa sa mga pagsubok ay awtomatikong napupunta sa produksyon — walang manu-manong gate |
### Mga Karaniwang Yugto ng Pipeline
| Yugto | Ano ang Mangyayari | Mga tool |
|-------|-------------|-------|
| **Pinagmulan** | Itinulak ng developer ang code sa Git | GitHub, GitLab, Bitbucket |
| **Bumuo** | Mag-compile ng code, mag-install ng mga dependencies | Maven, Gradle, npm, pip |
| **Pagsubok** | Patakbuhin ang unit, integration, lint checks | Jest, pytest, JUnit |
| **Pakete** | Bumuo ng imahe o artifact ng Docker | Docker, Buildpacks |
| **Deploy (staging)** | I-deploy sa kapaligiran ng pagtatanghal ng dula | Kubernetes, ECS, VM |
| **Pagsubok (pagtatanghal)** | Mga pagsubok sa pagsasama, mga pagsubok sa usok | Selenium, Postman |
| **I-deploy (produksyon)** | Paglabas sa produksyon | Blue-green, canary, rolling |
| **Subaybayan** | Obserbahan ang kalusugan, mga pagkakamali, pagganap | Prometheus, Grafana, Datadog |
### CI/CD Tools Compared
| Tool | Uri | Lakas |
|------|------|----------|
| **Mga Pagkilos sa GitHub** | Cloud CI/CD | Malalim na isinama sa GitHub; Mga workflow ng YAML |
| **GitLab CI** | Built-in na CI/CD | Isang platform para sa repo + pipeline |
| **Jenkins** | Self-host na CI/CD | Lubos na maisasaayos; napakalaking plugin ecosystem |
| **CircleCI** | Cloud CI/CD | Mabilis; mabuti para sa mga containerized na daloy ng trabaho |
| **ArgoCD** | GitOps para sa Kubernetes | Deklarasyon, Git-driven na mga deployment |
---

## Docker at Mga Container
### Bakit Container?
Bago ang mga lalagyan, ang klasikong problema ay "ito ay gumagana sa aking makina." Nire-solve ito ng mga container sa pamamagitan ng pag-package ng isang application kasama ang lahat ng mga dependency nito — mga library, runtime, config — sa isang solong portable na unit na tumatakbo kahit saan.
### Docker Essentials
| Konsepto | Paglalarawan |
|---------|-------------|
| **Larawan** | Read-only na template na may app + dependencies |
| **Lalagyan** | Running instance ng isang imahe |
| **Dockerfile** | Recipe para sa pagbuo ng isang imahe |
| **Registry** | Imbakan para sa mga larawan (Docker Hub, ECR, GCR) |
| **Dami** | Ang tuluy-tuloy na storage na nananatili sa container ay nag-restart |
| **Network** | Nakahiwalay na layer ng networking para sa mga container |
### Pinakamahuhusay na Kasanayan sa Dockerfile
```dockerfile
# Use specific base image tags, not 'latest'
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (leverage Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run as non-root user
USER appuser

# Expose port and define entrypoint
EXPOSE 8000
CMD ["python", "main.py"]
```

Mga pangunahing kasanayan: gumamit ng slim/alpine base na mga imahe, tumakbo bilang hindi-root, gumamit ng layer caching, gumamit ng`.dockerignore`, mag-scan ng mga larawan para sa mga kahinaan (`trivy`,`docker scan`), at magtakda ng mga limitasyon sa mapagkukunan.
### Docker Compose
Para sa pagpapatakbo ng maraming container nang magkasama (app + database + cache):
```yaml
services:
  app:
    build: .
    ports: ["8000:8000"]
    depends_on: [db, redis]
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/mydb
  db:
    image: postgres:16
    volumes: [pgdata:/var/lib/postgresql/data]
  redis:
    image: redis:7-alpine
volumes:
  pgdata:
```

---

## Kubernetes (K8s)
Ang Kubernetes ay ang pamantayang industriya ng container orchestrator. Pinamamahalaan nito ang pag-deploy, pag-scale, at pagpapatakbo ng mga containerized na application.
### Pangunahing Arkitektura
| Bahagi | Tungkulin |
|-----------|------|
| **Control Plane** | Pinamamahalaan ang cluster (API server, scheduler, etcd, controller manager) |
| **Node** | Worker machine (VM o pisikal) na nagpapatakbo ng mga container |
| **Pod** | Pinakamaliit na nade-deploy na unit; isa o higit pang mga lalagyan na nagbabahagi ng networking |
| **Serbisyo** | Matatag na endpoint ng network na nagruruta ng trapiko sa mga pod |
| **Deployment** | Pahayag na kahulugan ng nais na estado ng pod (mga replika, larawan, atbp.) |
| **Pagpasok** | Mga panuntunan sa pagruruta ng HTTP para sa panlabas na trapiko |
| **ConfigMap / Secret** | Configuration at sensitibong data na ini-inject sa mga pod |
### Mahahalagang Kubectl Command
```bash
kubectl get pods                    # List pods
kubectl get services                # List services
kubectl describe pod <name>         # Detailed pod info
kubectl logs <pod-name>             # View pod logs
kubectl exec -it <pod> -- /bin/sh   # Shell into a pod
kubectl apply -f deployment.yaml    # Apply a manifest
kubectl rollout status deploy/myapp # Check rollout progress
kubectl scale deploy/myapp --replicas=5  # Scale to 5 replicas
```

### Helm
Si Helm ang package manager para sa Kubernetes. Ang **chart** ay isang bundle ng mga paunang na-configure na mapagkukunan ng Kubernetes. Isipin ito bilang`apt`o`brew`para sa mga K8.
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## Imprastraktura bilang Code (IaC)
Tinatrato ng IaC ang configuration ng imprastraktura sa parehong paraan kung paano mo tinatrato ang application code: kinokontrol, sinubok, at na-deploy sa pamamagitan ng mga pipeline.
### Terraform vs Ansible
| Tool | Uri | Diskarte | Pinakamahusay Para sa |
|------|------|----------|----------|
| **Terraform** | Paglalaan | Pahayag (HCL); nakabatay sa estado | Paglikha ng mga mapagkukunan ng ulap (mga VPC, VM, database) |
| **Ansible** | Configuration | Pahayag (YAML); walang ahente | Pag-configure ng mga server, pag-install ng software |
| **Pulumi** | Paglalaan | Imperative (Python, Go, TS) | Mga koponan na mas gusto ang mga totoong programming language |
| **CloudFormation** | Paglalaan | Pahayag (YAML/JSON); AWS-native | AWS-only na imprastraktura |
### Halimbawa ng Terraform
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

Pinakamahuhusay na kagawian: gumamit ng mga module para sa muling paggamit, mag-imbak ng estado nang malayuan (S3 + DynamoDB para sa pag-lock), hindi kailanman mga hardcode na sikreto, at kontrolin ang lahat ng bersyon.
---

## Pagsubaybay at Pagmamasid
### Ang Tatlong Haligi
| Haligi | Ang Sinasabi Nito sa Iyo | Mga tool |
|--------|-------------------|-------|
| **Mga Sukatan** | Mga numerical na sukat sa paglipas ng panahon (CPU, rate ng kahilingan, rate ng error) | Prometheus, CloudWatch, Datadog |
| **Mga Log** | Mga discrete na kaganapan na may konteksto (mga error, kahilingan, pagbabago ng estado) | ELK Stack, Loki, CloudWatch Logs |
| **Mga Bakas** | End-to-end na paglalakbay sa paghiling sa mga serbisyo | Jaeger, X-Ray, Zipkin |
### Prometheus + Grafana Stack
Ang karaniwang open-source monitoring stack:
| Bahagi | Tungkulin |
|-----------|------|
| **Prometheus** | Database ng serye ng oras; kumukuha ng mga sukatan mula sa mga serbisyo |
| **Grafana** | Visualization at mga dashboard |
| **Alertmanager** | Mga alerto sa ruta sa Slack, PagerDuty, email |
| **Node Exporter** | Inilalantad ang mga sukatan sa antas ng system (CPU, RAM, disk) |
| **Blackbox Exporter** | Mga probe na endpoint (HTTP, TCP, ICMP) |
### Mga Pangunahing Sukatan na Susubaybayan
| Kategorya | Mga sukatan |
|----------|---------|
| **Imprastraktura** | CPU, RAM, paggamit ng disk, network I/O |
| **Aplikasyon** | Rate ng kahilingan, latency (p50, p95, p99), rate ng error |
| **Database** | Bilang ng query, mabagal na query, paggamit ng pool ng koneksyon |
| **Negosyo** | Mga pag-signup, conversion, kita |
---

## Mga Diskarte sa Pag-deploy
| Diskarte | Paano Ito Gumagana | Panganib | Rollback |
|----------|-------------|------|----------|
| **Rolling Update** | Palitan ang mga lumang instance ng mga bago nang unti-unting | Ang ilang mga gumagamit sa luma, ang ilan sa bagong bersyon | Bumalik sa nakaraang larawan |
| **Asul-Berde** | Magpatakbo ng dalawang magkatulad na kapaligiran; lumipat ng trapiko | Dobleng gastos sa imprastraktura sa panahon ng paglipat | Agad na lumipat pabalik |
| **Canary** | Iruta ang maliit na % ng trapiko sa bagong bersyon; unti-unting tumaas | Masalimuot na pamamahala ng trapiko | I-ruta ang trapiko pabalik sa stable |
| **Mga Flag ng Tampok** | I-deploy ang code ngunit itago ang mga feature sa likod ng mga toggle | Ang pagiging kumplikado ng code mula sa conditional logic | I-toggle off |
---

## GitOps
Dinadala ng GitOps ang IaC sa lohikal na konklusyon nito: ang Git repository ay ang nag-iisang pinagmumulan ng katotohanan para sa nais na estado ng iyong imprastraktura at mga aplikasyon.
| Prinsipyo | Paglalarawan |
|-----------|-------------|
| **Pahayag** | Lahat ng inilarawan bilang code (YAML, HCL) |
| **Bersyon** | Ang Git ay ang pinagmulan ng katotohanan |
| **Awtomatiko** | Patuloy na pinagkakasundo ng mga tool ang nais na estado sa aktwal na estado |
| **Naa-audit** | Ang bawat pagbabago ay isang Git commit |
Ang **ArgoCD** at **Flux** ay ang nangungunang mga tool sa GitOps para sa Kubernetes. Itulak mo ang isang pagbabago sa iyong Git repo, at awtomatikong i-deploy ito ng tool sa cluster.
---

## Tugon sa Insidente
Kapag may nasira sa 3 AM:
1. **Kilalanin** ang alerto.
2. **Turiin ang saklaw**: aling mga serbisyo, user, at data ang apektado?
3. **Kilalanin** ang ugat na sanhi — suriin ang mga log, sukatan, kamakailang pag-deploy.
4. **Contain** kung maaari — mga circuit breaker, feature flag, traffic shifting.
5. **Fix** — rollback o patch forward.
6. **Communicate** — i-update ang mga stakeholder at user (status page).
7. **Post-mortem** — sa loob ng 24–48 oras, idokumento ang ugat ng sanhi at mga item ng aksyon.
Ang layunin ay hindi lamang upang malutas ang insidente ngunit upang matiyak na ang parehong insidente ay hindi mauulit.