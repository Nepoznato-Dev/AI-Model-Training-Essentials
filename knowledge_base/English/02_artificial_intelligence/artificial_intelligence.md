# Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) refers to the simulation of human intelligence in machines programmed to think, learn, and solve problems. AI systems can perform tasks that typically require human intelligence, such as recognising speech, making decisions, translating languages, and identifying objects in images. The term was coined by John McCarthy in 1956 at the Dartmouth Conference, widely regarded as the founding event of AI as a field.

Modern AI is broadly divided into Narrow AI (also called Weak AI), which is designed for specific tasks, and the theoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domains. All current AI systems are Narrow AI.

## History of AI

The history of AI spans nearly eight decades. Early theoretical foundations were laid by Alan Turing, whose 1950 paper "Computing Machinery and Intelligence" introduced the Turing Test — a measure of a machine's ability to exhibit intelligent behaviour indistinguishable from a human. The 1956 Dartmouth Conference formally established AI as an academic discipline.

The 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) and LISP (a programming language designed for AI). The "AI winters" of the 1970s and 1980s were periods of reduced funding and interest following unmet expectations. A resurgence in the 1980s came with expert systems — rule-based programs that encoded human expertise. The 2000s brought machine learning breakthroughs fuelled by the internet and growing datasets. The 2010s saw the rise of deep learning, transforming computer vision, natural language processing (NLP), and reinforcement learning.

## Machine Learning

Machine Learning (ML) is a subset of AI that enables systems to learn from data without being explicitly programmed. Key ML categories include:

**Supervised Learning**: The model is trained on labelled input-output pairs. Examples include spam detection and image classification. Algorithms include linear regression, decision trees, support vector machines, and neural networks.

**Unsupervised Learning**: The model finds patterns in unlabelled data. Examples include customer segmentation and anomaly detection. Algorithms include k-means clustering and principal component analysis (PCA).

**Reinforcement Learning**: An agent learns by interacting with an environment, receiving rewards or penalties. Used in game-playing AI (AlphaGo, AlphaZero), robotics, and recommendation systems.

**Semi-Supervised and Self-Supervised Learning**: Combine small amounts of labelled data with large unlabelled datasets. GPT models use a self-supervised approach during pre-training.

## Deep Learning

Deep Learning is a subset of machine learning that uses artificial neural networks with many layers (deep networks). Inspired loosely by the brain's neural structure, these networks learn hierarchical representations of data. Deep learning powers:

- **Computer Vision**: Image recognition, object detection, medical imaging
- **Natural Language Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key deep learning architectures include convolutional neural networks (CNNs) for images, recurrent neural networks (RNNs) and LSTMs for sequences, transformers for language, and generative adversarial networks (GANs) for synthesis.

## Large Language Models (LLMs)

Large Language Models (LLMs) are AI systems trained on vast amounts of text data to understand and generate human language. They are based on the Transformer architecture, introduced in the 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict the next token (word piece) in a sequence, allowing them to generate coherent text, answer questions, write code, and perform reasoning tasks.

Notable LLMs include:
- **GPT series** (OpenAI): GPT-3, GPT-4, and successors — widely used for chat and code
- **Claude** (Anthropic): Focused on safety and helpfulness
- **Gemini** (Google DeepMind): Multimodal, integrating text, images, and code
- **LLaMA / Llama 3** (Meta): Open-weight models for research and local deployment
- **Mistral** (Mistral AI): Efficient open models competitive with much larger LLMs

LLMs are trained in two stages: pre-training (unsupervised on large text corpora) and fine-tuning (supervised or via reinforcement learning from human feedback, RLHF). Context windows describe how much text an LLM can process at once, ranging from 4K tokens (early GPT-3) to over 1 million tokens in the most advanced 2026 models.

## AI Ethics and Safety

AI raises important ethical questions including bias, privacy, job displacement, and the risk of misuse. Algorithmic bias occurs when training data reflects historical inequalities, causing AI systems to produce discriminatory outputs. Facial recognition systems have shown higher error rates for darker-skinned individuals. Hiring algorithms have been found to favour male candidates.

AI safety is the field dedicated to ensuring AI systems behave as intended without causing unintended harm. Key concerns include:
- **Alignment**: Ensuring AI goals match human values
- **Interpretability / Explainability**: Understanding why an AI made a decision (critical in medicine, law, finance)
- **Misuse**: AI-generated deepfakes, disinformation, cyberattacks
- **Existential risk**: Theoretical concern that a future AGI could pursue goals misaligned with human survival

Organisations working on AI safety include OpenAI's Safety team, Anthropic (founded by former OpenAI safety researchers), DeepMind's safety team, and independent institutes like MIRI and ARC.

## AI in Society

AI is transforming nearly every industry:

- **Healthcare**: AI assists in diagnosing cancer from medical images, predicting patient outcomes, accelerating drug discovery (AlphaFold solved protein folding structure prediction), and personalising treatment plans.
- **Finance**: Fraud detection, algorithmic trading, credit scoring, and robo-advisors use ML models.
- **Transportation**: Self-driving vehicles use computer vision, lidar, and reinforcement learning. Tesla Autopilot, Waymo, and Cruise are leading efforts.
- **Education**: Personalised learning platforms adapt content to individual student pace and learning style.
- **Creative fields**: AI generates music, art, and writing; tools like Midjourney, DALL-E, and GitHub Copilot have changed creative workflows.
- **Cybersecurity**: AI detects anomalies, identifies threats, and powers both attacks and defences.

## Robotics and Embodied AI

Robotics combines AI with physical machines. Modern robots use perception (cameras, lidar), planning, and control to navigate and manipulate environments. Boston Dynamics' Atlas demonstrates advanced bipedal movement. Industrial robots from companies like ABB and FANUC automate manufacturing. Household robots (Roomba) and surgical robots (da Vinci System) apply AI in everyday and medical settings. Embodied AI research focuses on agents that learn physical skills through interaction with the world, bridging the gap between simulated and real environments.

## Current AI Trends (2020s)

- **Multimodal AI**: Systems that process text, images, audio, and video together (GPT-4V, Gemini)
- **Agents and agentic AI**: LLMs that can use tools, browse the web, write code, and take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models for researchers
- **On-device AI**: Running AI models locally on phones and laptops without cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: The EU AI Act (2026) is the world's first comprehensive AI law, classifying AI systems by risk level
