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
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
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

# Cheat sheet di Docker e Kubernetes
Un riferimento pratico per containerizzare le applicazioni con Docker e orchestrarle con Kubernetes. Si presuppone una familiarità di base con la riga di comando.
---

## Fondamenti di Docker
| Concetto | Descrizione |
|---------|-----|
| **Immagine** | Modello di sola lettura con codice app + dipendenze + librerie del sistema operativo |
| **Contenitore** | Istanza in esecuzione di un'immagine; processo isolato |
| **Dockerfile** | Ricetta per costruire un'immagine |
| **Registro** | Archiviazione per immagini (Docker Hub, ECR, GCR, GHCR) |
| **Volume** | Archiviazione persistente che sopravvive al riavvio del contenitore |
| **Rete** | Contenitori di connessione di rete virtuale |
---

## Comandi essenziali di Docker
### Immagini
| Comando | Descrizione |
|---------|-----|
| `docker build -t myapp:1.0 .`| Crea un'immagine da un Dockerfile |
| `docker images`| Elenca le immagini locali |
| `docker pull nginx:latest`| Estrarre un'immagine da un registro |
| `docker push myrepo/myapp:1.0`| Invia un'immagine a un registro |
| `docker rmi myapp:1.0`| Rimuovere un'immagine locale |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| Contrassegna un'immagine per un registro |
| `docker image prune -a`| Rimuovi tutte le immagini inutilizzate |
### Contenitori
| Comando | Descrizione |
|---------|-----|
| `docker run -d -p 8080:80 nginx`| Esegui un contenitore in background, mappa la porta 8080→80 |
| `docker run -it ubuntu bash`| Esegui in modo interattivo con una shell |
| `docker run --name web -e DB_HOST=db nginx`| Imposta il nome del contenitore e la variabile di ambiente |
| `docker ps`| Elenca i contenitori in esecuzione |
| `docker ps -a`| Elenca tutti i contenitori (compresi quelli interrotti) |
| `docker stop web`| Interrompere un contenitore in esecuzione |
| `docker start web`| Avvia un contenitore arrestato |
| `docker rm web`| Rimuovere un contenitore bloccato |
| `docker exec -it web bash`| Aprire una shell all'interno di un contenitore in esecuzione |
| `docker logs -f web`| Segui i log del contenitore |
| `docker inspect web`| Metadati dettagliati del contenitore (JSON) |
| `docker stats`| Utilizzo delle risorse in tempo reale per tutti i contenitori |
### Ripulire
| Comando | Descrizione |
|---------|-----|
| `docker system prune -a`| Rimuovi tutti i contenitori, le immagini, le reti e la cache di build inutilizzati |
| `docker volume prune`| Rimuovere tutti i volumi inutilizzati |
| `docker container prune`| Rimuovere tutti i contenitori arrestati |
---

## Riferimento al Dockerfile
### Istruzioni comuni
| Istruzioni | Scopo | Esempio |
|-------------|---------|---------|
| `FROM`| Immagine di base | `FROM python:3.12-slim`|
| `WORKDIR`| Imposta la directory di lavoro all'interno dell'immagine | `WORKDIR /app`|
| `COPY`| Copia i file dall'host nell'immagine | `COPY requirements.txt .`|
| `ADD`| Come COPY, ma estrae anche i tar e supporta gli URL | `ADD app.tar.gz /app/`|
| `RUN`| Esegui un comando durante la compilazione | `RUN pip install -r requirements.txt`|
| `CMD`| Comando predefinito all'avvio del contenitore | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| Comando fisso; CMD diventa argomenti | `ENTRYPOINT ["python"]`|
| `ENV`| Imposta la variabile di ambiente | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| Documentare su quale porta è in ascolto l'app | `EXPOSE 8000`|
| `ARG`| Variabile in fase di compilazione | `ARG VERSION=1.0`|
| `USER`| Passa all'utente non root | `USER appuser`|
| `HEALTHCHECK`| Definire un comando di controllo dello stato | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| Crea un punto di montaggio | `VOLUME /data`|
### Migliori pratiche
| Pratica | Perché |
|----------|-----|
| Utilizza immagini slim/base | Immagini più piccole = tiri più veloci, superficie di attacco più piccola |
| Combina i comandi RUN con`&&`| Riduce i livelli dell'immagine |
| Copiare prima i file delle dipendenze, quindi codificare | Sfrutta la cache di build di Docker |
| Utilizzare`.dockerignore`| Escludi`node_modules`,`.git`,`__pycache__`|
| Esegui come utente non root | Migliori pratiche di sicurezza |
| Utilizza build a più fasi | Compilazione e runtime separati; immagine finale più piccola |
| Versioni immagine base pin | Build riproducibili (`python:3.12.1-slim`, non `python:latest`) |
### Esempio di creazione in più fasi
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

## Docker Componi
Docker Compose definisce applicazioni multi-contenitore in un singolo file YAML.
### Comandi chiave
| Comando | Descrizione |
|---------|-----|
| `docker compose up -d`| Avvia tutti i servizi in background |
| `docker compose down`| Arrestare e rimuovere contenitori, reti |
| `docker compose down -v`| Rimuovere anche i volumi |
| `docker compose logs -f`| Segui i log di tutti i servizi |
| `docker compose ps`| Elenco dei servizi in esecuzione |
| `docker compose build`| Ricostruisci immagini |
| `docker compose exec web bash`| Esegui il comando in un servizio in esecuzione |
| `docker compose pull`| Estrai le ultime immagini |
### Esempio di file di composizione
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

