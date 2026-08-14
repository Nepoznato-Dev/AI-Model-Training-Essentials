---
# Metadata
title: "Artificial Intelligence"
description: "AI overview, ML, deep learning, LLMs, ethics"
category: "AI and Machine Learning"
subcategory: "Foundations"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to foundations/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [artificial, intelligence, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Intelligence artificielle
L'intelligence artificielle est la tentative de construire des machines capables de faire des choses qui nécessiteraient de l'intelligence si un humain les faisait : reconnaître des visages, comprendre la parole, prendre des décisions, écrire des textes, jouer à des jeux, conduire des voitures, diagnostiquer des maladies. Ce domaine est aussi vieux que l'informatique elle-même. Alan Turing se demandait : « Les machines peuvent-elles penser ? » en 1950 – mais la récente explosion des capacités (années 2020) a fait de l’IA l’une des technologies les plus importantes et les plus contestées de l’histoire de l’humanité.
---

## Une brève histoire
L’IA traverse des cycles de battage médiatique et de déception depuis des décennies. Comprendre cette histoire vous aide à comprendre pourquoi les gens sont à la fois enthousiastes et sceptiques.
| Ère | Que s'est-il passé | Résultat |
|-----|---------------|---------|
| **Années 1950-1960** | Un optimisme précoce. Test de Turing proposé (1950). La conférence de Dartmouth crée « l'intelligence artificielle » (1956). Premiers programmes comme ELIZA (chatbot) et SHRDLU (compréhension du langage). | Excitation : « Nous aurons AGI dans une génération ! » |
| **Années 1970** | Premier hiver IA. Les limites des premières approches deviennent claires. Le financement se tarit. | Déception : promesses non tenues |
| **Années 1980** | Boom des systèmes experts : des programmes basés sur des règles qui codaient des connaissances spécialisées humaines. Le projet japonais de cinquième génération. | Encore de l’enthousiasme : les investissements des entreprises dans l’IA |
| **1987-1993** | Deuxième hiver IA. Les systèmes experts s’avèrent fragiles et coûteux à entretenir. | Encore une déception |
| **Années 2000** | L’apprentissage automatique gagne du terrain. Plus de données disponibles (Internet). Les méthodes statistiques remplacent les règles codées à la main. | Des progrès constants |
| **2012+** | Révolution de l'apprentissage profond. AlexNet remporte le concours ImageNet utilisant les GPU. Les réseaux de neurones commencent à surpasser les méthodes traditionnelles en matière de vision, de parole et de langage. | Transformation rapide |
| **2017** | Le document « L'attention est tout ce dont vous avez besoin » présente l'architecture Transformer. | Fondation pour tout ce qui suit |
| **2020-2026** | Grands modèles de langage (GPT-3, GPT-4, Claude, Gemini, LLaMA). L'IA génère du texte, du code, des images et des vidéos. L’adoption par les entreprises s’accélère. | L'IA fait partie de la vie quotidienne |
---

## Comment fonctionne l'IA moderne
### Machine Learning — Apprendre à partir des données
Au lieu de programmer des règles explicites, l’apprentissage automatique transmet les données à des algorithmes qui trouvent eux-mêmes des modèles.
| Tapez | Comment ça marche | Exemple |
|------|-------------|--------------|
| **Apprentissage supervisé** | S'entraîner sur des exemples étiquetés (entrée → sortie correcte) | Détection du spam : alimentez-le en milliers d'e-mails étiquetés "spam" ou "pas spam" |
| **Apprentissage non supervisé** | Rechercher des modèles dans des données non étiquetées | Segmentation client : regrouper les clients similaires sans prédéfinir les groupes |
| **Apprentissage par renforcement** | L'agent apprend par essais et erreurs, recevant des récompenses ou des pénalités | IA de jeu : essayez des mouvements, obtenez des points pour gagner, découvrez quelles stratégies fonctionnent |
### Deep Learning – Réseaux de neurones
L’apprentissage profond utilise des réseaux de neurones artificiels – des couches d’opérations mathématiques simples qui, empilées ensemble, peuvent apprendre des modèles incroyablement complexes. Le « profond » fait référence au nombre de couches.
Architectures clés :
| Architecture | Meilleur chez | Utilisation dans le monde réel |
|-------------|---------|----------------|
| **CNN** (Réseau de neurones convolutifs) | Images et données spatiales | Reconnaissance faciale, imagerie médicale, voitures autonomes |
| **RNN/LSTM** | Données séquentielles (séries chronologiques) | Reconnaissance vocale, génération de musique (largement remplacée par Transformers) |
| **Transformateur** | Tout — texte, images, audio, code | GPT, Claude, Gemini, BERT, DALL-E — l'architecture dominante |
| **GAN** (Réseau Adversaire Génératif) | Générer des données réalistes | Synthèse d'images, transfert de style (partiellement remplacé par des modèles de diffusion) |
| **Modèles à diffusion** | Génération d'images/vidéos de haute qualité | Diffusion stable, DALL-E 3, Midjourney, Sora |
### Grands modèles linguistiques (LLM)
Les LLM sont des modèles basés sur Transformer et entraînés sur d'énormes quantités de texte. Ils apprennent à prédire le prochain jeton (morceau de mot) dans une séquence, ce qui s'avère nécessiter une compréhension de la grammaire, des faits, du raisonnement et même de quelque chose qui ressemble à une « connaissance ».
| Modèle | Développeur | Caractéristique notable |
|-------|-----------|-----------------|
| **GPT-4 / GPT-4o** | OpenAI | Multimodal (texte + images) ; raisonnement fort |
| **Claude** | Anthropique | Mettre l'accent sur la sécurité et la serviabilité ; longues fenêtres contextuelles |
| **Gémeaux** | Google DeepMind | Nativement multimodal ; intégré aux services Google |
| **LLaMA / Lama 3** | Méta | Poids ouvert ; peut être exécuté localement ; grande communauté |
| **Mistral** | Mistral IA | Des modèles ouverts efficaces compétitifs par rapport à des modèles beaucoup plus grands |
**Processus de formation** :
1. **Pré-formation** : apprenez à partir de données textuelles massives (prédiction des prochains jetons). C'est là que le modèle acquiert des « connaissances ».
2. **Peaufinage** : Entraînez-vous sur des tâches spécifiques ou avec des préférences humaines.
3. **RLHF** (Reinforcement Learning from Human Feedback) : les humains évaluent les résultats du modèle ; le modèle apprend à produire les résultats que les humains préfèrent.
Les **fenêtres contextuelles** (la quantité de texte que le modèle peut traiter simultanément) sont passées de jetons 4K (au début de GPT-3) à plus d'un million de jetons dans les modèles 2026.
---

## Ce que l'IA peut et ne peut pas faire
### Capacités actuelles
| Tâche | Performances | Limites |
|------|-------------|-------------|
| **Génération de texte** | Excellent — cohérent, contextuel, stylistiquement varié | Peut halluciner (générer de fausses informations en toute confiance) |
| **Génération de code** | Très bon pour les modèles courants ; peut écrire des programmes entiers | Luttes avec de nouvelles architectures ; peut introduire des bugs subtils |
| **Génération d'images** | Photoréaliste ; styles artistiques; édition | Les mains et le texte sont encore imparfaits ; a du mal avec un raisonnement spatial précis |
| **Traduction** | Quasi-humain pour les principales paires de langues | Les langues à faibles ressources sont moins précises ; la nuance culturelle peut être perdue |
| **Reconnaissance vocale** | Presque humain dans un son clair | Luttes avec des accents lourds, des bruits de fond |
| **Raisonnement** | S'améliorer rapidement ; peut résoudre de nombreux problèmes logiques | Échoue sur des problèmes nouveaux nécessitant une véritable compréhension |
| **Mathématiques** | Bon pour les problèmes standards | Fait des erreurs sur les nouvelles preuves ; ne remplace pas la vérification formelle |
| **Planification et utilisation des outils** | Émergents (agents) | Toujours peu fiable pour les tâches complexes en plusieurs étapes sans surveillance humaine |
### Ce que l'IA ne peut pas faire (à partir de 2026)
- **Comprendre vraiment** tout ce qui se passe dans la manière dont les humains le font : ils traitent des modèles, sans signification
- **Garantir l'exactitude des faits** — l'hallucination reste un problème non résolu
- **Remplacer le jugement humain** dans les décisions à enjeux élevés sans surveillance
- **Généraliser parfaitement** à des domaines très différents des données d'entraînement
- **Fonctionner de manière autonome** dans des environnements physiques imprévisibles (la robotique est encore difficile)
---

## Éthique et sécurité de l'IA
L'IA n'est pas neutre. Il reflète les données sur lesquelles il a été formé, les choix de ses développeurs et les incitations des organisations qui le déploient.
### Préoccupations clés
| Problème | Que se passe-t-il | Exemple |
|-------|-------------|---------|
| **Biais** | Les systèmes d'IA reproduisent et amplifient les biais dans les données d'entraînement | Algorithmes de recrutement privilégiant les candidats masculins ; reconnaissance faciale avec des taux d'erreur plus élevés pour les peaux plus foncées |
| **Confidentialité** | IA entraînée sur les données personnelles ; capacités de surveillance | Formation sur les œuvres protégées par le droit d'auteur ; reconnaissance faciale dans les espaces publics |
| **Utilisation abusive** | Deepfakes, désinformation, phishing automatisé | Fausses vidéos de politiciens générées par l’IA ; appels frauduleux automatisés |
| **Déplacement d'emploi** | Automatisation de tâches auparavant effectuées par des humains | Création de contenu, service client, saisie de données, un peu de programmation |
| **Alignement** | S'assurer que les objectifs de l'IA correspondent aux valeurs humaines | Une IA chargée de « maximiser la production de trombones » pourrait convertir toute la matière en trombones |
| **Risque existentiel** | Préoccupation théorique concernant le futur AGI | Débat entre chercheurs : certains le jugent urgent, d'autres prématuré |
### Qui travaille sur la sécurité
- **Anthropic** — fondé par d'anciens chercheurs d'OpenAI spécifiquement axés sur la sécurité de l'IA
- **DeepMind Safety** — équipe de recherche au sein de Google DeepMind
- **MIRI** (Machine Intelligence Research Institute) — recherche théorique sur la sécurité
- **ARC** (AI Research Center) — recherche empirique sur la sécurité
- **Organismes gouvernementaux** — EU AI Act (2026), décrets américains, cadres internationaux
---

## L'IA en pratique – Industrie par industrie
| Industrie | Demande | Maturité |
|--------------|-------------|--------------|
| **Soins de santé** | Diagnostiquer le cancer à partir d'images ; découverte de médicaments (AlphaFold); prédire les résultats pour les patients | Déployé et en expansion |
| **Finances** | Détection de fraude, trading algorithmique, notation de crédit, robots-conseillers | Largement déployé |
| **Transport** | Véhicules autonomes (Waymo, Tesla Autopilot) ; optimisation des itinéraires | Partiellement déployé ; une autonomie totale encore limitée |
| **Éducation** | Apprentissage personnalisé ; Tutorat en IA ; classement automatisé | Croissance rapide |
| **Champs créatifs** | Génération d'images (Midjourney, DALL-E); musique; aide à la rédaction; achèvement du code | Transformer les flux de travail maintenant |
| **Cybersécurité** | Détection des menaces ; identification des anomalies ; à la fois attaques et défenses | Course aux armements en cours |
| **Légal** | Analyse du contrat ; examen de documents ; recherche juridique | Être adopté ; problèmes de précision |
| **Agriculture** | Suivi des cultures par satellite/drone ; pulvérisation de précision; prévision du rendement | Croissance |
| **Fabrication** | Contrôle qualité ; maintenance prédictive ; optimisation de la chaîne d'approvisionnement | Largement déployé |
---

## Robotique et IA incorporée
La robotique combine l'IA et les machines physiques. Malgré des décennies de progrès, l’interaction physique avec le monde reste bien plus difficile que l’intelligence numérique.
- **Atlas de Boston Dynamics** — mouvement bipède avancé ; parkour; tâches d'entrepôt
- **Robots industriels** (ABB, FANUC, KUKA) — automatisent la fabrication ; soudage; assemblage
- **Robots chirurgicaux** (système da Vinci) — chirurgie mini-invasive avec une précision dépassant les mains humaines
- **Robots domestiques** (Roomba) — simples mais commercialement réussis
- **Robots humanoïdes** (Tesla Optimus, Figure AI) — émergents ; les tâches physiques générales restent très difficiles
L’écart entre l’IA numérique (qui a fait d’énormes progrès) et l’IA physique (qui lutte avec la dextérité, l’équilibre et les environnements imprévisibles) est l’un des grands défis du domaine.
---

## Tendances actuelles (années 2020)
| Tendance | Que se passe-t-il |
|-------|---------|
| **IA multimodale** | Systèmes qui traitent ensemble le texte, les images, l'audio et la vidéo (GPT-4V, Gemini) |
| **Agents** | LLM capables d'utiliser des outils, de naviguer sur le Web, d'écrire du code et d'effectuer des actions en plusieurs étapes |
| **Modèles à poids ouvert** | LLaMA de Meta et d'autres démocratisent l'accès aux grands modèles |
| **IA sur l'appareil** | Exécution de modèles localement sur des téléphones et des ordinateurs portables (Apple Intelligence, Qualcomm NPU) |
| **Réglementation IA** | Loi de l’UE sur l’IA (2026) – première loi globale sur l’IA ; systèmes de classification par niveau de risque |
| **L'IA dans la science** | Repliement de protéines (AlphaFold), découverte de matériaux, modélisation climatique, preuves mathématiques |
| **Petits modèles de langage** | Modèles efficaces fonctionnant sur du matériel grand public ; qualité proche des modèles plus grands |
---

## Résumé
L’IA constitue jusqu’à présent le développement technologique le plus important du 21e siècle. Ce n’est pas de la magie : il s’agit d’une correspondance de modèles à grande échelle, rendue possible par des données massives, un matériel puissant et des architectures intelligentes. Ce qui le rend transformateur, c’est que la correspondance de modèles, suffisamment bien réalisée, peut reproduire de nombreuses tâches qui nécessitaient auparavant l’intelligence humaine. Les défis sont tout aussi importants : hallucinations, préjugés, suppression d’emplois, utilisation abusive et question ouverte de savoir si le chemin entre l’IA étroite et l’intelligence générale est court ou incroyablement long. Ce qui est clair, c’est que l’IA va remodeler chaque industrie, chaque profession et chaque aspect de la vie quotidienne. Comprendre comment cela fonctionne – et ce qu’il ne peut pas faire – est essentiel pour naviguer dans le monde que nous construisons.