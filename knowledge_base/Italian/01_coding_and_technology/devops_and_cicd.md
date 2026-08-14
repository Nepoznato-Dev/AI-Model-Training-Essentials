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
# DevOps e CI/CD
DevOps è la combinazione di filosofia culturale, pratiche e strumenti che consente ai team di fornire software in modo più rapido e affidabile. Abbatte il muro tra gli sviluppatori (che vogliono apportare modifiche) e le operazioni (che vogliono stabilità). CI/CD (Continuous Integration e Continuous Delivery) è la struttura portante dell'automazione che lo rende possibile.
---

## Condutture CI/CD
### Cosa significa realmente CI/CD
| Termine | Cosa fa |
|------|-------------|
| **Integrazione continua (CI)** | Gli sviluppatori uniscono frequentemente il codice; ogni unione attiva build e test automatizzati |
| **Consegna continua (CD)** | Il codice è sempre in uno stato distribuibile; il rilascio in produzione è una decisione manuale |
| **Distribuzione continua** | Ogni modifica che supera i test passa automaticamente alla produzione, senza alcuna operazione manuale |
### Fasi tipiche della pipeline
| Palcoscenico | Cosa succede | Strumenti |
|-------|-------------|-------|
| **Fonte** | Lo sviluppatore invia il codice a Git | GitHub, GitLab, Bitbucket |
| **Costruisci** | Compila il codice, installa le dipendenze | Maven, Gradle, npm, pip |
| **Prova** | Esegui unità, integrazione, controlli lanugine | Scherzo, pytest, JUnit |
| **Pacchetto** | Crea immagine o artefatto Docker | Docker, Buildpack |
| **Distribuzione (staging)** | Distribuire nell'ambiente di staging | Kubernetes, ECS, VM |
| **Test (stadiazione)** | Prove di integrazione, prove di fumo | Selenio, postino |
| **Distribuzione (produzione)** | Rilascio in produzione | Blu-verde, canarino, rotolante |
| **Monitoraggio** | Osservare salute, errori, prestazioni | Prometeo, Grafana, Datadog |
### Strumenti CI/CD a confronto
| Strumento | Digitare | Forza |
|------|------|----------|
| **Azioni GitHub** | CI/CD cloud | Profondamente integrato con GitHub; Flussi di lavoro YAML |
| **CI GitLab** | CI/CD integrato | Piattaforma unica per pronti contro termine + pipeline |
| **Jenkins** | CI/CD self-hosted | Altamente configurabile; enorme ecosistema di plugin |
| **CerchioCI** | CI/CD cloud | Veloce; buono per flussi di lavoro containerizzati |
| **ArgoCD** | GitOps per Kubernetes | Distribuzioni dichiarative guidate da Git |
---

## Finestra mobile e contenitori
### Perché i contenitori?
Prima dei contenitori, il problema classico era "funziona sulla mia macchina". I contenitori risolvono questo problema impacchettando un'applicazione con tutte le sue dipendenze (librerie, runtime, configurazione) in un'unica unità portatile che funziona in modo identico ovunque.
### Elementi essenziali di Docker
| Concetto | Descrizione |
|---------|-----|
| **Immagine** | Modello di sola lettura con app + dipendenze |
| **Contenitore** | Istanza in esecuzione di un'immagine |
| **Dockerfile** | Ricetta per costruire un'immagine |
| **Registro** | Archiviazione per immagini (Docker Hub, ECR, GCR) |
| **Volume** | Archiviazione persistente che sopravvive al riavvio del contenitore |
| **Rete** | Livello di rete isolato per contenitori |
### Migliori pratiche per Dockerfile
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

Pratiche chiave: utilizzare immagini di base slim/alpine, eseguire come non root, sfruttare la memorizzazione nella cache dei livelli, utilizzare `.dockerignore`, scansionare le immagini per individuare eventuali vulnerabilità (`trivy`, `docker scan`) e impostare limiti di risorse.
### Docker Componi
Per eseguire più contenitori insieme (app + database + cache):
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

## Kubernetes (K8)
Kubernetes è l'orchestratore di contenitori standard del settore. Gestisce la distribuzione, la scalabilità e il funzionamento delle applicazioni containerizzate.
### Architettura principale
| Componente | Ruolo |
|-----------|------|
| **Piano di controllo** | Gestisce il cluster (server API, scheduler, etcd, controller manager) |
| **Nodo** | Macchina di lavoro (VM o fisica) che esegue i contenitori |
| **Pod** | Unità più piccola dispiegabile; uno o più contenitori che condividono la rete |
| **Servizio** | Endpoint di rete stabile che instrada il traffico ai pod |
| **Distribuzione** | Definizione dichiarativa dello stato del pod desiderato (repliche, immagini, ecc.) |
| **Ingresso** | Regole di routing HTTP per il traffico esterno |
| **ConfigMap/Segreto** | Configurazione e dati sensibili inseriti nei pod |
### Comandi essenziali di kubectl
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

