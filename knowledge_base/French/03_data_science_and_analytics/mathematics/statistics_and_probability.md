<!--
---
# Metadata
title: "Statistics and Probability"
description: "Probability theory, statistical inference, hypothesis testing, regression, and Bayesian methods"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [statistics, probability, hypothesis-testing, regression, bayesian-methods, data-analysis]
difficulty_level: "intermediate"
prerequisites:
  - "../mathematics/mathematics.md"
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Statistiques et probabilités
Les probabilités et les statistiques constituent les fondements mathématiques de la science des données, de l'apprentissage automatique et de la recherche scientifique. La probabilité vous indique la probabilité que les événements soient probables ; les statistiques vous indiquent comment tirer des conclusions à partir des données. Ensemble, ils transforment l’incertitude en connaissances quantifiables et gérables.
---

## Théorie des probabilités
### Concepts de base
| Concepts | Descriptif | Exemple |
|---------|-------------|---------|
| **Espace d'échantillon** | Ensemble de tous les résultats possibles | Lancer un dé : {1, 2, 3, 4, 5, 6} |
| **Événement** | Un sous-ensemble de l'espace échantillon | Rouler un nombre pair : {2, 4, 6} |
| **Probabilité** | Nombre compris entre 0 et 1 mesurant la vraisemblance | P (rouler 6) = 1/6 |
| **Probabilité conditionnelle** | P(A|B) : la probabilité que A étant donné que B se soit produite | P(pluie | nuageux) |
| **Indépendance** | Événements où l'un n'affecte pas l'autre | Les lancers de pièces sont indépendants |
### Règles de probabilité
| Règle | Formule | Cas d'utilisation |
|------|---------|--------------|
| **Règle d'addition** | P(UNE ∪ B) = P(UNE) + P(B) − P(UNE ∩ B) | Probabilité de A ou B |
| **Règle de multiplication** | P(UNE ∩ B) = P(UNE) × P(B|UNE) | Probabilité de A et B |
| **Règle de complément** | P(pas A) = 1 − P(A) | Probabilité que l'événement ne se produise pas |
| **Loi de la probabilité totale** | P(A) = Σ P(A|Bᵢ) × P(Bᵢ) | Partitionnement par événements mutuellement exclusifs |
| **Théorème de Bayes** | P(UNE|B) = P(B|UNE) × P(UNE) / P(B) | Mettre à jour les croyances avec des preuves |
### Distributions de probabilité
| Distribution | Tapez | Paramètres clés | Cas d'utilisation |
|-------------|------|----------------|--------------|
| **Normal (gaussien)** | Continu | Moyenne (μ), écart type (σ) | Phénomènes naturels, erreurs de mesure |
| **Binôme** | Discret | n (essais), p (probabilité) | Le succès/l'échec compte |
| **Poisson** | Discret | λ (taux) | Événements rares dans le temps/espace |
| **Exponentiel** | Continu | λ (taux) | Temps entre les événements |
| **Uniforme** | Les deux | a, b (limites) | Résultats tout aussi probables |
| **Chi carré** | Continu | k (degrés de liberté) | Tests d'adéquation |
| **t-Distribution** | Continu | ν (degrés de liberté) | Inférence sur petit échantillon |
### Propriétés clés des distributions
| Propriété | Descriptif |
|--------------|-------------|
| **Moyenne (valeur attendue)** | Centre de masse de la distribution : E[X] = Σ xᵢ × P(xᵢ) |
| **Écart** | Etalé autour de la moyenne : Var(X) = E[(X − μ)²] |
| **Écart type** | Racine carrée de la variance ; mêmes unités que les données |
| ** Asymétrie ** | Asymétrie de la distribution |
| **Aplatissement** | "Tailedness" — quel est le poids des queues |
---

## Inférence statistique
### Statistiques descriptives et inférentielles
| | Descriptif | Inférentiel |
|---|-------------|-------------|
| **Objectif** | Résumer et décrire les données | Tirer des conclusions sur une population à partir d'un échantillon |
| **Outils** | Moyenne, médiane, mode, écart type, graphiques | Tests d'hypothèses, intervalles de confiance, régression |
| **Portée** | Seules les données dont vous disposez | Généraliser au-delà de votre échantillon |
### Cadre de test d'hypothèses
| Étape | Descriptif |
|------|-------------|
| 1. **Énumérer des hypothèses** | Hypothèse nulle (H₀) : aucun effet ; Alternative (H₁) : l'effet existe |
| 2. **Choisissez le niveau de signification** | α = 0,05 (conventionnel) |
| 3. **Sélectionnez le test** | Basé sur le type de données, la taille de l'échantillon et les hypothèses |
| 4. **Calculer les statistiques du test** | Dépend du test choisi |
| 5. **Trouver la valeur p** | Probabilité d'observer les données si H₀ est vrai |
| 6. **Prendre une décision** | Si p < α, rejeter H₀ ; sinon, ne parvenez pas à rejeter H₀ |
### Tests statistiques courants
| Test | Quand utiliser | Ce qu'il compare |
|------|-------------|-----------------|
| **test t** | Comparez les moyennes de 1 à 2 groupes | Regrouper les moyennes à une valeur ou les unes aux autres |
| **Test du chi carré** | Données catégorielles | Fréquences observées et attendues |
| **ANOVA** | Comparez les moyennes de 3+ groupes | Variance entre groupes et au sein des groupes |
| **Mann-Whitney U** | Alternative non paramétrique au test t | Répartitions des classements de deux groupes |
| **Corrélation de Pearson** | Relation linéaire entre deux variables continues | valeur r de −1 à +1 |
| **Corrélation de Spearman** | Relation monotone (basée sur le rang) | Valeur ρ pour les données ordinales ou non normales |
### Intervalles de confiance
Un intervalle de confiance donne une plage de valeurs plausibles pour un paramètre de population :
- **IC à 95 % pour la moyenne** (σ connu) : x̄ ± 1,96 × (σ / √n)
- **Interprétation** : "Nous sommes sûrs à 95 % que la véritable moyenne de la population se situe dans cet intervalle"
- **IC plus large** = plus d'incertitude (échantillon plus petit, variabilité plus élevée ou niveau de confiance plus élevé)
---

