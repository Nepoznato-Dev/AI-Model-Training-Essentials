# 데이터 과학 및 분석
AI 모델 교육 및 데이터 기반 의사 결정에 필수적인 수학적 기초, 데이터 과학 워크플로, 기계 학습 개념 및 분석 사례를 다루는 구조화된 참조 문서 모음입니다.
## 구조
```
03_data_science_and_analytics/
├── README.md                                       ← You are here
├── mathematics/                                    ← Mathematical foundations (see mathematics/README.md)
│   ├── Foundations
│   │   ├── mathematics.md                             Core math: algebra, calculus, linear algebra
│   │   ├── statistics_and_probability.md              Probability, inference, regression, Bayesian methods
│   │   └── logic_and_critical_thinking.md             Formal logic, fallacies, argument analysis
│   ├── Pure Mathematics
│   │   ├── discrete_mathematics.md                    Sets, relations, combinatorics, recurrence
│   │   ├── graph_theory.md                            Graphs, trees, traversals, shortest paths
│   │   ├── number_theory.md                           Primes, modular arithmetic, cryptography
│   │   ├── abstract_algebra.md                        Groups, rings, fields, vector spaces
│   │   └── real_analysis.md                           Limits, integration, metric spaces, measure theory
│   ├── Applied Mathematics
│   │   ├── optimization.md                            LP, convex optimization, gradient methods, duality
│   │   ├── information_theory.md                      Entropy, KL divergence, channel capacity
│   │   ├── numerical_methods.md                       Root finding, integration, ODE solvers
│   │   ├── dynamical_systems.md                       ODEs, PDEs, chaos, stability
│   │   └── stochastic_processes.md                    Markov chains, Brownian motion, MCMC
│   ├── Physics
│   │   ├── classical_mechanics.md                     Newton, Lagrange, Hamilton, orbital mechanics
│   │   ├── electromagnetism.md                        Maxwell's equations, waves, circuits
│   │   ├── thermodynamics_and_statistical_mechanics.md Thermodynamics, entropy, Boltzmann
│   │   ├── quantum_mechanics.md                       Schrodinger equation, qubits, entanglement
│   │   ├── relativity.md                              Special/general relativity, spacetime
│   │   └── optics_and_waves.md                        Wave equation, interference, diffraction
│   └── Engineering Mathematics
│       ├── signal_processing.md                       Fourier/Laplace transforms, filtering, wavelets
│       ├── control_theory.md                          Transfer functions, PID, stability
│       ├── operations_research.md                     LP, network flows, queueing, scheduling
│       └── game_theory.md                             Nash equilibrium, mechanism design, auctions
├── data_science_and_analytics.md                  Data science lifecycle, EDA, feature engineering
├── data_visualization.md                          Chart types, design principles, storytelling
├── statistical_testing_and_experimentation.md     A/B testing, experimental design
├── feature_engineering.md                         Feature creation, selection, transformation
├── ensemble_methods.md                            Bagging, boosting, stacking, voting
├── causal_inference.md                            Causal reasoning, treatment effects
├── data_ethics_and_privacy.md                     Ethical AI, privacy, bias, fairness
└── geospatial_analysis.md                         Spatial data, mapping, GIS
```

