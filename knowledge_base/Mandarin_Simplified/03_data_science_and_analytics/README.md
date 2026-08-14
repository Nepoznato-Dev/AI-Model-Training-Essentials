# 数据科学与分析
结构化参考文档集合，涵盖人工智能模型训练和数据驱动决策所必需的数学基础、数据科学工作流程、机器学习概念和分析实践。
＃＃ 结构
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

## 按主题分类的文件
### 数学 — 基础
|文件|描述 |
|------|-------------|
| [mathematics.md](mathematics/mathematics.md)|数系、代数、几何、微积分、集合论、线性代数 |
| [statistics_and_probability.md](mathematics/statistics_and_probability.md)|概率论、假设检验、回归、贝叶斯统计 |
| [logic_and_critical_thinking.md](mathematics/logic_and_critical_thinking.md)|命题逻辑、布尔代数、逻辑谬误、论证评估 |
### 数学 — 纯数学
|文件|描述 |
|------|-------------|
| [discrete_mathematics.md](mathematics/discrete_mathematics.md)|集合、关系、函数、组合、递推关系、生成函数 |
| [graph_theory.md](mathematics/graph_theory.md)|图、树、遍历、最短路径、MST、网络流、谱图论 |
| [number_theory.md](mathematics/number_theory.md)|素数、模算术、费马/欧拉定理、密码学 |
| [abstract_algebra.md](mathematics/abstract_algebra.md)|群、环、域、向量空间、本征理论、编码理论 |
| [real_analysis.md](mathematics/real_analysis.md)|序列、极限、连续性、黎曼/勒贝格积分、度量空间、测度论 |
### 数学 — 应用数学
|文件|描述 |
|------|-------------|
| [optimization.md](mathematics/optimization.md)|线性/凸优化、梯度下降、拉格朗日乘子、KKT、对偶性 |
| [information_theory.md](mathematics/information_theory.md)|香农熵、KL 散度、互信息、通道容量、压缩 |
| [numerical_methods.md](mathematics/numerical_methods.md)|浮点、求根、数值积分、ODE 求解器、稳定性 |
| [dynamical_systems.md](mathematics/dynamical_systems.md)|常微分方程、偏微分方程、相图、混沌、洛伦兹吸引子、分岔 |
| [stochastic_processes.md](mathematics/stochastic_processes.md)|马尔可夫链、随机游走、布朗运动、鞅、MCMC |
### 数学 — 物理
|文件|描述 |
|------|-------------|
| [classical_mechanics.md](mathematics/classical_mechanics.md)|牛顿定律、拉格朗日/哈密尔顿力学、守恒定律、轨道力学 |
| [electromagnetism.md](mathematics/electromagnetism.md)|麦克斯韦方程组、电场/磁场、电磁波、RLC 电路 |
| [thermodynamics_and_statistical_mechanics.md](mathematics/thermodynamics_and_statistical_mechanics.md)|热力学定律、熵、自由能、玻尔兹曼分布、配分函数 |
| [quantum_mechanics.md](mathematics/quantum_mechanics.md)|薛定谔方程、不确定性、叠加、纠缠、量子位、量子门 |
| [relativity.md](mathematics/relativity.md)|狭义/广义相对论、洛伦兹变换、时空曲率 |
| [optics_and_waves.md](mathematics/optics_and_waves.md)|波动方程、干涉、衍射、偏振、几何/傅里叶光学 |
### 数学 — 工程数学
|文件|描述 |
|------|-------------|
| [signal_processing.md](mathematics/signal_processing.md)|傅立叶/拉普拉斯/Z 变换、FFT、FIR/IIR 滤波器、采样定理、小波 |
| [control_theory.md](mathematics/control_theory.md)|传递函数、PID 控制器、稳定性分析、状态空间、卡尔曼滤波器 |
| [operations_research.md](mathematics/operations_research.md)| LP 公式、运输问题、动态规划、排队论 |
| [game_theory.md](mathematics/game_theory.md)|纳什均衡、极小极大、合作博弈、沙普利值、机制设计 |
### 数据科学与分析
|文件|描述 |
|------|-------------|
| [data_science_and_analytics.md](data_science_and_analytics.md)|数据科学生命周期、探索性数据分析、特征工程、管道 |
| [data_visualization.md](data_visualization.md)|图表选择、视觉编码、仪表板设计、数据故事 |
| [statistical_testing_and_experimentation.md](statistical_testing_and_experimentation.md)| A/B 测试、实验设计、假设检验在实践中 |
| [feature_engineering.md](feature_engineering.md)|特征创建、选择、转换、编码技术 |
| [ensemble_methods.md](ensemble_methods.md)| bagging、boosting、stacking、voting——组合模型以获得更好的性能 |
| [causal_inference.md](causal_inference.md)|因果推理、治疗效果、混杂因素、工具变量 |
| [data_ethics_and_privacy.md](data_ethics_and_privacy.md)|道德人工智能、隐私法规、偏见检测、机器学习公平性 |
| [geospatial_analysis.md](geospatial_analysis.md)|空间数据、制图、GIS、地理编码、空间统计 |
## 建议的阅读路径
### **数学基础路径**
1.`mathematics/mathematics.md`— 构建核心数学工具包
2.`mathematics/statistics_and_probability.md`— 学习用数据推理
3.`mathematics/logic_and_critical_thinking.md`— 提高你的推理能力
4.`mathematics/discrete_mathematics.md`— 形式结构和计数
5.`mathematics/real_analysis.md`— 严格的微积分基础
### **机器学习数学路径**
1.`mathematics/mathematics.md`— 线性代数和微积分基础
2.`mathematics/statistics_and_probability.md`— 概率和回归
3.`mathematics/optimization.md`— 模型如何学习（梯度下降、凸性）
4.`mathematics/information_theory.md`— 损失函数、熵、KL 散度
5.`mathematics/stochastic_processes.md`— 随机过程和 MCMC
6.`mathematics/numerical_methods.md`— 计算考虑因素
### **数据科学之路**
1.`mathematics/mathematics.md`— 数学先决条件
2.`mathematics/statistics_and_probability.md`— 统计基础
3.`data_science_and_analytics.md`— 数据科学工作流程
4.`data_visualization.md`— 有效地传达调查结果
5.`feature_engineering.md`— 准备建模数据
### **机器学习路径**
1.`mathematics/mathematics.md`— 线性代数和微积分
2.`mathematics/statistics_and_probability.md`— 概率和回归
3.`mathematics/optimization.md`— 训练的优化方法
4.`ensemble_methods.md`— 组合模型以获得更好的性能
5.`data_science_and_analytics.md`— 端到端 ML 管道
### **分析和实验路径**
1.`mathematics/statistics_and_probability.md`— 统计基础
2.`statistical_testing_and_experimentation.md`— 设计和分析实验
3.`causal_inference.md`— 超越相关性到因果关系
4.`data_ethics_and_privacy.md`— 负责任的数据实践
### **机器学习路径的物理**
1.`mathematics/mathematics.md`— 微积分和线性代数
2.`mathematics/classical_mechanics.md`— 确定性系统，哈密顿力学
3.`mathematics/thermodynamics_and_statistical_mechanics.md`— 熵和概率
4.`mathematics/quantum_mechanics.md`— 量子计算基础
5.`mathematics/information_theory.md`— 信息和熵连接
### **信号处理和工程路径**
1.`mathematics/mathematics.md`— 微积分和复数
2.`mathematics/optics_and_waves.md`— 波浪基本面
3.`mathematics/signal_processing.md`— 变换和滤波理论
4.`mathematics/control_theory.md`— 反馈和稳定性
5.`mathematics/dynamical_systems.md`— 系统随时间的行为