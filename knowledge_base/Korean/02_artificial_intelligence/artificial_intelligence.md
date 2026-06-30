<!-- 
This file was automatically translated from English to Korean.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

# # What is Artificial Intelligence?

Artificial Intelligence (인공 지능) refers to simulation human 인텔리전스 mach programmed to thk, learn, solve problems. 인공 지능 시스템 can perm tasks that typically require human 인텔리전스, such as recognis speech, mak decisions, translat 언어s, identify objects images. The term was coed by John McCarthy 1956 at Dartmouth Conference, widely regarded as found event 인공 지능 as a field.

Modern 인공 지능 is broadly divided 로 Narrow 인공 지능 (also called Weak 인공 지능), which is designed specific tasks, oretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domas. All current 인공 지능 시스템 are Narrow 인공 지능.

# # 역사 인공 지능

The 역사 인공 지능 spans nearly eight decades. Early oretical foundations were laid by Alan Tur, whose 1950 paper "Comput Machery Intelligence" troduced Tur Test — a measure a mache's ability to exhibit telligent behaviour distuishable from a human. The 1956 Dartmouth Conference mally established 인공 지능 as an academic disciple.

The 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) LISP (a programm 언어 designed 인공 지능). The "인공 지능 wters" 1970s 1980s were periods reduced fund terest follow unmet expectations. A resurgence 1980s came 함께 expert 시스템 — rule-based programs that encoded human expertise. The 2000s brought mache learn breakthroughs fuelled by ternet grow 데이 터sets. The 2010s saw rise deep learn, transm computer vision, natural 언어 process (NLP), recement learn.

# # Mache Learn

Mache Learn (기계 학습) is a subset 인공 지능 that enables 시스템 to learn from 데이 터 함께out be explicitly programmed. Key 기계 학습 categories 포함하다:

**Supervised Learn**: The model is traed on labelled put-output pairs. 예시 포함하다 spam detection image classification. Algorithms 포함하다 lear regression, decision trees, support vector mach, 신경망.

**Unsupervised Learn**: The model fds patterns unlabelled 데이 터. 예시 포함하다 customer segmentation anomaly detection. Algorithms 포함하다 k-means cluster prcipal component analysis (PCA).

**Recement Learn**: An agent learns by teract 함께 an 환경, receiv rewards or penalties. Used game-play 인공 지능 (AlphaGo, AlphaZero), robotics, recommendation 시스템.

**Semi-Supervised Self-Supervised Learn**: Combe small amounts labelled 데이 터 함께 large unlabelled 데이 터sets. GPT models use a self-supervised approach dur pre-tra.

# # Deep Learn

Deep Learn is a subset mache learn that uses artificial 신경망 함께 many layers (deep 네트워크s). Inspired loosely by bra's neural structure, se 네트워크s learn hierarchical representations 데이 터. Deep learn powers:

- **Computer Vision**: Image recognition, object detection, medical imag
- **Natural 언어 Process**: Mache translation, sentiment analysis, question answer
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative 인공 지능**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key deep learn 아키텍처s 포함하다 convolutional 신경망 (CNNs) images, recurrent 신경망 (RNNs) LSTMs sequences, transmers 언어, generative adversarial 네트워크s (GANs) synsis.

# # Large 언어 Models (대규모 언어 모델)

Large 언어 Models (대규모 언어 모델) are 인공 지능 시스템 traed on vast amounts text 데이 터 to underst generate human 언어. They are based on Transmer 아키텍처, troduced 2017 paper "Attention is All You Need" by Vaswani et al. 대규모 언어 모델 predict next token (word piece) a sequence, allow m to generate coherent text, answer questions, write code, perm reason tasks.

Notable 대규모 언어 모델 포함하다:
- **GPT series** (Open인공 지능): GPT-3, GPT-4, successors — widely used chat code
- **Claude** (Anthropic): Focused on 안전한ty helpfulness
- **Gemi** (Google DeepMd): Multimodal, tegrat text, images, code
- **LLaMA / Llama 3** (Meta): Open-weight models research local 배포
- **Mistral** (Mistral 인공 지능): Efficient open models competitive 함께 much larger 대규모 언어 모델

대규모 언어 모델 are traed two stages: pre-tra (unsupervised on large text corpora) fe-tun (supervised or via recement learn from human feedback, RLHF). Context wdows describe how much text an LLM can process at once, rang from 4K tokens (early GPT-3) to over 1 million tokens most 고급 2024 models.

# # 인공 지능 Ethics 안전한ty

인공 지능 raises important ethical questions clud bias, privacy, job displacement, risk misuse. Algorithmic bias occurs when tra 데이 터 reflects historical equalities, caus 인공 지능 시스템 to produce discrimatory outputs. Facial recognition 시스템 have shown higher error rates darker-skned dividuals. Hir algorithms have been found to favour male cidates.

인공 지능 안전한ty is field dedicated to ensur 인공 지능 시스템 behave as tended 함께out caus untended harm. Key concerns 포함하다:
- **Alignment**: Ensur 인공 지능 goals match human values
- **Interpretability / Explaability**: Underst why an 인공 지능 made a decision (critical medice, 법률, fance)
- **Misuse**: 인공 지능-generated deepfakes, dismation, cyberattacks
- **Existential risk**: Theoretical concern that a 미래 AGI could pursue goals misaligned 함께 human survival

Organisations work on 인공 지능 안전한ty 포함하다 Open인공 지능's 안전한ty team, Anthropic (founded by mer Open인공 지능 안전한ty researchers), DeepMd's 안전한ty team, dependent stitutes like MIRI ARC.

# # 인공 지능 Society

인공 지능 is transm nearly every dustry:

- **료**: 인공 지능 assists diagnos cancer from medical images, predict patient outcomes, accelerat drug discovery (AlphaFold solved prote fold structure prediction), personalis treatment plans.
- **Fance**: Fraud detection, algorithmic trad, credit scor, robo-advisors use 기계 학습 models.
- **Transportation**: Self-driv vehicles use computer vision, lidar, recement learn. Tesla Autopilot, Waymo, Cruise are lead efts.
- **Education**: Personalised learn platms adapt 콘텐츠 to dividual student pace learn style.
- **Creative fields**: 인공 지능 generates music, art, writ; tools like Midjourney, DALL-E, GitHub Copilot have changed creative workflows.
- **Cyber보안**: 인공 지능 detects anomalies, identifies threats, powers both attacks defences.

# # Robotics Embodied 인공 지능

Robotics comb 인공 지능 함께 physical mach. Modern robots use perception (cameras, lidar), plann, control to navigate manipulate 환경s. Boston Dynamics' Atlas demonstrates 고급 bipedal movement. Industrial robots from companies like ABB FANUC automate manufactur. Household robots (Roomba) surgical robots (da Vci System) apply 인공 지능 everyday medical setts. Embodied 인공 지능 research focuses on agents that learn physical skills through teraction 함께 world, bridg gap between simulated real 환경s.

# # Current 인공 지능 Trends (2020s)

- **Multimodal 인공 지능**: 시스템 that process text, images, audio, video toger (GPT-4V, Gemi)
- **Agents agentic 인공 지능**: 대규모 언어 모델 that can use tools, browse 웹, write code, take multi-step actions (Open인공 지능's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models researchers
- **On-device 인공 지능**: Runn 인공 지능 models locally on phones laptops 함께out 클라우드 connectivity (Apple Intelligence, Qualcomm NPUs)
- **인공 지능 regulation**: The EU 인공 지능 Act (2024) is world's first comprehensive 인공 지능 법률, classify 인공 지능 시스템 by risk level
