<!-- 
This file was automatically translated from English to French.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Intelligence artificielle

## Qu'est-ce que l'intelligence artificielle ?

L'intelligence artificielle (AI) désigne la simulation de l'intelligence humaine par des machines programmées pour penser, apprendre et résoudre des problèmes. Les systèmes d'IA peuvent accomplir des tâches qui exigent habituellement l'intelligence humaine, comme la reconnaissance de la parole, la prise de décision, la traduction de langues et l'identification d'objets dans des images. Le terme a été forgé par John McCarthy en 1956 lors de la conférence de Dartmouth, généralement considérée comme l'acte fondateur de l'IA en tant que discipline.

L'IA moderne se divise largement entre l'IA étroite (ou Weak AI), conçue pour des tâches spécifiques, et l'Artificial General Intelligence (AGI), encore théorique, qui égalerait ou dépasserait les capacités cognitives humaines dans tous les domaines. Tous les systèmes d'IA actuels relèvent de l'IA étroite.

## Histoire de l'IA

L'histoire de l'IA s'étend sur près de huit décennies. Les premières bases théoriques ont été posées par Alan Turing, dont l'article de 1950, "Computing Machinery and Intelligence", a introduit le test de Turing — une mesure de la capacité d'une machine à manifester un comportement intelligent indiscernable de celui d'un humain. La conférence de Dartmouth de 1956 a officiellement établi l'IA comme discipline universitaire.

