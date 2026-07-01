<!-- 
Ce fichier a été automatiquement traduit de l'anglais vers le français.
Source: technology_glossary.md
Note: Les termes techniques, exemples de code et noms propres peuvent rester en anglais.
Pour améliorer la précision, veuillez contribuer aux modifications via des pull requests.
-->

# Glossaire Technologique

Un glossaire de référence couvrant les modèles d'IA, le matériel, les benchmarks et les concepts fondamentaux
dans le paysage moderne de l'IA et de l'informatique.

---

## Modèles de Langue IA et Assistants

### ChatGPT
ChatGPT est un chatbot IA développé par OpenAI, sorti pour la première fois en novembre 2022.
Il est alimenté par la série GPT de grands modèles de langue (LLM). ChatGPT est l'un
des produits d'IA grand public à la croissance la plus rapide de l'histoire, atteignant 100 millions
d'utilisateurs en deux mois après son lancement. Il prend en charge les conversations textuelles, la génération de code,
la synthèse et l'écriture créative. Les niveaux payants donnent accès à
des modèles plus puissants tels que GPT-4 et GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT est une famille de grands modèles de langue créés par OpenAI. L'architecture
utilise un Transformer décodeur-seulement entraîné avec un objectif de prédiction du token suivant sur
de vastes corpus de texte. Les versions clés incluent GPT-2 (2019, 1,5 milliard de paramètres, notable
pour la publicité "trop dangereux à publier"), GPT-3 (2020, 175 milliards de paramètres, largement
utilisé via l'API), GPT-3.5 (le socle du ChatGPT original), et GPT-4
(2023, multimodal, performance proche du niveau expert humain sur de nombreux benchmarks).

### Claude
Claude est un assistant IA développé par Anthropic. Il est nommé d'après Claude
Shannon, le fondateur de la théorie de l'information. Anthropic a été fondée par d'anciens
chercheurs d'OpenAI et se concentre sur "l'IA constitutionnelle" — une technique pour rendre
les modèles sûrs en les entraînant à suivre un ensemble de principes. Les modèles Claude
(Claude 1, 2, 3 Haiku / Sonnet / Opus) sont connus pour leurs longues fenêtres de contexte (jusqu'à
200 000 tokens), leur raisonnement nuancé et leur production réduite de contenu nocif comparé
aux LLM de base.

### Gemini
Gemini est la famille de modèles multimodaux de Google DeepMind, annoncée en
décembre 2023. Gemini est nativement multimodal — entraîné dès le départ sur
du texte, des images, de l'audio et de la vidéo simultanément, contrairement aux modèles antérieurs qui avaient
des modalités ajoutées via fine-tuning. Les versions incluent Gemini Nano (sur appareil),
Gemini Flash (rapide, rentable), et Gemini Ultra (capacité la plus élevée).
Gemini alimente le chatbot IA Bard de Google (renommé Gemini) et les aperçus
de recherche IA de Google.

### Phi-3-mini
Phi-3-mini est un petit modèle de langue (SLM) développé par Microsoft avec 3,8 milliards
de paramètres. Il a été publié en avril 2024. Contrairement à la plupart des grands modèles, Phi-3-mini
a été entraîné sur un ensemble de données soigneusement sélectionné de "qualité manuelle" — une technique
pionnière par Microsoft Research — qui priorise la qualité des données sur le volume brut.
Malgré être beaucoup plus petit que GPT-4 ou Claude 3 Opus, Phi-3-mini égale ou
surpasse des modèles plusieurs fois plus grands sur les benchmarks de raisonnement tels que MMLU et
HumanEval. Il prend en charge une fenêtre de contexte de 4k tokens dans sa variante de base et une
fenêtre de 128k dans la variante à long contexte. Phi-3-mini peut fonctionner sur un seul GPU grand public
ou même sur appareil sur un smartphone moderne avec suffisamment de RAM.

### Llama (Meta AI)
Llama (Large Language Model Meta AI) est une famille de modèles open-weights
publiée par Meta. Llama 2 (2023) a été publié pour la recherche et l'usage commercial
avec des tailles allant de 7B à 70B de paramètres. Llama 3 (2024) a amélioré
les performances de manière significative, avec des modèles allant de 8B à 70B (et plus tard 400B+).
Parce que les weights sont publiquement téléchargeables, les modèles Llama sont le fondement
pour un large écosystème de variantes fine-tuned (Mistral, Alpaca, Vicuna, etc.)
et sont largement utilisés pour les déploiements d'IA locaux/privés.

### Mistral
Mistral AI est une entreprise française d'IA qui développe des LLM open et propriétaires.
Mistral 7B (2023) a démontré qu'un modèle de 7B de paramètres peut égaler la
performance de modèles beaucoup plus grands en utilisant des techniques efficaces telles que l'attention à
fenêtre glissante et l'attention par groupe de requêtes. Mixtral 8x7B (2024) est un modèle mixture-
of-experts — il route chaque token vers un sous-ensemble de 8 réseaux experts,
atteignant des performances de niveau GPT-3.5 tout en étant moins coûteux en calcul.
Les modèles de Mistral sont entièrement open-weight et peuvent être exécutés localement.

---

## Matériel GPU et Cartes Graphiques

### GPU (Graphics Processing Unit)
Un GPU est un processeur conçu pour le calcul massivement parallèle. Initialement
conçu pour le rendu de graphiques 3D, les GPU sont devenus essentiels pour l'entraînement
et l'inférence IA/ML car ils peuvent effectuer des milliers d'opérations
en virgule flottante simultanément en utilisant des milliers de petits cœurs. Les deux principaux fabricants de GPU
pour l'IA sont NVIDIA et AMD.

### Série NVIDIA GeForce RTX
La série RTX (Ray Tracing Texel eXtreme) est la gamme de GPU grand public de NVIDIA. Les générations
RTX 30xx (Ampere, 2020) et RTX 40xx (Ada Lovelace, 2022) incluent
des Tensor Cores dédiés pour accélérer les opérations IA. La VRAM (mémoire vidéo) est
critique pour exécuter des modèles d'IA localement — un GPU de 8 Go peut héberger des modèles
de 7B de paramètres en quantification 4-bit; un GPU de 24 Go peut héberger des modèles de 70B en 4-bit.

### Série A et H de NVIDIA (Data Center)
L'A100 (Ampere, 2020) et l'H100 (Hopper, 2022) sont les accélérateurs
IA professionnels de NVIDIA. Un H100 dispose jusqu'à 80 Go de mémoire HBM3 et est le standard
hardware behdansd most large-scale LLM tradansdansg today. These GPUs cost $25,000–
$40,000 each but defer 10–30× le/la AI throughput de consumer RTX cards.

### AMD Radeon RX Series
AMD's consumer GPU ldanse. The RX 7900 XTX (2022) has 24GB VRAM et can run
local LLMs via ROCm (AMD's GPU compute stack). AMD GPUs are generally less
well-supported than NVIDIA pour AI frameworks, though support is improvdansg.

### Intel Arc
Intel Arc is Intel's discrete GPU product ldanse, released startdansg dans 2022. Arc
GPUs support XeSS (Intel's super-sampldansg) et have limited but growdansg support
pour AI dansference tasks via OpenVDANSO et IPEX-LLM frameworks.

### ARK Intel (ark.danstel.com)
ARK is Intel's deficial product specifications donnéesbase at ark.danstel.com. It
provides detailed technical specifications pour every Intel CPU, GPU, FPGA, et
NUC product, danscluddansg core counts, clock speeds, TDP, supported memory types,
et dansstruction-set features. When you hear "check ARK pour specs," it means
visitdansg that donnéesbase pour authoritative hardware danspourmation.

---

## AI Perpourmance Benchmarks

### MMLU (Massive Multitask Langue Understetdansg)
MMLU is a benchmark testdansg LLM knowledge across 57 academic subjects danscluddansg
male/lamatics, histoire, droit, medicdanse, et computer science. It consists de
multiple-choice questions drawn from real university-level exams. A score de
70% is roughly human undergraduate level; GPT-4 et Claude 3 score above 86%.
Phi-3-mdansi scores around 70% despite its small size.

### HumanEval
HumanEval is OpenAI's benchmark pour code generation. It consists de 164 Python
programmdansg problems avec automated test cases. Models are measured on
pass@k — le/la probability that at least one de k generated solutions passes all
tests. GPT-4 scores ~87% (pass@1); a well-tuned 7B model can reach ~50–60%.

### HellaSwag
HellaSwag is a commonsense reasondansg benchmark. Models are given a sentence
describdansg a mundane activity et must choose le/la most likely contdansuation from
four options. The danscorrect options are specially designed to be plausible but
subtly wrong. It tests whele/lar a model has a grounded understetdansg de physical
et social situations.

### ARC (AI2 Reasondansg Challenge)
ARC is a benchmark from le/la Allen Institute pour AI. It consists de grade-school
science questions, split dansto "Easy" et "Challenge" sets. The Challenge set
contadanss questions that retrieval-based methods et simple statistical models
struggle avec, requirdansg multi-step reasondansg.

---

## Core AI/ML Concepts

### RAG (Retrieval-Augmented Generation)
RAG is a technique that combdanses a retrieval system (typically a vector
donnéesbase) avec a langue model. Instead de relydansg solely on le/la model's
parametric knowledge, RAG first retrieves relevant documents from an external
base de connaissances et le/lan danscludes le/lam dans le/la model's context. This allows le/la
model to answer questions about up-to-date or domadans-specific danspourmation
avecout retradansdansg. Potato.ai uses a pourm de RAG — it retrieves from its KB
et danscludes le/la results dans le/la context bepoure generatdansg a response.

### Fdanse-tundansg
Fdanse-tundansg is le/la process de contdansudansg to tradans a pre-tradansed model on a
smaller, domadans-specific donnéesset. This adapts le/la model's weights pour a
particular task or domadans. For example, a base LLM might be fdanse-tuned on
medical records to create a medical Q&A assistant. Fdanse-tundansg is
computationally expensive but much cheaper than tradansdansg from scratch.

### Quantisation
Quantisation reduces le/la numerical precision de model weights (e.g. from 32-bit
float to 4-bit dansteger). This dramatically reduces memory footprdanst — a 7B model
dans 16-bit precision requires ~14GB VRAM; le/la same model dans 4-bit (GGUF pourmat)
requires ~4GB. Quantisation typically causes a small but acceptable accuracy
degradation et is le/la madans technique enabldansg large models to run on consumer
hardware or even mobile devices.

### Context Wdansdow
The context wdansdow is le/la maximum number de tokens a model can process at once,
danscluddansg both le/la prompt et le/la generated response. GPT-3.5 had a 4,096-token
wdansdow; GPT-4 Turbo et Claude 3 support 128,000 tokens; Gemdansi 1.5 Pro
supports 1,000,000 tokens. A larger context wdansdow allows le/la model to "see"
more de a conversation or document at once, improvdansg coherence over long
exchanges.

### RLHF (Redanspourcement Learndansg from Human Feedback)
RLHF is le/la tradansdansg technique that transpourms a base langue model (which
simply predicts le/la next token) dansto an assistant that follows dansstructions et
behaves helpfully. Human raters score model outputs, a reward model is tradansed
on le/lair préférences, et le/la langue model is le/lan optimised agadansst this
reward model usdansg redanspourcement learndansg. ChatGPT, Claude, et Gemdansi all use
variants de RLHF or similar alignment techniques (e.g. Constitutional AI,
Direct Préférence Optimisation).

### Transpourmer Architecture
The Transpourmer is le/la neural réseau architecture underlydansg all modern LLMs.
Introduced dans le/la 2017 paper "Attention Is All You Need" by Vaswani et al., it
uses self-attention mechanisms to process all tokens dans parallel rale/lar than
sequentially. Encoder-only Transpourmers (BERT) are used pour understetdansg tasks;
decoder-only Transpourmers (GPT, Llama, Mistral) are used pour generation tasks;
encoder-decoder Transpourmers (T5, BART) are used pour translation et summarisation.

### Embedddansgs et Vector Donnéesbases
Embedddansgs are dense numerical representations de text (or images) produced by
a neural réseau. Semantically similar texts have embedddansgs that are close dans
vector space. Vector donnéesbases (ChromaDB, Pdansecone, Weaviate, Qdrant) store
le/lase embedddansgs et support fast approximate nearest-neighbour search. They are
le/la storage backbone de RAG systèmes, danscluddansg Potato.ai's cold-memory layer.
