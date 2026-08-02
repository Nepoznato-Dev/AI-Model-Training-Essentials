<!-- 
This file was automatically translated from English to Korean.
Source: technology_glossary.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 기술 용어집

현대 AI와 컴퓨팅 환경에서 자주 등장하는 AI 모델, 하드웨어, benchmark, 핵심 개념을 정리한 참고용 glossary입니다.

---

## AI 언어 모델과 어시스턴트

### ChatGPT
ChatGPT는 OpenAI가 개발한 AI chatbot으로, 2022년 11월에 처음 공개되었습니다.
GPT 계열의 large language model(LLM)을 기반으로 하며, 출시 두 달 만에 사용자 1억 명에 도달해 역사상 가장 빠르게 성장한 소비자용 AI 제품 가운데 하나로 꼽힙니다. 텍스트 대화, 코드 생성, 요약, 창의적 글쓰기를 지원하며, 유료 플랜에서는 GPT-4와 GPT-4o 같은 더 강력한 모델을 사용할 수 있습니다.

### GPT (Generative Pre-trained Transformer)
GPT는 OpenAI가 만든 large language model 계열입니다. 이 아키텍처는 방대한 텍스트 말뭉치를 대상으로 다음 토큰 예측(next-token prediction) 방식으로 학습한 decoder-only Transformer를 사용합니다. 대표적인 버전으로는 GPT-2(2019, 15억 파라미터, "too dangerous to release" 논란으로 유명), GPT-3(2020, 1750억 파라미터, API를 통해 널리 사용), GPT-3.5(초기 ChatGPT의 기반), GPT-4(2023, multimodal 지원, 여러 benchmark에서 인간 전문가 수준에 가까운 성능)가 있습니다.

### Claude
Claude는 Anthropic이 개발한 AI assistant입니다. 이름은 information theory의 창시자인 Claude Shannon에서 따왔습니다. Anthropic은 전 OpenAI 연구진이 설립했으며, 모델이 일련의 원칙을 따르도록 훈련해 더 안전하게 만드는 "constitutional AI" 접근법에 집중하고 있습니다. Claude 1, 2, 3 Haiku / Sonnet / Opus 등 Claude 계열 모델은 긴 context window(최대 200,000 tokens), 섬세한 추론, 그리고 기본형 LLM보다 낮은 유해 출력으로 잘 알려져 있습니다.

### Gemini
Gemini는 Google DeepMind가 발표한 multimodal AI 모델 계열로, 2023년 12월에 공개되었습니다. Gemini는 text, images, audio, video를 처음부터 함께 학습한 네이티브 multimodal 모델로, 기존 모델처럼 나중에 fine-tuning으로 모달리티를 덧붙인 형태와 구분됩니다. Gemini Nano(on-device), Gemini Flash(빠르고 비용 효율적), Gemini Ultra(최고 성능) 같은 버전이 있으며, Google의 AI chatbot Bard(현재 이름은 Gemini)와 Google Search AI Overviews를 구동합니다.

### Phi-3-mini
Phi-3-mini는 Microsoft가 개발한 38억 파라미터 규모의 small language model(SLM)입니다. 2026년 4월에 공개되었으며, 대부분의 대형 모델과 달리 Microsoft Research가 개척한 "textbook-quality" 데이터셋 구성 방식을 사용해 단순한 데이터 양보다 품질을 우선했습니다. GPT-4나 Claude 3 Opus보다 훨씬 작지만, MMLU와 HumanEval 같은 추론 benchmark에서는 자신보다 몇 배 큰 모델과 맞먹거나 더 나은 성능을 보입니다. 기본 버전은 4k token context window를, long-context 버전은 128k window를 지원합니다. 충분한 RAM이 있다면 일반 소비자용 GPU 한 장이나 최신 스마트폰 on-device 환경에서도 실행할 수 있습니다.

### Llama (Meta AI)
Llama(Large Language Model Meta AI)는 Meta가 공개한 open-weights 모델 계열입니다. Llama 2(2023)는 7B부터 70B까지 다양한 크기로 연구 및 상업적 활용을 위해 공개되었고, Llama 3(2026)는 성능을 크게 끌어올리며 8B부터 70B, 이후에는 400B+ 규모까지 확장되었습니다. 가중치를 공개 다운로드할 수 있기 때문에 Llama는 Mistral, Alpaca, Vicuna 같은 수많은 fine-tuned 변형 모델 생태계의 기반이 되었고, 로컬 또는 프라이빗 AI 배포에도 널리 사용됩니다.

