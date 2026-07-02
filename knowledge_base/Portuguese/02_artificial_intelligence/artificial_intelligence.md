<!-- 
This file was automatically translated from English to Portuguese.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) refers to o/a simulation de human intelligence em machines programmed to think, learn, e solve problems. AI Sistemas can perform tasks that typically require human intelligence, such as recognising speech, making decisions, translating languages, e identifying objects em images. o/a term was coined by John McCarthy em 1956 at o/a Dartmouth Conference, widely regarded as o/a founding event de AI as a field.

Modern AI is broadly divided into Narrow AI (also called Weak AI), which is designed para specific tasks, e o/a theoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domains. All current AI Sistemas are Narrow AI.

## História de AI

o/a História de AI spans nearly eight decades. Early theoretical foundations were laid by Alan Turing, whose 1950 paper "Computação Machinery e Intelligence" introduced o/a Turing Test — a measure de a machine's ability to exhibit intelligent behaviour indistinguishable from a human. o/a 1956 Dartmouth Conference formally established AI as an academic discipline.

o/a 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) e LISP (a programming Idioma designed para AI). o/a "AI winters" de o/a 1970s e 1980s were periods de reduced funding e interest following unmet expectations. A resurgence em o/a 1980s came com expert Sistemas — rule-based programs that encoded human expertise. o/a 2000s brought Aprendizado de máquina breakthroughs fuelled by o/a internet e growing datasets. o/a 2010s saw o/a rise de Aprendizado profundo, transforming computer vision, natural Idioma processing (NLP), e reinforcement learning.

## Aprendizado de máquina

Aprendizado de máquina (ML) is a subset de AI that enables Sistemas to learn from Dados without being explicitly programmed. Key ML categories include:

**Supervised Learning**: o/a model is trained on labelled input-output pairs. Exemplos include spam detection e image classification. Algorithms include linear regression, decision trees, support vector machines, e Redes neurais.

**Unsupervised Learning**: o/a model finds patterns em unlabelled Dados. Exemplos include customer segmentation e anomaly detection. Algorithms include k-means clustering e principal component analysis (PCA).

**Reinforcement Learning**: An agent learns by interacting com an environment, receiving rewards or penalties. Used em game-playing AI (AlphaGo, AlphaZero), robotics, e recommendation Sistemas.

**Semi-Supervised e Self-Supervised Learning**: Combine small amounts de labelled Dados com large unlabelled datasets. GPT models use a self-supervised approach during pre-training.

## Aprendizado profundo

Aprendizado profundo is a subset de Aprendizado de máquina that uses artificial Redes neurais com many layers (deep networks). Inspired loosely by o/a brain's neural structure, these networks learn hierarchical representations de Dados. Aprendizado profundo powers:

- **Computer Vision**: Image recognition, object detection, medical imaging
- **Natural Idioma Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key Aprendizado profundo architectures include convolutional Redes neurais (CNNs) para images, recurrent Redes neurais (RNNs) e LSTMs para sequences, transformers para Idioma, e generative adversarial networks (GANs) para synthesis.

## Large Idioma Models (LLMs)

Large Idioma Models (LLMs) are AI Sistemas trained on vast amounts de text Dados to understand e generate human Idioma. They are based on o/a Transformer Arquitetura, introduced em o/a 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict o/a next token (word piece) em a sequence, allowing them to generate coherent text, answer questions, write code, e perform reasoning tasks.

Notable LLMs include:
- **GPT series** (OpenAI): GPT-3, GPT-4, e successors — widely used para chat e code
- **Claude** (Anthropic): Focused on safety e helpfulness
- **Gemini** (Google DeepMind): Multimodal, integrating text, images, e code
- **LLaMA / Llama 3** (Meta): Open-weight models para research e local Implantação
- **Mistral** (Mistral AI): Efficient open models competitive com much larger LLMs

LLMs are trained em two stages: pre-training (unsupervised on large text corpora) e fine-tuning (supervised or via reinforcement learning from human feedback, RLHF). Context windows describe how much text an LLM can process at once, ranging from 4K tokens (early GPT-3) to over 1 million tokens em o/a most Avançado 2024 models.

## AI Ethics e Safety

AI raises important ethical questions including bias, privacy, job displacement, e o/a risk de misuse. Algorithmic bias occurs when training Dados reflects historical inequalities, causing AI Sistemas to produce discriminatory outputs. Facial recognition Sistemas have shown higher error rates para darker-skinned individuals. Hiring algorithms have been found to favour male candidates.

AI safety is o/a field dedicated to ensuring AI Sistemas behave as intended without causing unintended harm. Key concerns include:
- **Alignment**: Ensuring AI goals match human values
- **Interpretability / Explainability**: Understanding why an AI made a decision (critical em Medicina, Direito, Finanças)
- **Misuse**: AI-generated deepfakes, disinformation, cyberattacks
- **Existential risk**: Theoretical concern that a Futuro AGI could pursue goals misaligned com human survival

Organisations working on AI safety include OpenAI's Safety team, Anthropic (founded by former OpenAI safety researchers), DeepMind's safety team, e independent institutes like MIRI e ARC.

## AI em Society

AI is transforming nearly every industry:

- **Saúde**: AI assists em diagnosing cancer from medical images, predicting patient outcomes, accelerating drug discovery (AlphaFold solved protein folding structure prediction), e personalising treatment plans.
- **Finanças**: Fraud detection, algorithmic trading, credit scoring, e robo-advisors use ML models.
- **Transportation**: Self-driving vehicles use computer vision, lidar, e reinforcement learning. Tesla Autopilot, Waymo, e Cruise are leading efforts.
- **Education**: Personalised learning platforms adapt content to individual student pace e learning style.
- **Creative fields**: AI generates music, art, e writing; tools like Midjourney, DALL-E, e GitHub Copilot have changed creative workflows.
- **Cybersecurity**: AI detects anomalies, identifies threats, e powers both attacks e defences.

## Robotics e Embodied AI

Robotics combines AI com physical machines. Modern robots use perception (cameras, lidar), planning, e control to navigate e manipulate environments. Boston Dynamics' Atlas demonstrates Avançado bipedal movement. Industrial robots from companies like ABB e FANUC automate manufacturing. Household robots (Roomba) e surgical robots (da Vinci System) apply AI em everyday e medical settings. Embodied AI research focuses on agents that learn physical skills through interaction com o/a world, bridging o/a gap between simulated e real environments.

## Current AI Trends (2020s)

- **Multimodal AI**: Sistemas that process text, images, audio, e video together (GPT-4V, Gemini)
- **Agents e agentic AI**: LLMs that can use tools, browse o/a Web, write code, e take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models para researchers
- **On-device AI**: Running AI models locally on phones e laptops without cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: o/a EU AI Act (2024) is o/a world's first comprehensive AI Direito, classifying AI Sistemas by risk level
