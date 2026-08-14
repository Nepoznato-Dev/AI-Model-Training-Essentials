# Intelligenza artificiale e apprendimento automatico
Una raccolta strutturata di documenti di riferimento che coprono i fondamenti dell'intelligenza artificiale, le architetture dei modelli, l'ingegneria ML, l'elaborazione del linguaggio e della visione e l'etica dell'IA, dai concetti fondamentali all'implementazione della produzione.
## Struttura
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

## File per sottocategoria
### Fondazioni
| File | Descrizione |
|------|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| Panoramica sull'intelligenza artificiale, ML, deep learning, LLM, etica |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| Pipeline ML, metriche, best practice |
### Architetture modello
| File | Descrizione |
|------|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GAN, VAE, modelli di diffusione, LLM, applicazioni di intelligenza artificiale generativa |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN, GAT, scambio di messaggi, grafici della conoscenza |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP, Q-learning, gradienti politici, RLHF, sistemi multi-agente |
| [recommendation_systems.md](architectures/recommendation_systems.md)| Filtraggio collaborativo, basato sul contenuto, ibrido, fattorizzazione a matrice |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| Formazione decentralizzata, privacy differenziale, aggregazione sicura |
### Ingegneria ML
| File | Descrizione |
|------|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| Quantizzazione, potatura, distillazione, ONNX, servizio |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| Serving di modelli, registri, strategie di distribuzione, monitoraggio della deriva |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT, data lake, orchestrazione, Kafka, feature store |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| Architetture di distribuzione dell'intelligenza artificiale locale |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| Esecuzione di modelli localmente |
### PNL e discorso
| File | Descrizione |
|------|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| Elaborazione del testo, incorporamenti, Transformers, BERT, GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR, TTS, funzionalità audio, Whisper |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA, Prophet, LSTM, stagionalità, rilevamento di anomalie |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN, rilevamento di oggetti, segmentazione, trasferimento di apprendimento |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| Modelli visione-linguaggio, CLIP, DALL-E, apprendimento cross-modale |
### Etica e Sicurezza
| File | Descrizione |
|------|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| Pregiudizi sull’intelligenza artificiale, equità, responsabilità, regolamentazione, governance |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| Problema di allineamento, RLHF, interpretabilità, ricerca sulla sicurezza dell'IA |
## Percorsi di lettura consigliati
### **Percorso per principianti AI**
1.`foundations/artificial_intelligence.md`— Cos'è l'intelligenza artificiale?
2. `foundations/ml_evaluation_and_workflow.md`: come funziona il machine learning end-to-end
3. `nlp_and_speech/nlp_fundamentals.md`: elaborazione di testo e lingua
4. `nlp_and_speech/computer_vision_fundamentals.md`: elaborazione di immagini e visione
### **Percorso ML Engineer**
1. `foundations/ml_evaluation_and_workflow.md`: condutture ML
2. `engineering/data_engineering_and_pipelines.md`: infrastruttura dati
3. `engineering/model_optimization_and_deployment.md`: ottimizzazione del modello
4. `engineering/ml_engineering_and_mlops.md`: MLOps e servizio
5. `engineering/local_ai_architecture.md`: architetture di distribuzione
### **Percorso di ricerca**
1. `foundations/artificial_intelligence.md`: concetti fondamentali
2. `architectures/generative_ai_deep_dive.md`: modelli generativi
3. `architectures/graph_neural_networks.md`: modelli basati su grafici
4.`architectures/reinforcement_learning.md`— RL e processo decisionale
5.`ethics_and_safety/ai_safety_and_alignment.md`— Considerazioni sulla sicurezza