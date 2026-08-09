---
# Metadata
title: "DevOps and CI/CD"
description: "CI/CD pipelines, Docker, Kubernetes, Terraform, GitOps"
category: "Coding and Technology"
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
    date: "2026-08-05"
    author: "AI Model Training Team"
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
# DevOps und CI/CD
DevOps ist die Kombination aus kultureller Philosophie, Praktiken und Tools, die es Teams ermöglicht, Software schneller und zuverlässiger bereitzustellen. Es durchbricht die Mauer zwischen Entwicklern (die Änderungen liefern möchten) und Betrieben (die Stabilität wünschen). CI/CD – Continuous Integration und Continuous Delivery – ist das Automatisierungsrückgrat, das dies ermöglicht.
---

## CI/CD-Pipelines
### Was CI/CD eigentlich bedeutet
| Begriff | Was es tut |
|------|-------------|
| **Kontinuierliche Integration (CI)** | Entwickler führen häufig Code zusammen; Jede Zusammenführung löst automatisierte Builds und Tests aus |
| **Kontinuierliche Lieferung (CD)** | Code befindet sich immer in einem bereitstellbaren Zustand; Die Freigabe für die Produktion ist eine manuelle Entscheidung |
| **Kontinuierliche Bereitstellung** | Jede Änderung, die die Tests besteht, geht automatisch in die Produktion – kein manuelles Gate |
### Typische Pipeline-Stufen
| Bühne | Was passiert | Werkzeuge |
|-------|-------------|-------|
| **Quelle** | Entwickler verschiebt Code an Git | GitHub, GitLab, Bitbucket |
| **Bauen** | Code kompilieren, Abhängigkeiten installieren | Maven, Gradle, npm, pip |
| **Test** | Laufeinheit, Integration, Flusenprüfungen | Scherz, Pytest, JUnit |
| **Paket** | Docker-Image oder Artefakt erstellen | Docker, Buildpacks |
| **Bereitstellen (Staging)** | In der Staging-Umgebung bereitstellen | Kubernetes, ECS, VM |
| **Test (Staging)** | Integrationstests, Rauchtests | Selen, Postbote |
| **Bereitstellen (Produktion)** | Freigabe für die Produktion | Blaugrün, Kanarienvogel, rollend |
| **Überwachen** | Beobachten Sie Zustand, Fehler und Leistung | Prometheus, Grafana, Datadog |
### CI/CD-Tools im Vergleich
| Werkzeug | Geben Sie | ein Stärke |
|------|------|----------|
| **GitHub-Aktionen** | Cloud CI/CD | Tief integriert mit GitHub; YAML-Workflows |
| **GitLab CI** | Integriertes CI/CD | Eine einzige Plattform für Repo + Pipeline |
| **Jenkins** | Selbstgehostetes CI/CD | Hochgradig konfigurierbar; riesiges Plugin-Ökosystem |
| **KreisCI** | Cloud CI/CD | Schnell; gut für containerisierte Arbeitsabläufe |
| **ArgoCD** | GitOps für Kubernetes | Deklarative, Git-gesteuerte Bereitstellungen |
---

## Docker und Container
### Warum Container?
Vor Containern war das klassische Problem: „Es funktioniert auf meinem Rechner.“ Container lösen dieses Problem, indem sie eine Anwendung mit all ihren Abhängigkeiten – Bibliotheken, Laufzeit, Konfiguration – in einer einzigen, tragbaren Einheit packen, die überall identisch ausgeführt wird.
### Docker Essentials
| Konzept | Beschreibung |
|---------|-------------|
| **Bild** | Schreibgeschützte Vorlage mit App + Abhängigkeiten |
| **Container** | Laufende Instanz eines Bildes |
| **Dockerfile** | Rezept zum Erstellen eines Images |
| **Registrierung** | Speicher für Bilder (Docker Hub, ECR, GCR) |
| **Volumen** | Persistenter Speicher, der Container-Neustarts übersteht |
| **Netzwerk** | Isolierte Netzwerkschicht für Container |
### Best Practices für Dockerfile
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

Wichtige Vorgehensweisen: Slim/Alpine-Basisimages verwenden, als Nicht-Root ausführen, Layer-Caching nutzen,`.dockerignore`verwenden, Images auf Schwachstellen scannen (`trivy`,`docker scan`) und Ressourcenlimits festlegen.
### Docker Compose
Zum gleichzeitigen Ausführen mehrerer Container (App + Datenbank + Cache):
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
Kubernetes ist der branchenübliche Container-Orchestrator. Es verwaltet die Bereitstellung, Skalierung und den Betrieb von Containeranwendungen.
### Kernarchitektur
| Komponente | Rolle |
|-----------|------|
| **Kontrollebene** | Verwaltet den Cluster (API-Server, Scheduler, etcd, Controller-Manager) |
| **Knoten** | Arbeitsmaschine (VM oder physisch), die Container ausführt |
| **Pod** | Kleinste einsetzbare Einheit; ein oder mehrere Container, die das Netzwerk gemeinsam nutzen |
| **Service** | Stabiler Netzwerkendpunkt, der den Datenverkehr an Pods weiterleitet |
| **Bereitstellung** | Deklarative Definition des gewünschten Pod-Status (Replikate, Bild usw.) |
| **Eingang** | HTTP-Routing-Regeln für externen Datenverkehr |
| **ConfigMap / Secret** | In Pods injizierte Konfigurations- und vertrauliche Daten |
### Wichtige kubectl-Befehle
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
Helm ist der Paketmanager für Kubernetes. Ein **Diagramm** ist ein Bündel vorkonfigurierter Kubernetes-Ressourcen. Betrachten Sie es als`apt`oder`brew`für K8s.
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## Infrastruktur als Code (IaC)
IaC behandelt die Infrastrukturkonfiguration genauso wie Anwendungscode: versioniert, getestet und über Pipelines bereitgestellt.
### Terraform vs. Ansible
| Werkzeug | Geben Sie | ein Ansatz | Am besten für |
|------|------|----------|----------|
| **Terraform** | Bereitstellung | Deklarativ (HCL); staatsbasiert | Erstellen von Cloud-Ressourcen (VPCs, VMs, Datenbanken) |
| **Ansible** | Konfiguration | Deklarativ (YAML); agentenlos | Server konfigurieren, Software installieren |
| **Pulumi** | Bereitstellung | Imperativ (Python, Go, TS) | Teams, die echte Programmiersprachen bevorzugen |
| **CloudFormation** | Bereitstellung | Deklarativ (YAML/JSON); AWS-nativ | Nur AWS-Infrastruktur |
### Terraform-Beispiel
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

