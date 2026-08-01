<!-- 
This file was automatically translated from English to French.
Source: local_ai_architecture.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Architecture IA locale

Guide pratique pour exécuter de grands modèles de langage entièrement sur l'appareil — considérations matérielles, moteurs d'inférence, optimisation de la mémoire et conception de systèmes pour le déploiement en edge.

---

## Pourquoi exécuter l'IA localement ?

- **Confidentialité** : aucune donnée ne quitte l'appareil.
- **Coût** : aucun frais d'API par token.
- **Latence** : une inférence prévisible, sans dépendance au réseau.
- **Disponibilité hors ligne** : fonctionne sans connexion internet.
- **Contrôle** : contrôle complet de la version du modèle, de la personnalisation et du fine-tuning.

---

## Exigences matérielles

### Mémoire GPU (VRAM)
C'est la ressource la plus critique. La taille d'un modèle en mémoire ≈ **nombre de paramètres × octets par paramètre**.

| Precision | Bytes per parameter | 3.8B model | 7B model | 13B model | 70B model |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32      | 4                   | ~15 GB     | ~28 GB   | ~52 GB    | ~280 GB   |
| FP16      | 2                   | ~7.6 GB    | ~14 GB   | ~26 GB    | ~140 GB   |
| INT8 (8-bit) | 1              | ~3.8 GB    | ~7 GB    | ~13 GB    | ~70 GB    |
| INT4 (4-bit) | 0.5            | ~1.9 GB    | ~3.5 GB  | ~6.5 GB   | ~35 GB    |

**Repères pratiques :**
- 8 GB de VRAM → jusqu'à des modèles 7B en 4 bits.
- 12 GB de VRAM → jusqu'à des modèles 13B en 4 bits.
- 24 GB de VRAM → jusqu'à des modèles 70B en 4 bits (ou 13B en 8 bits).
- Les systèmes Apple Silicon à mémoire unifiée peuvent exécuter des modèles 70B sur des machines disposant de 64 GB ou plus.

### RAM (mémoire système)
- Pour l'inférence CPU, il faut suffisamment de RAM système pour charger le modèle (des besoins comparables à ceux de la VRAM).
- Pour l'inférence GPU, la RAM système sert à charger le modèle en mémoire avant son transfert vers la VRAM.

### Stockage
- Les poids quantifiés occupent quelques GB (par exemple, un modèle 7B en 4 bits ≈ 4 GB sur disque). Prévoyez au moins 20 à 50 GB libres pour stocker plusieurs modèles.

### CPU
- Pour le traitement du prompt (prefill) et le déchargement partiel sur CPU, un processeur multicœur moderne est utile.
- Les puces Apple M-series offrent d'excellentes performances sur les LLM grâce à la mémoire unifiée et au Neural Engine.

---

## Quantification

La quantification réduit la précision numérique des poids, ce qui diminue fortement l'usage mémoire et accélère l'exécution, au prix d'une légère perte de précision.

### Formats populaires

| Format | Bits | Description | Typical use |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | Format de llama.cpp, optimisé pour un usage hybride CPU/GPU | Idéal pour l'inférence locale |
| **GPTQ** | 4–8 | Réservé au GPU, efficace sur CUDA | Idéal pour les GPU NVIDIA |
| **AWQ** | 4 | Quantification sensible aux activations, uniquement GPU | Bon pour l'inférence par lots sur GPU |
| **ONNX** | variable | Standardisé, multiplateforme | Service en production |

### Choisir un niveau de quantification
- **Q8_0** (8 bits) : perte de qualité minimale, taille la plus importante.
- **Q6_K** (6 bits) : bonne qualité, compression correcte.
- **Q5_K_M** (5 bits) : compromis courant et équilibré.
- **Q4_K_M** (4 bits) : plus compact, qualité acceptable pour la plupart des tâches.
- **IQ4_XS** / **IQ3_XS** : quantification améliorée avec une meilleure perplexité à 4/3 bits.

**Règle générale :** utilisez Q4_K_M pour un bon équilibre entre qualité et taille. Si vous disposez de davantage de VRAM, préférez Q5 ou Q6.

---

## Moteurs d'inférence (locaux)

### llama.cpp
- Écrit en C++.
- Prend en charge le format GGUF.
- Optimisé pour CPU et GPU (via CUDA, Metal, OpenCL).
- Très rapide, en particulier sur CPU.
- Disponible en ligne de commande, en mode serveur et via des bindings Python.

