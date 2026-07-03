<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) refers to 這 simulation 的 human intelligence 在 machines programmed to think, learn, 和 solve problems. AI 系統 can perform tasks that typically require human intelligence, such as recognising speech, making decisions, translating languages, 和 identifying objects 在 images. 這 term was coined by John McCarthy 在 1956 at 這 Dartmouth Conference, widely regarded as 這 founding event 的 AI as a field.

Modern AI is broadly divided into Narrow AI (also called Weak AI), which is designed 為 specific tasks, 和 這 theoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domains. All current AI 系統 are Narrow AI.

## 歷史 的 AI

這 歷史 的 AI spans nearly eight decades. Early theoretical foundations were laid by Alan Turing, whose 1950 paper "計算 Machinery 和 Intelligence" introduced 這 Turing Test — a measure 的 a machine's ability to exhibit intelligent behaviour indistinguishable from a human. 這 1956 Dartmouth Conference formally established AI as an academic discipline.

這 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) 和 LISP (a programming 語言 designed 為 AI). 這 "AI winters" 的 這 1970s 和 1980s were periods 的 reduced funding 和 interest following unmet expectations. A resurgence 在 這 1980s came 與 expert 系統 — rule-based programs that encoded human expertise. 這 2000s brought 機器學習 breakthroughs fuelled by 這 internet 和 growing datasets. 這 2010s saw 這 rise 的 深度學習, transforming computer vision, natural 語言 processing (NLP), 和 reinforcement learning.

## 機器學習

機器學習 (ML) is a subset 的 AI that enables 系統 to learn from 資料 without being explicitly programmed. Key ML categories include:

**Supervised Learning**: 這 model is trained on labelled input-output pairs. 範例 include spam detection 和 image classification. Algorithms include linear regression, decision trees, 支援 vector machines, 和 神經網絡.

**Unsupervised Learning**: 這 model finds patterns 在 unlabelled 資料. 範例 include customer segmentation 和 anomaly detection. Algorithms include k-means clustering 和 principal component analysis (PCA).

**Reinforcement Learning**: An agent learns by interacting 與 an environment, receiving rewards or penalties. Used 在 game-playing AI (AlphaGo, AlphaZero), robotics, 和 recommendation 系統.

**Semi-Supervised 和 Self-Supervised Learning**: Combine small amounts 的 labelled 資料 與 large unlabelled datasets. GPT models use a self-supervised approach during pre-training.

## 深度學習

深度學習 is a subset 的 機器學習 that uses artificial 神經網絡 與 many layers (deep networks). Inspired loosely by 這 brain's neural structure, these networks learn hierarchical representations 的 資料. 深度學習 powers:

- **Computer Vision**: Image recognition, object detection, medical imaging
- **Natural 語言 Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key 深度學習 architectures include convolutional 神經網絡 (CNNs) 為 images, recurrent 神經網絡 (RNNs) 和 LSTMs 為 sequences, transformers 為 語言, 和 generative adversarial networks (GANs) 為 synthesis.

## Large 語言 Models (LLMs)

Large 語言 Models (LLMs) are AI 系統 trained on vast amounts 的 text 資料 to understand 和 generate human 語言. They are based on 這 Transformer 架構, introduced 在 這 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict 這 next token (word piece) 在 a sequence, allowing them to generate coherent text, answer questions, write code, 和 perform reasoning tasks.

Notable LLMs include:
- **GPT series** (OpenAI): GPT-3, GPT-4, 和 successors — widely used 為 chat 和 code
- **Claude** (Anthropic): Focused on safety 和 helpfulness
- **Gemini** (Google DeepMind): Multimodal, integrating text, images, 和 code
- **LLaMA / Llama 3** (Meta): Open-weight models 為 research 和 local 部署
- **Mistral** (Mistral AI): Efficient open models competitive 與 much larger LLMs

LLMs are trained 在 two stages: pre-training (unsupervised on large text corpora) 和 fine-tuning (supervised or via reinforcement learning from human 回饋, RLHF). Context windows describe how much text an LLM can process at once, ranging from 4K tokens (early GPT-3) to over 1 million tokens 在 這 most 高級 2024 models.

## AI Ethics 和 Safety

AI raises important ethical questions including bias, privacy, job displacement, 和 這 risk 的 misuse. Algorithmic bias occurs when training 資料 reflects historical inequalities, causing AI 系統 to produce discriminatory outputs. Facial recognition 系統 have shown higher error rates 為 darker-skinned individuals. Hiring algorithms have been found to favour male candidates.

AI safety is 這 field dedicated to ensuring AI 系統 behave as intended without causing unintended harm. Key concerns include:
- **Alignment**: Ensuring AI goals match human values
- **Interpretability / Explainability**: Understanding why an AI made a decision (critical 在 醫學, 法律, 金融)
- **Misuse**: AI-generated deepfakes, disinformation, cyberattacks
- **Existential risk**: Theoretical concern that a 未來 AGI could pursue goals misaligned 與 human survival

Organisations working on AI safety include OpenAI's Safety team, Anthropic (founded by former OpenAI safety researchers), DeepMind's safety team, 和 independent institutes like MIRI 和 ARC.

## AI 在 Society

AI is transforming nearly every industry:

- **醫療**: AI assists 在 diagnosing cancer from medical images, predicting patient outcomes, accelerating drug discovery (AlphaFold solved protein folding structure prediction), 和 personalising treatment plans.
- **金融**: Fraud detection, algorithmic trading, credit scoring, 和 robo-advisors use ML models.
- **Transportation**: Self-driving vehicles use computer vision, lidar, 和 reinforcement learning. Tesla Autopilot, Waymo, 和 Cruise are leading efforts.
- **Education**: Personalised learning platforms adapt content to individual student pace 和 learning style.
- **Creative fields**: AI generates music, art, 和 writing; tools like Midjourney, DALL-E, 和 GitHub Copilot have changed creative workflows.
- **Cybersecurity**: AI detects anomalies, identifies threats, 和 powers both attacks 和 defences.

## Robotics 和 Embodied AI

Robotics combines AI 與 physical machines. Modern robots use perception (cameras, lidar), planning, 和 control to navigate 和 manipulate environments. Boston Dynamics' Atlas demonstrates 高級 bipedal movement. Industrial robots from companies like ABB 和 FANUC automate manufacturing. Household robots (Roomba) 和 surgical robots (da Vinci System) apply AI 在 everyday 和 medical settings. Embodied AI research focuses on agents that learn physical skills through interaction 與 這 world, bridging 這 gap between simulated 和 real environments.

## Current AI Trends (2020s)

- **Multimodal AI**: 系統 that process text, images, audio, 和 video together (GPT-4V, Gemini)
- **Agents 和 agentic AI**: LLMs that can use tools, browse 這 網路, write code, 和 take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models 為 researchers
- **On-device AI**: Running AI models locally on phones 和 laptops without cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: 這 EU AI Act (2024) is 這 world's first comprehensive AI 法律, classifying AI 系統 by risk level
