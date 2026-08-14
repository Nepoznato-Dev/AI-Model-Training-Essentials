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
# DevOps na CI/CD
DevOps ni mchanganyiko wa falsafa ya kitamaduni, mazoea na zana ambazo huwezesha timu kutoa programu kwa haraka na kwa uhakika zaidi. Inavunja ukuta kati ya watengenezaji (wanaotaka kusafirisha mabadiliko) na shughuli (wanaotaka utulivu). CI/CD - Ujumuishaji Unaoendelea na Uwasilishaji Unaoendelea - ndio uti wa mgongo wa kiotomatiki ambao hufanya iwezekanavyo.
---

## Mabomba ya CI/CD
### Nini Maana Ya CI/CD Halisi
| Muda | Inafanya Nini |
|------|-------------|
| **Muunganisho Unaoendelea (CI)** | Watengenezaji huunganisha msimbo mara kwa mara; kila unganisho huchochea miundo na majaribio ya kiotomatiki |
| **Utoaji Unaoendelea (CD)** | Msimbo daima uko katika hali inayoweza kutumiwa; kuachilia kwa uzalishaji ni uamuzi wa mwongozo |
| **Usambazaji Unaoendelea** | Kila badiliko linalofaulu majaribio huenda kwa uzalishaji kiotomatiki — hakuna lango la mkono |
### Hatua za Kawaida za Bomba
| Jukwaa | Nini Kinatokea | Zana |
|-------|-------------|--------|
| **Chanzo** | Msanidi programu anasukuma msimbo hadi Git | GitHub, GitLab, Bitbucket |
| **Jenga** | Kusanya msimbo, sakinisha vitegemezi | Maven, Gradle, npm, bomba |
| **Mtihani** | Endesha kitengo, ujumuishaji, ukaguzi wa pamba | Jest, pytest, JUnit |
| **Kifurushi** | Jenga picha ya Docker au bandia | Docker, Vifurushi vya ujenzi |
| **Weka (kuweka)** | Sambaza kwa mazingira ya jukwaa | Kubernetes, ECS, VM |
| **Mtihani (staging)** | Vipimo vya ujumuishaji, vipimo vya moshi | Selenium, Mtumishi |
| **Peleka (uzalishaji)** | Kutolewa kwa uzalishaji | Bluu-kijani, canary, rolling |
| **Fuatilia** | Angalia afya, makosa, utendaji | Prometheus, Grafana, Datadog |
### Zana za CI/CD Ikilinganishwa
| Zana | Andika | Nguvu |
|------|------|----------|
| **Vitendo vya GitHub** | Cloud CI/CD | Imeunganishwa kwa undani na GitHub; mtiririko wa kazi wa YAML |
| **GitLab CI** | Imejengwa ndani CI/CD | Jukwaa moja la repo + bomba |
| **Jenkins** | CI/CD inayojiendesha yenyewe | Inaweza kusanidiwa sana; mfumo mkubwa wa ikolojia wa programu-jalizi |
| **MduaraCI** | Cloud CI/CD | Haraka; nzuri kwa mtiririko wa kazi ulio na vyombo |
| **ArgoCD** | GitOps kwa Kubernetes | Matangazo, uwekaji unaoendeshwa na Git |
---

## Docker na Vyombo
### Kwanini Vyombo?
Kabla ya vyombo, shida ya kawaida ilikuwa "inafanya kazi kwenye mashine yangu." Vyombo hutatua hili kwa kupakia programu na vitegemezi vyake vyote - maktaba, muda wa utekelezaji, usanidi - katika kitengo kimoja, kinachobebeka ambacho hutumika sawa popote.
### Muhimu wa Docker
| Dhana | Maelezo |
|---------|-------------|
| **Picha** | Kiolezo cha kusoma pekee chenye programu na vitegemezi |
| **Kontena** | Mfano wa kukimbia wa picha |
| **Dockerfile** | Kichocheo cha kujenga picha |
| **Msajili** | Hifadhi ya picha (Docker Hub, ECR, GCR) |
| **Kiasi** | Hifadhi ya kudumu ambayo itasalia kwenye kontena kuanzishwa upya |
| **Mtandao** | Safu ya mtandao iliyotengwa kwa vyombo |
### Mbinu Bora za Dockerfile
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

