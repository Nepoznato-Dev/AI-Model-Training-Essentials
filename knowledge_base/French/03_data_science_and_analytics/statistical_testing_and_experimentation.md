<!--
---
# Metadata
title: "Statistical Testing and Experimentation"
description: "Hypothesis testing, A/B testing, effect size, causal inference"
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
tags: [statistical, testing, experimentation, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Tests statistiques et expérimentation
Les statistiques sont la grammaire de la science. Il vous donne les outils nécessaires pour distinguer les modèles réels du bruit aléatoire, pour mesurer si un changement a réellement amélioré les choses et pour prendre des décisions dans l'incertitude. Ce fichier couvre les concepts fondamentaux du test d'hypothèses, de la conception expérimentale et des pièges courants qui font trébucher les gens.
---

## Le cadre de test d'hypothèse
Chaque test statistique suit la même logique :
1. **Énoncez l'hypothèse nulle (H₀)** : Il n'y a aucun effet / aucune différence.
2. **Énoncez l'hypothèse alternative (H₁)** : Il y a un effet / une différence.
3. **Choisissez un niveau de signification (α)** : généralement 0,05 (5 % de chance de faux positif).
4. **Collectez des données et calculez une statistique de test**.
5. **Calculez la valeur p** : Probabilité d'observer ce résultat (ou plus extrême) si H₀ est vrai.
6. **Prenez une décision** : Si p < α, rejetez H₀ (statistiquement significatif). Sinon, ne parvenez pas à rejeter H₀.
### Concepts clés
| Concepts | Signification | Idée fausse courante |
|---------|---------|-----------|
| **valeur p** | P(données \| H₀ est vraie) | PAS "la probabilité que H₀ soit vrai" |
| **α (niveau de signification)** | Seuil de rejet de H₀ | Pas une mesure de l'importance de l'effet |
| **importance statistique** | Résultat improbable dû au seul hasard | Ne signifie PAS pratiquement significatif |
| **Taille de l'effet** | Ampleur de l'effet observé | Séparé de la valeur p ; un effet minime peut être significatif avec un grand N |
| **Puissance** | Probabilité de rejeter correctement un faux H₀ | Visez généralement 80 %+ |
| **Intervalle de confiance** | Plage de valeurs plausibles pour le paramètre | Un IC à 95 % ne signifie pas « 95 % de probabilité que la vraie valeur se situe dans cette plage » |
---

## Types d'erreurs
| | H₀ est vrai | H₀ est faux |
|---|-----------|------------|
| **Rejeter H₀** | Erreur de type I (faux positif) | ✅ Correct (vrai positif) |
| **Échec du rejet de H₀** | ✅ Correct (vrai négatif) | Erreur de type II (faux négatif) |
| Erreur | Symbole | Signification |
|-------|--------|---------|
| **Type I** | α | Conclure qu'il y a un effet quand il n'y en a pas |
| **Type II** | β | Il manque un véritable effet |
---

## Choisir le bon test
| Scénario | Test | Hypothèses |
|--------------|------|-------------|
| Comparer les moyennes de 2 groupes | **t-test** (indépendant) | Distribution normale, variance égale |
| Comparer les moyennes d'observations appariées | **Test t apparié** | Les différences sont normalement distribuées |
| Comparez les moyennes de 3+ groupes | **ANOVA** | Distribution normale, variance égale |
| Comparez les distributions catégorielles | **Test du chi carré** | Taille d'échantillon suffisante par cellule |
| Comparer les distributions (non paramétriques) | **Mann-Whitney U** | Aucune hypothèse de normalité |
| Comparez plus de 3 groupes (non paramétriques) | **Kruskal-Wallis** | Aucune hypothèse de normalité |
| Corrélation des tests | **Pearson** (linéaire) ou **Spearman** (monotonique) | Pearson : normalité ; Spearman : basé sur le classement |
| Tester si les données suivent une distribution | **Kolmogorov-Smirnov** | Données continues |
### Paramétrique vs non paramétrique
| | Paramétrique | Non paramétrique |
|---|-----------|---------------|
| **Hypothèses** | Les données suivent une distribution spécifique (généralement normale) | Aucune hypothèse de distribution |
| **Puissance** | Plus élevé lorsque les hypothèses sont remplies | Plus bas, mais plus robuste |
| **Quand utiliser** | Grands échantillons, données approximativement normales | Petits échantillons, données asymétriques, données ordinales |
---

## Tests spécifiques en détail
### Test t
Compare les moyennes de deux groupes.
| Variante | Cas d'utilisation |
|---------|----------|
| **Test t indépendant** | Deux groupes distincts (traitement vs contrôle) |
| **Test t apparié** | Même groupe mesuré deux fois (avant vs après) |
| **Test t sur un échantillon** | Comparer la moyenne d'un échantillon à une valeur connue |
```python
from scipy import stats

# Independent t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)
```

### ANOVA (Analyse de Variance)
Compare les moyennes de 3 groupes ou plus. Teste si au moins une moyenne de groupe diffère des autres.
| Tapez | Conception |
|------|--------|
| **ANOVA unidirectionnelle** | Une variable indépendante avec 3+ niveaux |
| **ANOVA bidirectionnelle** | Deux variables indépendantes ; teste les effets d'interaction |
| **ANOVA à mesures répétées** | Mêmes sujets mesurés dans des conditions différentes |
Si l'ANOVA est significative, effectuez un suivi avec des **tests post-hoc** (HSD de Tukey) pour découvrir quels groupes spécifiques diffèrent.
### Test du chi carré
Teste si deux variables catégorielles sont indépendantes.
| Cas d'utilisation | Exemple |
|----------|---------|
| **Test d'indépendance** | Le sexe est-il associé à la préférence en matière de produit ? |
| **Bon ajustement** | Un jet de dé suit-il une distribution uniforme ? |
**Règle générale** : chaque cellule doit avoir un nombre attendu d'au moins 5.
---

## Tests A/B
Les tests A/B sont l'application de tests d'hypothèses aux décisions commerciales, comparant généralement un contrôle (A) à une variante (B).
### Processus de conception
| Étape | Descriptif |
|------|-------------|
| **1. Définir l'hypothèse** | "Changer la couleur du bouton du bleu au vert augmentera le taux de clics" |
| **2. Choisissez la métrique** | Primaire : taux de clics. Secondaire : taux de conversion, revenus. |
| **3. Calculer la taille de l'échantillon** | Basé sur l'effet minimum détectable, la puissance (80 %) et la signification (5 %) |
| **4. Randomiser** | Assignez aléatoirement les utilisateurs au contrôle et au traitement |
| **5. Exécuter le test** | Collecter des données jusqu'à ce que la taille d'échantillon cible soit atteinte |
| **6. Analyser** | Comparez les métriques à l'aide d'un test statistique approprié |
| **7. Décider** | Mettre en œuvre si statistiquement et pratiquement significatif |
### Calcul de la taille de l'échantillon
La taille de l'échantillon dont vous avez besoin dépend de :
| Facteur | Effet sur la taille de l'échantillon |
|--------|----------------------|
| **Effet plus petit à détecter** | Besoin de plus d'échantillons |
| **Puissance supérieure** | Besoin de plus d'échantillons |
| **Niveau de signification inférieur** | Besoin de plus d'échantillons |
| **Écart plus élevé** | Besoin de plus d'échantillons |
### Erreurs courantes dans les tests A/B
| Erreur | Pourquoi c'est faux |
|---------|---------------|
| **Un coup d'oeil tôt** | La vérification quotidienne des résultats gonfle le taux de faux positifs |
| **Plusieurs métriques sans correction** | Test de 20 métriques à α=0,05 → attendre 1 faux positif par hasard |
| **Arrêt avant la cible N** | Un test sous-alimenté ne parvient pas à détecter les effets réels |
| **Ignorer la saisonnalité** | Exécution d'un test sur une période de vacances par rapport à une semaine normale |
| **Affectation non aléatoire** | Biais de sélection (par exemple, affectation de nouveaux utilisateurs au traitement) |
| **Confondre signification et importance** | Une augmentation de 0,1 % peut être statistiquement significative mais ne vaut pas la peine d'être expédiée |
---

## Comparaisons multiples
Lorsque vous exécutez plusieurs tests simultanément, le risque d’obtenir au moins un faux positif augmente considérablement.
| Nombre d'essais | Probabilité de ≥1 faux positif (à α=0,05) |
|----------------|----------------------------------------------|
| 1 | 5% |
| 5 | 23% |
| 10 | 40% |
| 20 | 64% |
### Corrections
| Méthode | Comment ça marche | Quand utiliser |
|--------|-------------|-------------|
| **Bonferroni** | Divisez α par le nombre de tests (α/n) | Conservateur; quelques comparaisons |
| **Holm-Bonferroni** | Procédure de déclassement ; moins conservateur | Usage général |
| **Benjamini-Hochberg (FDR)** | Contrôle le taux de fausses découvertes | De nombreux tests ; analyse exploratoire |
---

## Taille de l'effet
Les valeurs P vous indiquent *si* un effet existe. La taille de l'effet vous indique *quelle est sa taille*.
| Mesurer | Pour | Interprétation |
|---------|-----|---------------|
| **La merde de Cohen** | Différence entre deux moyennes | 0,2 = petit, 0,5 = moyen, 0,8 = grand |
| **Le r** de Pearson | Corrélation | 0,1 = petit, 0,3 = moyen, 0,5 = grand |
| **η² (êta-carré)** | ANOVA | 0,01 = petit, 0,06 = moyen, 0,14 = grand |
| **Rapport de cotes** | Résultats catégoriques | 1,0 = aucun effet ; >1 ou <1 = effet |
**Indiquez toujours l'ampleur de l'effet avec les valeurs p.** Un résultat peut être statistiquement significatif mais pratiquement dénué de sens.
---

## Bayésien vs fréquentiste
| Aspects | Fréquentiste | Bayésien |
|--------|------------|----------|
| **Probabilité** | Fréquence des événements à long terme | Degré de croyance |
| **Paramètres** | Corrigé mais inconnu | Variables aléatoires avec distributions |
| **Utilisations** | valeurs p, intervalles de confiance, tests d'hypothèses | Distributions a posteriori, intervalles crédibles |
| **Avant** | Aucune croyance antérieure incorporée | Distribution préalable explicite |
| **Interprétation** | "Si nous répétions cette expérience plusieurs fois..." | "Compte tenu des données, la probabilité que..." |
| **Forces** | Objectif, bien établi, simple | Interprétation intuitive, intègre les connaissances préalables |
| **Faiblesses** | Les valeurs p largement mal comprises | Le choix du prior peut être subjectif |
---

## Bases de l'inférence causale
La corrélation n’est pas la causalité. Mais parfois, vous avez besoin de savoir *si X a causé Y*, pas seulement s'ils sont associés.
| Méthode | Descriptif | Quand utiliser |
|--------|-------------|-------------|
| **Expériences randomisées** | L’étalon-or ; l'assignation aléatoire élimine les facteurs de confusion | Quand pouvez-vous randomiser |
| **Différence dans les différences (DiD)** | Comparer les changements au fil du temps entre le traitement et le contrôle | Changements de politique, expériences naturelles |
| **Discontinuité de régression (RDD)** | Exploiter un seuil de coupure | Bourses, seuils d'éligibilité |
| **Variables instrumentales (IV)** | Utiliser un instrument qui affecte le traitement mais pas directement le résultat | Quand la randomisation n'est pas possible |
| **Correspondance du score de propension** | Faire correspondre les unités traitées et témoins sur les caractéristiques observées | Études observationnelles |
---

## Erreurs statistiques courantes
| Erreur | Descriptif |
|---------|-------------|
| **p-piratage** | Essayer de nombreuses analyses jusqu'à ce que vous trouviez p <0,05 |
| **ÉCOUTER** | Faire des hypothèses une fois les résultats connus |
| **Biais de survie** | Regarder uniquement les réussites (par exemple, les entreprises qui réussissent) |
| **Le paradoxe de Simpson** | La tendance s'inverse lorsque les données sont agrégées ou divisées par groupe |
| **Négligence du taux de base** | Ignorer la probabilité a priori lors de l'interprétation des résultats |
| **Erreur écologique** | Déduire un comportement individuel à partir de données au niveau du groupe |
| **Confondant** | Une troisième variable explique la relation observée |
| **Surapprentissage** | Le modèle capture le bruit, pas le signal |
---

## Résumé
Les tests statistiques consistent à prendre des décisions dans l’incertitude avec honnêteté intellectuelle. Énoncez toujours vos hypothèses avant de collecter des données. Choisissez le bon test pour votre type de données. Signalez les tailles d’effet, pas seulement les valeurs p. Correct pour plusieurs comparaisons. Et rappelez-vous : la signification statistique n’est pas la même chose que la signification pratique.