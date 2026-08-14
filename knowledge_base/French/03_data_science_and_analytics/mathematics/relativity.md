<!--
---
# Metadata
title: "Relativity"
description: "Special relativity, Lorentz transformations, time dilation, length contraction, mass-energy equivalence, four-vectors, and introduction to general relativity"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into relativity"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [relativity, special-relativity, general-relativity, lorentz-transformations, time-dilation, length-contraction, mass-energy, spacetime]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Relativité
Les théories de la relativité d'Einstein ont révolutionné notre compréhension de l'espace, du temps et de la gravité. La **Relativité restreinte** (1905) a montré que l'espace et le temps ne sont pas séparés mais tissés en un seul tissu appelé espace-temps, et que la vitesse de la lumière est la même pour tous les observateurs. La **Relativité générale** (1915) a réinventé la gravité non pas comme une force mais comme la courbure de l'espace-temps causée par la masse et l'énergie. Ces théories sous-tendent la navigation GPS, les accélérateurs de particules et notre compréhension des trous noirs et de l'évolution de l'univers.
---

## Postulats de la relativité restreinte
Einstein a construit la relativité restreinte sur deux postulats trompeusement simples :
| Postulat | Déclaration |
|-----------|---------------|
| **Principe de relativité** | Les lois de la physique sont les mêmes dans tous les référentiels inertiels (non accélérateurs) |
| **Constabilité de c** | La vitesse de la lumière dans le vide (c ≈ 3 × 10⁸ m/s) est la même pour tous les observateurs, quel que soit leur mouvement ou celui de la source |
Ces deux postulats, combinés, bouleversent des siècles d’intuition newtonienne sur l’espace et le temps absolus.
---

## Transformations de Lorentz
Les **transformations de Lorentz** relient les coordonnées entre deux référentiels inertiels se déplaçant à une vitesse relative v.
### Équations de transformation
Pour l'image S' se déplaçant à la vitesse v le long de l'axe des x par rapport à l'image S :
| Quantité | Transformations |
|--------------|--------------------|
| x' | γ(x − vt) |
| t' | γ(t − vx/c²) |
| y' | y |
| z' | z |
où γ (facteur de Lorentz) = 1/√(1 − v²/c²)
### Le facteur de Lorentz γ
| c/c | y | Effet |
|-----|---|--------|
| 0 | 1.0 | Pas d'effets relativistes (limite newtonienne) |
| 0,1 | 1,005 | Correction de 0,5% |
| 0,5 | 1.155 | Correction de 15,5% |
| 0,9 | 2.294 | Dilatation significative du temps |
| 0,99 | 7.089 | Effets extrêmes |
| 0,999 | 22h37 | Régime accélérateur de particules |
| → 1 | → ∞ | Impossible pour les objets massifs |
### Transformations inverses
Pour passer de S' à S : remplacez v par −v.
---

