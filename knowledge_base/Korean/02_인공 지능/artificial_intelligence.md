<!-- 
This file was automatically translated from English to Korean.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 인공지능

## 인공지능이란?

Artificial Intelligence (AI)는 생각하고 학습하며 문제를 해결하도록 설계된 기계가 인간 지능을 모방하는 것을 뜻합니다. AI 시스템은 음성 인식, 의사결정, 언어 번역, 이미지 속 객체 식별처럼 일반적으로 인간 지능이 필요한 작업을 수행할 수 있습니다. 이 용어는 1956년 Dartmouth Conference에서 John McCarthy가 처음 사용했으며, 이 행사는 AI라는 학문 분야의 출발점으로 널리 여겨집니다.

현대 AI는 크게 두 범주로 나뉩니다. 하나는 특정 작업을 위해 설계된 Narrow AI(Weak AI라고도 함)이고, 다른 하나는 모든 영역에서 인간의 인지 능력과 맞먹거나 이를 뛰어넘는 이론적 개념인 Artificial General Intelligence (AGI)입니다. 현재 존재하는 모든 AI 시스템은 Narrow AI에 속합니다.

## AI의 역사

AI의 역사는 거의 80년에 걸쳐 이어집니다. 초기 이론적 토대는 Alan Turing이 마련했는데, 그는 1950년 논문 "Computing Machinery and Intelligence"에서 Turing Test를 제시했습니다. 이는 기계가 인간과 구별되지 않을 정도로 지능적인 행동을 보일 수 있는지를 평가하는 기준입니다. 1956년 Dartmouth Conference는 AI를 정식 학문 분야로 확립했습니다.

1950년대부터 1970년대까지는 ELIZA(간단한 챗봇), LISP(AI를 위해 설계된 프로그래밍 언어) 같은 초기 프로그램이 낙관적 기대를 모았습니다. 1970~1980년대의 "AI winter"는 기대에 미치지 못한 성과로 인해 자금과 관심이 줄어든 시기였습니다. 1980년대에는 인간의 전문 지식을 규칙으로 담아낸 expert systems의 등장으로 AI가 다시 주목받았습니다. 2000년대에는 인터넷과 대규모 데이터셋의 확산을 바탕으로 머신러닝이 큰 도약을 이뤘습니다. 2010년대에는 딥러닝이 부상하며 computer vision, natural language processing (NLP), reinforcement learning을 크게 변화시켰습니다.

## 기계 학습

머신러닝(Machine Learning, ML)은 AI의 하위 분야로, 시스템이 명시적으로 프로그래밍되지 않아도 데이터로부터 학습할 수 있게 합니다. 주요 ML 범주는 다음과 같습니다.

**지도 학습 (Supervised Learning)**: 모델은 라벨이 붙은 입력-출력 쌍을 바탕으로 학습합니다. 예로는 spam detection과 image classification이 있습니다. 알고리즘에는 linear regression, decision trees, support vector machines, neural networks가 포함됩니다.

**비지도 학습 (Unsupervised Learning)**: 모델은 라벨이 없는 데이터에서 패턴을 찾습니다. 예로는 customer segmentation과 anomaly detection이 있습니다. 알고리즘에는 k-means clustering과 principal component analysis (PCA)가 있습니다.

**강화 학습 (Reinforcement Learning)**: 에이전트가 환경과 상호작용하면서 보상이나 벌칙을 받고 학습합니다. game-playing AI(AlphaGo, AlphaZero), robotics, recommendation systems 등에 사용됩니다.

**준지도 학습과 자기지도 학습 (Semi-Supervised and Self-Supervised Learning)**: 소량의 라벨된 데이터와 대규모 비라벨 데이터셋을 함께 사용합니다. GPT 모델은 사전학습 단계에서 self-supervised 방식을 사용합니다.

## 딥 러닝

딥러닝(Deep Learning)은 머신러닝의 하위 분야로, 여러 층을 가진 인공 신경망(neural networks)을 사용합니다. 뇌의 신경 구조에서 느슨하게 영감을 받은 이 네트워크는 데이터의 계층적 표현을 학습합니다. 딥러닝은 다음 분야를 뒷받침합니다.

- **Computer Vision**: 이미지 인식, 객체 탐지, 의료 영상
- **Natural Language Processing**: 기계 번역, 감성 분석, 질의응답
- **Speech Recognition**: Siri, Alexa, Google Assistant 같은 음성 비서
- **Generative AI**: 이미지 생성(DALL-E, Stable Diffusion), 텍스트 생성(GPT)

주요 deep learning 아키텍처에는 이미지용 convolutional neural networks (CNNs), 시퀀스용 recurrent neural networks (RNNs)와 LSTMs, 언어용 transformers, 생성용 generative adversarial networks (GANs)가 있습니다.

## 대규모 언어 모델 (LLMs)

대규모 언어 모델(Large Language Models, LLMs)은 방대한 양의 텍스트 데이터를 학습하여 인간 언어를 이해하고 생성하는 AI 시스템입니다. 이들은 2017년 Vaswani et al.의 논문 "Attention is All You Need"에서 제시된 Transformer 아키텍처를 기반으로 합니다. LLM은 시퀀스에서 다음 token(word piece)을 예측하며, 이를 통해 일관된 텍스트를 생성하고 질문에 답하며 코드를 작성하고 추론 작업을 수행합니다.

