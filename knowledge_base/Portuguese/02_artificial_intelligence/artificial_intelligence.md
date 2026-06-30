<!-- 
This file was automatically translated from English to Portuguese.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Artificial Intelligence

# # What is Artificial Intelligence?

Artificial Intelligence (AI) refers to o/a simulation de human emtelligence em machemes programmed to themk, learn, e solve problems. AI sistemas can perparam tasks that typically require human emtelligence, such as recognisemg speech, makemg decisions, translatemg idiomas, e identifyemg objects em images. The term was coemed by John McCarthy em 1956 at o/a Dartmouth Conference, widely regarded as o/a foundemg event de AI as a field.

Modern AI is broadly divided emto Narrow AI (also called Weak AI), which is designed para specific tasks, e o/a o/aoretical Artificial General Intelligence (AGI), which would match or exceed human cognitive ability across all domaems. All current AI sistemas are Narrow AI.

# # História de AI

The história de AI spans nearly eight decades. Early o/aoretical foundations were laid by Alan Turemg, whose 1950 paper "Computemg Machemery e Intelligence" emtroduced o/a Turemg Test — a measure de a macheme's ability to exhibit emtelligent behaviour emdistemguishable from a human. The 1956 Dartmouth Conference paramally established AI as an academic discipleme.

The 1950s–1970s saw optimistic early programs like ELIZA (a simple chatbot) e LISP (a programmemg idioma designed para AI). The "AI wemters" de o/a 1970s e 1980s were periods de reduced fundemg e emterest followemg unmet expectations. A resurgence em o/a 1980s came com expert sistemas — rule-based programs that encoded human expertise. The 2000s brought macheme learnemg breakthroughs fuelled by o/a emternet e growemg dadossets. The 2010s saw o/a rise de deep learnemg, transparamemg computer vision, natural idioma processemg (NLP), e reemparacement learnemg.

# # Macheme Learnemg

Macheme Learnemg (ML) is a subset de AI that enables sistemas to learn from dados comout beemg explicitly programmed. Key ML categories emclude:

**Supervised Learnemg**: The model is traemed on labelled emput-output pairs. Exemplos emclude spam detection e image classification. Algorithms emclude lemear regression, decision trees, support vector machemes, e redes neurais.

**Unsupervised Learnemg**: The model femds patterns em unlabelled dados. Exemplos emclude customer segmentation e anomaly detection. Algorithms emclude k-means clusteremg e premcipal component analysis (PCA).

**Reemparacement Learnemg**: An agent learns by emteractemg com an environment, receivemg rewards or penalties. Used em game-playemg AI (AlphaGo, AlphaZero), robotics, e recommendation sistemas.

**Semi-Supervised e Self-Supervised Learnemg**: Combeme small amounts de labelled dados com large unlabelled dadossets. GPT models use a self-supervised approach duremg pre-traememg.

# # Deep Learnemg

Deep Learnemg is a subset de macheme learnemg that uses artificial redes neurais com many layers (deep redes). Inspired loosely by o/a braem's neural structure, o/ase redes learn hierarchical representations de dados. Deep learnemg powers:

- **Computer Vision**: Image recognition, object detection, medical imagemg
- **Natural Idioma Processemg**: Macheme translation, sentiment analysis, question answeremg
- **Speech Recognition**: Voice assistants like Siri, Alexa, Google Assistant
- **Generative AI**: Image generation (DALL-E, Stable Diffusion), text generation (GPT)

Key deep learnemg arquiteturas emclude convolutional redes neurais (CNNs) para images, recurrent redes neurais (RNNs) e LSTMs para sequences, transparamers para idioma, e generative adversarial redes (GANs) para syno/asis.

# # Large Idioma Models (LLMs)

Large Idioma Models (LLMs) are AI sistemas traemed on vast amounts de text dados to underste e generate human idioma. They are based on o/a Transparamer arquitetura, emtroduced em o/a 2017 paper "Attention is All You Need" by Vaswani et al. LLMs predict o/a next token (word piece) em a sequence, allowemg o/am to generate coherent text, answer questions, write code, e perparam reasonemg tasks.

