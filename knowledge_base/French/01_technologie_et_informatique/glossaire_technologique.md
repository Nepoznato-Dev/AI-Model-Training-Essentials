<!-- 
This file was automatically translated from English to French.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Glossaire technologique

Glossaire de référence couvrant les modèles d'IA, le matériel, les benchmarks et les concepts fondamentaux du paysage moderne de l'IA et de l'informatique.

---

## Modèles de langage d'IA et assistants

### ChatGPT
ChatGPT est un agent conversationnel d'IA développé par OpenAI et lancé pour la première fois en novembre 2022. Il repose sur la série de grands modèles de langage GPT (LLM). ChatGPT a été l'un des produits d'IA grand public à la croissance la plus rapide de l'histoire, atteignant 100 millions d'utilisateurs en deux mois. Il prend en charge la conversation textuelle, la génération de code, la synthèse et l'écriture créative. Les offres payantes donnent accès à des modèles plus puissants comme GPT-4 et GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT est une famille de grands modèles de langage créée par OpenAI. L'architecture utilise un Transformer de type décodeur entraîné avec un objectif de prédiction du token suivant sur d'immenses corpus de texte. Parmi les versions majeures figurent GPT-2 (2019, 1,5 milliard de paramètres, remarqué pour la controverse « too dangerous to release »), GPT-3 (2020, 175 milliards de paramètres, largement utilisé via l'API), GPT-3.5 (la base du ChatGPT d'origine) et GPT-4 (2023, multimodal, avec des performances proches du niveau d'expert humain sur de nombreux benchmarks).

### Claude
Claude est un assistant d'IA développé par Anthropic. Son nom rend hommage à Claude Shannon, le fondateur de la théorie de l'information. Anthropic a été fondée par d'anciens chercheurs d'OpenAI et met l'accent sur la « constitutional AI », une technique visant à rendre les modèles plus sûrs en les entraînant à suivre un ensemble de principes. Les modèles Claude (Claude 1, 2, 3 Haiku / Sonnet / Opus) sont connus pour leurs longues fenêtres de contexte (jusqu'à 200 000 tokens), leur raisonnement nuancé et une production moins nocive que celle des LLM de base.

### Gemini
Gemini est la famille de modèles d'IA multimodaux de Google DeepMind, annoncée en décembre 2023. Gemini est nativement multimodal : il a été entraîné dès le départ sur du texte, des images, de l'audio et de la vidéo simultanément, contrairement aux modèles plus anciens auxquels on ajoutait des modalités par fine-tuning. Les versions comprennent Gemini Nano (sur appareil), Gemini Flash (rapide et économique) et Gemini Ultra (la plus puissante). Gemini alimente le chatbot Bard de Google, renommé Gemini, ainsi que les AI Overviews de Google Search.

### Phi-3-mini
Phi-3-mini est un petit modèle de langage (SLM) développé par Microsoft avec 3,8 milliards de paramètres. Il est sorti en avril 2024. Contrairement à la plupart des grands modèles, Phi-3-mini a été entraîné sur un jeu de données soigneusement sélectionné, de qualité « textbook », une technique mise au point par Microsoft Research qui privilégie la qualité des données plutôt que leur volume brut. Malgré une taille bien inférieure à celle de GPT-4 ou Claude 3 Opus, Phi-3-mini égale ou dépasse des modèles plusieurs fois plus grands sur des benchmarks de raisonnement comme MMLU et HumanEval. Il prend en charge une fenêtre de contexte de 4k tokens dans sa version de base et de 128k dans sa version long context. Phi-3-mini peut fonctionner sur un seul GPU grand public, voire directement sur un smartphone moderne disposant de suffisamment de RAM.

### Llama (Meta AI)
Llama (Large Language Model Meta AI) est une famille de modèles à poids ouverts publiée par Meta. Llama 2 (2023) a été diffusé pour la recherche et l'usage commercial avec des tailles allant de 7B à 70B paramètres. Llama 3 (2024) a nettement amélioré les performances, avec des modèles allant de 8B à 70B, puis 400B+. Comme les poids sont téléchargeables publiquement, les modèles Llama servent de base à un vaste écosystème de variantes affinées (Mistral, Alpaca, Vicuna, etc.) et sont largement utilisés pour des déploiements d'IA locaux ou privés.

