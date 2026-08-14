<!--
---
# Metadata
title: "Data Visualization"
description: "Chart selection, design principles, storytelling, tools"
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
tags: [data, visualization, data-science-and-analytics]
difficulty_level: "intermediate"
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
# Visualisation des données
Un graphique bien conçu peut révéler des modèles que cachent les tableaux de nombres. Un texte mal conçu peut induire en erreur, confondre ou ennuyer. La visualisation des données consiste à transformer les données en histoires visuelles qui éclairent les décisions. Ce fichier couvre la sélection des graphiques, les principes de conception, les erreurs courantes et les outils qui rendent tout cela possible.
---

## Choisir le bon graphique
La décision la plus importante dans toute visualisation consiste à choisir le type de graphique adapté à vos données et à votre message.
### Guide de sélection des graphiques
| Votre objectif | Meilleurs types de graphiques |
|---------------|-----------------|
| **Comparez les catégories** | Graphique à barres, graphique à barres groupées |
| **Afficher le changement au fil du temps** | Graphique linéaire, graphique en aires |
| **Afficher la distribution** | Histogramme, boîte à moustaches, intrigue en violon |
| **Afficher la relation** | Nuage de points, graphique à bulles |
| **Afficher la composition** | Barres empilées, diagramme circulaire (tranches limitées), treemap |
| **Afficher la corrélation** | Nuage de points, carte thermique, diagramme de paires |
| **Afficher le classement** | Graphique à barres horizontales |
| **Afficher les modèles géographiques** | Carte choroplèthe, carte à points |
| **Afficher la partie vers le tout au fil du temps** | Graphique en aires empilées |
### Quand utiliser chaque graphique
| Graphique | Points forts | À éviter quand |
|-------|-----------|---------------|
| **Bar** | Comparaisons claires entre les catégories | Trop de catégories (>15) |
| **Ligne** | Tendances au fil du temps ; données continues | Les données ne sont pas séquentielles |
| **Dispersion** | Relations entre deux variables | Trop de points qui se chevauchent |
| **Histogramme** | Forme de distribution d'une variable | Petits échantillons (<20) |
| **Box plot** | Summary statistics + outliers; compare distributions | Audience unfamiliar with them |
| **Heatmap** | Correlation matrices; patterns in 2D data | Too many variables |
| **Pie chart** | Simple composition (2–5 slices) | More than 5 slices; precise comparisons needed |
| **Violin plot** | Distribution density + quartiles | Small audiences unfamiliar with them |
| **Pair plot** | Quick overview of all variable relationships | Many variables (>8) |
---

## Principes de conception
### Les idées fondamentales de Tufte
Les principes d'Edward Tufte restent la référence en matière de visualisation de données :
| Principe | Descriptif |
|---------------|-------------|
| **Maximiser le rapport données-encre** | Chaque goutte d’encre doit véhiculer des données. Supprimez tout le reste. |
| **Éliminer les déchets graphiques** | Pas d'effets 3D, de dégradés gratuits ou d'éléments décoratifs. |
| **Afficher les données** | Ne déformez pas, ne cachez pas et ne sélectionnez pas. Laissez parler les données. |
| **Petits multiples** | Utilisez de petits graphiques répétés pour comparer les catégories. |
| **Sparklines** | De minuscules graphiques de la taille d'un mot pour les données de tendance en ligne. |
### Règles de conception pratiques
| Règle | Pourquoi |
|------|-----|
| **Démarrer l'axe Y à zéro** (pour les graphiques à barres) | Sinon, vous exagérez les différences |
| **Étiquetez directement** | Mettez des étiquettes sur les lignes/barres au lieu d'utiliser une légende lorsque cela est possible |
| **Utilisez la couleur à bon escient** | Mettez en valeur ce qui compte ; utiliser le gris pour le contexte |
| **Gardez les choses simples** | Un message par graphique ; ne surchargez pas |
| **Utilisez des échelles cohérentes** | Lorsque vous comparez des graphiques, conservez les mêmes axes |
| **Commandez de manière significative** | Trier les barres par valeur (et non par ordre alphabétique) sauf s'il existe un ordre naturel |
| **Fournir le contexte** | Ajouter des références, des objectifs ou des moyennes historiques |
### Directives de couleur
| Cas d'utilisation | Approche |
|----------|----------|
| **Catégorique** | Teintes distinctes (bleu, orange, vert, rouge) — 7 à 8 catégories maximum |
| **Séquentiel** | Clair à foncé d'une teinte (bleu clair → bleu foncé) |
| **Divergent** | Dégradé de deux teintes pour les données avec un point médian significatif (rouge ← blanc → bleu) |
| **Accessibilité** | Testez avec des simulateurs de daltonisme ; ne comptez pas uniquement sur la couleur (ajoutez des étiquettes ou des motifs) |
---