## Architettura Kubernetes
| Componente | Ruolo |
|-----------|------|
| **Gruppo** | Un insieme di nodi (macchine) che eseguono applicazioni containerizzate |
| **Piano di controllo** | Server API, scheduler, gestore controller, etcd (stato del cluster) |
| **Nodo** | Una macchina lavoratore (VM o fisica) che esegue i pod |
| **Pod** | Unità più piccola; uno o più contenitori strettamente accoppiati |
| **Distribuzione** | Gestisce le repliche di un pod; gestisce gli aggiornamenti continui |
| **Servizio** | Endpoint di rete stabile per un set di pod |
| **Ingresso** | Instradamento HTTP dall'esterno del cluster ai servizi |
| **ConfigMappa** | Dati di configurazione non segreti |
| **Segreto** | Dati sensibili (codifica base64) |
| **Spazio dei nomi** | Isolamento logico all'interno di un cluster |
| **Volume persistente (PV)** | Risorsa di archiviazione a livello di cluster |
| **PersistentVolumeClaim (PVC)** | Richiesta di archiviazione da parte di un pod |
---

## Comandi kubectl
### Informazioni sul cluster
| Comando | Descrizione |
|---------|-----|
| `kubectl cluster-info`| Dettagli dell'endpoint del cluster |
| `kubectl get nodes`| Elenca tutti i nodi |
| `kubectl get namespaces`| Elenca gli spazi dei nomi |
| `kubectl config current-context`| Mostra il contesto attuale del cluster |
| `kubectl config use-context prod`| Cambia contesto |
### Carichi di lavoro
| Comando | Descrizione |
|---------|-----|
| `kubectl get pods`| Elenca i pod nello spazio dei nomi corrente |
| `kubectl get pods -A`| Elenca i pod in tutti gli spazi dei nomi |
| `kubectl get deployments`| Elenco distribuzioni |
| `kubectl get services`| Elenco servizi |
| `kubectl get ingress`| Elenca le risorse in ingresso |
| `kubectl describe pod <name>`| Informazioni dettagliate sul pod (eventi, stato, specifiche) |
| `kubectl logs <pod>`| Visualizza i log dei pod |
| `kubectl logs -f <pod>`| Segui i log dei pod |
| `kubectl logs <pod> -c <container>`| Log da un contenitore specifico in un pod a più contenitori |
| `kubectl exec -it <pod> -- bash`| Sgusciare in un baccello |
| `kubectl delete pod <name>`| Elimina un pod (verrà ricreato dal suo controller) |
| `kubectl rollout status deployment/<name>`| Controlla lo stato di avanzamento dell'implementazione |
| `kubectl rollout undo deployment/<name>`| Torna alla versione precedente |
### Applicazione della configurazione
| Comando | Descrizione |
|---------|-----|
| `kubectl apply -f deployment.yaml`| Applicare un manifest YAML |
| `kubectl apply -f ./dir/`| Applica tutti i file YAML in una directory |
| `kubectl delete -f deployment.yaml`| Elimina le risorse definite in un file YAML |
| `kubectl scale deployment/web --replicas=5`| Scalare una distribuzione |
| `kubectl set image deployment/web web=myapp:2.0`| Aggiorna l'immagine del contenitore |
---

## Manifesti Kubernetes comuni
### Distribuzione
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

### Servizio
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

### Ingresso
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

## Nozioni di base sul timone
Helm è il gestore di pacchetti per Kubernetes. Raggruppa le risorse Kubernetes in grafici riutilizzabili.
| Comando | Descrizione |
|---------|-----|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| Aggiungi un repository di grafici |
| `helm repo update`| Aggiorna l'indice della carta locale |
| `helm search repo nginx`| Cerca un grafico |
| `helm install my-release bitnami/nginx`| Installa un grafico |
| `helm install my-release bitnami/nginx --set replicaCount=3`| Installa con valori personalizzati |
| `helm install my-release bitnami/nginx -f values.yaml`| Installare con un file di valori |
| `helm list`| Elenco versioni installate |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| Aggiorna una versione |
| `helm rollback my-release 1`| Tornare a una revisione precedente |
| `helm uninstall my-release`| Disinstallare una versione |
| `helm status my-release`| Mostra stato di rilascio |
---

## Guida rapida per la risoluzione dei problemi
| Problema | Comandi da provare |
|---------|----------------|
| Il pod non si avvia | `kubectl describe pod <name>`→ controlla Eventi |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ scopri perché si è bloccato |
| Errore di estrazione dell'immagine | Controlla il nome dell'immagine, il tag e le credenziali del registro |
| Servizio non raggiungibile | `kubectl get endpoints <service>`→ i pod sono selezionati? |
| OOMUcciso | Aumenta i limiti di memoria o ottimizza l'utilizzo della memoria delle app |
| Pod in sospeso | `kubectl describe pod`→ controlla le risorse del nodo, le incompatibilità, l'affinità |
| Problemi DNS | `kubectl exec <pod> -- nslookup kubernetes.default`|