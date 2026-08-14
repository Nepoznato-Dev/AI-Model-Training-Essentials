---
# Metadata
title: "Local AI Architecture"
description: "Local AI deployment architectures"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
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
tags: [local, ai, architecture, ai-and-machine-learning]
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
# Architecture d'IA locale
Un guide pratique pour exécuter de grands modèles de langage entièrement sur l'appareil : considérations matérielles, moteurs d'inférence, optimisation de la mémoire et conception du système pour le déploiement en périphérie.
---

## Pourquoi exécuter l'IA localement ?
- **Confidentialité** : aucune donnée ne quitte l'appareil.
- **Coût** : aucun frais d'API par jeton.
- **Latence** : inférence prévisible et sans réseau.
- **Disponibilité hors ligne** : fonctionne sans Internet.
- **Contrôle** : Contrôle total sur la version du modèle, la personnalisation et le réglage fin.
---

## Configuration matérielle requise
### Mémoire GPU (VRAM)
La ressource la plus critique. Taille du modèle en mémoire ≈ **paramètres × octets par paramètre**.
| Précision | Octets par paramètre | Modèle 3.8B | Modèle 7B | Modèle 13B | Modèle 70B |
|-----------|-----------|------------|--------------|---------------|----------------|
| PC32 | 4 | ~15 Go | ~28 Go | ~52 Go | ~280 Go |
| PC16 | 2 | ~7,6 Go | ~14 Go | ~26 Go | ~140 Go |
| INT8 (8 bits) | 1 | ~3,8 Go | ~7 Go | ~13 Go | ~70 Go |
| INT4 (4 bits) | 0,5 | ~1,9 Go | ~3,5 Go | ~6,5 Go | ~35 Go |
**Consignes pratiques :**
- 8 Go de VRAM → jusqu'à 7 modèles B en 4 bits.
- 12 Go de VRAM → jusqu'à 13 Go de modèles en 4 bits.
- 24 Go de VRAM → jusqu'à 70 Go de modèles en 4 bits (ou 13 Go en 8 bits).
- Apple Silicon (mémoire unifiée) peut exécuter des modèles 70B sur des systèmes de plus de 64 Go.
### RAM (Mémoire système)
- Pour l'inférence CPU, vous avez besoin de suffisamment de RAM système pour charger le modèle (similaire aux numéros VRAM).
- Pour l'inférence GPU, la RAM système est importante pour charger le modèle en mémoire avant de le décharger vers la VRAM.
### Stockage
- Les poids des modèles quantifiés occupent quelques Go (par exemple, 4 bits 7B ≈ 4 Go sur le disque). Assurez-vous d'avoir au moins 20 à 50 Go d'espace libre pour plusieurs modèles.
### Processeur
- Pour un traitement rapide (préremplissage) et un déchargement du processeur, un processeur multicœur moderne est utile.
- Les puces Apple de la série M offrent d'excellentes performances pour les LLM grâce à la mémoire unifiée et au Neural Engine.
---

## Quantification
La quantification réduit la précision numérique des poids, réduisant considérablement la mémoire et augmentant la vitesse pour un faible coût en précision.
### Formats populaires
| Formater | Morceaux | Descriptif | Utilisation typique |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | format lama.cpp, optimisé pour les hybrides CPU/GPU | Idéal pour l'inférence locale |
| **GPTQ** | 4–8 | GPU uniquement, efficace sur CUDA | Idéal pour les GPU NVIDIA |
| **AWQ** | 4 | Compatible avec l'activation, GPU uniquement | Idéal pour l'inférence par lots sur les GPU |
| **ONNX** | variables | Standardisé, multiplateforme | Service de production |
### Choisir un niveau de quantification
- **Q8_0** (8 bits) : perte de qualité minimale, taille la plus grande.
- **Q6_K** (6 bits) : bonne qualité, compression correcte.
- **Q5_K_M** (5 bits) : point idéal commun.
- **Q4_K_M** (4 bits) : qualité la plus petite et acceptable pour la plupart des tâches.
- **IQ4_XS** / **IQ3_XS** : Quantification améliorée avec une meilleure perplexité à 4/3 bits.
**Règle générale :** Utilisez Q4_K_M pour un bon équilibre entre qualité et taille. Si vous disposez de VRAM supplémentaire, utilisez Q5 ou Q6.
---

## Moteurs d'inférence (local)
### lama.cpp
- Écrit en C++.
- Prend en charge le format GGUF.
- Optimisé pour CPU et GPU (via CUDA, Metal, OpenCL).
- Très rapide, surtout sur le CPU.
- Liaisons ligne de commande, mode serveur et Python.
**Exemple de commande :**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### Ollama
- Encapsule llama.cpp avec une simple CLI et une API REST.
- Télécharge automatiquement les modèles, les gère.
- Idéal pour le prototypage et les applications de bureau.
- Prend en charge les fichiers modèles personnalisés pour les invites système.
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

