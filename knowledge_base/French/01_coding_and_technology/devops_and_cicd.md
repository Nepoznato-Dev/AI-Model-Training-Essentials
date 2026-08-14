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
# DevOps et CI/CD
DevOps est la combinaison d'une philosophie culturelle, de pratiques et d'outils qui permet aux équipes de fournir des logiciels plus rapidement et de manière plus fiable. Cela brise le mur entre les développeurs (qui souhaitent apporter des modifications) et les opérations (qui souhaitent de la stabilité). CI/CD – Intégration continue et livraison continue – est l'épine dorsale de l'automatisation qui rend cela possible.
---

## Pipelines CI/CD
### Ce que signifie réellement CI/CD
| Terme | Ce qu'il fait |
|------|-------------|
| **Intégration continue (CI)** | Les développeurs fusionnent fréquemment le code ; chaque fusion déclenche des builds et des tests automatisés |
| **Livraison continue (CD)** | Le code est toujours dans un état déployable ; la mise en production est une décision manuelle |
| **Déploiement continu** | Chaque modification qui réussit les tests est automatiquement mise en production – pas de portail manuel |
### Étapes typiques d'un pipeline
| Scène | Que se passe-t-il | Outils |
|-------|-------------|-------|
| **Source** | Le développeur envoie le code vers Git | GitHub, GitLab, Bitbucket |
| **Construire** | Compiler le code, installer les dépendances | Maven, Gradle, npm, pépin |
| **Tester** | Unité d'exécution, intégration, contrôle des peluches | Blague, pytest, JUnit |
| **Forfait** | Créer une image ou un artefact Docker | Docker, packs de construction |
| **Déployer (stade)** | Déployer dans un environnement de test | Kubernetes, ECS, VM |
| **Test (mise en scène)** | Tests d'intégration, tests de fumée | Sélénium, facteur |
| **Déployer (production)** | Mise en production | Bleu-vert, canari, roulant |
| **Moniteur** | Observer la santé, les erreurs, les performances | Prométhée, Grafana, Datadog |
### Outils CI/CD comparés
| Outil | Tapez | Force |
|------|------|----------|
| **Actions GitHub** | CI/CD cloud | Profondément intégré à GitHub ; Flux de travail YAML |
| **GitLabCI** | CI/CD intégré | Plateforme unique pour repo + pipeline |
| **Jenkins** | CI/CD auto-hébergé | Hautement configurable ; écosystème de plugins massif |
| **CercleCI** | CI/CD cloud | Rapide; bon pour les flux de travail conteneurisés |
| **ArgoCD** | GitOps pour Kubernetes | Déploiements déclaratifs basés sur Git |
---

## Docker et conteneurs
### Pourquoi des conteneurs ?
Avant les conteneurs, le problème classique était « ça fonctionne sur ma machine ». Les conteneurs résolvent ce problème en regroupant une application avec toutes ses dépendances (bibliothèques, runtime, configuration) dans une seule unité portable qui s'exécute de manière identique partout.
### L'essentiel de Docker
| Concepts | Descriptif |
|---------|-------------|
| **Image** | Modèle en lecture seule avec application + dépendances |
| **Conteneur** | Instance en cours d'exécution d'une image |
| **Fichier Docker** | Recette pour construire une image |
| **Registre** | Stockage des images (Docker Hub, ECR, GCR) |
| **Volume** | Stockage persistant qui survit aux redémarrages des conteneurs |
| **Réseau** | Couche réseau isolée pour conteneurs |
### Bonnes pratiques Dockerfile
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

Pratiques clés : utiliser des images de base minces/alpines, exécuter en tant que non-root, tirer parti de la mise en cache des couches, utiliser`.dockerignore`, analyser les images à la recherche de vulnérabilités (`trivy`,`docker scan`) et définir des limites de ressources.
### Docker Composer
Pour exécuter plusieurs conteneurs ensemble (application + base de données + cache) :
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
Kubernetes est l'orchestrateur de conteneurs standard de l'industrie. Il gère le déploiement, la mise à l'échelle et le fonctionnement des applications conteneurisées.
### Architecture de base
| Composant | Rôle |
|---------------|------|
| **Plan de contrôle** | Gère le cluster (serveur API, planificateur, etcd, gestionnaire de contrôleur) |
| **Nœud** | Machine de travail (VM ou physique) qui exécute des conteneurs |
| **Pod** | La plus petite unité déployable ; un ou plusieurs conteneurs partageant le réseau |
| **Service** | Point de terminaison de réseau stable qui achemine le trafic vers les pods |
| **Déploiement** | Définition déclarative de l'état du pod souhaité (répliques, image, etc.) |
| **Entrée** | Règles de routage HTTP pour le trafic externe |
| **ConfigMap / Secret** | Configuration et données sensibles injectées dans les pods |
### Commandes kubectl essentielles
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

