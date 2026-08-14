# 數據科學與分析
結構化參考文件集合，涵蓋人工智慧模型訓練和資料驅動決策所必需的數學基礎、資料科學工作流程、機器學習概念和分析實踐。
＃＃ 結構
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

## 按主題分類的文件
### 數學 — 基礎
|文件|描述 |
|------|-------------|
|[mathematics.md](mathematics/mathematics.md)|數系、代數、幾何、微積分、集合論、線性代數 |
|[statistics_and_probability.md](mathematics/statistics_and_probability.md)|機率論、假設檢定、迴歸、貝葉斯統計 |
|[logic_and_critical_thinking.md](mathematics/logic_and_critical_thinking.md)|命題邏輯、布林代數、邏輯謬誤、論證評估 |
### 數學 — 純數學
|文件|描述 |
|------|-------------|
|[discrete_mathematics.md](mathematics/discrete_mathematics.md)|集合、關聯、函數、組合、遞推關係、生成函數 |
|[graph_theory.md](mathematics/graph_theory.md)|圖、樹、遍歷、最短路徑、MST、網路流程、譜圖論 |
|[number_theory.md](mathematics/number_theory.md)|素數、模算術、費馬/歐拉定理、密碼學 |
|[abstract_algebra.md](mathematics/abstract_algebra.md)|群、環、域、向量空間、本徵理論、編碼理論 |
|[real_analysis.md](mathematics/real_analysis.md)|序列、極限、連續性、黎曼/勒貝格積分、度量空間、測度論 |
### 数学 — 应用数学
|文件|描述 |
|------|-------------|
|[optimization.md](mathematics/optimization.md)|線性/凸優化、梯度下降、拉格朗日乘、KKT、對偶性 |
|[information_theory.md](mathematics/information_theory.md)|香農熵、KL 散度、互資訊、通道容量、壓縮 |
|[numerical_methods.md](mathematics/numerical_methods.md)|浮點、求根、數值積分、ODE 解算器、穩定性 |
|[dynamical_systems.md](mathematics/dynamical_systems.md)|常微分方程、偏微分方程、相圖、混沌、洛倫茲吸引子、分岔 |
|[stochastic_processes.md](mathematics/stochastic_processes.md)|馬可夫鏈、隨機遊走、布朗運動、鞅、MCMC |
### 數學 — 物理
|文件|描述 |
|------|-------------|
|[classical_mechanics.md](mathematics/classical_mechanics.md)|牛頓定律、拉格朗日/哈密爾頓力學、守恆定律、軌道力學 |
|[electromagnetism.md](mathematics/electromagnetism.md)|麥克斯韋方程組、電場/磁場、電磁波、RLC 電路 |
|[thermodynamics_and_statistical_mechanics.md](mathematics/thermodynamics_and_statistical_mechanics.md)|熱力學定律、熵、自由能、玻爾茲曼分佈、配分函數 |
|[quantum_mechanics.md](mathematics/quantum_mechanics.md)|薛丁格方程式、不確定性、疊加、糾纏、量子位元、量子閘 |
|[relativity.md](mathematics/relativity.md)|狹義/廣義相對論、洛倫茲變換、時空曲率 |
|[optics_and_waves.md](mathematics/optics_and_waves.md)|波動方程式、干涉、繞射、偏振、幾何/傅立葉光學 |
### 數學 — 工程數學
|文件|描述 |
|------|-------------|
|[signal_processing.md](mathematics/signal_processing.md)|傅立葉/拉普拉斯/Z 轉換、FFT、FIR/IIR 濾波器、取樣定理、小波 |
|[control_theory.md](mathematics/control_theory.md)|傳輸函數、PID 控制器、穩定性分析、狀態空間、卡爾曼濾波器 |
|[operations_research.md](mathematics/operations_research.md)| LP 公式、運輸問題、動態規劃、排隊理論 |
|[game_theory.md](mathematics/game_theory.md)|納許均衡、極小極大、合作賽局、沙普利值、機制設計 |
### 資料科學與分析
|文件|描述 |
|------|-------------|
|[data_science_and_analytics.md](data_science_and_analytics.md)|資料科學生命週期、探索性資料分析、特徵工程、管道 |
|[data_visualization.md](data_visualization.md)|圖表選擇、視覺編碼、儀表板設計、資料故事 |
|[statistical_testing_and_experimentation.md](statistical_testing_and_experimentation.md)| A/B 測試、實驗設計、假設檢定在實務上 |
|[feature_engineering.md](feature_engineering.md)|特徵建立、選擇、轉換、編碼技術 |
|[ensemble_methods.md](ensemble_methods.md)| bagging、boosting、stacking、voting——組合模型以獲得更好的效能 |
|[causal_inference.md](causal_inference.md)|因果推理、治療效果、混雜因素、工具變數 |
|[data_ethics_and_privacy.md](data_ethics_and_privacy.md)|道德人工智慧、隱私法規、偏見偵測、機器學習公平性 |
|[geospatial_analysis.md](geospatial_analysis.md)|空間資料、製圖、GIS、地理編碼、空間統計 |
## 建議的閱讀路徑
### **數學基礎路徑**
1.`mathematics/mathematics.md`— 建構核心數學工具包
2.`mathematics/statistics_and_probability.md`— 學習用資料推理
3.`mathematics/logic_and_critical_thinking.md`— 提升你的推理能力
4.`mathematics/discrete_mathematics.md`— 形式結構與計數
5.`mathematics/real_analysis.md`— 嚴格的微積分基礎
### **機器學習數學路徑**
1.`mathematics/mathematics.md`— 線性代數與微積分基礎
2.`mathematics/statistics_and_probability.md`— 機率和回歸
3.`mathematics/optimization.md`— 模型如何學習（梯度下降、凸性）
4.`mathematics/information_theory.md`— 損失函數、熵、KL 散度
5.`mathematics/stochastic_processes.md`— 隨機過程與 MCMC
6.`mathematics/numerical_methods.md`— 計算考量
### **數據科學之路**
1.`mathematics/mathematics.md`— 數學先決條件
2.`mathematics/statistics_and_probability.md`— 統計基礎
3.`data_science_and_analytics.md`— 資料科學工作流程
4.`data_visualization.md`— 有效傳達調查結果
5.`feature_engineering.md`— 準備建模數據
### **機器學習路徑**
1.`mathematics/mathematics.md`— 線性代數與微積分
2.`mathematics/statistics_and_probability.md`— 機率和回歸
3.`mathematics/optimization.md`— 訓練的最佳化方法
4.`ensemble_methods.md`— 組合模型以獲得更好的效能
5.`data_science_and_analytics.md`— 端對端 ML 管道
### **分析與實驗路徑**
1.`mathematics/statistics_and_probability.md`— 統計基礎
2.`statistical_testing_and_experimentation.md`— 設計與分析實驗
3.`causal_inference.md`— 超越相關性到因果關係
4.`data_ethics_and_privacy.md`— 負責任的資料實踐
### **機器學習路徑的物理**
1.`mathematics/mathematics.md`— 微積分與線性代數
2.`mathematics/classical_mechanics.md`— 確定性系統，哈密頓力學
3.`mathematics/thermodynamics_and_statistical_mechanics.md`— 熵與機率
4.`mathematics/quantum_mechanics.md`— 量子運算基礎
5.`mathematics/information_theory.md`— 資訊與熵連接
### **訊號處理與工程路徑**
1.`mathematics/mathematics.md`— 微積分與複數
2.`mathematics/optics_and_waves.md`— 波浪基本面
3.`mathematics/signal_processing.md`— 變換與濾波理論
4.`mathematics/control_theory.md`— 回饋與穩定性
5.`mathematics/dynamical_systems.md`— 系統隨時間的行為