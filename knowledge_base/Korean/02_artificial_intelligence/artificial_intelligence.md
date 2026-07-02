<!-- 
This file was automatically translated from English to Korean.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) refers to 그 simulation 의 human intelligence 에서 machines programmed to think, learn, 와 solve problems. AI 시스템 can perform tasks that typically require human intelligence, such as recognising speech, making decisions, translating languages, 와 identifying objects 에서 images. 그 term was coined by John McCarthy 에서 1956 at 그 Dartmouth Conference, widely regarded as 그 founding event 의 AI as a field.

Modern AI is broadly divided into Narrow AI (also called Weak AI), which is designed 위한 specific tasks, 와 그 theoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domains. All current AI 시스템 are Narrow AI.

## 역사 의 AI

그 역사 의 AI spans nearly eight decades. Early theoretical foundations were laid by Alan Turing, whose 1950 paper "컴퓨팅 Machinery 와 Intelligence" introduced 그 Turing Test — a measure 의 a machine's ability to exhibit intelligent behaviour indistinguishable from a human. 그 1956 Dartmouth Conference formally established AI as an academic discipline.

그 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) 와 LISP (a programming 언어 designed 위한 AI). 그 "AI winters" 의 그 1970s 와 1980s were periods 의 reduced funding 와 interest following unmet expectations. A resurgence 에서 그 1980s came 와 함께 expert 시스템 — rule-based programs that encoded human expertise. 그 2000s brought 기계 학습 breakthroughs fuelled by 그 internet 와 growing datasets. 그 2010s saw 그 rise 의 딥 러닝, transforming computer vision, natural 언어 processing (NLP), 와 reinforcement learning.

## 기계 학습

기계 학습 (ML) is a subset 의 AI that enables 시스템 to learn from 데이터 without being explicitly programmed. Key ML categories include:

**Supervised Learning**: 그 model is trained on labelled input-output pairs. 예시 include spam detection 와 image classification. Algorithms include linear regression, decision trees, support vector machines, 와 신경망.

**Unsupervised Learning**: 그 model finds patterns 에서 unlabelled 데이터. 예시 include customer segmentation 와 anomaly detection. Algorithms include k-means clustering 와 principal component analysis (PCA).

**Reinforcement Learning**: An agent learns by interacting 와 함께 an environment, receiving rewards or penalties. Used 에서 game-playing AI (AlphaGo, AlphaZero), robotics, 와 recommendation 시스템.

**Semi-Supervised 와 Self-Supervised Learning**: Combine small amounts 의 labelled 데이터 와 함께 large unlabelled datasets. GPT models use a self-supervised approach during pre-training.

## 딥 러닝

딥 러닝 is a subset 의 기계 학습 that uses artificial 신경망 와 함께 many layers (deep networks). Inspired loosely by 그 brain's neural structure, these networks learn hierarchical representations 의 데이터. 딥 러닝 powers:

- **Computer Vision**: Image recognition, object detection, medical imaging
- **Natural 언어 Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key 딥 러닝 architectures include convolutional 신경망 (CNNs) 위한 images, recurrent 신경망 (RNNs) 와 LSTMs 위한 sequences, transformers 위한 언어, 와 generative adversarial networks (GANs) 위한 synthesis.

## Large 언어 Models (LLMs)

Large 언어 Models (LLMs) are AI 시스템 trained on vast amounts 의 text 데이터 to understand 와 generate human 언어. They are based on 그 Transformer 아키텍처, introduced 에서 그 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict 그 next token (word piece) 에서 a sequence, allowing them to generate coherent text, answer questions, write code, 와 perform reasoning tasks.

Notable LLMs include:
- **GPT series** (OpenAI): GPT-3, GPT-4, 와 successors — widely used 위한 chat 와 code
- **Claude** (Anthropic): Focused on safety 와 helpfulness
- **Gemini** (Google DeepMind): Multimodal, integrating text, images, 와 code
- **LLaMA / Llama 3** (Meta): Open-weight models 위한 research 와 local 배포
- **Mistral** (Mistral AI): Efficient open models competitive 와 함께 much larger LLMs

LLMs are trained 에서 two stages: pre-training (unsupervised on large text corpora) 와 fine-tuning (supervised or via reinforcement learning from human feedback, RLHF). Context windows describe how much text an LLM can process at once, ranging from 4K tokens (early GPT-3) to over 1 million tokens 에서 그 most 고급 2024 models.

## AI Ethics 와 Safety

AI raises important ethical questions including bias, privacy, job displacement, 와 그 risk 의 misuse. Algorithmic bias occurs when training 데이터 reflects historical inequalities, causing AI 시스템 to produce discriminatory outputs. Facial recognition 시스템 have shown higher error rates 위한 darker-skinned individuals. Hiring algorithms have been found to favour male candidates.

AI safety is 그 field dedicated to ensuring AI 시스템 behave as intended without causing unintended harm. Key concerns include:
- **Alignment**: Ensuring AI goals match human values
- **Interpretability / Explainability**: Understanding why an AI made a decision (critical 에서 의학, 법률, 금융)
- **Misuse**: AI-generated deepfakes, disinformation, cyberattacks
- **Existential risk**: Theoretical concern that a 미래 AGI could pursue goals misaligned 와 함께 human survival

Organisations working on AI safety include OpenAI's Safety team, Anthropic (founded by former OpenAI safety researchers), DeepMind's safety team, 와 independent institutes like MIRI 와 ARC.

## AI 에서 Society

AI is transforming nearly every industry:

- **의료**: AI assists 에서 diagnosing cancer from medical images, predicting patient outcomes, accelerating drug discovery (AlphaFold solved protein folding structure prediction), 와 personalising treatment plans.
- **금융**: Fraud detection, algorithmic trading, credit scoring, 와 robo-advisors use ML models.
- **Transportation**: Self-driving vehicles use computer vision, lidar, 와 reinforcement learning. Tesla Autopilot, Waymo, 와 Cruise are leading efforts.
- **Education**: Personalised learning platforms adapt content to individual student pace 와 learning style.
- **Creative fields**: AI generates music, art, 와 writing; tools like Midjourney, DALL-E, 와 GitHub Copilot have changed creative workflows.
- **Cybersecurity**: AI detects anomalies, identifies threats, 와 powers both attacks 와 defences.

## Robotics 와 Embodied AI

Robotics combines AI 와 함께 physical machines. Modern robots use perception (cameras, lidar), planning, 와 control to navigate 와 manipulate environments. Boston Dynamics' Atlas demonstrates 고급 bipedal movement. Industrial robots from companies like ABB 와 FANUC automate manufacturing. Household robots (Roomba) 와 surgical robots (da Vinci System) apply AI 에서 everyday 와 medical settings. Embodied AI research focuses on agents that learn physical skills through interaction 와 함께 그 world, bridging 그 gap between simulated 와 real environments.

## Current AI Trends (2020s)

- **Multimodal AI**: 시스템 that process text, images, audio, 와 video together (GPT-4V, Gemini)
- **Agents 와 agentic AI**: LLMs that can use tools, browse 그 웹, write code, 와 take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models 위한 researchers
- **On-device AI**: Running AI models locally on phones 와 laptops without cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: 그 EU AI Act (2024) is 그 world's first comprehensive AI 법률, classifying AI 시스템 by risk level