**Exemple de commande :**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
(-ngl 32 offloads 32 layers to GPU)
```

### Ollama
- Enveloppe llama.cpp avec une CLI simple et une API REST.
- Télécharge automatiquement les modèles et les gère.
- Très pratique pour le prototypage et les applications desktop.
- Prend en charge des `Modelfile` personnalisés pour les prompts système.

**Utilisation :**
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM Studio
- Application desktop graphique pour Windows, macOS et Linux.
- Téléchargement en un clic et interface de chat intégrée.
- Serveur local inclus avec API compatible OpenAI.
- Bien adapté aux utilisateurs non techniques et aux tests rapides.

### Hugging Face Transformers + bitsandbytes
- Bibliothèque Python de référence pour les modèles Hugging Face.
- Utilise `bitsandbytes` pour la quantification 4 bits (`load_in_4bit=True`).
- Plus flexible pour le fine-tuning, mais généralement plus lent que llama.cpp pour l'inférence.

### ExLlamaV2
- Inférence GPU très rapide pour GPTQ et AWQ.
- Offre d'excellentes performances sur les GPU NVIDIA.
- Prend en charge la génération par lots.

### mlx (Apple)
- Framework d'Apple pour les puces M-series.
- Très optimisé pour Apple Silicon.
- Dispose d'une API Python.

---

## Gestion de la mémoire

### Fenêtre de contexte et cache KV
Le cache KV stocke des paires clé-valeur pour chaque couche et chaque token du contexte. Il croît linéairement avec la longueur du contexte.

Coût mémoire ≈ 2 × couches × (têtes KV × dimension de tête) × tokens × octets par valeur

Pour un modèle de 32 couches avec 8 têtes KV et une dimension de tête de 128, chaque token coûte ~32 × 8 × 128 × 2 bytes = 65 KB par token. Pour 128k tokens, cela représente ~8 GB uniquement pour le cache.

### Stratégies de déchargement
Déchargement de couches : placez certaines couches sur le GPU et d'autres sur le CPU. C'est plus rapide qu'une exécution 100 % CPU tout en réduisant les besoins en VRAM.

Streaming des tokens : traitez les tokens de manière incrémentale plutôt que d'un seul bloc.

### Mise en cache des prompts
Réutilisez les caches KV entre des prompts similaires pour éviter de recalculer la phase de prefill. Certains frameworks le prennent en charge (par exemple vLLM, llama.cpp avec `--prompt-cache`).

### Fichiers mappés en mémoire
Chargez les poids du modèle directement depuis le disque sans les charger entièrement en RAM (utile pour les très gros modèles sur des machines limitées en mémoire). llama.cpp utilise le memory-mapping par défaut.

---

## Architectures de déploiement

### Mode mono-appareil
Un modèle s'exécute sur une seule machine (ordinateur portable, smartphone, appareil edge). Ce mode convient aux assistants personnels, aux applications de prise de notes et à la complétion de code.

### Edge-cloud hybride
Le modèle local gère les requêtes courantes, puis bascule vers un modèle cloud pour les questions complexes. On obtient ainsi le meilleur des deux mondes : rapidité et confidentialité dans la majorité des cas, capacité accrue pour les situations limites.

### Inférence distribuée (multi-GPU)
Pour les grands modèles, répartissez les couches sur plusieurs GPU (tensor parallelism) ou répartissez le contexte entre plusieurs appareils (pipeline parallelism). Utilisez llama.cpp avec `-ngl` ou ExLlamaV2 avec `--num-gpu-layers`.

### Déploiement mobile
Android : utilisez llama.cpp via des bindings JNI ou ML Kit.

iOS : utilisez llama.cpp via des bindings Swift ou `mlx`.

Web : utilisez WebLLM (exécution sur WebGPU via ONNX runtime) ou transformers.js.

---

## Optimisation des performances

### Flash Attention
Accélère le calcul de l'attention et réduit l'usage mémoire. Disponible dans llama.cpp, ExLlamaV2 et les bibliothèques modernes basées sur transformers.

### Inférence par lots
Traitez plusieurs prompts en un seul passage avant. Le débit augmente fortement. Utilisez `llama-batch` ou vLLM.

### Arrêt anticipé / budget de tokens
Définissez un budget maximal de tokens pour éviter une génération sans borne.

### Décodage spéculatif
Utilisez un petit modèle rapide (draft model) pour prédire des tokens, puis faites-les vérifier en parallèle par le grand modèle. Cela peut apporter une accélération de 2 à 3×.

---

## Guide pratique d'installation

1. **Installer Ollama**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
2. **Télécharger un modèle**
```bash
ollama pull phi3:3.8b-q4_K_M
```
3. **Exécuter avec l'API**
```bash
ollama serve
```
Envoyez ensuite des requêtes à `http://localhost:11434/api/generate`.

