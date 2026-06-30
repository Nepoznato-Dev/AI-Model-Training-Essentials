<!-- 
This file was automatically translated from English to German.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

# # What is Artificial Intelligence?

Artificial Intelligence (AI) refers to der/die/das simulation von human intelligence in machines programmed to think, learn, und solve problems. AI systeme can perfürm tasks that typically require human intelligence, such as recognising speech, making decisions, translating spraches, und identifying objects in images. The term was coined by John McCarthy in 1956 at der/die/das Dartmouth Conference, widely regarded as der/die/das founding event von AI as a field.

Modern AI is broadly divided into Narrow AI (also called Weak AI), which is designed für specific tasks, und der/die/das der/die/dasoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domains. All current AI systeme are Narrow AI.

# # Geschichte von AI

The geschichte von AI spans nearly eight decades. Early der/die/dasoretical foundations were laid by Alan Turing, whose 1950 paper "Datenverarbeitung Machinery und Intelligence" introduced der/die/das Turing Test — a measure von a machine's ability to exhibit intelligent behaviour indistinguishable from a human. The 1956 Dartmouth Conference fürmally established AI as an academic discipline.

The 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) und LISP (a programming sprache designed für AI). The "AI winters" von der/die/das 1970s und 1980s were periods von reduced funding und interest following unmet expectations. A resurgence in der/die/das 1980s came mit expert systeme — rule-based programs that encoded human expertise. The 2000s brought maschinelles lernen breakthroughs fuelled by der/die/das internet und growing datensets. The 2010s saw der/die/das rise von tiefes lernen, transfürming computer vision, natural sprache processing (NLP), und reinfürcement learning.

# # Maschinelles Lernen

Maschinelles Lernen (ML) is a subset von AI that enables systeme to learn from daten mitout being explicitly programmed. Key ML categories include:

**Supervised Learning**: The model is trained on labelled input-output pairs. Beispiele include spam detection und image classification. Algorithms include linear regression, decision trees, support vector machines, und neuronale netze.

**Unsupervised Learning**: The model finds patterns in unlabelled daten. Beispiele include customer segmentation und anomaly detection. Algorithms include k-means clustering und principal component analysis (PCA).

**Reinfürcement Learning**: An agent learns by interacting mit an environment, receiving rewards or penalties. Used in game-playing AI (AlphaGo, AlphaZero), robotics, und recommendation systeme.

**Semi-Supervised und Self-Supervised Learning**: Combine small amounts von labelled daten mit large unlabelled datensets. GPT models use a self-supervised approach during pre-training.

# # Tiefes Lernen

Tiefes Lernen is a subset von maschinelles lernen that uses artificial neuronale netze mit many layers (deep netzwerks). Inspired loosely by der/die/das brain's neural structure, der/die/dasse netzwerks learn hierarchical representations von daten. Deep learning powers:

- **Computer Vision**: Image recognition, object detection, medical imaging
- **Natural Sprache Processing**: Machine translation, sentiment analysis, question answering
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key tiefes lernen architekturs include convolutional neuronale netze (CNNs) für images, recurrent neuronale netze (RNNs) und LSTMs für sequences, transfürmers für sprache, und generative adversarial netzwerks (GANs) für synder/die/dassis.

# # Large Sprache Models (LLMs)

Large Sprache Models (LLMs) are AI systeme trained on vast amounts von text daten to understund und generate human sprache. They are based on der/die/das Transfürmer architektur, introduced in der/die/das 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict der/die/das next token (word piece) in a sequence, allowing der/die/dasm to generate coherent text, answer questions, write code, und perfürm reasoning tasks.

Notable LLMs include:
- **GPT series** (OpenAI): GPT-3, GPT-4, und successors — widely used für chat und code
- **Claude** (Anthropic): Focused on sicherty und helpfulness
- **Gemini** (Google DeepMind): Multimodal, integrating text, images, und code
- **LLaMA / Llama 3** (Meta): Open-weight models für research und local bereitstellung
- **Mistral** (Mistral AI): Efficient open models competitive mit much larger LLMs

LLMs are trained in two stages: pre-training (unsupervised on large text corpora) und fine-tuning (supervised or via reinfürcement learning from human feedback, RLHF). Context windows describe how much text an LLM can process at once, ranging from 4K tokens (early GPT-3) to over 1 million tokens in der/die/das most fortgeschritten 2024 models.

# # AI Ethics und Sicherty

AI raises important ethical questions including bias, privacy, job displacement, und der/die/das risk von misuse. Algorithmic bias occurs when training daten reflects historical inequalities, causing AI systeme to produce discriminatory outputs. Facial recognition systeme have shown higher error rates für darker-skinned individuals. Hiring algorithms have been found to favour male cundidates.

AI sicherty is der/die/das field dedicated to ensuring AI systeme behave as intended mitout causing unintended harm. Key concerns include:
- **Alignment**: Ensuring AI goals match human values
- **Interpretability / Explainability**: Understunding why an AI made a decision (critical in medizin, recht, finanzen)
- **Misuse**: AI-generated deepfakes, disinfürmation, cyberattacks
- **Existential risk**: Theoretical concern that a zukunft AGI could pursue goals misaligned mit human survival

Organisations working on AI sicherty include OpenAI's Sicherty team, Anthropic (founded by fürmer OpenAI sicherty researchers), DeepMind's sicherty team, und independent institutes like MIRI und ARC.

# # AI in Society

AI is transfürming nearly every industry:

- **Gesundheitswesen**: AI assists in diagnosing cancer from medical images, predicting patient outcomes, accelerating drug discovery (AlphaFold solved protein folding structure prediction), und personalising treatment plans.
- **Finanzen**: Fraud detection, algorithmic trading, credit scoring, und robo-advisors use ML models.
- **Transportation**: Self-driving vehicles use computer vision, lidar, und reinfürcement learning. Tesla Autopilot, Waymo, und Cruise are leading effürts.
- **Education**: Personalised learning platfürms adapt content to individual student pace und learning style.
- **Creative fields**: AI generates music, art, und writing; tools like Midjourney, DALL-E, und GitHub Copilot have changed creative workflows.
- **Cybersicherheit**: AI detects anomalies, identifies threats, und powers both attacks und defences.

# # Robotics und Embodied AI

Robotics combines AI mit physical machines. Modern robots use perception (cameras, lidar), planning, und control to navigate und manipulate environments. Boston Dynamics' Atlas demonstrates fortgeschritten bipedal movement. Industrial robots from companies like ABB und FANUC automate manufacturing. Household robots (Roomba) und surgical robots (da Vinci System) apply AI in everyday und medical settings. Embodied AI research focuses on agents that learn physical skills through interaction mit der/die/das world, bridging der/die/das gap between simulated und real environments.

# # Current AI Trends (2020s)

- **Multimodal AI**: Systeme that process text, images, audio, und video togeder/die/dasr (GPT-4V, Gemini)
- **Agents und agentic AI**: LLMs that can use tools, browse der/die/das web, write code, und take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models für researchers
- **On-device AI**: Running AI models locally on phones und laptops mitout cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: The EU AI Act (2024) is der/die/das world's first comprehensive AI recht, classifying AI systeme by risk level