### Mistral
Mistral AI는 open 및 proprietary LLM을 개발하는 프랑스 AI 기업입니다. Mistral 7B(2023)는 sliding window attention, grouped-query attention 같은 효율적 기법을 활용해 70억 파라미터 모델이 훨씬 큰 모델과 비슷한 성능을 낼 수 있음을 보여주었습니다. Mixtral 8x7B(2026)는 mixture-of-experts 구조를 사용해 각 token을 8개의 expert network 중 일부로만 보내면서, GPT-3.5 수준의 성능을 더 낮은 계산 비용으로 달성합니다. Mistral의 일부 모델은 완전한 open-weight 형태로 공개되어 로컬 실행이 가능합니다.

---

## GPU 하드웨어와 그래픽 카드

### GPU (Graphics Processing Unit)
GPU는 대규모 병렬 계산을 위해 설계된 프로세서입니다. 원래는 3D graphics 렌더링을 위해 만들어졌지만, 수천 개의 작은 코어로 부동소수점 연산을 동시에 수행할 수 있기 때문에 오늘날에는 AI/ML 학습과 inference에 필수적인 하드웨어가 되었습니다. AI 분야의 대표적인 GPU 제조사는 NVIDIA와 AMD입니다.

### NVIDIA GeForce RTX Series
RTX(Ray Tracing Texel eXtreme) 시리즈는 NVIDIA의 소비자용 GPU 제품군입니다. RTX 30xx(Ampere, 2020)와 RTX 40xx(Ada Lovelace, 2022) 세대에는 AI 연산을 가속하는 전용 Tensor Cores가 포함되어 있습니다. 로컬에서 AI 모델을 실행할 때는 VRAM(video RAM)이 특히 중요합니다. 예를 들어 8GB GPU는 4-bit quantisation 기준으로 7B 모델을 다룰 수 있고, 24GB GPU는 70B 모델을 4-bit로 실행할 수 있습니다.

### NVIDIA A-Series와 H-Series (데이터 센터)
A100(Ampere, 2020)과 H100(Hopper, 2022)은 NVIDIA의 전문 AI accelerator입니다. H100은 최대 80GB의 HBM3 memory를 탑재하며, 오늘날 대부분의 대규모 LLM 학습을 뒷받침하는 사실상의 표준 하드웨어입니다. 가격은 장당 $25,000-$40,000 수준이지만, 소비자용 RTX 카드보다 10-30배 높은 AI 처리량을 제공합니다.

### AMD Radeon RX Series
AMD의 소비자용 GPU 제품군입니다. RX 7900 XTX(2022)는 24GB VRAM을 갖추고 있으며, ROCm(AMD의 GPU compute stack)을 통해 로컬 LLM을 실행할 수 있습니다. 아직은 AI framework 지원 면에서 NVIDIA보다 불리하지만, 지원 범위는 점차 개선되고 있습니다.

### Intel Arc
Intel Arc는 2022년부터 출시된 Intel의 discrete GPU 라인업입니다. Arc GPU는 XeSS(Intel의 super-sampling 기술)를 지원하며, OpenVINO와 IPEX-LLM framework를 통해 제한적이지만 점점 확대되는 AI inference 지원을 제공합니다.

### ARK Intel (ark.intel.com)
ARK는 Intel이 운영하는 공식 제품 사양 데이터베이스로, 주소는 ark.intel.com입니다. 여기에는 CPU, GPU, FPGA, NUC를 포함한 모든 Intel 제품의 코어 수, 클럭 속도, TDP, 지원 메모리 종류, instruction set 기능 등 상세한 기술 사양이 정리되어 있습니다. "spec은 ARK에서 확인하라"는 말은, 신뢰할 수 있는 하드웨어 정보를 얻기 위해 그 데이터베이스를 보라는 뜻입니다.

---

## AI 성능 벤치마크

### MMLU (Massive Multitask Language Understanding)
MMLU는 mathematics, history, law, medicine, computer science를 포함한 57개 학문 분야에서 LLM의 지식을 평가하는 benchmark입니다. 실제 대학 수준 시험에서 가져온 객관식 문제로 구성되어 있습니다. 대략 70% 점수면 학부생 수준으로 간주되며, GPT-4와 Claude 3는 86%를 넘는 점수를 기록합니다. Phi-3-mini는 작은 규모에도 불구하고 약 70% 수준을 보입니다.

### HumanEval
HumanEval은 OpenAI가 만든 코드 생성 benchmark입니다. 자동 테스트 케이스가 포함된 164개의 Python programming 문제로 이루어져 있습니다. 평가는 pass@k, 즉 생성된 k개의 해답 가운데 하나 이상이 모든 테스트를 통과할 확률로 측정합니다. GPT-4는 pass@1 기준 약 87%를 기록하며, 잘 조정된 7B 모델은 대략 50-60% 수준에 도달할 수 있습니다.

