---
# Métadonnées
titre : « Fondamentaux de la PNL »
description : "Traitement de texte, intégrations, Transformers, BERT, GPT"
catégorie : "IA et Machine Learning"
version : "1.0.0"
statut : "actif"
# Contribution
auteurs :
  - nom : « Équipe de formation des modèles IA »
    email: ""
    rôle : "original_author"
contributeurs : []
journal des modifications :
  - version : "1.0.0"
    date : "05/08/2026"
    auteur : « Équipe de formation des modèles IA »
    modifications : « Ajout des métadonnées de premier plan YAML pour le suivi des contributeurs »
# Révision
créé : "2026-08-05"
last_modified : "05/08/2026"
date_de_revue : "05/02/2027"
review_by : "Équipe de base de connaissances sur l'IA et l'apprentissage automatique"
next_review : "2027-08-05"
#Classement
Mots-clés : [PNL, IA et apprentissage automatique]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "8 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Fondamentaux de la PNL
Le traitement du langage naturel (NLP) est le domaine de l'enseignement aux machines pour comprendre, générer et travailler avec le langage humain. Il alimente les moteurs de recherche, les chatbots, les systèmes de traduction, l'analyse des sentiments et les grands modèles linguistiques (LLM) qui ont transformé l'IA depuis 2020. Ce fichier couvre l'évolution des techniques classiques vers les architectures modernes basées sur Transformer.
---

## Prétraitement du texte
Le texte brut est compliqué. Avant qu’un modèle puisse l’utiliser, il doit être nettoyé et structuré.
| Étape | Ce qu'il fait | Exemple |
|------|-------------|--------------|
| **Tokenisation** | Diviser le texte en jetons (mots, sous-mots ou caractères) | "J'adore la PNL" →`["I", "love", "NLP"]`|
| **Minuscules** | Convertir en minuscule | "Bonjour" → "bonjour" |
| **Suppression des mots d'arrêt** | Supprimer les mots courants (le, est, à) | "le chat assis" → "le chat assis" |
| **Dérivant** | Hacher les terminaisons de mots (brut) | "courir" → "courir" |
| **Lemmatisation** | Réduire sous forme de dictionnaire (contextuel) | "meilleur" → "bien" |
| **Normalisation** | Corriger l'encodage, supprimer les caractères spéciaux, développer les contractions | "ne pas" → "ne pas" |
Les modèles Transformer modernes ignorent souvent la suppression et la racine des mots vides : ils apprennent ces modèles à partir des données.
---

## Représentation textuelle
Les machines ont besoin de chiffres, pas de mots. La façon dont nous représentons le texte en tant que vecteurs est fondamentale.
### Approches classiques
| Méthode | Descriptif | Limitation |
|--------|-------------|---------------|
| **Encodage à chaud** | Chaque mot occupe une position unique dans un immense vecteur | Clairsemé; pas de sens sémantique |
| **Sac de mots (BoW)** | Compter les fréquences des mots ; ignorer l'ordre | Perd complètement l’ordre des mots |
| **TF-IDF** | Pondérer les mots par fréquence dans le document × rareté dans le corpus | Ignore toujours l'ordre et le contexte |
### Intégrations de mots
Les intégrations mappent les mots sur des vecteurs denses où les mots similaires sont proches les uns des autres.
| Modèle | Idée clé |
|-------|--------------|
| **Mot2Vec** (2013) | Prédire le mot à partir du contexte (CBOW) ou le contexte à partir du mot (Skip-gram) |
| **Gant** (2014) | Statistiques globales de cooccurrence → vecteurs denses |
| **FastText** (2016) | Word2Vec + informations sur les sous-mots (gère mieux les mots rares) |
Le fameux exemple :`king - man + woman ≈ queen`. Les intégrations capturent les relations sémantiques.
**Limitation** : les plongements classiques attribuent un vecteur par mot, ils ne peuvent donc pas gérer la polysémie (mots avec des significations multiples). « Banque » dans « rive du fleuve » et « compte bancaire » obtiennent le même vecteur.
---

