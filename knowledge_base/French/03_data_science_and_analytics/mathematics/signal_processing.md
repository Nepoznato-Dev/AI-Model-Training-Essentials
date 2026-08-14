<!--
---
# Metadata
title: "Signal Processing"
description: "Fourier transforms, FFT, Laplace transforms, Z-transforms, filtering, sampling theorem, windowing, spectral analysis, and wavelets"
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
    changes: "Initial deep-dive into signal processing"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [signal-processing, fourier-transform, fft, laplace-transform, z-transform, filtering, sampling-theorem, wavelets]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "optics_and_waves.md"
  - "numerical_methods.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Traitement du signal
Le traitement du signal est la science de l'analyse, de la modification et de la synthèse de signaux, c'est-à-dire des représentations de grandeurs physiques variant dans le temps, l'espace ou la fréquence. L'audio, les images, la vidéo, les données des capteurs, les ondes cérébrales, les cours boursiers sont tous des signaux. Les outils mathématiques de traitement du signal (transformées de Fourier, filtres, théorie de l'échantillonnage) sont fondamentaux pour l'apprentissage automatique, les communications, l'imagerie médicale et pratiquement tous les domaines travaillant avec des données.
---

## Signaux et systèmes
###Classification des signaux
| Tapez | Descriptif | Exemple |
|------|-------------|--------------|
| **Temps continu** | Défini pour tout t ∈ ℝ | Tension audio, température |
| **Temps discret** | Défini à des indices entiers n | Audio échantillonné, valeurs de pixels |
| **Analogique** | Continu en temps et en amplitude | Rainure de disque vinyle |
| **Numérique** | Discret en temps et amplitude quantifiée | Fichier MP3, image JPEG |
| **Périodique** | x(t + T) = x(t) pour tout t | Onde sinusoïdale, onde carrée |
| **Apériodique** | Aucun motif répétitif | Discours, musique |
| **Déterministe** | Complètement prévisible | Onde sinusoïdale |
| **Stochastique** | Contient du hasard | Bruit, cours des actions |
### Propriétés du système
| Propriété | Définition | Exemple |
|----------|-----------|---------|
| **Linéaire** | T[ax₁ + bx₂] = aT[x₁] + bT[x₂] | Filtre passe-bas |
| **Invariant dans le temps** | Décalage en entrée → même décalage en sortie | Tout filtre fixe |
| **Casalité** | La production dépend uniquement des apports présents et passés | Système temps réel |
| **Étable (BIBO)** | Entrée limitée → sortie limitée | Filtre bien conçu |
| **Sans mémoire** | La sortie dépend uniquement de l'entrée actuelle | Amplificateur |
---

## Transformée de Fourier
La **transformée de Fourier** décompose un signal en ses fréquences constitutives.
### Transformée de Fourier continue
X(f) = ∫_{−∞}^{∞} x(t) e^{−j2πft} dt
Inverse : x(t) = ∫_{−∞}^{∞} X(f) e^{j2πft} df
### Paires de transformées de Fourier
| Domaine temporel x(t) | Domaine fréquentiel X(f) |
|---------|----------------------|
| Impulsion rectangulaire | fonction sin |
| fonction sin | Impulsion rectangulaire |
| Gaussienne e^{−at²} | Gaussienne (√(π/a))e^{−π²f²/a} |
| Delta de Dirac δ(t) | 1 (toutes les fréquences) |
| Exponentiel complexe e^{j2πf₀t} | δ(f-f₀) |
| Cosinus cos(2πf₀t) | ½[δ(f−f₀) + δ(f+f₀)] |
### Propriétés clés
| Propriété | Domaine temporel | Domaine fréquentiel |
|--------------|-------------|-----------------|
| Linéarité | ax₁(t) + bx₂(t) | aX₁(f) + bX₂(f) |
| Décalage horaire | x(t − t₀) | X(f)e^{−j2πft₀} |
| Changement de fréquence | x(t)e^{j2πf₀t} | X(f-f₀) |
| Convolution | x₁(t) ∗ x₂(t) | X₁(f) · X₂(f) |
| Multiplications | x₁(t) · x₂(t) | X₁(f) ∗ X₂(f) |
| Différenciation | dx/dt | j2πfX(f) |
| Théorème de Parseval | ∫\|x(t)\|² dt | ∫\|X(f)\|² df |
**Théorème de convolution :** Convolution en temps = multiplication en fréquence. C'est la propriété la plus importante : elle transforme des opérations de convolution coûteuses en multiplications bon marché.
### Transformée de Fourier discrète (TFD)
Pour une séquence x[0], x[1], ..., x[N−1] :
X[k] = Σ_{n=0}^{N−1} x[n] e^{−j2πkn/N}, k = 0, 1, ..., N−1
| Propriété | Valeur |
|--------------|-------|
| Entrée | N échantillons réels ou complexes |
| Sortie | N groupes de fréquences complexes |
| Résolution de fréquence | f_s/N (où f_s est le taux d'échantillonnage) |
| Fréquence de Nyquist | f_s/2 (fréquence maximale représentable) |
| Complexité | Calcul direct O(N²) |
### Transformée de Fourier rapide (FFT)
La **FFT** calcule la DFT en O(N log N) au lieu de O(N²).
| N | Opérations O(N²) | O(N log N) Opérations | Accélération |
|---|--------|------------|---------|
| 1 024 | 1 048 576 | 10 240 | 102× |
| 1 048 576 | 1,1 × 10¹² | 20 971 520 | 52 428 × |
La FFT est l’un des algorithmes les plus importants jamais inventés. Il permet le traitement audio en temps réel, la compression d'images (JPEG), la communication sans fil (OFDM) et l'analyse spectrale.
---

## Transformation de Laplace
La **transformée de Laplace** étend la transformée de Fourier pour gérer les systèmes instables et l'analyse transitoire.
F(s) = ∫₀^∞ f(t) e^{−st} dt, où s = σ + jω
### Transformations de Laplace courantes
| f(t) | F(s) | Région de convergence |
|------|------|----------------------|
| δ(t) (impulsion) | 1 | Tous les |
| u(t) (étape) | 1/s | Re(s) > 0 |
| e^{−at}u(t) | 1/(s+a) | Re(s) > −a |
| tuⁿtu(t) | n!/s^{n+1} | Re(s) > 0 |
| péché(ωt)u(t) | ω/(s²+ω²) | Re(s) > 0 |
| cos(ωt)u(t) | s/(s²+ω²) | Re(s) > 0 |
### Connexion à la transformée de Fourier
Lorsque σ = 0 (s = jω), la transformée de Laplace se réduit à la transformée de Fourier. La transformée de Laplace fournit une image plus complète en incluant des informations sur la croissance/décroissance (σ).
---

## Transformation Z
La **transformation Z** est l'équivalent en temps discret de la transformée de Laplace.
X(z) = Σ_{n=−∞}^{∞} x[n] z^{−n}
### Transformations Z courantes
| x[n] | X(z) | ROC |
|------|------|-----|
| δ[n] | 1 | Tous les z |
| u[n] (étape) | z/(z−1) | \|z\| > 1 |
| aⁿu[n] | z/(z−a) | \|z\| > \|un\| |
| naⁿu[n] | az/(z−a)² | \|z\| > \|un\| |
| péché(ω₀n)u[n] | z sin(ω₀)/(z²−2z cos(ω₀)+1) | \|z\| > 1 |
### Relation avec d'autres transformations
| Transformer | Domaine | Variables |
|-----------|--------|---------------|
| Fourier | Fréquence continue | f ou ω |
| Laplace | Fréquence complexe | s = σ + jω |
| Transformation en Z | Fréquence complexe (discrète) | z = e^{sT} |
Le cercle unité dans le plan z (|z| = 1) correspond à la transformée de Fourier.
---

## Filtres
Les filtres transmettent ou bloquent sélectivement certaines composantes de fréquence.
### Types de filtres
| Tapez | Laissez-passer | Blocs | Demande |
|------|--------|--------|-------------|
| **Passe-bas** | Basses fréquences | Hautes fréquences | Lissage, anticrénelage |
| **Passe-haut** | Hautes fréquences | Basses fréquences | Détection des bords, suppression du bruit |
| ** Passe-bande ** | Une gamme de fréquences | Hors plage | Sélection des chaînes (radio) |
| **Band-stop (encoche)** | Tout sauf une gamme | Une gamme spécifique | Suppression du bourdonnement des lignes électriques |
### Filtres FIR vs IIR
| Propriété | FIR (Réponse Impulsionnelle Finie) | IIR (Réponse Impulsive Infinie) |
|--------------|-------------------------------|--------------------------------|
| Réponse impulsionnelle | Durée finie | Durée infinie |
| Stabilité | Toujours stable | Peut être instable |
| Phases | Peut être exactement linéaire | Phase généralement non linéaire |
| Commentaires | Non | Oui |
| Calcul | Plus de coefficients nécessaires | Moins de coefficients pour le même roll-off |
| Conception | Fenêtres, Parks-McClellan | Butterworth, Chebyshev, elliptique |
| Fonction de transfert | H(z) = Σ bₖz⁻ᵏ | H(z) = Σ bₖz⁻ᵏ / (1 + Σ aₖz⁻ᵏ) |
### Spécifications de conception du filtre
| Paramètre | Descriptif |
|---------------|-------------|
| **Bande passante** | Gamme de fréquences qui devrait passer avec une perte minimale |
| **Bande d'arrêt** | Gamme de fréquences à atténuer |
| **Fréquence limite** | Limite entre la bande passante et la bande d'arrêt |
| **Ondulation** | Variation du gain de bande passante (ou bande d'arrêt) |
| **Déroulage** | Taux d'atténuation (dB par octave ou décade) |
| **Bande de transition** | Région entre la bande passante et la bande d'arrêt |
### Conceptions de filtres courantes
| Conception | Caractéristiques | Cas d'utilisation |
|--------|----------------|----------|
| **Butterworth** | Bande passante extrêmement plate, atténuation modérée | Usage général |
| **Chebyshev Type I** | Ondulation dans la bande passante, atténuation plus raide | Quand le roll-off compte |
| **Tchebychev Type II** | Ondulation dans la bande d'arrêt, bande passante plate | Quand la planéité de la bande passante est importante |
| **Elliptique (Cauer)** | Ondulation dans les deux cas, inclinaison la plus raide | Commande minimum requise |
| **Bessel** | Phase linéaire (délai de groupe maximum plat) | Préserver la forme de la forme d'onde |
---

## Théorie de l'échantillonnage
### Théorème d'échantillonnage de Nyquist-Shannon
Un signal continu peut être parfaitement reconstruit à partir de ses échantillons si la fréquence d'échantillonnage dépasse deux fois la fréquence maximale :
f_s > 2f_max
| Terme | Définition |
|------|------------|
| **Taux d'échantillonnage** (f_s) | Nombre d'échantillons par seconde |
| **Tarif Nyquist** | 2f_max (taux d'échantillonnage minimum) |
| **Fréquence de Nyquist** | f_s/2 (fréquence maximale représentable) |
| **Aliasing** | Hautes fréquences se faisant passer pour des basses fréquences lorsque f_s < 2f_max |
### Taux d'échantillonnage courants
| Demande | Tarif | Fréquence Nyquist |
|-------------|------|---------|
| Discours téléphonique | 8kHz | 4kHz |
| CD-audio | 44,1 kHz | 22,05 kHz |
| Audio professionnel | 48 kHz | 24 kHz |
| Audio haute résolution | 96 kHz | 48kHz |
| Vidéo (30 ips) | 30 Hz (temporel) | 15 Hz |
### Anticrénelage
Avant l'échantillonnage, un **filtre anti-aliasing** (passe-bas) supprime les fréquences supérieures à f_s/2 pour éviter l'alias.
---

## Fenêtrage
Lors de l'analyse d'un segment fini d'un signal, nous multiplions implicitement par une fenêtre rectangulaire, provoquant une fuite spectrale. Les **fonctions de fenêtre** réduisent cette fuite.
### Fenêtres communes
| Fenêtre | Largeur du lobe principal | Niveau des lobes latéraux | Cas d'utilisation |
|--------|----------------|-----------------|----------|
| Rectangulaire | Le plus étroit | −13dB | Quand la résolution compte le plus |
| Hann | 2× rectangulaire | −31dB | Usage général |
| Hamming | 2× rectangulaire | −41dB | Lobe latéral le plus proche réduit |
| Homme noir | 3× rectangulaire | −58dB | Plage dynamique élevée |
| Kaiser | Ajustable | Réglable (via β) | Quand le compromis est réglable |
### Fuite spectrale
La multiplication d'un signal par une fenêtre fait convoluer son spectre avec celui de la fenêtre. Des lobes principaux plus larges réduisent la résolution en fréquence ; les lobes latéraux inférieurs réduisent les fuites.
---

## Ondelettes
Les **Wavelets** sont de petites fonctions de type onde localisées utilisées pour l'analyse de signaux multi-résolution.
### Transformation en ondelettes
Contrairement à la transformée de Fourier (qui donne des informations globales sur la fréquence), la transformée en ondelettes donne une localisation **temps-fréquence**.
| Transformer | Résolution temporelle | Résolution de fréquence |
|-----------|----------------|-----------|
| Fourier | Aucun (mondial) | Excellent |
| FT de courte durée | Fixe (taille de la fenêtre) | Fixe |
| Ondelette | Variable (bon à haute fréquence) | Variable (bon à basse fréquence) |
### Familles d'ondelettes courantes
| Famille | Propriétés | Demande |
|--------|-----------|-------------|
| **Cheveux** | Le plus simple, discontinu | Détection des contours, analyse rapide |
| **Daubechies** (dbN) | Support compact, N moments de fuite | Compression, débruitage |
| **Symlets** | Daubechies presque symétriques | Distorsion de phase réduite |
| **Coiffes** | Conçu pour les conditions momentanées | Traitement du signal |
| **Morlet** | Sinusoïde à fenêtre gaussienne | Analyse temps-fréquence |
| **Chapeau mexicain** | Dérivée seconde de Gaussienne | Détection de fonctionnalités |
### Applications des ondelettes
| Demande | Comment les ondelettes aident |
|-------------|---------|
| Compression d'images (JPEG 2000) | Représentation multi-résolution, meilleure que DCT pour les bords |
| Débruitage | Seuil des petits coefficients d'ondelettes (le signal est en grands coefficients) |
| Détection de fonctionnalités | Détection de contours, détection de transitoires dans des séries temporelles |
| Analyse ECG | Détection des complexes QRS, classification des arythmies |
| Analyse sismique | Identification des couches géologiques, traitement du signal sismique |
---

## Pertinence pour l'apprentissage automatique et la science des données
| Concept de traitement du signal | Demande |
|----------------|-------------|
| Transformée de Fourier | Fonctionnalités spectrales pour le ML audio, analyse dans le domaine fréquentiel des séries temporelles |
| FFT | Convolution rapide dans les CNN (convolution spectrale), corrélation efficace |
| Théorème de convolution | Comprendre le fonctionnement des CNN (ce sont des filtres appris) |
| Filtres | Prétraitement (lissage, débruitage), extraction de caractéristiques |
| Théorème d'échantillonnage | Comprendre la discrétisation, choisir les fréquences des capteurs, éviter l'aliasing |
| Fenêtrage | STFT pour audio ML (spectrogrammes), analyse temps-fréquence |
| Ondelettes | Extraction de caractéristiques pour les séries chronologiques, la compression, le débruitage |
| Transformation de Laplace/Z | Théorie du contrôle pour la robotique, compréhension de la stabilité du système |
| Analyse spectrale | Analyse EEG/IRMf, surveillance des vibrations, maintenance prédictive |
| Tarif Nyquist | Choisir des taux de collecte de données appropriés pour les pipelines ML |
---

## Résumé
| Outil | Domaine | Aperçu clé |
|------|--------|-------------|
| Transformée de Fourier | Temps → Fréquence | Les signaux sont des sommes de sinusoïdes |
| Transformation de Laplace | Temps → Fréquence complexe | Gère les transitoires et la stabilité |
| Transformation Z | Temps discret → Complexe | Analyse et conception de filtres numériques |
| FFT | Calcul DFT efficace | O(N log N) au lieu de O(N²) |
| Filtres | Sélection de fréquence | Transmettez ce dont vous avez besoin, bloquez ce dont vous ne faites pas |
| Théorème d'échantillonnage | Continu ↔ discret | Échantillonnez assez vite, ne perdez rien |
| Fenêtrage | Compromis temps-fréquence | Résolution d'équilibre et fuite |
| Ondelettes | Analyse multi-résolution | Local en temps et en fréquence |
Le traitement du signal fournit la base mathématique pour comprendre, analyser et manipuler les données. Chaque pipeline d'apprentissage automatique qui fonctionne avec des séries temporelles, de l'audio, des images ou des données de capteurs utilise implicitement des concepts de traitement du signal. La transformée de Fourier, en particulier, est sans doute l’outil mathématique le plus important après le calcul pour tout data scientist.