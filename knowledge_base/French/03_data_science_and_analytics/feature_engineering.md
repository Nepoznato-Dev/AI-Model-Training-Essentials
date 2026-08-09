---
# Métadonnées
titre : "Ingénierie des fonctionnalités"
description: "Transformations, encodages, sélection de fonctionnalités, réduction de dimensionnalité"
catégorie : "Science des données et analyse"
version : "1.0.0"
statut : "actif"
# Contribution
auteurs :
  - nom : « Équipe de formation des modèles IA »
    email: ""
    rôle : "original_author"
contributeurs : []
journal des modifications :
  - version : "1.0.0"
    date : "05/08/2026"
    auteur : « Équipe de formation des modèles IA »
    modifications : « Ajout des métadonnées de premier plan YAML pour le suivi des contributeurs »
# Révision
créé : "2026-08-05"
last_modified : "05/08/2026"
date_de_revue : "05/02/2027"
review_by : "Équipe de la base de connaissances sur la science des données et l'analyse"
next_review : "2027-08-05"
#Classement
tags : [fonctionnalité, ingénierie, science des données et analyse]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "7 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Ingénierie des fonctionnalités
L'ingénierie des fonctionnalités est le processus de transformation des données brutes en représentations qui rendent les modèles d'apprentissage automatique plus efficaces. Elle est souvent décrite comme l'étape la plus importante du pipeline ML : les fonctionnalités que vous donnez à un modèle comptent plus que l'algorithme que vous choisissez. Un modèle simple doté de fonctionnalités bien conçues surpassera généralement un modèle complexe comportant des entrées brutes et non traitées. L’art consiste à comprendre suffisamment bien le domaine et les données pour créer des signaux dont le modèle peut tirer des leçons.
---

## Pourquoi l'ingénierie des fonctionnalités est importante
| Facteur | Impact |
|--------|--------|
| **Qualité du signal** | Meilleures fonctionnalités = modèles plus clairs à apprendre pour le modèle |
| **Simplicité du modèle** | De bonnes fonctionnalités permettent aux modèles plus simples de bien fonctionner ; moins besoin d'architectures complexes |
| **Vitesse d'entraînement** | Les fonctionnalités pertinentes et bien mises à l'échelle convergent plus rapidement |
| **Généralisation** | Les fonctionnalités basées sur le domaine aident les modèles à travailler sur des données invisibles |
| **Interprétabilité** | Les fonctionnalités significatives sont plus faciles à expliquer aux parties prenantes |
---

