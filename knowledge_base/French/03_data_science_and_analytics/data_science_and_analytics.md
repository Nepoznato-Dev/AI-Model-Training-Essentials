<!--
---
# Metadata
title: "Data Science and Analytics"
description: "Data processing, ML, big data, BI"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [data, science, analytics, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Science des données et analyse
La science des données est la discipline qui consiste à transformer des données brutes en informations exploitables. Il se situe à l’intersection des statistiques, de l’informatique et de l’expertise du domaine – et il est devenu essentiel dans tous les secteurs, de la finance à la santé. Ce fichier présente les concepts, outils et flux de travail de base que tout praticien devrait connaître.
---

## Le processus de science des données
La plupart des projets suivent une variante de **CRISP-DM**, le cycle de vie standard de l'industrie :
| Phases | Que se passe-t-il | Heure typique |
|-------|-------------|--------------|
| **Compréhension commerciale** | Définir les objectifs, les indicateurs de réussite et les contraintes | 10 à 15 % |
| **Compréhension des données** | Collecter, explorer et profiler les données | 10 à 15 % |
| **Préparation des données** | Nettoyer, transformer, concevoir des fonctionnalités | ~50-60 % |
| **Modélisation** | Sélectionner et entraîner des modèles | 10 à 15 % |
| **Évaluation** | Évaluer les performances par rapport aux objectifs commerciaux | 5 à 10 % |
| **Déploiement** | Envoyer le modèle en production | 5 à 10 % |
La préparation des données, en particulier le nettoyage des données, est largement estimée à environ 80 % du temps d'un data scientist.
---

## Types de données en un coup d'œil
| Tapez | Descriptif | Exemple |
|------|-------------|--------------|
| **Structuré** | Organisé en lignes et colonnes | Tableaux SQL, feuilles de calcul |
| **Non structuré** | Pas de format prédéfini | Texte, images, audio, vidéo |
| **Semi-structuré** | Une certaine organisation mais flexible | JSON, XML, HTML |
| **Séries chronologiques** | Données séquentielles indexées par temps | Cours des actions, relevés des capteurs |
| **Spatial** | Géographique ou géolocalisé | Coordonnées GPS, données cartographiques |
| **Graphique** | Nœuds et arêtes représentant des relations | Réseaux sociaux, graphes de connaissances |
---

## Fondamentaux des statistiques
### Statistiques descriptives et inférentielles
Les statistiques descriptives résument ce que vous *avez* ; les statistiques inférentielles vous permettent de tirer des conclusions sur ce que vous *n'avez pas* (la population au sens large).
| Concepts | Idées clés |
|---------|-----------|
| **Tendance centrale** | Moyenne (sensible aux valeurs aberrantes), médiane (robuste), mode (le plus fréquent) |
| **Dispersion** | Intervalle, variance, écart type, intervalle interquartile |
| **Forme de répartition** | Asymétrie (asymétrie), kurtosis (lourdeur de la queue) |
| **Test d'hypothèse** | Hypothèse nulle ou alternative, valeurs p, niveau de signification (α) |
| **Intervalles de confiance** | Plage contenant probablement le véritable paramètre de population |
| **Erreurs de type I/Type II** | Faux positif (rejet d'un vrai nul) / faux négatif (manque d'un effet réel) |
### Tests statistiques courants
| Test | Quand utiliser |
|------|-------------|
| **test t** | Comparer les moyennes entre deux groupes |
| **ANOVA** | Comparer les moyennes de trois groupes ou plus |
| **Chi carré** | Test d'indépendance des variables catégorielles |
| **Mann-Whitney U** | Alternative non paramétrique au test t (pas d'hypothèse de normalité) |
| **Corrélation de Pearson** | Relation linéaire entre deux variables continues |
| **Corrélation de Spearman** | Relation monotone (basée sur le classement, plus robuste) |
### Distributions de probabilité à connaître
| Distribution | Cas d'utilisation |
|-------------|----------|
| **Normal** | Phénomènes naturels, erreurs de mesure — la courbe en cloche classique |
| **Binôme** | Le succès/l'échec compte (lancements de pièces, taux de conversion) |
| **Poisson** | Les événements comptent dans un intervalle fixe (appels par heure, défauts par lot) |
| **Exponentiel** | Temps entre les événements (temps d'attente, intervalles de défaillance) |
| **t-Distribution** | Petits échantillons ou variance de population inconnue |
| **Chi carré** | Analyse de données catégorielles, tests d'adéquation |
---

## Collecte et stockage de données
### D'où proviennent les données
Les données du monde réel proviennent de nombreuses sources : bases de données relationnelles, API (REST, GraphQL), fichiers plats (CSV, JSON, Parquet), plateformes de streaming (Kafka, Kinesis), enquêtes et référentiels publics (Kaggle, portails gouvernementaux). Le format que vous recevez détermine une grande partie de votre stratégie de prétraitement.
### Concepts d'entreposage de données
| Concepts | Descriptif |
|---------|-------------|
| **ETL** | Extraire → Transformer → Charger — approche pipeline traditionnelle |
| **ELT** | Extraire → Charger → Transformer — approche cloud moderne (charger brut, transformer en entrepôt) |
| **Lac de données** | Données brutes stockées au format natif (schéma à la lecture) |
| **Entrepôt de données** | Données structurées et traitées optimisées pour l'analyse (schéma sur écriture) |
| **Marché de données** | Un sous-ensemble d'un entrepôt, limité à un département ou un domaine |
| **Schéma en étoile** | Table de faits centrale entourée de tables de dimensions |
| **Schéma flocon de neige** | Tables de dimensions normalisées (moins de redondance, plus de jointures) |
### Types de bases de données
| Tapez | Exemples | Idéal pour |
|------|----------|--------------|
| **Relationnel (SQL)** | PostgreSQL, MySQL, Oracle | Données structurées, transactions ACID |
| **Document** | MongoDB, CouchDB | Schémas flexibles, données de type JSON |
| **Valeur-clé** | Redis, DynamoDB | Mise en cache, sessions, recherches simples |
| **Colonne-Famille** | Cassandra, HBase | Charges de travail lourdes en écriture, séries chronologiques |
| **Graphique** | Neo4j, Amazon Neptune | Relations, réseaux sociaux |
| **Série chronologique** | InfluxDB, TimescaleDB | Métriques IoT, surveillance |
| **Vecteur** | Pomme de pin, Milvus | Intégration du stockage pour la recherche ML/AI |
---

## Prétraitement des données et ingénierie des fonctionnalités
### Liste de contrôle de nettoyage
Chaque ensemble de données réel comporte des problèmes. Voici le nettoyage standard :
| Problème | Approche |
|-------|--------------|
| **Valeurs manquantes** | Imputation (moyenne, médiane, prédiction) ou suppression si rare |
| **Valeurs aberrantes** | Détecter via IQR ou Z-score ; traiter avec bouchage ou transformation |
| **Doublons** | Identifier et supprimer |
| **Incohérences** | Standardisez les formats, corrigez les fautes de frappe, normalisez les unités |
### Techniques de transformation
| Techniques | Ce qu'il fait |
|---------------|-------------|
| **Normalisation** | Met à l'échelle les valeurs sur une plage de 0 à 1 |
| **Standardisation** | Score Z : moyenne = 0, standard = 1 |
| **Encodage à chaud** | Convertit les catégories en colonnes binaires |
| **Encodage des étiquettes** | Attribue des étiquettes entières aux catégories |
| **Transformation du journal** | Réduit l'inclinaison à droite des données |
| **Regroupement** | Regroupe les valeurs continues dans des compartiments discrets |
### Ingénierie des fonctionnalités
L’ingénierie des fonctionnalités fait souvent la différence entre un modèle médiocre et un excellent. Les techniques clés comprennent :
- **Création de fonctionnalités** : dériver de nouvelles colonnes à partir de colonnes existantes (par exemple,`age_group`à partir de`age`).
- **Sélection de fonctionnalités** : méthodes de filtrage (corrélation), méthodes wrapper (élimination récursive), méthodes intégrées (LASSO, importance de l'arbre).
- **Réduction de dimensionnalité** : PCA pour linéaire, t-SNE ou UMAP pour la visualisation.
- **Termes d'interaction** : combinaison de fonctionnalités de manière multiplicative pour capturer les effets conjoints.
---

## Analyse exploratoire des données (EDA)
L'EDA est l'endroit où vous développez votre intuition sur vos données avant la modélisation. L’objectif est de repérer des modèles, des anomalies et des relations.
### Choisir le bon graphique
| Type de graphique | Idéal pour |
|-----------|----------|
| **Histogramme** | Distribution d'une seule variable |
| **Box plot** | Résumé à cinq chiffres, détection des valeurs aberrantes |
| **Nuage de points** | Relation entre deux variables continues |
| **Carte thermique** | Matrices de corrélation, visualisation de densité |
| **Graphique à barres** | Comparaison des catégories |
| **Graphique linéaire** | Tendances au fil du temps |
| **Intrigue du violon** | Densité de distribution + résumé des boîtes à moustaches |
| **Parcelle en paire** | Aperçu rapide de toutes les paires de variables |
### La pile Python EDA
| Bibliothèque | Rôle |
|--------------|------|
| **pandas** | Manipulation et analyse de données |
| **numpy** | Informatique numérique |
| **matplotlib** | Traçage des fondations |
| **né de la mer** | Visualisation statistique (construite sur matplotlib) |
| **intrigue** | Visualisations interactives basées sur le Web |
| **scipy** | Calcul scientifique et statistiques |
---

## Apprentissage automatique en science des données
### L'apprentissage supervisé en un coup d'œil
| Tâche | Algorithmes |
|------|-----------|
| **Régression** (prédire un nombre) | Linéaire, Ridge/LASSO, Arbre de décision, Forêt aléatoire, Boosting de gradient (XGBoost, LightGBM) |
| **Classification** (prédire une catégorie) | Régression logistique, k-NN, Naive Bayes, SVM, arbres de décision, forêt aléatoire, réseaux de neurones |
### L'apprentissage non supervisé en un coup d'œil
| Tâche | Algorithmes |
|------|-----------|
| **Regroupement** | k-Means, modèles hiérarchiques, DBSCAN, mélanges gaussiens |
| **Réduction de dimensionnalité** | PCA, t-SNE, UMAP, auto-encodeurs |
| **Règles de l'association** | A priori, FP-Croissance |
### Évaluation du modèle
| Type métrique | Indicateurs clés |
|-------------|-------------|
| **Classement** | Exactitude, précision, rappel, score F1, ROC-AUC, matrice de confusion |
| **Régression** | MAE, MSE, RMSE, R², R² ajusté |
| **Validation** | validation croisée k-fold, stratifiée, division de séries chronologiques |
| **Réglage** | Recherche par grille, recherche aléatoire, optimisation bayésienne |
---

## Technologies du Big Data
Lorsque les ensembles de données dépassent ce qu’une seule machine peut gérer, l’informatique distribuée entre en scène.
| Cadre | Force |
|-----------|----------|
| **Apache Spark** | Traitement en mémoire ; Spark SQL, Streaming, MLlib, GraphX ​​|
| **Apache Hadoop** | MapReduce + HDFS — la pile Big Data originale |
| **Apache Flink** | Traitement de flux à faible latence |
| **Apache Beam** | Modèle unifié par lots et streaming |
### Plateformes de données cloud
| Fournisseur | Services clés |
|--------------|-------------|
| **AWS** | S3, EMR, Redshift, SageMaker, Colle |
| **Google Cloud** | BigQuery, Dataproc, AI Platform, stockage cloud |
| **Azur** | Synapse Analytics, Databricks, Machine Learning, Data Lake |
| **Flocon de neige** | Entrepôt de données cloud natif (indépendant du fournisseur) |
### Orchestration des pipelines
| Outil | Remarques |
|------|-------|
| **Apache Airflow** | Norme industrielle ; DAG basés sur Python |
| **Préfet** | Alternative moderne avec une API plus propre |
| **Dague** | Orchestration centrée sur les actifs |
| **dette** | Transformation des données SQL first en entrepôt |
---

## Intelligence d'affaires et analyses
### Outils BI comparés
| Outil | Tapez | Force |
|------|------|----------|
| **Tableau** | Commerciale | Analyses visuelles riches, glisser-déposer |
| **Power BI** | Commercial (Microsoft) | Intégration profonde d'Office/Azure |
| **Observateur** | Commercial (Google) | Exploration de données, modélisation LookML |
| **Métabase** | Open source | Installation facile, SQL natif |
| **Superset** | Open source (Apache) | Évolutif, SQL d'abord |
### Principes de conception du tableau de bord
Les bons tableaux de bord suivent quelques règles : connaissez votre public, choisissez la bonne visualisation pour chaque métrique, utilisez la couleur de manière stratégique (et non décorative), maintenez des échelles cohérentes et activez l'interactivité (filtres, analyses approfondies). Les performances comptent également : personne n’attend un tableau de bord lent.
### Catégories de KPI courantes
| Catégorie | Exemples |
|----------|---------|
| **Financière** | Revenus, marge bénéficiaire, retour sur investissement, valeur à vie du client |
| **Client** | Coût d'acquisition (CAC), taux de désabonnement, NPS, score de satisfaction |
| **Opérationnel** | Taux d'efficacité, temps de cycle, taux de défauts |
| **Marketing** | Taux de conversion, taux de clics, ROAS, attribution |
| **Produit** | Utilisateurs actifs quotidiens, engagement, fidélisation, adoption des fonctionnalités |
---

## Analyses avancées
| Approche | Techniques | Quand utiliser |
|--------------|-----------|-------------|
| **Prédictif** | Séries chronologiques (ARIMA, Prophet, LSTM), modélisation des risques, prédiction du taux de désabonnement | Prévoir les valeurs futures |
| **Prescriptif** | Programmation linéaire, simulation Monte Carlo, tests A/B, bandits multi-bras | Optimiser les décisions |
| **Analyse de texte** | Tokenisation, analyse des sentiments, modélisation de sujets (LDA), NER, intégrations de mots (Word2Vec, BERT) | Extraire des informations à partir d'un texte |
---

## Éthique et gouvernance des données
### Règlement sur la confidentialité
| Réglementation | Portée |
|---------------|-------|
| **RGPD** | Personnes concernées par les données de l'UE ; droit à l'effacement, consentement, portabilité des données |
| **CCPA** | Consommateurs californiens ; désinscription des ventes de données |
| **HIPAA** | Données de santé aux États-Unis ; règles de confidentialité strictes |
### Dimensions de la qualité des données
| Dimensions | Question |
|-----------|----------|
| **Précision** | Les données sont-elles correctes ? |
| **Exhaustivité** | Est-ce qu'il manque quelque chose ? |
| **Cohérence** | Les sources sont-elles d’accord ? |
| **Rapidité** | Est-ce actuel ? |
| **Validité** | Est-il conforme aux formats attendus ? |
| **Unicité** | Y a-t-il des doublons ? |
### Biais et équité
Les biais peuvent intervenir à n’importe quelle étape : biais d’échantillonnage (données non représentatives), biais de mesure (instruments défectueux) ou biais algorithmique (prédictions discriminatoires). Les stratégies d'atténuation comprennent le pré-traitement (fixation des données), le traitement (contrainte du modèle) et le post-traitement (ajustement des résultats). Les mesures d’équité telles que la parité démographique et l’égalité des chances aident à quantifier le problème.
---

## Cheminements de carrière
| Rôle | Mise au point |
|------|-------|
| **Analyste de données** | Analyses descriptives, tableaux de bord, reporting |
| **Scientifique des données** | Modélisation statistique, ML, analyses avancées |
| **Ingénieur ML** | Systèmes ML de production, déploiement de modèles, MLOps |
| **Ingénieur de données** | Pipelines de données, infrastructure, ETL |
| **Responsable des analyses** | Leadership d'équipe, stratégie, gestion des parties prenantes |
| **Chercheur scientifique** | Nouveaux algorithmes, publications |
---

## Tendances émergentes
- **AutoML** : création automatisée de pipelines et sélection de modèles.
- **MLOps** : pratiques DevOps appliquées à la gestion du cycle de vie du ML.
- **Feature Stores** : gestion centralisée des fonctionnalités pour une réutilisation entre les équipes.
- **Data Mesh** : architecture de données décentralisée appartenant au domaine.
- **LLM et IA générative** : grands modèles de langage transformant les flux de travail de texte, de code et d'images.
- **Edge Analytics** : traitement des données sur l'appareil plutôt que dans le cloud.
- **Inférence causale** : aller au-delà de la corrélation pour comprendre la cause et l'effet réels.
- **Federated Learning** : entraînez des modèles sur des données décentralisées sans les déplacer.
- **IA responsable** : L'éthique, l'explicabilité et la transparence deviennent des exigences standards.