### Mistral
Mistral AI est une entreprise française d'IA qui développe des LLM ouverts et propriétaires. Mistral 7B (2023) a montré qu'un modèle de 7 milliards de paramètres pouvait rivaliser avec des modèles bien plus grands grâce à des techniques efficaces comme la sliding window attention et la grouped-query attention. Mixtral 8x7B (2024) est un modèle mixture-of-experts : chaque token est routé vers un sous-ensemble de 8 réseaux experts, ce qui lui permet d'atteindre un niveau proche de GPT-3.5 tout en coûtant moins cher en calcul. Les modèles de Mistral sont entièrement open-weight et peuvent être exécutés localement.

---

## Matériel GPU et cartes graphiques

### GPU (Graphics Processing Unit)
Un GPU est un processeur conçu pour le calcul massivement parallèle. Initialement développé pour le rendu graphique 3D, il est devenu essentiel pour l'entraînement et l'inférence en IA/ML, car il peut exécuter simultanément des milliers d'opérations en virgule flottante grâce à un très grand nombre de petits cœurs. Les deux principaux fabricants de GPU pour l'IA sont NVIDIA et AMD.

### Série NVIDIA GeForce RTX
La série RTX (Ray Tracing Texel eXtreme) est la gamme de GPU grand public de NVIDIA. Les générations RTX 30xx (Ampere, 2020) et RTX 40xx (Ada Lovelace, 2022) intègrent des Tensor Cores dédiés à l'accélération des opérations d'IA. La VRAM (mémoire vidéo) est essentielle pour exécuter des modèles d'IA localement : un GPU de 8 Go peut gérer des modèles de 7B paramètres en quantification 4 bits ; un GPU de 24 Go peut gérer des modèles de 70B en 4 bits.

### Séries NVIDIA A et H (centres de données)
Les A100 (Ampere, 2020) et H100 (Hopper, 2022) sont les accélérateurs professionnels d'IA de NVIDIA. Un H100 dispose de jusqu'à 80 Go de mémoire HBM3 et constitue le matériel de référence derrière la plupart des entraînements de grands LLM aujourd'hui. Ces GPU coûtent entre 25 000 et 40 000 dollars l'unité, mais offrent un débit IA 10 à 30 fois supérieur à celui des cartes RTX grand public.

### Série AMD Radeon RX
Il s'agit de la gamme de GPU grand public d'AMD. La RX 7900 XTX (2022) dispose de 24 Go de VRAM et peut faire tourner des LLM locaux via ROCm (la pile de calcul GPU d'AMD). Les GPU AMD sont généralement moins bien pris en charge que ceux de NVIDIA par les frameworks d'IA, même si le support progresse.

### Intel Arc
Intel Arc est la gamme de GPU dédiés d'Intel, lancée à partir de 2022. Les GPU Arc prennent en charge XeSS (la technologie de super-échantillonnage d'Intel) et offrent un support encore limité mais croissant pour les tâches d'inférence IA via les frameworks OpenVINO et IPEX-LLM.

### ARK Intel (ark.intel.com)
ARK est la base de données officielle des spécifications produit d'Intel, disponible sur ark.intel.com. Elle fournit des spécifications techniques détaillées pour chaque CPU, GPU, FPGA et produit NUC d'Intel, notamment le nombre de cœurs, les fréquences, le TDP, les types de mémoire pris en charge et les jeux d'instructions. Lorsque l'on vous conseille de consulter ARK pour les spécifications, cela signifie qu'il faut se référer à cette base de données pour obtenir une information matérielle faisant autorité.

---

## Tests de référence de performance en IA

### MMLU (Massive Multitask Language Understanding)
MMLU est un benchmark qui évalue les connaissances des LLM dans 57 matières universitaires, dont les mathématiques, l'histoire, le droit, la médecine et l'informatique. Il se compose de questions à choix multiple issues de véritables examens de niveau universitaire. Un score de 70 % correspond approximativement au niveau d'un étudiant de premier cycle ; GPT-4 et Claude 3 dépassent 86 %. Phi-3-mini obtient environ 70 % malgré sa petite taille.

### HumanEval
HumanEval est le benchmark d'OpenAI pour la génération de code. Il comprend 164 problèmes de programmation Python accompagnés de cas de test automatisés. Les modèles sont évalués avec la métrique pass@k, c'est-à-dire la probabilité qu'au moins une des k solutions générées réussisse tous les tests. GPT-4 atteint environ 87 % en pass@1 ; un modèle 7B bien ajusté peut monter à 50–60 %.

### HellaSwag
HellaSwag est un benchmark de raisonnement de bon sens. Les modèles reçoivent une phrase décrivant une activité banale et doivent choisir la suite la plus probable parmi quatre options. Les mauvaises réponses sont spécialement conçues pour paraître plausibles tout en étant subtilement incorrectes. Ce test mesure si un modèle possède une compréhension ancrée des situations physiques et sociales.

