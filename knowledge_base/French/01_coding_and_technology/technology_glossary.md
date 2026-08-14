---
# Metadata
title: "Technology Glossary"
description: "Technical terminology (AI models, hardware, benchmarks)"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, glossary, coding-and-technology]
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
# Glossaire technologique
Un glossaire de référence couvrant les modèles d'IA, le matériel, les benchmarks et les concepts de base
dans le paysage moderne de l’IA et de l’informatique.
---

## Modèles linguistiques et assistants IA
### ChatGPT
ChatGPT est un chatbot IA développé par OpenAI, lancé pour la première fois en novembre 2022.
Il est alimenté par la série GPT de grands modèles de langage (LLM). ChatGPT en est un
des produits d'IA grand public à la croissance la plus rapide de l'histoire, atteignant 100 millions
utilisateurs dans les deux mois suivant le lancement. Il prend en charge les conversations textuelles, le code
génération, résumé et écriture créative. Les niveaux payants donnent accès à
des modèles plus puissants tels que GPT-4 et GPT-4o.
### GPT (Transformateur Génératif Pré-entraîné)
GPT est une famille de grands modèles de langage créés par OpenAI. L'architecture
utilise un transformateur réservé au décodeur entraîné avec un objectif de prédiction du prochain jeton sur
corpus de textes massifs. Les versions clés incluent GPT-2 (2019, paramètres 1,5B, notables
pour la publicité "trop dangereux à diffuser"), GPT-3 (2020, paramètres 175B, largement
utilisé via l'API), GPT-3.5 (l'épine dorsale du ChatGPT original) et GPT-4
(2023, multimodal, performances proches du niveau expert humain sur de nombreux benchmarks).
###Claude
Claude est un assistant IA développé par Anthropic. Il porte le nom de Claude
Shannon, la fondatrice de la théorie de l'information. Anthropic a été fondée par l'ancien
chercheurs d'OpenAI et se concentre sur « l'IA constitutionnelle » — une technique pour créer
rendre les modèles plus sûrs en les formant à suivre un ensemble de principes. Modèles Claude
(Claude 1, 2, 3 Haïku / Sonnet / Opus) sont connus pour leurs longues fenêtres contextuelles (jusqu'à
à 200 000 jetons), un raisonnement nuancé et une production nocive réduite par rapport à
LLM de base.
### Gémeaux
Gemini est la famille de modèles d'IA multimodaux de Google DeepMind, annoncée dans
Décembre 2023. Gemini est nativement multimodal – formé de A à Z
texte, images, audio et vidéo simultanément, contrairement aux modèles précédents qui avaient
modalités ajoutées via un réglage fin. Les versions incluent Gemini Nano (sur l'appareil),
Gemini Flash (rapide et économique) et Gemini Ultra (capacité la plus élevée).
Gemini alimente le chatbot IA Bard de Google (renommé Gemini) et Google Search AI
Aperçus.
### Phi-3-mini
Phi-3-mini est un petit modèle de langage (SLM) développé par Microsoft avec 3,8 B
paramètres. Il est sorti en avril 2024. Contrairement à la plupart des grands modèles, le Phi-3-mini
a été formé sur un ensemble de données soigneusement organisé de « qualité manuelle » – une technique
lancé par Microsoft Research – qui donne la priorité à la qualité des données plutôt qu’au volume brut.
Bien qu'ils soient bien plus petits que GPT-4 ou Claude 3 Opus, les matchs Phi-3-mini ou
surpasse les modèles plusieurs fois plus grands sur des benchmarks de raisonnement tels que MMLU et
HumanEval. Il prend en charge une fenêtre contextuelle de jeton 4k dans sa variante de base et une fenêtre contextuelle de 128k
fenêtre dans la variante à contexte long. Phi-3-mini peut fonctionner sur un seul GPU grand public
ou même sur l'appareil sur un smartphone moderne avec suffisamment de RAM.
### Lama (Méta AI)
Llama (Large Language Model Meta AI) est une famille de modèles à pondération ouverte
publié par Meta. Llama 2 (2023) a été publié à des fins de recherche et d'utilisation commerciale
avec des tailles allant de 7B à 70B paramètres. Lama 3 (2024) amélioré
performances de manière significative, avec des modèles allant de 8B à 70B (et plus tard 400B+).
Parce que les poids sont téléchargeables publiquement, les modèles Lama constituent la base
pour un large écosystème de variantes raffinées (Mistral, Alpaca, Vicuna, etc.)
et sont largement utilisés pour les déploiements d’IA locaux/privés.
###Mistral
Mistral AI est une société française d'IA qui développe des LLM ouverts et propriétaires.
Mistral 7B (2023) a démontré qu'un modèle à paramètres 7B peut correspondre au
performance de modèles beaucoup plus grands utilisant des techniques efficaces telles que le glissement
attention de la fenêtre et attention des requêtes groupées. Mixtral 8x7B (2023) est un mélange-
modèle d'experts - il achemine chaque jeton vers un sous-ensemble de 8 réseaux experts,
atteindre des performances de niveau GPT-3.5 tout en étant moins coûteux en termes de calcul.
Les modèles de Mistral sont entièrement ouverts et peuvent être utilisés localement.
---

## Matériel GPU et cartes graphiques
### GPU (unité de traitement graphique)
Un GPU est un processeur conçu pour le calcul massivement parallèle. À l'origine
conçus pour le rendu de graphiques 3D, les GPU sont devenus essentiels pour la formation AI/ML
et l'inférence car ils peuvent effectuer des milliers d'opérations en virgule flottante
en utilisant simultanément des milliers de petits noyaux. Les deux principaux fabricants de GPU
pour l'IA, NVIDIA et AMD.
### Série NVIDIA GeForce RTX
La série RTX (Ray Tracing Texel eXtreme) est la gamme de GPU grand public de NVIDIA. RTX
Les générations 30xx (Ampere, 2020) et RTX 40xx (Ada Lovelace, 2022) incluent
Des cœurs Tensor dédiés pour accélérer les opérations d’IA. La VRAM (RAM vidéo) est
essentiel pour exécuter des modèles d'IA localement : un GPU de 8 Go peut gérer le paramètre 7B
modèles en quantification 4 bits ; un GPU de 24 Go peut gérer les modèles 70B en 4 bits.
### NVIDIA Série A et Série H (centre de données)
L'A100 (Ampere, 2020) et le H100 (Hopper, 2022) sont l'IA professionnelle de NVIDIA
accélérateurs. Un H100 dispose de jusqu'à 80 Go de mémoire HBM3 et constitue la norme
matériel derrière la plupart des formations LLM à grande échelle aujourd'hui. Ces GPU coûtent 25 000 $.
40 000 $ chacune, mais offrent 10 à 30 fois le débit IA des cartes RTX grand public.
### Série AMD Radeon RX
Gamme de GPU grand public d'AMD. Le RX 7900 XTX (2022) dispose de 24 Go de VRAM et peut fonctionner
LLM locaux via ROCm (pile de calcul GPU d'AMD). Les GPU AMD sont généralement moins
bien pris en charge que NVIDIA pour les frameworks AI, bien que la prise en charge s'améliore.
### IntelArc
Intel Arc est la gamme de produits GPU discrets d'Intel, lancée à partir de 2022. Arc
Les GPU prennent en charge XeSS (le super-échantillonnage d'Intel) et bénéficient d'un support limité mais croissant
pour les tâches d'inférence d'IA via les frameworks OpenVINO et IPEX-LLM.
### ARK Intel (ark.intel.com)
ARK est la base de données officielle des spécifications des produits d'Intel sur ark.intel.com. Il
fournit des spécifications techniques détaillées pour chaque processeur Intel, GPU, FPGA et
Produit NUC, y compris le nombre de cœurs, les vitesses d'horloge, le TDP, les types de mémoire pris en charge,
et des fonctionnalités de jeu d'instructions. Lorsque vous entendez « vérifiez les spécifications d'ARK », cela signifie
visiter cette base de données pour obtenir des informations faisant autorité sur le matériel.
---

## Benchmarks de performances de l'IA
### MMLU (Compréhension massive du langage multitâche)
MMLU est une référence testant les connaissances LLM dans 57 matières académiques, notamment
mathématiques, histoire, droit, médecine et informatique. Il consiste en
questions à choix multiples tirées de véritables examens de niveau universitaire. Une vingtaine de
70 % correspondent à peu près au niveau humain du premier cycle ; GPT-4 et Claude 3 obtiennent un score supérieur à 86 %.
Le Phi-3-mini obtient un score d'environ 70 % malgré sa petite taille.
### HumanEval
HumanEval est la référence d'OpenAI pour la génération de code. Il se compose de 164 Python
problèmes de programmation avec des cas de tests automatisés. Les modèles sont mesurés sur
pass@k — la probabilité qu'au moins une des k solutions générées réussisse toutes
essais. GPT-4 obtient un score d'environ 87 % (réussite à 1) ; un modèle 7B bien réglé peut atteindre environ 50 à 60 %.
### HellaSwag
HellaSwag est une référence en matière de raisonnement de bon sens. Les modèles reçoivent une phrase
décrivant une activité banale et doit choisir la continuation la plus probable parmi
quatre options. Les options incorrectes sont spécialement conçues pour être plausibles mais
subtilement faux. Il teste si un modèle a une compréhension fondée des phénomènes physiques.
et situations sociales.
### ARC (Défi de raisonnement AI2)
ARC est une référence de l'Allen Institute for AI. Il s'agit d'une école primaire
questions scientifiques, divisées en ensembles « Facile » et « Défi ». L'ensemble du défi
contient des questions basées sur des méthodes de récupération et des modèles statistiques simples
lutter avec, nécessitant un raisonnement en plusieurs étapes.
---

## Concepts de base de l'IA/ML
### RAG (génération augmentée par récupération)
RAG est une technique qui combine un système de récupération (généralement un vecteur
base de données) avec un modèle de langage. Au lieu de s'appuyer uniquement sur le modèle
connaissances paramétriques, RAG récupère d'abord les documents pertinents à partir d'un
base de connaissances et les inclut ensuite dans le contexte du modèle. Cela permet au
modèle pour répondre aux questions sur les informations à jour ou spécifiques au domaine
sans reconversion. Potato.ai utilise une forme de RAG — il récupère de sa base de connaissances
et inclut les résultats dans le contexte avant de générer une réponse.
### Mise au point
Le réglage fin est le processus consistant à continuer à former un modèle pré-entraîné sur un
ensemble de données plus petit et spécifique au domaine. Cela adapte les poids du modèle pour un
une tâche ou un domaine particulier. Par exemple, un LLM de base peut être affiné sur
dossiers médicaux pour créer un assistant médical questions-réponses. Le réglage fin est
coûteux en termes de calcul, mais beaucoup moins cher que la formation à partir de zéro.
### Quantification
La quantification réduit la précision numérique des poids du modèle (par exemple à partir de 32 bits
flottant en entier de 4 bits). Cela réduit considérablement l'empreinte mémoire - un modèle 7B
en précision 16 bits, nécessite ~ 14 Go de VRAM ; le même modèle en 4 bits (format GGUF)
nécessite ~ 4 Go. La quantification entraîne généralement une précision faible mais acceptable
dégradation et constitue la principale technique permettant de faire fonctionner de grands modèles sur des ordinateurs grand public.
matériel ou même des appareils mobiles.
### Fenêtre contextuelle
La fenêtre contextuelle est le nombre maximum de jetons qu'un modèle peut traiter à la fois,
y compris à la fois l'invite et la réponse générée. GPT-3.5 avait un jeton de 4 096
fenêtre; GPT-4 Turbo et Claude 3 prennent en charge 128 000 jetons ; Gémeaux 1.5 Pro
prend en charge 1 000 000 de jetons. Une fenêtre contextuelle plus grande permet au modèle de « voir »
plus d'une conversation ou d'un document à la fois, améliorant ainsi la cohérence sur le long terme
échanges.
### RLHF (Apprentissage par renforcement à partir du feedback humain)
RLHF est la technique de formation qui transforme un modèle de langage de base (qui
prédit simplement le prochain jeton) dans un assistant qui suit les instructions et
se comporte de manière utile. Les évaluateurs humains notent les résultats du modèle, un modèle de récompense est formé
sur leurs préférences, et le modèle de langage est ensuite optimisé en fonction de cela
modèle de récompense utilisant l’apprentissage par renforcement. ChatGPT, Claude et Gemini utilisent tous
des variantes du RLHF ou des techniques d'alignement similaires (par exemple, l'IA constitutionnelle,
Optimisation des préférences directes).
### Architecture du transformateur
Le Transformer est l'architecture de réseau neuronal qui sous-tend tous les LLM modernes.
Introduit dans l'article de 2017 « L'attention est tout ce dont vous avez besoin » par Vaswani et al., il
utilise des mécanismes d'auto-attention pour traiter tous les jetons en parallèle plutôt que
séquentiellement. Les transformateurs à codeur uniquement (BERT) sont utilisés pour comprendre les tâches ;
Les transformateurs décodeur uniquement (GPT, Llama, Mistral) sont utilisés pour les tâches de génération ;
Les transformateurs codeur-décodeur (T5, BART) sont utilisés pour la traduction et la synthèse.
### Embeddings et bases de données vectorielles
Les intégrations sont des représentations numériques denses de texte (ou d'images) produites par
un réseau de neurones. Les textes sémantiquement similaires ont des intégrations proches
espace vectoriel. Magasin de bases de données vectorielles (ChromaDB, Pinecone, Weaviate, Qdrant)
ces intégrations et prennent en charge la recherche rapide du voisin le plus proche. Ils sont
l'épine dorsale de stockage des systèmes RAG, y compris la couche de mémoire froide de Potato.ai.