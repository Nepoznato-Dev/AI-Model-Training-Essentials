# KI und maschinelles Lernen
Eine strukturierte Sammlung von Referenzdokumenten zu den Grundlagen der künstlichen Intelligenz, Modellarchitekturen, ML-Engineering, Sprach- und Bildverarbeitung sowie KI-Ethik – von Kernkonzepten bis hin zum Produktionseinsatz.
## Struktur
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

## Dateien nach Unterkategorie
### Stiftungen
| Datei | Beschreibung |
|------|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| KI-Überblick, ML, Deep Learning, LLMs, Ethik |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| ML-Pipelines, Metriken, Best Practices |
### Modellarchitekturen
| Datei | Beschreibung |
|------|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GANs, VAEs, Diffusionsmodelle, LLMs, generative KI-Anwendungen |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCNs, GATs, Message Passing, Wissensgraphen |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDPs, Q-Learning, Policy Gradients, RLHF, Multi-Agenten-Systeme |
| [recommendation_systems.md](architectures/recommendation_systems.md)| Kollaborative Filterung, inhaltsbasiert, hybrid, Matrixfaktorisierung |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| Dezentrales Training, differenzierter Datenschutz, sichere Aggregation |
### ML-Engineering
| Datei | Beschreibung |
|------|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| Quantisierung, Beschneidung, Destillation, ONNX, Servieren |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| Modellbereitstellung, Register, Bereitstellungsstrategien, Driftüberwachung |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT, Data Lakes, Orchestrierung, Kafka, Feature Stores |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| Lokale KI-Bereitstellungsarchitekturen |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| Modelle lokal ausführen |
### NLP und Sprache
| Datei | Beschreibung |
|------|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| Textverarbeitung, Einbettungen, Transformer, BERT, GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR, TTS, Audiofunktionen, Whisper |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA, Prophet, LSTMs, Saisonalität, Anomalieerkennung |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNNs, Objekterkennung, Segmentierung, Transferlernen |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| Vision-Sprachmodelle, CLIP, DALL-E, modalübergreifendes Lernen |
### Ethik und Sicherheit
| Datei | Beschreibung |
|------|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| KI-Voreingenommenheit, Fairness, Rechenschaftspflicht, Regulierung, Governance |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| Ausrichtungsproblem, RLHF, Interpretierbarkeit, KI-Sicherheitsforschung |
## Empfohlene Lesepfade
### **KI-Anfängerpfad**
1.`foundations/artificial_intelligence.md`– Was ist KI?
2.`foundations/ml_evaluation_and_workflow.md`– Wie ML durchgängig funktioniert
3.`nlp_and_speech/nlp_fundamentals.md`– Text- und Sprachverarbeitung
4.`nlp_and_speech/computer_vision_fundamentals.md`– Bild- und Bildverarbeitung
### **ML-Ingenieurpfad**
1.`foundations/ml_evaluation_and_workflow.md`– ML-Pipelines
2.`engineering/data_engineering_and_pipelines.md`– Dateninfrastruktur
3.`engineering/model_optimization_and_deployment.md`– Modelloptimierung
4.`engineering/ml_engineering_and_mlops.md`– MLOps und Servieren
5.`engineering/local_ai_architecture.md`– Bereitstellungsarchitekturen
### **Forschungspfad**
1.`foundations/artificial_intelligence.md`– Kernkonzepte
2.`architectures/generative_ai_deep_dive.md`– Generative Modelle
3.`architectures/graph_neural_networks.md`– Diagrammbasierte Modelle
4.`architectures/reinforcement_learning.md`– RL und Entscheidungsfindung
5.`ethics_and_safety/ai_safety_and_alignment.md`– Sicherheitsüberlegungen