4. **Intégration Python**
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```
5. **(Alternative) Utiliser llama.cpp directement**
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## Supervision et observabilité

- Surveillez l'utilisation du GPU (`nvidia-smi` sur Linux, Moniteur d'activité sur macOS).
- Suivez l'utilisation mémoire (RAM et VRAM).
- Mesurez le nombre de tokens par seconde (débit).
- Mesurez le temps jusqu'au premier token (latence).
- Utilisez les journaux intégrés de llama.cpp ou d'Ollama.

---

## Limites et compromis

- **Écart de qualité** : les petits modèles locaux (3.8B–7B) restent généralement en retrait par rapport aux grands modèles cloud (GPT-4, Claude 3.5) sur le raisonnement complexe.
- **Date de coupure des connaissances** : les connaissances du modèle sont figées au moment de l'entraînement ; utilisez le RAG pour injecter des informations récentes.
- **Multilinguisme** : les petits modèles peuvent être moins performants dans plusieurs langues.
- **Utilisation d'outils** : les workflows agentiques (function calling) peuvent être moins fiables sur les petits modèles.

Pour de nombreuses tâches courantes (résumé, questions-réponses, complétion de code, classification), les modèles locaux sont déjà suffisants et progressent rapidement.

text

---

## Fichier 4 : `security_best_practices.md`

# Bonnes pratiques de sécurité

Guide pratique pour sécuriser les applications, l'infrastructure et les données — du développement à la production.

---

## OWASP Top 10 (2021) — Aperçu

1. **Broken Access Control** : des utilisateurs peuvent accéder à des ressources auxquelles ils ne devraient pas avoir accès.
2. **Cryptographic Failures** : chiffrement faible ou absent.
3. **Injection** : injection SQL, NoSQL, de commandes OS ou LDAP.
4. **Insecure Design** : défauts de conception architecturale.
5. **Security Misconfiguration** : mots de passe par défaut, ports ouverts, erreurs trop verbeuses.
6. **Vulnerable and Outdated Components** : dépendances comportant des CVE connues.
7. **Identification and Authentication Failures** : mots de passe faibles, mauvaise gestion des sessions.
8. **Software and Data Integrity Failures** : attaques de la chaîne d'approvisionnement, mises à jour non signées.
9. **Security Logging and Monitoring Failures** : absence de détection des compromissions.
10. **Server-Side Request Forgery (SSRF)** : détournement du serveur pour effectuer des requêtes vers des systèmes internes.

---

## Validation des entrées et encodage des sorties

### Règles de validation
- **Liste blanche > liste noire** : définissez les motifs autorisés (par exemple une regex pour un email) plutôt que de bloquer uniquement les motifs déjà connus comme dangereux.
- **Limites de longueur** : imposez des longueurs maximales pour éviter les buffer overflows et les attaques DoS.
- **Vérification de type** : assurez-vous qu'un entier est bien un entier, qu'un booléen est bien un booléen.
- **Utiliser des bibliothèques éprouvées** : pour la validation des emails, des URL et des dates, utilisez des bibliothèques standards (par exemple `email-validator` en Python, `validator.js` en Node).

### Encodage des sorties
- **Encodage HTML** : encodez `<`, `>`, `&`, `"`, `'` pour éviter les XSS.
- **Paramétrisation SQL** : ne concaténez jamais l'entrée utilisateur dans des requêtes SQL. Utilisez des requêtes paramétrées (prepared statements) ou un ORM.
- **Échappement shell** : évitez de construire des commandes shell à partir d'entrées utilisateur ; si c'est inévitable, utilisez `shlex.quote()` ou un équivalent.

---

## Authentification et autorisation

