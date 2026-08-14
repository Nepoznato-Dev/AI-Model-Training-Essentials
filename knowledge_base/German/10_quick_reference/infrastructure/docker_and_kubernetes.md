---
# Metadata
title: "Docker and Kubernetes Cheat Sheet"
description: "Docker, Docker Compose, Kubernetes, Helm cheat sheet"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [docker, kubernetes, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "15 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Docker- und Kubernetes-Spickzettel
Eine praktische Referenz für die Containerisierung von Anwendungen mit Docker und deren Orchestrierung mit Kubernetes. Setzt grundlegende Kenntnisse der Befehlszeile voraus.
---

## Docker-Grundlagen
| Konzept | Beschreibung |
|---------|-------------|
| **Bild** | Schreibgeschützte Vorlage mit App-Code + Abhängigkeiten + Betriebssystembibliotheken |
| **Container** | Laufende Instanz eines Bildes; isolierter Prozess |
| **Docker-Datei** | Rezept zum Erstellen eines Images |
| **Registrierung** | Speicher für Bilder (Docker Hub, ECR, GCR, GHCR) |
| **Volumen** | Persistenter Speicher, der Container-Neustarts übersteht |
| **Netzwerk** | Virtuelles Netzwerk, das Container verbindet |
---

## Wichtige Docker-Befehle
### Bilder
| Befehl | Beschreibung |
|---------|-------------|
| `docker build -t myapp:1.0 .`| Erstellen Sie ein Image aus einer Docker-Datei |
| `docker images`| Lokale Bilder auflisten |
| `docker pull nginx:latest`| Ein Image aus einer Registrierung abrufen |
| `docker push myrepo/myapp:1.0`| Ein Bild in eine Registrierung übertragen |
| `docker rmi myapp:1.0`| Ein lokales Image entfernen |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| Markieren Sie ein Bild für eine Registrierung |
| `docker image prune -a`| Alle nicht verwendeten Bilder entfernen |
### Container
| Befehl | Beschreibung |
|---------|-------------|
| `docker run -d -p 8080:80 nginx`| Führen Sie einen Container im Hintergrund aus und ordnen Sie Port 8080→80 | zu
| `docker run -it ubuntu bash`| Interaktiv mit einer Shell ausführen |
| `docker run --name web -e DB_HOST=db nginx`| Containernamen und Umgebungsvariable festlegen |
| `docker ps`| Laufende Container auflisten |
| `docker ps -a`| Alle Container auflisten (einschließlich gestoppter) |
| `docker stop web`| Stoppen Sie einen laufenden Container |
| `docker start web`| Starten Sie einen gestoppten Container |
| `docker rm web`| Einen angehaltenen Container entfernen |
| `docker exec -it web bash`| Öffnen Sie eine Shell in einem laufenden Container |
| `docker logs -f web`| Containerprotokolle verfolgen |
| `docker inspect web`| Detaillierte Container-Metadaten (JSON) |
| `docker stats`| Live-Ressourcennutzung für alle Container |
### Aufräumen
| Befehl | Beschreibung |
|---------|-------------|
| `docker system prune -a`| Entfernen Sie alle nicht verwendeten Container, Bilder, Netzwerke und den Build-Cache |
| `docker volume prune`| Alle nicht verwendeten Volumes entfernen |
| `docker container prune`| Alle gestoppten Container entfernen |
---

## Dockerfile-Referenz
### Allgemeine Anweisungen
| Anleitung | Zweck | Beispiel |
|-------------|---------|---------|
| `FROM`| Basisbild | `FROM python:3.12-slim`|
| `WORKDIR`| Arbeitsverzeichnis im Bild festlegen | `WORKDIR /app`|
| `COPY`| Dateien vom Host in das Image kopieren | `COPY requirements.txt .`|
| `ADD`| Wie COPY, extrahiert aber auch TARs und unterstützt URLs | `ADD app.tar.gz /app/`|
| `RUN`| Führen Sie während des Buildvorgangs einen Befehl aus | `RUN pip install -r requirements.txt`|
| `CMD`| Standardbefehl beim Containerstart | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| Fester Befehl; CMD wird zu Argumenten | `ENTRYPOINT ["python"]`|
| `ENV`| Umgebungsvariable festlegen | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| Dokumentieren Sie, auf welchem ​​Port die App lauscht | `EXPOSE 8000`|
| `ARG`| Variable zur Erstellungszeit | `ARG VERSION=1.0`|
| `USER`| Zum Nicht-Root-Benutzer wechseln | `USER appuser`|
| `HEALTHCHECK`| Definieren Sie einen Befehl zur Integritätsprüfung | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| Erstellen Sie einen Mount-Punkt | `VOLUME /data`|
### Best Practices
| Üben | Warum |
|----------|-----|
| Verwenden Sie schlanke/Basisbilder | Kleinere Bilder = schnellere Pulls, kleinere Angriffsfläche |
| Kombinieren Sie RUN-Befehle mit`&&`| Reduziert Bildebenen |
| Kopieren Sie zuerst die Abhängigkeitsdateien und dann den Code | Nutzt den Build-Cache von Docker |
| Verwenden Sie`.dockerignore`|`node_modules`,`.git`,`__pycache__`ausschließen |
| Als Nicht-Root-Benutzer ausführen | Best Practice für Sicherheit |
| Mehrstufige Builds verwenden | Separate Build- und Laufzeitumgebung; kleineres Endbild |
| Pin-Basisbildversionen | Reproduzierbare Builds (`python:3.12.1-slim`, nicht `python:latest`) |
### Beispiel für einen mehrstufigen Build
```dockerfile
# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

---

## Docker Compose
Docker Compose definiert Multi-Container-Anwendungen in einer einzigen YAML-Datei.
### Tastenbefehle
| Befehl | Beschreibung |
|---------|-------------|
| `docker compose up -d`| Alle Dienste im Hintergrund starten |
| `docker compose down`| Stoppen und entfernen Sie Container und Netzwerke |
| `docker compose down -v`| Entfernen Sie auch Volumes |
| `docker compose logs -f`| Verfolgen Sie die Protokolle aller Dienste |
| `docker compose ps`| Laufende Dienste auflisten |
| `docker compose build`| Bilder neu erstellen |
| `docker compose exec web bash`| Befehl in einem laufenden Dienst ausführen |
| `docker compose pull`| Neueste Bilder abrufen |
### Beispiel für eine Compose-Datei
```yaml
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/mydb
      - REDIS_URL=redis://cache:6379
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 5s
      timeout: 5s
      retries: 5

  cache:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  pgdata:
```

---

## Kubernetes-Architektur
| Komponente | Rolle |
|-----------|------|
| **Cluster** | Eine Reihe von Knoten (Maschinen), auf denen Containeranwendungen ausgeführt werden |
| **Kontrollebene** | API-Server, Scheduler, Controller-Manager usw. (Clusterstatus) |
| **Knoten** | Eine Arbeitsmaschine (VM oder physisch), die Pods | ausführt
| **Pod** | Kleinste Einheit; ein oder mehrere eng verbundene Behälter |
| **Bereitstellung** | Verwaltet Replikate eines Pods; kümmert sich um fortlaufende Updates |
| **Service** | Stabiler Netzwerkendpunkt für eine Reihe von Pods |
| **Eingang** | HTTP-Routing von außerhalb des Clusters zu Diensten |
| **ConfigMap** | Nicht geheime Konfigurationsdaten |
| **Geheimnis** | Sensible Daten (base64-kodiert) |
| **Namensraum** | Logische Isolation innerhalb eines Clusters |
| **PersistentVolume (PV)** | Speicherressource auf Clusterebene |
| **PersistentVolumeClaim (PVC)** | Antrag auf Lagerung durch einen Pod |
---

## kubectl-Befehle
### Cluster-Info
| Befehl | Beschreibung |
|---------|-------------|
| `kubectl cluster-info`| Details zum Cluster-Endpunkt |
| `kubectl get nodes`| Alle Knoten auflisten |
| `kubectl get namespaces`| Namespaces auflisten |
| `kubectl config current-context`| Aktuellen Clusterkontext anzeigen |
| `kubectl config use-context prod`| Kontext wechseln |
### Arbeitslasten
| Befehl | Beschreibung |
|---------|-------------|
| `kubectl get pods`| Pods im aktuellen Namespace auflisten |
| `kubectl get pods -A`| Pods über alle Namespaces hinweg auflisten |
| `kubectl get deployments`| Bereitstellungen auflisten |
| `kubectl get services`| Dienste auflisten |
| `kubectl get ingress`| Ingress-Ressourcen auflisten |
| `kubectl describe pod <name>`| Detaillierte Pod-Informationen (Ereignisse, Status, Spezifikationen) |
| `kubectl logs <pod>`| Pod-Protokolle anzeigen |
| `kubectl logs -f <pod>`| Folgen Sie den Pod-Protokollen |
| `kubectl logs <pod> -c <container>`| Protokolle aus einem bestimmten Container in einem Multi-Container-Pod |
| `kubectl exec -it <pod> -- bash`| Schale in eine Schote |
| `kubectl delete pod <name>`| Einen Pod löschen (er wird von seinem Controller neu erstellt) |
| `kubectl rollout status deployment/<name>`| Rollout-Fortschritt prüfen |
| `kubectl rollout undo deployment/<name>`| Rollback zur vorherigen Version |
### Konfiguration anwenden
| Befehl | Beschreibung |
|---------|-------------|
| `kubectl apply -f deployment.yaml`| Wenden Sie ein YAML-Manifest an |
| `kubectl apply -f ./dir/`| Alle YAML-Dateien in einem Verzeichnis anwenden |
| `kubectl delete -f deployment.yaml`| In einer YAML-Datei definierte Ressourcen löschen |
| `kubectl scale deployment/web --replicas=5`| Skalieren Sie eine Bereitstellung |
| `kubectl set image deployment/web web=myapp:2.0`| Container-Image aktualisieren |
---

## Gemeinsame Kubernetes-Manifeste
### Bereitstellung
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  labels:
    app: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: myapp:1.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 15
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

### Service
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP    # Internal only
  # type: LoadBalancer  # External (cloud provider)
  # type: NodePort      # External via node IP + port
```

### Eindringung
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web
            port:
              number: 80
```

---

## Helm-Grundlagen
Helm ist der Paketmanager für Kubernetes. Es verpackt Kubernetes-Ressourcen in wiederverwendbare Diagramme.
| Befehl | Beschreibung |
|---------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| Diagramm-Repository hinzufügen |
| `helm repo update`| Lokalen Diagrammindex aktualisieren |
| `helm search repo nginx`| Nach einem Diagramm suchen |
| `helm install my-release bitnami/nginx`| Installieren Sie ein Diagramm |
| `helm install my-release bitnami/nginx --set replicaCount=3`| Mit benutzerdefinierten Werten installieren |
| `helm install my-release bitnami/nginx -f values.yaml`| Mit einer Wertedatei | installieren
| `helm list`| Installierte Versionen auflisten |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| Ein Release aktualisieren |
| `helm rollback my-release 1`| Rollback zu einer früheren Revision |
| `helm uninstall my-release`| Eine Version deinstallieren |
| `helm status my-release`| Veröffentlichungsstatus anzeigen |
---

## Kurzreferenz zur Fehlerbehebung
| Problem | Befehle zum Ausprobieren |
|---------|----------------|
| Pod startet nicht | `kubectl describe pod <name>`→ Ereignisse prüfen |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ Sehen Sie, warum es abgestürzt ist |
| Bild-Pull-Fehler | Überprüfen Sie den Bildnamen, das Tag und die Registrierungsdaten |
| Dienst nicht erreichbar | `kubectl get endpoints <service>`→ Sind Pods ausgewählt? |
| OOMKilled | Speicherlimits erhöhen oder App-Speichernutzung optimieren |
| Ausstehende Pods | `kubectl describe pod`→ Knotenressourcen, Taints, Affinität prüfen |
| DNS-Probleme | `kubectl exec <pod> -- nslookup kubernetes.default`|