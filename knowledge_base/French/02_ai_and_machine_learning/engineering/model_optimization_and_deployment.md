---
# Metadata
title: "Model Optimisation and Deployment"
description: "Quantisation, pruning, distillation, ONNX, serving infrastructure"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [model, optimization, deployment, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Optimisation et déploiement du modèle
La formation d’un grand modèle d’IA est une réussite importante, mais son déploiement efficace est l’endroit où la plupart des efforts d’ingénierie sont nécessaires. Un modèle qui met 10 secondes à répondre ou qui nécessite huit GPU A100 n'est pas pratique pour la plupart des applications réelles. L'optimisation des modèles consiste à créer des modèles plus petits, plus rapides et plus rentables, tout en maintenant une qualité acceptable. Ce dossier couvre la quantification, l'élagage, la distillation et les outils pratiques de déploiement des modèles en production.
---

## Pourquoi optimiser ?
| Préoccupation | Impact |
|---------|--------|
| **Latence** | Les utilisateurs s'attendent à des réponses en moins d'une seconde ; chaque 100 ms supplémentaire perd l'engagement |
| **Coût** | L'inférence GPU coûte cher ; un modèle 70B coûte environ 0,05 à 0,15 $ par million de jetons sur le matériel cloud |
| **Mémoire** | Un modèle 7B en FP32 a besoin de 28 Go de VRAM ; la plupart des GPU grand public ont 8 à 24 Go |
| **Énergie** | Faire fonctionner de grands modèles consomme beaucoup d’électricité ; questions pour le mobile et le Edge |
| **Échelle** | Servir des millions d'utilisateurs nécessite des modèles adaptés au matériel disponible |
---

## Quantification
La quantification réduit la précision des pondérations du modèle de la virgule flottante 32 bits (FP32) à des formats plus petits comme INT8, INT4 ou même inférieurs.
### Formats de précision
| Formater | Bits par poids | Mémoire pour le modèle 7B | Qualité |
|--------|----------------|----------|---------|
| **FP32** | 32 | 28 Go | Ligne de base (pleine précision) |
| **FP16 / BF16** | 16 | 14 Go | Presque identique au FP32 |
| **INT8** | 8 | 7 Go | Très petite perte de qualité |
| **INT4** | 4 | 3,5 Go | Perte de qualité modérée ; toujours utilisable |
| **INT3 / INT2** | 3-2 | 2,6-1,75 Go | Perte de qualité importante ; étape de recherche |
### Méthodes de quantification
| Méthode | Quand ça arrive | Comment ça marche | Qualité |
|--------|----------------|--------------|---------|
| **Quantisation post-formation (PTQ)** | Une fois la formation terminée | Calibrer le modèle sur un petit ensemble de données ; trouver des échelles optimales | Bon pour INT8 ; se dégrade à INT4 |
| **GPTQ** | Après la formation | Quantification INT4 compatible GPU utilisant des informations approximatives de second ordre | Bonne qualité chez INT4 |
| **AWQ** (Quantification du poids sensible à l'activation) | Après la formation | Protéger les poids saillants en fonction des magnitudes d'activation | Mieux que GPTQ à INT4 |
| **GGUF** (format lama.cpp) | Après la formation | Quantification conviviale pour le processeur ; précision mixte par couche | Optimisé pour l'inférence CPU |
| **Formation basée sur la quantification (QAT)** | Pendant la formation | Simulez la quantification pendant l'entraînement pour que le modèle apprenne à s'en sortir | Meilleure qualité ; nécessite une reconversion |
### Impact pratique
| Modèle | Taille FP16 | Taille INT4 | Accélération | Perte de qualité |
|-------|-----------|---------------|---------|-------------|
| **LLaMA 7B** | 14 Go | 3,5 Go | 2-4x | ~1-2% sur les benchmarks |
| **LLaMA 70B** | 140 Go | 35 Go | 2-3x | ~2-3% sur les benchmarks |
---

## Taille
L'élagage supprime les poids ou les neurones inutiles d'un modèle entraîné.
| Tapez | Descriptif | Avantage | Défi |
|------|-------------|-----------|---------------|
| **Non structuré** | Supprimer les poids individuels (mis à zéro) | Taux de compression les plus élevés | Nécessite un support matériel clairsemé |
| **Structuré** | Supprimez des neurones entiers, des têtes d'attention ou des couches | Réduit directement la taille du modèle | Peut perdre plus de qualité |
| **Basé sur la magnitude** | Supprimer les poids avec les plus petites valeurs absolues | Simple; fonctionne bien | Peut manquer de petits poids importants |
| **Basé sur l'importance** | Supprimer les pondérations en fonction de leur contribution à la sortie | Préservation de meilleure qualité | Plus cher à calculer |
### Pipeline d'élagage
| Étape | Descriptif |
|------|-------------|
| 1. Former | Entraîner le modèle complet normalement |
| 2. Notation | Calculer les scores d'importance pour chaque poids/neurone |
| 3. Tailler | Supprimer les éléments les moins importants |
| 4. Affiner | Recycler pour récupérer la précision perdue |
| 5. Répétez | Répéter l'élagage et le réglage fin pour une compression plus élevée |
---

## Distillation des connaissances
Former un petit modèle « étudiant » pour imiter un grand modèle « enseignant ».
| Composant | Rôle |
|---------------|------|
| **Professeur** | Grand modèle de haute qualité |
| **Étudiant** | Petit modèle qui apprend du professeur |
| **Perte par distillation** | L'élève essaie de faire correspondre la distribution des résultats de l'enseignant (étiquettes souples) |
### Types de distillation
| Tapez | Descriptif | Exemple |
|------|-------------|--------------|
| **Basé sur Logit** | L'élève correspond aux probabilités de sortie de l'enseignant | La distillation originale de Hinton |
| **Basé sur les fonctionnalités** | L'élève correspond aux représentations intermédiaires de l'enseignant | FitNets |
| **Basé sur les relations** | L'élève fait correspondre les relations entre les échantillons | RKD (Distillation des connaissances relationnelles) |
| **Sans données** | Aucune donnée de formation originale n'est nécessaire ; utiliser la génération des enseignants | DAFL, DeepInversion |
### Exemples de distillation notables
| Enseignant | Étudiant | Résultat |
|---------|---------|--------|
| **GPT-4** | GPT-3.5-turbo (rumeur) | Modèle plus petit avec une grande partie de la qualité du GPT-4 |
| **BERT-Grand** | DistilBERT | 40 % plus petit, 60 % plus rapide, 97 % des performances de BERT |
| **LLaMA 70B** | LLaMA 7B (par distillation) | Petit modèle open source approchant la qualité du grand modèle |
---

## Optimisations spécifiques au LLM
### Optimisation du cache KV
Les grands modèles de langage mettent en cache les paires clé-valeur des jetons précédents pour éviter le recalcul.
| Techniques | Descriptif | Impact |
|---------------|-------------|--------|
| **Attention multi-requêtes (MQA)** | Toutes les têtes d'attention partagent une paire KV | Réduit la mémoire ; légère perte de qualité |
| **Attention aux requêtes groupées (GQA)** | Des groupes de têtes partagent des paires KV | Équilibre entre MQA et attention standard |
| **Attention fenêtre coulissante** | Ne vous occupez que des derniers jetons W | Réduit la taille du cache KV pour les contextes longs |
### Décodage spéculatif
| Étape | Descriptif |
|------|-------------|
| 1 | Un petit modèle « brouillon » génère rapidement K jetons |
| 2 | Le grand modèle vérifie tous les jetons K en un seul passage |
| 3 | Les jetons acceptés sont conservés ; ceux rejetés sont régénérés |
Résultat : accélération de la génération 2 à 3 fois sans perte de qualité (le grand modèle a toujours le dernier mot).
### Attention éclair
| Fonctionnalité | Descriptif |
|---------|-------------|
| **Problème** | L'attention standard nécessite une mémoire O(n²) pour la matrice d'attention |
| **Solution** | Calculez l’attention en blocs ; ne matérialise jamais la matrice complète en mémoire |
| **Résultat** | 2 à 4 fois plus rapide ; permet des fenêtres contextuelles beaucoup plus longues |
| **Variantes** | Flash Attention 2 (plus rapide), FlashDecoding (optimisé pour l'inférence) |
---

## Cadres de service
| Cadre | Idéal pour | Caractéristique clé |
|-----------|----------|-------------|
| **vLLM** | LLM au service | PagedAttention ; dosage continu ; haut débit |
| **TensorRT-LLM** | Inférence GPU NVIDIA | Performances maximales sur le matériel NVIDIA |
| **lama.cpp** | Inférence CPU et GPU grand public | Exécute des modèles quantifiés sur les ordinateurs portables et les téléphones |
| **Ollama** | Modèle local en cours d'exécution | Wrapper convivial autour de llama.cpp |
| **Serveur d'inférence Triton** | Service multi-framework | Prend en charge TensorFlow, PyTorch, ONNX, TensorRT |
| **TorchServe** | Modèle PyTorch servant | Intégration native de PyTorch |
| **Exécution ONNX** | Inférence multiplateforme | Exécution optimisée sur tout le matériel |
| **BentoML** | Déploiement en production | Indépendant du framework ; s'occupe du conditionnement et du service |
---

## Modèles de déploiement
| Modèle | Descriptif | Quand utiliser |
|---------|-------------|-------------|
| **Déploiement Edge** | Exécuter des modèles sur des téléphones, des appareils IoT ou du matériel embarqué | Faible latence ; hors ligne ; confidentialité |
| **API Cloud** | Héberger des modèles sur des GPU cloud ; servir via API | Calcul maximal ; paiement à l'utilisation |
| **Hybride** | Petit modèle sur appareil ; grand modèle dans le cloud | Le meilleur des deux mondes |
| **Sans serveur** | Échelle à zéro ; payer uniquement lorsqu'il est utilisé | Trafic sporadique ; sensible aux coûts |
| **Inférence par lots** | Traiter les données en masse selon un planning | Quand le temps réel n'est pas nécessaire |
---

## Analyse comparative
| Métrique | Ce qu'il mesure |
|--------|-----------------|
| **Jetons par seconde** | Débit de génération (plus c'est élevé, mieux c'est) |
| **Délai d'obtention du premier jeton (TTFT)** | Latence avant l'apparition du premier jeton de sortie |
| **Latence par requête** | Temps total entre l'entrée et la sortie complète |
| **Utilisation de la mémoire** | VRAM ou RAM consommée lors de l'inférence |
| **Débit** | Requêtes servies par seconde |
| **Coût par million de jetons** | Coût en dollars du traitement d'un million de jetons |
---

## Conseils pratiques
- **Commencez par la quantification.** La quantification INT4 (AWQ ou GPTQ) offre le meilleur compromis qualité/taille. La plupart des modèles 7B fonctionnent confortablement sur un seul GPU grand public à INT4.
- **Utilisez vLLM pour le service LLM.** Il s'agit de l'option open source la plus rapide pour l'inférence LLM à haut débit.
- **Profil avant optimisation.** Mesurez où le temps est réellement passé. C'est souvent la bande passante mémoire, et non le calcul, qui constitue le goulot d'étranglement.
- **Faites correspondre le modèle à la tâche.** Un modèle 7B convient à la plupart des tâches. N'utilisez pas 70B alors que 7B fera l'affaire.
- **Envisagez la distillation.** Si vous avez besoin d'un modèle petit et rapide pour la production, distillez à partir d'un modèle plus grand plutôt que de vous entraîner à partir de zéro.
- **Surveiller en continu.** Les performances du modèle peuvent se dégrader au fil du temps à mesure que la distribution des données évolue. Suivez les mesures de latence, de débit et de qualité.
---

## Résumé
L'optimisation des modèles est le pont entre la recherche et la production. La quantification réduit les modèles de 4 à 8 fois avec une perte de qualité minimale. La taille supprime le poids mort. La distillation transfère les connaissances des grands modèles vers les petits modèles. Les astuces Flash Attention et KV-cache accélèrent l'inférence. Ensemble, ces techniques transforment un modèle nécessitant un centre de données en un modèle fonctionnant sur un ordinateur portable ou un téléphone. Le domaine évolue rapidement : ce qui nécessitait huit A100 l’année dernière fonctionne aujourd’hui sur un GPU grand public.