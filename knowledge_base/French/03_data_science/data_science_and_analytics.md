# Science des données et analytique

## Concepts fondamentaux

### Qu'est-ce que la science des données ?
La science des données est un domaine interdisciplinaire qui utilise des méthodes scientifiques, des processus, des algorithmes et des systèmes pour extraire des connaissances et des enseignements à partir de données structurées et non structurées. Elle combine :
- **Statistiques** : base mathématique de l'analyse
- **Informatique** : programmation, algorithmes, structures de données
- **Expertise métier** : connaissance du domaine
- **Visualisation des données** : communication efficace des résultats

### Types de données
- **Données structurées** : organisées en lignes/colonnes (bases de données, feuilles de calcul)
- **Données non structurées** : sans format prédéfini (texte, images, audio, vidéo)
- **Données semi-structurées** : comportent une certaine organisation sans être rigides (JSON, XML, HTML)
- **Données de séries temporelles** : points de données séquentiels indexés dans l'ordre du temps
- **Données spatiales** : informations géographiques ou basées sur la localisation
- **Données de graphe** : nœuds et arêtes représentant des relations

### Le processus de science des données (CRISP-DM)
1. **Compréhension métier** : définir les objectifs et les exigences
2. **Compréhension des données** : collecter et explorer les données initiales
3. **Préparation des données** : nettoyer, transformer et mettre en forme les données (80 % du travail)
4. **Modélisation** : sélectionner et appliquer des techniques de modélisation
5. **Évaluation** : évaluer les performances du modèle par rapport aux objectifs
6. **Déploiement** : mettre en œuvre le modèle dans un environnement de production

## Fondamentaux des statistiques

### Statistiques descriptives
- **Mesures de tendance centrale** : moyenne, médiane, mode
- **Mesures de dispersion** : étendue, variance, écart-type, intervalle interquartile
- **Forme de la distribution** : asymétrie (skewness), aplatissement (kurtosis)
- **Percentiles et quartiles** : position au sein d'une distribution