## 주제별 파일
### 수학 — 기초
| 파일 | 설명 |
|------|-------------|
| [mathematics.md](mathematics/mathematics.md)| 수체계, 대수학, 기하학, 미적분학, 집합론, 선형대수학 |
| [statistics_and_probability.md](mathematics/statistics_and_probability.md)| 확률이론, 가설검정, 회귀, 베이지안 통계 |
| [logic_and_critical_thinking.md](mathematics/logic_and_critical_thinking.md)| 명제 논리, 부울 대수, 논리적 오류, 논증 평가 |
### 수학 — 순수 수학
| 파일 | 설명 |
|------|-------------|
| [discrete_mathematics.md](mathematics/discrete_mathematics.md)| 집합, 관계, 함수, 조합론, 순환 관계, 함수 생성 |
| [graph_theory.md](mathematics/graph_theory.md)| 그래프, 트리, 순회, 최단 경로, MST, 네트워크 흐름, 스펙트럼 그래프 이론 |
| [number_theory.md](mathematics/number_theory.md)| 소수, 모듈러 연산, 페르마/오일러의 정리, 암호화 |
| [abstract_algebra.md](mathematics/abstract_algebra.md)| 그룹, 링, 필드, 벡터 공간, 고유 이론, 코딩 이론 |
| [real_analysis.md](mathematics/real_analysis.md)| 수열, 극한, 연속성, 리만/르베그 적분, 미터법 공간, 측정 이론 |
### 수학 — 응용 수학
| 파일 | 설명 |
|------|-------------|
| [optimization.md](mathematics/optimization.md)| 선형/볼록 최적화, 경사하강법, 라그랑주 승수, KKT, 이중성 |
| [information_theory.md](mathematics/information_theory.md)| 섀넌 엔트로피, KL 발산, 상호 정보, 채널 용량, 압축 |
| [numerical_methods.md](mathematics/numerical_methods.md)| 부동 소수점, 근 찾기, 수치 적분, ODE 솔버, 안정성 |
| [dynamical_systems.md](mathematics/dynamical_systems.md)| ODE, PDE, 위상 초상화, 카오스, 로렌츠 어트랙터, 분기점 |
| [stochastic_processes.md](mathematics/stochastic_processes.md)| 마르코프 체인, 랜덤 워크, 브라운 운동, 마틴게일, MCMC |
### 수학 — 물리학
| 파일 | 설명 |
|------|-------------|
| [classical_mechanics.md](mathematics/classical_mechanics.md)| 뉴턴의 법칙, 라그랑주/해밀턴 역학, 보존 법칙, 궤도 역학 |
| [electromagnetism.md](mathematics/electromagnetism.md)| 맥스웰 방정식, 전기/자기장, EM파, RLC 회로 |
| [thermodynamics_and_statistical_mechanics.md](mathematics/thermodynamics_and_statistical_mechanics.md)| 열역학 법칙, 엔트로피, 자유 에너지, 볼츠만 분포, 분배 함수 |
| [quantum_mechanics.md](mathematics/quantum_mechanics.md)| 슈뢰딩거 방정식, 불확실성, 중첩, 얽힘, 큐비트, 양자 게이트 |
| [relativity.md](mathematics/relativity.md)| 특수/일반 상대성 이론, 로렌츠 변환, 시공간 곡률 |
| [optics_and_waves.md](mathematics/optics_and_waves.md)| 파동 방정식, 간섭, 회절, 편광, 기하학/푸리에 광학 |
### 수학 — 공학 수학
| 파일 | 설명 |
|------|-------------|
| [signal_processing.md](mathematics/signal_processing.md)| 푸리에/라플라스/Z 변환, FFT, FIR/IIR 필터, 샘플링 정리, 웨이블릿 |
| [control_theory.md](mathematics/control_theory.md)| 전달 함수, PID 제어기, 안정성 분석, 상태공간, 칼만 필터 |
| [operations_research.md](mathematics/operations_research.md)| LP 공식화, 운송 문제, 동적 프로그래밍, 큐잉 이론 |
| [game_theory.md](mathematics/game_theory.md)| 내쉬균형, 미니맥스, 협력게임, 샤플리 가치, 메커니즘 설계 |
### 데이터 과학 및 분석
| 파일 | 설명 |
|------|-------------|
| [data_science_and_analytics.md](data_science_and_analytics.md)| 데이터 과학 수명주기, 탐색적 데이터 분석, 기능 엔지니어링, 파이프라인 |
| [data_visualization.md](data_visualization.md)| 차트 선택, 시각적 인코딩, 대시보드 디자인, 데이터 스토리텔링 |
| [statistical_testing_and_experimentation.md](statistical_testing_and_experimentation.md)| A/B 테스트, 실험 설계, 가설 테스트 실제 |
| [feature_engineering.md](feature_engineering.md)| 기능 생성, 선택, 변환, 인코딩 기술 |
| [ensemble_methods.md](ensemble_methods.md)| 배깅, 부스팅, 스태킹, 투표 - 더 나은 성능을 위한 모델 결합 |
| [causal_inference.md](causal_inference.md)| 인과 추론, 치료 효과, 혼란 요인, 도구 변수 |
| [data_ethics_and_privacy.md](data_ethics_and_privacy.md)| ML의 윤리적 AI, 개인 정보 보호 규정, 편견 탐지, 공정성 |
| [geospatial_analysis.md](geospatial_analysis.md)| 공간 데이터, 매핑, GIS, 지오코딩, 공간 통계 |
## 권장 읽기 경로
### **수학적 기초 과정**
1.`mathematics/mathematics.md`— 핵심 수학 툴킷 구축
2.`mathematics/statistics_and_probability.md`— 데이터로 추론하는 방법 배우기
3.`mathematics/logic_and_critical_thinking.md`— 추론을 강화하세요
4.`mathematics/discrete_mathematics.md`— 형식적 구조 및 계산
5.`mathematics/real_analysis.md`— 미적분학의 엄격한 기초
### **머신러닝 수학 과정**
1.`mathematics/mathematics.md`— 선형 대수학 및 미적분학 기초
2.`mathematics/statistics_and_probability.md`— 확률 및 회귀
3.`mathematics/optimization.md`— 모델 학습 방법(경사하강법, 볼록성)
4.`mathematics/information_theory.md`— 손실 함수, 엔트로피, KL 발산
5.`mathematics/stochastic_processes.md`— 랜덤 프로세스 및 MCMC
6.`mathematics/numerical_methods.md`— 계산 고려 사항
### **데이터 과학 경로**
1.`mathematics/mathematics.md`— 수학 전제 조건
2.`mathematics/statistics_and_probability.md`— 통계적 기초
3.`data_science_and_analytics.md`— 데이터 과학 워크플로
4.`data_visualization.md`— 결과를 효과적으로 전달합니다.
5.`feature_engineering.md`— 모델링을 위한 데이터 준비
### **머신러닝 과정**
1.`mathematics/mathematics.md`— 선형 대수학 및 미적분학
2.`mathematics/statistics_and_probability.md`— 확률 및 회귀
3.`mathematics/optimization.md`— 훈련을 위한 최적화 방법
4.`ensemble_methods.md`— 더 나은 성능을 위한 모델 결합
5.`data_science_and_analytics.md`— 엔드투엔드 ML 파이프라인
### **분석 및 실험 경로**
1.`mathematics/statistics_and_probability.md`— 통계 기반
2.`statistical_testing_and_experimentation.md`— 실험 설계 및 분석
3.`causal_inference.md`— 상관관계를 넘어 인과관계까지 파악
4.`data_ethics_and_privacy.md`— 책임 있는 데이터 관행
### **ML 경로의 물리학**
1.`mathematics/mathematics.md`— 미적분학 및 선형 대수학
2.`mathematics/classical_mechanics.md`— 결정론적 시스템, 해밀턴 역학
3.`mathematics/thermodynamics_and_statistical_mechanics.md`— 엔트로피와 확률
4.`mathematics/quantum_mechanics.md`— 양자 컴퓨팅 기반
5.`mathematics/information_theory.md`— 정보 및 엔트로피 연결
### **신호 처리 및 엔지니어링 경로**
1.`mathematics/mathematics.md`— 미적분학 및 복소수
2.`mathematics/optics_and_waves.md`— 웨이브 기본 사항
3.`mathematics/signal_processing.md`— 변환 및 필터 이론
4.`mathematics/control_theory.md`— 피드백 및 안정성
5.`mathematics/dynamical_systems.md`— 시간 경과에 따른 시스템 동작