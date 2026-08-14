---
# Metadata
title: "Technology Glossary"
description: "Technical terminology (AI models, hardware, benchmarks)"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, glossary, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# 기술 용어집
AI 모델, 하드웨어, 벤치마크, 핵심 개념을 다루는 참조 용어집
현대 AI 및 컴퓨팅 환경에서
---

## AI 언어 모델 및 보조자
### 채팅GPT
ChatGPT는 OpenAI가 개발한 AI 챗봇으로, 2022년 11월 첫 출시되었습니다.
이는 LLM(대형 언어 모델)의 GPT 시리즈로 구동됩니다. ChatGPT는 하나입니다
역사상 가장 빠르게 성장하는 소비자 AI 제품 중 하나로 1억 개에 도달
출시 후 2개월 이내의 사용자 수입니다. 텍스트 기반의 대화, 코드를 지원합니다.
생성, 요약 및 창의적인 글쓰기. 유료 등급에서는 다음에 대한 액세스를 제공합니다.
GPT-4 및 GPT-4o와 같은 더 강력한 모델.
### GPT(생성 사전 훈련된 변환기)
GPT는 OpenAI가 만든 대규모 언어 모델 제품군입니다. 아키텍처
다음 토큰 예측 목표로 학습된 디코더 전용 Transformer를 사용합니다.
대규모 텍스트 말뭉치. 주요 버전에는 GPT-2(2019, 1.5B 매개변수, 주목할만한 사항)가 포함됩니다.
"공개하기에는 너무 위험함" 홍보용), GPT-3(2020, 175B 매개변수, 널리
API를 통해 사용됨), GPT-3.5(원래 ChatGPT의 백본) 및 GPT-4
(2023년, 다중 모드, 많은 벤치마크에서 인간 전문가 수준에 가까운 성능)
### 클로드
클로드(Claude)는 앤트로픽(Anthropic)이 개발한 AI 비서이다. 클로드의 이름을 따서 명명되었습니다.
정보이론의 창시자인 섀넌. Anthropic은 이전에 설립되었습니다.
OpenAI 연구진은 "헌법적 AI"에 중점을 두고 있습니다.
일련의 원칙을 따르도록 교육하여 더 안전한 모델을 만듭니다. 클로드 모델
(Claude 1, 2, 3 Haiku / Sonnet / Opus)는 긴 컨텍스트 창(위로)으로 알려져 있습니다.
최대 200,000개 토큰), 미묘한 추론, 유해한 출력 감소
기본 LLM.
### 쌍둥이자리
Gemini는 Google DeepMind의 다중 모드 AI 모델 제품군으로,
2023년 12월. Gemini는 기본적으로 다중 모드입니다.
이전 모델과 달리 텍스트, 이미지, 오디오 및 비디오를 동시에
미세 조정을 통해 추가된 양식입니다. 버전에는 Gemini Nano(온디바이스),
Gemini Flash(빠르고 비용 효율적) 및 Gemini Ultra(최고 성능).
Gemini는 Google의 AI 챗봇인 Bard(Gemini로 이름 변경) 및 Google 검색 AI를 지원합니다.
개요.
### 파이-3-미니
Phi-3-mini는 Microsoft가 3.8B로 개발한 소규모 언어 모델(SLM)입니다.
매개변수. 2024년 4월에 출시되었습니다. 대부분의 대형 모델과 달리 파이-3-미니는
신중하게 선별된 "교과서 품질" 데이터 세트에 대해 교육을 받았습니다.
Microsoft Research가 개척한 기술로, 원본 볼륨보다 데이터 품질을 우선시합니다.
GPT-4나 Claude 3 Opus보다 훨씬 작지만 Phi-3-mini와 일치하거나
MMLU와 같은 추론 벤치마크에서 모델보다 몇 배 더 큰 성능을 발휘합니다.
HumanEval. 기본 변형에서는 4k 토큰 컨텍스트 창을 지원하고 128k
긴 컨텍스트 변형의 창. Phi-3-mini는 단일 소비자 GPU에서 실행 가능
또는 RAM이 충분한 최신 스마트폰의 기기에서도 가능합니다.
### 라마(메타 AI)
Llama(Large Language Model Meta AI)는 개방형 모델 제품군입니다.
메타에서 발매. Llama 2(2023)가 연구 및 상업용으로 출시되었습니다.
7B~70B 매개변수 범위의 크기를 갖습니다. 라마 3(2024) 개선
8B에서 70B(및 이후 400B+) 범위의 모델에서 성능이 크게 향상되었습니다.
가중치는 공개적으로 다운로드할 수 있으므로 Llama 모델이 기초입니다.
미세 조정된 변종(Mistral, Alpaca, Vicuna 등)의 대규모 생태계
로컬/프라이빗 AI 배포에 널리 사용됩니다.
### 미스트랄
Mistral AI는 개방형 독점 LLM을 개발하는 프랑스 AI 회사입니다.
Mistral 7B(2023)는 7B 매개변수 모델이
슬라이딩과 같은 효율적인 기술을 사용하여 훨씬 더 큰 모델의 성능을 발휘합니다.
윈도우 어텐션과 그룹 쿼리 어텐션. Mixtral 8x7B (2023)은 혼합물입니다.
전문가 모델 — 각 토큰을 8개 전문가 네트워크의 하위 집합으로 라우팅합니다.
계산 비용이 저렴하면서도 GPT-3.5 수준의 성능을 달성합니다.
Mistral의 모델은 완전 개방형이며 로컬에서 실행할 수 있습니다.
---

