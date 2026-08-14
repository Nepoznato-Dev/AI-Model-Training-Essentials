# 数学
全面的深入参考文档集合，涵盖纯数学、应用数学、物理和工程数学——数据科学、机器学习和科学计算所必需的定量基础。
＃＃ 结构
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

## 文件按类别
### 基础
|文件|描述 |难度|
|------|-------------|------------|
| [mathematics.md](mathematics.md)| Number systems, algebra, geometry, calculus, set theory, linear algebra, binary |中级|
| [statistics_and_probability.md](statistics_and_probability.md)| Probability theory, hypothesis testing, regression, Bayesian statistics |中级|
| [logic_and_critical_thinking.md](logic_and_critical_thinking.md)| Propositional logic, Boolean algebra, logical fallacies, argument evaluation |初学者 |
### 纯数学
|文件|描述 |难度|
|------|-------------|------------|
| [discrete_mathematics.md](discrete_mathematics.md)|集合、关系、函数、组合数学、鸽巢原理、递推关系、生成函数 |中级|
| [graph_theory.md](graph_theory.md)|图表示、树、遍历、最短路径、MST、网络流、谱图论 |中级|
| [number_theory.md](number_theory.md)|可整除性、素数、模算术、欧拉/费马定理、CRT、密码学 |高级|
| [abstract_algebra.md](abstract_algebra.md)|群、环、域、向量空间、线性映射、本征理论、编码理论联系 |高级|
| [real_analysis.md](real_analysis.md)|序列、级数、极限、连续性、黎曼/勒贝格积分、度量空间、测度论 |高级|
### 应用数学
|文件|描述 |难度|
|------|-------------|------------|
| [optimization.md](optimization.md)|线性/凸优化、梯度下降、拉格朗日乘子、KKT、对偶性、整数规划 |中级|
| [information_theory.md](information_theory.md)|香农熵、互信息、KL 散度、信道容量、源编码、ML 连接 |中级|
| [numerical_methods.md](numerical_methods.md)|浮点、求根、数值积分、ODE 求解器、插值、稳定性 |中级|
| [dynamical_systems.md](dynamical_systems.md)|常微分方程、相图、李雅普诺夫稳定性、混沌、洛伦兹吸引子、偏微分方程 |高级|
| [stochastic_processes.md](stochastic_processes.md)|马尔可夫链、随机游走、布朗运动、泊松过程、鞅、MCMC |高级|
### 物理
|文件|描述 |难度|
|------|-------------|------------|
| [classical_mechanics.md](classical_mechanics.md)|牛顿定律、拉格朗日/哈密尔顿力学、守恒定律、轨道力学 |中级|
| [electromagnetism.md](electromagnetism.md)|电场/磁场、麦克斯韦方程组、电磁波、RLC 电路 |高级|
| [thermodynamics_and_statistical_mechanics.md](thermodynamics_and_statistical_mechanics.md)|热力学定律、熵、自由能、玻尔兹曼分布、配分函数 |高级|
| [quantum_mechanics.md](quantum_mechanics.md)|薛定谔方程、算子、不确定性、叠加、纠缠、量子位 |高级|
| [relativity.md](relativity.md)|洛伦兹变换、时间膨胀、质能等效、广义相对论简介 |高级|
| [optics_and_waves.md](optics_and_waves.md)|波动方程、干涉、衍射、偏振、几何/傅立叶光学 |中级|
### 工程数学
|文件|描述 |难度|
|------|-------------|------------|
| [signal_processing.md](signal_processing.md)|傅立叶/拉普拉斯/Z 变换、FFT、FIR/IIR 滤波器、采样定理、小波 |高级|
| [control_theory.md](control_theory.md)|传递函数、PID 控制器、稳定性分析、状态空间、最优控制 |高级|
| [operations_research.md](operations_research.md)| LP 公式、运输问题、动态规划、排队论、调度 |中级|
| [game_theory.md](game_theory.md)|纳什均衡、极小极大、合作博弈、Shapley 值、机制设计、多智能体 RL |中级|
## 建议的阅读路径
### 数学基础路径
1.`mathematics.md`— 构建核心数学工具包
2.`statistics_and_probability.md`— 学习用数据推理
3.`logic_and_critical_thinking.md`— 提高你的推理能力
4.`discrete_mathematics.md`— 形式结构和计数
5.`real_analysis.md`— 严格的微积分基础
### 机器学习数学路径
1.`mathematics.md`— 线性代数和微积分基础
2.`statistics_and_probability.md`— 概率和回归
3.`optimization.md`— 模型如何学习
4.`information_theory.md`— 损失函数和信息
5.`stochastic_processes.md`— 随机过程和 MCMC
6.`numerical_methods.md`— 计算考虑因素
### 数据科学和算法路径
1.`mathematics.md`— 核心数学
2.`discrete_mathematics.md`— 组合数学和结构
3.`graph_theory.md`— 网络分析
4.`optimization.md`— 优化方法
5.`operations_research.md`— 决策数学
### ML 路径物理
1.`mathematics.md`— 微积分和线性代数
2.`classical_mechanics.md`— 确定性系统
3.`thermodynamics_and_statistical_mechanics.md`— 熵和概率
4.`quantum_mechanics.md`— 量子计算基础
5.`information_theory.md`— 信息和熵连接
### 信号处理和工程路径
1.`mathematics.md`— 微积分和复数
2.`optics_and_waves.md`— 波浪基本面
3.`signal_processing.md`— 变换和滤波理论
4.`control_theory.md`— 反馈和稳定性
5.`dynamical_systems.md`— 系统随时间的行为
## 交叉引用
许多文件是相互构建的。关键依赖链：
- **优化** 基于 `mathematics.md`（微积分、线性代数）和 `real_analysis.md`（收敛）
- **信息论** 连接到`statistics_and_probability.md`和 `thermodynamics_and_statistical_mechanics.md`（熵）
- **量子力学**需要 `abstract_algebra.md`（向量空间）和 `classical_mechanics.md`（哈密尔顿类比）
- **信号处理**依赖于 `optics_and_waves.md`（波动理论）和 `numerical_methods.md`（FFT 计算）
- **博弈论**连接到`optimization.md`和`stochastic_processes.md`（混合策略，进化动力学）