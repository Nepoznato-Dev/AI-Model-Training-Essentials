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

# Aide-mémoire Docker et Kubernetes
Une référence pratique pour conteneuriser des applications avec Docker et les orchestrer avec Kubernetes. Suppose une connaissance de base de la ligne de commande.
---

## Fondamentaux de Docker
| Concepts | Descriptif |
|---------|-------------|
| **Image** | Modèle en lecture seule avec code d'application + dépendances + bibliothèques de système d'exploitation |
| **Conteneur** | Instance en cours d’exécution d’une image ; processus isolé |
| **Fichier Docker** | Recette pour construire une image |
| **Registre** | Stockage des images (Docker Hub, ECR, GCR, GHCR) |
| **Volume** | Stockage persistant qui survit aux redémarrages des conteneurs |
| **Réseau** | Conteneurs de connexion au réseau virtuel |
---

## Commandes Docker essentielles
### Images
| Commande | Descriptif |
|---------|-------------|
| `docker build -t myapp:1.0 .`| Créer une image à partir d'un Dockerfile |
| `docker images`| Liste des images locales |
| `docker pull nginx:latest`| Extraire une image d'un registre |
| `docker push myrepo/myapp:1.0`| Transférer une image vers un registre |
| `docker rmi myapp:1.0`| Supprimer une image locale |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| Marquer une image pour un registre |
| `docker image prune -a`| Supprimez toutes les images inutilisées |
### Conteneurs
| Commande | Descriptif |
|---------|-------------|
| `docker run -d -p 8080:80 nginx`| Exécutez un conteneur en arrière-plan, mappez le port 8080 → 80 |
| `docker run -it ubuntu bash`| Exécutez de manière interactive avec un shell |
| `docker run --name web -e DB_HOST=db nginx`| Définir le nom du conteneur et la variable d'environnement |
| `docker ps`| Liste des conteneurs en cours d'exécution |
| `docker ps -a`| Lister tous les conteneurs (y compris arrêtés) |
| `docker stop web`| Arrêter un conteneur en cours d'exécution |
| `docker start web`| Démarrer un conteneur arrêté |
| `docker rm web`| Supprimer un conteneur arrêté |
| `docker exec -it web bash`| Ouvrir un shell dans un conteneur en cours d'exécution |
| `docker logs -f web`| Suivre les journaux du conteneur |
| `docker inspect web`| Métadonnées détaillées du conteneur (JSON) |
| `docker stats`| Utilisation des ressources en direct pour tous les conteneurs |
### Nettoyage
| Commande | Descriptif |
|---------|-------------|
| `docker system prune -a`| Supprimez tous les conteneurs, images, réseaux et créer le cache inutilisés |
| `docker volume prune`| Supprimez tous les volumes inutilisés |
| `docker container prune`| Supprimer tous les conteneurs arrêtés |
---

## Référence du fichier Docker
### Instructions communes
| Instructions | Objectif | Exemple |
|-------------|---------|---------|
| `FROM`| Image de base | `FROM python:3.12-slim`|
| `WORKDIR`| Définir le répertoire de travail à l'intérieur de l'image | `WORKDIR /app`|
| `COPY`| Copier les fichiers de l'hôte vers l'image | `COPY requirements.txt .`|
| `ADD`| Comme COPY, mais extrait également les tars et prend en charge les URL | `ADD app.tar.gz /app/`|
| `RUN`| Exécuter une commande pendant la construction | `RUN pip install -r requirements.txt`|
| `CMD`| Commande par défaut au démarrage du conteneur | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| Commande fixe ; CMD devient un argument | `ENTRYPOINT ["python"]`|
| `ENV`| Définir la variable d'environnement | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| Documenter le port sur lequel l'application écoute | `EXPOSE 8000`|
| `ARG`| Variable de temps de construction | `ARG VERSION=1.0`|
| `USER`| Passer à un utilisateur non root | `USER appuser`|
| `HEALTHCHECK`| Définir une commande de vérification de l'état | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| Créer un point de montage | `VOLUME /data`|
### Bonnes pratiques
| Pratique | Pourquoi |
|----------|-----|
| Utiliser des images minces/de base | Images plus petites = tirages plus rapides, surface d'attaque plus petite |
| Combinez les commandes RUN avec`&&`| Réduit les calques d'image |
| Copiez d'abord les fichiers de dépendance, puis codez | Exploite le cache de build de Docker |
| Utiliser`.dockerignore`| Exclure`node_modules`,`.git`,`__pycache__`|
| Exécuter en tant qu'utilisateur non root | Meilleures pratiques de sécurité |
| Utiliser des builds en plusieurs étapes | Séparez la construction et l'exécution ; image finale plus petite |
| Versions de l'image de base des broches | Constructions reproductibles (`python:3.12.1-slim`, pas`python:latest`) |
### Exemple de construction en plusieurs étapes
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

## Docker Composer
Docker Compose définit les applications multi-conteneurs dans un seul fichier YAML.
### Raccourcis clavier
| Commande | Descriptif |
|---------|-------------|
| `docker compose up -d`| Démarrer tous les services en arrière-plan |
| `docker compose down`| Arrêter et supprimer les conteneurs, les réseaux |
| `docker compose down -v`| Supprimez également les volumes |
| `docker compose logs -f`| Suivre les journaux de tous les services |
| `docker compose ps`| Liste des services en cours d'exécution |
| `docker compose build`| Reconstruire des images |
| `docker compose exec web bash`| Exécuter une commande dans un service en cours d'exécution |
| `docker compose pull`| Extraire les dernières images |
### Exemple de fichier de composition
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