### Gestion des mots de passe
- **Hashing** : stockez les mots de passe avec un algorithme de hachage robuste et lent : **Argon2id** (préféré), **bcrypt**, **scrypt** ou **PBKDF2**.
- **Salage** : ajoutez un sel unique pour chaque utilisateur.
- **Longueur minimale** : imposez au moins 12 à 16 caractères.
- **MFA (Multi-Factor Authentication)** : exigez un second facteur (TOTP, SMS, clé matérielle) pour les opérations sensibles.
- **Rate limiting** : empêchez les tentatives de force brute sur les points d'entrée de connexion (par exemple 5 tentatives par 5 minutes et par IP/utilisateur).

### Gestion des sessions
- Utilisez des cookies sécurisés, HTTP-only et SameSite pour les jetons de session.
- Définissez des durées d'expiration appropriées.
- Invalidez les sessions lors de la déconnexion et après un changement de mot de passe.
- Évitez d'exposer les identifiants de session dans les URL.

### OAuth2 / OIDC
- Utilisez des bibliothèques reconnues (par exemple Authlib, PyJWT, Passport.js, Spring Security).
- Validez rigoureusement les ID tokens (signature, issuer, audience, expiration).
- Utilisez des paramètres `state` pour prévenir les attaques CSRF.
- Gardez les secrets client confidentiels.

### JWT (JSON Web Tokens)
- **Signature** : utilisez RS256 ou ES256 (asymétrique) pour une meilleure sécurité ; HS256 (symétrique) reste acceptable si les secrets partagés sont bien gérés.
- **Validation** : vérifiez toujours la signature, l'émetteur (`iss`), l'audience (`aud`) et l'expiration (`exp`).
- **Expiration courte** : 15 à 60 minutes pour les access tokens ; utilisez des refresh tokens pour les sessions plus longues.
- **Stockage sécurisé** : ne stockez jamais de JWT dans `localStorage` (vulnérable au XSS) ; préférez des cookies HTTP-only.

---

## Sécurité des API

### Authentification
- Authentifiez toujours les appels d'API (sauf pour les endpoints publics).
- Préférez des clés API ou des jetons OAuth2 à l'authentification basique (qui envoie les identifiants à chaque requête).

### Rate limiting et throttling
- Appliquez des limites par utilisateur et par IP pour prévenir les abus et les attaques DoS.
- Renvoyez `429 Too Many Requests` avec un en-tête `Retry-After`.

### CORS (Cross-Origin Resource Sharing)
- N'autorisez que des origines spécifiques (jamais `*` en production).
- Validez l'en-tête `Origin` côté serveur.

### Validation des entrées
- Validez tous les paramètres de requête, y compris les en-têtes et le corps.
- Rejetez les champs inattendus (`"strict": true` ou `additionalProperties: false` dans JSON Schema).

### HTTPS / TLS
- Imposez HTTPS en production.
- Utilisez HSTS (HTTP Strict Transport Security) pour forcer les navigateurs à utiliser HTTPS.
- Utilisez TLS 1.2 ou 1.3 (désactivez TLS 1.0/1.1).

---

## Gestion des secrets

### Ne jamais coder les secrets en dur
- Ne versionnez pas de secrets (clés API, mots de passe, URL de base de données) dans le code source.
- Utilisez des variables d'environnement ou des outils de gestion des secrets.

### Outils
- **HashiCorp Vault** : niveau entreprise, secrets dynamiques.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager** : solutions cloud natives.
- **SOPS** : chiffre les secrets dans des fichiers avant de les versionner (avec KMS ou GPG).
- **Docker secrets** : pour le mode Swarm ; Kubernetes secrets (encodés en base64, donc à utiliser avec prudence ; envisagez un Secrets Store CSI driver externe).

### Rotation
- Faites tourner régulièrement les secrets et les comptes de service.
- Automatisez la rotation lorsque c'est possible.

---

## Gestion des dépendances

### Analyse des vulnérabilités
- **Python** : `safety`, `pip-audit`, `bandit`.
- **Node** : `npm audit`, `yarn audit`, `snyk`.
- **Rust** : `cargo audit`.
- **Go** : `govulncheck`.
- **Général** : `Dependabot` (GitHub), `Renovate`, `Trivy`.

### Correctifs
- Maintenez les dépendances à jour vers des versions corrigées.
- Mettez en place des pull requests automatiques pour les mises à jour mineures et correctives.
- Consultez les changelogs pour détecter les breaking changes.

