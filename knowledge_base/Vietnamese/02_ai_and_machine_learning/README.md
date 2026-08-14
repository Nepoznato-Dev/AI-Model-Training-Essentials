# AI và Học máy
Một bộ sưu tập có cấu trúc gồm các tài liệu tham khảo bao gồm các nguyên tắc cơ bản về trí tuệ nhân tạo, kiến ​​trúc mô hình, kỹ thuật ML, xử lý ngôn ngữ và hình ảnh cũng như đạo đức AI - từ các khái niệm cốt lõi đến triển khai sản xuất.
## Kết cấu
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

## Tệp theo danh mục con
### Nền móng
| Tập tin | Mô tả |
|------|-------------|
| [artificial_intelligence.md](foundations/artificial_intelligence.md)| Tổng quan về AI, ML, học sâu, LLM, đạo đức |
| [ml_evaluation_and_workflow.md](foundations/ml_evaluation_and_workflow.md)| Quy trình ML, số liệu, phương pháp hay nhất |
### Kiến trúc mô hình
| Tập tin | Mô tả |
|------|-------------|
| [generative_ai_deep_dive.md](architectures/generative_ai_deep_dive.md)| GAN, VAE, mô hình khuếch tán, LLM, ứng dụng AI tổng hợp |
| [graph_neural_networks.md](architectures/graph_neural_networks.md)| GCN, GAT, truyền tin nhắn, biểu đồ tri thức |
| [reinforcement_learning.md](architectures/reinforcement_learning.md)| MDP, Q-learning, độ dốc chính sách, RLHF, hệ thống đa tác nhân |
| [recommendation_systems.md](architectures/recommendation_systems.md)| Lọc cộng tác, dựa trên nội dung, kết hợp, nhân tố ma trận |
| [federated_learning_and_privacy.md](architectures/federated_learning_and_privacy.md)| Đào tạo phi tập trung, quyền riêng tư khác biệt, tổng hợp an toàn |
### Kỹ thuật ML
| Tập tin | Mô tả |
|------|-------------|
| [model_optimization_and_deployment.md](engineering/model_optimization_and_deployment.md)| Định lượng, cắt tỉa, chưng cất, ONNX, phục vụ |
| [ml_engineering_and_mlops.md](engineering/ml_engineering_and_mlops.md)| Phục vụ mô hình, đăng ký, chiến lược triển khai, giám sát trôi dạt |
| [data_engineering_and_pipelines.md](engineering/data_engineering_and_pipelines.md)| ETL/ELT, hồ dữ liệu, điều phối, Kafka, cửa hàng tính năng |
| [local_ai_architecture.md](engineering/local_ai_architecture.md)| Kiến trúc triển khai AI cục bộ |
| [phi3_and_local_models.md](engineering/phi3_and_local_models.md)| Chạy mô hình cục bộ |
### NLP và Lời nói
| Tập tin | Mô tả |
|------|-------------|
| [nlp_fundamentals.md](nlp_and_speech/nlp_fundamentals.md)| Xử lý văn bản, nhúng, Transformers, BERT, GPT |
| [speech_and_audio_processing.md](nlp_and_speech/speech_and_audio_processing.md)| ASR, TTS, tính năng âm thanh, Whisper |
| [time_series_and_forecasting.md](nlp_and_speech/time_series_and_forecasting.md)| ARIMA, Nhà tiên tri, LSTM, tính thời vụ, phát hiện sự bất thường |
| [computer_vision_fundamentals.md](nlp_and_speech/computer_vision_fundamentals.md)| CNN, phát hiện đối tượng, phân đoạn, học chuyển giao |
| [multimodal_ai.md](nlp_and_speech/multimodal_ai.md)| Mô hình ngôn ngữ thị giác, CLIP, DALL-E, học tập đa phương thức |
### Đạo đức và An toàn
| Tập tin | Mô tả |
|------|-------------|
| [ai_ethics_and_governance.md](ethics_and_safety/ai_ethics_and_governance.md)| AI thiên vị, công bằng, trách nhiệm giải trình, quy định, quản trị |
| [ai_safety_and_alignment.md](ethics_and_safety/ai_safety_and_alignment.md)| Bài toán căn chỉnh, RLHF, khả năng diễn giải, nghiên cứu an toàn AI |
## Đường dẫn đọc được đề xuất
### **Con đường dành cho người mới bắt đầu AI**
1.`foundations/artificial_intelligence.md`- AI là gì?
2.`foundations/ml_evaluation_and_workflow.md`- Cách ML hoạt động từ đầu đến cuối
3.`nlp_and_speech/nlp_fundamentals.md`— Xử lý văn bản và ngôn ngữ
4.`nlp_and_speech/computer_vision_fundamentals.md`— Xử lý hình ảnh và tầm nhìn
### **Con đường kỹ sư ML**
1.`foundations/ml_evaluation_and_workflow.md`- đường ống ML
2.`engineering/data_engineering_and_pipelines.md`— Cơ sở hạ tầng dữ liệu
3.`engineering/model_optimization_and_deployment.md`— Tối ưu hóa mô hình
4.`engineering/ml_engineering_and_mlops.md`— MLOps và phân phát
5.`engineering/local_ai_architecture.md`— Kiến trúc triển khai
### **Con đường nghiên cứu**
1.`foundations/artificial_intelligence.md`— Khái niệm cốt lõi
2.`architectures/generative_ai_deep_dive.md`— Mô hình sáng tạo
3.`architectures/graph_neural_networks.md`— Mô hình dựa trên đồ thị
4.`architectures/reinforcement_learning.md`- RL và ra quyết định
5.`ethics_and_safety/ai_safety_and_alignment.md`— Những cân nhắc về an toàn