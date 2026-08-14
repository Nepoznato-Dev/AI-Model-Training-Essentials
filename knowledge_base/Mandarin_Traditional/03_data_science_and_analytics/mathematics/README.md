# 數學
全面的深入參考文件集合，涵蓋純數學、應用數學、物理和工程數學——數據科學、機器學習和科學計算所必需的定量基礎。
＃＃ 結構
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

## 檔案按類別
### 基礎
|文件|描述 |難度|
|------|-------------|------------|
|[mathematics.md](mathematics.md)|數系、代數、幾何、微積分、集合論、線性代數、二進位 |中級|
|[statistics_and_probability.md](statistics_and_probability.md)|機率論、假設檢定、迴歸、貝葉斯統計 |中級|
|[logic_and_critical_thinking.md](logic_and_critical_thinking.md)|命題邏輯、布林代數、邏輯謬誤、論證評估 |初學者 |
### 純數學
|文件|描述 |難度|
|------|-------------|------------|
|[discrete_mathematics.md](discrete_mathematics.md)|集合、關聯、函數、組合數學、鴿巢原理、遞推關係、生成函數 |中級|
|[graph_theory.md](graph_theory.md)|圖表示、樹、遍歷、最短路徑、MST、網路流、譜圖論 |中階|
|[number_theory.md](number_theory.md)|可整除性、質數、模算術、歐拉/費馬定理、CRT、密碼學 |高級|
|[abstract_algebra.md](abstract_algebra.md)|群、環、域、向量空間、線性映射、本徵理論、編碼理論連結 |高階|
|[real_analysis.md](real_analysis.md)|序列、級數、極限、連續性、黎曼/勒貝格積分、度量空間、測度論 |高階|
### 應用數學
|文件|描述 |難度|
|------|-------------|------------|
|[optimization.md](optimization.md)|線性/凸優化、梯度下降、拉格朗日乘、KKT、對偶性、整數規劃 |中級|
|[information_theory.md](information_theory.md)|香農熵、互資訊、KL 散度、通道容量、來源編碼、ML 連線 |中級|
|[numerical_methods.md](numerical_methods.md)|浮點、求根、數值積分、ODE 解算器、插值、穩定性 |中級|
|[dynamical_systems.md](dynamical_systems.md)|常微分方程、相圖、李雅普諾夫穩定性、混沌、洛倫茲吸引子、偏微分方程 |高階|
|[stochastic_processes.md](stochastic_processes.md)|馬可夫鏈、隨機遊走、布朗運動、泊松過程、鞅、MCMC |進階|
### 物理
|文件|描述 |難度|
|------|-------------|------------|
|[classical_mechanics.md](classical_mechanics.md)|牛頓定律、拉格朗日/哈密爾頓力學、守恆定律、軌道力學 |中級|
|[electromagnetism.md](electromagnetism.md)|電場/磁場、麥克斯韋方程組、電磁波、RLC 電路 |進階|
|[thermodynamics_and_statistical_mechanics.md](thermodynamics_and_statistical_mechanics.md)|熱力學定律、熵、自由能、玻爾茲曼分佈、配分函數 |高階|
|[quantum_mechanics.md](quantum_mechanics.md)|薛丁格方程式、算子、不確定性、疊加、糾纏、量子位元 |進階|
|[relativity.md](relativity.md)|洛倫茲變換、時間膨脹、質能等價、廣義相對論簡介 |高階|
|[optics_and_waves.md](optics_and_waves.md)|波動方程式、干涉、繞射、偏振、幾何/傅立葉光學 |中級|
### 工程數學
|文件|描述 |難度|
|------|-------------|------------|
|[signal_processing.md](signal_processing.md)|傅立葉/拉普拉斯/Z 轉換、FFT、FIR/IIR 濾波器、取樣定理、小波 |進階|
|[control_theory.md](control_theory.md)|傳遞函數、PID 控制器、穩定性分析、狀態空間、最佳控制 |進階|
|[operations_research.md](operations_research.md)| LP 公式、運輸問題、動態規劃、排隊論、調度 |中級|
|[game_theory.md](game_theory.md)|納許均衡、極小極大、合作賽局、Shapley 值、機制設計、多智能體 RL |中級|
## 建議的閱讀路徑
### 數學基礎路徑
1.`mathematics.md`— 建構核心數學工具包
2.`statistics_and_probability.md`— 學習用資料推理
3.`logic_and_critical_thinking.md`— 提升你的推理能力
4.`discrete_mathematics.md`— 形式結構與計數
5.`real_analysis.md`— 嚴格的微積分基礎
### 機器學習數學路徑
1.`mathematics.md`— 線性代數與微積分基礎
2.`statistics_and_probability.md`— 機率和回歸
3.`optimization.md`— 模型如何學習
4.`information_theory.md`— 損失函數與訊息
5.`stochastic_processes.md`— 隨機過程與 MCMC
6.`numerical_methods.md`— 計算考量
### 資料科學與演算法路徑
1.`mathematics.md`— 核心數學
2.`discrete_mathematics.md`— 組合數學與結構
3.`graph_theory.md`— 網路分析
4.`optimization.md`— 最佳化方法
5.`operations_research.md`— 決策數學
### ML 路徑物理
1.`mathematics.md`— 微積分與線性代數
2.`classical_mechanics.md`— 確定性系統
3.`thermodynamics_and_statistical_mechanics.md`— 熵與機率
4.`quantum_mechanics.md`— 量子運算基礎
5.`information_theory.md`— 資訊與熵連接
### 訊號處理與工程路徑
1.`mathematics.md`— 微積分與複數
2.`optics_and_waves.md`— 波浪基本面
3.`signal_processing.md`— 變換與濾波理論
4.`control_theory.md`— 回饋與穩定性
5.`dynamical_systems.md`— 系統隨時間的行為
## 交叉引用
許多文件是相互建構的。關鍵依賴鏈：
- **最佳化** 基於 `mathematics.md`（微積分、線性代數）和 `real_analysis.md`（收斂）
- **資訊理論** 連接到`statistics_and_probability.md`和 `thermodynamics_and_statistical_mechanics.md`（熵）
- **量子力學**需要 `abstract_algebra.md`（向量空間）和 `classical_mechanics.md`（哈密爾頓類比）
- **訊號處理**依賴 `optics_and_waves.md`（波動理論）和 `numerical_methods.md`（FFT 計算）
- **博弈論**連結到`optimization.md`和`stochastic_processes.md`（混合策略，演化動力學）