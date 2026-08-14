# 수학
데이터 과학, 기계 학습 및 과학 컴퓨팅에 필수적인 정량적 기초인 순수 수학, 응용 수학, 물리학 및 공학 수학을 다루는 포괄적인 심층 참조 문서 컬렉션입니다.
## 구조
```
mathematics/
├── README.md                                    ← You are here
│
├── Foundations (existing)
│   ├── mathematics.md                              Core math: number systems, algebra, calculus, linear algebra
│   ├── statistics_and_probability.md               Probability, inference, regression, Bayesian methods
│   └── logic_and_critical_thinking.md              Formal logic, fallacies, argument analysis
│
├── Pure Mathematics
│   ├── discrete_mathematics.md                     Sets, relations, combinatorics, recurrence, generating functions
│   ├── graph_theory.md                             Graphs, trees, traversals, shortest paths, network flows
│   ├── number_theory.md                            Primes, modular arithmetic, cryptography
│   ├── abstract_algebra.md                         Groups, rings, fields, vector spaces
│   └── real_analysis.md                            Limits, continuity, integration, metric spaces, measure theory
│
├── Applied Mathematics
│   ├── optimization.md                             Linear/convex optimization, gradient methods, duality
│   ├── information_theory.md                       Entropy, KL divergence, channel capacity, compression
│   ├── numerical_methods.md                        Root finding, integration, ODE solvers, stability
│   ├── dynamical_systems.md                        ODEs, PDEs, chaos, stability, bifurcations
│   └── stochastic_processes.md                     Markov chains, Brownian motion, MCMC
│
├── Physics
│   ├── classical_mechanics.md                      Newton, Lagrange, Hamilton, orbital mechanics
│   ├── electromagnetism.md                         Maxwell's equations, waves, circuits
│   ├── thermodynamics_and_statistical_mechanics.md  Laws of thermodynamics, entropy, Boltzmann
│   ├── quantum_mechanics.md                        Schrodinger equation, qubits, entanglement
│   ├── relativity.md                               Special/general relativity, spacetime
│   └── optics_and_waves.md                         Wave equation, interference, diffraction, Fourier optics
│
└── Engineering Mathematics
    ├── signal_processing.md                        Fourier/Laplace transforms, filtering, wavelets
    ├── control_theory.md                           Transfer functions, PID, stability analysis
    ├── operations_research.md                      LP, network flows, queueing, scheduling
    └── game_theory.md                              Nash equilibrium, mechanism design, auctions
```

