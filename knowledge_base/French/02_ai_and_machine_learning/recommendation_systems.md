---
# Métadonnées
titre : "Systèmes de recommandation"
description: "Filtrage collaboratif, basé sur le contenu, hybride, factorisation matricielle"
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
tags : [recommandation, systèmes, IA et apprentissage automatique]
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
# Systèmes de recommandation
Les systèmes de recommandation prédisent ce qu’un utilisateur voudra voir, acheter ou avec lequel interagir ensuite. Ils alimentent les flux de contenu sur les réseaux sociaux, les suggestions de produits sur les sites de commerce électronique, les sélections de films sur les plateformes de streaming et les résultats de recherche. Bien qu'ils soient invisibles pour la plupart des utilisateurs, ils comptent parmi les systèmes d'IA les plus impactants commercialement au monde : Netflix estime que son moteur de recommandation permet d'économiser plus d'un milliard de dollars par an en réduisant le taux de désabonnement des abonnés.
---

## Pourquoi les recommandations sont difficiles
| Défi | Descriptif |
|---------------|-------------|
| **Échelle** | Millions d'utilisateurs × millions d'éléments = milliards de paires possibles |
| **Disparité** | Chaque utilisateur a interagi avec une infime fraction des éléments disponibles |
| **Démarrage à froid** | Les nouveaux utilisateurs et les nouveaux éléments n'ont pas d'historique d'interaction |
| **Préférences dynamiques** | Les goûts des utilisateurs changent avec le temps |
| **Au-delà de la précision** | Les recommandations doivent également être diverses, nouvelles et fortuites |
| **Objectifs commerciaux** | Maximiser l'engagement ≠ maximiser le bien-être des utilisateurs |
---

## Approches de base
### Filtrage collaboratif
L'idée : si les utilisateurs A et B étaient d'accord dans le passé, ils le seront probablement à l'avenir.
| Tapez | Comment ça marche | Exemple |
|------|-------------|--------------|
| **Basé sur l'utilisateur** | Trouver des utilisateurs similaires ; recommandent ce qu'ils ont aimé | "Les utilisateurs qui ont aimé ont aussi aimé..." |
| **Basé sur les articles** | Trouver des articles similaires à ceux que l'utilisateur aime déjà | "Parce que tu as regardé..." |
| **Factorisation matricielle** | Décomposer la matrice d'interaction utilisateur-élément en facteurs latents | SVD, ALS (moindres carrés alternés) |
| Force | Faiblesse |
|----------|----------|
| Pas besoin de comprendre les éléments eux-mêmes | Problème de démarrage à froid : impossible de recommander de nouveaux éléments |
| Capture les préférences complexes et implicites | Nécessite beaucoup de données d'interaction |
| Fonctionne sur n'importe quel type de contenu | Biais de popularité : recommande des articles déjà populaires |
### Filtrage basé sur le contenu
Recommandez des articles similaires à ceux que l'utilisateur aime déjà, en fonction des caractéristiques de l'article.
| Type de fonctionnalité | Exemple |
|-------------|---------|
| **Texte** | Genre, description, mots-clés, distribution |
| **Audio** | Tempo, genre, ambiance (pour la musique) |
| **Visuel** | Palette de couleurs, style (pour images/mode) |
| **Métadonnées** | Prix, marque, catégorie |
| Force | Faiblesse |
|----------|----------|
| Pas de démarrage à froid des éléments (les fonctionnalités sont connues) | Impossible de recommander des articles qui ne correspondent pas aux goûts existants de l'utilisateur |
| Fonctionne avec moins de données d'interaction | Nécessite une bonne ingénierie des fonctionnalités |
| Explainable ("recommandé car similaire à X") | Moins de hasard |
### Approches hybrides
La plupart des systèmes de production combinent des méthodes collaboratives et basées sur le contenu.
| Stratégie hybride | Descriptif |
|----------------|-------------|
| **Pondéré** | Combiner les scores de plusieurs modèles |
| **Commutation** | Utiliser le contenu pour les nouveaux utilisateurs, le collaboratif pour les utilisateurs établis |
| **Cascade** | Utilisez d'abord un modèle simple, puis affinez-le avec un modèle complexe |
| **Combinaison de fonctionnalités** | Fusionner les fonctionnalités de collaboration et de contenu en un seul modèle |
| **Méta-apprentissage** | Apprenez à combiner différents recommandataires |
---

