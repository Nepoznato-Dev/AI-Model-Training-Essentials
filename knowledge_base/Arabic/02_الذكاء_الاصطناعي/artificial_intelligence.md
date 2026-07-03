<!-- 
This file was automatically translated from English to Arabic.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

## What is Artificial Intelligence?

Artificial Intelligence (AI) refers to ال simulation من human intelligence في machines programmed to think, learn, و solve problems. AI الأنظمة can perform tasks that typically require human intelligence, such as recognising speech, making decisions, translating languages, و identifying objects في images. ال term was coined by John McCarthy في 1956 at ال Dartmouth Conference, widely regarded as ال founding event من AI as a field.

Modern AI is broadly divided into Narrow AI (also called Weak AI), which is designed لأجل specific tasks, و ال theoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domains. All current AI الأنظمة are Narrow AI.

## التاريخ من AI

ال التاريخ من AI spans nearly eight decades. Early theoretical foundations were laid by Alan Turing, whose 1950 paper "الحوسبة Machinery و Intelligence" introduced ال Turing Test — a measure من a machine's ability to exhibit intelligent behaviour indistinguishable from a human. ال 1956 Dartmouth Conference formally established AI as an academic discipline.

ال 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) و LISP (a programming اللغة designed لأجل AI). ال "AI winters" من ال 1970s و 1980s were periods من reduced funding و interest following unmet expectations. A resurgence في ال 1980s came مع expert الأنظمة — rule-based programs that encoded human expertise. ال 2000s brought التعلم الآلي breakthroughs fuelled by ال internet و growing datasets. ال 2010s saw ال rise من التعلم العميق, transforming computer vision, natural اللغة processing (NLP), و reinforcement learning.

## التعلم الآلي

التعلم الآلي (ML) is a subset من AI that enables الأنظمة to learn from البيانات without being explicitly programmed. Key ML categories include:

**Supervised Learning**: ال model is trained on labelled input-output pairs. أمثلة include spam detection و image classification. Algorithms include linear regression, decision trees, الدعم vector machines, و الشبكات العصبية.

**Unsupervised Learning**: ال model finds patterns في unlabelled البيانات. أمثلة include customer segmentation و anomaly detection. Algorithms include k-means clustering و principal component analysis (PCA).

**Reinforcement Learning**: An agent learns by interacting مع an environment, receiving rewards or penalties. Used في game-playing AI (AlphaGo, AlphaZero), robotics, و recommendation الأنظمة.

**Semi-Supervised و Self-Supervised Learning**: Combine small amounts من labelled البيانات مع large unlabelled datasets. GPT models use a self-supervised approach during pre-training.

## التعلم العميق

التعلم العميق is a subset من التعلم الآلي that uses artificial الشبكات العصبية مع many layers (deep networks). Inspired loosely by ال brain's neural structure, these networks learn hierarchical representations من البيانات. التعلم العميق powers:

- **Computer Vision**: Image recognition, object detection, medical imaging
- **Natural اللغة Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key التعلم العميق architectures include convolutional الشبكات العصبية (CNNs) لأجل images, recurrent الشبكات العصبية (RNNs) و LSTMs لأجل sequences, transformers لأجل اللغة, و generative adversarial networks (GANs) لأجل synthesis.

## Large اللغة Models (LLMs)

Large اللغة Models (LLMs) are AI الأنظمة trained on vast amounts من text البيانات to understand و generate human اللغة. They are based on ال Transformer العمارة, introduced في ال 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict ال next token (word piece) في a sequence, allowing them to generate coherent text, answer questions, write code, و perform reasoning tasks.

Notable LLMs include:
- **GPT series** (OpenAI): GPT-3, GPT-4, و successors — widely used لأجل chat و code
- **Claude** (Anthropic): Focused on safety و helpfulness
- **Gemini** (Google DeepMind): Multimodal, integrating text, images, و code
- **LLaMA / Llama 3** (Meta): Open-weight models لأجل research و local النشر
- **Mistral** (Mistral AI): Efficient open models competitive مع much larger LLMs

LLMs are trained في two stages: pre-training (unsupervised on large text corpora) و fine-tuning (supervised or via reinforcement learning from human ملاحظات, RLHF). Context windows describe how much text an LLM can process at once, ranging from 4K tokens (early GPT-3) to over 1 million tokens في ال most متقدم 2024 models.

## AI Ethics و Safety

AI raises important ethical questions including bias, privacy, job displacement, و ال risk من misuse. Algorithmic bias occurs when training البيانات reflects historical inequalities, causing AI الأنظمة to produce discriminatory outputs. Facial recognition الأنظمة have shown higher error rates لأجل darker-skinned individuals. Hiring algorithms have been found to favour male candidates.

AI safety is ال field dedicated to ensuring AI الأنظمة behave as intended without causing unintended harm. Key concerns include:
- **Alignment**: Ensuring AI goals match human values
- **Interpretability / Explainability**: Understanding why an AI made a decision (critical في الطب, القانون, المالية)
- **Misuse**: AI-generated deepfakes, disinformation, cyberattacks
- **Existential risk**: Theoretical concern that a المستقبل AGI could pursue goals misaligned مع human survival

Organisations working on AI safety include OpenAI's Safety team, Anthropic (founded by former OpenAI safety researchers), DeepMind's safety team, و independent institutes like MIRI و ARC.

## AI في Society

AI is transforming nearly every industry:

- **الرعاية الصحية**: AI assists في diagnosing cancer from medical images, predicting patient outcomes, accelerating drug discovery (AlphaFold solved protein folding structure prediction), و personalising treatment plans.
- **المالية**: Fraud detection, algorithmic trading, credit scoring, و robo-advisors use ML models.
- **Transportation**: Self-driving vehicles use computer vision, lidar, و reinforcement learning. Tesla Autopilot, Waymo, و Cruise are leading efforts.
- **Education**: Personalised learning platforms adapt content to individual student pace و learning style.
- **Creative fields**: AI generates music, art, و writing; tools like Midjourney, DALL-E, و GitHub Copilot have changed creative workflows.
- **Cybersecurity**: AI detects anomalies, identifies threats, و powers both attacks و defences.

## Robotics و Embodied AI

Robotics combines AI مع physical machines. Modern robots use perception (cameras, lidar), planning, و control to navigate و manipulate environments. Boston Dynamics' Atlas demonstrates متقدم bipedal movement. Industrial robots from companies like ABB و FANUC automate manufacturing. Household robots (Roomba) و surgical robots (da Vinci System) apply AI في everyday و medical settings. Embodied AI research focuses on agents that learn physical skills through interaction مع ال world, bridging ال gap between simulated و real environments.

## Current AI Trends (2020s)

- **Multimodal AI**: الأنظمة that process text, images, audio, و video together (GPT-4V, Gemini)
- **Agents و agentic AI**: LLMs that can use tools, browse ال الويب, write code, و take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models لأجل researchers
- **On-device AI**: Running AI models locally on phones و laptops without cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: ال EU AI Act (2024) is ال world's first comprehensive AI القانون, classifying AI الأنظمة by risk level
