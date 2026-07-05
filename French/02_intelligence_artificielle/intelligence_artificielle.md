<!-- 
This file was automatically translated from English to French.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) refers to le/la simulation de human intelligence dans machines programmed to think, learn, et solve problems. AI Systèmes can perform tasks that typically require human intelligence, such as recognising speech, making decisions, translating languages, et identifying objects dans images. le/la term was coined by John McCarthy dans 1956 at le/la Dartmouth Conference, widely regarded as le/la founding event de AI as a field.

Modern AI is broadly divided into Narrow AI (also called Weak AI), which is designed pour specific tasks, et le/la theoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domains. All current AI Systèmes are Narrow AI.

## Histoire de AI

le/la Histoire de AI spans nearly eight decades. Early theoretical foundations were laid by Alan Turing, whose 1950 paper "Informatique Machinery et Intelligence" introduced le/la Turing Test — a measure de a machine's ability to exhibit intelligent behaviour indistinguishable from a human. le/la 1956 Dartmouth Conference formally established AI as an academic discipline.

le/la 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) et LISP (a programming Langue designed pour AI). le/la "AI winters" de le/la 1970s et 1980s were periods de reduced funding et interest following unmet expectations. A resurgence dans le/la 1980s came avec expert Systèmes — rule-based programs that encoded human expertise. le/la 2000s brought Apprentissage automatique breakthroughs fuelled by le/la internet et growing datasets. le/la 2010s saw le/la rise de Apprentissage profond, transforming computer vision, natural Langue processing (NLP), et reinforcement learning.

## Apprentissage automatique

Apprentissage automatique (ML) is a subset de AI that enables Systèmes to learn from Données without being explicitly programmed. Key ML categories include:

**Supervised Learning**: le/la model is trained on labelled input-output pairs. Exemples include spam detection et image classification. Algorithms include linear regression, decision trees, Assistance vector machines, et Réseaux de neurones.

**Unsupervised Learning**: le/la model finds patterns dans unlabelled Données. Exemples include customer segmentation et anomaly detection. Algorithms include k-means clustering et principal component analysis (PCA).

**Reinforcement Learning**: An agent learns by interacting avec an environment, receiving rewards or penalties. Used dans game-playing AI (AlphaGo, AlphaZero), robotics, et recommendation Systèmes.

**Semi-Supervised et Self-Supervised Learning**: Combine small amounts de labelled Données avec large unlabelled datasets. GPT models use a self-supervised approach during pre-training.

## Apprentissage profond

Apprentissage profond is a subset de Apprentissage automatique that uses artificial Réseaux de neurones avec many layers (deep networks). Inspired loosely by le/la brain's neural structure, these networks learn hierarchical representations de Données. Apprentissage profond powers:

- **Computer Vision**: Image recognition, object detection, medical imaging
- **Natural Langue Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key Apprentissage profond architectures include convolutional Réseaux de neurones (CNNs) pour images, recurrent Réseaux de neurones (RNNs) et LSTMs pour sequences, transformers pour Langue, et generative adversarial networks (GANs) pour synthesis.

## Large Langue Models (LLMs)

Large Langue Models (LLMs) are AI Systèmes trained on vast amounts de text Données to understand et generate human Langue. They are based on le/la Transformer Architecture, introduced dans le/la 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict le/la next token (word piece) dans a sequence, allowing them to generate coherent text, answer questions, write code, et perform reasoning tasks.

Notable LLMs include:
- **GPT series** (OpenAI): GPT-3, GPT-4, et successors — widely used pour chat et code
- **Claude** (Anthropic): Focused on safety et helpfulness
- **Gemini** (Google DeepMind): Multimodal, integrating text, images, et code
- **LLaMA / Llama 3** (Meta): Open-weight models pour research et local Déploiement
- **Mistral** (Mistral AI): Efficient open models competitive avec much larger LLMs

LLMs are trained dans two stages: pre-training (unsupervised on large text corpora) et fine-tuning (supervised or via reinforcement learning from human Retour, RLHF). Context windows describe how much text an LLM can process at once, ranging from 4K tokens (early GPT-3) to over 1 million tokens dans le/la most Avancé 2024 models.

## AI Ethics et Safety

AI raises important ethical questions including bias, privacy, job displacement, et le/la risk de misuse. Algorithmic bias occurs when training Données reflects historical inequalities, causing AI Systèmes to produce discriminatory outputs. Facial recognition Systèmes have shown higher error rates pour darker-skinned individuals. Hiring algorithms have been found to favour male candidates.

AI safety is le/la field dedicated to ensuring AI Systèmes behave as intended without causing unintended harm. Key concerns include:
- **Alignment**: Ensuring AI goals match human values
- **Interpretability / Explainability**: Understanding why an AI made a decision (critical dans Médecine, Droit, Finance)
- **Misuse**: AI-generated deepfakes, disinformation, cyberattacks
- **Existential risk**: Theoretical concern that a Futur AGI could pursue goals misaligned avec human survival

Organisations working on AI safety include OpenAI's Safety team, Anthropic (founded by former OpenAI safety researchers), DeepMind's safety team, et independent institutes like MIRI et ARC.

## AI dans Society

AI is transforming nearly every industry:

- **Soins de santé**: AI assists dans diagnosing cancer from medical images, predicting patient outcomes, accelerating drug discovery (AlphaFold solved protein folding structure prediction), et personalising treatment plans.
- **Finance**: Fraud detection, algorithmic trading, credit scoring, et robo-advisors use ML models.
- **Transportation**: Self-driving vehicles use computer vision, lidar, et reinforcement learning. Tesla Autopilot, Waymo, et Cruise are leading efforts.
- **Education**: Personalised learning platforms adapt content to individual student pace et learning style.
- **Creative fields**: AI generates music, art, et writing; tools like Midjourney, DALL-E, et GitHub Copilot have changed creative workflows.
- **Cybersecurity**: AI detects anomalies, identifies threats, et powers both attacks et defences.

## Robotics et Embodied AI

Robotics combines AI avec physical machines. Modern robots use perception (cameras, lidar), planning, et control to navigate et manipulate environments. Boston Dynamics' Atlas demonstrates Avancé bipedal movement. Industrial robots from companies like ABB et FANUC automate manufacturing. Household robots (Roomba) et surgical robots (da Vinci System) apply AI dans everyday et medical settings. Embodied AI research focuses on agents that learn physical skills through interaction avec le/la world, bridging le/la gap between simulated et real environments.

## Current AI Trends (2020s)

- **Multimodal AI**: Systèmes that process text, images, audio, et video together (GPT-4V, Gemini)
- **Agents et agentic AI**: LLMs that can use tools, browse le/la Web, write code, et take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models pour researchers
- **On-device AI**: Running AI models locally on phones et laptops without cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: le/la EU AI Act (2024) is le/la world's first comprehensive AI Droit, classifying AI Systèmes by risk level