## Types de transformations de fonctionnalités
### Transformations numériques
| Transformations | Formule / Description | Quand utiliser |
|---------------|------------|-------------|
| **Transformation du journal** | log(x) ou log(x + 1) | Distributions asymétriques à droite ; valeurs monétaires |
| **Racine carrée** | carré(x) | Asymétrie modérée ; compter les données |
| **Boîte-Cox** | Transformation paramétrique qui trouve la meilleure transformation de puissance | Rendre les données plus normalement distribuées |
| **Yeo-Johnson** | Comme Box-Cox mais gère les valeurs négatives | Données asymétriques avec des valeurs négatives |
| **Normalisation** | (x - moyenne) / std | Des fonctionnalités à différentes échelles ; algorithmes supposant la normalité |
| **Mise à l'échelle min-max** | (x - min) / (max - min) | Caractéristiques limites à [0, 1] ; valeurs des pixels de l'image |
| **Mise à l'échelle robuste** | (x - médiane) / IQR | Données avec valeurs aberrantes |
| **Regroupement** | Convertir continu en catégoriel | Relations non linéaires ; arbres de décision |
| **Caractéristiques polynomiales** | x², x³, x₁×x₂ | Capturer des relations non linéaires dans des modèles linéaires |
### Encodages catégoriels
| Encodage | Descriptif | Quand utiliser |
|--------------|-------------|-------------|
| **Encodage à chaud** | Créer une colonne binaire pour chaque catégorie | Catégories de faible cardinalité ; les modèles arborescents sont gérés de manière native |
| **Encodage des étiquettes** | Attribuer un entier à chaque catégorie | Catégories ordinales ; modèles arborescents |
| **Encodage cible** | Remplacer la catégorie par la moyenne de la variable cible | Catégories à haute cardinalité ; éviter le surapprentissage avec le lissage |
| **Codage de fréquence** | Remplacer la catégorie par son nombre ou sa fréquence | Quand la fréquence elle-même est informative |
| **Encodage binaire** | Convertir les catégories codées en nombres entiers en chiffres binaires | Haute cardinalité ; réduit la dimensionnalité par rapport au one-hot |
| **Intégration** | Apprendre la représentation vectorielle dense | Cardinalité très élevée ; PNL ; systèmes de recommandation |
| **Encodage de hachage** | Hacher des catégories vers un nombre fixe de fonctionnalités | Cardinalité très élevée ; apprentissage en ligne |
### Fonctionnalités de date et d'heure
| Fonctionnalité | Descriptif |
|---------|-------------|
| **Heure de la journée** | Capture les schémas quotidiens (heures de pointe, nuit) |
| **Jour de la semaine** | Effets en semaine ou en week-end |
| **Mois / trimestre** | Modèles saisonniers |
| **C'est le week-end** | Drapeau binaire pour le week-end |
| **Est-ce des vacances** | Drapeau binaire pour les jours fériés |
| **Durée depuis l'événement** | Jours depuis le dernier achat ; heures depuis la dernière connexion |
| **Codage cyclique** | sin(2π × heure / 24), cos(2π × heure / 24) — préserve la nature circulaire du temps |
---

## Gestion des valeurs manquantes
| Stratégie | Descriptif | Quand utiliser |
|--------------|-------------|-------------|
| **Supprimer des lignes** | Supprimer les lignes avec des valeurs manquantes | Les données manquantes ne représentent qu’une petite fraction ; MCAR (manquant complètement au hasard) |
| **Supprimer les colonnes** | Supprimer les fonctionnalités avec trop de valeurs manquantes | La fonctionnalité est pour la plupart manquante ; pas important |
| **Imputation moyenne/médiane** | Remplissez avec la moyenne ou la médiane de l'entité | Simple; préserve la moyenne mais réduit la variance |
| **Imputation de mode** | Remplissez la catégorie avec la valeur la plus fréquente | Caractéristiques catégorielles |
| **Imputation KNN** | Utiliser les k voisins les plus proches pour estimer la valeur manquante | Quand des instances similaires aident à prédire la valeur manquante |
| **Imputation basée sur un modèle** | Entraîner un modèle pour prédire les valeurs manquantes | Plus précis ; coûteux en calcul |
| **Indicateur manquant** | Ajouter une colonne binaire signalant les absences | Quand le manque lui-même est informatif |
| **Interpolation** | Remplir avec des valeurs interpolées (linéaire, spline) | Séries chronologiques ; données commandées |
---

## Sélection des fonctionnalités
### Méthodes de filtrage
| Méthode | Descriptif |
|--------|-------------|
| **Corrélation** | Supprimer les fonctionnalités fortement corrélées les unes aux autres |
| **Seuil d'écart** | Supprimer les fonctionnalités avec une variance proche de zéro |
| **Information mutuelle** | Mesurer les informations fournies par chaque fonctionnalité sur la cible |
| **Chi carré** | Indépendance des tests entre les caractéristiques catégorielles et la cible |
| **Test F ANOVA** | Tester si les moyennes des caractéristiques numériques diffèrent selon les classes cibles |
### Méthodes d'emballage
| Méthode | Descriptif |
|--------|-------------|
| **Sélection avant** | Commencez à vide ; ajouter la meilleure fonctionnalité une à la fois |
| **Élimination en amont** | Commencez par tout ; supprimer la pire fonctionnalité une à la fois |
| **Élimination de fonctionnalités récursives (RFE)** | Entraîner le modèle à plusieurs reprises ; supprimer les fonctionnalités les moins importantes |
### Méthodes intégrées
| Méthode | Descriptif |
|--------|-------------|
| **Régularisation L1 (Lasso)** | Réduit les poids des caractéristiques non pertinentes à zéro |
| **Importance basée sur les arbres** | Utiliser l'importance des fonctionnalités à partir des modèles d'arborescence |
| **Valeurs SHAP** | Mesurer la contribution de chaque fonctionnalité aux prédictions |
---