## Modèles de séquence
Avant Transformers, l’approche standard de la PNL consistait à traiter le texte de manière séquentielle.
| Architecture | Comment ça marche | Force | Faiblesse |
|-------------|-------------|----------|----------|
| **RNN** | Traitez les jetons un par un ; maintenir l'état caché | Gère les entrées de longueur variable | Des dégradés qui disparaissent ; ne peut pas capturer de longues dépendances |
| **LSTM** | RNN avec portes (oubli, entrée, sortie) pour contrôler le flux d'informations | Mieux dans les dépendances à longue portée | Toujours séquentiel ; lent à s'entraîner |
| **GRU** | LSTM simplifié (moins de portes) | Plus rapide que LSTM ; performances similaires | Mêmes limites fondamentales |
Ces modèles traitent le texte de gauche à droite, ce qui signifie qu'ils sont lents à s'entraîner (impossibles de parallélisme) et ont du mal avec les dépendances à longue portée.
---

## Le mécanisme d'attention
L'attention permet à un modèle d'examiner simultanément toutes les positions d'une séquence et de décider lesquelles sont les plus pertinentes pour la prédiction actuelle.
### Aperçu clé
Au lieu de compresser une phrase entière dans un seul état caché (comme le font les RNN), l'attention calcule une somme pondérée de tous les états cachés, où les poids sont appris.
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

| Composant | Rôle |
|---------------|------|
| **Requête (Q)** | Qu'est-ce que je recherche ? |
| **Clé (K)** | Qu'est-ce que je contient ? |
| **Valeur (V)** | Quelles informations dois-je fournir ? |
| **√d_k** | Facteur d'échelle pour éviter les produits à gros points |
---