Les années 1950 à 1970 ont vu naître des programmes pionniers et optimistes comme ELIZA (un chatbot simple) et LISP (un langage de programmation conçu pour l'IA). Les « hivers de l'IA » des années 1970 et 1980 ont été des périodes de baisse du financement et de l'intérêt, après des attentes non satisfaites. Une reprise s'est produite dans les années 1980 avec les systèmes experts — des programmes fondés sur des règles qui encodaient une expertise humaine. Les années 2000 ont apporté des percées en machine learning, alimentées par internet et par l'essor des jeux de données. Les années 2010 ont vu la montée du deep learning, qui a transformé la vision par ordinateur, le traitement automatique du langage naturel (NLP) et l'apprentissage par renforcement.

## Machine learning

Le machine learning (ML) est un sous-domaine de l'IA qui permet aux systèmes d'apprendre à partir de données sans être explicitement programmés. Les principales catégories sont les suivantes :

**Supervised Learning** : le modèle est entraîné sur des paires entrée-sortie étiquetées. Exemples : détection de spam et classification d'images. Les algorithmes incluent la régression linéaire, les arbres de décision, les Support Vector Machines et les réseaux de neurones.

**Unsupervised Learning** : le modèle découvre des motifs dans des données non étiquetées. Exemples : segmentation de clients et détection d'anomalies. Les algorithmes incluent le clustering k-means et l'analyse en composantes principales (PCA).

**Reinforcement Learning** : un agent apprend en interagissant avec un environnement, en recevant des récompenses ou des pénalités. Utilisé dans les IA de jeux (AlphaGo, AlphaZero), la robotique et les systèmes de recommandation.

**Semi-Supervised and Self-Supervised Learning** : combine de petites quantités de données étiquetées avec de vastes ensembles non étiquetés. Les modèles GPT utilisent une approche self-supervised pendant le pré-entraînement.

## Deep learning

Le deep learning est un sous-domaine du machine learning qui utilise des réseaux de neurones artificiels à nombreuses couches (réseaux profonds). Inspirés de manière lointaine par la structure neuronale du cerveau, ces réseaux apprennent des représentations hiérarchiques des données. Le deep learning alimente notamment :

- **Vision par ordinateur** : reconnaissance d'images, détection d'objets, imagerie médicale
- **Traitement du langage naturel** : traduction automatique, analyse de sentiment, question-réponse
- **Reconnaissance vocale** : assistants vocaux comme Siri, Alexa, Google Assistant
- **IA générative** : génération d'images (DALL-E, Stable Diffusion), génération de texte (GPT)

Les principales architectures de deep learning incluent les réseaux de neurones convolutionnels (CNN) pour les images, les réseaux récurrents (RNN) et les LSTM pour les séquences, les transformers pour le langage et les generative adversarial networks (GANs) pour la synthèse.

## Grands modèles de langage (LLMs)

Les grands modèles de langage (LLMs) sont des systèmes d'IA entraînés sur d'immenses volumes de données textuelles afin de comprendre et générer le langage humain. Ils reposent sur l'architecture Transformer, introduite dans l'article de 2017 "Attention is All You Need" de Vaswani et al. Les LLM prédisent le token suivant (fragment de mot) dans une séquence, ce qui leur permet de générer un texte cohérent, de répondre à des questions, d'écrire du code et d'effectuer des tâches de raisonnement.

Parmi les LLM notables, on trouve :
- **GPT series** (OpenAI) : GPT-3, GPT-4 et leurs successeurs — largement utilisés pour la conversation et le code
- **Claude** (Anthropic) : centré sur la sûreté et l'utilité
- **Gemini** (Google DeepMind) : multimodal, intégrant texte, images et code
- **LLaMA / Llama 3** (Meta) : modèles à poids ouverts pour la recherche et le déploiement local
- **Mistral** (Mistral AI) : modèles ouverts efficaces et compétitifs face à des LLM bien plus grands

Les LLM sont entraînés en deux étapes : le pré-entraînement (non supervisé sur de grands corpus textuels) puis le fine-tuning (supervisé ou via reinforcement learning from human feedback, RLHF). Les fenêtres de contexte décrivent la quantité de texte qu'un LLM peut traiter en une fois, allant de 4K tokens (premiers GPT-3) à plus d'un million de tokens pour les modèles les plus avancés de 2026.

## Éthique et sécurité de l'IA

L'IA soulève des questions éthiques importantes, notamment les biais, la vie privée, le remplacement d'emplois et le risque de mésusage. Les biais algorithmiques apparaissent lorsque les données d'entraînement reflètent des inégalités historiques, ce qui conduit les systèmes d'IA à produire des résultats discriminatoires. Des systèmes de reconnaissance faciale ont montré des taux d'erreur plus élevés pour les personnes à la peau plus foncée. Des algorithmes de recrutement ont été observés comme favorisant les candidats masculins.

La sécurité de l'IA est le domaine qui vise à garantir que les systèmes d'IA se comportent comme prévu, sans causer de dommages non intentionnels. Les principales préoccupations incluent :
- **Alignment** : faire en sorte que les objectifs de l'IA correspondent aux valeurs humaines
- **Interpretability / Explainability** : comprendre pourquoi une IA a pris une décision (crucial en médecine, en droit et en finance)
- **Misuse** : deepfakes générés par IA, désinformation, cyberattaques
- **Existential risk** : inquiétude théorique selon laquelle une future AGI pourrait poursuivre des objectifs incompatibles avec la survie humaine

Parmi les organisations qui travaillent sur la sécurité de l'IA figurent l'équipe Safety d'OpenAI, Anthropic (fondée par d'anciens chercheurs en sécurité d'OpenAI), l'équipe safety de DeepMind et des instituts indépendants comme MIRI et ARC.

## L'IA dans la société

L'IA transforme presque tous les secteurs :

- **Santé** : l'IA aide à diagnostiquer des cancers à partir d'images médicales, à prédire l'évolution des patients, à accélérer la découverte de médicaments (AlphaFold a résolu la prédiction de la structure des protéines) et à personnaliser les plans de traitement.
- **Finance** : la détection de fraude, le trading algorithmique, le credit scoring et les robo-advisors utilisent des modèles de ML.
- **Transports** : les véhicules autonomes utilisent la vision par ordinateur, le lidar et l'apprentissage par renforcement. Tesla Autopilot, Waymo et Cruise sont des acteurs majeurs.
- **Éducation** : des plateformes d'apprentissage personnalisées adaptent le contenu au rythme et au style d'apprentissage de chaque élève.
- **Domaines créatifs** : l'IA génère de la musique, de l'art et de l'écriture ; des outils comme Midjourney, DALL-E et GitHub Copilot ont transformé les workflows créatifs.
- **Cybersécurité** : l'IA détecte des anomalies, identifie des menaces et alimente à la fois les attaques et les défenses.

## Robotique et IA incarnée

La robotique combine l'IA et les machines physiques. Les robots modernes utilisent la perception (caméras, lidar), la planification et le contrôle pour naviguer et manipuler leur environnement. Atlas, de Boston Dynamics, illustre un mouvement bipède avancé. Les robots industriels d'entreprises comme ABB et FANUC automatisent la fabrication. Les robots domestiques (Roomba) et les robots chirurgicaux (da Vinci System) appliquent l'IA dans la vie quotidienne et en milieu médical. La recherche en embodied AI s'intéresse à des agents qui apprennent des compétences physiques par interaction avec le monde, en comblant l'écart entre environnements simulés et réels.

## Tendances actuelles de l'IA (années 2020)

- **IA multimodale** : systèmes capables de traiter ensemble texte, images, audio et vidéo (GPT-4V, Gemini)
- **Agents et agentic AI** : LLM capables d'utiliser des outils, de naviguer sur le Web, d'écrire du code et d'accomplir des actions en plusieurs étapes (OpenAI's Operator, Anthropic Computer Use)
- **Modèles à poids ouverts** : LLaMA de Meta a démocratisé l'accès aux grands modèles pour les chercheurs
- **IA sur appareil** : exécution de modèles d'IA localement sur téléphones et ordinateurs portables sans dépendance au cloud (Apple Intelligence, Qualcomm NPUs)
- **Régulation de l'IA** : l'EU AI Act (2026) est la première législation globale de grande ampleur sur l'IA, classant les systèmes selon leur niveau de risque
