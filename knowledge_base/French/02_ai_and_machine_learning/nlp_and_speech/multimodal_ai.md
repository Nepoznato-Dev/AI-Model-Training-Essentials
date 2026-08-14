<!--
---
# Metadata
title: "Multimodal AI"
description: "Vision-language models, CLIP, DALL-E, cross-modal learning"
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
tags: [multimodal, ai, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# IA multimodale
Les systèmes d’IA multimodaux traitent et combinent simultanément des informations provenant de plusieurs types de données (texte, images, audio, vidéo, etc.). Alors que les systèmes d’IA antérieurs étaient généralement à modalité unique (texte uniquement, image uniquement), les systèmes modernes les plus performants sont multimodaux. GPT-4V lit les images et le texte ensemble ; Gemini traite le texte, les images, l'audio et la vidéo de manière native ; et des systèmes comme Sora génèrent des vidéos à partir de descriptions textuelles. Ce fichier explique le fonctionnement de l'IA multimodale, les architectures qui la sous-tendent et pourquoi la combinaison de modalités est si puissante.
---

## Pourquoi le multimodal ?
| Avantage | Descriptif | Exemple |
|---------|-------------|---------|
| **Compréhension plus riche** | Différentes modalités fournissent des informations complémentaires | Une vidéo transmet du mouvement, du son et du contexte que le texte seul ne peut pas |
| **Meilleure généralisation** | L'apprentissage à travers les modalités crée des représentations plus robustes | Un modèle qui a vu à la fois des images et des descriptions textuelles de « chat » comprend mieux le concept |
| **Interaction plus naturelle** | Les humains communiquent via plusieurs canaux | Des assistants vocaux qui voient ce que vous pointez |
| **Transfert multimodal** | La connaissance d'une modalité aide avec une autre | La compréhension des images améliore la génération de texte, et vice versa |
---

## Architectures de base
### Modèles Vision-Langage (VLM)
Modèles qui traitent à la fois les images et le texte.
| Architecture | Comment ça marche | Exemples |
|-------------|-------------|---------|
| **Double encodeur** | Encodeurs séparés pour l'image et le texte ; combiner ultérieurement | CLIP, ALIGNEZ |
| **Encodeur Fusion** | Les jetons d'image et de texte sont entrelacés et traités ensemble | Flamant rose, Gémeaux |
| **Attention croisée** | Les jetons de texte s'occupent des fonctionnalités de l'image (ou vice versa) | Flamant rose, CoCa |
| **Tokeniser unifié** | Les images sont converties en jetons et traitées avec les jetons de texte | Gémeaux, caméléon |
### Comment fonctionnent les modèles vision-langage
| Étape | Descriptif |
|------|-------------|
| **1. Encoder l'image** | Un encodeur de vision (ViT, SigLIP) convertit l'image en un ensemble de vecteurs de caractéristiques |
| **2. Encoder du texte** | Un encodeur de langue traite les jetons de texte |
| **3. Modalités de fusion** | Les caractéristiques de l'image sont projetées dans l'espace d'intégration du modèle de langage |
| **4. Générer** | Le modèle de langage produit du texte conditionné à la fois par des entrées d'image et de texte |
### Modèles clés de vision et de langage
| Modèle | Développeur | Architecture | Caractéristique notable |
|-------|-----------|-------------|------------------|
| **CLIP** | OpenAI | Double encodeur (ViT + encodeur de texte) | Classification d'images Zero-shot via texte |
| **LLaVA** | Open source | Encodeur visuel LLaMA + CLIP | VLM open source ; communauté forte |
| **GPT-4V / 4o** | OpenAI | Multimodal unifié | Traite le texte, les images et l'audio ensemble |
| **Gémeaux** | Google DeepMind | Nativement multimodal dès la formation | Conçu pour le multimodal dès le départ |
| **Claude** | Anthropique | Vision + texte | Fort dans la compréhension des documents et des graphiques |
| **Qwen-VL** | Alibaba | VLM à poids ouvert | Compétitif avec les modèles fermés |
| **StagiaireVL** | Open source | Encodeur de vision multi-échelle | Forte option open source |
---

## Modèles audio et vocaux
### Reconnaissance vocale (ASR)
| Modèle | Architecture | Caractéristique notable |
|-------|-------------|-----------------|
| **Chuchotement** (OpenAI) | Transformateur codeur-décodeur | Formé sur 680 000 heures d'audio multilingue ; robuste |
| **Conforme** | Convolution + auto-attention | Combine des fonctionnalités locales et mondiales |
| **wav2vec 2.0** | Auto-supervisé | Apprend d'un discours sans étiquette |
| **USM** (Google) | Modèle de parole universel | 2 millions d'heures de données étiquetées ; Plus de 300 langues |
### Synthèse vocale (TTS)
| Modèle | Approche | Caractéristique notable |
|-------|----------|-----------------|
| **VALL-E** (Microsoft) | Codec neuronal | Clonage vocal à partir d'un échantillon de 3 secondes |
| **Écorce** (Suno) | Basé sur un transformateur | Multilingue; inclut des sons non vocaux |
| **OnzeLabs** | Commerciale | Clonage vocal de haute qualité |
| **ChatTTS** | Open source | Discours conversationnel à prosodie naturelle |
| **Discours de poisson** | Open source | Multilingue; inférence rapide |
### Compréhension audio
| Modèle | Capacité |
|-------|---------------|
| **AudioLDM** | Génération d'effets sonores à partir de texte |
| **MusicGen** (Méta) | Génération de texte en musique |
| **Qwen-Audio** | Compréhension audio (parole, musique, sons environnementaux) |
| **SAUMON** | Compréhension de la parole, de l'audio, du langage, de la musique et du bruit |
---

## Modèles vidéo
La vidéo combine des images, de l'audio, du texte et du temps, ce qui en fait la modalité la plus complexe.
| Modèle | Tapez | Capacité |
|-------|------|-------------|
| **Sora** (OpenAI) | Texte vers vidéo | Jusqu'à 1080p ; comprend la physique |
| **Gémeaux** | Compréhension vidéo | Peut analyser de longues vidéos avec audio |
| **Vidéo-LLaVA** | Vidéo + texte | Compréhension de la vidéo open source |
| **Piste Gen-3** | Texte/image vers vidéo | Génération de vidéos commerciales |
| **Kling** | Texte vers vidéo | Génération de vidéo longue durée |
### Vidéo Comprendre les défis
| Défi | Descriptif |
|---------------|-------------|
| **Raisonnement temporel** | Comprendre les événements qui se déroulent au fil du temps |
| **Contexte long** | Les vidéos peuvent durer des heures ; le traitement de toutes les images coûte cher |
| **Synchronisation audiovisuelle** | Relier ce qui est dit à ce qui est montré |
| **Causalité** | Comprendre les causes et les effets dans les séquences vidéo |
---

## Récupération multimodale
Trouver du contenu pertinent selon différentes modalités.
| Tâche | Descriptif | Exemple |
|------|-------------|--------------|
| **Texte → Image** | Rechercher des images correspondant à une requête textuelle | Rechercher "coucher de soleil sur les montagnes" dans une photothèque |
| **Image → Texte** | Rechercher du texte pertinent pour une image | Générer des légendes pour les images |
| **Texte → Audio** | Trouver des sons correspondant à une description | Conception sonore : "des pas sur les graviers" |
| **Image → Image** | Trouver des images visuellement similaires | Recherche de produits par image |
### CLIP pour la récupération multimodale
L'espace d'intégration partagé de CLIP permet une récupération multimodale sans tir :
| Étape | Descriptif |
|------|-------------|
| 1 | Encodez toutes les images avec l'encodeur vision |
| 2 | Encodez la requête texte avec l'encodeur de texte |
| 3 | Calculer la similarité cosinus entre l'incorporation de texte et toutes les incorporations d'images |
| 4 | Renvoie les images avec la plus grande similarité |
Cela fonctionne sans aucune formation spécifique à la tâche – une propriété appelée capacité **zero-shot**.
---

## IA incarnée
L’IA incarnée combine la perception multimodale et l’action physique.
| Système | Modalité | Demande |
|--------|----------|-------------|
| **RT-2** (Google) | Vision + langage → actions du robot | Commande de robot à usage général à partir d'instructions textuelles |
| **Octobre** | Politique relative aux robots open source | Formé sur diverses données robotiques |
| **Tesla Optimus** | Vision + langage → tâches physiques | Robot humanoïde pour tâches générales |
| **Figure 01** | Vision + langage + parole | Robot humanoïde avec capacité conversationnelle |
### Défis de l'IA incorporée
| Défi | Pourquoi c'est difficile |
|-----------|--------------|
| **Écart entre la simulation et le réel** | La simulation ne capture pas parfaitement la physique du monde réel |
| **Dextérité** | Le contrôle de la motricité fine (mains, doigts) est extrêmement difficile |
| **Sécurité** | Les robots physiques peuvent causer de réels dégâts |
| **Traitement en temps réel** | Doit percevoir, décider et agir en quelques millisecondes |
| **Généralisation** | Un robot entraîné à ramasser des gobelets rouges pourrait échouer avec des gobelets bleus |
---

## Données et formation
### Données de formation multimodales
| Ensemble de données | Modalités | Taille |
|---------|-----------|------|
| **LAION-5B** | Paires image-texte | 5,85 milliards de paires |
| **Compte de données** | Image-texte organisée | Benchmark pour la conception d'ensembles de données |
| ** Esprit ** (Wikipédia) | Image-texte de Wikipédia | 11,5 millions de paires |
| **Comment100M** | Vidéo-texte (vidéos explicatives) | 100 millions de clips |
| **LibriDiscours** | Texte vocal | 1 000 heures d'anglais |
| **Voix commune** | Texte vocal | Multilingue; contribué par la communauté |
### Stratégies de formation
| Stratégie | Descriptif | Quand utiliser |
|--------------|-------------|-------------|
| **Formation conjointe** | Entraînez-vous sur toutes les modalités simultanément | Lorsque vous avez aligné les données multimodales |
| **Apprentissage du programme** | Commencez par des exemples simples ; augmenter la difficulté | Améliore la convergence |
| **Apprentissage contrasté** | Apprenez à faire correspondre les paires associées selon les modalités (style CLIP) | Construire des représentations partagées |
| **Réglage des instructions** | S'entraîner sur des paires instruction-réponse multimodales | Faire des modèles suit des instructions multimodales |
---

## Évaluation
| Référence | Modalités | Ce qu'il teste |
|-----------|-----------|---------------|
| **MMLU** | Texte | Connaissances dans 57 matières |
| **MMMU** | Texte + images | Raisonnement de niveau collégial avec diagrammes |
| **MathVista** | Texte + images | Raisonnement mathématique avec des données visuelles |
| **Vidéo-MME** | Texte + vidéo | Compréhension vidéo et raisonnement temporel |
| **CASQUE** | Texte + audio | Évaluation multimodale à contexte long |
| **Banc SWE** | Texte + code | Tâches d'ingénierie logicielle du monde réel |
---

## Résumé
L’IA multimodale représente le passage de modèles à objectif unique à des systèmes qui perçoivent et raisonnent sur toutes les formes de données. Les modèles de langage visuel comme GPT-4V et Gemini peuvent comprendre les images et le texte ensemble ; les modèles vocaux comme Whisper et VALL-E gèrent l'audio ; les modèles vidéo commencent à traiter toute la complexité des images en mouvement avec le son. La tendance est claire : les systèmes d’IA les plus performants du futur seront nativement multimodaux, traitant tous les types d’informations simultanément. Les défis – alignement des données, coût de calcul, évaluation et déploiement intégré – sont importants, mais les progrès en 2024-2026 ont été rapides.