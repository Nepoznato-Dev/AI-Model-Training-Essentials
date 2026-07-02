<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) refers to 这 simulation 的 human intelligence 在 machines programmed to think, learn, 和 solve problems. AI 系统 can perform tasks that typically require human intelligence, such as recognising speech, making decisions, translating languages, 和 identifying objects 在 images. 这 term was coined by John McCarthy 在 1956 at 这 Dartmouth Conference, widely regarded as 这 founding event 的 AI as a field.

Modern AI is broadly divided into Narrow AI (also called Weak AI), which is designed 为 specific tasks, 和 这 theoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domains. All current AI 系统 are Narrow AI.

## 历史 的 AI

这 历史 的 AI spans nearly eight decades. Early theoretical foundations were laid by Alan Turing, whose 1950 paper "计算 Machinery 和 Intelligence" introduced 这 Turing Test — a measure 的 a machine's ability to exhibit intelligent behaviour indistinguishable from a human. 这 1956 Dartmouth Conference formally established AI as an academic discipline.

这 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) 和 LISP (a programming 语言 designed 为 AI). 这 "AI winters" 的 这 1970s 和 1980s were periods 的 reduced funding 和 interest following unmet expectations. A resurgence 在 这 1980s came 与 expert 系统 — rule-based programs that encoded human expertise. 这 2000s brought 机器学习 breakthroughs fuelled by 这 internet 和 growing datasets. 这 2010s saw 这 rise 的 深度学习, transforming computer vision, natural 语言 processing (NLP), 和 reinforcement learning.

## 机器学习

机器学习 (ML) is a subset 的 AI that enables 系统 to learn from 数据 without being explicitly programmed. Key ML categories include:

**Supervised Learning**: 这 model is trained on labelled input-output pairs. 示例 include spam detection 和 image classification. Algorithms include linear regression, decision trees, support vector machines, 和 神经网络.

**Unsupervised Learning**: 这 model finds patterns 在 unlabelled 数据. 示例 include customer segmentation 和 anomaly detection. Algorithms include k-means clustering 和 principal component analysis (PCA).

**Reinforcement Learning**: An agent learns by interacting 与 an environment, receiving rewards or penalties. Used 在 game-playing AI (AlphaGo, AlphaZero), robotics, 和 recommendation 系统.

**Semi-Supervised 和 Self-Supervised Learning**: Combine small amounts 的 labelled 数据 与 large unlabelled datasets. GPT models use a self-supervised approach during pre-training.

## 深度学习

深度学习 is a subset 的 机器学习 that uses artificial 神经网络 与 many layers (deep networks). Inspired loosely by 这 brain's neural structure, these networks learn hierarchical representations 的 数据. 深度学习 powers:

- **Computer Vision**: Image recognition, object detection, medical imaging
- **Natural 语言 Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key 深度学习 architectures include convolutional 神经网络 (CNNs) 为 images, recurrent 神经网络 (RNNs) 和 LSTMs 为 sequences, transformers 为 语言, 和 generative adversarial networks (GANs) 为 synthesis.

## Large 语言 Models (LLMs)

Large 语言 Models (LLMs) are AI 系统 trained on vast amounts 的 text 数据 to understand 和 generate human 语言. They are based on 这 Transformer 架构, introduced 在 这 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict 这 next token (word piece) 在 a sequence, allowing them to generate coherent text, answer questions, write code, 和 perform reasoning tasks.

Notable LLMs include:
- **GPT series** (OpenAI): GPT-3, GPT-4, 和 successors — widely used 为 chat 和 code
- **Claude** (Anthropic): Focused on safety 和 helpfulness
- **Gemini** (Google DeepMind): Multimodal, integrating text, images, 和 code
- **LLaMA / Llama 3** (Meta): Open-weight models 为 research 和 local 部署
- **Mistral** (Mistral AI): Efficient open models competitive 与 much larger LLMs

LLMs are trained 在 two stages: pre-training (unsupervised on large text corpora) 和 fine-tuning (supervised or via reinforcement learning from human feedback, RLHF). Context windows describe how much text an LLM can process at once, ranging from 4K tokens (early GPT-3) to over 1 million tokens 在 这 most 高级 2024 models.

## AI Ethics 和 Safety

AI raises important ethical questions including bias, privacy, job displacement, 和 这 risk 的 misuse. Algorithmic bias occurs when training 数据 reflects historical inequalities, causing AI 系统 to produce discriminatory outputs. Facial recognition 系统 have shown higher error rates 为 darker-skinned individuals. Hiring algorithms have been found to favour male candidates.

AI safety is 这 field dedicated to ensuring AI 系统 behave as intended without causing unintended harm. Key concerns include:
- **Alignment**: Ensuring AI goals match human values
- **Interpretability / Explainability**: Understanding why an AI made a decision (critical 在 医学, 法律, 金融)
- **Misuse**: AI-generated deepfakes, disinformation, cyberattacks
- **Existential risk**: Theoretical concern that a 未来 AGI could pursue goals misaligned 与 human survival

Organisations working on AI safety include OpenAI's Safety team, Anthropic (founded by former OpenAI safety researchers), DeepMind's safety team, 和 independent institutes like MIRI 和 ARC.

## AI 在 Society

AI is transforming nearly every industry:

- **医疗**: AI assists 在 diagnosing cancer from medical images, predicting patient outcomes, accelerating drug discovery (AlphaFold solved protein folding structure prediction), 和 personalising treatment plans.
- **金融**: Fraud detection, algorithmic trading, credit scoring, 和 robo-advisors use ML models.
- **Transportation**: Self-driving vehicles use computer vision, lidar, 和 reinforcement learning. Tesla Autopilot, Waymo, 和 Cruise are leading efforts.
- **Education**: Personalised learning platforms adapt content to individual student pace 和 learning style.
- **Creative fields**: AI generates music, art, 和 writing; tools like Midjourney, DALL-E, 和 GitHub Copilot have changed creative workflows.
- **Cybersecurity**: AI detects anomalies, identifies threats, 和 powers both attacks 和 defences.

## Robotics 和 Embodied AI

Robotics combines AI 与 physical machines. Modern robots use perception (cameras, lidar), planning, 和 control to navigate 和 manipulate environments. Boston Dynamics' Atlas demonstrates 高级 bipedal movement. Industrial robots from companies like ABB 和 FANUC automate manufacturing. Household robots (Roomba) 和 surgical robots (da Vinci System) apply AI 在 everyday 和 medical settings. Embodied AI research focuses on agents that learn physical skills through interaction 与 这 world, bridging 这 gap between simulated 和 real environments.

## Current AI Trends (2020s)

- **Multimodal AI**: 系统 that process text, images, audio, 和 video together (GPT-4V, Gemini)
- **Agents 和 agentic AI**: LLMs that can use tools, browse 这 网络, write code, 和 take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models 为 researchers
- **On-device AI**: Running AI models locally on phones 和 laptops without cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: 这 EU AI Act (2024) is 这 world's first comprehensive AI 法律, classifying AI 系统 by risk level