###LM Studio
- Application de bureau graphique pour Windows, macOS, Linux.
- Interface de téléchargement et de discussion en un clic.
- Serveur local intégré avec API compatible OpenAI.
- Idéal pour les utilisateurs non techniques et les tests rapides.
### Transformateurs de visage câlins + bitsandbytes
- La bibliothèque Python standard pour les modèles HF.
- Utilisez`bitsandbytes`pour la quantification 4 bits (`load_in_4bit=True`).
- Plus flexible pour le réglage fin mais plus lent que llama.cpp pour l'inférence.
### ExLlamaV2
- Inférence GPU très rapide pour GPTQ et AWQ.
- Meilleures performances sur les GPU NVIDIA.
- Prend en charge la génération par lots.
### mlx (Pomme)
- Le framework Apple pour les puces de la série M.
- Hautement optimisé pour Apple Silicon.
- API Python.
---

## Gestion de la mémoire
### Fenêtre contextuelle et cache KV
Le cache KV stocke les paires clé-valeur pour chaque couche et chaque jeton dans le contexte. Il croît linéairement avec la longueur du contexte.
Coût de la mémoire ≈ 2 × couches × (têtes KV × dim de la tête) × jetons × octets par valeur
Pour un modèle à 32 couches avec 8 têtes KV et 128 têtes dim, chaque jeton coûte environ 32 × 8 × 128 × 2 octets = 65 Ko par jeton. Pour 128 000 jetons, cela représente environ 8 Go uniquement pour le cache.
### Stratégies de déchargement
- **Déchargement de couches** : placez certaines couches sur le GPU, d'autres sur le CPU. Plus rapide que le processeur pur, exigences inférieures en VRAM.
- **Streaming de jetons** : traitez les jetons de manière incrémentielle plutôt que d'un seul coup.
### Mise en cache des invites
Réutilisez les caches KV dans des invites similaires pour éviter de recalculer la phase de pré-remplissage. Certains frameworks le prennent en charge (par exemple, vLLM, llama.cpp avec`--prompt-cache`).
### Fichiers mappés en mémoire
Chargez les poids des modèles directement à partir du disque sans les charger entièrement dans la RAM (utile pour les modèles volumineux sur des systèmes à mémoire limitée). llama.cpp utilise le mappage mémoire par défaut.
---

## Architectures de déploiement
### Mode mono-appareil
Un modèle fonctionne sur une machine (ordinateur portable, smartphone, appareil Edge). Utilisé pour les assistants personnels, les applications de prise de notes, la complétion de code.
### Edge-Cloud hybride
Le modèle local gère les requêtes courantes ; recours à un modèle cloud pour les questions complexes. Cela offre le meilleur des deux mondes : vitesse/privé pour la plupart, capacité pour les cas extrêmes.
### Inférence distribuée (multi-GPU)
Pour les modèles plus grands, divisez les couches sur plusieurs GPU (parallélisme tenseur) ou divisez le contexte entre les appareils (parallélisme pipeline). Utilisez llama.cpp avec`-ngl`ou ExLlamaV2 avec`--num-gpu-layers`.
### Déploiement mobile
- **Android** : utilisez lama.cpp via les liaisons JNI ou ML Kit.
- **iOS** : utilisez lama.cpp via les liaisons Swift ou mlx.
- **Web** : utilisez WebLLM (fonctionne sur WebGPU via le runtime ONNX) ou transformers.js.
---

## Optimisation des performances
### Attention éclair
Accélère le calcul de l'attention et réduit l'utilisation de la mémoire. Disponible dans les bibliothèques llama.cpp, ExLlamaV2 et de transformateurs modernes.
### Inférence par lots
Traitez plusieurs invites en une seule passe avant. Augmente considérablement le débit. Utilisez`llama-batch`ou vLLM.
### Arrêt anticipé / Budgétisation des jetons
Définissez un budget de jetons maximum pour empêcher une génération illimitée.
### Décodage spéculatif
Utilisez un petit modèle rapide (ébauche) pour prédire les jetons, puis vérifiez avec le grand modèle en parallèle. Peut produire une accélération de 2 à 3 fois.
---

## Guide de configuration pratique
### 1. Installez Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Tirez un modèle
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. Exécuter avec l'API
```bash
ollama serve
```

Envoyez ensuite les requêtes à`http://localhost:11434/api/generate`.
### 4. Intégration Python
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (Alternative) Utilisez directement lama.cpp
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## Surveillance et observabilité
- Suivez l'utilisation du GPU (`nvidia-smi` sous Linux, Activity Monitor sur macOS).
- Suivre l'utilisation de la mémoire (RAM et VRAM).
- Suivre les jetons par seconde (débit).
- Suivez le temps jusqu'au premier jeton (latence).
- Utilisez la journalisation intégrée de llama.cpp ou Ollama.
---

## Limites et compromis
- **Écart de qualité** : les petits modèles locaux (3,8B–7B) sont généralement sous-performants les grands modèles de nuages ​​(GPT-4, Claude 3,5) sur un raisonnement complexe.
- **Connaissance limite** : les connaissances du modèle sont gelées au moment de la formation ; utilisez RAG pour injecter des informations actuelles.
- **Multilingue** : les modèles plus petits peuvent avoir moins de capacités multilingues.
- **Utilisation de l'outil** : les workflows agentiques (appel de fonction) peuvent être moins fiables sur les petits modèles.
Pour de nombreuses tâches quotidiennes (résumé, questions-réponses, complétion de code, classification), les modèles locaux sont déjà suffisants et s'améliorent rapidement.