Mbinu kuu: tumia taswira nyembamba/msingi za alpine, endesha kama zisizo na mizizi, ongeza akiba ya safu, tumia`.dockerignore`, changanua picha ili kubaini udhaifu (`trivy`,`docker scan`) na uweke vikomo vya rasilimali.
### Utungaji wa Docker
Kwa kuendesha vyombo vingi pamoja (programu + hifadhidata + kashe):
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
Kubernetes ndiye orchestrator ya kontena ya kiwango cha tasnia. Inasimamia uwekaji, upanuzi, na uendeshaji wa programu zilizo na vyombo.
### Usanifu wa Msingi
| Sehemu | Jukumu |
|-----------|------|
| **Ndege ya Kudhibiti** | Hudhibiti kundi (seva ya API, kipanga ratiba, nk, kidhibiti kidhibiti) |
| **Njia** | Mashine ya wafanyakazi (VM au ya kimwili) inayoendesha vyombo |
| **Pod** | Kitengo kidogo kinachoweza kupelekwa; kontena moja au zaidi zinazoshiriki mitandao |
| **Huduma** | Mwisho wa mtandao thabiti unaoelekeza trafiki kwenye maganda |
| **Usambazaji** | Ufafanuzi wa kutangaza wa hali ya ganda inayotakiwa (nakili, picha, n.k.) |
| **Ingress** | Sheria za uelekezaji wa HTTP kwa trafiki ya nje |
| **ConfigMap / Siri** | Usanidi na data nyeti iliyoingizwa kwenye maganda |
### Amri Muhimu za kubectl
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
Helm ndiye msimamizi wa kifurushi cha Kubernetes. **Chati** ni rundo la rasilimali za Kubernetes zilizosanidiwa awali. Ifikirie kama`apt`au`brew`kwa K8s.
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## Miundombinu kama Kanuni (IaC)
IaC hushughulikia usanidi wa miundombinu jinsi unavyoshughulikia msimbo wa programu: kudhibitiwa kwa toleo, kujaribiwa, na kutumwa kupitia bomba.
### Terraform vs Ansible
| Zana | Andika | Mbinu | Bora Kwa |
|------|------|----------------------|
| **Terraform** | Utoaji | Declarative (HCL); ya serikali | Kuunda rasilimali za wingu (VPC, VM, hifadhidata) |
| **Inawezekana** | Usanidi | Declarative (YAML); bila wakala | Kusanidi seva, kusakinisha programu |
| **Pulumi** | Utoaji | Muhimu (Python, Go, TS) | Timu zinazopendelea lugha halisi za programu |
| **CloudFormation** | Utoaji | Kutangaza (YAML/JSON); AWS-asili | Miundombinu ya AWS pekee |
### Mfano wa Terraform
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

Mbinu bora: tumia moduli za kutumika tena, hifadhi hali ukiwa mbali (S3 + DynamoDB kwa kufunga), usiwahi siri za msimbo ngumu na udhibiti kila kitu.
---

