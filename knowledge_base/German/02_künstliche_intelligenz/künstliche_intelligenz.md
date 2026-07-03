<!-- 
This file was automatically translated from English to German.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) refers to der/die/das simulation von human intelligence in machines programmed to think, learn, und solve problems. AI Systeme can perform tasks that typically require human intelligence, such as recognising speech, making decisions, translating languages, und identifying objects in images. der/die/das term was coined by John McCarthy in 1956 at der/die/das Dartmouth Conference, widely regarded as der/die/das founding event von AI as a field.

Modern AI is broadly divided into Narrow AI (also called Weak AI), which is designed für specific tasks, und der/die/das theoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domains. All current AI Systeme are Narrow AI.

## Geschichte von AI

der/die/das Geschichte von AI spans nearly eight decades. Early theoretical foundations were laid by Alan Turing, whose 1950 paper "Datenverarbeitung Machinery und Intelligence" introduced der/die/das Turing Test — a measure von a machine's ability to exhibit intelligent behaviour indistinguishable from a human. der/die/das 1956 Dartmouth Conference formally established AI as an academic discipline.

der/die/das 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) und LISP (a programming Sprache designed für AI). der/die/das "AI winters" von der/die/das 1970s und 1980s were periods von reduced funding und interest following unmet expectations. A resurgence in der/die/das 1980s came mit expert Systeme — rule-based programs that encoded human expertise. der/die/das 2000s brought Maschinelles Lernen breakthroughs fuelled by der/die/das internet und growing datasets. der/die/das 2010s saw der/die/das rise von Tiefes Lernen, transforming computer vision, natural Sprache processing (NLP), und reinforcement learning.

## Maschinelles Lernen

Maschinelles Lernen (ML) is a subset von AI that enables Systeme to learn from Daten without being explicitly programmed. Key ML categories include:

**Supervised Learning**: der/die/das model is trained on labelled input-output pairs. Beispiele include spam detection und image classification. Algorithms include linear regression, decision trees, Support vector machines, und Neuronale Netze.

**Unsupervised Learning**: der/die/das model finds patterns in unlabelled Daten. Beispiele include customer segmentation und anomaly detection. Algorithms include k-means clustering und principal component analysis (PCA).

**Reinforcement Learning**: An agent learns by interacting mit an environment, receiving rewards or penalties. Used in game-playing AI (AlphaGo, AlphaZero), robotics, und recommendation Systeme.

**Semi-Supervised und Self-Supervised Learning**: Combine small amounts von labelled Daten mit large unlabelled datasets. GPT models use a self-supervised approach during pre-training.

## Tiefes Lernen

Tiefes Lernen is a subset von Maschinelles Lernen that uses artificial Neuronale Netze mit many layers (deep networks). Inspired loosely by der/die/das brain's neural structure, these networks learn hierarchical representations von Daten. Tiefes Lernen powers:

- **Computer Vision**: Image recognition, object detection, medical imaging
- **Natural Sprache Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key Tiefes Lernen architectures include convolutional Neuronale Netze (CNNs) für images, recurrent Neuronale Netze (RNNs) und LSTMs für sequences, transformers für Sprache, und generative adversarial networks (GANs) für synthesis.

## Large Sprache Models (LLMs)

Large Sprache Models (LLMs) are AI Systeme trained on vast amounts von text Daten to understand und generate human Sprache. They are based on der/die/das Transformer Architektur, introduced in der/die/das 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict der/die/das next token (word piece) in a sequence, allowing them to generate coherent text, answer questions, write code, und perform reasoning tasks.

Notable LLMs include:
- **GPT series** (OpenAI): GPT-3, GPT-4, und successors — widely used für chat und code
- **Claude** (Anthropic): Focused on safety und helpfulness
- **Gemini** (Google DeepMind): Multimodal, integrating text, images, und code
- **LLaMA / Llama 3** (Meta): Open-weight models für research und local Bereitstellung
- **Mistral** (Mistral AI): Efficient open models competitive mit much larger LLMs

LLMs are trained in two stages: pre-training (unsupervised on large text corpora) und fine-tuning (supervised or via reinforcement learning from human Rückmeldung, RLHF). Context windows describe how much text an LLM can process at once, ranging from 4K tokens (early GPT-3) to over 1 million tokens in der/die/das most Fortgeschritten 2024 models.

## AI Ethics und Safety

AI raises important ethical questions including bias, privacy, job displacement, und der/die/das risk von misuse. Algorithmic bias occurs when training Daten reflects historical inequalities, causing AI Systeme to produce discriminatory outputs. Facial recognition Systeme have shown higher error rates für darker-skinned individuals. Hiring algorithms have been found to favour male candidates.

AI safety is der/die/das field dedicated to ensuring AI Systeme behave as intended without causing unintended harm. Key concerns include:
- **Alignment**: Ensuring AI goals match human values
- **Interpretability / Explainability**: Understanding why an AI made a decision (critical in Medizin, Recht, Finanzen)
- **Misuse**: AI-generated deepfakes, disinformation, cyberattacks
- **Existential risk**: Theoretical concern that a Zukunft AGI could pursue goals misaligned mit human survival

Organisations working on AI safety include OpenAI's Safety team, Anthropic (founded by former OpenAI safety researchers), DeepMind's safety team, und independent institutes like MIRI und ARC.

## AI in Society

AI is transforming nearly every industry:

- **Gesundheitswesen**: AI assists in diagnosing cancer from medical images, predicting patient outcomes, accelerating drug discovery (AlphaFold solved protein folding structure prediction), und personalising treatment plans.
- **Finanzen**: Fraud detection, algorithmic trading, credit scoring, und robo-advisors use ML models.
- **Transportation**: Self-driving vehicles use computer vision, lidar, und reinforcement learning. Tesla Autopilot, Waymo, und Cruise are leading efforts.
- **Education**: Personalised learning platforms adapt content to individual student pace und learning style.
- **Creative fields**: AI generates music, art, und writing; tools like Midjourney, DALL-E, und GitHub Copilot have changed creative workflows.
- **Cybersecurity**: AI detects anomalies, identifies threats, und powers both attacks und defences.

## Robotics und Embodied AI

Robotics combines AI mit physical machines. Modern robots use perception (cameras, lidar), planning, und control to navigate und manipulate environments. Boston Dynamics' Atlas demonstrates Fortgeschritten bipedal movement. Industrial robots from companies like ABB und FANUC automate manufacturing. Household robots (Roomba) und surgical robots (da Vinci System) apply AI in everyday und medical settings. Embodied AI research focuses on agents that learn physical skills through interaction mit der/die/das world, bridging der/die/das gap between simulated und real environments.

## Current AI Trends (2020s)

- **Multimodal AI**: Systeme that process text, images, audio, und video together (GPT-4V, Gemini)
- **Agents und agentic AI**: LLMs that can use tools, browse der/die/das Web, write code, und take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models für researchers
- **On-device AI**: Running AI models locally on phones und laptops without cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: der/die/das EU AI Act (2024) is der/die/das world's first comprehensive AI Recht, classifying AI Systeme by risk level