### Statistiques inférentielles
- **Tests d'hypothèse** : hypothèse nulle, hypothèse alternative, p-values
- **Intervalles de confiance** : plage de valeurs susceptible de contenir le paramètre de population
- **Significativité statistique** : probabilité que les résultats soient dus au hasard
- **Erreur de type I** : faux positif (rejet d'une hypothèse nulle vraie)
- **Erreur de type II** : faux négatif (non-rejet d'une hypothèse nulle fausse)
- **Puissance** : probabilité de rejeter correctement une hypothèse nulle fausse

### Distributions de probabilité
- **Distribution normale** : courbe en cloche, moyenne = médiane = mode
- **Distribution binomiale** : issues succès/échec
- **Distribution de Poisson** : nombre d'événements dans un intervalle fixe
- **Distribution uniforme** : toutes les issues sont équiprobables
- **Distribution exponentielle** : temps entre les événements
- **Distribution t** : petits échantillons, variance de population inconnue
- **Distribution du chi carré** : analyse de données catégorielles

### Tests statistiques
- **t-test** : comparer les moyennes entre deux groupes
- **ANOVA** : comparer les moyennes entre plusieurs groupes
- **Test du chi carré** : tester l'indépendance de variables catégorielles
- **Mann-Whitney U** : alternative non paramétrique au t-test
- **Corrélation de Pearson** : relation linéaire entre variables continues
- **Corrélation de Spearman** : relation monotone (basée sur les rangs)
- **Kolmogorov-Smirnov** : comparer des distributions

## Collecte et stockage des données

### Sources de données
- **Bases de données** : SQL, NoSQL, relationnelles, documentaires
- **APIs** : REST, GraphQL, web scraping
- **Fichiers** : CSV, JSON, XML, Parquet, Avro
- **Données en flux** : Kafka, Kinesis, flux en temps réel
- **Enquêtes et expériences** : collecte de données primaires
- **Jeux de données publics** : données gouvernementales, Kaggle, dépôts universitaires

### Entrepôts de données
- **ETL** : processus Extract, Transform, Load
- **Data Lake** : stockage de données brutes dans leur format natif
- **Data Warehouse** : données structurées et traitées pour l'analyse
- **Data Mart** : sous-ensemble d'un entrepôt pour un service précis
- **OLAP** : Online Analytical Processing, requêtes multidimensionnelles
- **Schéma en étoile** : tables de faits entourées de tables de dimensions
- **Schéma en flocon** : tables de dimensions normalisées

### Types de bases de données
- **Relationnelles (SQL)** : MySQL, PostgreSQL, Oracle, SQL Server
- **Documentaires** : MongoDB, CouchDB (documents de type JSON)
- **Clé-valeur** : Redis, DynamoDB (paires clé-valeur simples)
- **Famille de colonnes** : Cassandra, HBase (optimisées pour les colonnes)
- **Graphe** : Neo4j, Amazon Neptune (nœuds et relations)
- **Séries temporelles** : InfluxDB, TimescaleDB (données horodatées)
- **Vectorielles** : Pinecone, Milvus (stockage d'embeddings pour le ML)

## Prétraitement des données

### Nettoyage des données
- **Valeurs manquantes** : imputation (moyenne, médiane, mode, prédiction), suppression
- **Valeurs aberrantes** : détection (IQR, Z-score), traitement (capping, transformation)
- **Doublons** : identification et suppression
- **Incohérences** : standardisation des formats, correction des fautes de frappe
- **Validation des données** : vérification des contraintes, des plages et des types

### Transformation des données
- **Normalisation** : mise à l'échelle dans une plage de 0 à 1
- **Standardisation** : normalisation Z-score (moyenne = 0, écart-type = 1)
- **Encodage** : one-hot, label, ordinal, target encoding
- **Discrétisation** : regroupement de valeurs continues en catégories
- **Transformation logarithmique** : réduction de l'asymétrie
- **Mise à l'échelle des variables** : rendre les variables comparables

### Ingénierie des variables
- **Création de variables** : dériver de nouvelles variables à partir de variables existantes
- **Sélection de variables** : choisir les variables les plus pertinentes
  - Méthodes de filtrage (corrélation, chi carré)
  - Méthodes wrapper (élimination récursive de variables)
  - Méthodes intégrées (LASSO, importance basée sur les arbres)
- **Réduction de dimensionnalité** : PCA, t-SNE, UMAP
- **Termes d'interaction** : combinaison multiplicative de variables
- **Variables polynomiales** : création de termes d'ordre supérieur

## Analyse exploratoire des données (EDA)

### Techniques d'EDA
- **Statistiques récapitulatives** : décrire la tendance centrale, la dispersion et la forme
- **Analyse univariée** : distributions d'une seule variable
- **Analyse bivariée** : relations entre deux variables
- **Analyse multivariée** : interactions entre plusieurs variables
- **Analyse de corrélation** : identifier les relations et la multicolinéarité
- **Segmentation** : regrouper des observations similaires

### Outils de visualisation
- **Histogrammes** : distribution d'une seule variable
- **Boîtes à moustaches** : résumé en cinq nombres, détection des valeurs aberrantes
- **Nuages de points** : relation entre deux variables continues
- **Cartes de chaleur** : matrices de corrélation, densité
- **Diagrammes en barres** : comparaisons catégorielles
- **Graphiques linéaires** : tendances au fil du temps
- **Graphiques en violon** : densité de distribution avec éléments de boîte à moustaches
- **Pair plots** : plusieurs nuages de points pour des paires de variables

### Bibliothèques Python pour l'EDA
- **pandas** : manipulation et analyse de données
- **numpy** : calcul numérique
- **matplotlib** : visualisation de base
- **seaborn** : visualisation statistique
- **plotly** : visualisations interactives
- **scipy** : calcul scientifique et statistiques

## Apprentissage automatique en science des données

### Apprentissage supervisé
- **Régression** : prédire des valeurs continues
  - Régression linéaire
  - Régression polynomiale
  - Ridge/LASSO/Elastic Net
  - Régression par arbre de décision
  - Régression par forêt aléatoire
  - Gradient Boosting (XGBoost, LightGBM, CatBoost)
  
- **Classification** : prédire des étiquettes catégorielles
  - Régression logistique
  - k plus proches voisins
  - Naive Bayes
  - Machines à vecteurs de support
  - Arbres de décision
  - Forêt aléatoire
  - Gradient Boosting
  - Réseaux de neurones

### Apprentissage non supervisé
- **Clustering** : regrouper des observations similaires
  - k-Means
  - Classification hiérarchique
  - DBSCAN (basé sur la densité)
  - Modèles de mélanges gaussiens
  - Clustering spectral
  
- **Réduction de dimensionnalité** : réduire le nombre de variables
  - Analyse en composantes principales (PCA)
  - t-Distributed Stochastic Neighbor Embedding (t-SNE)
  - Uniform Manifold Approximation (UMAP)
  - Autoencodeurs
  
- **Règles d'association** : trouver les éléments qui coexistent fréquemment
  - Algorithme Apriori
  - FP-Growth

### Évaluation des modèles
- **Mesures de classification** : accuracy, precision, recall, F1-score, ROC-AUC, matrice de confusion
- **Mesures de régression** : MAE, MSE, RMSE, R², R² ajusté
- **Validation croisée** : k-fold, stratifiée, leave-one-out, découpage de séries temporelles
- **Réglage des hyperparamètres** : grid search, random search, optimisation bayésienne
- **Courbes d'apprentissage** : diagnostiquer le compromis biais-variance

## Technologies Big Data

### Frameworks de calcul distribué
- **Apache Hadoop** : MapReduce, HDFS (Hadoop Distributed File System)
- **Apache Spark** : traitement en mémoire, plus rapide que Hadoop
  - Spark SQL : traitement des données structurées
  - Spark Streaming : données en temps réel
  - MLlib : bibliothèque de machine learning
  - GraphX : traitement de graphes
- **Apache Flink** : traitement de flux à faible latence
- **Apache Beam** : unification du batch et du streaming

### Plateformes cloud
- **AWS** : S3, EMR, Redshift, SageMaker, Glue
- **Google Cloud** : BigQuery, Dataproc, AI Platform, Cloud Storage
- **Azure** : Synapse Analytics, Databricks, Machine Learning, Data Lake
- **Snowflake** : entrepôt de données cloud

### Outils de pipelines de données
- **Apache Airflow** : orchestration de workflows
- **Luigi** : gestion de pipelines (Spotify)
- **Prefect** : orchestration moderne de workflows
- **Dagster** : orchestrateur de données centré sur les assets
- **dbt** : transformation des données dans l'entrepôt

## Business intelligence et analytique

### Outils de BI
- **Tableau** : plateforme d'analyse visuelle
- **Power BI** : analytique décisionnelle de Microsoft
- **Looker** : exploration des données et génération d'insights (Google)
- **Qlik Sense** : analytique associative
- **Metabase** : BI open source
- **Superset** : BI open source d'Apache

### Principes de conception de tableaux de bord
- **Connaître son public** : adapter le contenu aux besoins des utilisateurs
- **Choisir les bonnes visualisations** : faire correspondre le graphique au type de données
- **Utiliser la couleur de manière stratégique** : mettre en évidence les informations importantes
- **Maintenir la cohérence** : standardiser les formats et les échelles
- **Permettre l'interactivité** : filtres, drill-downs, infobulles
- **Optimiser les performances** : chargement rapide, requêtes efficaces
- **Considérations mobiles** : conception responsive

### Indicateurs clés de performance (KPI)
- **Financiers** : chiffre d'affaires, marge bénéficiaire, ROI, valeur vie client
- **Clients** : coût d'acquisition, taux d'attrition, score de satisfaction, NPS
- **Opérationnels** : taux d'efficacité, temps de cycle, taux de défauts
- **Marketing** : taux de conversion, taux de clic, attribution
- **Produit** : utilisateurs actifs, engagement, rétention, adoption des fonctionnalités

## Analytique avancée

### Analytique prédictive
- **Prévision** : prédiction de séries temporelles (ARIMA, Prophet, LSTM)
- **Modélisation du risque** : scoring de crédit, détection de fraude, assurance
- **Analytique client** : prédiction de l'attrition, modèles de propension
- **Prévision de la demande** : optimisation des stocks, chaîne d'approvisionnement
- **Prévision de maintenance** : anticipation des pannes d'équipement

### Analytique prescriptive
- **Optimisation** : programmation linéaire, programmation en nombres entiers
- **Simulation** : méthodes de Monte Carlo, simulation à événements discrets
- **Analyse décisionnelle** : arbres de décision, diagrammes d'influence
- **Tests A/B** : plan d'expérience, significativité statistique
- **Bandits manchots multi-bras** : expérimentation adaptative

### Analyse de texte (NLP)
- **Prétraitement du texte** : tokenization, stemming, lemmatization
- **Analyse de sentiment** : classification positif/négatif/neutre
- **Modélisation de sujets** : LDA, NMF pour découvrir des thèmes
- **Reconnaissance d'entités nommées** : identification des personnes, lieux et organisations
- **Classification de texte** : détection de spam, catégorisation
- **Représentations vectorielles de mots** : Word2Vec, GloVe, BERT

## Éthique et gouvernance des données

### Confidentialité des données
- **GDPR** : Règlement général sur la protection des données de l'UE
- **CCPA** : California Consumer Privacy Act
- **HIPAA** : Health Insurance Portability and Accountability Act (santé aux États-Unis)
- **Anonymisation** : suppression des informations personnellement identifiables
- **Confidentialité différentielle** : ajout de bruit pour protéger les individus
- **Gestion du consentement** : mécanismes d'opt-in/opt-out

### Qualité des données
- **Exactitude** : correction des données
- **Exhaustivité** : présence de toutes les données requises
- **Cohérence** : absence de contradictions entre les sources
- **Actualité** : disponibilité des données au moment opportun
- **Validité** : conformité aux règles définies
- **Unicité** : absence de doublons

### Biais et équité
- **Biais d'échantillonnage** : collecte de données non représentative
- **Biais de mesure** : instruments de collecte de données défaillants
- **Biais algorithmique** : prédictions discriminatoires des modèles
- **Mesures d'équité** : parité démographique, égalité des chances
- **Atténuation des biais** : prétraitement, traitement en cours, post-traitement

### Cadre de gouvernance des données
- **Gestion des données** : responsabilité sur les actifs de données
- **Gestion des métadonnées** : documentation des données sur les données
- **Traçabilité des données** : suivi des flux de données et des transformations
- **Contrôle d'accès** : autorisations basées sur les rôles
- **Pistes d'audit** : journalisation des accès et des modifications de données
- **Conformité** : respect des réglementations

## Parcours de carrière en science des données

### Rôles
- **Data Analyst** : analytique descriptive, tableaux de bord, reporting
- **Data Scientist** : modélisation statistique, machine learning, analytique avancée
- **ML Engineer** : systèmes de ML en production, déploiement de modèles, MLOps
- **Data Engineer** : pipelines de données, infrastructure, processus ETL
- **Analytics Manager** : leadership d'équipe, stratégie, gestion des parties prenantes
- **BI Developer** : création de tableaux de bord, développement de rapports
- **Research Scientist** : nouveaux algorithmes, publications, recherche avancée

### Matrice de compétences
- **Techniques** : Python/R, SQL, statistiques, frameworks de ML, plateformes cloud
- **Analytiques** : résolution de problèmes, pensée critique, conception expérimentale
- **Communication** : storytelling, visualisation, compétences de présentation
- **Métier** : connaissance du domaine, gestion des parties prenantes, analyse du ROI
- **Outils** : Git, Jupyter, Docker, CI/CD, gestion de versions pour les modèles

## Tendances émergentes

### Évolutions actuelles
- **AutoML** : création automatisée de pipelines de machine learning
- **MLOps** : pratiques DevOps pour le machine learning
- **Feature Stores** : gestion centralisée des variables
- **Data Mesh** : architecture de données décentralisée
- **LLMs et IA générative** : grands modèles de langage, génération de contenu
- **Analytique en périphérie** : traitement des données à la source
- **Analytique en temps réel** : analyse de données en flux
- **Analytique augmentée** : préparation des données et insights assistés par l'IA

### Orientations futures
- **Quantum Machine Learning** : informatique quantique appliquée au ML
- **Federated Learning** : entraînement de modèles sur des données décentralisées
- **Causal Inference** : passer de la corrélation à la causalité
- **IA responsable** : éthique, explicabilité, transparence
- **Data Fabric** : gestion intégrée des données entre environnements