## 카테고리별 파일
### 기초
| 파일 | 설명 | 난이도 |
|------|-------------|------------|
| [mathematics.md](mathematics.md)| 수 체계, 대수학, 기하학, 미적분학, 집합론, 선형 대수학, 이진법 | 중급 |
| [statistics_and_probability.md](statistics_and_probability.md)| 확률이론, 가설검정, 회귀, 베이지안 통계 | 중급 |
| [logic_and_critical_thinking.md](logic_and_critical_thinking.md)| 명제 논리, 부울 대수, 논리적 오류, 논증 평가 | 초보자 |
### 순수 수학
| 파일 | 설명 | 난이도 |
|------|-------------|------------|
| [discrete_mathematics.md](discrete_mathematics.md)| 집합, 관계, 함수, 조합론, 비둘기집 원리, 순환 관계, 함수 생성 | 중급 |
| [graph_theory.md](graph_theory.md)| 그래프 표현, 트리, 순회, 최단 경로, MST, 네트워크 흐름, 스펙트럼 그래프 이론 | 중급 |
| [number_theory.md](number_theory.md)| 가분성, 소수, 모듈러 연산, 오일러/페르마의 정리, CRT, 암호화 | 고급 |
| [abstract_algebra.md](abstract_algebra.md)| 그룹, 링, 필드, 벡터 공간, 선형 맵, 고유 이론, 코딩 이론 연결 | 고급 |
| [real_analysis.md](real_analysis.md)| 수열, 급수, 극한, 연속성, 리만/르베그 적분, 미터법 공간, 측정 이론 | 고급 |
### 응용수학
| 파일 | 설명 | 난이도 |
|------|-------------|------------|
| [optimization.md](optimization.md)| 선형/볼록 최적화, 경사하강법, 라그랑주 승수, KKT, 이중성, 정수 프로그래밍 | 중급 |
| [information_theory.md](information_theory.md)| 섀넌 엔트로피, 상호 정보, KL 발산, 채널 용량, 소스 코딩, ML 연결 | 중급 |
| [numerical_methods.md](numerical_methods.md)| 부동 소수점, 근 찾기, 수치 적분, ODE 풀이, 보간, 안정성 | 중급 |
| [dynamical_systems.md](dynamical_systems.md)| ODE, 위상 초상화, Lyapunov 안정성, 혼돈, 로렌츠 어트랙터, PDE | 고급 |
| [stochastic_processes.md](stochastic_processes.md)| 마르코프 체인, 랜덤 워크, 브라운 운동, 포아송 과정, 마틴게일, MCMC | 고급 |
### 물리학
| 파일 | 설명 | 난이도 |
|------|-------------|------------|
| [classical_mechanics.md](classical_mechanics.md)| 뉴턴의 법칙, 라그랑주/해밀턴 역학, 보존 법칙, 궤도 역학 | 중급 |
| [electromagnetism.md](electromagnetism.md)| 전기/자기장, 맥스웰 방정식, EM파, RLC 회로 | 고급 |
| [thermodynamics_and_statistical_mechanics.md](thermodynamics_and_statistical_mechanics.md)| 열역학 법칙, 엔트로피, 자유 에너지, 볼츠만 분포, 분배 함수 | 고급 |
| [quantum_mechanics.md](quantum_mechanics.md)| 슈뢰딩거 방정식, 연산자, 불확실성, 중첩, 얽힘, 큐비트 | 고급 |
| [relativity.md](relativity.md)| 로렌츠 변환, 시간 팽창, 질량-에너지 등가성, 일반 상대성 이론 입문 | 고급 |
| [optics_and_waves.md](optics_and_waves.md)| 파동방정식, 간섭, 회절, 편광, 기하/푸리에 광학 | 중급 |
### 공학 수학
| 파일 | 설명 | 난이도 |
|------|-------------|------------|
| [signal_processing.md](signal_processing.md)| 푸리에/라플라스/Z 변환, FFT, FIR/IIR 필터, 샘플링 정리, 웨이블릿 | 고급 |
| [control_theory.md](control_theory.md)| 전달함수, PID 제어기, 안정성 분석, 상태공간, 최적 제어 | 고급 |
| [operations_research.md](operations_research.md)| LP 공식화, 운송 문제, 동적 프로그래밍, 큐잉 이론, 스케줄링 | 중급 |
| [game_theory.md](game_theory.md)| 내쉬 균형, 미니맥스, 협력 게임, 샤플리 가치, 메커니즘 설계, 다중 에이전트 RL | 중급 |
## 권장 읽기 경로
### 수학 기초 경로
1.`mathematics.md`— 핵심 수학 툴킷 구축
2.`statistics_and_probability.md`— 데이터로 추론하는 방법 배우기
3.`logic_and_critical_thinking.md`— 추론을 강화하세요
4.`discrete_mathematics.md`— 형식적 구조 및 계산
5.`real_analysis.md`— 미적분학의 엄격한 기초
### 머신러닝 수학 경로
1.`mathematics.md`— 선형 대수학 및 미적분학 기초
2.`statistics_and_probability.md`— 확률 및 회귀
3.`optimization.md`— 모델 학습 방법
4.`information_theory.md`— 손실 기능 및 정보
5.`stochastic_processes.md`— 랜덤 프로세스 및 MCMC
6.`numerical_methods.md`— 계산 고려 사항
### 데이터 과학 및 알고리즘 경로
1.`mathematics.md`— 핵심 수학
2.`discrete_mathematics.md`— 조합 및 구조
3.`graph_theory.md`— 네트워크 분석
4.`optimization.md`— 최적화 방법
5.`operations_research.md`— 의사결정 수학
### ML 경로의 물리학
1.`mathematics.md`— 미적분학 및 선형 대수학
2.`classical_mechanics.md`— 결정론적 시스템
3.`thermodynamics_and_statistical_mechanics.md`— 엔트로피와 확률
4.`quantum_mechanics.md`— 양자 컴퓨팅 기반
5.`information_theory.md`— 정보 및 엔트로피 연결
### 신호 처리 및 엔지니어링 경로
1.`mathematics.md`— 미적분학 및 복소수
2.`optics_and_waves.md`— 웨이브 기본 사항
3.`signal_processing.md`— 변환 및 필터 이론
4.`control_theory.md`— 피드백 및 안정성
5.`dynamical_systems.md`— 시간 경과에 따른 시스템 동작
## 상호 참조
많은 파일이 서로를 기반으로 구축됩니다. 주요 종속성 체인:
- **최적화**는 `mathematics.md`(미적분학, 선형 대수학) 및 `real_analysis.md`(수렴)를 기반으로 합니다.
- **정보 이론**은`statistics_and_probability.md`및 `thermodynamics_and_statistical_mechanics.md`(엔트로피)에 연결됩니다.
- **양자 역학**에는 `abstract_algebra.md`(벡터 공간) 및 `classical_mechanics.md`(해밀턴 유추)가 필요합니다.
- **신호 처리**는 `optics_and_waves.md`(파동 이론) 및 `numerical_methods.md`(FFT 계산)에 의존합니다.
- **게임 이론**은`optimization.md`및 `stochastic_processes.md`에 연결됩니다(혼합 전략, 진화 역학)