## Dilatation du temps
Les horloges en mouvement fonctionnent lentement.
Δt = γΔt₀
où Δt₀ est le **temps propre** (temps mesuré dans la trame de repos de l'horloge).
**Exemple concret :** Un muon créé à 10 km d'altitude se déplace à 0,998c. Sa durée de vie reste-trame est de 2,2 μs.
- γ = 1/√(1 − 0,998²) ≈ 15,8
- Durée de vie dilatée : Δt = 15,8 × 2,2 μs = 34,8 μs
- Distance parcourue : d = 0,998c × 34,8 μs ≈ 10,4 km
- Sans dilatation du temps : d = 0,998c × 2,2 μs ≈ 0,66 km (n'atteindrait jamais le sol)
- **Réalité :** Les muons atteignent la surface de la Terre, confirmant expérimentalement la dilatation du temps.
### Paradoxe des jumeaux
Un jumeau voyage à grande vitesse et revient. Ils sont plus jeunes que les jumeaux au foyer. Ce n'est pas un vrai paradoxe : le jumeau voyageur accélère (change de référentiel inertiel), brisant la symétrie.
---

## Contraction de la longueur
Les objets en mouvement sont raccourcis dans la direction du mouvement.
L = L₀/γ
où L₀ est la **longueur appropriée** (longueur mesurée dans le cadre de repos de l'objet).
| c/c | y | Facteur de contraction L/L₀ |
|-----|---|------------------------|
| 0,5 | 1.15 | 87% |
| 0,9 | 2.29 | 44% |
| 0,99 | 7.09 | 14% |
| 0,999 | 22.4 | 4,5% |
**Point clé :** La contraction de la longueur n'est pas une illusion d'optique : il s'agit d'un véritable effet physique mesuré par des observateurs en mouvement relatif.
---

## Relativité de la simultanéité
Les événements simultanés dans une image ne sont PAS simultanés dans une autre image se déplaçant par rapport à la première.
**Expérience de pensée d'Einstein sur le train :** La foudre frappe les deux extrémités d'un train en mouvement. Un observateur sur la plateforme les voit simultanément. Un observateur dans le train (se dirigeant vers une frappe) voit en premier la frappe frontale.
**Conclusion :** « Simultané » n'est pas absolu — cela dépend du cadre de référence de l'observateur.
---

## Ajout de vitesse
Les vitesses n’ajoutent pas simplement de la relativité restreinte.
### Ajout de vitesse relativiste
Si un objet se déplace à la vitesse u' dans le cadre S' et que S' se déplace à la vitesse v par rapport à S :
u = (u' + v) / (1 + u'v/c²)
| Scénario | Résultat |
|--------------|--------|
| u' = c (lumière) | u = c (la vitesse de la lumière est invariante) |
| u', v ≪ c | u ≈ u' + v (se réduit à l'addition galiléenne) |
| u' = 0,9c, v = 0,9c | u = 0,9945c (ne dépasse jamais c) |
---

## Equivalence masse-énergie
E = mc²
| Concepts | Formule | Signification |
|---------|---------|---------|
| Énergie de repos | E₀ = mc² | Énergie d'une masse au repos |
| Énergie totale | E = γmc² | Comprend l'énergie cinétique |
| Énergie cinétique | KE = (γ − 1)mc² | Se réduit à ½mv² pour v ≪ c |
| Momentum-énergie | E² = (pc)² + (mc²)² | Relation relativiste énergie-impulsion |
| Particules sans masse | E = pc | Les photons ont de l'énergie et de l'élan mais pas de masse au repos |
### Exemples d'énergie nucléaire
| Réaction | Défaut de masse | Énergie libérée |
|--------------|-------------|-----------------|
| Fission de l'U-235 | 0,1% de la masse | ~200 MeV par fission |
| Fusion DT | 0,7% de la masse | 17,6 MeV par réaction |
| Matière-antimatière | 100% de la masse | 2mc² (conversion complète) |
---

## Quatre vecteurs et espace-temps
### Espace-temps de Minkowski
La relativité restreinte unifie l'espace et le temps en **espace-temps de Minkowski** 4D avec des coordonnées (ct, x, y, z).
### L'intervalle spatio-temporel
ds² = −c²dt² + dx² + dy² + dz²
| Type d'intervalle | État | Signification |
|--------------|-----------|---------|
| **Timelike** | ds²< 0 | Events can be causally connected |
| **Lightlike (null)** | ds² = 0 | Connected by a light signal |
| **Spacelike** | ds² >0 | Les événements ne peuvent pas s'influencer mutuellement |
L'intervalle spatio-temporel est **invariant** — tous les observateurs sont d'accord sur sa valeur.
### Quatre vecteurs
| Quatre vecteurs | Composants | Quantité invariante |
|-------------|-----------|-------------------|
| Poste | (ct, x, y, z) | Intervalle spatio-temporel |
| Vitesse | γ(c, vₓ, vᵧ, v_z) | Le bon moment |
| Élan | (E/c, pₓ, pᵧ, p_z) | Masse au repos : m²c² = E²/c² − p² |
| Forcer | dP/dτ | Bonne accélération |
---

## Introduction à la Relativité Générale
### Le principe d'équivalence
| Version | Déclaration |
|---------|-----------|
| **Faible** | Masse gravitationnelle = masse inertielle (tous les objets tombent au même rythme) |
| **Einstein** | Un cadre à accélération uniforme est localement impossible à distinguer d'un champ gravitationnel |
| **Fort** | Toutes les lois physiques (pas seulement la mécanique) sont localement les mêmes dans un référentiel en chute libre |
### La gravité comme espace-temps courbe
L'idée centrale de la relativité générale : la masse et l'énergie courbent l'espace-temps, et les objets suivent les chemins les plus droits possibles (géodésiques) à travers l'espace-temps courbe.
**Équations du champ d'Einstein :**
G_μν + Λg_μν = (8πG/c⁴) T_μν
| Symbole | Signification |
|--------|---------|
| G_μν | Tenseur d'Einstein (code la courbure de l'espace-temps) |
| Λ | Constante cosmologique (énergie sombre) |
| g_μν | Tenseur métrique (décrit la géométrie de l'espace-temps) |
| G | Constante gravitationnelle de Newton |
| T_μν | Tenseur contrainte-énergie (contenu matière et énergie) |
**Résumé de John Wheeler :** "L'espace-temps indique à la matière comment se déplacer ; la matière indique à l'espace-temps comment se courber."
### Prédictions de la Relativité Générale
| Prédiction | Descriptif | Confirmé? |
|---------------|-------------|------------|
| Dilatation gravitationnelle du temps | Les horloges fonctionnent plus lentement dans des champs gravitationnels plus forts | Oui (le GPS nécessite une correction) |
| Lentilles gravitationnelles | La lumière se courbe autour d'objets massifs | Oui (Eddington 1919, images Hubble) |
| Redshift gravitationnel | La lumière perd de l'énergie en sortant des puits gravitationnels | Oui (Pound-Rebka 1959) |
| Trous noirs | Régions où la courbure de l'espace-temps empêche la lumière de s'échapper | Oui (LIGO, EHT 2019) |
| Ondes gravitationnelles | Ondulations dans l'espace-temps dues à l'accélération des masses | Oui (LIGO 2015) |
| Précession du périhélie de Mercure | 43 secondes d'arc supplémentaires par siècle | Oui (anomalie expliquée depuis 1859) |
| Glissement du cadre | Les masses en rotation entraînent l'espace-temps autour d'elles | Oui (Sonde Gravité B 2011) |
### Métrique de Schwarzschild
La solution de trou noir la plus simple (non rotative, non chargée) :
ds² = −(1 − 2GM/rc²)c²dt² + (1 − 2GM/rc²)⁻¹dr² + r²dΩ²
**Rayon Schwarzschild :** r_s = 2GM/c²
| Objet | Messe | r_s |
|--------|------|-----|
| Terre | 6 × 10²⁴ kg | 9 millimètres |
| Soleil | 2 × 10³⁰kg | 3km |
| Sgr A* (centre de la Voie Lactée) | 4 × 10⁶M☉ | 12 millions de kilomètres |
---

## Pertinence pour l'apprentissage automatique et la science des données
| Concept de relativité | Demande |
|---------|-------------|
| Transformations de Lorentz | Réseaux de neurones équivariants de Lorentz, modèles sensibles à la symétrie |
| Géométrie spatio-temporelle | Apprentissage profond géométrique, apprentissage multiple |
| Quatre vecteurs | Notation tensorielle utilisée dans les simulations de physique relativiste |
| Dilatation gravitationnelle du temps | Corrections GPS (services de localisation, ML géospatial) |
| Lentilles gravitationnelles | Analyse de données astronomiques, cartographie de la matière noire |
| Relativité générale | Réseaux de neurones basés sur la physique pour la détection des ondes gravitationnelles |
| Géométrie riemannienne | Descente de gradient naturel (géométrie de l'information), optimisation multiple |
| Tenseur métrique | Définit les distances dans les espaces courbes – fondamental pour l'apprentissage multiple |
| Géodésiques | Chemins les plus courts sur les variétés — utilisés en robotique, intégration de graphes |
| Calcul tensoriel | Base pour comprendre les variétés de données de grande dimension |
---

## Résumé
| Concepts | Idée de base | Équation clé |
|---------|-----------|-------------|
| Relativité restreinte | L'espace et le temps sont unifiés ; c est absolu | Transformations de Lorentz |
| Dilatation du temps | Les horloges en mouvement fonctionnent lentement | Δt = γΔt₀ |
| Contraction de la longueur | Les objets en mouvement raccourcissent | L = L₀/γ |
| Masse-énergie | La masse et l'énergie sont équivalentes | E = mc² |
| Quatre vecteurs | Descriptions spatio-temporelles unifiées | Intervalle invariant ds² |
| Principe d'équivalence | Gravité = accélération localement | Fondation de GR |
| Relativité générale | La gravité est un espace-temps incurvé | G_μν = (8πG/c⁴)T_μν |
| Géodésiques | Les objets suivent les chemins les plus droits dans un espace-temps courbe | Chemin le plus court sur le collecteur |
La relativité a remodelé notre compréhension des aspects les plus fondamentaux de la réalité : l'espace, le temps, la masse, l'énergie et la gravité. Ses outils mathématiques – tenseurs, variétés, géodésiques, espaces métriques – ont migré bien au-delà de la physique vers l’apprentissage automatique, où ils alimentent l’apprentissage géométrique profond, les méthodes de gradient naturel et les algorithmes d’apprentissage multiple.