## GPU 하드웨어 및 그래픽 카드
### GPU(그래픽 처리 장치)
GPU는 대규모 병렬 계산을 위해 설계된 프로세서입니다. 원래
3D 그래픽 렌더링을 위해 구축된 GPU는 AI/ML 교육에 필수적입니다.
수천 개의 부동 소수점 연산을 수행할 수 있기 때문에 추론
수천 개의 작은 코어를 동시에 사용합니다. 두 가지 주요 GPU 제조업체
AI 분야에는 NVIDIA와 AMD가 있습니다.
### NVIDIA GeForce RTX 시리즈
RTX(Ray Tracing Texel eXtreme) 시리즈는 NVIDIA의 소비자 GPU 라인입니다. RTX
30xx(Ampere, 2020) 및 RTX 40xx(Ada Lovelace, 2022) 세대에는 다음이 포함됩니다.
AI 작업 가속화를 위한 전용 Tensor 코어. VRAM(비디오 RAM)은
AI 모델을 로컬에서 실행하는 데 매우 중요합니다. 8GB GPU는 7B 매개변수를 처리할 수 있습니다.
4비트 양자화 모델; 24GB GPU는 4비트로 70B 모델을 처리할 수 있습니다.
### NVIDIA A 시리즈 및 H 시리즈(데이터 센터)
A100(Ampere, 2020)과 H100(Hopper, 2022)은 NVIDIA의 전문 AI입니다.
가속기. H100은 최대 80GB의 HBM3 메모리를 갖추고 있으며 표준입니다.
오늘날 대부분의 대규모 LLM 교육을 지원하는 하드웨어입니다. 이 GPU의 가격은 25,000달러입니다.
각각 $40,000이지만 소비자 RTX 카드의 AI 처리량의 10~30배를 제공합니다.
### AMD Radeon RX 시리즈
AMD의 소비자 GPU 라인. RX 7900 XTX(2022)에는 24GB VRAM이 있으며 실행할 수 있습니다.
ROCm(AMD의 GPU 컴퓨팅 스택)을 통한 로컬 LLM. AMD GPU는 일반적으로 더 적습니다.
AI 프레임워크에 대해서는 NVIDIA보다 잘 지원되지만 지원은 개선되고 있습니다.
### 인텔 아크
Intel Arc는 2022년부터 출시되는 Intel의 개별 GPU 제품 라인입니다. Arc
GPU는 XeSS(Intel의 슈퍼 샘플링)를 지원하며 제한적이지만 지원이 늘어나고 있습니다.
OpenVINO 및 IPEX-LLM 프레임워크를 통한 AI 추론 작업용.
### ARK 인텔(ark.intel.com)
ARK는 ark.intel.com에 있는 Intel의 공식 제품 사양 데이터베이스입니다. 그것
모든 Intel CPU, GPU, FPGA 및
코어 수, 클럭 속도, TDP, 지원되는 메모리 유형을 포함한 NUC 제품,
및 명령어 세트 기능. "ARK의 사양을 확인하세요"라는 말을 들으면
신뢰할 수 있는 하드웨어 정보를 확인하려면 해당 데이터베이스를 방문하세요.
---

## AI 성능 벤치마크
### MMLU(대규모 멀티태스킹 언어 이해)
MMLU는 다음을 포함한 57개 학문 과목에 대한 LLM 지식을 테스트하는 벤치마크입니다.
수학, 역사, 법률, 의학, 컴퓨터 과학. 그것은 다음과 같이 구성됩니다
실제 대학 수준의 시험에서 나온 객관식 문제입니다. 점수
70%는 대략 인간 학부 수준입니다. GPT-4 및 Claude 3 점수는 86% 이상입니다.
Phi-3-mini는 작은 크기에도 불구하고 약 70%의 점수를 받았습니다.
### 인간평가
HumanEval은 OpenAI의 코드 생성 벤치마크입니다. 164개의 Python으로 구성되어 있습니다.
자동화된 테스트 케이스의 프로그래밍 문제. 모델은 다음에서 측정됩니다.
pass@k — 생성된 k개 솔루션 중 적어도 하나가 모든 솔루션을 통과할 확률
테스트. GPT-4 점수 ~87%(pass@1); 잘 조정된 7B 모델은 ~50~60%에 도달할 수 있습니다.
### 헬라스웨그
HellaSwag는 상식 추론 벤치마크입니다. 모델에게 문장이 주어진다
일상적인 활동을 설명하고 다음 중 가장 가능성이 높은 것을 선택해야 합니다.
네 가지 옵션. 잘못된 옵션은 그럴듯하게 특별히 설계되었지만
미묘하게 틀렸어. 모델이 물리적인 현상에 대한 근거 있는 이해를 갖고 있는지 테스트합니다.
그리고 사회적 상황.
### ARC(AI2 추론 챌린지)
ARC는 Allen Institute for AI의 벤치마크입니다. 초등학교로 구성되어 있습니다.
과학 질문은 "쉬움"과 "도전" 세트로 나뉩니다. 챌린지 세트
검색 기반 방법과 간단한 통계 모델이 포함된 질문이 포함되어 있습니다.
다단계 추론이 필요한 어려움을 겪습니다.
---

