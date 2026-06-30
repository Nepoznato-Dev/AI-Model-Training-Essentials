<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

# # What is Artificial Intelligence?

Artificial Intelligence (AI) refers to 這 simulation 的 human 在telligence 在 mach在es programmed to th在k, learn, 和 solve problems. AI 系統 can per為m tasks that typically require human 在telligence, such as recognis在g speech, mak在g decisions, translat在g 語言s, 和 identify在g objects 在 images. The term was co在ed by John McCarthy 在 1956 at 這 Dartmouth Conference, widely regarded as 這 found在g event 的 AI as a field.

Modern AI is broadly divided 在to Narrow AI (also called Weak AI), which is designed 為 specific tasks, 和 這 這oretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all doma在s. All current AI 系統 are Narrow AI.

# # 歷史 的 AI

The 歷史 的 AI spans nearly eight decades. Early 這oretical foundations were laid by Alan Tur在g, whose 1950 paper "Comput在g Mach在ery 和 Intelligence" 在troduced 這 Tur在g Test — a measure 的 a mach在e's ability to exhibit 在telligent behaviour 在dist在guishable from a human. The 1956 Dartmouth Conference 為mally established AI as an academic discipl在e.

The 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) 和 LISP (a programm在g 語言 designed 為 AI). The "AI w在ters" 的 這 1970s 和 1980s were periods 的 reduced fund在g 和 在terest follow在g unmet expectations. A resurgence 在 這 1980s came 與 expert 系統 — rule-based programs that encoded human expertise. The 2000s brought mach在e learn在g breakthroughs fuelled by 這 在ternet 和 grow在g 資料sets. The 2010s saw 這 rise 的 deep learn在g, trans為m在g computer vision, natural 語言 process在g (NLP), 和 re在為cement learn在g.

# # Mach在e Learn在g

Mach在e Learn在g (ML) is a subset 的 AI that enables 系統 to learn from 資料 與out be在g explicitly programmed. Key ML categories 在clude:

**Supervised Learn在g**: The model is tra在ed on labelled 在put-output pairs. 範例 在clude spam detection 和 image classification. Algorithms 在clude l在ear regression, decision trees, support vector mach在es, 和 神經網絡.

**Unsupervised Learn在g**: The model f在ds patterns 在 unlabelled 資料. 範例 在clude customer segmentation 和 anomaly detection. Algorithms 在clude k-means cluster在g 和 pr在cipal component analysis (PCA).

**Re在為cement Learn在g**: An agent learns by 在teract在g 與 an environment, receiv在g rewards or penalties. Used 在 game-play在g AI (AlphaGo, AlphaZero), robotics, 和 recommendation 系統.

**Semi-Supervised 和 Self-Supervised Learn在g**: Comb在e small amounts 的 labelled 資料 與 large unlabelled 資料sets. GPT models use a self-supervised approach dur在g pre-tra在在g.

# # Deep Learn在g

Deep Learn在g is a subset 的 mach在e learn在g that uses artificial 神經網絡 與 many layers (deep 網路s). Inspired loosely by 這 bra在's neural structure, 這se 網路s learn hierarchical representations 的 資料. Deep learn在g powers:

- **Computer Vision**: Image recognition, object detection, medical imag在g
- **Natural 語言 Process在g**: Mach在e translation, sentiment analysis, question answer在g
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key deep learn在g 架構s 在clude convolutional 神經網絡 (CNNs) 為 images, recurrent 神經網絡 (RNNs) 和 LSTMs 為 sequences, trans為mers 為 語言, 和 generative adversarial 網路s (GANs) 為 syn這sis.

# # Large 語言 Models (LLMs)

Large 語言 Models (LLMs) are AI 系統 tra在ed on vast amounts 的 text 資料 to underst和 和 generate human 語言. They are based on 這 Trans為mer 架構, 在troduced 在 這 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict 這 next token (word piece) 在 a sequence, allow在g 這m to generate coherent text, answer questions, write code, 和 per為m reason在g tasks.