### Intégrité de la chaîne d'approvisionnement
- Utilisez des lockfiles (`package-lock.json`, `Cargo.lock`, `go.sum`) pour garantir des builds reproductibles.
- Vérifiez les checksums des dépendances téléchargées.
- Préférez les registres officiels et ne faites confiance qu'aux éditeurs vérifiés.

---

## Sécurité de l'infrastructure

### Pare-feu
- Bloquez tous les ports entrants sauf ceux explicitement nécessaires (par exemple 80, 443).
- Limitez l'accès SSH à des plages d'IP précises (ou utilisez un VPN ou un bastion host).
- Utilisez des security groups (AWS) ou des NSG (Azure) pour un contrôle fin.

### Renforcement de l'OS
- Appliquez régulièrement les mises à jour de sécurité (`sudo apt upgrade`, `yum update`).
- Désactivez les services inutiles et les comptes par défaut.
- Utilisez fail2ban pour bloquer les tentatives de force brute sur SSH.
- Renforcez SSH : désactivez la connexion root, utilisez l'authentification par clé, changez le port par défaut si nécessaire.

### Segmentation réseau
- Placez les bases de données et les caches dans des sous-réseaux privés sans accès internet.
- Utilisez une DMZ pour les services exposés au public.
- Appliquez le principe du moindre privilège aux accès réseau.

### Secrets dans l'infrastructure
- Ne stockez jamais de secrets dans les variables d'environnement CI/CD sans chiffrement.
- Utilisez les rôles IAM du fournisseur cloud pour les instances EC2/VM plutôt que des clés longue durée.

---

## Journalisation et supervision

### Que journaliser
- Les événements d'authentification (succès/échec).
- Les décisions de contrôle d'accès (échecs d'autorisation).
- Les actions d'administration (création d'utilisateur, suppression, modification des permissions).
- Les changements de schéma de base de données.
- Les erreurs système et les exceptions.
- Les requêtes et réponses API (en masquant les données sensibles).

### Ce qu'il ne faut pas journaliser
- Les mots de passe, secrets, tokens et PII (Personally Identifiable Information), sauf s'ils sont hachés ou masqués.
- Les numéros complets de carte bancaire.

### Alertes
- Mettez en place des alertes pour :
  - plusieurs échecs de connexion (force brute potentielle) ;
  - des schémas d'accès inhabituels (par exemple depuis de nouveaux lieux ou à des heures anormales) ;
  - la création de nouveaux comptes administrateurs ;
  - des taux d'erreur élevés ou des pics de latence.
- Utilisez un SIEM (Security Information and Event Management) pour une corrélation avancée.

### Rétention des logs
- Conservez les logs au moins 30 à 90 jours selon les obligations réglementaires.
- Stockez-les dans un système centralisé et résistant à la falsification (par exemple ELK Stack, Splunk, Datadog).

---

## Secure Development Lifecycle (SDL)

1. **Formation** : veillez à ce que les développeurs comprennent les vulnérabilités courantes.
2. **Modélisation des menaces** : identifiez les menaces potentielles dès la phase de conception.
3. **Standards de développement sécurisé** : imposez-les via des linters et des checklists de revue de code.
4. **SAST** (Static Application Security Test) : analysez le code source à la recherche de vulnérabilités (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Security Test) : analysez les applications en cours d'exécution (OWASP ZAP, Burp Suite).
6. **SCA** (Software Composition Analysis) : analysez les dépendances.
7. **Test d'intrusion** : réalisez régulièrement des exercices d'ethical hacking.
8. **Bug bounty** : encouragez les chercheurs externes à signaler les vulnérabilités de manière responsable.
9. **Plan de réponse aux incidents** : disposez d'un plan clair pour le cas où une compromission est détectée.

---

## Checklist d'urgence (en cas de suspicion de compromission)

1. **Ne paniquez pas** — mais agissez vite.
2. **Isolez** les systèmes concernés (déconnectez-les du réseau si nécessaire).
3. **Préservez les preuves** : capturez les logs, dumps mémoire et images disque.
4. **Identifiez** le périmètre : quels systèmes, quelles données.
5. **Faites tourner** tous les identifiants et secrets compromis.
6. **Corrigez** la vulnérabilité.
7. **Informez** les utilisateurs concernés et les autorités de régulation si nécessaire (dans les délais légaux).
8. **Réalisez un post-mortem** pour comprendre la cause racine et améliorer les processus.