## 핵심 AI/ML 개념
### RAG(검색 증강 생성)
RAG는 검색 시스템(일반적으로 벡터)을 결합한 기술입니다.
데이터베이스) 언어 모델을 사용합니다. 모델의 말에만 의존하기보다는
파라메트릭 지식을 바탕으로 RAG는 먼저 외부에서 관련 문서를 검색합니다.
지식 베이스를 모델의 컨텍스트에 포함시킵니다. 이를 통해
최신 정보 또는 도메인별 정보에 대한 질문에 답하는 모델
재교육 없이. Potato.ai는 RAG 형식을 사용합니다. KB에서 검색합니다.
응답을 생성하기 전에 컨텍스트에 결과를 포함합니다.
### 미세 조정
미세 조정은 미리 훈련된 모델을 계속 학습하는 프로세스입니다.
더 작은 도메인별 데이터 세트. 이는 모델의 가중치를 다음과 같이 조정합니다.
특정 작업이나 도메인. 예를 들어, 기본 LLM은 다음과 같이 미세 조정될 수 있습니다.
의료 기록을 작성하여 의료 Q&A 도우미를 만듭니다. 미세 조정은
계산 비용이 많이 들지만 처음부터 훈련하는 것보다 훨씬 저렴합니다.
### 양자화
양자화는 모델 가중치의 수치 정밀도를 감소시킵니다(예: 32비트에서
4비트 정수로 부동 소수점). 이로 인해 메모리 공간이 크게 줄어듭니다 - 7B 모델
16비트 정밀도에서는 ~14GB VRAM이 필요합니다. 4비트(GGUF 형식)의 동일한 모델
~4GB가 필요합니다. 양자화는 일반적으로 작지만 허용 가능한 정확도를 유발합니다.
성능을 저하시키며 대형 모델을 소비자에서 실행할 수 있게 하는 주요 기술입니다.
하드웨어 또는 심지어 모바일 장치.
### 컨텍스트 창
컨텍스트 창은 모델이 한 번에 처리할 수 있는 최대 토큰 수입니다.
프롬프트와 생성된 응답을 모두 포함합니다. GPT-3.5에는 4,096개의 토큰이 있었습니다.
창; GPT-4 Turbo 및 Claude 3는 128,000개의 토큰을 지원합니다. 제미니 1.5 프로
1,000,000개의 토큰을 지원합니다. 더 큰 컨텍스트 창을 통해 모델은 "볼" 수 있습니다.
한 번에 더 많은 대화나 문서를 처리하여 장기간에 걸쳐 일관성을 향상시킵니다.
교환.
### RLHF(인간 피드백을 통한 강화 학습)
RLHF는 기본 언어 모델(
단순히 다음 토큰을 예측하는 것)을 지침을 따르고
도움이 되는 행동을 합니다. 인간 평가자가 모델 출력에 점수를 매기고 보상 모델이 학습됩니다.
선호도에 따라 언어 모델이 최적화됩니다.
강화학습을 이용한 보상 모델. ChatGPT, Claude 및 Gemini는 모두 사용합니다.
RLHF의 변형 또는 유사한 정렬 기술(예: Constitutional AI,
직접 선호도 최적화).
### 트랜스포머 아키텍처
Transformer는 모든 최신 LLM의 기반이 되는 신경망 아키텍처입니다.
Vaswani 등의 2017년 논문 "Attention Is All You Need"에 소개된 내용입니다.
self-attention 메커니즘을 사용하여 모든 토큰을 병렬로 처리합니다.
순차적으로. BERT(인코더 전용 변환기)는 작업을 이해하는 데 사용됩니다.
디코더 전용 변환기(GPT, Llama, Mistral)는 생성 작업에 사용됩니다.
인코더-디코더 변환기(T5, BART)는 번역 및 요약에 사용됩니다.
### 임베딩 및 벡터 데이터베이스
임베딩은 다음에서 생성된 텍스트(또는 이미지)를 밀집된 숫자로 표현한 것입니다.
신경망. 의미상 유사한 텍스트에는 가까운 임베딩이 있습니다.
벡터 공간. 벡터 데이터베이스(ChromaDB, Pinecone, Weaviate, Qdrant) 스토어
이러한 임베딩을 통해 빠른 근사 최근접 검색을 지원합니다. 그들은
Potato.ai의 콜드 메모리 레이어를 포함한 RAG 시스템의 스토리지 백본입니다.