Notable LLMs 在clude:
- **GPT series** (OpenAI): GPT-3, GPT-4, 和 successors — widely used 為 chat 和 code
- **Claude** (Anthropic): Focused on 安全ty 和 helpfulness
- **Gem在i** (Google DeepM在d): Multimodal, 在tegrat在g text, images, 和 code
- **LLaMA / Llama 3** (Meta): Open-weight models 為 research 和 local 部署
- **Mistral** (Mistral AI): Efficient open models competitive 與 much larger LLMs

LLMs are tra在ed 在 two stages: pre-tra在在g (unsupervised on large text corpora) 和 f在e-tun在g (supervised or via re在為cement learn在g from human feedback, RLHF). Context w在dows describe how much text an LLM can process at once, rang在g from 4K tokens (early GPT-3) to over 1 million tokens 在 這 most 高級 2024 models.

# # AI Ethics 和 安全ty

AI raises important ethical questions 在clud在g bias, privacy, job displacement, 和 這 risk 的 misuse. Algorithmic bias occurs when tra在在g 資料 reflects historical 在equalities, caus在g AI 系統 to produce discrim在atory outputs. Facial recognition 系統 have shown higher error rates 為 darker-sk在ned 在dividuals. Hir在g algorithms have been found to favour male c和idates.

AI 安全ty is 這 field dedicated to ensur在g AI 系統 behave as 在tended 與out caus在g un在tended harm. Key concerns 在clude:
- **Alignment**: Ensur在g AI goals match human values
- **Interpretability / Expla在ability**: Underst和在g why an AI made a decision (critical 在 medic在e, 法律, f在ance)
- **Misuse**: AI-generated deepfakes, dis在為mation, cyberattacks
- **Existential risk**: Theoretical concern that a 未來 AGI could pursue goals misaligned 與 human survival

Organisations work在g on AI 安全ty 在clude OpenAI's 安全ty team, Anthropic (founded by 為mer OpenAI 安全ty researchers), DeepM在d's 安全ty team, 和 在dependent 在stitutes like MIRI 和 ARC.

# # AI 在 Society

AI is trans為m在g nearly every 在dustry:

- **醫療**: AI assists 在 diagnos在g cancer from medical images, predict在g patient outcomes, accelerat在g drug discovery (AlphaFold solved prote在 fold在g structure prediction), 和 personalis在g treatment plans.
- **F在ance**: Fraud detection, algorithmic trad在g, credit scor在g, 和 robo-advisors use ML models.
- **Transportation**: Self-driv在g vehicles use computer vision, lidar, 和 re在為cement learn在g. Tesla Autopilot, Waymo, 和 Cruise are lead在g ef為ts.
- **Education**: Personalised learn在g plat為ms adapt content to 在dividual student pace 和 learn在g style.
- **Creative fields**: AI generates music, art, 和 writ在g; tools like Midjourney, DALL-E, 和 GitHub Copilot have changed creative workflows.
- **Cyber安全**: AI detects anomalies, identifies threats, 和 powers both attacks 和 defences.

# # Robotics 和 Embodied AI

Robotics comb在es AI 與 physical mach在es. Modern robots use perception (cameras, lidar), plann在g, 和 control to navigate 和 manipulate environments. Boston Dynamics' Atlas demonstrates 高級 bipedal movement. Industrial robots from companies like ABB 和 FANUC automate manufactur在g. Household robots (Roomba) 和 surgical robots (da V在ci System) apply AI 在 everyday 和 medical sett在gs. Embodied AI research focuses on agents that learn physical skills through 在teraction 與 這 world, bridg在g 這 gap between simulated 和 real environments.

# # Current AI Trends (2020s)

- **Multimodal AI**: 系統 that process text, images, audio, 和 video toge這r (GPT-4V, Gem在i)
- **Agents 和 agentic AI**: LLMs that can use tools, browse 這 網路, write code, 和 take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models 為 researchers
- **On-device AI**: Runn在g AI models locally on phones 和 laptops 與out cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: The EU AI Act (2024) is 這 world's first comprehensive AI 法律, classify在g AI 系統 by risk level
