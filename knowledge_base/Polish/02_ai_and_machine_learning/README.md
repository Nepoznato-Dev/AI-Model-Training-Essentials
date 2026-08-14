# Sztuczna inteligencja i uczenie maszynowe
Ustrukturyzowany zbiór dokumentów referencyjnych obejmujący podstawy sztucznej inteligencji, architektury modeli, inżynierię uczenia maszynowego, przetwarzanie języka i wizji oraz etykę sztucznej inteligencji — od podstawowych koncepcji po wdrożenie produkcyjne.
## Struktura
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

## Pliki według podkategorii
### Fundamenty
| Plik | Opis |
|------|------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| Przegląd AI, ML, głębokie uczenie się, LLM, etyka |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| Potoki ML, metryki, najlepsze praktyki |
### Architektury modeli
| Plik | Opis |
|------|------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GAN, VAE, modele dyfuzyjne, LLM, generatywne zastosowania AI |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN, GAT, przekazywanie komunikatów, wykresy wiedzy |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP, Q-learning, gradienty polityki, RLHF, systemy wieloagentowe |
| [recommendation_systems.md](architectures/recommendation_systems.md)| Filtrowanie oparte na współpracy, oparte na treści, hybrydowe, faktoryzacja macierzowa |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| Zdecentralizowane szkolenie, zróżnicowana prywatność, bezpieczna agregacja |
### Inżynieria ML
| Plik | Opis |
|------|------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| Kwantyzacja, przycinanie, destylacja, ONNX, serwowanie |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| Obsługa modeli, rejestry, strategie wdrażania, monitorowanie dryfu |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT, jeziora danych, orkiestracja, Kafka, sklepy z funkcjami |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| Lokalne architektury wdrażania AI |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| Uruchamianie modeli lokalnie |
### NLP i mowa
| Plik | Opis |
|------|------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| Przetwarzanie tekstu, osadzanie, Transformers, BERT, GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR, TTS, funkcje audio, szept |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA, Prorok, LSTM, sezonowość, wykrywanie anomalii |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN, wykrywanie obiektów, segmentacja, uczenie transferowe |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| Modele wizjonersko-językowe, CLIP, DALL-E, uczenie się międzymodalne |
### Etyka i bezpieczeństwo
| Plik | Opis |
|------|------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| Stronniczość AI, uczciwość, odpowiedzialność, regulacje, zarządzanie |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| Problem dopasowania, RLHF, interpretowalność, badania nad bezpieczeństwem AI |
## Sugerowane ścieżki czytania
### **Ścieżka dla początkujących AI**
1.`foundations/artificial_intelligence.md`— Co to jest sztuczna inteligencja?
2.`foundations/ml_evaluation_and_workflow.md`— Jak kompleksowo działa ML
3.`nlp_and_speech/nlp_fundamentals.md`— Przetwarzanie tekstu i języka
4.`nlp_and_speech/computer_vision_fundamentals.md`— Przetwarzanie obrazu i wizji
### **Ścieżka inżyniera ML**
1.`foundations/ml_evaluation_and_workflow.md`— rurociągi ML
2.`engineering/data_engineering_and_pipelines.md`— Infrastruktura danych
3.`engineering/model_optimization_and_deployment.md`— Optymalizacja modelu
4.`engineering/ml_engineering_and_mlops.md`— MLOps i serwowanie
5.`engineering/local_ai_architecture.md`— Architektury wdrożeniowe
### **Ścieżka badawcza**
1.`foundations/artificial_intelligence.md`— Podstawowe pojęcia
2.`architectures/generative_ai_deep_dive.md`— Modele generatywne
3.`architectures/graph_neural_networks.md`— modele oparte na grafach
4.`architectures/reinforcement_learning.md`— RL i podejmowanie decyzji
5.`ethics_and_safety/ai_safety_and_alignment.md`— Względy bezpieczeństwa