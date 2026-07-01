<!-- 
This file was automatically translated from English to French.
Source: local_ai_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Architecture IA Locale

Un guide pratique pour exécuter des modèles de langage volumineux entièrement sur l'appareil — considérations matérielles, moteurs d'inférence, optimisation de la mémoire et conception système pour le déploiement en périphérie.

---

## Pourquoi exécuter l'IA localement ?

- **Confidentialité** : Aucune donnée ne quitte l'appareil.
- **Coût** : Aucun frais d'API par token.
- **Latence** : Inférence prévisible, sans réseau.
- **Disponibilité hors ligne** : Fonctionne sans Internet.
- **Contrôle** : Contrôle total sur la version du modèle, la personnalisation et le fine-tuning.

---

## Configuration matérielle requise

### Mémoire GPU (VRAM)
La ressource la plus critique. Taille du modèle en mémoire ≈ **paramètres × octets par paramètre**.

| Précision | Octets par paramètre | Modèle 3.8B | Modèle 7B | Modèle 13B | Modèle 70B |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| INT8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| INT4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Directives pratiques :**
- 8GB VRAM → jusqu'aux modèles 7B en 4-bit.
- 12GB VRAM → jusqu'aux modèles 13B en 4-bit.
- 24GB VRAM → jusqu'aux modèles 70B en 4-bit (ou 13B en 8-bit).
- Apple Silicon (mémoire unifiée) peut exécuter des modèles 70B sur des systèmes avec 64GB+.

### RAM (Mémoire système)
- Pour l'inférence CPU, vous avez besoin de suffisamment de RAM système pour charger le modèle (similaire aux chiffres VRAM).
- Pour l'inférence GPU, la RAM système est importante pour charger le modèle dans la mémoire avant de le transférer vers la VRAM.

### Stockage
- Les poids de modèle quantifiés occupent quelques Go (par exemple, 4-bit 7B ≈ 4 Go sur disque). Assurez-vous d'avoir au moins 20–50 Go libres pour plusieurs modèles.

### CPU
- Pour le traitement des prompts (prefill) et le déchargement CPU, un CPU multi-cœur moderne aide.
- Les puces Apple série M ont d'excellentes performances pour les LLM grâce à la mémoire unifiée et au Neural Engine.

---

## Quantification

La quantification réduit la précision numérique des poids, réduisant considérablement la mémoire et augmentant la vitesse avec un faible coût en précision.

### Formats populaires

| Format | Bits | Description | Utilisation typique |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | Format llama.cpp, optimisé pour hybride CPU/GPU | Meilleur pour l'inférence locale |
| **GPTQ** | 4–8 | GPU uniquement, efficace sur CUDA | Meilleur pour les GPU NVIDIA |
| **AWQ** | 4 | Conscient de l'activation, GPU uniquement | Bon pour l'inférence par lots sur GPU |
| **ONNX** | variable | Standardisé, multiplateforme | Service en production |

### Choisir un niveau de quantification
- **Q8_0** (8-bit) : perte de qualité minimale, taille la plus grande.
- **Q6_K** (6-bit) : bonne qualité, compression décente.
- **Q5_K_M** (5-bit) : juste milieu courant.
- **Q4_K_M** (4-bit) : le plus petit, qualité acceptable pour la plupart des tâches.
- **IQ4_XS** / **IQ3_XS** : Quantification améliorée avec une meilleure perplexité à 4/3 bits.

**Règle générale :** Utilisez Q4_K_M pour un bon équilibre entre qualité et taille. Si vous avez de la VRAM supplémentaire, utilisez Q5 ou Q6.

---

## Moteurs d'inférence (local)

### llama.cpp
- Écrit en C++.
- Prend en charge le format GGUF.
- Optimisé pour CPU et GPU (via CUDA, Metal, OpenCL).
- Très rapide, surtout sur CPU.
- Ligne de commande, mode serveur et liaisons Python.

