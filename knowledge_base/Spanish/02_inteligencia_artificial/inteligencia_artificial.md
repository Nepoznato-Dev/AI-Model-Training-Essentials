<!-- 
This file was automatically translated from English to Spanish.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) refers to el simulation de human intelligence en machines programmed to think, learn, y solve problems. AI Sistemas can perform tasks that typically require human intelligence, such as recognising speech, making decisions, translating languages, y identifying objects en images. el term was coined by John McCarthy en 1956 at el Dartmouth Conference, widely regarded as el founding event de AI as a field.

Modern AI is broadly divided into Narrow AI (also llamado Weak AI), which is designed para specific tasks, y el theoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domains. All current AI Sistemas are Narrow AI.

## Historia de AI

el Historia de AI spans nearly eight decades. Early theoretical foundations were laid by Alan Turing, whose 1950 paper "Informática Machinery y Intelligence" introduced el Turing Test — a measure de a machine's ability to exhibit intelligent behaviour indistinguishable from a human. el 1956 Dartmouth Conference formally established AI as an academic discipline.

el 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) y LISP (a programming Idioma designed para AI). el "AI winters" del 1970s y 1980s were periods de reduced funding y interest following unmet expectations. A resurgence en el 1980s came con expert Sistemas — rule-based programs that encoded human expertise. el 2000s brought Aprendizaje automático breakthroughs fuelled by el internet y growing datasets. el 2010s saw el surgimiento del Aprendizaje profundo, transforming computer vision, natural Idioma processing (NLP), y reinforcement learning.

## Aprendizaje automático

Aprendizaje automático (ML) is a subset de AI that enables Sistemas to learn from Datos without being explicitly programmed. Key ML categories incluyen:

**Supervised Learning**: el model is trained on labelled input-output pairs. Ejemplos incluyen spam detection y image classification. Algorithms incluyen linear regression, decision trees, Soporte vector machines, y Redes neuronales.

**Unsupervised Learning**: el model finds patterns en unlabelled Datos. Ejemplos incluyen customer segmentation y anomaly detection. Algorithms incluyen k-means clustering y principal component analysis (PCA).

**Reinforcement Learning**: An agent learns by interacting con an environment, receiving rewards or penalties. Used en game-playing AI (AlphaGo, AlphaZero), robotics, y recommendation Sistemas.

**Semi-Supervised y Self-Supervised Learning**: Combine small amounts de labelled Datos con large unlabelled datasets. GPT models use a self-supervised approach during pre-training.

## Aprendizaje profundo

Aprendizaje profundo is a subset de Aprendizaje automático that uses artificial Redes neuronales con many layers (deep networks). Inspired loosely by el brain's neural structure, these networks learn hierarchical representations de Datos. Aprendizaje profundo powers:

- **Computer Vision**: Image recognition, object detection, medical imaging
- **Natural Idioma Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key Aprendizaje profundo architectures incluyen convolutional Redes neuronales (CNNs) para images, recurrent Redes neuronales (RNNs) y LSTMs para sequences, transformers para Idioma, y generative adversarial networks (GANs) para synthesis.

## Large Idioma Models (LLMs)

Large Idioma Models (LLMs) are AI Sistemas trained on vast amounts de text Datos to understand y generate human Idioma. They are based on el Transformer Arquitectura, introduced en el 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict el next token (word piece) en a sequence, allowing them to generate coherent text, answer questions, write code, y perform razóning tasks.

Notable LLMs incluyen:
- **GPT series** (OpenAI): GPT-3, GPT-4, y successors — widely used para chat y code
- **Claude** (Anthropic): Focused on safety y helpfulness
- **Gemini** (Google DeepMind): Multimodal, integrating text, images, y code
- **LLaMA / Llama 3** (Meta): Open-weight models para research y local Implementación
- **Mistral** (Mistral AI): Efficient open models competitive con much larger LLMs

LLMs are trained en two stages: pre-training (unsupervised on large text corpora) y fine-tuning (supervised or via reinforcement learning from human Comentarios, RLHF). Context windows describe how much text an LLM can process at once, ranging from 4K tokens (early GPT-3) to over 1 million tokens en el most Avanzado 2026 models.

## AI Ethics y Safety

AI raises important ethical questions including bias, privacy, job displacement, y el risk de misuse. Algorithmic bias occurs when training Datos reflects historical inequalities, causing AI Sistemas to produce discriminatory outputs. Facial recognition Sistemas have shown higher error rates para darker-skinned individuals. Hiring algorithms have been found to favour male candidates.

AI safety is el field dedicated to ensuring AI Sistemas behave as intended without causing unintended harm. Key concerns incluyen:
- **Alignment**: Ensuring AI goals match human values
- **Interpretability / Explainability**: Understanding why an AI made a decision (critical en Medicina, Derecho, Finanzas)
- **Misuse**: AI-generated deepfakes, disinformation, cyberattacks
- **Existential risk**: Theoretical concern that a Futuro AGI could pursue goals misaligned con human survival

Organisations working on AI safety incluyen OpenAI's Safety team, Anthropic (founded by former OpenAI safety researchers), DeepMind's safety team, y independent institutes like MIRI y ARC.

## AI en Society

AI is transforming nearly every industry:

- **Atención médica**: AI assists en diagnosing cancer from medical images, predicting patient outcomes, accelerating drug discovery (AlphaFold solved protein folding structure prediction), y personalising treatment plans.
- **Finanzas**: Fraud detection, algorithmic trading, credit scoring, y robo-advisors use ML models.
- **Transportation**: Self-driving vehicles use computer vision, lidar, y reinforcement learning. Tesla Autopilot, Waymo, y Cruise are leading efforts.
- **Education**: Personalised learning platforms adapt content to individual student pace y learning style.
- **Creative fields**: AI generates music, art, y writing; tools like Midjourney, DALL-E, y GitHub Copilot have changed creative workflows.
- **Cybersecurity**: AI detects anomalies, identifies threats, y powers both attacks y defences.

## Robotics y Embodied AI

Robotics combines AI con physical machines. Modern robots use perception (cameras, lidar), planning, y control to navigate y manipulate environments. Boston Dynamics' Atlas demonstrates Avanzado bipedal movement. Industrial robots from companies like ABB y FANUC automate manufacturing. Household robots (Roomba) y surgical robots (da Vinci System) apply AI en everyday y medical settings. Embodied AI research se centra en agents that learn physical skills through interaction con el world, bridging el gap between simulated y real environments.

## Current AI Trends (2020s)

- **Multimodal AI**: Sistemas that process text, images, audio, y video together (GPT-4V, Gemini)
- **Agents y agentic AI**: LLMs that can use tools, browse el Web, write code, y take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models para researchers
- **On-device AI**: Running AI models locally on phones y laptops without cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: el EU AI Act (2026) is el world's first comprehensive AI Derecho, classifying AI Sistemas by risk level