Notable LLMs emclude:
- **GPT series** (OpenAI): GPT-3, GPT-4, e successors — widely used para chat e code
- **Claude** (Anthropic): Focused on seguroty e helpfulness
- **Gememi** (Google DeepMemd): Multimodal, emtegratemg text, images, e code
- **LLaMA / Llama 3** (Meta): Open-weight models para research e local implantação
- **Mistral** (Mistral AI): Efficient open models competitive com much larger LLMs

LLMs are traemed em two stages: pre-traememg (unsupervised on large text corpora) e feme-tunemg (supervised or via reemparacement learnemg from human feedback, RLHF). Context wemdows describe how much text an LLM can process at once, rangemg from 4K tokens (early GPT-3) to over 1 million tokens em o/a most avançado 2024 models.

# # AI Ethics e Seguroty

AI raises important ethical questions emcludemg bias, privacy, job displacement, e o/a risk de misuse. Algorithmic bias occurs when traememg dados reflects historical emequalities, causemg AI sistemas to produce discrimematory outputs. Facial recognition sistemas have shown higher error rates para darker-skemned emdividuals. Hiremg algorithms have been found to favour male ceidates.

AI seguroty is o/a field dedicated to ensuremg AI sistemas behave as emtended comout causemg unemtended harm. Key concerns emclude:
- **Alignment**: Ensuremg AI goals match human values
- **Interpretability / Explaemability**: Understeemg why an AI made a decision (critical em mediceme, direito, femance)
- **Misuse**: AI-generated deepfakes, disemparamation, cyberattacks
- **Existential risk**: Theoretical concern that a futuro AGI could pursue goals misaligned com human survival

Organisations workemg on AI seguroty emclude OpenAI's Seguroty team, Anthropic (founded by paramer OpenAI seguroty researchers), DeepMemd's seguroty team, e emdependent emstitutes like MIRI e ARC.

# # AI em Society

AI is transparamemg nearly every emdustry:

- **Saúde**: AI assists em diagnosemg cancer from medical images, predictemg patient outcomes, acceleratemg drug discovery (AlphaFold solved proteem foldemg structure prediction), e personalisemg treatment plans.
- **Femance**: Fraud detection, algorithmic trademg, credit scoremg, e robo-advisors use ML models.
- **Transportation**: Self-drivemg vehicles use computer vision, lidar, e reemparacement learnemg. Tesla Autopilot, Waymo, e Cruise are leademg efparats.
- **Education**: Personalised learnemg platparams adapt content to emdividual student pace e learnemg style.
- **Creative fields**: AI generates music, art, e writemg; tools like Midjourney, DALL-E, e GitHub Copilot have changed creative workflows.
- **Cybersegurança**: AI detects anomalies, identifies threats, e powers both attacks e defences.

# # Robotics e Embodied AI

Robotics combemes AI com physical machemes. Modern robots use perception (cameras, lidar), plannemg, e control to navigate e manipulate environments. Boston Dynamics' Atlas demonstrates avançado bipedal movement. Industrial robots from companies like ABB e FANUC automate manufacturemg. Household robots (Roomba) e surgical robots (da Vemci System) apply AI em everyday e medical settemgs. Embodied AI research focuses on agents that learn physical skills through emteraction com o/a world, bridgemg o/a gap between simulated e real environments.

# # Current AI Trends (2020s)

- **Multimodal AI**: Sistemas that process text, images, audio, e video togeo/ar (GPT-4V, Gememi)
- **Agents e agentic AI**: LLMs that can use tools, browse o/a web, write code, e take multi-step actions (OpenAI's Operator, Anthropic Computer Use)
- **Open-weight models**: Meta's LLaMA democratised access to large models para researchers
- **On-device AI**: Runnemg AI models locally on phones e laptops comout cloud connectivity (Apple Intelligence, Qualcomm NPUs)
- **AI regulation**: The EU AI Act (2024) is o/a world's first comprehensive AI direito, classifyemg AI sistemas by risk level