**Exemple de commande :**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
(-ngl 32 délègue 32 couches au GPU)
```

### Ollama
- Enveloppe llama.cpp avec une CLI simple et une API REST.
- Télécharge automatiquement les modèles, les gère.
- Idéal pour le prototypage et les applications de bureau.
- Prend en charge les Modelfiles personnalisés pour les invites système.

**Utilisation :**
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM Studio
- Application de bureau graphique pour Windows, macOS, Linux.
- Interface de chat et téléchargement en un clic.
- Serveur local intégré avec API compatible OpenAI.
- Bon pour les utilisateurs non techniques et les tests rapides.

### Hugging Face Transformers + bitsandbytes
- La bibliothèque Python standard pour les modèles HF.
- Utilisez bitsandbytes pour la quantification 4-bit (load_in_4bit=True).
- Plus flexible pour le fine-tuning mais plus lent que llama.cpp pour l'inférence.

### ExLlamaV2
- Inférence GPU très rapide pour GPTQ et AWQ.
- Meilleures performances sur les GPU NVIDIA.
- Prend en charge la génération par lots.

### mlx (Apple)
- Framework d'Apple pour les puces série M.
- Hautement optimisé pour Apple Silicon.
- API Python.

## Gestion de la mémoire

### Fenêtre de contexte et cache KV
Le cache KV stocke les paires clé-valeur pour chaque couche et chaque token dans le contexte. Il croît linéairement avec la longueur du contexte.

Coût mémoire ≈ 2 × couches × (têtes KV × dim tête) × tokens × octets par valeur

Pour un modèle à 32 couches avec 8 têtes KV et 128 de dimension de tête, chaque token coûte ~32 × 8 × 128 × 2 octets = 65 Ko par token. Pour 128k tokens, c'est ~8 Go rien que pour le cache.

### Stratégies de déchargement
- **Déchargement de couches** : Mettez certaines couches sur le GPU, d'autres sur le CPU. Plus rapide que le CPU pur, exigence de VRAM plus faible.
- **Streaming de tokens** : Traitez les tokens de manière incrémentielle plutôt que tous à la fois.

### Mise en cache des prompts
Réutilisez les caches KV pour des prompts similaires afin d'éviter de recalculer la phase de prefill. Certains frameworks prennent cela en charge (par exemple, vLLM, llama.cpp avec --prompt-cache).

### Fichiers mappés en mémoire
Chargez les poids du modèle directement depuis le disque sans les charger entièrement dans la RAM (utile pour les modèles énormes sur des systèmes à mémoire limitée). llama.cpp utilise le mappage mémoire par défaut.

## Architectures de déploiement

### Mode appareil unique
Un modèle s'exécute sur une machine (ordinateur portable, smartphone, appareil edge). Utilisé pour les assistants personnels, les applications de prise de notes, la complétion de code.

### Hybride Edge-Cloud
Le modèle local gère les requêtes courantes ; recours à un modèle cloud pour les questions complexes. Cela donne le meilleur des deux mondes — rapidité/confidentialité pour la plupart, capacité pour les cas limites.

### Inférence distribuée (multi-GPU)
Pour les modèles plus grands, divisez les couches sur plusieurs GPU (parallélisme tensoriel) ou divisez le contexte sur les appareils (parallélisme de pipeline). Utilisez llama.cpp avec -ngl ou ExLlamaV2 avec --num-gpu-layers.

### Déploiement mobile
- **Android** : Utilisez llama.cpp via des liaisons JNI ou ML Kit.
- **iOS** : Utilisez llama.cpp via des liaisons Swift ou mlx.
- **Web** : Utilisez WebLLM (s'exécute sur WebGPU via le runtime ONNX) ou transformers.js.

## Optimisation des performances

### Flash Attention
Accélère le calcul d'attention et réduit l'utilisation de la mémoire. Disponible dans llama.cpp, ExLlamaV2 et les bibliothèques transformers modernes.

### Inférence par lots
Traitez plusieurs prompts en un seul passage avant. Augmente considérablement le débit. Utilisez llama-batch ou vLLM.

### Arrêt précoce / Budgétisation de tokens
Définissez un budget maximum de tokens pour empêcher la génération illimitée.

### Décodage spéculatif
Utilisez un petit modèle rapide (brouillon) pour prédire les tokens, puis vérifiez avec le grand modèle en parallèle. Peut donner un gain de vitesse de 2 à 3 fois.

## Guide de configuration pratique

### 1. Installer Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Récupérer un modèle
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. Exécuter avec l'API
```bash
ollama serve
```
Ensuite, envoyez des requêtes à http://localhost:11434/api/generate.

### 4. Intégration Python
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (Alternative) Utiliser llama.cpp directement
```bash
# Télécharger GGUF depuis Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Exécuter le serveur
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

## Surveillance et observabilité

- Suivez l'utilisation du GPU (nvidia-smi sur Linux, Moniteur d'activité sur macOS).
- Suivez l'utilisation de la mémoire (RAM et VRAM).
- Suivez les tokens par seconde (débit).
- Suivez le temps jusqu'au premier token (latence).
- Utilisez la journalisation intégrée de llama.cpp ou Ollama.

## Limitations et compromis

- **Écart de qualité** : Les petits modèles locaux (3.8B–7B) sont généralement moins performants que les grands modèles cloud (GPT-4, Claude 3.5) sur le raisonnement complexe.
- **Limite de connaissances** : Les connaissances du modèle sont figées au moment de l'entraînement ; utilisez RAG pour injecter des informations actuelles.
- **Multilingue** : Les petits modèles peuvent avoir moins de capacités multilingues.
- **Utilisation d'outils** : Les flux de travail agentiques (appel de fonctions) peuvent être moins fiables sur les petits modèles.

Pour de nombreuses tâches quotidiennes (résumé, questions-réponses, complétion de code, classification), les modèles locaux sont déjà suffisants et s'améliorent rapidement.

---derstet common vulnerabilities.
2. **Threat modelldansg**: Identify potential threats early dans design.
3. **Secure coddansg stetards**: Enpource via ldansters et code review checklists.
4. **SAST** (Static Application Sécurité Testdansg): Scan source code pour vulnerabilities (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Sécurité Testdansg): Scan runndansg applications (OWASP ZAP, Burp Suite).
6. **SCA** (Sdetware Composition Analysis): Scan dependencies.
7. **Penetration testdansg**: Regular ethical hackdansg exercises.
8. **Bug bounty**: Encourage external researchers to fdansd vulnerabilities responsibly.
9. **Incident response plan**: Have a clear plan pour when a breach is detected.

---

## Emergency Checklist (When a Breach is Suspected)

1. **Do not panic** — but act quickly.
2. **Isolate** le/la affected systèmes (disconnect from réseau if needed).
3. **Preserve evidence**: Capture logs, memory dumps, et disk images.
4. **Identify** le/la scope: which systèmes, which données.
5. **Rotate** all compromised credentials et secrets.
6. **Patch** le/la vulnerability.
7. **Notify** affected users et regulatory bodies if required (avecdans juridique timeframes).
8. **Conduct a post-mortem** to understet root cause et improve processes.