<!-- 
Ce fichier a été automatiquement traduit de l'anglais vers le français.
Source: artificial_intelligence.md
Note: Les termes techniques, exemples de code et noms propres peuvent rester en anglais.
Pour améliorer la précision, veuillez contribuer aux modifications via des pull requests.
-->

# Intelligence Artificielle

## Qu'est-ce que l'Intelligence Artificielle ?

L'Intelligence Artificielle (IA) fait référence à la simulation de l'intelligence humaine dans des machines programmées pour penser, apprendre et résoudre des problèmes. Les systèmes d'IA peuvent effectuer des tâches qui nécessitent généralement l'intelligence humaine, telles que reconnaître la parole, prendre des décisions, traduire des langues et identifier des objets dans des images. Le terme a été inventé par John McCarthy en 1956 lors de la conférence de Dartmouth, largement considérée comme l'événement fondateur de l'IA en tant que domaine.

L'IA moderne est largement divisée entre l'IA Étroite (également appelée IA Faible), conçue pour des tâches spécifiques, et l'Intelligence Artificielle Générale (IAG) théorique, qui égalerait ou dépasserait les capacités cognitives humaines dans tous les domaines. Toutes les IA actuelles sont des IA Étroites.

## Histoire de l'IA

L'histoire de l'IA s'étend sur près de huit décennies. Les premiers fondements théoriques ont été posés par Alan Turing, dont l'article de 1950 « Computing Machinery and Intelligence » a présenté le Test de Turing — une mesure de la capacité d'une machine à exhiber un comportement intelligent indiscernable de celui d'un humain. La conférence de Dartmouth de 1956 a officiellement établi l'IA en tant que discipline académique.