## Architecture Kubernetes
| Composant | Rôle |
|---------------|------|
| **Grappe** | Un ensemble de nœuds (machines) exécutant des applications conteneurisées |
| **Plan de contrôle** | Serveur API, planificateur, gestionnaire de contrôleur, etcd (état du cluster) |
| **Nœud** | Une machine de travail (VM ou physique) qui exécute des pods |
| **Pod** | La plus petite unité ; un ou plusieurs conteneurs étroitement couplés |
| **Déploiement** | Gère les répliques d'un pod ; gère les mises à jour progressives |
| **Service** | Point de terminaison réseau stable pour un ensemble de pods |
| **Entrée** | Routage HTTP depuis l'extérieur du cluster vers les services |
| **ConfigMap** | Données de configuration non secrètes |
| **Secret** | Données sensibles (codées en base64) |
| **Espace de noms** | Isolation logique au sein d'un cluster |
| **Volume persistant (PV)** | Ressource de stockage au niveau du cluster |
| **Réclamation de volume persistant (PVC)** | Demande de stockage par un pod |
---

## Commandes kubectl
### Informations sur le cluster
| Commande | Descriptif |
|---------|-------------|
| `kubectl cluster-info`| Détails du point de terminaison du cluster |
| `kubectl get nodes`| Lister tous les nœuds |
| `kubectl get namespaces`| Liste des espaces de noms |
| `kubectl config current-context`| Afficher le contexte actuel du cluster |
| `kubectl config use-context prod`| Changer de contexte |
### Charges de travail
| Commande | Descriptif |
|---------|-------------|
| `kubectl get pods`| Répertorier les pods dans l'espace de noms actuel |
| `kubectl get pods -A`| Répertorier les pods dans tous les espaces de noms |
| `kubectl get deployments`| Répertorier les déploiements |
| `kubectl get services`| Liste des services |
| `kubectl get ingress`| Répertorier les ressources d'entrée |
| `kubectl describe pod <name>`| Informations détaillées sur le pod (événements, statut, spécifications) |
| `kubectl logs <pod>`| Afficher les journaux des pods |
| `kubectl logs -f <pod>`| Suivre les journaux des pods |
| `kubectl logs <pod> -c <container>`| Journaux d'un conteneur spécifique dans un pod multi-conteneur |
| `kubectl exec -it <pod> -- bash`| Coquille dans une cosse |
| `kubectl delete pod <name>`| Supprimer un pod (il sera recréé par son contrôleur) |
| `kubectl rollout status deployment/<name>`| Vérifier la progression du déploiement |
| `kubectl rollout undo deployment/<name>`| Revenir à la version précédente |
### Application de la configuration
| Commande | Descriptif |
|---------|-------------|
| `kubectl apply -f deployment.yaml`| Appliquer un manifeste YAML |
| `kubectl apply -f ./dir/`| Appliquer tous les fichiers YAML dans un répertoire |
| `kubectl delete -f deployment.yaml`| Supprimer les ressources définies dans un fichier YAML |
| `kubectl scale deployment/web --replicas=5`| Faire évoluer un déploiement |
| `kubectl set image deployment/web web=myapp:2.0`| Mettre à jour l'image du conteneur |
---

## Manifestes Kubernetes courants
### Déploiement
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

### Entrée
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

## Bases du casque
Helm est le gestionnaire de packages pour Kubernetes. Il regroupe les ressources Kubernetes dans des graphiques réutilisables.
| Commande | Descriptif |
|---------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| Ajouter un référentiel de graphiques |
| `helm repo update`| Mettre à jour l'index des cartes locales |
| `helm search repo nginx`| Rechercher un graphique |
| `helm install my-release bitnami/nginx`| Installer un graphique |
| `helm install my-release bitnami/nginx --set replicaCount=3`| Installer avec des valeurs personnalisées |
| `helm install my-release bitnami/nginx -f values.yaml`| Installer avec un fichier de valeurs |
| `helm list`| Liste des versions installées |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| Mettre à niveau une version |
| `helm rollback my-release 1`| Revenir à une révision précédente |
| `helm uninstall my-release`| Désinstaller une version |
| `helm status my-release`| Afficher l'état de la version |
---

## Référence rapide de dépannage
| Problème | Commandes à essayer |
|---------|----------------|
| Le pod ne démarre pas | `kubectl describe pod <name>`→ vérifier les événements |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ voir pourquoi il s'est écrasé |
| Erreur d'extraction d'image | Vérifier le nom de l'image, la balise et les informations d'identification du registre |
| Service non joignable | `kubectl get endpoints <service>`→ les pods sont-ils sélectionnés ? |
| OOMTué | Augmentez les limites de mémoire ou optimisez l'utilisation de la mémoire des applications |
| Pods en attente | `kubectl describe pod`→ vérifier les ressources du nœud, les teintes, l'affinité |
| Problèmes DNS | `kubectl exec <pod> -- nslookup kubernetes.default`|