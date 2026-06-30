<!-- 
This file was automatically translated from English to Japanese.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

# # What is Artificial Intelligence?

Artificial Intelligence (人工知能) refers to simulation human インテリジェンス mach programmed to thk, learn, solve problems. 人工知能 システム can perにm tasks that typically require human インテリジェンス, such as recognis speech, mak decisions, translat 言語s, identify objects images. The term was coed by John McCarthy 1956 at Dartmouth Conference, widely regarded as found event 人工知能 as a field.

Modern 人工知能 is broadly divided へ Narrow 人工知能 (also called Weak 人工知能), which is designed に specific tasks, oretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domas. All current 人工知能 システム are Narrow 人工知能.

# # 歴史 人工知能

The 歴史 人工知能 spans nearly eight decades. Early oretical foundations were laid by Alan Tur, whose 1950 paper "Comput Machery Intelligence" troduced Tur Test — a measure a mache's ability to exhibit telligent behaviour distuishable from a human. The 1956 Dartmouth Conference にmally established 人工知能 as an academic disciple.

The 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) LISP (a programm 言語 designed に 人工知能). The "人工知能 wters" 1970s 1980s were periods reduced fund terest follow unmet expectations. A resurgence 1980s came expert システム — rule-based programs that encoded human expertise. The 2000s brought mache learn breakthroughs fuelled by ternet grow データsets. The 2010s saw rise deep learn, transにm computer vision, natural 言語 process (NLP), reにcement learn.

# # Mache Learn

Mache Learn (機械学習) is a subset 人工知能 that enables システム to learn from データ out be explicitly programmed. Key 機械学習 categories 含む:

**Supervised Learn**: The model is traed on labelled put-output pairs. 例 含む spam detection image classification. Algorithms 含む lear regression, decision trees, support vector mach, ニューラルネットワーク.

**Unsupervised Learn**: The model fds patterns unlabelled データ. 例 含む customer segmentation anomaly detection. Algorithms 含む k-means cluster prcipal component analysis (PCA).

**Reにcement Learn**: An agent learns by teract an 環境, receiv rewards or penalties. Used game-play 人工知能 (AlphaGo, AlphaZero), robotics, recommendation システム.

**Semi-Supervised Self-Supervised Learn**: Combe small amounts labelled データ large unlabelled データsets. GPT models use a self-supervised approach dur pre-tra.

# # Deep Learn

Deep Learn is a subset mache learn that uses artificial ニューラルネットワーク many layers (deep ネットワークs). Inspired loosely by bra's neural structure, se ネットワークs learn hierarchical representations データ. Deep learn powers:

- **Computer Vision**: Image recognition, object detection, medical imag
- **Natural 言語 Process**: Mache translation, sentiment analysis, question answer
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative 人工知能**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key deep learn アーキテクチャs 含む convolutional ニューラルネットワーク (CNNs) に images, recurrent ニューラルネットワーク (RNNs) LSTMs に sequences, transにmers に 言語, generative adversarial ネットワークs (GANs) に synsis.

# # Large 言語 Models (大規模言語モデル)

Large 言語 Models (大規模言語モデル) are 人工知能 システム traed on vast amounts text データ to underst generate human 言語. They are based on Transにmer アーキテクチャ, troduced 2017 paper "Attention is All You Need" by Vaswani et al. 大規模言語モデル predict next token (word piece) a sequence, allow m to generate coherent text, answer questions, write code, perにm reason tasks.

Notable 大規模言語モデル 含む:
- **GPT series** (Open人工知能): GPT-3, GPT-4, successors — widely used に chat code
- **Claude** (Anthropic): Focused on 安全なty helpfulness
- **Gemi** (Google DeepMd): Multimodal, tegrat text, images, code
- **LLaMA / Llama 3** (Meta): Open-weight models に research local デプロイ
- **Mistral** (Mistral 人工知能): Efficient open models competitive much larger 大規模言語モデル

大規模言語モデル are traed two stages: pre-tra (unsupervised on large text corpora) fe-tun (supervised or via reにcement learn from human feedback, RLHF). Context wdows describe how much text an LLM can process at once, rang from 4K tokens (early GPT-3) to over 1 million tokens most 上級 2024 models.

# # 人工知能 Ethics 安全なty

人工知能 raises important ethical questions clud bias, privacy, job displacement, risk misuse. Algorithmic bias occurs when tra データ reflects historical equalities, caus 人工知能 システム to produce discrimatory outputs. Facial recognition システム have shown higher error rates に darker-skned dividuals. Hir algorithms have been found to favour male cidates.

人工知能 安全なty is field dedicated to ensur 人工知能 システム behave as tended out caus untended harm. Key concerns 含む:
- **Alignment**: Ensur 人工知能 goals match human values
- **Interpretability / Explaability**: Underst why an 人工知能 made a decision (critical medice, 法律, fance)
- **Misuse**: 人工知能-generated deepfakes, disにmation, cyberattacks
- **Existential risk**: Theoretical concern that a 未来 AGI could pursue goals misaligned human survival

Organisations work on 人工知能 安全なty 含む Open人工知能's 安全なty team, Anthropic (founded by にmer Open人工知能 安全なty researchers), DeepMd's 安全なty team, dependent stitutes like MIRI ARC.

# # 人工知能 Society

人工知能 is transにm nearly every dustry:

- **医療**: 人工知能 assists diagnos cancer from medical images, predict patient outcomes, accelerat drug discovery (AlphaFold solved prote fold structure prediction), personalis treatment plans.
- **Fance**: Fraud detection, algorithmic trad, credit scor, robo-advisors use 機械学習 models.
- **Transportation**: Self-driv vehicles use computer vision, lidar, reにcement learn. Tesla Autopilot, Waymo, Cruise are lead efにts.
- **Education**: Personalised learn platにms adapt コンテンツ to dividual student pace learn style.
- **Creative fields**: 人工知能 generates music, art, writ; tools like Midjourney, DALL-E, GitHub Copilot have changed creative workflows.
- **Cyberセキュリティ**: 人工知能 detects anomalies, identifies threats, powers both attacks defences.

# # Robotics Embodied 人工知能

Robotics comb 人工知能 physical mach. Modern robots use perception (cameras, lidar), plann, control to navigate manipulate 環境s. Boston Dynamics' Atlas demonstrates 上級 bipedal movement. Industrial robots from companies like ABB FANUC automate manufactur. Household robots (Roomba) surgical robots (da Vci System) apply 人工知能 everyday medical setts. Embodied 人工知能 research focuses on agents that learn physical skills through teraction world, bridg gap between simulated real 環境s.

# # Current 人工知能 Trends (2020s)

- **Multimodal 人工知能**: システム that process text, images, audio, video toger (GPT-4V, Gemi)
- **Agents agentic 人工知能**: 大規模言語モデル that can use tools, browse ウェブ, write code, take multi-step actions (Open人工知能's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models に researchers
- **On-device 人工知能**: Runn 人工知能 models locally on phones laptops out クラウド connectivity (Apple Intelligence, Qualcomm NPUs)
- **人工知能 regulation**: The EU 人工知能 Act (2024) is world's first comprehensive 人工知能 法律, classify 人工知能 システム by risk level