## Approches modernes d'apprentissage en profondeur
### Modèles à deux tours
L'architecture dominante pour la recommandation à grande échelle (utilisée par YouTube, Pinterest, Spotify).
| Composant | Rôle |
|---------------|------|
| **Tour utilisateur** | Réseau neuronal qui encode les fonctionnalités et l'historique des utilisateurs dans une intégration |
| **Tour d'objets** | Réseau neuronal qui encode les caractéristiques des éléments dans une intégration |
| ** Similitude ** | Produit scalaire ou similarité cosinus entre les incorporations d'utilisateurs et d'éléments |
| Étape | Descriptif |
|------|-------------|
| 1 | Entraînez les deux tours pour produire des intégrations similaires pour les paires utilisateur-élément qui interagissent |
| 2 | Au moment de la diffusion, précalculez les incorporations d'éléments |
| 3 | Pour une demande utilisateur, calculez l'intégration utilisateur |
| 4 | Utilisez la recherche du voisin le plus proche (ANN) pour trouver les éléments les plus similaires |
### Modèles de séquence pour les recommandations
Le comportement des utilisateurs est séquentiel : ce que vous avez regardé hier influence ce que vous regarderez aujourd'hui.
| Modèle | Approche |
|-------|--------------|
| **GRU4Rec** | Modèle basé sur GRU pour les recommandations basées sur les sessions |
| **SASRec** | Recommandeur séquentiel basé sur l'auto-attention |
| **BERT4Rec** | Transformateur bidirectionnel pour recommandations séquentielles |
| **YouTube DNN** | Réseau neuronal profond traitant l’historique des montres comme une séquence |
### Récupération vs classement
Les systèmes modernes divisent les recommandations en deux étapes :
| Scène | Objectif | Méthode |
|-------|---------|--------|
| **Récupération (génération de candidats)** | Limiter des millions d'éléments à environ 1 000 candidats | Modèle à deux tours ; Recherche ANN ; rapide mais approximatif |
| **Classement (notation)** | Noter et classer précisément les candidats | Modèle profond avec de nombreuses fonctionnalités ; plus lent mais précis |
| **Reclassement** | S'adapter à la diversité, aux règles commerciales et à la fraîcheur | Bandits contextuels ; optimisation des contraintes |
---

## Métriques d'évaluation
| Métrique | Ce qu'il mesure | Quand utiliser |
|--------|-------|-------------|
| **Précision@K** | Fraction des recommandations top-K qui sont pertinentes | Lorsque vous vous souciez de l'exactitude des meilleurs choix |
| **Rappel@K** | Fraction des éléments pertinents trouvés dans le top-K | Quand vous avez à cœur de ne pas manquer de bons objets |
| **NDCG** (gain cumulatif actualisé normalisé) | Qualité du classement ; récompenses augmentant les éléments pertinents | Quand l'ordre de classement est important |
| **MAP** (précision moyenne moyenne) | Précision moyenne sur tous les utilisateurs | Qualité globale du classement |
| **Taux de réussite@K** | Si au moins un élément pertinent apparaît dans top-K | Scénarios de pertinence binaire |
| **Couverture** | Fraction des articles recommandés | Diversité et équité |
| **Sérendipité** | Des recommandations inattendues mais pertinentes | Satisfaction des utilisateurs |
---

## Le problème du démarrage à froid
| Scénario | Défi | Solutions |
|----------|-----------|---------------|
| **Nouvel utilisateur** | Aucun historique d'interaction | Utiliser les données démographiques ; afficher les articles populaires ; utiliser des signaux contextuels (emplacement, appareil, heure) |
| **Nouvel article** | Personne n'a encore interagi avec | Utiliser les fonctionnalités de contenu ; stratégies d'exploration-exploitation ; algorithmes de bandits |
| **Nouveau système** | Aucune donnée du tout | Transférer l'apprentissage de domaines similaires ; organiser le contenu initial |
---