## Analyse de régression
### Types de régression
| Tapez | Variable dépendante | Cas d'utilisation |
|------|---------|----------|
| **Régression linéaire** | Continu | Prédire les prix des logements, les ventes |
| **Régression logistique** | Binaire (0/1) | Classification : détection de spam, diagnostic de maladies |
| **Régression polynomiale** | Continu (courbé) | Courbes de croissance, tendances non linéaires |
| **Régression multiple** | Continu (2+ prédicteurs) | Contrôler les facteurs confondants |
| **Crête / Lasso** | Continu (régularisé) | Prévention du surapprentissage, sélection des fonctionnalités |
### Bases de la régression linéaire
Le modèle : **y = β₀ + β₁x + ε**
| Composant | Signification |
|-----------|---------|
| β₀ (interception) | Valeur de y lorsque x = 0 |
| β₁ (pente) | Changement de y pour un changement d'une unité de x |
| ε (terme d'erreur) | Variation inexpliquée |
**Mesures clés :**
- **R² (coefficient de détermination)** : Proportion de variance expliquée par le modèle (0 à 1)
- **R² ajusté** : R² pénalisé pour le nombre de prédicteurs
- **RMSE** : erreur quadratique moyenne — erreur de prédiction moyenne dans les mêmes unités que y
### Hypothèses de régression linéaire
| Hypothèse | Ce que cela signifie | Comment vérifier |
|---------------|--------------|--------------|
| **Linéarité** | La relation entre X et Y est linéaire | Nuages ​​de points |
| **Indépendance** | Les observations sont indépendantes | Conception de l'étude |
| **Homoscédasticité** | Variance constante des résidus | Parcelles résiduelles |
| **Normalité** | Les résidus sont normalement distribués | Graphique Q-Q, test de Shapiro-Wilk |
| **Pas de multicolinéarité** | Les prédicteurs ne sont pas fortement corrélés | VIF (Facteur d'Inflation de Variance) |
---

## Statistiques bayésiennes
### Fréquentiste vs bayésien
| | Fréquentiste | Bayésien |
|---|-------------|--------------|
| **La probabilité signifie** | Fréquence à long terme | Degré de croyance |
| **Les paramètres sont** | Corrigé mais inconnu | Variables aléatoires avec distributions |
| **Utilisations** | valeurs p, intervalles de confiance | Distributions a posteriori, intervalles crédibles |
| **Forces** | Objectif bien établi | Intègre les connaissances préalables et l'interprétation intuitive |
### Théorème de Bayes en pratique
** Postérieur = (Probabilité × Antérieur) / Preuve **
Exemple — tests médicaux :
- Prévalence de la maladie : 1 % (avant)
- Sensibilité du test : 95 % (taux de vrais positifs)
- Spécificité du test : 90% (taux de vrais négatifs)
- Si votre test est positif : P(maladie | positif) = (0,95 × 0,01) / (0,95 × 0,01 + 0,10 × 0,99) ≈ 8,8 %
Ce résultat contre-intuitif – la plupart des résultats positifs sont des faux positifs lorsque la maladie est rare – est l’**erreur du taux de base**, et il montre pourquoi la pensée bayésienne est importante.
---

## Conseils pratiques
- **Visualisez toujours vos données** avant d'exécuter un test statistique
- **Vérifiez les hypothèses** — les violations peuvent invalider les résultats
- **La taille de l'effet compte** — un résultat statistiquement significatif peut être pratiquement dénué de sens
- **Une corrélation n'est pas un lien de causalité** — même des corrélations fortes peuvent avoir des facteurs confondants
- **Des comparaisons multiples** gonflent les taux de faux positifs — appliquez des corrections (Bonferroni, FDR)
- **Rapportez les intervalles de confiance**, pas seulement les valeurs p
---

## Pourquoi c'est important
Les statistiques constituent l’épine dorsale de la recherche scientifique, de l’analyse commerciale et de l’apprentissage automatique. Sans cela, vous ne pouvez pas distinguer le signal du bruit, identifier les effets réels des fluctuations aléatoires ou faire des prédictions avec une incertitude quantifiée. Que vous analysiez des tests A/B, formiez des modèles ML ou lisiez des articles de recherche, les connaissances statistiques sont essentielles.