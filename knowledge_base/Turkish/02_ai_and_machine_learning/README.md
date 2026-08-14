# Yapay Zeka ve Makine Öğrenimi
Temel kavramlardan üretim dağıtımına kadar yapay zekanın temellerini, model mimarilerini, makine öğrenimi mühendisliğini, dil ve görüntü işlemeyi ve yapay zeka etiğini kapsayan yapılandırılmış bir referans belgeleri koleksiyonu.
## Yapı
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

## Alt Kategoriye Göre Dosyalar
### Temeller
| Dosya | Açıklama |
|------|-----------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| Yapay zekaya genel bakış, makine öğrenimi, derin öğrenme, Yüksek Lisans, etik |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| ML ardışık düzenleri, ölçümleri, en iyi uygulamaları |
### Model Mimarileri
| Dosya | Açıklama |
|------|-----------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GAN'lar, VAE'ler, yayılma modelleri, LLM'ler, üretken yapay zeka uygulamaları |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN'ler, GAT'ler, mesaj aktarma, bilgi grafikleri |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP'ler, Q-öğrenme, politika geçişleri, RLHF, çoklu aracı sistemleri |
| [recommendation_systems.md](architectures/recommendation_systems.md)| İşbirlikçi filtreleme, içerik tabanlı, hibrit, matris çarpanlarına ayırma |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| Merkezi olmayan eğitim, farklı gizlilik, güvenli toplama |
### ML Mühendisliği
| Dosya | Açıklama |
|------|-----------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| Niceleme, budama, damıtma, ONNX, servis |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| Model sunumu, kayıtlar, dağıtım stratejileri, sapma izleme |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT, veri gölleri, orkestrasyon, Kafka, özellik depoları |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| Yerel AI dağıtım mimarileri |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| Modelleri yerel olarak çalıştırma |
### NLP ve Konuşma
| Dosya | Açıklama |
|------|-----------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| Metin işleme, yerleştirmeler, Transformatörler, BERT, GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR, TTS, ses özellikleri, Whisper |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA, Peygamber, LSTM'ler, mevsimsellik, anormallik tespiti |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN'ler, nesne algılama, segmentasyon, aktarım öğrenimi |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| Vizyon-dil modelleri, CLIP, DALL-E, modlar arası öğrenme |
### Etik ve Güvenlik
| Dosya | Açıklama |
|------|-----------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| Yapay zeka önyargısı, adalet, hesap verebilirlik, düzenleme, yönetişim |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| Hizalama sorunu, RLHF, yorumlanabilirlik, AI güvenlik araştırması |
## Önerilen Okuma Yolları
### **Yapay Zeka Başlangıç Yolu**
1.`foundations/artificial_intelligence.md`— Yapay zeka nedir?
2.`foundations/ml_evaluation_and_workflow.md`— Makine öğrenimi uçtan uca nasıl çalışır?
3.`nlp_and_speech/nlp_fundamentals.md`— Metin ve dil işleme
4.`nlp_and_speech/computer_vision_fundamentals.md`— Görüntü ve görüntü işleme
### **ML Mühendis Yolu**
1.`foundations/ml_evaluation_and_workflow.md`— ML ardışık düzenleri
2.`engineering/data_engineering_and_pipelines.md`— Veri altyapısı
3.`engineering/model_optimization_and_deployment.md`— Model optimizasyonu
4.`engineering/ml_engineering_and_mlops.md`— MLOps ve sunum
5.`engineering/local_ai_architecture.md`— Dağıtım mimarileri
### **Araştırma Yolu**
1.`foundations/artificial_intelligence.md`— Temel kavramlar
2.`architectures/generative_ai_deep_dive.md`— Üretken modeller
3.`architectures/graph_neural_networks.md`— Grafik tabanlı modeller
4.`architectures/reinforcement_learning.md`— RL ve karar verme
5.`ethics_and_safety/ai_safety_and_alignment.md`— Güvenlik hususları