## Exploration vs Exploitation
| Stratégie | Descriptif | Compromis |
|--------------|-------------|---------------|
| **ε-gourmand** | Afficher les éléments aléatoires avec une probabilité ε | Simple mais inefficace |
| **Échantillonnage Thompson** | Échantillon de la distribution postérieure de la qualité des articles | Fondé sur des principes ; bonnes propriétés théoriques |
| ** Limite de confiance supérieure (UCB) ** | Préférer les éléments avec une grande incertitude | Bon équilibre entre exploration et exploitation |
| **Bandits contextuels** | Exploration conditionnée au contexte utilisateur | Plus efficace que l'exploration aveugle |
| **Injection de diversité** | Inclure délibérément des éléments divers ou nouveaux | Simple; peut réduire l'engagement à court terme |
---

## Biais et équité
| Type de biais | Descriptif | Impact |
|---------------|-------------|--------|
| **Biais de popularité** | Les articles populaires sont davantage recommandés et deviennent de plus en plus populaires | Les articles à longue traîne sont mal desservis |
| **Biais de sélection** | Les modèles apprennent des interactions observées, mais pas de toutes les interactions possibles | Destiné aux utilisateurs actifs |
| **Biais de position** | Les éléments affichés dans des positions plus élevées génèrent plus de clics, quelle que soit leur qualité | Renforce les premières positions |
| **Biais d'exposition** | Les éléments qui ont été affichés reçoivent plus de signal d'entraînement | Boucle de rétroaction |
| **Biais démographique** | Les recommandations diffèrent de manière injuste selon les données démographiques | Discrimination; mauvaise expérience pour certains groupes |
### Stratégies d'atténuation
| Stratégie | Descriptif |
|--------------|-------------|
| **Pondération de propension inverse** | Articles populaires à faible poids lors de l'entraînement |
| **Couches de débiassage** | Ajouter un composant de débiassage au modèle |
| **Contraintes d'équité** | Ajouter des contraintes pour garantir un traitement équitable |
| **Diverses recommandations** | Optimiser explicitement pour la diversité et la pertinence |
| **Audit et suivi** | Vérifiez régulièrement les recommandations pour détecter les préjugés entre les groupes |
---

## Exemples d'industrie
| Entreprise | Système | Approche |
|---------|--------|--------------|
| **Netflix** | Recommandations cinéma/TV | Récupération à deux tours + classement approfondi + bandits contextuels pour les œuvres d'art |
| **YouTube** | Recommandations vidéo | Réseau neuronal profond pour la génération de candidats ; modèle de classement distinct |
| **Spotify** | Recommandations musicales | Filtrage collaboratif + PNL sur playlists + analyse audio |
| **Amazon** | Recommandations de produits | Filtrage collaboratif élément à élément ; personnalisé à grande échelle |
| **TikTok** | Flux vidéo court | Apprentissage par renforcement ; un fort accent sur l'exploration |
| **Pinterest** | Recommandations visuelles | Modèle à deux tours ; similarité visuelle |
---

## Outils et cadres
| Outil | Objectif |
|------|--------------|
| **Recommandateurs TensorFlow (TFRS)** | Modèles à deux tours, récupération, classement |
| **PyTorch RecSys** | Modèles de recommandation axés sur la recherche |
| **Surprise** | Filtrage collaboratif classique (SVD, NMF, KNN) |
| **Imlicite** | Filtrage collaboratif rapide pour les commentaires implicites (ALS, BPR) |
| **Faiss** (Méta) | Recherche approximative du voisin le plus proche à grande échelle |
| **Milvus / Pomme de pin / Weaviate** | Bases de données vectorielles pour la recherche de similarité |
| **Recbole** | Bibliothèque complète de recherche de recommandations |
| **Merlin** (NVIDIA) | Pipeline de recommandations accéléré par GPU |
---

## Résumé
Les systèmes de recommandation comptent parmi les applications d’IA les plus efficaces de l’industrie. Le domaine a évolué d'un simple filtrage collaboratif à des architectures d'apprentissage en profondeur qui combinent l'historique des utilisateurs, le contenu des éléments, les signaux contextuels et les objectifs commerciaux. Les systèmes modernes utilisent un pipeline de récupération, de classement et de reclassement, avec des modèles à deux tours pour une génération rapide de candidats et des modèles approfondis pour une notation précise. Les défis (démarrage à froid, biais, exploration et équilibre entre la satisfaction des utilisateurs et les objectifs commerciaux) restent des domaines actifs de recherche et d'ingénierie.