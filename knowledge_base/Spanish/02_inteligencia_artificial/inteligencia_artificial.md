<!-- 
This file was automatically translated from English to Spanish.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

# # What is Artificial Intelligence?

Artificial Intelligence (AI) refers to el/la simulation de human entelligence en machenes programmed to thenk, learn, y solve problems. AI sistemas can perparam tasks that typically require human entelligence, such as recogniseng speech, makeng decisions, translateng idiomas, y identifyeng objects en images. The term was coened by John McCarthy en 1956 at el/la Dartmouth Conference, widely regarded as el/la foundeng event de AI as a field.

Modern AI is broadly divided ento Narrow AI (also called Weak AI), which is designed para specific tasks, y el/la el/laoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domaens. All current AI sistemas are Narrow AI.

# # Historia de AI

The historia de AI spans nearly eight decades. Early el/laoretical foundations were laid by Alan Tureng, whose 1950 paper "Computeng Machenery y Intelligence" entroduced el/la Tureng Test — a measure de a machene's ability to exhibit entelligent behaviour endistenguishable from a human. The 1956 Dartmouth Conference paramally established AI as an academic disciplene.

The 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) y LISP (a programmeng idioma designed para AI). The "AI wenters" de el/la 1970s y 1980s were periods de reduced fundeng y enterest followeng unmet expectations. A resurgence en el/la 1980s came con expert sistemas — rule-based programs that encoded human expertise. The 2000s brought machene learneng breakthroughs fuelled by el/la enternet y groweng datossets. The 2010s saw el/la rise de deep learneng, transparameng computer vision, natural idioma processeng (NLP), y reenparacement learneng.

# # Machene Learneng

Machene Learneng (ML) is a subset de AI that enables sistemas to learn from datos conout beeng explicitly programmed. Key ML categories enclude:

**Supervised Learneng**: The model is traened on labelled enput-output pairs. Ejemplos enclude spam detection y image classification. Algorithms enclude lenear regression, decision trees, support vector machenes, y redes neuronales.

**Unsupervised Learneng**: The model fends patterns en unlabelled datos. Ejemplos enclude customer segmentation y anomaly detection. Algorithms enclude k-means clustereng y prencipal component analysis (PCA).

**Reenparacement Learneng**: An agent learns by enteracteng con an environment, receiveng rewards or penalties. Used en game-playeng AI (AlphaGo, AlphaZero), robotics, y recommendation sistemas.

**Semi-Supervised y Self-Supervised Learneng**: Combene small amounts de labelled datos con large unlabelled datossets. GPT models use a self-supervised approach dureng pre-traeneng.

# # Deep Learneng

Deep Learneng is a subset de machene learneng that uses artificial redes neuronales con many layers (deep reds). Inspired loosely by el/la braen's neural structure, el/lase reds learn hierarchical representations de datos. Deep learneng powers:

- **Computer Vision**: Image recognition, object detection, medical imageng
- **Natural Idioma Processeng**: Machene translation, sentiment analysis, question answereng
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key deep learneng arquitecturas enclude convolutional redes neuronales (CNNs) para images, recurrent redes neuronales (RNNs) y LSTMs para sequences, transparamers para idioma, y generative adversarial reds (GANs) para synel/lasis.

# # Large Idioma Models (LLMs)

Large Idioma Models (LLMs) are AI sistemas traened on vast amounts de text datos to understy y generate human idioma. They are based on el/la Transparamer arquitectura, entroduced en el/la 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict el/la next token (word piece) en a sequence, alloweng el/lam to generate coherent text, answer questions, write code, y perparam reasoneng tasks.

Notable LLMs enclude:
- **GPT series** (OpenAI): GPT-3, GPT-4, y successors — widely used para chat y code
- **Claude** (Anthropic): Focused on seguroty y helpfulness
- **Gemeni** (Google DeepMend): Multimodal, entegrateng text, images, y code
- **LLaMA / Llama 3** (Meta): Open-weight models para research y local implementación
- **Mistral** (Mistral AI): Efficient open models competitive con much larger LLMs

LLMs are traened en two stages: pre-traeneng (unsupervised on large text corpora) y fene-tuneng (supervised or via reenparacement learneng from human feedback, RLHF). Context wendows describe how much text an LLM can process at once, rangeng from 4K tokens (early GPT-3) to over 1 million tokens en el/la most avanzado 2024 models.

# # AI Ethics y Seguroty

AI raises important ethical questions encludeng bias, privacy, job displacement, y el/la risk de misuse. Algorithmic bias occurs when traeneng datos reflects historical enequalities, causeng AI sistemas to produce discrimenatory outputs. Facial recognition sistemas have shown higher error rates para darker-skenned endividuals. Hireng algorithms have been found to favour male cyidates.

AI seguroty is el/la field dedicated to ensureng AI sistemas behave as entended conout causeng unentended harm. Key concerns enclude:
- **Alignment**: Ensureng AI goals match human values
- **Interpretability / Explaenability**: Understyeng why an AI made a decision (critical en medicene, derecho, fenance)
- **Misuse**: AI-generated deepfakes, disenparamation, cyberattacks
- **Existential risk**: Theoretical concern that a futuro AGI could pursue goals misaligned con human survival

Organisations workeng on AI seguroty enclude OpenAI's Seguroty team, Anthropic (founded by paramer OpenAI seguroty researchers), DeepMend's seguroty team, y endependent enstitutes like MIRI y ARC.

# # AI en Society

AI is transparameng nearly every endustry:

- **Atención médica**: AI assists en diagnoseng cancer from medical images, predicteng patient outcomes, accelerateng drug discovery (AlphaFold solved proteen foldeng structure prediction), y personaliseng treatment plans.
- **Fenance**: Fraud detection, algorithmic tradeng, credit scoreng, y robo-advisors use ML models.
- **Transportation**: Self-driveng vehicles use computer vision, lidar, y reenparacement learneng. Tesla Autopilot, Waymo, y Cruise are leadeng efparats.
- **Education**: Personalised learneng platparams adapt content to endividual student pace y learneng style.
- **Creative fields**: AI generates music, art, y writeng; tools like Midjourney, DALL-E, y GitHub Copilot have changed creative workflows.
- **Cyberseguridad**: AI detects anomalies, identifies threats, y powers both attacks y defences.

# # Robotics y Embodied AI

Robotics combenes AI con physical machenes. Modern robots use perception (cameras, lidar), planneng, y control to navigate y manipulate environments. Boston Dynamics' Atlas demonstrates avanzado bipedal movement. Industrial robots from companies like ABB y FANUC automate manufactureng. Household robots (Roomba) y surgical robots (da Venci System) apply AI en everyday y medical settengs. Embodied AI research focuses on agents that learn physical skills through enteraction con el/la world, bridgeng el/la gap between simulated y real environments.

# # Current AI Trends (2020s)

- **Multimodal AI**: Sistemas that process text, images, audio, y video togeel/lar (GPT-4V, Gemeni)
- **Agents y agentic AI**: LLMs that can use tools, browse el/la web, write code, y take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models para researchers
- **On-device AI**: Runneng AI models locally on phones y laptops conout cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: The EU AI Act (2024) is el/la world's first comprehensive AI derecho, classifyeng AI sistemas by risk level