### Heaume
Helm est le gestionnaire de packages pour Kubernetes. Un **chart** est un ensemble de ressources Kubernetes préconfigurées. Considérez-le comme`apt`ou`brew`pour les K8.
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## Infrastructure en tant que code (IaC)
IaC traite la configuration de l'infrastructure de la même manière que vous traitez le code d'application : version contrôlée, testée et déployée via des pipelines.
### Terraform contre Ansible
| Outil | Tapez | Approche | Idéal pour |
|------|------|----------|--------------|
| **Terraforme** | Approvisionnement | Déclaratif (HCL); basé sur l'état | Création de ressources cloud (VPC, VM, bases de données) |
| **Ansible** | Configuration | Déclaratif (YAML) ; sans agent | Configuration des serveurs, installation des logiciels |
| **Pulumi** | Approvisionnement | Impératif (Python, Go, TS) | Les équipes qui préfèrent les vrais langages de programmation |
| **CloudFormation** | Approvisionnement | Déclaratif (YAML/JSON) ; Natif AWS | Infrastructure uniquement AWS |
### Exemple de Terraform
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

Meilleures pratiques : utilisez les modules pour la réutilisabilité, stockez l'état à distance (S3 + DynamoDB pour le verrouillage), ne codez jamais en dur les secrets et contrôlez tout en version.
---

## Surveillance et observabilité
### Les trois piliers
| Pilier | Ce qu'il vous dit | Outils |
|--------|--------|-------|
| **Mesures** | Mesures numériques dans le temps (CPU, taux de requêtes, taux d'erreur) | Prometheus, CloudWatch, Datadog |
| **Journaux** | Événements discrets avec contexte (erreurs, demandes, changements d'état) | Pile ELK, Loki, journaux CloudWatch |
| **Traces** | Parcours de demande de bout en bout à travers les services | Jaeger, X-Ray, Zipkin |
### Prométhée + Pile Grafana
La pile de surveillance open source standard :
| Composant | Rôle |
|---------------|------|
| **Prométhée** | Base de données de séries chronologiques ; extrait les métriques des services |
| **Grafana** | Visualisation et tableaux de bord |
| **Gestionnaire d'alertes** | Achemine les alertes vers Slack, PagerDuty, e-mail |
| **Exportateur de nœuds** | Expose les métriques au niveau du système (CPU, RAM, disque) |
| **Exportateur de boîte noire** | Sondes les points de terminaison (HTTP, TCP, ICMP) |
### Indicateurs clés à suivre
| Catégorie | Métriques |
|--------------|---------|
| **Infrastructures** | CPU, RAM, utilisation du disque, E/S réseau |
| **Candidature** | Taux de requêtes, latence (p50, p95, p99), taux d'erreur |
| **Base de données** | Nombre de requêtes, requêtes lentes, utilisation du pool de connexions |
| **Entreprise** | Inscriptions, conversions, revenus |
---

## Stratégies de déploiement
| Stratégie | Comment ça marche | Risque | Restauration |
|--------------|-------------|------|--------------|
| **Mise à jour continue** | Remplacer progressivement les anciennes instances par de nouvelles | Certains utilisateurs sur l'ancienne version, d'autres sur la nouvelle version | Revenir à l'image précédente |
| **Bleu-Vert** | Exécutez deux environnements identiques ; changer de trafic | Coût d'infrastructure double pendant la transition | Retour instantané |
| **Canari** | Acheminer un petit % du trafic vers la nouvelle version ; augmenter progressivement | Gestion complexe du trafic | Acheminer le trafic vers un état stable |
| **Drapeaux de fonctionnalité** | Déployer le code mais masquer les fonctionnalités derrière les bascules | Complexité du code à partir de la logique conditionnelle | Désactiver |
---

##GitOps
GitOps amène IaC à sa conclusion logique : le référentiel Git est la source unique de vérité sur l'état souhaité de votre infrastructure et de vos applications.
| Principe | Descriptif |
|---------------|-------------|
| **Déclaratif** | Tout est décrit sous forme de code (YAML, HCL) |
| ** Versionné ** | Git est la source de la vérité |
| **Automatisé** | Les outils réconcilient en permanence l'état souhaité avec l'état réel |
| **Auditable** | Chaque changement est un commit Git |
**ArgoCD** et **Flux** sont les principaux outils GitOps pour Kubernetes. Vous transmettez une modification à votre dépôt Git et l'outil la déploie automatiquement sur le cluster.
---

## Réponse aux incidents
Quand quelque chose se brise à 3 heures du matin :
1. **Acceptez** l'alerte.
2. **Évaluer la portée** : quels services, utilisateurs et données sont concernés ?
3. **Identifiez** la cause première : vérifiez les journaux, les métriques et les déploiements récents.
4. **Contenir** si possible — disjoncteurs, indicateurs de fonctionnalité, déplacement du trafic.
5. **Correction** — restauration ou transfert de correctif.
6. **Communiquer** — mettre à jour les parties prenantes et les utilisateurs (page d'état).
7. **Post-mortem** — dans les 24 à 48 heures, documentez la cause première et les mesures à prendre.
L’objectif n’est pas seulement de résoudre l’incident, mais aussi de garantir que le même incident ne se reproduise pas.