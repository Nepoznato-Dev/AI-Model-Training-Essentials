---
# Métadonnées
titre : "Séries chronologiques et prévisions"
description : "ARIMA, Prophet, LSTM, saisonnalité, détection d'anomalies"
catégorie : "IA et Machine Learning"
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
review_by : "Équipe de base de connaissances sur l'IA et l'apprentissage automatique"
next_review : "2027-08-05"
#Classement
tags : [temps, séries, prévisions, IA et apprentissage automatique]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "8 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Séries chronologiques et prévisions
Les données de séries chronologiques sont toutes les données collectées au fil du temps : cours des actions, relevés de température, trafic sur un site Web, chiffres de ventes, moniteurs de fréquence cardiaque, consommation d'énergie. La prévision signifie prédire les valeurs futures sur la base de modèles passés. Il s’agit de l’une des applications pratiques les plus précieuses de la science des données – et l’une des plus difficiles, car l’avenir est véritablement incertain et les séries chronologiques du monde réel sont pleines de bruit, de saisonnalité et de ruptures structurelles.
---

## Caractéristiques des séries chronologiques
| Composant | Descriptif | Exemple |
|---------------|-------------|---------|
| **Tendance** | Augmentation ou diminution à long terme | Les températures mondiales augmentent au fil des décennies |
| **Saisonnalité** | Modèles réguliers et prévisibles à intervalles fixes | Les ventes au détail augmentent chaque mois de décembre |
| **Cyclicité** | Fluctuations à intervalles non fixes (souvent économiques) | Récessions tous les 5 à 10 ans |
| **Bruit (résiduel)** | Variation aléatoire qui ne peut être expliquée | Mouvements quotidiens du cours des actions |
| **Autocorrélation** | Les valeurs actuelles dépendent des valeurs passées | La température d'aujourd'hui est similaire à celle d'hier |
### Stationnarité
Une série chronologique est **stationnaire** si ses propriétés statistiques (moyenne, variance) ne changent pas dans le temps. La plupart des méthodes de prévision supposent la stationnarité.
| Test | Objectif |
|------|--------------|
| **Dickey-Fuller augmenté (ADF)** | Teste si une racine unitaire est présente (non stationnaire) |
| **Test KPSS** | Teste si la série est tendance-stationnaire |
| Transformations | Quand utiliser |
|---------------|-------------|
| **Différence** | Supprimer la tendance : y'(t) = y(t) - y(t-1) |
| **Transformation du journal** | Stabiliser la variance (pour une croissance exponentielle) |
| **Différence saisonnière** | Supprimer la saisonnalité : y'(t) = y(t) - y(t-s) où s est la durée de la saison |
---

## Méthodes de prévision classiques
### Moyennes mobiles
| Méthode | Descriptif | Idéal pour |
|--------|-------------|--------------|
| **Moyenne mobile simple (SMA)** | Moyenne des N dernières observations | Lissage des données bruitées |
| **Moyenne mobile pondérée** | Les observations plus récentes obtiennent un poids plus élevé | Quand les données récentes comptent davantage |
| **Moyenne mobile exponentielle (EMA)** | Poids décroissants exponentiellement | Suivre les tendances avec moins de décalage |
### Lissage exponentiel
| Méthode | Composants | Cas d'utilisation |
|--------|-----------|--------------|
| **Simple (SES)** | Niveau uniquement | Pas de tendance, pas de saisonnalité |
| **Holt's (Double)** | Niveau + tendance | Données avec tendance mais pas de saisonnalité |
| **Holt-Winters (Triple)** | Niveau + tendance + saisonnalité | Données avec tendance et saisonnalité |
### ARIMA et variantes
ARIMA (AutoRegressive Integrated Moving Average) est le cheval de bataille de la prévision de séries chronologiques classiques.
| Composant | Signification | Paramètre |
|-----------|---------|---------------|
| **AR (p)** | Régression sur les valeurs p précédentes | Combien de valeurs passées utiliser |
| **Je (d)** | Nombre d'étapes de différenciation pour rendre stationnaire | Combien de fois faire la différence |
| **MA (q)** | Modéliser l'erreur comme une combinaison d'erreurs passées | Combien d'erreurs passées utiliser |
| Variante | Rallonge | Cas d'utilisation |
|---------|-----------|--------------|
| **SARIMA** | Ajoute des composants saisonniers (P, D, Q, s) | Données à forte saisonnalité |
| **ARIMAX** | Ajoute des variables externes | Quand vous êtes informé des événements à venir |
| **VAR** | ARIMA multivarié ; séries multiples interdépendantes | Quand les variables s'influencent mutuellement |
---