Les années 1950-1970 ont vu des programmes optimistes comme ELIZA (un chatbot simple) et LISP (un langage de programmation conçu pour l'IA). Les « hivers de l'IA » des années 1970 et 1980 ont été des périodes de réduction du financement et de l'intérêt suite à des attentes non satisfaites. Une résurgence dans les années 1980 est venue avec les systèmes experts — des programmes basés sur des règles qui encodaient l'expertise humaine. Les années 2000 ont apporté des percées en apprentissage automatique alimentées par Internet et la croissance des jeux de données. Les années 2010 ont vu l'essor de l'apprentissage profond, transformant la vision par ordinateur, le traitement du langage naturel (NLP) et l'apprentissage par renforcement.

## Apprentissage Automatique

L'Apprentissage Automatique (Machine Learning - ML) est un sous-ensemble de l'IA qui permet aux systèmes d'apprendre à partir de données sans être explicitement programmés. Les principales catégories de ML comprennent :

**Apprentissage Supervisé** : Le modèle est entraîné sur des paires entrée-sortie étiquetées. Les exemples incluent la détection de spam et la classification d'images. Les algorithmes incluent la régression linéaire, les arbres de décision, les machines à vecteurs de support et les réseaux de neurones.

**Apprentissage Non Supervisé** : Le modèle trouve des motifs dans des données non étiquetées. Les exemples incluent la segmentation client et la détection d'anomalies. Les algorithmes incluent le clustering k-means et l'analyse en composantes principales (ACP).

**Apprentissage par Renforcement** : Un agent apprend en interagissant avec un environnement, recevant des récompenses ou des pénalités. Utilisé dans l'IA de jeu (AlphaGo, AlphaZero), la robotique et les systèmes de recommandation.

**Apprentissage Semi-Supervisé et Auto-Supervisé** : Combine de petites quantités de données étiquetées avec de grands ensembles de données non étiquetées. Les modèles GPT utilisent une approche auto-supervisée pendant le pré-entraînement.

## Apprentissage Profond

L'Apprentissage Profond (Deep Learning) est un sous-ensemble de l'apprentissage automatique qui utilise des réseaux de neurones artificiels avec de nombreuses couches (réseaux profonds). Inspirés vaguement par la structure neuronale du cerveau, ces réseaux apprennent des représentations hiérarchiques des données. L'apprentissage profond alimente :

- **Vision par Ordinateur** : Reconnaissance d'images, détection d'objets, imagerie médicale
- **Traitement du Langage Naturel** : Traduction automatique, analyse de sentiment, réponse aux questions
- **Reconnaissance Vocale** : Assistants vocaux comme Siri, Alexa, Google Assistant
- **IA Générative** : Génération d'images (DALL-E, Stable Diffusion), génération de texte (GPT)

Les architectures clés d'apprentissage profond incluent les réseaux de neurones convolutifs (CNN) pour les images, les réseaux de neurones récurrents (RNN) et les LSTM pour les séquences, les transformers pour le langage, et les réseaux antagonistes génératifs (GAN) pour la synthèse.

## Modèles de Langage à Grande Échelle (LLM)

Les Modèles de Langage à Grande Échelle (Large Language Models - LLM) sont des systèmes d'IA entraînés sur de vastes quantités de données textuelles pour comprendre et générer du langage humain. Ils sont basés sur l'architecture Transformer, présentée dans l'article de 2017 « Attention is All You Need » de Vaswani et al. Les LLM prédisent le prochain token (morceau de mot) dans une séquence, leur permettant de générer du texte cohérent, de répondre à des questions, d'écrire du code et d'effectuer des tâches de raisonnement.

Les LLM notables incluent :
- **Série GPT** (OpenAI) : GPT-3, GPT-4 et successeurs — largement utilisés pour le chat et le code
- **Claude** (Anthropic) : Axé sur la sécurité et l'utilité
- **Gemini** (Google DeepMind) : Multimodal, intégrant texte, images et code
- **LLaMA / Llama 3** (Meta) : Modèles open-weight pour la recherche et le déploiement local
- **Mistral** (Mistral AI) : Modèles open efficaces compétitifs avec des LLM beaucoup plus grands

Les LLM sont entraînés en deux étapes : le pré-entraînement (non supervisé sur de grands corpus de texte) et l'affinage (supervisé ou via apprentissage par renforcement à partir de retours humains, RLHF). Les fenêtres de contexte décrivent la quantité de texte qu'un LLM peut traiter à la fois, allant de 4K tokens (GPT-3 précoce) à plus d'un million de tokens dans les modèles les plus avancés de 2024.

## Éthique et Sécurité de l'IA

L'IA soulève d'importantes questions éthiques, notamment les biais, la vie privée, le déplacement d'emplois et le risque de mauvaise utilisation. Le biais algorithmique se produit lorsque les données d'entraînement reflètent des inégalités historiques, amenant les systèmes d'IA à produire des résultats discriminatoires. Les systèmes de reconnaissance faciale ont montré des taux d'erreur plus élevés pour les individus à la peau plus foncée. Des algorithmes d'embauche ont été trouvés favorisant les candidats masculins.

La sécurité de l'IA est le domaine dédié à garantir que les systèmes d'IA se comportent comme prévu sans causer de dommages involontaires. Les principales préoccupations incluent :
- **Alignement** : Garantir que les objectifs de l'IA correspondent aux valeurs humaines
- **Interprétabilité / Explicabilité** : Comprendre pourquoi une IA a pris une décision (critique en médecine, droit, finance)
- **Mauvaise Utilisation** : Deepfakes générés par IA, désinformation, cyberattaques
- **Risque Existentiel** : Préoccupation théorique qu'une IAG future pourrait poursuivre des objectifs mal alignés avec la survie humaine

Les organisations travaillant sur la sécurité de l'IA incluent l'équipe de sécurité d'OpenAI, Anthropic (fondée par d'anciens chercheurs en sécurité d'OpenAI), l'équipe de sécurité de DeepMind, et des instituts indépendants comme MIRI et ARC.

## L'IA dans la Société

L'IA transforme presque toutes les industries :

- **Soins de Santé** : L'IA aide à diagnostiquer le cancer à partir d'images médicales, prédire les résultats des patients, accélérer la découverte de médicaments (AlphaFold a résolu la prédiction de la structure de repliement des protéines) et personnaliser les plans de traitement.
- **Finance** : Détection de fraude, trading algorithmique, scoring de crédit et robo-conseillers utilisent des modèles ML.
- **Transport** : Les véhicules autonomes utilisent la vision par ordinateur, le lidar et l'apprentissage par renforcement. Tesla Autopilot, Waymo et Cruise sont des efforts de premier plan.
- **Éducation** : Les plateformes d'apprentissage personnalisé adaptent le contenu au rythme et au style d'apprentissage de chaque élève.
- **Domaines Créatifs** : L'IA génère de la musique, de l'art et de l'écriture ; des outils comme Midjourney, DALL-E et GitHub Copilot ont changé les flux de travail créatifs.
- **Cybersécurité** : L'IA détecte les anomalies, identifie les menaces et alimente à la fois les attaques et les défenses.

## Robotique et IA Embodied

La robotique combine l'IA avec des machines physiques. Les robots modernes utilisent la perception (caméras, lidar), la planification et le contrôle pour naviguer et manipuler des environnements. Atlas de Boston Dynamics démontre un mouvement bipède avancé. Les robots industriels de sociétés comme ABB et FANUC automatisent la fabrication. Les robots domestiques (Roomba) et les robots chirurgicaux (système da Vinci) appliquent l'IA dans des contextes quotidiens et médicaux. La recherche en IA embodied se concentre sur les agents qui apprennent des compétences physiques par interaction avec le monde, comblant l'écart entre les environnements simulés et réels.

## Tendances Actuelles de l'IA (Années 2020)

- **IA Multimodale** : Systèmes traitant texte, images, audio et vidéo ensemble (GPT-4V, Gemini)
- **Agents et IA Agentique** : LLM capables d'utiliser des outils, de naviguer sur le web, d'écrire du code et d'entreprendre des actions multi-étapes (Operator d'OpenAI, Computer Use d'Anthropic)
- **Modèles Open-Weight** : LLaMA de Meta a démocratisé l'accès aux grands modèles pour les chercheurs
- **IA sur Appareil** : Exécution de modèles d'IA localement sur téléphones et ordinateurs portables sans connectivité cloud (Apple Intelligence, NPU Qualcomm)
- **Réglementation de l'IA** : L'EU AI Act (2024) est la première loi complète sur l'IA au monde, classifiant les systèmes d'IA par niveau de risque
