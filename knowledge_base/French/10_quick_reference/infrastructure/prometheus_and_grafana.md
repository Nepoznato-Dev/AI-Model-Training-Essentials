<!--
---
# Metadata
title: "Prometheus and Grafana"
description: "PromQL, exporters, dashboards, alerting, monitoring stack"
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
tags: [prometheus, grafana, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Prométhée et Grafana
Prometheus est une boîte à outils open source de surveillance et d'alerte conçue pour la fiabilité et l'évolutivité. Grafana est la principale plateforme open source de visualisation de données de séries chronologiques. Ensemble, ils forment la pile de surveillance la plus populaire pour les infrastructures et applications modernes. Prometheus collecte et stocke des métriques ; Grafana les affiche dans des tableaux de bord.
---

## Architecture de Prométhée
| Composant | Descriptif |
|---------------|-------------|
| **Serveur Prometheus** | Supprime les métriques des cibles ; stocke les données de séries chronologiques ; évalue les règles d'alerte |
| **Exportateur** | Expose les métriques d'un système (Node Exporter, cAdvisor, etc.) |
| **Passerelle** | Reçoit les métriques des tâches de courte durée (tâches par lots, CI) |
| **Gestionnaire d'alertes** | Gère les alertes : regroupement, mise sous silence, routage, inhibition |
| **Découverte de services** | Détecte automatiquement les cibles (Kubernetes, Consul, EC2, etc.) |
---

## Concepts clés
| Concepts | Descriptif |
|---------|-------------|
| **Métrique** | Une mesure nommée avec des étiquettes facultatives et une valeur |
| **Séries chronologiques** | Un flux de points de données pour une combinaison spécifique de métrique et d'étiquette |
| **Emploi** | Une collection de cibles ayant le même objectif |
| **Instance** | Une seule cible à gratter (généralement un processus) |
| **Gratte** | Prometheus extrait les métriques d'une cible à intervalles réguliers |
| **Étiquette** | Une paire clé-valeur qui dimensionne une métrique (par exemple,`method="GET"`) |
| **Échantillon** | Une valeur à un instant donné : (horodatage, valeur) |
---

## Types de métriques
| Tapez | Descriptif | Cas d'utilisation |
|------|-------------|--------------|
| **Compteur** | Valeur croissante de manière monotone (ne monte que) | Nombre de demandes ; erreurs ; tâches accomplies |
| **Jauge** | Valeur qui peut augmenter ou diminuer | Température; utilisation de la mémoire ; longueur de la file d'attente |
| **Histogramme** | Observations regroupées par valeur | Latence des demandes ; taille de la réponse |
| **Résumé** | Similaire à l'histogramme ; calcule les quantiles côté client | Centiles de latence |
---

## PromQL (langage de requête)
### Requêtes de base
| Requête | Descriptif |
|-------|-------------|
| `http_requests_total`| Séries chronologiques brutes |
| `http_requests_total{method="GET"}`| Filtrer par étiquette |
| `http_requests_total{method="GET", status="200"}`| Filtres d'étiquettes multiples |
| `rate(http_requests_total[5m])`| Taux par seconde sur 5 minutes |
| `increase(http_requests_total[1h])`| Augmentation totale sur 1 heure |
| `sum(rate(http_requests_total[5m])) by (status)`| Taux global par statut |
| `histogram_quantile(0.95, rate(http_duration_bucket[5m]))`| Latence du 95e percentile |
| `avg(node_cpu_seconds_total{mode="idle"})`| Inactivité moyenne du processeur |
| `1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))`| Utilisation du processeur |
### Fonctions communes
| Fonction | Descriptif | Exemple |
|--------------|-------------|---------|
| `rate()`| Taux d'augmentation moyen par seconde | `rate(requests_total[5m])`|
| `irate()`| Taux par seconde basé sur les deux derniers points de données | `irate(requests_total[1m])`|
| `increase()`| Augmentation totale au fil du temps | `increase(errors_total[1h])`|
| `sum()`| Somme sur toutes les séries | `sum(rate(requests_total[5m])) by (service)`|
| `avg()`| Moyenne sur l'ensemble des séries | `avg(node_memory_usage)`|
| `histogram_quantile()`| Calculer le quantile à partir de l'histogramme | `histogram_quantile(0.99, rate(duration_bucket[5m]))`|
| `topk()`| Meilleures séries K par valeur | `topk(5, rate(requests_total[5m]))`|
| `predict_linear()`| Prédiction linéaire | `predict_linear(disk_usage[1h], 4*3600)`|
| `absent()`| Vérifier si la métrique est manquante | `absent(up{job="myapp"})`|
---

## Exportateurs courants
| Exportateur | Ce qu'il surveille |
|--------------|-----------------|
| **Exportateur de nœuds** | Métriques de l'hôte Linux/Unix (CPU, mémoire, disque, réseau) |
| **cConseiller** | Métriques du conteneur (CPU, mémoire, réseau, système de fichiers) |
| **Exportateur MySQL** | Métriques de la base de données MySQL |
| **Exportateur PostgreSQL** | Métriques de la base de données PostgreSQL |
| **Exportateur Redis** | Métriques Redis |
| **Exportateur de boîte noire** | Sonder les points de terminaison via HTTP, HTTPS, DNS, TCP, ICMP |
| **Exportateur SNMP** | Métriques des périphériques réseau via SNMP |
| **Exportateur JSON** | Métriques personnalisées des API JSON |
---

## Grafana
### Concepts clés
| Concepts | Descriptif |
|---------|-------------|
| **Source de données** | Connexion à Prometheus (ou à d'autres backends) |
| **Tableau de bord** | Collection de panneaux disposés selon une disposition |
| **Panneau** | Visualisation unique (graphique, jauge, tableau, carte thermique) |
| **Variable** | Filtre dynamique pour les tableaux de bord (par exemple, sélectionner une instance) |
| **Annotations** | Marquer les événements sur des graphiques (déploiements, incidents) |
| **Règle d'alerte** | Alertes basées sur un seuil dans Grafana |
| **Modèle** | Modèles de tableaux de bord réutilisables avec variables |
### Modèles de tableaux de bord utiles
| Modèle | Descriptif |
|---------|-------------|
| **Ligne de présentation** | Aperçu des indicateurs clés : taux d'erreur, latence, débit |
| **Détail** | Cliquez du résumé à la vue détaillée à l'aide de variables |
| **Méthode ROUGE** | Taux, Erreurs, Durée – les trois indicateurs clés du service |
| **Méthode UTILISER** | Utilisation, saturation, erreurs — pour les infrastructures |
| **Signaux d'or** | Latence, trafic, erreurs, saturation (livre SRE de Google) |
---

## Alerte
### Structure des règles d'alerte
```yaml
groups:
  - name: example
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.05
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate on {{ $labels.instance }}"
          description: "Error rate is {{ $value | humanizePercentage }}"
```

### Routage du gestionnaire d'alertes
| Concepts | Descriptif |
|---------|-------------|
| **Groupe** | Combinez des alertes similaires en une seule notification |
| **Itinéraire** | Arbre de correspondances qui détermine où vont les alertes |
| **Récepteur** | Où envoyer des alertes (e-mail, Slack, PagerDuty, webhook) |
| **Inhiber** | Supprimer les alertes lorsqu'une autre alerte se déclenche |
| **Silence** | Désactiver temporairement les alertes par label matcher |
---

## Dépannage
| Problème | Solutions |
|---------|----------|
| **Ciblez vers le bas** | Vérifiez si l'exportateur est en cours d'exécution ; vérifier le réseau/pare-feu ; vérifier la configuration de scrape |
| **Aucune donnée** | Vérifiez l’orthographe du nom de la métrique ; vérifier les filtres d'étiquettes ; vérifier la plage horaire |
| ** Cardinalité élevée ** | Trop de combinaisons d'étiquettes ; réduire les valeurs des étiquettes ; utiliser les règles d'enregistrement |
| **Requêtes lentes** | Utiliser des règles d'enregistrement pour les requêtes complexes ; augmenter l'intervalle de grattage |
| **Alerte fatigue** | Ajuster les seuils ; ajouter la durée `for` ; alertes liées au groupe |
| **Mesures manquantes après le redémarrage** | Prometheus stocke les données localement ; vérifier les paramètres de conservation |
---

## Résumé
Prometheus surveille les systèmes en récupérant les statistiques des exportateurs à intervalles réguliers. Les métriques sont de quatre types : compteurs (montent uniquement), jauges (haut et bas), histogrammes (observations regroupées) et résumés (quantiles). PromQL est le langage de requête —`rate()`,`increase()`,`histogram_quantile()`et les fonctions d'agrégation (`sum`,`avg`) sont les opérations les plus courantes. Grafana visualise les données Prometheus dans des tableaux de bord avec des panneaux, des variables et des annotations. Alerting utilise Alertmanager pour regrouper, acheminer, désactiver et inhiber les alertes. Les principaux modèles de surveillance sont les signaux d'or de Google (latence, trafic, erreurs, saturation) et la méthode RED (taux, erreurs, durée) pour les services et la méthode USE (utilisation, saturation, erreurs) pour l'infrastructure.