## L'architecture du transformateur
Le Transformateur (Vaswani et al., 2017 — « L'attention est tout ce dont vous avez besoin ») a entièrement remplacé la récurrence par l'attention. C'est le fondement de pratiquement toute la PNL moderne.
### Architecture
| Composant | Descriptif |
|---------------|-------------|
| **Encodeur** | Lit le texte saisi ; produit des représentations contextuelles |
| **Décodeur** | Génère le texte de sortie ; s'occupe de la sortie de l'encodeur |
| **Attention personnelle** | Chaque jeton s'occupe de tous les autres jetons dans la même séquence |
| **Attention multi-têtes** | Exécutez plusieurs têtes d’attention en parallèle ; capturer différentes relations |
| **Encodage positionnel** | Injecter des informations de position (puisqu'il n'y a pas de récurrence) |
| **Réseau Feed-Forward** | Appliqué à chaque poste indépendamment |
| **Normalisation des calques** | Stabiliser la formation |
| **Connexions résiduelles** | Ignorer les connexions pour le flux dégradé |
### Encodeur uniquement, décodeur uniquement, encodeur-décodeur
| Variante | Architecture | Idéal pour | Exemples |
|---------|-------------|--------------|---------|
| **Encodeur uniquement** | Comprend le texte | Classification, NER, analyse des sentiments | BERT, RoBERTa, DeBERTa |
| **Décodeur uniquement** | Génère du texte | Modèles de langage, chatbots, génération de code | GPT-3/4, LLaMA, Claude |
| **Encodeur-Décodeur** | Transforme le texte | Traduction, résumé | T5, BART, mBART |
---

## Principales familles de modèles
### Famille BERT (encodeur uniquement)
| Modèle | Caractéristique clé |
|-------|-------------|
| **BERT** (2018) | Modèle de langage masqué + prédiction de la phrase suivante |
| **RoBERTa** | NSP supprimé ; entraîné plus longtemps avec plus de données |
| **ALBERT** | Partage de paramètres ; empreinte réduite |
| **DeBERTa** | Attention démêlée ; NLU amélioré |
| **DistilBERT** | 40 % plus petit, 60 % plus rapide, conserve 97 % des performances de BERT |
### Famille GPT (décodeur uniquement)
| Modèle | Paramètres | Remarques |
|-------|-----------|-------|
| **GPT-2** | 1,5 milliards | Les modèles affichés uniquement avec décodeur peuvent générer un texte cohérent |
| **GPT-3** | 175B | Apprentissage en quelques étapes ; incité plutôt que peaufiné |
| **GPT-3.5/GPT-4** | Non divulgué | Adapté aux instructions + RLHF ; conversationnel |
| **LLaMA** (Méta) | 7B-70B | Poids ouvert ; a engendré l'écosystème LLM open source |
| **Mistral / Mixtral** | 7B / 8×7B (MoE) | Modèles ouverts efficaces avec de fortes performances |
---

## Tâches PNL principales
| Tâche | Descriptif | Modèle typique |
|------|-------------|--------------|
| **Classification du texte** | Attribuer une étiquette au texte (spam/non spam, positif/négatif) | BERT, classificateurs affinés |
| **Reconnaissance d'entité nommée (NER)** | Identifier des personnes, des organisations et des lieux dans du texte | Couche BERT + CRF |
| **Analyse des sentiments** | Déterminer le ton émotionnel | BERT affiné ou LLM zéro tir |
| **Traduction automatique** | Traduire entre les langues | T5, mBART, MarianMT |
| **Réponse aux questions** | Répondre aux questions dans le contexte | BERT (extractif), GPT (génératif) |
| **Résumé** | Condenser le texte long | T5, BART, GPT |
| **Génération de texte** | Produire un texte cohérent | GPT-4, LLaMA, Claude |
---

## Réglage fin ou invite
| Approche | Comment ça marche | Quand utiliser |
|--------------|-------------|-------------|
| **Réglage fin** | Mettez à jour les pondérations du modèle sur vos données spécifiques à la tâche | Vous avez étiqueté des données ; besoin de performances maximales |
| **Invite** | Donner les instructions du modèle en langage naturel | Prototypage rapide ; données limitées ; utiliser les LLM |
| **Quelques plans** | Inclure des exemples dans l'invite | Quand vous avez quelques exemples mais pas assez pour peaufiner |
| **LoRA/QLoRA** | Mise au point efficace ; mettre à jour les petites matrices de bas rang | Affinez les grands modèles avec une mémoire GPU limitée |
---

## Outils et cadres
| Outil | Objectif |
|------|--------------|
| **Transformateurs de visage câlins** | Modèles pré-entraînés, tokeniseurs, pipelines de réglage fin |
| **spaCy** | Pipeline NLP de qualité production (tokenisation, NER, POS, dépendance) |
| **NLTK** | Pédagogique; algorithmes PNL classiques |
| **Gensim** | Modélisation de sujets (LDA), incorporations de mots (Word2Vec, Doc2Vec) |
| **LangChain / LlamaIndex** | Cadres pour créer des applications basées sur LLM |
| **vLLM** | Service LLM à haut débit |
| **Tokeniseurs (HF)** | Tokenisation rapide (BPE, WordPièce, SentencePièce) |
---

## Le paysage du LLM
Le paysage NLP moderne est dominé par les grands modèles linguistiques :
| Catégorie | Exemples | Remarques |
|--------------|---------|-------|
| **Propriétaire** | GPT-4, Claude, Gémeaux | Meilleures performances ; Accès API uniquement |
| **Poids ouvert** | LLaMA 3, Mistral, Qwen | Poids disponibles ; exécuter localement |
| **Open source** | Pythie, OPT | Entièrement ouvert (données, poids, code) |
| **Multimodal** | GPT-4V, Gémeaux, LLaVA | Traiter le texte + les images |
| **Spécialisé dans le code** | CodeLlama, StarCoder, Codeur DeepSeek | Formé au code |
| **Petit / Efficace** | Phi-3, Gemma, TinyLlama | Forte performance à petite échelle |
Le domaine évolue rapidement. Ce qui est à la pointe aujourd’hui pourrait être dépassé dans quelques mois. Les fondamentaux – attention, tokenisation, réglage fin, évaluation – restent stables.