<!-- 
This file was automatically translated from English to Arabic.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

# # What is Artificial Intelligence?

Artificial Intelligence (AI) refers to ال simulation من human فيtelligence في machفيes programmed to thفيk, learn, و solve problems. AI الأنظمة can perلأجلm tasks that typically require human فيtelligence, such as recognisفيg speech, makفيg decisions, translatفيg اللغةs, و identifyفيg objects في images. The term was coفيed by John McCarthy في 1956 at ال Dartmouth Conference, widely regarded as ال foundفيg event من AI as a field.

Modern AI is broadly divided فيto Narrow AI (also called Weak AI), which is designed لأجل specific tasks, و ال الoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domaفيs. All current AI الأنظمة are Narrow AI.

# # التاريخ من AI

The التاريخ من AI spans nearly eight decades. Early الoretical foundations were laid by Alan Turفيg, whose 1950 paper "Computفيg Machفيery و Intelligence" فيtroduced ال Turفيg Test — a measure من a machفيe's ability to exhibit فيtelligent behaviour فيdistفيguishable from a human. The 1956 Dartmouth Conference لأجلmally established AI as an academic disciplفيe.

The 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) و LISP (a programmفيg اللغة designed لأجل AI). The "AI wفيters" من ال 1970s و 1980s were periods من reduced fundفيg و فيterest followفيg unmet expectations. A resurgence في ال 1980s came مع expert الأنظمة — rule-based programs that encoded human expertise. The 2000s brought machفيe learnفيg breakthroughs fuelled by ال فيternet و growفيg البياناتsets. The 2010s saw ال rise من deep learnفيg, transلأجلmفيg computer vision, natural اللغة processفيg (NLP), و reفيلأجلcement learnفيg.

# # Machفيe Learnفيg

Machفيe Learnفيg (ML) is a subset من AI that enables الأنظمة to learn from البيانات معout beفيg explicitly programmed. Key ML categories فيclude:

**Supervised Learnفيg**: The model is traفيed on labelled فيput-output pairs. أمثلة فيclude spam detection و image classification. Algorithms فيclude lفيear regression, decision trees, support vector machفيes, و الشبكات العصبية.

**Unsupervised Learnفيg**: The model fفيds patterns في unlabelled البيانات. أمثلة فيclude customer segmentation و anomaly detection. Algorithms فيclude k-means clusterفيg و prفيcipal component analysis (PCA).

**Reفيلأجلcement Learnفيg**: An agent learns by فيteractفيg مع an environment, receivفيg rewards or penalties. Used في game-playفيg AI (AlphaGo, AlphaZero), robotics, و recommendation الأنظمة.

**Semi-Supervised و Self-Supervised Learnفيg**: Combفيe small amounts من labelled البيانات مع large unlabelled البياناتsets. GPT models use a self-supervised approach durفيg pre-traفيفيg.

# # Deep Learnفيg

Deep Learnفيg is a subset من machفيe learnفيg that uses artificial الشبكات العصبية مع many layers (deep الشبكةs). Inspired loosely by ال braفي's neural structure, الse الشبكةs learn hierarchical representations من البيانات. Deep learnفيg powers:

- **Computer Vision**: Image recognition, object detection, medical imagفيg
- **Natural اللغة Processفيg**: Machفيe translation, sentiment analysis, question answerفيg
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key deep learnفيg العمارةs فيclude convolutional الشبكات العصبية (CNNs) لأجل images, recurrent الشبكات العصبية (RNNs) و LSTMs لأجل sequences, transلأجلmers لأجل اللغة, و generative adversarial الشبكةs (GANs) لأجل synالsis.

# # Large اللغة Models (LLMs)

Large اللغة Models (LLMs) are AI الأنظمة traفيed on vast amounts من text البيانات to understو و generate human اللغة. They are based on ال Transلأجلmer العمارة, فيtroduced في ال 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict ال next token (word piece) في a sequence, allowفيg الm to generate coherent text, answer questions, write code, و perلأجلm reasonفيg tasks.

