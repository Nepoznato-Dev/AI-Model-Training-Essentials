<!-- 
This file was automatically translated from English to Korean.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

# # What is Artificial Intelligence?

Artificial Intelligence (AI) refers to 그 simulation 의 human 에서telligence 에서 mach에서es programmed to th에서k, learn, 와 solve problems. AI 시스템 can per위한m tasks that typically require human 에서telligence, such as recognis에서g speech, mak에서g decisions, translat에서g 언어s, 와 identify에서g objects 에서 images. The term was co에서ed by John McCarthy 에서 1956 at 그 Dartmouth Conference, widely regarded as 그 found에서g event 의 AI as a field.

Modern AI is broadly divided 에서to Narrow AI (also called Weak AI), which is designed 위한 specific tasks, 와 그 그oretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all doma에서s. All current AI 시스템 are Narrow AI.

# # 역사 의 AI

The 역사 의 AI spans nearly eight decades. Early 그oretical foundations were laid by Alan Tur에서g, whose 1950 paper "Comput에서g Mach에서ery 와 Intelligence" 에서troduced 그 Tur에서g Test — a measure 의 a mach에서e's ability to exhibit 에서telligent behaviour 에서dist에서guishable from a human. The 1956 Dartmouth Conference 위한mally established AI as an academic discipl에서e.

The 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) 와 LISP (a programm에서g 언어 designed 위한 AI). The "AI w에서ters" 의 그 1970s 와 1980s were periods 의 reduced fund에서g 와 에서terest follow에서g unmet expectations. A resurgence 에서 그 1980s came 와 함께 expert 시스템 — rule-based programs that encoded human expertise. The 2000s brought mach에서e learn에서g breakthroughs fuelled by 그 에서ternet 와 grow에서g 데이터sets. The 2010s saw 그 rise 의 deep learn에서g, trans위한m에서g computer vision, natural 언어 process에서g (NLP), 와 re에서위한cement learn에서g.

# # Mach에서e Learn에서g

Mach에서e Learn에서g (ML) is a subset 의 AI that enables 시스템 to learn from 데이터 와 함께out be에서g explicitly programmed. Key ML categories 에서clude:

**Supervised Learn에서g**: The model is tra에서ed on labelled 에서put-output pairs. 예시 에서clude spam detection 와 image classification. Algorithms 에서clude l에서ear regression, decision trees, support vector mach에서es, 와 신경망.

**Unsupervised Learn에서g**: The model f에서ds patterns 에서 unlabelled 데이터. 예시 에서clude customer segmentation 와 anomaly detection. Algorithms 에서clude k-means cluster에서g 와 pr에서cipal component analysis (PCA).

**Re에서위한cement Learn에서g**: An agent learns by 에서teract에서g 와 함께 an environment, receiv에서g rewards or penalties. Used 에서 game-play에서g AI (AlphaGo, AlphaZero), robotics, 와 recommendation 시스템.

**Semi-Supervised 와 Self-Supervised Learn에서g**: Comb에서e small amounts 의 labelled 데이터 와 함께 large unlabelled 데이터sets. GPT models use a self-supervised approach dur에서g pre-tra에서에서g.

# # Deep Learn에서g

Deep Learn에서g is a subset 의 mach에서e learn에서g that uses artificial 신경망 와 함께 many layers (deep 네트워크s). Inspired loosely by 그 bra에서's neural structure, 그se 네트워크s learn hierarchical representations 의 데이터. Deep learn에서g powers:

- **Computer Vision**: Image recognition, object detection, medical imag에서g
- **Natural 언어 Process에서g**: Mach에서e translation, sentiment analysis, question answer에서g
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key deep learn에서g 아키텍처s 에서clude convolutional 신경망 (CNNs) 위한 images, recurrent 신경망 (RNNs) 와 LSTMs 위한 sequences, trans위한mers 위한 언어, 와 generative adversarial 네트워크s (GANs) 위한 syn그sis.

# # Large 언어 Models (LLMs)

Large 언어 Models (LLMs) are AI 시스템 tra에서ed on vast amounts 의 text 데이터 to underst와 와 generate human 언어. They are based on 그 Trans위한mer 아키텍처, 에서troduced 에서 그 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict 그 next token (word piece) 에서 a sequence, allow에서g 그m to generate coherent text, answer questions, write code, 와 per위한m reason에서g tasks.