Best Practices: Verwenden Sie Module für die Wiederverwendbarkeit, speichern Sie den Status remote (S3 + DynamoDB zum Sperren), kodieren Sie niemals Geheimnisse fest und führen Sie für alles eine Versionskontrolle durch.
---

## Überwachung und Beobachtbarkeit
### Die drei Säulen
| Säule | Was es Ihnen sagt | Werkzeuge |
|--------|----|-------|
| **Metriken** | Numerische Messungen im Zeitverlauf (CPU, Anforderungsrate, Fehlerrate) | Prometheus, CloudWatch, Datadog |
| **Protokolle** | Diskrete Ereignisse mit Kontext (Fehler, Anfragen, Zustandsänderungen) | ELK Stack, Loki, CloudWatch Logs |
| **Spuren** | End-to-End-Anfragereise über Dienste hinweg | Jaeger, Röntgen, Zipkin |
### Prometheus + Grafana-Stapel
Der standardmäßige Open-Source-Überwachungsstapel:
| Komponente | Rolle |
|-----------|------|
| **Prometheus** | Zeitreihendatenbank; ruft Metriken von Diensten ab |
| **Grafana** | Visualisierung und Dashboards |
| **Alertmanager** | Leitet Benachrichtigungen an Slack, PagerDuty und E-Mail weiter
| **Knotenexporteur** | Macht Metriken auf Systemebene verfügbar (CPU, RAM, Festplatte) |
| **Blackbox-Exporteur** | Prüft Endpunkte (HTTP, TCP, ICMP) |
### Wichtige Kennzahlen zum Verfolgen
| Kategorie | Metriken |
|----------|---------|
| **Infrastruktur** | CPU, RAM, Festplattennutzung, Netzwerk-E/A |
| **Bewerbung** | Anforderungsrate, Latenz (p50, p95, p99), Fehlerrate |
| **Datenbank** | Anzahl der Abfragen, langsame Abfragen, Nutzung des Verbindungspools |
| **Geschäft** | Anmeldungen, Conversions, Umsatz |
---

## Bereitstellungsstrategien
| Strategie | Wie es funktioniert | Risiko | Rollback |
|----------|-------------|------|----------|
| **Laufendes Update** | Alte Instanzen nach und nach durch neue ersetzen | Einige Benutzer verwenden die alte, andere die neue Version | Zum vorherigen Bild zurückkehren |
| **Blau-Grün** | Führen Sie zwei identische Umgebungen aus; Verkehr wechseln | Doppelte Infrastrukturkosten während des Übergangs | Sofortiges Zurückschalten |
| **Kanarienvogel** | Leiten Sie einen kleinen Prozentsatz des Datenverkehrs an die neue Version weiter. schrittweise erhöhen | Komplexes Verkehrsmanagement | Leiten Sie den Verkehr zurück zum Stall |
| **Feature-Flags** | Code bereitstellen, aber Funktionen hinter Schaltern ausblenden | Codekomplexität aus bedingter Logik | Ausschalten |
---

## GitOps
GitOps führt IaC zu seinem logischen Schluss: Das Git-Repository ist die einzige Quelle der Wahrheit für den gewünschten Zustand Ihrer Infrastruktur und Anwendungen.
| Prinzip | Beschreibung |
|-----------|-------------|
| **Deklarativ** | Alles als Code beschrieben (YAML, HCL) |
| **Versioniert** | Git ist die Quelle der Wahrheit |
| **Automatisiert** | Werkzeuge gleichen Soll-Zustand kontinuierlich mit Ist-Zustand ab |
| **Überprüfbar** | Jede Änderung ist ein Git-Commit |
**ArgoCD** und **Flux** sind die führenden GitOps-Tools für Kubernetes. Sie übertragen eine Änderung an Ihr Git-Repository und das Tool stellt sie automatisch im Cluster bereit.
---

## Reaktion auf Vorfälle
Wenn um 3 Uhr morgens etwas kaputt geht:
1. **Bestätigen** Sie die Warnung.
2. **Umfang beurteilen**: Welche Dienste, Benutzer und Daten sind betroffen?
3. **Identifizieren** Sie die Grundursache – überprüfen Sie Protokolle, Metriken und aktuelle Bereitstellungen.
4. **Wenn möglich eindämmen** – Leistungsschalter, Feature-Flags, Verkehrsverlagerung.
5. **Fix** – Rollback oder Patch-Forward.
6. **Kommunizieren** – Stakeholder und Benutzer aktualisieren (Statusseite).
7. **Post-Mortem** – innerhalb von 24–48 Stunden Grundursache und Maßnahmen dokumentieren.
Das Ziel besteht nicht nur darin, den Vorfall zu beheben, sondern auch sicherzustellen, dass derselbe Vorfall nicht noch einmal passieren kann.