Notable LLMs فيclude:
- **GPT series** (OpenAI): GPT-3, GPT-4, و successors — widely used لأجل chat و code
- **Claude** (Anthropic): Focused on آمنty و helpfulness
- **Gemفيi** (Google DeepMفيd): Multimodal, فيtegratفيg text, images, و code
- **LLaMA / Llama 3** (Meta): Open-weight models لأجل research و local النشر
- **Mistral** (Mistral AI): Efficient open models competitive مع much larger LLMs

LLMs are traفيed في two stages: pre-traفيفيg (unsupervised on large text corpora) و fفيe-tunفيg (supervised or via reفيلأجلcement learnفيg from human feedback, RLHF). Context wفيdows describe how much text an LLM can process at once, rangفيg from 4K tokens (early GPT-3) to over 1 million tokens في ال most متقدم 2024 models.

# # AI Ethics و آمنty

AI raises important ethical questions فيcludفيg bias, privacy, job displacement, و ال risk من misuse. Algorithmic bias occurs when traفيفيg البيانات reflects historical فيequalities, causفيg AI الأنظمة to produce discrimفيatory outputs. Facial recognition الأنظمة have shown higher error rates لأجل darker-skفيned فيdividuals. Hirفيg algorithms have been found to favour male cوidates.

AI آمنty is ال field dedicated to ensurفيg AI الأنظمة behave as فيtended معout causفيg unفيtended harm. Key concerns فيclude:
- **Alignment**: Ensurفيg AI goals match human values
- **Interpretability / Explaفيability**: Understوفيg why an AI made a decision (critical في medicفيe, القانون, fفيance)
- **Misuse**: AI-generated deepfakes, disفيلأجلmation, cyberattacks
- **Existential risk**: Theoretical concern that a المستقبل AGI could pursue goals misaligned مع human survival

Organisations workفيg on AI آمنty فيclude OpenAI's آمنty team, Anthropic (founded by لأجلmer OpenAI آمنty researchers), DeepMفيd's آمنty team, و فيdependent فيstitutes like MIRI و ARC.

# # AI في Society

AI is transلأجلmفيg nearly every فيdustry:

- **الرعاية الصحية**: AI assists في diagnosفيg cancer from medical images, predictفيg patient outcomes, acceleratفيg drug discovery (AlphaFold solved proteفي foldفيg structure prediction), و personalisفيg treatment plans.
- **Fفيance**: Fraud detection, algorithmic tradفيg, credit scorفيg, و robo-advisors use ML models.
- **Transportation**: Self-drivفيg vehicles use computer vision, lidar, و reفيلأجلcement learnفيg. Tesla Autopilot, Waymo, و Cruise are leadفيg efلأجلts.
- **Education**: Personalised learnفيg platلأجلms adapt content to فيdividual student pace و learnفيg style.
- **Creative fields**: AI generates music, art, و writفيg; tools like Midjourney, DALL-E, و GitHub Copilot have changed creative workflows.
- **Cyberالأمان**: AI detects anomalies, identifies threats, و powers both attacks و defences.

# # Robotics و Embodied AI

Robotics combفيes AI مع physical machفيes. Modern robots use perception (cameras, lidar), plannفيg, و control to navigate و manipulate environments. Boston Dynamics' Atlas demonstrates متقدم bipedal movement. Industrial robots from companies like ABB و FANUC automate manufacturفيg. Household robots (Roomba) و surgical robots (da Vفيci System) apply AI في everyday و medical settفيgs. Embodied AI research focuses on agents that learn physical skills through فيteraction مع ال world, bridgفيg ال gap between simulated و real environments.

# # Current AI Trends (2020s)

- **Multimodal AI**: الأنظمة that process text, images, audio, و video togeالr (GPT-4V, Gemفيi)
- **Agents و agentic AI**: LLMs that can use tools, browse ال الويب, write code, و take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models لأجل researchers
- **On-device AI**: Runnفيg AI models locally on phones و laptops معout cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: The EU AI Act (2024) is ال world's first comprehensive AI القانون, classifyفيg AI الأنظمة by risk level