## Ufuatiliaji na Uangalizi
### Nguzo Tatu
| Nguzo | Inachokuambia | Zana |
|--------|--------------------------|
| **Vipimo** | Vipimo vya nambari kwa wakati (CPU, kiwango cha ombi, kiwango cha makosa) | Prometheus, CloudWatch, Datadog |
| **Magogo** | Matukio tofauti na muktadha (makosa, maombi, mabadiliko ya hali) | ELK Stack, Loki, Kumbukumbu za CloudWatch |
| **Mafumbo** | Safari ya ombi la mwisho hadi mwisho katika huduma zote | Jaeger, X-Ray, Zipkin |
### Prometheus + Grafana Stack
Rafu ya kawaida ya ufuatiliaji wa chanzo-wazi:
| Sehemu | Jukumu |
|-----------|------|
| **Prometheus** | Database ya mfululizo wa wakati; huchota vipimo kutoka kwa huduma |
| **Grafana** | Taswira na dashibodi |
| **Msimamizi wa Tahadhari** | Arifa za njia kwa Slack, PagerDuty, barua pepe |
| **Msafirishaji wa nodi** | Inaonyesha vipimo vya kiwango cha mfumo (CPU, RAM, diski) |
| **Blackbox Exporter** | Huchunguza sehemu za mwisho (HTTP, TCP, ICMP) |
### Vipimo Muhimu vya Kufuatilia
| Kitengo | Vipimo |
|----------|---------|
| **Miundombinu** | CPU, RAM, matumizi ya diski, mtandao wa I/O |
| **Maombi** | Kiwango cha ombi, muda wa kusubiri (p50, p95, p99), kiwango cha makosa |
| ** Hifadhidata** | Idadi ya hoja, maswali ya polepole, matumizi ya bwawa la unganisho |
| **Biashara** | Usajili, ubadilishaji, mapato |
---

## Mikakati ya Usambazaji
| Mkakati | Jinsi Inavyofanya Kazi | Hatari | Rudisha |
|----------|--------------------|----------|
| **Sasisho linaloendelea** | Badilisha hali za zamani na mpya polepole | Watumiaji wengine wa zamani, wengine kwenye toleo jipya | Rudi kwenye picha iliyotangulia |
| **Bluu-Kijani** | Endesha mazingira mawili yanayofanana; badilisha trafiki | Gharama ya miundombinu mara mbili wakati wa mpito | Rudisha papo hapo |
| **Canary** | Njia ndogo ya % ya trafiki hadi toleo jipya; kuongezeka hatua kwa hatua | Udhibiti tata wa trafiki | Rejesha trafiki kwenye njia thabiti |
| **Alama za Kipengele** | Tumia msimbo lakini ufiche vipengele nyuma ya vigeuza | Utata wa msimbo kutoka kwa mantiki ya masharti | Zima |
---

## GitOps
GitOps inachukua IaC kwa hitimisho lake la kimantiki: hazina ya Git ndio chanzo kimoja cha ukweli kwa hali inayotaka ya miundombinu na programu zako.
| Kanuni | Maelezo |
|-----------|-------------|
| **Tamko** | Kila kitu kilichofafanuliwa kama msimbo (YAML, HCL) |
| **Iliyotolewa** | Git ndio chanzo cha ukweli |
| **Otomatiki** | Zana zinaendelea kupatanisha hali inayotakiwa na hali halisi |
| **Inaweza kukaguliwa** | Kila mabadiliko ni ahadi ya Git |
**ArgoCD** na **Flux** ndizo zana zinazoongoza za GitOps za Kubernetes. Unasukuma mabadiliko kwenye repo lako la Git, na chombo huipeleka kiotomatiki kwenye nguzo.
---

## Majibu ya Tukio
Wakati kitu kinakatika saa 3 asubuhi:
1. **Kubali** tahadhari.
2. **Tathmini upeo**: ni huduma gani, watumiaji na data zimeathirika?
3. **Tambua ** chanzo kikuu - angalia kumbukumbu, vipimo, uwekaji wa hivi karibuni.
4. **Ina** ikiwezekana — vivunja saketi, bendera za vipengele, kuhamisha trafiki.
5. **Rekebisha** — rudisha nyuma au weka kiraka mbele.
6. **Wasiliana** — sasisha wadau na watumiaji (ukurasa wa hali).
7. **Uchunguzi wa baada ya maiti** — ndani ya saa 24–48, andika sababu kuu na vipengee vya kushughulikia.
Kusudi sio tu kusuluhisha tukio lakini kuhakikisha tukio kama hilo haliwezi kujirudia.