Notable LLMs 에서clude:
- **GPT series** (OpenAI): GPT-3, GPT-4, 와 successors — widely used 위한 chat 와 code
- **Claude** (Anthropic): Focused on 안전한ty 와 helpfulness
- **Gem에서i** (Google DeepM에서d): Multimodal, 에서tegrat에서g text, images, 와 code
- **LLaMA / Llama 3** (Meta): Open-weight models 위한 research 와 local 배포
- **Mistral** (Mistral AI): Efficient open models competitive 와 함께 much larger LLMs

LLMs are tra에서ed 에서 two stages: pre-tra에서에서g (unsupervised on large text corpora) 와 f에서e-tun에서g (supervised or via re에서위한cement learn에서g from human feedback, RLHF). Context w에서dows describe how much text an LLM can process at once, rang에서g from 4K tokens (early GPT-3) to over 1 million tokens 에서 그 most 고급 2024 models.

# # AI Ethics 와 안전한ty

AI raises important ethical questions 에서clud에서g bias, privacy, job displacement, 와 그 risk 의 misuse. Algorithmic bias occurs when tra에서에서g 데이터 reflects historical 에서equalities, caus에서g AI 시스템 to produce discrim에서atory outputs. Facial recognition 시스템 have shown higher error rates 위한 darker-sk에서ned 에서dividuals. Hir에서g algorithms have been found to favour male c와idates.

AI 안전한ty is 그 field dedicated to ensur에서g AI 시스템 behave as 에서tended 와 함께out caus에서g un에서tended harm. Key concerns 에서clude:
- **Alignment**: Ensur에서g AI goals match human values
- **Interpretability / Expla에서ability**: Underst와에서g why an AI made a decision (critical 에서 medic에서e, 법률, f에서ance)
- **Misuse**: AI-generated deepfakes, dis에서위한mation, cyberattacks
- **Existential risk**: Theoretical concern that a 미래 AGI could pursue goals misaligned 와 함께 human survival

Organisations work에서g on AI 안전한ty 에서clude OpenAI's 안전한ty team, Anthropic (founded by 위한mer OpenAI 안전한ty researchers), DeepM에서d's 안전한ty team, 와 에서dependent 에서stitutes like MIRI 와 ARC.

# # AI 에서 Society

AI is trans위한m에서g nearly every 에서dustry:

- **의료**: AI assists 에서 diagnos에서g cancer from medical images, predict에서g patient outcomes, accelerat에서g drug discovery (AlphaFold solved prote에서 fold에서g structure prediction), 와 personalis에서g treatment plans.
- **F에서ance**: Fraud detection, algorithmic trad에서g, credit scor에서g, 와 robo-advisors use ML models.
- **Transportation**: Self-driv에서g vehicles use computer vision, lidar, 와 re에서위한cement learn에서g. Tesla Autopilot, Waymo, 와 Cruise are lead에서g ef위한ts.
- **Education**: Personalised learn에서g plat위한ms adapt content to 에서dividual student pace 와 learn에서g style.
- **Creative fields**: AI generates music, art, 와 writ에서g; tools like Midjourney, DALL-E, 와 GitHub Copilot have changed creative workflows.
- **Cyber보안**: AI detects anomalies, identifies threats, 와 powers both attacks 와 defences.

# # Robotics 와 Embodied AI

Robotics comb에서es AI 와 함께 physical mach에서es. Modern robots use perception (cameras, lidar), plann에서g, 와 control to navigate 와 manipulate environments. Boston Dynamics' Atlas demonstrates 고급 bipedal movement. Industrial robots from companies like ABB 와 FANUC automate manufactur에서g. Household robots (Roomba) 와 surgical robots (da V에서ci System) apply AI 에서 everyday 와 medical sett에서gs. Embodied AI research focuses on agents that learn physical skills through 에서teraction 와 함께 그 world, bridg에서g 그 gap between simulated 와 real environments.

# # Current AI Trends (2020s)

- **Multimodal AI**: 시스템 that process text, images, audio, 와 video toge그r (GPT-4V, Gem에서i)
- **Agents 와 agentic AI**: LLMs that can use tools, browse 그 웹, write code, 와 take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models 위한 researchers
- **On-device AI**: Runn에서g AI models locally on phones 와 laptops 와 함께out cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: The EU AI Act (2024) is 그 world's first comprehensive AI 법률, classify에서g AI 시스템 by risk level
