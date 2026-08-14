# IA et apprentissage automatique
Une collection structurée de documents de référence couvrant les principes fondamentaux de l'intelligence artificielle, les architectures de modèles, l'ingénierie ML, le traitement du langage et de la vision et l'éthique de l'IA, des concepts de base au déploiement en production.
## Structure
```
02_ai_and_machine_learning/
├── README.md                          ← You are here
├── foundations/                       ← Core AI/ML concepts and workflows
│   ├── artificial_intelligence.md        AI overview, ML, deep learning, LLMs
│   └── ml_evaluation_and_workflow.md     ML pipelines, metrics, best practices
├── architectures/                     ← Advanced model types
│   ├── generative_ai_deep_dive.md        GANs, VAEs, diffusion models, LLMs
│   ├── graph_neural_networks.md          GCNs, GATs, knowledge graphs
│   ├── reinforcement_learning.md         MDPs, Q-learning, RLHF, multi-agent
│   ├── recommendation_systems.md         Collaborative filtering, matrix factorisation
│   └── federated_learning_and_privacy.md Decentralised training, differential privacy
├── engineering/                       ← Deployment and infrastructure
│   ├── model_optimization_and_deployment.md  Quantisation, pruning, ONNX, serving
│   ├── ml_engineering_and_mlops.md           Model serving, registries, drift monitoring
│   ├── data_engineering_and_pipelines.md     ETL/ELT, data lakes, Kafka, feature stores
│   ├── local_ai_architecture.md              Local AI deployment architectures
│   └── phi3_and_local_models.md              Running models locally
├── nlp_and_speech/                    ← Language, vision, audio, and sequence models
│   ├── nlp_fundamentals.md               Text processing, embeddings, Transformers
│   ├── speech_and_audio_processing.md    ASR, TTS, Whisper, audio features
│   ├── time_series_and_forecasting.md    ARIMA, Prophet, LSTMs, seasonality
│   ├── computer_vision_fundamentals.md   CNNs, object detection, segmentation
│   └── multimodal_ai.md                  Vision-language models, CLIP, DALL-E
└── ethics_and_safety/                 ← Responsible AI
    ├── ai_ethics_and_governance.md       Bias, fairness, accountability, regulation
    └── ai_safety_and_alignment.md        Alignment problem, RLHF, interpretability
```

## Fichiers par sous-catégorie
### Fondations
| Fichier | Descriptif |
|------|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| Présentation de l'IA, ML, apprentissage profond, LLM, éthique |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| Pipelines ML, métriques, meilleures pratiques |
### Architectures modèles
| Fichier | Descriptif |
|------|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GAN, VAE, modèles de diffusion, LLM, applications d'IA générative |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN, GAT, transmission de messages, graphiques de connaissances |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP, Q-learning, gradients politiques, RLHF, systèmes multi-agents |
| [recommendation_systems.md](architectures/recommendation_systems.md)| Filtrage collaboratif, basé sur le contenu, hybride, factorisation matricielle |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| Formation décentralisée, confidentialité différentielle, agrégation sécurisée |
### Ingénierie ML
| Fichier | Descriptif |
|------|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| Quantification, élagage, distillation, ONNX, portionnement |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| Service de modèles, registres, stratégies de déploiement, surveillance des dérives |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT, lacs de données, orchestration, Kafka, magasins de fonctionnalités |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| Architectures de déploiement d'IA locales |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| Exécuter des modèles localement |
### PNL et parole
| Fichier | Descriptif |
|------|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| Traitement de texte, intégrations, Transformers, BERT, GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR, TTS, fonctionnalités audio, Whisper |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA, Prophet, LSTM, saisonnalité, détection d'anomalies |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN, détection d'objets, segmentation, apprentissage par transfert |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| Modèles vision-langage, CLIP, DALL-E, apprentissage cross-modal |
### Éthique et sécurité
| Fichier | Descriptif |
|------|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| Biais de l'IA, équité, responsabilité, réglementation, gouvernance |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| Problème d'alignement, RLHF, interprétabilité, recherche sur la sécurité de l'IA |
## Chemins de lecture suggérés
### **Parcours IA pour débutants**
1.`foundations/artificial_intelligence.md`— Qu'est-ce que l'IA ?
2.`foundations/ml_evaluation_and_workflow.md`— Comment fonctionne le ML de bout en bout
3.`nlp_and_speech/nlp_fundamentals.md`— Traitement du texte et du langage
4.`nlp_and_speech/computer_vision_fundamentals.md`— Traitement de l'image et de la vision
### **Parcours d'ingénieur ML**
1.`foundations/ml_evaluation_and_workflow.md`— Pipelines ML
2.`engineering/data_engineering_and_pipelines.md`— Infrastructure de données
3.`engineering/model_optimization_and_deployment.md`— Optimisation du modèle
4.`engineering/ml_engineering_and_mlops.md`— MLOps et service
5.`engineering/local_ai_architecture.md`— Architectures de déploiement
### **Chemin de recherche**
1.`foundations/artificial_intelligence.md`— Concepts de base
2.`architectures/generative_ai_deep_dive.md`— Modèles génératifs
3.`architectures/graph_neural_networks.md`— Modèles basés sur des graphiques
4.`architectures/reinforcement_learning.md`— RL et prise de décision
5.`ethics_and_safety/ai_safety_and_alignment.md`— Considérations de sécurité