### HellaSwag
HellaSwag는 상식 추론을 평가하는 benchmark입니다. 모델은 일상적인 활동을 설명하는 문장을 받고, 네 개의 선택지 중 가장 그럴듯한 다음 문장을 골라야 합니다. 오답 선택지는 그럴듯해 보이지만 미묘하게 틀리도록 설계되어 있어, 모델이 물리적·사회적 상황을 실제로 이해하는지 시험합니다.

### ARC (AI2 Reasoning Challenge)
ARC는 Allen Institute for AI가 만든 benchmark입니다. 초등·중등 수준의 과학 문제로 구성되며, "Easy"와 "Challenge" 세트로 나뉩니다. Challenge 세트는 단순 검색 기반 방식이나 통계적 모델로는 풀기 어렵고, 여러 단계를 거치는 추론을 요구합니다.

---

## 핵심 AI/ML 개념

### RAG (Retrieval-Augmented Generation)
RAG는 retrieval system(보통 vector database)과 language model을 결합하는 기법입니다. 모델의 내부 파라미터 지식에만 의존하는 대신, 먼저 외부 지식 기반에서 관련 문서를 찾아온 뒤 그 내용을 model context에 넣어 응답을 생성합니다. 이 방식 덕분에 재학습 없이도 최신 정보나 도메인 특화 정보를 다룰 수 있습니다. Potato.ai도 RAG의 한 형태를 사용하며, KB에서 관련 내용을 검색해 context에 포함한 뒤 답변을 생성합니다.

### Fine-tuning
Fine-tuning은 사전 학습된 모델을 더 작은 도메인 특화 데이터셋으로 추가 학습시키는 과정입니다. 이를 통해 모델 가중치를 특정 작업이나 분야에 맞게 조정할 수 있습니다. 예를 들어 기본 LLM을 medical records 기반으로 fine-tune하면 의료 Q&A assistant를 만들 수 있습니다. 계산 비용은 적지 않지만, 처음부터 모델을 새로 학습하는 것보다는 훨씬 저렴합니다.

### Quantisation
Quantisation은 모델 가중치의 수치 정밀도를 낮추는 방법입니다(예: 32-bit float → 4-bit integer). 이렇게 하면 메모리 사용량이 크게 줄어듭니다. 예를 들어 16-bit 정밀도의 7B 모델은 약 14GB VRAM이 필요하지만, 같은 모델을 4-bit(GGUF format)로 양자화하면 약 4GB 정도면 됩니다. 정확도는 소폭 떨어질 수 있지만, 대형 모델을 소비자용 하드웨어나 모바일 기기에서 실행 가능하게 만드는 핵심 기법입니다.

### Context Window
Context window는 모델이 한 번에 처리할 수 있는 최대 token 수를 말하며, prompt와 생성된 응답을 모두 포함합니다. GPT-3.5는 4,096-token window를 가졌고, GPT-4 Turbo와 Claude 3는 128,000 tokens를 지원하며, Gemini 1.5 Pro는 1,000,000 tokens까지 지원합니다. Context window가 클수록 긴 대화나 긴 문서를 한 번에 더 많이 볼 수 있어 장문의 일관성이 좋아집니다.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF는 단순히 다음 token을 예측하던 base language model을 지시를 따르는 assistant로 바꾸는 학습 기법입니다. 사람 평가자가 모델 출력을 비교·평가하면, 그 선호를 바탕으로 reward model을 학습시키고, 이후 reinforcement learning으로 language model을 최적화합니다. ChatGPT, Claude, Gemini는 모두 RLHF 또는 유사한 alignment 기법(예: Constitutional AI, Direct Preference Optimisation)의 변형을 사용합니다.

### Transformer 아키텍처
Transformer는 현대 LLM 전반의 기반이 되는 neural network 아키텍처입니다. 2017년 Vaswani et al.의 논문 "Attention Is All You Need"에서 처음 소개되었으며, 토큰을 순차적으로 처리하는 대신 self-attention 메커니즘으로 병렬 처리합니다. Encoder-only Transformer(BERT)는 이해 작업에, decoder-only Transformer(GPT, Llama, Mistral)는 생성 작업에, encoder-decoder Transformer(T5, BART)는 번역과 요약 작업에 주로 사용됩니다.

### 임베딩과 벡터 데이터베이스
Embeddings는 neural network가 만들어낸 텍스트(또는 이미지)의 밀집 수치 표현입니다. 의미가 비슷한 텍스트는 vector space에서 서로 가까운 embedding을 갖습니다. Vector databases(ChromaDB, Pinecone, Weaviate, Qdrant)는 이러한 embedding을 저장하고 빠른 approximate nearest-neighbour 검색을 지원합니다. 이런 저장 계층은 RAG 시스템의 핵심 기반이며, Potato.ai의 cold-memory layer도 여기에 해당합니다.