### Timone
Helm è il gestore di pacchetti per Kubernetes. Un **grafico** è un insieme di risorse Kubernetes preconfigurate. Consideralo come`apt`o`brew`per i K8.
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## Infrastruttura come codice (IaC)
IaC tratta la configurazione dell'infrastruttura nello stesso modo in cui tratti il ​​codice dell'applicazione: controllato dalla versione, testato e distribuito tramite pipeline.
### Terraform contro Ansible
| Strumento | Digitare | Avvicinamento | Ideale per |
|------|------|----------|----------|
| **Terraforma** | Approvvigionamento | Dichiarativo (HCL); su base statale | Creazione di risorse cloud (VPC, VM, database) |
| **Ansible** | Configurazione | Dichiarativo (YAML); senza agenti | Configurazione server, installazione software |
| **Pulumi** | Approvvigionamento | Imperativo (Python, Go, TS) | Team che preferiscono linguaggi di programmazione reali |
| **CloudFormation** | Approvvigionamento | Dichiarativo (YAML/JSON); Nativo AWS | Infrastruttura solo AWS |
### Esempio di terraformazione
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

Best practice: utilizzare i moduli per la riusabilità, archiviare lo stato in remoto (S3 + DynamoDB per il blocco), non codificare mai i segreti e controllare la versione di tutto.
---

## Monitoraggio e osservabilità
### I tre pilastri
| Pilastro | Cosa ti dice | Strumenti |
|--------|-----------------|-------|
| **Metriche** | Misurazioni numeriche nel tempo (CPU, tasso di richieste, tasso di errore) | Prometeo, CloudWatch, Datadog |
| **Registri** | Eventi discreti con contesto (errori, richieste, cambiamenti di stato) | ELK Stack, Loki, CloudWatch Logs |
| **Tracce** | Percorso delle richieste end-to-end attraverso i servizi | Jaeger, Raggi X, Zipkin |
### Prometeo + Pila di Grafana
Lo stack di monitoraggio open source standard:
| Componente | Ruolo |
|-----------|------|
| **Prometeo** | Database delle serie temporali; estrae le metriche dai servizi |
| **Grafana** | Visualizzazione e dashboard |
| **Gestione avvisi** | Indirizza gli avvisi a Slack, PagerDuty, e-mail |
| **Esportatore nodo** | Espone le metriche a livello di sistema (CPU, RAM, disco) |
| **Esportatore Blackbox** | Esamina gli endpoint (HTTP, TCP, ICMP) |
### Metriche chiave da monitorare
| Categoria | Metriche |
|----------|---------|
| **Infrastrutture** | CPU, RAM, utilizzo del disco, I/O di rete |
| **Applicazione** | Tasso di richiesta, latenza (p50, p95, p99), tasso di errore |
| **Banca dati** | Conteggio query, query lente, utilizzo del pool di connessioni |
| **Affari** | Iscrizioni, conversioni, entrate |
---

## Strategie di distribuzione
| Strategia | Come funziona | Rischio | Ripristino |
|----------|-------------|------|----------|
| **Aggiornamento progressivo** | Sostituisci gradualmente le vecchie istanze con quelle nuove | Alcuni utenti della vecchia versione, altri della nuova versione | Torna all'immagine precedente |
| **Blu-Verde** | Esegui due ambienti identici; cambiare traffico | Doppio costo delle infrastrutture durante la transizione | Ritorno istantaneo |
| **Canarie** | Indirizzare una piccola percentuale di traffico alla nuova versione; aumentare gradualmente | Gestione complessa del traffico | Reindirizza il traffico a stabile |
| **Flag funzionalità** | Distribuisci il codice ma nascondi le funzionalità dietro gli interruttori | Complessità del codice dalla logica condizionale | Disattiva |
---

## GitOps
GitOps porta IaC alla sua logica conclusione: il repository Git è l'unica fonte di verità per lo stato desiderato della tua infrastruttura e delle tue applicazioni.
| Principio | Descrizione |
|-----------|-------------|
| **Dichiarativo** | Tutto descritto come codice (YAML, HCL) |
| **Versione** | Git è la fonte della verità |
| **Automatizzato** | Gli strumenti riconciliano continuamente lo stato desiderato con lo stato reale |
| **Verificabile** | Ogni modifica è un commit Git |
**ArgoCD** e **Flux** sono gli strumenti GitOps principali per Kubernetes. Invii una modifica al tuo repository Git e lo strumento la distribuisce automaticamente al cluster.
---

## Risposta all'incidente
Quando qualcosa si rompe alle 3 del mattino:
1. **Conferma** l'avviso.
2. **Valutare l'ambito**: quali servizi, utenti e dati sono interessati?
3. **Identificare** la causa principale: controllare log, parametri e distribuzioni recenti.
4. **Contenere** se possibile: interruttori automatici, indicatori di funzionalità, spostamento del traffico.
5. **Correzione**: rollback o avanzamento patch.
6. **Comunicare**: aggiornare le parti interessate e gli utenti (pagina di stato).
7. **Post mortem**: entro 24-48 ore, documentare la causa principale e le azioni da intraprendere.
L’obiettivo non è solo risolvere l’incidente ma garantire che lo stesso incidente non possa ripetersi.