## Ingénierie de fonctionnalités spécifiques au domaine
### Fonctionnalités de texte
| Fonctionnalité | Descriptif |
|---------|-------------|
| **TF-IDF** | Fréquence des termes pondérée par la fréquence inverse des documents |
| **Intégrations de mots** | Vecteurs denses capturant le sens sémantique (Word2Vec, GloVe) |
| **N-grammes de caractères** | Capturez les modèles de sous-mots ; utile pour les fautes de frappe et la morphologie |
| **Statistiques de texte** | Longueur; nombre de mots ; nombre de phrases ; longueur moyenne des mots |
| **Notes de lisibilité** | Flesch-Kincaid ; Indice de brouillard de tir |
### Fonctionnalités des séries chronologiques
| Fonctionnalité | Descriptif |
|---------|-------------|
| **Fonctionnalités de décalage** | Valeurs précédentes : y(t-1), y(t-7), y(t-30) |
| **Statistiques glissantes** | Moyenne, std, min, max sur une fenêtre |
| **Différence** | y(t) - y(t-1); capture la tendance |
| **Différence saisonnière** | y(t) - y(t-12) pour les données mensuelles avec saisonnalité annuelle |
| **Termes de Fourier** | Termes sinus et cosinus pour les modèles saisonniers |
### Fonctionnalités d'image (pré-apprentissage profond)
| Fonctionnalité | Descriptif |
|---------|-------------|
| **HOG** (Histogramme de dégradés orientés) | Répartition des directions des bords |
| **LBP** (modèles binaires locaux) | Description des textures |
| **SIFT** (Transformation de fonctionnalités invariantes à l'échelle) | Descripteurs de points clés |
| **Histogrammes de couleurs** | Répartition des couleurs dans l'image |
---

## Meilleures pratiques d'ingénierie des fonctionnalités
| Pratique | Descriptif |
|--------------|-------------|
| **Éviter les fuites de données** | N'utilisez jamais d'informations du futur ou de l'ensemble de test pour créer des fonctionnalités |
| **Documentez tout** | Enregistrez quelles transformations ont été appliquées et pourquoi |
| ** Versionnez vos fonctionnalités ** | Suivre les modifications de fonctionnalités parallèlement aux modifications de modèle |
| **Valider avec et sans** | Tester si une nouvelle fonctionnalité améliore réellement les performances du modèle |
| **Gardez-le reproductible** | Les pipelines d'ingénierie de fonctionnalités doivent être déterministes et reproductibles |
| **Surveiller la dérive des fonctionnalités** | Les distributions de fonctionnalités peuvent changer au fil du temps ; surveiller et recycler |
---

## Résumé
L’ingénierie des fonctionnalités est le point où la connaissance du domaine rencontre l’apprentissage automatique. Il s'agit du processus de transformation de données brutes (désordonnées, incomplètes, de grande dimension) en représentations claires et informatives dont les modèles peuvent tirer des leçons. Les transformations numériques gèrent l'inclinaison et l'échelle. Les encodages catégoriels convertissent les étiquettes en nombres que les modèles peuvent utiliser. Les fonctionnalités de date capturent des modèles temporels. Les stratégies de valeur manquante gèrent des données incomplètes. La sélection des fonctionnalités supprime le bruit et la redondance. Les meilleurs ingénieurs de fonctionnalités pensent comme des détectives : ils demandent quels signaux doivent être présents dans les données, où ces signaux peuvent être cachés et comment les extraire d'une manière honnête (pas de fuite de données), reproductible et robuste pour évoluer dans le temps.