---
# Metadata
title: "ML Engineering and MLOps"
description: "Model serving, registries, deployment strategies, drift monitoring"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [ml, engineering, mlops, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Ingénierie ML et MLOps
Construire un modèle d’apprentissage automatique ne représente que la moitié de la bataille. Le mettre en production, le maintenir en fonctionnement fiable, surveiller les dérives et itérer dessus : c'est là qu'interviennent l'ingénierie ML et les MLOps. Ce fichier couvre le cycle de vie complet, de l'expérimentation au système de production.
---

## Le cycle de vie du ML
| Phases | Descriptif | Activités clés |
|-------|-------------|--------------------|
| **1. Définition du problème** | Présenter le problème commercial comme une tâche de ML | Définir les métriques, les contraintes, les critères de réussite |
| **2. Collecte de données** | Recueillir et étiqueter les données de formation | ETL, étiquetage, augmentation |
| **3. Expérimentation** | Former et évaluer des modèles | Ingénierie des fonctionnalités, réglage des hyperparamètres |
| **4. Sélection de modèles** | Choisissez le meilleur modèle | Comparez les mesures, évaluez les compromis |
| **5. Déploiement** | Envoyer le modèle en production | Infrastructure de service, API, batch |
| **6. Surveillance** | Surveillez la dérive et la dégradation | Dérive des données, dérive des concepts, performances |
| **7. Reconversion** | Mettre à jour le modèle avec de nouvelles données | Reconversion programmée ou déclenchée |
La majeure partie de la valeur (et de la difficulté) se situe dans les phases 5 à 7. Un modèle placé dans un notebook Jupyter ne crée pas de valeur commerciale.
---

## Modèles de diffusion de modèles
| Modèle | Descriptif | Latence | Cas d'utilisation |
|---------|-------------|---------|----------|
| **Inférence par lots** | Exécuter le modèle sur un lot de données selon un planning | Horaires | Recommandations quotidiennes, notation de fraude |
| **Inférence en ligne** | Prédiction en temps réel par requête | Millisecondes | Classement de recherche, classification en temps réel |
| **Inférence de streaming** | Traiter les prédictions sur un flux de données | Secondes | Détection d'anomalies, traitement des événements |
### Infrastructure de service
| Outil | Tapez | Idéal pour |
|------|------|----------|
| **Service TensorFlow** | Serveur de modèles | Modèles TensorFlow |
| **TorchServe** | Serveur de modèles | Modèles PyTorch |
| **Serveur d'inférence Triton** | Multi-framework | Inférence GPU, frameworks multiples |
| **vLLM** | LLM au service | Inférence LLM à haut débit |
| **BentoML** | Service unifié | Déploiement indépendant du framework |
| **Seldon** | K8s-natif | Déploiement du modèle Kubernetes |
| **Ray Servir** | Service évolutif | Grands modèles, inférence distribuée |
---

## Registres de modèles
Un registre de modèles est un magasin centralisé pour la gestion des modèles ML : leurs versions, métadonnées, métriques et état de déploiement.
| Capacité | Descriptif |
|---------------|-------------|
| **Gestion des versions** | Suivez chaque version du modèle avec un identifiant unique |
| **Métadonnées** | Données d'entraînement, hyperparamètres, métriques, auteur |
| **Transitions de scène** | Déplacez les modèles à travers les étapes : Mise en scène → Production → Archivé |
| **Lignée** | Tracez les données et le code qui ont produit chaque modèle |
| Outil | Descriptif |
|------|-------------|
| **MLflow** | Source ouverte ; registre des modèles + suivi des expériences |
| **Poids et biais (W&B)** | Commercial; suivi des expériences + registre des modèles |
| **DVC** | Versionnement des données et des modèles avec Git |
| **Azure ML/SageMaker** | Gestion de modèles cloud-native |
---

## Suivi des expériences
Chaque expérience de ML doit être suivie : quelles données ont été utilisées, quels hyperparamètres, quelles métriques en ont résulté.
| Outil | Principales fonctionnalités |
|------|-------------|
| **MLflow** | Open source, auto-hébergé, suit les paramètres/métriques/artefacts |
| **W&B** | Interface utilisateur riche, balayages, versionnage d'artefacts, rapports |
| **Neptune** | Magasin de métadonnées pour MLOps |
| **TensorBoard** | Intégré à TensorFlow ; visualiser les courbes d'entraînement |
### Que suivre
| Catégorie | Exemples |
|--------------|---------|
| **Paramètres** | Taux d'apprentissage, taille du lot, architecture du modèle, nombre d'époques |
| **Mesures** | Précision, perte, F1, AUC-ROC (par époque et finale) |
| **Artefacts** | Poids du modèle, matrices de confusion, échantillons de prédiction |
| **Données** | Version de l'ensemble de données, ratios de répartition, étapes de prétraitement |
| **Environnement** | Version Python, versions de bibliothèque, matériel |
---

## Stratégies de déploiement de modèles
| Stratégie | Comment ça marche | Risque |
|--------------|-------------|------|
| **Déploiement fantôme** | Le nouveau modèle côtoie l’ancien ; prédictions comparées mais non servies | Risque zéro ; valide avant de passer en direct |
| **Version Canary** | Acheminer un petit pourcentage du trafic vers le nouveau modèle ; augmenter progressivement | Faible risque ; restauration rapide |
| **Tests A/B** | Répartissez les utilisateurs entre anciens et nouveaux ; comparer les indicateurs commerciaux | Mesure l'impact réel |
| **Bleu-Vert** | Deux environnements identiques ; basculer tout le trafic en même temps | Restauration instantanée ; double coût pendant la transition |
| **Drapeaux de fonctionnalité** | Activer/désactiver le modèle par segment d'utilisateurs | Contrôle à grain fin |
---

## Surveillance des systèmes ML
Les systèmes ML nécessitent plus de surveillance que les logiciels traditionnels, car les données elles-mêmes peuvent changer.
### Types de dérive
| Type de dérive | Quels changements | Exemple |
|---------------|-------------|---------|
| **Dérive des données** | Modifications de la distribution des entrées | La démographie des clients change après une campagne marketing |
| **Dérive des concepts** | Relation entre les changements d'entrée et de sortie | Le comportement des consommateurs change pendant une récession |
| **Dérive des étiquettes** | Modifications de la distribution cible | Le taux de fraude passe de 1% à 5% |
### Que surveiller
| Catégorie | Métriques |
|--------------|---------|
| **Performances du modèle** | Exactitude, précision, rappel, F1, AUC (par rapport à la ligne de base) |
| **Qualité des données** | Valeurs manquantes, distributions de fonctionnalités, valeurs aberrantes |
| **Détection de dérive** | Tests statistiques (test KS, PSI, divergence KL) |
| **Infrastructures** | Latence, débit, utilisation du GPU, mémoire |
| **Mesures commerciales** | Taux de conversion, impact sur les revenus, satisfaction des utilisateurs |
### Outils de surveillance
| Outil | Tapez |
|------|------|
| **Évidemment l'IA** | Dérive des données open source et surveillance des performances des modèles |
| **Grafana** | Visualisation du tableau de bord (fonctionne avec Prometheus) |
| **PourquoiLabs** | Plateforme d'observabilité des données |
| **Arize** | Observabilité du ML et analyse des causes profondes |
| **Prométhée + Grafana** | Métriques d'infrastructure et d'application |
---

## Formation reproductible
La reproductibilité signifie que vous pouvez relancer une expérience et obtenir le même résultat. C’est essentiel pour le débogage, l’audit et la conformité.
### Exigences
| Exigence | Comment y parvenir |
|-------------|---------|
| **Version des données** | Instantanés DVC, Delta Lake ou ensemble de données avec hachages |
| **Version du code** | Git pour tout le code de formation |
| **Épinglage d'environnement** | `requirements.txt`,`conda env`, images Docker avec versions exactes |
| **Réglage des graines** | Correction des graines aléatoires pour numpy, torch, tensorflow |
| **Gestion des configurations** | Configurations Hydra, OmegaConf ou YAML pour tous les hyperparamètres |
| **Suivi des artefacts** | MLflow ou W&B pour enregistrer chaque expérience |
---

## Inférence de mise à l'échelle
Lorsqu'un modèle doit répondre à des millions de requêtes par jour, les performances sont importantes.
| Techniques | Descriptif |
|---------------|-------------|
| **Mise en lots** | Regrouper plusieurs requêtes en une seule passe avant |
| **Quantification** | Réduisez la précision du modèle (FP32 → INT8 ou INT4) pour une inférence plus rapide |
| **Distillation modèle** | Entraîner un modèle plus petit pour imiter un modèle plus grand |
| **Taille** | Supprimez les poids ou les neurones sans importance |
| **Mise en cache** | Mettre en cache les prédictions fréquentes pour éviter le recalcul |
| **Optimisation du processeur graphique** | TensorRT, exécution ONNX, attention Flash |
| **Mise à l'échelle horizontale** | Exécuter plusieurs réplicas de modèle derrière un équilibreur de charge |
---

## Indicateurs de fonctionnalités pour le ML
Les indicateurs de fonctionnalités vous permettent de contrôler quelle version du modèle sert quels utilisateurs, sans redéployer.
| Cas d'utilisation | Descriptif |
|--------------|-------------|
| **Déploiement progressif** | Proposer le nouveau modèle à 5 % des utilisateurs, puis augmenter |
| **Interrupteur d'arrêt** | Revenir instantanément au modèle précédent si des problèmes sont détectés |
| **Basé sur des segments** | Différents modèles pour différents segments d'utilisateurs |
| **Expérimentation** | Variantes du modèle de test A/B avec métriques commerciales |
Outils : LaunchDarkly, Unleash, Flagsmith ou de simples indicateurs de fonctionnalités basés sur une base de données.
---

## La courbe de maturité MLOps
| Niveau | Caractéristiques |
|-------|----------------|
| **Niveau 0 — Manuel** | Formation manuelle, déploiement manuel, pas de surveillance |
| **Niveau 1 — Expérimentation** | Suivi des expériences, registre de modèles, CI de base |
| **Niveau 2 — Automatisation** | Recyclage automatisé, CI/CD pour modèles, tests automatisés |
| **Niveau 3 — Pipeline complet** | Pipeline automatisé de bout en bout avec surveillance, détection de dérive et recyclage automatique |
La plupart des organisations se situent entre le niveau 0 et le niveau 1. L'objectif est le niveau 2 et 3, où le cycle de vie du ML est automatisé et auto-réparateur.