대표적인 LLM은 다음과 같습니다.
- **GPT series** (OpenAI): GPT-3, GPT-4 및 후속 모델로, 대화와 코드 작업에 널리 사용됩니다.
- **Claude** (Anthropic): 안전성과 유용성에 중점을 둡니다.
- **Gemini** (Google DeepMind): 텍스트, 이미지, 코드를 통합하는 멀티모달 모델입니다.
- **LLaMA / Llama 3** (Meta): 연구와 로컬 배포에 적합한 open-weight 모델입니다.
- **Mistral** (Mistral AI): 훨씬 더 큰 LLM과 경쟁할 수 있는 효율적인 오픈 모델입니다.

LLM은 두 단계로 학습됩니다. 첫 번째는 대규모 텍스트 코퍼스에 대한 비지도 사전학습(pre-training)이고, 두 번째는 supervised 방식 또는 인간 피드백 기반 강화학습(RLHF)을 활용한 fine-tuning입니다. Context window는 LLM이 한 번에 처리할 수 있는 텍스트 양을 뜻하며, 초기 GPT-3의 4K tokens부터 2026년 최상위 모델의 100만 tokens 이상까지 다양합니다.

## AI 윤리와 안전

AI는 편향, 프라이버시, 일자리 대체, 오용 위험 등 중요한 윤리적 질문을 제기합니다. 학습 데이터가 역사적 불평등을 반영할 경우 알고리즘 편향(algorithmic bias)이 발생해 AI 시스템이 차별적인 출력을 낼 수 있습니다. 예를 들어 facial recognition 시스템은 피부가 더 어두운 사람들에게서 더 높은 오류율을 보였고, 일부 채용 알고리즘은 남성 지원자를 더 선호하는 경향을 드러냈습니다.

AI 안전성(AI safety)은 AI 시스템이 의도한 대로 행동하면서도 예상치 못한 해를 끼치지 않도록 보장하는 분야입니다. 핵심 관심사는 다음과 같습니다.
- **Alignment**: AI의 목표가 인간의 가치와 일치하도록 하는 것
- **Interpretability / Explainability**: AI가 왜 그런 결정을 내렸는지 이해하는 것(의학, 법률, 금융에서 특히 중요)
- **Misuse**: AI가 생성한 deepfake, 허위 정보, 사이버 공격
- **Existential risk**: 미래의 AGI가 인간의 생존과 어긋나는 목표를 추구할 수 있다는 이론적 우려

AI safety에 힘쓰는 조직으로는 OpenAI의 Safety team, Anthropic(전 OpenAI 안전 연구자들이 설립), DeepMind의 safety team, 그리고 MIRI와 ARC 같은 독립 연구기관이 있습니다.

## 사회 속의 AI

AI는 거의 모든 산업을 변화시키고 있습니다.

- **Healthcare**: 의료 영상으로 암을 진단하고, 환자 예후를 예측하며, 신약 개발을 가속하고(AlphaFold는 단백질 접힘 구조 예측 문제 해결에 큰 기여를 했습니다), 맞춤형 치료 계획을 세우는 데 AI가 활용됩니다.
- **Finance**: fraud detection, algorithmic trading, credit scoring, robo-advisors에 ML 모델이 사용됩니다.
- **Transportation**: 자율주행 차량은 computer vision, lidar, reinforcement learning을 사용합니다. Tesla Autopilot, Waymo, Cruise가 대표적인 사례입니다.
- **Education**: 개인 맞춤형 학습 플랫폼은 학생별 속도와 학습 스타일에 맞춰 콘텐츠를 조정합니다.
- **Creative fields**: AI는 음악, 예술, 글을 생성하며 Midjourney, DALL-E, GitHub Copilot 같은 도구는 창작 워크플로를 바꾸고 있습니다.
- **Cybersecurity**: AI는 이상 징후를 탐지하고 위협을 식별하며, 공격과 방어 양쪽 모두에 활용됩니다.

## 로보틱스와 Embodied AI

로보틱스(Robotics)는 AI와 물리적 기계를 결합하는 분야입니다. 현대 로봇은 perception(카메라, lidar), planning, control을 사용해 환경을 탐색하고 조작합니다. Boston Dynamics의 Atlas는 고도의 이족보행 능력을 보여 줍니다. ABB와 FANUC 같은 기업의 산업용 로봇은 제조 공정을 자동화합니다. Household robots(Roomba)와 surgical robots(da Vinci System)는 일상과 의료 현장에서 AI를 활용합니다. Embodied AI 연구는 에이전트가 세계와의 상호작용을 통해 물리적 기술을 학습하도록 하며, 시뮬레이션 환경과 실제 환경 사이의 간극을 줄이는 데 초점을 맞춥니다.

## 현재 AI 동향 (2020s)

- **Multimodal AI**: 텍스트, 이미지, 오디오, 비디오를 함께 처리하는 시스템입니다(GPT-4V, Gemini).
- **Agents and agentic AI**: 도구를 사용하고, 웹을 탐색하고, 코드를 작성하며, 여러 단계의 행동을 수행할 수 있는 LLM입니다(OpenAI's Operator, Anthropic Computer Use).
- **Open-weight models**: Meta의 LLaMA는 연구자들이 대규모 모델에 접근할 수 있는 길을 넓혔습니다.
- **On-device AI**: 클라우드 연결 없이 휴대폰과 노트북에서 AI 모델을 로컬로 실행하는 방식입니다(Apple Intelligence, Qualcomm NPUs).
- **AI regulation**: EU AI Act(2026)는 위험 수준에 따라 AI 시스템을 분류하는 세계 최초의 포괄적 AI 법률입니다.
