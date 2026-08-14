---
# Metadata
title: "Speech and Audio Processing"
description: "ASR, TTS, audio features, Whisper, speech pipelines"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [speech, audio, processing, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Traitement de la parole et de l'audio
Le traitement de la parole et de l'audio couvre les technologies qui permettent aux machines d'entendre, de comprendre, de générer et de manipuler le son. Cela comprend la reconnaissance vocale (transformation de mots prononcés en texte), la synthèse vocale (transformation de texte en mots prononcés), l'identification du locuteur, la génération de musique et la compréhension des sons environnementaux. Le domaine a été transformé par l’apprentissage en profondeur : les systèmes modernes se rapprochent d’une précision de niveau humain pour la reconnaissance vocale et produisent des voix synthétiques étrangement naturelles.
---

## Fondamentaux de l'audio numérique
Le son est une onde de pression. Pour la traiter numériquement, nous échantillonnons l'onde à intervalles réguliers.
| Concepts | Descriptif | Valeur typique |
|---------|-------------|---------------|
| **Taux d'échantillonnage** | Combien de fois par seconde le son est mesuré | 8 kHz (téléphone), 16 kHz (parole), 44,1 kHz (CD), 48 kHz (professionnel) |
| **Profondeur de bits** | Précision de chaque échantillon | 16 bits (CD), 24 bits (professionnel), 32 bits float (traitement) |
| **Chaînes** | Mono (1), stéréo (2), surround (5.1, 7.1) | Stéréo pour la musique ; mono pour la parole |
| **Durée** | Durée de l'audio | Varie |
Un enregistrement mono d'une minute à 16 kHz, 16 bits = 1,92 Mo. Une chanson stéréo de 3 minutes à 44,1 kHz, 16 bits = 30,3 Mo.
---

## Extraction de fonctionnalités audio
Les formes d’onde audio brutes sont difficiles à utiliser directement pour les modèles. Nous extrayons des fonctionnalités qui capturent les caractéristiques importantes du son.
| Fonctionnalité | Ce qu'il capture | Cas d'utilisation |
|---------|-----------------|----------|
| **Spectrogramme Mel** | Contenu fréquentiel au fil du temps, mappé à la perception auditive humaine | Reconnaissance vocale, classification musicale |
| **MFCC** (coefficients cepstraux Mel-Fréquence) | Représentation compacte de l'enveloppe spectrale | Reconnaissance vocale traditionnelle |
| **Chromagramme** | Répartition des classes de hauteur (quelles notes jouent) | Analyse musicale, détection d'accords |
| **Taux de passage à zéro** | À quelle fréquence le signal franchit zéro | Détection vocale ou non vocale |
| **Énergie RMS** | Intensité du signal au fil du temps | Détection d'activité vocale |
| **Pas (F0)** | Fréquence fondamentale | Identification du locuteur, transcription musicale |
### Spectrogramme de Mel
La représentation audio la plus courante pour l’apprentissage profond. Il convertit l'audio dans un format semblable à une image 2D :
| Axe | Représente |
|------|-----------|
| **Axe X** | Temps |
| **Axe Y** | Fréquence (sur l'échelle de Mel — espacée perceptuellement) |
| **Couleur/intensité** | Énergie à cette fréquence et à ce moment |
L'échelle de Mel se rapproche de l'audition humaine : nous distinguons mieux les basses fréquences que les hautes.
---

## Reconnaissance vocale automatique (ASR)
ASR convertit la langue parlée en texte. Il s’agit de l’une des applications commerciales les plus importantes de l’IA audio.
### Évolution de l'ASR
| Ère | Approche | Limitation |
|-----|----------|------------|
| **Avant 2010** | Modèles de Markov cachés + modèles de mélange gaussien | Une ingénierie manuelle approfondie requise ; médiocre dans des conditions bruyantes |
| **2010-2015** | Hybride DNN-HMM | Les réseaux de neurones ont remplacé les GMM ; amélioration significative |
| **2015-2020** | Modèles de bout en bout (Deep Speech, LAS) | Réseau neuronal unique de l'audio au texte |
| **2020+** | Basé sur un transformateur (Whisper, Conformer) | Précision de pointe ; multilingue; robuste |
### Modèles ASR clés
| Modèle | Architecture | Données de formation | Caractéristique notable |
|-------|-------------|---------------|-----------------|
| **Chuchotement** (OpenAI) | Transformateur codeur-décodeur | 680 000 heures, 99 langues | Multilingue; robuste aux accents et au bruit; open source |
| **Conforme** | Convolution + auto-attention | Divers | Combine des fonctionnalités locales (conv) et globales (attention) |
| **wav2vec 2.0** | Transformateur auto-supervisé | Discours sans étiquette | Apprend à partir de l'audio brut sans transcriptions |
| **USM** (Google) | Modèle de parole universel | 2 millions d'heures, plus de 300 langues | La plupart des langues couvertes |
| **MMS** (méta) | Discours massivement multilingue | Plus de 1 400 langues | Étend la couverture aux langues à faibles ressources |
### Métriques ASR
| Métrique | Descriptif |
|--------|-------------|
| **WER** (taux d'erreur de mots) | Pourcentage de mots mal transcrits. Plus bas, c'est mieux. La performance humaine est d'environ 4 à 5 % pour un anglais propre. |
| **CER** (taux d'erreur de caractère) | Identique à WER mais au niveau du personnage. Utilisé pour les langues sans limites de mots (chinois, japonais). |
### Défis ASR courants
| Défi | Descriptif |
|---------------|-------------|
| **Accents et dialectes** | Les performances chutent considérablement pour les accents non standard |
| **Bruit de fond** | La musique, le trafic et les autres haut-parleurs dégradent la précision |
| **Commutation de code** | Intervenants passant d'une langue à l'autre au milieu d'une phrase |
| **Homophones** | « Là » contre « leur » contre « ils sont » — nécessite un contexte |
| ** Ponctuation et mise en forme ** | La sortie ASR est généralement non ponctuée ; a besoin de post-traitement |
| **Langues à faibles ressources** | La plupart des modèles fonctionnent mal pour les langues avec peu de données de formation |
---

## Synthèse vocale (TTS)
TTS convertit le texte écrit en audio parlé. Les systèmes modernes produisent une parole qui est souvent impossible à distinguer des enregistrements humains.
### Évolution du TTS
| Ère | Approche | Qualité |
|-----|----------|---------|
| **Avant 2010** | Concaténatif (assemblage de fragments enregistrés) | Robotique ; expressivité limitée |
| **2010-2017** | Paramétrique statistique (HMM, neurones précoces) | Mieux mais toujours reconnaissable comme synthétique |
| **2017-2020** | Neuronal (Tacotron, WaveNet) | Qualité quasi humaine ; expressif |
| **2020+** | Codec neuronal (VALL-E, Bark) | Clonage vocal ; quelques coups; hautement naturel |
### Modèles TTS clés
| Modèle | Architecture | Caractéristique notable |
|-------|-------------|-----------------|
| **WaveNet** (DeepMind) | Modèle génératif autorégressif | Premier TTS au son véritablement naturel |
| **Tacotron 2** (Google) | Seq2seq + vocodeur | De bout en bout ; haute qualité |
| **VITS** | Inférence variationnelle + entraînement contradictoire | Rapide; bonne qualité; largement utilisé |
| **VALL-E** (Microsoft) | Modèle de langage de codec neuronal | Clonage vocal à partir d'un échantillon de 3 secondes |
| **Écorce** (Suno) | Basé sur un transformateur | Multilingue; sons non vocaux (rire, musique) |
| **OnzeLabs** | Commerciale | Clonage vocal leader du secteur |
| **ChatTTS** | Open source | Optimisé pour le discours conversationnel |
| **Discours de poisson** | Open source | Rapide; multilingue |
### Clonage de voix
Le clonage vocal crée une voix synthétique qui ressemble à une personne spécifique à partir d'un court échantillon audio.
| Méthode | Données nécessaires | Qualité |
|--------|------------|---------|
| **Réglage fin** | 10 à 60 minutes de discours | Haute qualité; spécifique au locuteur |
| **Quelques plans** | 3-30 secondes de discours | Bonne qualité; configuration rapide |
| **Tir zéro** | Aucune donnée sur le locuteur cible | Utilise l'audio de référence au moment de l'inférence |
**Préoccupation éthique** : le clonage vocal peut être utilisé à des fins d'usurpation d'identité, de fraude et de deepfakes. La plupart des fournisseurs commerciaux exigent un consentement vocal.
---

## Reconnaissance du locuteur
| Tâche | Descriptif | Demande |
|------|-------------|-------------|
| **Vérification du locuteur** | "Est-ce que cette personne est celle qu'ils prétendent être ?" | Services bancaires par téléphone, déverrouillage d'appareil |
| **Identification du locuteur** | "Qui parle?" | Transcription de réunion, criminalistique |
| ** Diarisation du haut-parleur ** | "Qui a parlé quand ?" (en audio multi-haut-parleurs) | Résumés de réunions, génération de sous-titres |
| Modèle | Approche |
|-------|--------------|
| **ECAPA-TDNN** | Basé sur l'intégration ; état de l'art pour la vérification |
| **d-vecteur** | Intégrations de haut-parleurs simples de DNN |
| **x-vecteur** | Intégrations de haut-parleurs améliorées ; largement utilisé |
---

## Récupération d'informations musicales
| Tâche | Descriptif | Outils/Modèles |
|------|-------------|-------------|
| **Transcription musicale** | Convertir l'audio en partitions / MIDI | Emplacement de base Spotify, Spleeter |
| **Séparation des sources** | Isoler des instruments ou des voix individuels | Demucs, Spleeter, séparation des sources musicales |
| **Classement par genre** | Classer la musique par genre | CNN sur les spectrogrammes |
| **Suivi des battements** | Détecter le tempo et les positions de battement | Librosa, Madmaman |
| **Reconnaissance d'accords** | Identifier les accords dans la musique | Modèles Chord-CNN, CRF |
| **Génération musicale** | Créer une nouvelle musique | MusicGen, MuseNet, AIVA |
---

## Détection du bruit environnemental
| Tâche | Descriptif | Demande |
|------|-------------|-------------|
| **Détection d'événement sonore** | Identifier les sons dans un environnement | Maison intelligente (brise-verre, bébé qui pleure) |
| **Classification des scènes acoustiques** | Classer l'environnement (bureau, parc, circulation) | Appareils contextuels |
| **Détection d'anomalies** | Détecter les sons inhabituels | Surveillance industrielle (machineæ•…éšœ) |
| Ensemble de données | Sons | Taille |
|---------|--------|------|
| **Ensemble audio** | 632 cours de son | Plus de 2 millions de clips YouTube |
| **ESC-50** | 50 cours de son environnemental | 2 000 extraits |
| **UrbanSound8K** | Sons urbains | 8 732 extraits |
---

## Outils et cadres
| Outil | Objectif |
|------|--------------|
| **Librosa** | Bibliothèque Python pour l'analyse audio (fonctionnalités, effets, visualisation) |
| **Pydub** | Manipulation audio simple (couper, concaténer, exporter) |
| **FFmpeg** | Traitement audio/vidéo en ligne de commande (le couteau suisse) |
| **Torcheaudio** | Traitement audio PyTorch (transformations, ensembles de données, modèles) |
| **Visage câlin (transformateurs)** | Modèles ASR et TTS pré-entraînés |
| ** Chuchotement (OpenAI) ** | Reconnaissance vocale (open source) |
| **Coqui TTS** | Boîte à outils TTS open source |
| **Démocrates** | Séparation des sources musicales |
| **DiscoursCerveau** | Boîte à outils vocale tout-en-un (ASR, TTS, reconnaissance du locuteur) |
---

## Conseils pratiques
- **Écoutez toujours vos données.** Avant d'entraîner quoi que ce soit, écoutez un échantillon audio. Notez la fréquence d'échantillonnage, le niveau de bruit et les caractéristiques des haut-parleurs.
- **Faire correspondre les fréquences d'échantillonnage.** Whisper attend 16 kHz. Si votre audio est à 44,1 kHz, rééchantillonnez-le, mais sachez que le sous-échantillonnage perd des informations.
- **Augmentez les données audio.** Ajoutez du bruit de fond, faites varier la vitesse et la hauteur, simulez différents microphones. Cela améliore considérablement la robustesse.
- **Utilisez des modèles pré-entraînés.** Whisper pour l'ASR et VITS/Bark pour TTS sont d'excellents points de départ. La mise au point est presque toujours préférable à la formation à partir de zéro.
- **Gérer le silence.** La détection d'activité vocale (VAD) supprime le silence avant le traitement, économisant ainsi le calcul et améliorant la précision. Silero VAD et WebRTC VAD sont des choix populaires.
- **Normaliser le volume.** Différents enregistrements ont des niveaux de volume très différents. Normaliser à un niveau constant avant le traitement.
---

## Résumé
Le traitement de la parole et de l’audio a été révolutionné par l’apprentissage profond. Les systèmes ASR modernes comme Whisper approchent la précision au niveau humain dans des dizaines de langues. Les systèmes TTS produisent une parole de plus en plus impossible à distinguer des enregistrements humains. Le clonage vocal fonctionne à partir de quelques secondes d'audio. La génération de musique, la séparation des sources et la détection des sons environnementaux progressent rapidement. Le domaine est confronté à des défis permanents – langues à faibles ressources, environnements bruyants, préoccupations éthiques autour du clonage de la voix – mais la trajectoire est claire : les machines deviennent aussi performantes que les humains pour entendre, comprendre et produire du son.