## Approches modernes du ML
### Modèles basés sur LSTM et RNN
| Modèle | Architecture | Avantage |
|-------|-------------|---------------|
| **LSTM** | Réseau de mémoire à long terme | Capture les dépendances temporelles à longue portée |
| **GRU** | Unité récurrente fermée (LSTM plus simple) | Formation plus rapide ; performances similaires |
| **Seq2Seq** | Encodeur-décodeur pour séries temporelles | Longueurs d'entrée/sortie flexibles |
| **Réseau convolutif temporel (TCN)** | Circonvolutions causales dilatées | Formation parallèle ; champ récepteur long |
### Prophète (méta)
Un outil de prévision pratique conçu pour les séries chronologiques commerciales.
| Fonctionnalité | Descriptif |
|---------|-------------|
| **Décomposition** | Tendance + saisonnalité + vacances |
| **Flexible** | Gère les données manquantes, les valeurs aberrantes et les ruptures structurelles |
| **Interprétable** | Les composants sont lisibles par l'homme |
| **Automatique** | Défauts raisonnables ; réglage minimal requis |
| Force | Limitation |
|--------------|------------|
| Idéal pour les indicateurs commerciaux (ventes, utilisateurs) | Pas idéal pour les données à très haute fréquence |
| Gère les vacances et les événements spéciaux | Suppose une saisonnalité additive ou multiplicative |
| Robuste aux valeurs aberrantes | Moins précis que l'apprentissage profond pour les modèles complexes |
### Modèles basés sur des transformateurs
| Modèle | Caractéristique clé |
|-------|-------------|
| **Informateur** | ProbAttention rare pour les longues séquences |
| **Autoformeur** | Mécanisme d'autocorrélation pour la décomposition en série |
| **PatchTST** | Corrige la série chronologique ; indépendant du canal |
| **TimesFM** (Google) | Modèle de base pour les séries chronologiques ; pré-formés sur des données diverses |
| **Chronos** (Amazon) | Tokenise les séries chronologiques ; utilise une architecture de style LLM |
---

## Détection d'anomalies dans les séries chronologiques
Détecter des modèles inhabituels qui s'écartent du comportement attendu.
| Méthode | Approche | Cas d'utilisation |
|--------|----------|--------------|
| **Statistique** | Score Z, IQR, cartes de contrôle | Simple, bien compris |
| **Forêt d'isolement** | Basé sur des arbres ; isole les anomalies par partitionnement aléatoire | Détection d'anomalies multivariées |
| **LOF** (Facteur de valeur aberrante locale) | Basé sur la densité ; compare la densité locale à celle des voisins | Quand les anomalies se situent dans des régions à faible densité |
| **Encodeurs automatiques** | Erreur de reconstruction ; erreur élevée = anomalie | Modèles complexes et non linéaires |
| **Basé sur LSTM** | Prédire la prochaine étape ; grande erreur de prédiction = anomalie | Anomalies séquentielles |
### Candidatures
| Domaine | Que signifient les anomalies |
|--------|---------|
| **Finances** | Fraude, krachs boursiers, krachs éclair |
| **Soins de santé** | Fréquence cardiaque anormale, apparition de crises |
| **Fabrication** | Panne d'équipement, défauts de qualité |
| **Cybersécurité** | Tentatives d'intrusion, attaques DDoS |
| **Infrastructures** | Surcharge du serveur, pannes de réseau |
---

## Métriques d'évaluation
| Métrique | Formule (conceptuelle) | Quand utiliser |
|--------|-----------|-------------|
| **MAE** (erreur absolue moyenne) | Moyenne des erreurs absolues | Interprétable; mêmes unités que les données |
| **RMSE** (erreur quadratique moyenne) | Racine carrée des erreurs quadratiques moyennes | Pénalise davantage les grosses erreurs |
| **MAPE** (Pourcentage d'erreur absolu moyen) | Moyenne des erreurs en pourcentage absolu | Quand l'erreur relative compte |
| **SMAPE** (MAPE symétrique) | Version symétrique de MAPE | Gère mieux les valeurs proches de zéro |
| **MASE** (erreur d'échelle absolue moyenne) | MAE par rapport à une prévision naïve | Comparaison entre différentes séries |
---

## Flux de travail pratique
| Étape | Descriptif |
|------|-------------|
| **1. Explorer** | Tracez la série ; identifier la tendance, la saisonnalité, les valeurs aberrantes |
| **2. Décomposer** | Séparer en composants tendance, saisonniers et résiduels |
| **3. Stationner** | Appliquer des différenciations ou des transformations si nécessaire |
| **4. Divisé** | Répartition temporelle (jamais de répartition aléatoire pour les séries chronologiques) |
| **5. Référence** | Commencez avec une prévision naïve (dernière valeur, saisonniere naïve) |
| **6. Modèle** | Essayez les méthodes classiques (ARIMA, Prophet), puis les méthodes ML |
| **7. Évaluer** | Utiliser des mesures appropriées ; comparer à la ligne de base |
| **8. Itérer** | Ajoutez des fonctionnalités, essayez différents modèles, ajustez les hyperparamètres |
---

## Outils et bibliothèques
| Outil | Objectif |
|------|--------------|
| **modèles de statistiques** | Séries temporelles classiques (ARIMA, ETS, décomposition) |
| **Prophète** (Méta) | Prévisions de séries chronologiques commerciales |
| **heure de jeu** | Interface ML unifiée pour les séries chronologiques |
| **Fléchettes** | Bibliothèque de prévisions complète (classique + deep learning) |
| **GluonTS** (Amazon) | Modélisation de séries chronologiques probabilistes |
| **NeuralProphète** | Prophète avec des composants de réseau neuronal |
| **tsfresh** | Extraction automatique des caractéristiques des séries chronologiques |
| **pandas** | Manipulation et rééchantillonnage de séries chronologiques |
---

## Résumé
La prévision de séries chronologiques associe les statistiques classiques à l’apprentissage automatique moderne. Les méthodes classiques (ARIMA, lissage exponentiel, Prophet) sont interprétables, rapides et souvent étonnamment précises. Les méthodes d'apprentissage profond (LSTM, Transformers) capturent des modèles complexes mais nécessitent plus de données et de réglages. Les principes clés restent les mêmes quelle que soit la méthode : comprenez la structure de vos données (tendance, saisonnalité, bruit), comparez toujours par rapport à une base de référence simple, évaluez avec des mesures appropriées et rappelez-vous que l'avenir n'est jamais une répétition parfaite du passé.