## Narration avec des données
Un graphique sans récit n’est qu’une image. La narration transforme les données en informations.
### Le cadre de narration
1. **Contexte** : Quelle est la situation ? Que sait déjà le public ?
2. **Conflit** : quel est le problème, la surprise ou la tension dans les données ?
3. **Résolution** : Que doit faire le public avec cet aperçu ?
### Conseils pratiques
| Astuce | Descriptif |
|-----|-------------|
| ** Dirigez avec la perspicacité ** | Titrez le graphique avec les points à retenir, pas les données (« Les revenus ont augmenté de 30 % » et non « Les revenus par trimestre ») |
| **Annoter les points clés** | Ajoutez des légendes de texte pour des événements importants ou des tournants |
| **Utiliser la divulgation progressive** | Afficher un graphique à la fois ; construire l'histoire étape par étape |
| **Soulignez ce qui compte** | Utilisez la couleur ou la taille pour attirer l'attention sur le point de données clé |
| **Fournir un "et alors ?"** | Chaque graphique doit répondre à une question ou inciter à une action |
---

## Erreurs courantes
| Erreur | Pourquoi c'est mauvais | Corriger |
|---------|-------------|-----|
| **Axe Y tronqué** | Exagère les petites différences | Commencer à zéro pour les graphiques à barres |
| **Plage horaire de cueillette** | Induire en erreur sur les tendances | Afficher toute la gamme disponible |
| **Trop de couleurs** | Submerge le spectateur | Limiter à 5-7 ; utiliser le gris pour le contexte |
| **Double axe Y** | Implique une corrélation qui peut ne pas exister | Utiliser deux graphiques distincts |
| **Graphiques 3D** | Déforme les proportions | Utilisez toujours 2D |
| **Graphiques circulaires avec plus de 10 tranches** | Impossible de comparer | Utilisez plutôt un graphique à barres |
| **Étiquettes manquantes** | Le spectateur ne comprend pas le graphique | Toujours étiqueter les axes, le titre et les unités |
| **Graphiques en aires trompeuses** | Les zones empilées faussent la perception des séries individuelles | Utilisez des graphiques linéaires ou de petits multiples |
---

## Outils
###Python
| Bibliothèque | Force |
|---------|----------|
| **matplotlib** | Fondation du traçage Python ; entièrement personnalisable |
| **né de la mer** | Visualisation statistique ; beaux défauts ; construit sur matplotlib |
| **intrigue** | Graphiques interactifs basés sur le Web ; tableaux de bord |
| **altaïr** | Grammaire déclarative des graphiques (Vega-Lite) |
| **bokeh** | Visualisation interactive pour les navigateurs |
### JavaScript/Web
| Bibliothèque | Force |
|---------|----------|
| **D3.js** | Flexibilité maximale ; courbe d'apprentissage abrupte |
| **Graphique.js** | Graphiques simples et réactifs |
| **Rechargements** | Cartographie conviviale |
| **Tracé observable** | Grammaire graphique légère et expressive |
### Outils No-Code / BI
| Outil | Tapez |
|------|------|
| **Tableau** | Analyse visuelle conforme aux normes de l'industrie |
| **Power BI** | Écosystème Microsoft ; BI d'entreprise |
| **Observateur** | Google Cloud ; exploration de données |
| **Métabase** | Source ouverte ; configuration simple |
| **Surensemble Apache** | Source ouverte ; SQL natif |
---

## Conception du tableau de bord
Un tableau de bord est un ensemble de visualisations qui, ensemble, racontent une histoire complète sur un processus, un système ou une entreprise.
### Types de tableaux de bord
| Tapez | Public | Objectif |
|------|----------|---------|
| **Stratégique** | Dirigeants | KPI de haut niveau ; tendances à long terme |
| **Opérationnel** | Gestionnaires | Surveillance en temps réel ; opérations quotidiennes |
| **Analyse** | Analystes | Exploration profonde ; filtrage, exploration |
### Liste de contrôle de conception
- **Connaissez votre audience** : quelles décisions prendront-ils à partir de ce tableau de bord ?
- **Règle des 5 secondes** : le point principal à retenir peut-il être compris en 5 secondes ?
- **Mise en page** : statistiques les plus importantes en haut à gauche (là où les yeux vont en premier).
- **Types de graphiques limités** : 3 à 4 types maximum par tableau de bord pour plus de cohérence.
- **Interactif par défaut** : filtres, sélecteurs de plage de dates, analyses approfondies.
- **Performance** : les tableaux de bord dont le chargement prend plus de 5 secondes ne sont pas utilisés.
- **Mobile** : envisagez une conception réactive si les utilisateurs en ont besoin en déplacement.
---

## Résumé
Une bonne visualisation des données est une question de clarté, d’honnêteté et d’impact. Choisissez le bon graphique pour vos données. Supprimez tout ce qui ne sert pas le message. Utilisez la couleur et les annotations pour guider le spectateur. Et laissez toujours les données raconter l’histoire, et non l’inverse.