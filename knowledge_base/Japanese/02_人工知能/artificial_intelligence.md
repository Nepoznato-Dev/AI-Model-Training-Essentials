<!-- 
This file was automatically translated from English to Japanese.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) refers to その simulation の human intelligence で machines programmed to think, learn, と solve problems. AI システム can perform tasks that typically require human intelligence, such as recognising speech, making decisions, translating languages, と identifying objects で images. その term was coined by John McCarthy で 1956 at その Dartmouth Conference, widely regarded as その founding event の AI as a field.

Modern AI is broadly divided into Narrow AI (also called Weak AI), which is designed のために specific tasks, と その theoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domains. All current AI システム are Narrow AI.

## 歴史 の AI

その 歴史 の AI spans nearly eight decades. Early theoretical foundations were laid by Alan Turing, whose 1950 paper "コンピューティング Machinery と Intelligence" introduced その Turing Test — a measure の a machine's ability to exhibit intelligent behaviour indistinguishable from a human. その 1956 Dartmouth Conference formally established AI as an academic discipline.

その 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) と LISP (a programming 言語 designed のために AI). その "AI winters" の その 1970s と 1980s were periods の reduced funding と interest following unmet expectations. A resurgence で その 1980s came と expert システム — rule-based programs that encoded human expertise. その 2000s brought 機械学習 breakthroughs fuelled by その internet と growing datasets. その 2010s saw その rise の 深層学習, transforming computer vision, natural 言語 processing (NLP), と reinforcement learning.

## 機械学習

機械学習 (ML) is a subset の AI that enables システム to learn from データ without being explicitly programmed. Key ML categories include:

**Supervised Learning**: その model is trained on labelled input-output pairs. 例 include spam detection と image classification. Algorithms include linear regression, decision trees, サポート vector machines, と ニューラルネットワーク.

**Unsupervised Learning**: その model finds patterns で unlabelled データ. 例 include customer segmentation と anomaly detection. Algorithms include k-means clustering と principal component analysis (PCA).

**Reinforcement Learning**: An agent learns by interacting と an environment, receiving rewards or penalties. Used で game-playing AI (AlphaGo, AlphaZero), robotics, と recommendation システム.

**Semi-Supervised と Self-Supervised Learning**: Combine small amounts の labelled データ と large unlabelled datasets. GPT models use a self-supervised approach during pre-training.

## 深層学習

深層学習 is a subset の 機械学習 that uses artificial ニューラルネットワーク と many layers (deep networks). Inspired loosely by その brain's neural structure, these networks learn hierarchical representations の データ. 深層学習 powers:

- **Computer Vision**: Image recognition, object detection, medical imaging
- **Natural 言語 Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key 深層学習 architectures include convolutional ニューラルネットワーク (CNNs) のために images, recurrent ニューラルネットワーク (RNNs) と LSTMs のために sequences, transformers のために 言語, と generative adversarial networks (GANs) のために synthesis.

## Large 言語 Models (LLMs)

Large 言語 Models (LLMs) are AI システム trained on vast amounts の text データ to understand と generate human 言語. They are based on その Transformer アーキテクチャ, introduced で その 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict その next token (word piece) で a sequence, allowing them to generate coherent text, answer questions, write code, と perform reasoning tasks.

Notable LLMs include:
- **GPT series** (OpenAI): GPT-3, GPT-4, と successors — widely used のために chat と code
- **Claude** (Anthropic): Focused on safety と helpfulness
- **Gemini** (Google DeepMind): Multimodal, integrating text, images, と code
- **LLaMA / Llama 3** (Meta): Open-weight models のために research と local デプロイ
- **Mistral** (Mistral AI): Efficient open models competitive と much larger LLMs

LLMs are trained で two stages: pre-training (unsupervised on large text corpora) と fine-tuning (supervised or via reinforcement learning from human フィードバック, RLHF). Context windows describe how much text an LLM can process at once, ranging from 4K tokens (early GPT-3) to over 1 million tokens で その most 上級 2024 models.

## AI Ethics と Safety

AI raises important ethical questions including bias, privacy, job displacement, と その risk の misuse. Algorithmic bias occurs when training データ reflects historical inequalities, causing AI システム to produce discriminatory outputs. Facial recognition システム have shown higher error rates のために darker-skinned individuals. Hiring algorithms have been found to favour male candidates.

AI safety is その field dedicated to ensuring AI システム behave as intended without causing unintended harm. Key concerns include:
- **Alignment**: Ensuring AI goals match human values
- **Interpretability / Explainability**: Understanding why an AI made a decision (critical で 医学, 法律, 金融)
- **Misuse**: AI-generated deepfakes, disinformation, cyberattacks
- **Existential risk**: Theoretical concern that a 未来 AGI could pursue goals misaligned と human survival

Organisations working on AI safety include OpenAI's Safety team, Anthropic (founded by former OpenAI safety researchers), DeepMind's safety team, と independent institutes like MIRI と ARC.

## AI で Society

AI is transforming nearly every industry:

- **医療**: AI assists で diagnosing cancer from medical images, predicting patient outcomes, accelerating drug discovery (AlphaFold solved protein folding structure prediction), と personalising treatment plans.
- **金融**: Fraud detection, algorithmic trading, credit scoring, と robo-advisors use ML models.
- **Transportation**: Self-driving vehicles use computer vision, lidar, と reinforcement learning. Tesla Autopilot, Waymo, と Cruise are leading efforts.
- **Education**: Personalised learning platforms adapt content to individual student pace と learning style.
- **Creative fields**: AI generates music, art, と writing; tools like Midjourney, DALL-E, と GitHub Copilot have changed creative workflows.
- **Cybersecurity**: AI detects anomalies, identifies threats, と powers both attacks と defences.

## Robotics と Embodied AI

Robotics combines AI と physical machines. Modern robots use perception (cameras, lidar), planning, と control to navigate と manipulate environments. Boston Dynamics' Atlas demonstrates 上級 bipedal movement. Industrial robots from companies like ABB と FANUC automate manufacturing. Household robots (Roomba) と surgical robots (da Vinci System) apply AI で everyday と medical settings. Embodied AI research focuses on agents that learn physical skills through interaction と その world, bridging その gap between simulated と real environments.

## Current AI Trends (2020s)

- **Multimodal AI**: システム that process text, images, audio, と video together (GPT-4V, Gemini)
- **Agents と agentic AI**: LLMs that can use tools, browse その ウェブ, write code, と take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models のために researchers
- **On-device AI**: Running AI models locally on phones と laptops without cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: その EU AI Act (2024) is その world's first comprehensive AI 法律, classifying AI システム by risk level
