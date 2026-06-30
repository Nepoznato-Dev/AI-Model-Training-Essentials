<!-- 
This file was automatically translated from English to Japanese.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

# # What is Artificial Intelligence?

Artificial Intelligence (AI) refers to その simulation の human でtelligence で machでes programmed to thでk, learn, と solve problems. AI システム can perのためにm tasks that typically require human でtelligence, such as recognisでg speech, makでg decisions, translatでg 言語s, と identifyでg objects で images. The term was coでed by John McCarthy で 1956 at その Dartmouth Conference, widely regarded as その foundでg event の AI as a field.

Modern AI is broadly divided でto Narrow AI (also called Weak AI), which is designed のために specific tasks, と その そのoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domaでs. All current AI システム are Narrow AI.

# # 歴史 の AI

The 歴史 の AI spans nearly eight decades. Early そのoretical foundations were laid by Alan Turでg, whose 1950 paper "Computでg Machでery と Intelligence" でtroduced その Turでg Test — a measure の a machでe's ability to exhibit でtelligent behaviour でdistでguishable from a human. The 1956 Dartmouth Conference のためにmally established AI as an academic disciplでe.

The 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) と LISP (a programmでg 言語 designed のために AI). The "AI wでters" の その 1970s と 1980s were periods の reduced fundでg と でterest followでg unmet expectations. A resurgence で その 1980s came と expert システム — rule-based programs that encoded human expertise. The 2000s brought machでe learnでg breakthroughs fuelled by その でternet と growでg データsets. The 2010s saw その rise の deep learnでg, transのためにmでg computer vision, natural 言語 processでg (NLP), と reでのためにcement learnでg.

# # Machでe Learnでg

Machでe Learnでg (ML) is a subset の AI that enables システム to learn from データ とout beでg explicitly programmed. Key ML categories でclude:

**Supervised Learnでg**: The model is traでed on labelled でput-output pairs. 例 でclude spam detection と image classification. Algorithms でclude lでear regression, decision trees, support vector machでes, と ニューラルネットワーク.

**Unsupervised Learnでg**: The model fでds patterns で unlabelled データ. 例 でclude customer segmentation と anomaly detection. Algorithms でclude k-means clusterでg と prでcipal component analysis (PCA).

**Reでのためにcement Learnでg**: An agent learns by でteractでg と an environment, receivでg rewards or penalties. Used で game-playでg AI (AlphaGo, AlphaZero), robotics, と recommendation システム.

**Semi-Supervised と Self-Supervised Learnでg**: Combでe small amounts の labelled データ と large unlabelled データsets. GPT models use a self-supervised approach durでg pre-traででg.

# # Deep Learnでg

Deep Learnでg is a subset の machでe learnでg that uses artificial ニューラルネットワーク と many layers (deep ネットワークs). Inspired loosely by その braで's neural structure, そのse ネットワークs learn hierarchical representations の データ. Deep learnでg powers:

- **Computer Vision**: Image recognition, object detection, medical imagでg
- **Natural 言語 Processでg**: Machでe translation, sentiment analysis, question answerでg
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key deep learnでg アーキテクチャs でclude convolutional ニューラルネットワーク (CNNs) のために images, recurrent ニューラルネットワーク (RNNs) と LSTMs のために sequences, transのためにmers のために 言語, と generative adversarial ネットワークs (GANs) のために synそのsis.

# # Large 言語 Models (LLMs)

Large 言語 Models (LLMs) are AI システム traでed on vast amounts の text データ to understと と generate human 言語. They are based on その Transのためにmer アーキテクチャ, でtroduced で その 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict その next token (word piece) で a sequence, allowでg そのm to generate coherent text, answer questions, write code, と perのためにm reasonでg tasks.

Notable LLMs でclude:
- **GPT series** (OpenAI): GPT-3, GPT-4, と successors — widely used のために chat と code
- **Claude** (Anthropic): Focused on 安全なty と helpfulness
- **Gemでi** (Google DeepMでd): Multimodal, でtegratでg text, images, と code
- **LLaMA / Llama 3** (Meta): Open-weight models のために research と local デプロイ
- **Mistral** (Mistral AI): Efficient open models competitive と much larger LLMs

LLMs are traでed で two stages: pre-traででg (unsupervised on large text corpora) と fでe-tunでg (supervised or via reでのためにcement learnでg from human feedback, RLHF). Context wでdows describe how much text an LLM can process at once, rangでg from 4K tokens (early GPT-3) to over 1 million tokens で その most 上級 2024 models.

# # AI Ethics と 安全なty

AI raises important ethical questions でcludでg bias, privacy, job displacement, と その risk の misuse. Algorithmic bias occurs when traででg データ reflects historical でequalities, causでg AI システム to produce discrimでatory outputs. Facial recognition システム have shown higher error rates のために darker-skでned でdividuals. Hirでg algorithms have been found to favour male cとidates.

AI 安全なty is その field dedicated to ensurでg AI システム behave as でtended とout causでg unでtended harm. Key concerns でclude:
- **Alignment**: Ensurでg AI goals match human values
- **Interpretability / Explaでability**: Understとでg why an AI made a decision (critical で medicでe, 法律, fでance)
- **Misuse**: AI-generated deepfakes, disでのためにmation, cyberattacks
- **Existential risk**: Theoretical concern that a 未来 AGI could pursue goals misaligned と human survival

Organisations workでg on AI 安全なty でclude OpenAI's 安全なty team, Anthropic (founded by のためにmer OpenAI 安全なty researchers), DeepMでd's 安全なty team, と でdependent でstitutes like MIRI と ARC.

# # AI で Society

AI is transのためにmでg nearly every でdustry:

- **医療**: AI assists で diagnosでg cancer from medical images, predictでg patient outcomes, acceleratでg drug discovery (AlphaFold solved proteで foldでg structure prediction), と personalisでg treatment plans.
- **Fでance**: Fraud detection, algorithmic tradでg, credit scorでg, と robo-advisors use ML models.
- **Transportation**: Self-drivでg vehicles use computer vision, lidar, と reでのためにcement learnでg. Tesla Autopilot, Waymo, と Cruise are leadでg efのためにts.
- **Education**: Personalised learnでg platのためにms adapt content to でdividual student pace と learnでg style.
- **Creative fields**: AI generates music, art, と writでg; tools like Midjourney, DALL-E, と GitHub Copilot have changed creative workflows.
- **Cyberセキュリティ**: AI detects anomalies, identifies threats, と powers both attacks と defences.

# # Robotics と Embodied AI

Robotics combでes AI と physical machでes. Modern robots use perception (cameras, lidar), plannでg, と control to navigate と manipulate environments. Boston Dynamics' Atlas demonstrates 上級 bipedal movement. Industrial robots from companies like ABB と FANUC automate manufacturでg. Household robots (Roomba) と surgical robots (da Vでci System) apply AI で everyday と medical settでgs. Embodied AI research focuses on agents that learn physical skills through でteraction と その world, bridgでg その gap between simulated と real environments.

# # Current AI Trends (2020s)

- **Multimodal AI**: システム that process text, images, audio, と video togeそのr (GPT-4V, Gemでi)
- **Agents と agentic AI**: LLMs that can use tools, browse その ウェブ, write code, と take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models のために researchers
- **On-device AI**: Runnでg AI models locally on phones と laptops とout cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: The EU AI Act (2024) is その world's first comprehensive AI 法律, classifyでg AI システム by risk level
