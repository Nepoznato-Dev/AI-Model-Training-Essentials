<!-- 
This file was automatically translated from English to Russian.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) refers to the simulation из human intelligence в machines programmed to think, learn, и solve problems. AI Системы can perform tasks that typically require human intelligence, such as recognising speech, making decisions, translating languages, и identifying objects в images. the term was coined by John McCarthy в 1956 at the Dartmouth Conference, widely regarded as the founding event из AI as a field.

Modern AI is broadly divided into Narrow AI (also called Weak AI), which is designed для specific tasks, и the theoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domains. All current AI Системы are Narrow AI.

## История из AI

the История из AI spans nearly eight decades. Early theoretical foundations were laid by Alan Turing, whose 1950 paper "Вычисления Machinery и Intelligence" introduced the Turing Test — a measure из a machine's ability to exhibit intelligent behaviour indistinguishable from a human. the 1956 Dartmouth Conference formally established AI as an academic discipline.

the 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) и LISP (a programming Язык designed для AI). the "AI winters" из the 1970s и 1980s were periods из reduced funding и interest following unmet expectations. A resurgence в the 1980s came с expert Системы — rule-based programs that encoded human expertise. the 2000s brought Машинное обучение breakthroughs fuelled by the internet и growing datasets. the 2010s saw the rise из Глубокое обучение, transforming computer vision, natural Язык processing (NLP), и reinforcement learning.

## Машинное обучение

Машинное обучение (ML) is a subset из AI that enables Системы to learn from Данные without being explicitly programmed. Key ML categories include:

**Supervised Learning**: the model is trained on labelled input-output pairs. Примеры include spam detection и image classification. Algorithms include linear regression, decision trees, Поддержка vector machines, и Нейронные сети.

**Unsupervised Learning**: the model finds patterns в unlabelled Данные. Примеры include customer segmentation и anomaly detection. Algorithms include k-means clustering и principal component analysis (PCA).

**Reinforcement Learning**: An agent learns by interacting с an environment, receiving rewards or penalties. Used в game-playing AI (AlphaGo, AlphaZero), robotics, и recommendation Системы.

**Semi-Supervised и Self-Supervised Learning**: Combine small amounts из labelled Данные с large unlabelled datasets. GPT models use a self-supervised approach during pre-training.

## Глубокое обучение

Глубокое обучение is a subset из Машинное обучение that uses artificial Нейронные сети с many layers (deep networks). Inspired loosely by the brain's neural structure, these networks learn hierarchical representations из Данные. Глубокое обучение powers:

- **Computer Vision**: Image recognition, object detection, medical imaging
- **Natural Язык Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key Глубокое обучение architectures include convolutional Нейронные сети (CNNs) для images, recurrent Нейронные сети (RNNs) и LSTMs для sequences, transformers для Язык, и generative adversarial networks (GANs) для synthesis.

## Large Язык Models (LLMs)

Large Язык Models (LLMs) are AI Системы trained on vast amounts из text Данные to understand и generate human Язык. They are based on the Transformer Архитектура, introduced в the 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict the next token (word piece) в a sequence, allowing them to generate coherent text, answer questions, write code, и perform reasoning tasks.

Notable LLMs include:
- **GPT series** (OpenAI): GPT-3, GPT-4, и successors — widely used для chat и code
- **Claude** (Anthropic): Focused on safety и helpfulness
- **Gemini** (Google DeepMind): Multimodal, integrating text, images, и code
- **LLaMA / Llama 3** (Meta): Open-weight models для research и local Развертывание
- **Mistral** (Mistral AI): Efficient open models competitive с much larger LLMs

LLMs are trained в two stages: pre-training (unsupervised on large text corpora) и fine-tuning (supervised or via reinforcement learning from human Обратная связь, RLHF). Context windows describe how much text an LLM can process at once, ranging from 4K tokens (early GPT-3) to over 1 million tokens в the most Продвинутый 2024 models.

## AI Ethics и Safety

AI raises important ethical questions including bias, privacy, job displacement, и the risk из misuse. Algorithmic bias occurs when training Данные reflects historical inequalities, causing AI Системы to produce discriminatory outputs. Facial recognition Системы have shown higher error rates для darker-skinned individuals. Hiring algorithms have been found to favour male candidates.

AI safety is the field dedicated to ensuring AI Системы behave as intended without causing unintended harm. Key concerns include:
- **Alignment**: Ensuring AI goals match human values
- **Interpretability / Explainability**: Understanding why an AI made a decision (critical в Медицина, Закон, Финансы)
- **Misuse**: AI-generated deepfakes, disinformation, cyberattacks
- **Existential risk**: Theoretical concern that a Будущее AGI could pursue goals misaligned с human survival

Organisations working on AI safety include OpenAI's Safety team, Anthropic (founded by former OpenAI safety researchers), DeepMind's safety team, и independent institutes like MIRI и ARC.

## AI в Society

AI is transforming nearly every industry:

- **Здравоохранение**: AI assists в diagnosing cancer from medical images, predicting patient outcomes, accelerating drug discovery (AlphaFold solved protein folding structure prediction), и personalising treatment plans.
- **Финансы**: Fraud detection, algorithmic trading, credit scoring, и robo-advisors use ML models.
- **Transportation**: Self-driving vehicles use computer vision, lidar, и reinforcement learning. Tesla Autopilot, Waymo, и Cruise are leading efforts.
- **Education**: Personalised learning platforms adapt content to individual student pace и learning style.
- **Creative fields**: AI generates music, art, и writing; tools like Midjourney, DALL-E, и GitHub Copilot have changed creative workflows.
- **Cybersecurity**: AI detects anomalies, identifies threats, и powers both attacks и defences.

## Robotics и Embodied AI

Robotics combines AI с physical machines. Modern robots use perception (cameras, lidar), planning, и control to navigate и manipulate environments. Boston Dynamics' Atlas demonstrates Продвинутый bipedal movement. Industrial robots from companies like ABB и FANUC automate manufacturing. Household robots (Roomba) и surgical robots (da Vinci System) apply AI в everyday и medical settings. Embodied AI research focuses on agents that learn physical skills through interaction с the world, bridging the gap between simulated и real environments.

## Current AI Trends (2020s)

- **Multimodal AI**: Системы that process text, images, audio, и video together (GPT-4V, Gemini)
- **Agents и agentic AI**: LLMs that can use tools, browse the Веб, write code, и take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models для researchers
- **On-device AI**: Running AI models locally on phones и laptops without cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: the EU AI Act (2024) is the world's first comprehensive AI Закон, classifying AI Системы by risk level