### ARC (AI2 Reasoning Challenge)
ARC est un benchmark créé par l'Allen Institute for AI. Il se compose de questions scientifiques de niveau primaire, réparties entre des ensembles « Easy » et « Challenge ». L'ensemble Challenge contient des questions qui résistent aux méthodes fondées sur la récupération d'information et aux modèles statistiques simples, et nécessitent un raisonnement en plusieurs étapes.

---

## Concepts fondamentaux de l'IA/ML

### RAG (Retrieval-Augmented Generation)
Le RAG est une technique qui combine un système de recherche d'information (généralement une base vectorielle) avec un modèle de langage. Au lieu de s'appuyer uniquement sur la connaissance paramétrique du modèle, le RAG récupère d'abord des documents pertinents depuis une base de connaissances externe, puis les insère dans le contexte du modèle. Cela permet au modèle de répondre à des questions portant sur des informations récentes ou spécifiques à un domaine sans nécessiter de réentraînement. Potato.ai utilise une forme de RAG : il interroge sa base de connaissances puis injecte les résultats dans le contexte avant de générer une réponse.

### Fine-tuning
Le fine-tuning est le processus qui consiste à poursuivre l'entraînement d'un modèle préentraîné sur un jeu de données plus petit et spécifique à un domaine. Cela adapte les poids du modèle à une tâche ou à un domaine particulier. Par exemple, un LLM de base peut être affiné sur des dossiers médicaux pour créer un assistant de questions-réponses médicales. Le fine-tuning est coûteux en calcul, mais reste bien moins onéreux qu'un entraînement complet depuis zéro.

### Quantification
La quantification réduit la précision numérique des poids d'un modèle (par exemple de flottants 32 bits à des entiers 4 bits). Cela diminue fortement l'empreinte mémoire : un modèle 7B en précision 16 bits nécessite environ 14 Go de VRAM, alors que le même modèle en 4 bits (format GGUF) demande environ 4 Go. La quantification entraîne généralement une légère perte de précision, mais acceptable, et constitue la technique principale qui permet d'exécuter de grands modèles sur du matériel grand public, voire sur des appareils mobiles.

### Fenêtre de contexte
La fenêtre de contexte correspond au nombre maximal de tokens qu'un modèle peut traiter en une seule fois, en incluant à la fois le prompt et la réponse générée. GPT-3.5 disposait d'une fenêtre de 4 096 tokens ; GPT-4 Turbo et Claude 3 prennent en charge 128 000 tokens ; Gemini 1.5 Pro monte à 1 000 000 de tokens. Une fenêtre de contexte plus grande permet au modèle de « voir » une plus grande partie d'une conversation ou d'un document simultanément, ce qui améliore la cohérence sur les échanges longs.

### RLHF (Reinforcement Learning from Human Feedback)
Le RLHF est une technique d'entraînement qui transforme un modèle de langage de base (qui prédit simplement le token suivant) en assistant capable de suivre des instructions et de se comporter de manière utile. Des évaluateurs humains notent les sorties du modèle, un modèle de récompense est entraîné à partir de leurs préférences, puis le modèle de langage est optimisé contre ce modèle de récompense au moyen de l'apprentissage par renforcement. ChatGPT, Claude et Gemini utilisent tous des variantes du RLHF ou des techniques d'alignement proches (par exemple Constitutional AI ou Direct Preference Optimisation).

### Architecture Transformer
Le Transformer est l'architecture de réseau neuronal à la base de tous les LLM modernes. Présenté dans l'article de 2017 « Attention Is All You Need » de Vaswani et al., il utilise des mécanismes d'auto-attention pour traiter tous les tokens en parallèle plutôt que séquentiellement. Les Transformers encodeur seul (BERT) sont utilisés pour les tâches de compréhension ; les Transformers décodeur seul (GPT, Llama, Mistral) servent à la génération ; les Transformers encodeur-décodeur (T5, BART) sont employés pour la traduction et la synthèse.

### Embeddings et bases de données vectorielles
Les embeddings sont des représentations numériques denses du texte (ou des images) produites par un réseau neuronal. Des textes sémantiquement proches ont des embeddings proches dans l'espace vectoriel. Les bases de données vectorielles (ChromaDB, Pinecone, Weaviate, Qdrant) stockent ces embeddings et permettent une recherche approximative rapide des plus proches voisins. Elles constituent l'épine dorsale du stockage des systèmes RAG, y compris la couche de mémoire froide de Potato.ai.
