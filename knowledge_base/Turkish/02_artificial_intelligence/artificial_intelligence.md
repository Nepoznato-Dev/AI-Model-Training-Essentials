<!-- 
This file was automatically translated from English to Turkish.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) refers to bu simulation içinde human intelligence içinde machines programmed to think, learn, ve solve problems. AI Sistemler can perform tasks that typically require human intelligence, such as recognising speech, making decisions, translating languages, ve identifying objects içinde images. bu term was coined by John McCarthy içinde 1956 at bu Dartmouth Conference, widely regarded as bu founding event içinde AI as a field.

Modern AI is broadly divided into Narrow AI (also called Weak AI), which is designed için specific tasks, ve bu theoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domains. All current AI Sistemler are Narrow AI.

## Tarih içinde AI

bu Tarih içinde AI spans nearly eight decades. Early theoretical foundations were laid by Alan Turing, whose 1950 paper "Bilişim Machinery ve Intelligence" introduced bu Turing Test — a measure içinde a machine's ability to exhibit intelligent behaviour indistinguishable from a human. bu 1956 Dartmouth Conference formally established AI as an academic discipline.

bu 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) ve LISP (a programming Dil designed için AI). bu "AI winters" içinde bu 1970s ve 1980s were periods içinde reduced funding ve interest following unmet expectations. A resurgence içinde bu 1980s came ile expert Sistemler — rule-based programs that encoded human expertise. bu 2000s brought Makine Öğrenimi breakthroughs fuelled by bu internet ve growing datasets. bu 2010s saw bu rise içinde Derin Öğrenme, transforming computer vision, natural Dil processing (NLP), ve reinforcement learning.

## Makine Öğrenimi

Makine Öğrenimi (ML) is a subset içinde AI that enables Sistemler to learn from Veri without being explicitly programmed. Key ML categories include:

**Supervised Learning**: bu model is trained on labelled input-output pairs. Örnekler include spam detection ve image classification. Algorithms include linear regression, decision trees, Destek vector machines, ve Sinir Ağları.

**Unsupervised Learning**: bu model finds patterns içinde unlabelled Veri. Örnekler include customer segmentation ve anomaly detection. Algorithms include k-means clustering ve principal component analysis (PCA).

**Reinforcement Learning**: An agent learns by interacting ile an environment, receiving rewards or penalties. Used içinde game-playing AI (AlphaGo, AlphaZero), robotics, ve recommendation Sistemler.

**Semi-Supervised ve Self-Supervised Learning**: Combine small amounts içinde labelled Veri ile large unlabelled datasets. GPT models use a self-supervised approach during pre-training.

## Derin Öğrenme

Derin Öğrenme is a subset içinde Makine Öğrenimi that uses artificial Sinir Ağları ile many layers (deep networks). Inspired loosely by bu brain's neural structure, these networks learn hierarchical representations içinde Veri. Derin Öğrenme powers:

- **Computer Vision**: Image recognition, object detection, medical imaging
- **Natural Dil Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key Derin Öğrenme architectures include convolutional Sinir Ağları (CNNs) için images, recurrent Sinir Ağları (RNNs) ve LSTMs için sequences, transformers için Dil, ve generative adversarial networks (GANs) için synthesis.

## Large Dil Models (LLMs)

Large Dil Models (LLMs) are AI Sistemler trained on vast amounts içinde text Veri to understand ve generate human Dil. They are based on bu Transformer Mimari, introduced içinde bu 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict bu next token (word piece) içinde a sequence, allowing them to generate coherent text, answer questions, write code, ve perform reasoning tasks.

Notable LLMs include:
- **GPT series** (OpenAI): GPT-3, GPT-4, ve successors — widely used için chat ve code
- **Claude** (Anthropic): Focused on safety ve helpfulness
- **Gemini** (Google DeepMind): Multimodal, integrating text, images, ve code
- **LLaMA / Llama 3** (Meta): Open-weight models için research ve local Dağıtım
- **Mistral** (Mistral AI): Efficient open models competitive ile much larger LLMs

LLMs are trained içinde two stages: pre-training (unsupervised on large text corpora) ve fine-tuning (supervised or via reinforcement learning from human Geri Bildirim, RLHF). Context windows describe how much text an LLM can process at once, ranging from 4K tokens (early GPT-3) to over 1 million tokens içinde bu most İleri Düzey 2024 models.

## AI Ethics ve Safety

AI raises important ethical questions including bias, privacy, job displacement, ve bu risk içinde misuse. Algorithmic bias occurs when training Veri reflects historical inequalities, causing AI Sistemler to produce discriminatory outputs. Facial recognition Sistemler have shown higher error rates için darker-skinned individuals. Hiring algorithms have been found to favour male candidates.

AI safety is bu field dedicated to ensuring AI Sistemler behave as intended without causing unintended harm. Key concerns include:
- **Alignment**: Ensuring AI goals match human values
- **Interpretability / Explainability**: Understanding why an AI made a decision (critical içinde Tıp, Hukuk, Finans)
- **Misuse**: AI-generated deepfakes, disinformation, cyberattacks
- **Existential risk**: Theoretical concern that a Gelecek AGI could pursue goals misaligned ile human survival

Organisations working on AI safety include OpenAI's Safety team, Anthropic (founded by former OpenAI safety researchers), DeepMind's safety team, ve independent institutes like MIRI ve ARC.

## AI içinde Society

AI is transforming nearly every industry:

- **Sağlık Hizmetleri**: AI assists içinde diagnosing cancer from medical images, predicting patient outcomes, accelerating drug discovery (AlphaFold solved protein folding structure prediction), ve personalising treatment plans.
- **Finans**: Fraud detection, algorithmic trading, credit scoring, ve robo-advisors use ML models.
- **Transportation**: Self-driving vehicles use computer vision, lidar, ve reinforcement learning. Tesla Autopilot, Waymo, ve Cruise are leading efforts.
- **Education**: Personalised learning platforms adapt content to individual student pace ve learning style.
- **Creative fields**: AI generates music, art, ve writing; tools like Midjourney, DALL-E, ve GitHub Copilot have changed creative workflows.
- **Cybersecurity**: AI detects anomalies, identifies threats, ve powers both attacks ve defences.

## Robotics ve Embodied AI

Robotics combines AI ile physical machines. Modern robots use perception (cameras, lidar), planning, ve control to navigate ve manipulate environments. Boston Dynamics' Atlas demonstrates İleri Düzey bipedal movement. Industrial robots from companies like ABB ve FANUC automate manufacturing. Household robots (Roomba) ve surgical robots (da Vinci System) apply AI içinde everyday ve medical settings. Embodied AI research focuses on agents that learn physical skills through interaction ile bu world, bridging bu gap between simulated ve real environments.

## Current AI Trends (2020s)

- **Multimodal AI**: Sistemler that process text, images, audio, ve video together (GPT-4V, Gemini)
- **Agents ve agentic AI**: LLMs that can use tools, browse bu Web, write code, ve take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models için researchers
- **On-device AI**: Running AI models locally on phones ve laptops without cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: bu EU AI Act (2024) is bu world's first comprehensive AI Hukuk, classifying AI Sistemler by risk level
