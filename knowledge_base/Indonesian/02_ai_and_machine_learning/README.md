# AI dan Pembelajaran Mesin
Kumpulan dokumen referensi terstruktur yang mencakup dasar-dasar kecerdasan buatan, arsitektur model, teknik ML, pemrosesan bahasa dan visi, serta etika AI — mulai dari konsep inti hingga penerapan produksi.
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

## File berdasarkan Subkategori
### Yayasan
| Berkas | Deskripsi |
|------|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| Ikhtisar AI, ML, pembelajaran mendalam, LLM, etika |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| Pipeline ML, metrik, praktik terbaik |
### Model Arsitektur
| Berkas | Deskripsi |
|------|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GAN, VAE, model difusi, LLM, aplikasi AI generatif |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN, GAT, penyampaian pesan, grafik pengetahuan |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP, Q-learning, gradien kebijakan, RLHF, sistem multi-agen |
| [recommendation_systems.md](architectures/recommendation_systems.md)| Pemfilteran kolaboratif, berbasis konten, hibrid, faktorisasi matriks |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| Pelatihan terdesentralisasi, privasi diferensial, agregasi aman |
### Rekayasa ML
| Berkas | Deskripsi |
|------|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| Kuantisasi, pemangkasan, distilasi, ONNX, penyajian |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| Penyajian model, registrasi, strategi penerapan, pemantauan penyimpangan |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT, data lake, orkestrasi, Kafka, penyimpanan fitur |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| Arsitektur penerapan AI lokal |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| Menjalankan model secara lokal |
### NLP dan Pidato
| Berkas | Deskripsi |
|------|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| Pemrosesan teks, penyematan, Transformers, BERT, GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR, TTS, fitur audio, Bisikan |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA, Nabi, LSTM, musiman, deteksi anomali |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN, deteksi objek, segmentasi, pembelajaran transfer |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| Model bahasa visi, CLIP, DALL-E, pembelajaran lintas modal |
### Etika dan Keamanan
| Berkas | Deskripsi |
|------|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| Bias AI, keadilan, akuntabilitas, regulasi, tata kelola |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| Masalah penyelarasan, RLHF, interpretabilitas, penelitian keamanan AI |
## Jalur Bacaan yang Disarankan
### **Jalur Pemula AI**
1.`foundations/artificial_intelligence.md`— Apa itu AI?
2.`foundations/ml_evaluation_and_workflow.md`— Cara kerja ML secara menyeluruh
3.`nlp_and_speech/nlp_fundamentals.md`— Pemrosesan teks dan bahasa
4.`nlp_and_speech/computer_vision_fundamentals.md`— Pemrosesan gambar dan penglihatan
### **Jalur Insinyur ML**
1.`foundations/ml_evaluation_and_workflow.md`- saluran pipa ML
2.`engineering/data_engineering_and_pipelines.md`— Infrastruktur data
3.`engineering/model_optimization_and_deployment.md`— Pengoptimalan model
4.`engineering/ml_engineering_and_mlops.md`— MLOps dan servis
5.`engineering/local_ai_architecture.md`— Arsitektur penerapan
### **Jalur Penelitian**
1.`foundations/artificial_intelligence.md`— Konsep inti
2.`architectures/generative_ai_deep_dive.md`— Model generatif
3.`architectures/graph_neural_networks.md`— Model berbasis grafik
4.`architectures/reinforcement_learning.md`- RL dan pengambilan keputusan
5.`ethics_and_safety/ai_safety_and_alignment.md`— Pertimbangan keamanan