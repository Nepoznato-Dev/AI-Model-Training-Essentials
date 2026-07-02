# Glossaire technologique

Un glossaire de référence couvrant les modèles d'IA, le matériel, les benchmarks et les concepts fondamentaux
dans le paysage moderne de l'IA et de l'informatique.

---

## Modèles de langage d'IA et assistants

### ChatGPT
ChatGPT est un chatbot d'IA développé par OpenAI, publié pour la première fois en novembre 2022.
Il repose sur la série GPT de grands modèles de langage (LLMs). ChatGPT est l'un
des produits d'IA grand public à la croissance la plus rapide de l'histoire, atteignant 100 millions
d'utilisateurs en deux mois après son lancement. Il prend en charge la conversation textuelle, la génération
de code, la synthèse et l'écriture créative. Les offres payantes donnent accès à
des modèles plus puissants tels que GPT-4 et GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT est une famille de grands modèles de langage créée par OpenAI. L'architecture
utilise un Transformer décodeur seul entraîné avec un objectif de prédiction du token suivant sur
d'immenses corpus textuels. Les versions clés incluent GPT-2 (2019, 1,5B paramètres, notable
pour la publicité « too dangerous to release »), GPT-3 (2020, 175B paramètres, largement
utilisé via l'API), GPT-3.5 (la base du ChatGPT d'origine) et GPT-4
(2023, multimodal, performances proches du niveau d'un expert humain sur de nombreux benchmarks).

### Claude
Claude est un assistant d'IA développé par Anthropic. Il porte le nom de Claude
Shannon, le fondateur de la théorie de l'information. Anthropic a été fondée par d'anciens
chercheurs d'OpenAI et se concentre sur la « constitutional AI » — une technique destinée à rendre les
modèles plus sûrs en les entraînant à suivre un ensemble de principes. Les modèles Claude
(Claude 1, 2, 3 Haiku / Sonnet / Opus) sont connus pour leurs longues fenêtres de contexte (jusqu'à
200,000 tokens), leur raisonnement nuancé et une réduction des sorties nuisibles par rapport aux
LLMs de référence.

### Gemini
Gemini est la famille de modèles d'IA multimodaux de Google DeepMind, annoncée en
décembre 2023. Gemini est nativement multimodal — entraîné dès le départ sur
du texte, des images, de l'audio et de la vidéo simultanément, contrairement aux modèles antérieurs auxquels on avait
ajouté des modalités via fine-tuning. Les versions incluent Gemini Nano (sur appareil),
Gemini Flash (rapide, économique) et Gemini Ultra (capacité maximale).
Gemini alimente le chatbot d'IA Bard de Google (renommé Gemini) ainsi que Google Search AI
Overviews.

### Phi-3-mini
Phi-3-mini est un small language model (SLM) développé par Microsoft avec 3.8B
paramètres. Il a été publié en avril 2024. Contrairement à la plupart des grands modèles, Phi-3-mini
a été entraîné sur un jeu de données soigneusement sélectionné de qualité « textbook » — une technique
pionnière de Microsoft Research — qui privilégie la qualité des données au volume brut.
Bien plus petit que GPT-4 ou Claude 3 Opus, Phi-3-mini atteint ou
dépasse des modèles plusieurs fois plus grands sur des benchmarks de raisonnement tels que MMLU et
HumanEval. Il prend en charge une fenêtre de contexte de 4k tokens dans sa variante de base et une fenêtre de 128k
dans la variante long-context. Phi-3-mini peut fonctionner sur un seul GPU grand public
ou même sur appareil sur un smartphone moderne disposant de suffisamment de RAM.

### Llama (Meta AI)
Llama (Large Language Model Meta AI) est une famille de modèles à poids ouverts
publiée par Meta. Llama 2 (2023) a été publié pour la recherche et l'usage commercial
avec des tailles allant de 7B à 70B paramètres. Llama 3 (2024) a significativement amélioré les
performances, avec des modèles allant de 8B à 70B (puis 400B+).
Parce que les poids sont téléchargeables publiquement, les modèles Llama constituent la base
d'un vaste écosystème de variantes fine-tuned (Mistral, Alpaca, Vicuna, etc.)
et sont largement utilisés pour des déploiements d'IA locaux/privés.

### Mistral
Mistral AI est une entreprise française d'IA qui développe des LLMs ouverts et propriétaires.
Mistral 7B (2023) a démontré qu'un modèle de 7B paramètres peut égaler les
performances de modèles bien plus grands grâce à des techniques efficaces telles que le sliding
window attention et le grouped-query attention. Mixtral 8x7B (2024) est un modèle mixture-
of-experts — il route chaque token vers un sous-ensemble de 8 réseaux experts,
attribuant des performances de niveau GPT-3.5 avec un coût de calcul plus faible.
Les modèles de Mistral sont entièrement open-weight et peuvent être exécutés localement.

---

## Matériel GPU et cartes graphiques

### GPU (Graphics Processing Unit)
Un GPU est un processeur conçu pour le calcul massivement parallèle. Initialement
créés pour le rendu graphique 3D, les GPU sont devenus essentiels pour l'entraînement
et l'inférence en IA/ML parce qu'ils peuvent effectuer des milliers d'opérations en virgule flottante
simultanément grâce à des milliers de petits cœurs. Les deux principaux fabricants de GPU
pour l'IA sont NVIDIA et AMD.

### Série NVIDIA GeForce RTX
La série RTX (Ray Tracing Texel eXtreme) est la gamme de GPU grand public de NVIDIA. Les générations RTX
30xx (Ampere, 2020) et RTX 40xx (Ada Lovelace, 2022) incluent des Tensor Cores dédiés pour accélérer les opérations d'IA. La VRAM (video RAM) est
critique pour exécuter des modèles d'IA localement — un GPU de 8GB peut gérer des modèles de 7B paramètres
en quantization 4-bit ; un GPU de 24GB peut gérer des modèles 70B en 4-bit.

### Séries NVIDIA A et H (Data Centre)
Les A100 (Ampere, 2020) et H100 (Hopper, 2022) sont les accélérateurs professionnels d'IA de NVIDIA.
Un H100 dispose de jusqu'à 80GB de mémoire HBM3 et constitue le matériel
standard derrière la plupart des entraînements de grands LLMs aujourd'hui. Ces GPU coûtent entre $25,000 et
$40,000 l'unité mais offrent 10 à 30× le débit IA des cartes RTX grand public.

### Série AMD Radeon RX
La gamme de GPU grand public d'AMD. La RX 7900 XTX (2022) dispose de 24GB de VRAM et peut exécuter des
LLMs locaux via ROCm (la pile de calcul GPU d'AMD). Les GPU AMD sont généralement moins
bien pris en charge que ceux de NVIDIA par les frameworks d'IA, même si le support s'améliore.

### Intel Arc
Intel Arc est la gamme de GPU discrets d'Intel, lancée à partir de 2022. Les GPU Arc
prennent en charge XeSS (le super-sampling d'Intel) et bénéficient d'un support encore limité mais croissant
pour les tâches d'inférence IA via les frameworks OpenVINO et IPEX-LLM.

### ARK Intel (ark.intel.com)
ARK est la base officielle des spécifications produits d'Intel sur ark.intel.com. Elle
fournit des spécifications techniques détaillées pour chaque produit CPU, GPU, FPGA et
NUC d'Intel, notamment le nombre de cœurs, les fréquences, le TDP, les types de mémoire pris en charge
et les fonctionnalités du jeu d'instructions. Quand vous entendez « check ARK for specs », cela signifie
consulter cette base pour obtenir des informations matérielles faisant autorité.

---

## Benchmarks de performance IA

### MMLU (Massive Multitask Language Understanding)
MMLU est un benchmark qui teste les connaissances des LLMs dans 57 matières universitaires, notamment
les mathématiques, l'histoire, le droit, la médecine et l'informatique. Il se compose de
questions à choix multiple tirées de véritables examens universitaires. Un score de
70 % correspond approximativement au niveau d'un étudiant de premier cycle ; GPT-4 et Claude 3 dépassent 86 %.
Phi-3-mini obtient environ 70 % malgré sa petite taille.

### HumanEval
HumanEval est le benchmark d'OpenAI pour la génération de code. Il se compose de 164 problèmes de programmation Python
avec des cas de test automatisés. Les modèles sont évalués sur
pass@k — la probabilité qu'au moins une des k solutions générées réussisse tous les
tests. GPT-4 obtient ~87 % (pass@1) ; un modèle 7B bien réglé peut atteindre ~50–60 %.

### HellaSwag
HellaSwag est un benchmark de raisonnement de sens commun. Les modèles reçoivent une phrase
décrivant une activité banale et doivent choisir la continuation la plus probable parmi
quatre options. Les options incorrectes sont spécialement conçues pour sembler plausibles mais
subtilement fausses. Il teste si un modèle possède une compréhension ancrée des situations physiques
et sociales.

### ARC (AI2 Reasoning Challenge)
ARC est un benchmark de l'Allen Institute for AI. Il se compose de questions de sciences de niveau
aire scolaire, réparties entre ensembles « Easy » et « Challenge ». L'ensemble Challenge
contient des questions auxquelles les méthodes basées sur la recherche et les modèles statistiques simples
répondent difficilement, ce qui exige un raisonnement en plusieurs étapes.

---

## Concepts fondamentaux de l'IA/ML

### RAG (Retrieval-Augmented Generation)
RAG est une technique qui combine un système de retrieval (généralement une vector
database) avec un modèle de langage. Au lieu de s'appuyer uniquement sur la connaissance
paramétrique du modèle, RAG récupère d'abord des documents pertinents depuis une base de
connaissances externe puis les inclut dans le contexte du modèle. Cela permet au
modèle de répondre à des questions sur des informations à jour ou spécifiques à un domaine
sans réentraînement. Potato.ai utilise une forme de RAG — il récupère depuis sa KB
et inclut les résultats dans le contexte avant de générer une réponse.

### Fine-tuning
Le fine-tuning consiste à poursuivre l'entraînement d'un modèle préentraîné sur un
jeu de données plus petit et spécifique à un domaine. Cela adapte les poids du modèle à une
tâche ou un domaine particulier. Par exemple, un LLM de base peut être fine-tuned sur
des dossiers médicaux pour créer un assistant de questions-réponses médical. Le fine-tuning est
coûteux en calcul mais bien moins que l'entraînement depuis zéro.

### Quantization
La quantization réduit la précision numérique des poids du modèle (par ex. d'un format 32-bit
float à un entier 4-bit). Cela réduit drastiquement l'empreinte mémoire — un modèle 7B
en précision 16-bit nécessite ~14GB de VRAM ; le même modèle en 4-bit (format GGUF)
nécessite ~4GB. La quantization entraîne généralement une légère mais acceptable perte de précision
et constitue la principale technique qui permet d'exécuter de grands modèles sur du matériel grand public
ou même sur des appareils mobiles.

### Context Window
La context window est le nombre maximal de tokens qu'un modèle peut traiter en une fois,
y compris le prompt et la réponse générée. GPT-3.5 disposait d'une fenêtre de 4,096 tokens ;
GPT-4 Turbo et Claude 3 prennent en charge 128,000 tokens ; Gemini 1.5 Pro
prend en charge 1,000,000 tokens. Une context window plus grande permet au modèle de « voir »
une plus grande partie d'une conversation ou d'un document en une seule fois, améliorant la cohérence sur les
échanges longs.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF est la technique d'entraînement qui transforme un modèle de langage de base (qui
prédit simplement le token suivant) en assistant qui suit les instructions et
agit de manière utile. Des évaluateurs humains notent les sorties du modèle, un reward model est entraîné
sur leurs préférences, puis le modèle de langage est optimisé contre ce
reward model à l'aide du reinforcement learning. ChatGPT, Claude et Gemini utilisent tous
des variantes de RLHF ou de techniques d'alignement similaires (ex. Constitutional AI,
Direct Preference Optimisation).

### Architecture Transformer
Le Transformer est l'architecture de réseau neuronal à la base de tous les LLMs modernes.
Introduit dans l'article de 2017 « Attention Is All You Need » de Vaswani et al., il
utilise des mécanismes de self-attention pour traiter tous les tokens en parallèle plutôt que
séquentiellement. Les Transformers encoder-only (BERT) sont utilisés pour les tâches de compréhension ;
les Transformers decoder-only (GPT, Llama, Mistral) sont utilisés pour les tâches de génération ;
les Transformers encoder-decoder (T5, BART) sont utilisés pour la traduction et la synthèse.

### Embeddings et vector databases
Les embeddings sont des représentations numériques denses du texte (ou des images) produites par
un réseau neuronal. Les textes sémantiquement proches possèdent des embeddings proches dans
l'espace vectoriel. Les vector databases (ChromaDB, Pinecone, Weaviate, Qdrant) stockent
ces embeddings et permettent une recherche approximative rapide des plus proches voisins. Elles constituent
la base de stockage des systèmes RAG, y compris la couche de mémoire froide de Potato.ai.
