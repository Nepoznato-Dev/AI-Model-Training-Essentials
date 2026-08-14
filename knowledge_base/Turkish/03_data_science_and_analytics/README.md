# Veri Bilimi ve Analitik
Yapay zeka modeli eğitimi ve veriye dayalı karar verme için gerekli olan matematiksel temelleri, veri bilimi iş akışlarını, makine öğrenimi kavramlarını ve analitik uygulamalarını kapsayan yapılandırılmış bir referans belgeleri koleksiyonu.
## Yapı
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

## Konuya Göre Dosyalar
### Matematik — Temeller
| Dosya | Açıklama |
|------|-----------------|
| [mathematics.md](mathematics/mathematics.md)| Sayı sistemleri, cebir, geometri, analiz, küme teorisi, doğrusal cebir |
| [statistics_and_probability.md](mathematics/statistics_and_probability.md)| Olasılık teorisi, hipotez testi, regresyon, Bayes istatistikleri |
| [logic_and_critical_thinking.md](mathematics/logic_and_critical_thinking.md)| Önerme mantığı, Boole cebiri, mantıksal yanılgılar, argüman değerlendirmesi |
### Matematik — Saf Matematik
| Dosya | Açıklama |
|------|-----------------|
| [discrete_mathematics.md](mathematics/discrete_mathematics.md)| Kümeler, ilişkiler, fonksiyonlar, kombinatorik, yineleme ilişkileri, fonksiyon üretme |
| [graph_theory.md](mathematics/graph_theory.md)| Grafikler, ağaçlar, geçişler, en kısa yollar, MST'ler, ağ akışları, spektral grafik teorisi |
| [number_theory.md](mathematics/number_theory.md)| Asal sayılar, modüler aritmetik, Fermat/Euler teoremleri, kriptografi |
| [abstract_algebra.md](mathematics/abstract_algebra.md)| Gruplar, halkalar, alanlar, vektör uzayları, öz teorisi, kodlama teorisi |
| [real_analysis.md](mathematics/real_analysis.md)| Diziler, limitler, süreklilik, Riemann/Lebesgue entegrasyonu, metrik uzaylar, ölçü teorisi |
### Matematik — Uygulamalı Matematik
| Dosya | Açıklama |
|------|-----------------|
| [optimization.md](mathematics/optimization.md)| Doğrusal/dışbükey optimizasyon, gradyan inişi, Lagrange çarpanları, KKT, dualite |
| [information_theory.md](mathematics/information_theory.md)| Shannon entropisi, KL ıraksaması, karşılıklı bilgi, kanal kapasitesi, sıkıştırma |
| [numerical_methods.md](mathematics/numerical_methods.md)| Kayan nokta, kök bulma, sayısal entegrasyon, ODE çözücüler, kararlılık |
| [dynamical_systems.md](mathematics/dynamical_systems.md)| ODE'ler, PDE'ler, faz portreleri, kaos, Lorenz çekicisi, çatallanmalar |
| [stochastic_processes.md](mathematics/stochastic_processes.md)| Markov zincirleri, rastgele yürüyüşler, Brown hareketi, martingales, MCMC |
### Matematik — Fizik
| Dosya | Açıklama |
|------|-----------------|
| [classical_mechanics.md](mathematics/classical_mechanics.md)| Newton yasaları, Lagrange/Hamilton mekaniği, korunum yasaları, yörünge mekaniği |
| [electromagnetism.md](mathematics/electromagnetism.md)| Maxwell denklemleri, elektrik/manyetik alanlar, EM dalgalar, RLC devreleri |
| [thermodynamics_and_statistical_mechanics.md](mathematics/thermodynamics_and_statistical_mechanics.md)| Termodinamik yasalar, entropi, serbest enerji, Boltzmann dağılımı, bölme fonksiyonları |
| [quantum_mechanics.md](mathematics/quantum_mechanics.md)| Schrödinger denklemi, belirsizlik, süperpozisyon, dolaşıklık, kübitler, kuantum kapıları |
| [relativity.md](mathematics/relativity.md)| Özel/genel görelilik, Lorentz dönüşümleri, uzay-zaman eğriliği |
| [optics_and_waves.md](mathematics/optics_and_waves.md)| Dalga denklemi, girişim, kırınım, polarizasyon, geometrik/Fourier optiği |
### Matematik — Mühendislik Matematiği
| Dosya | Açıklama |
|------|-----------------|
| [signal_processing.md](mathematics/signal_processing.md)| Fourier/Laplace/Z-dönüşümleri, FFT, FIR/IIR filtreleri, örnekleme teoremi, dalgacıklar |
| [control_theory.md](mathematics/control_theory.md)| Transfer fonksiyonları, PID kontrolörleri, kararlılık analizi, durum uzayı, Kalman filtresi |
| [operations_research.md](mathematics/operations_research.md)| LP formülasyonları, taşıma problemleri, dinamik programlama, kuyruk teorisi |
| [game_theory.md](mathematics/game_theory.md)| Nash dengesi, minimax, işbirlikçi oyunlar, Shapley değeri, mekanizma tasarımı |
### Veri Bilimi ve Analitik
| Dosya | Açıklama |
|------|-----------------|
| [data_science_and_analytics.md](data_science_and_analytics.md)| Veri bilimi yaşam döngüsü, keşif amaçlı veri analizi, özellik mühendisliği, işlem hatları |
| [data_visualization.md](data_visualization.md)| Grafik seçimi, görsel kodlama, gösterge tablosu tasarımı, veri hikayesi anlatımı |
| [statistical_testing_and_experimentation.md](statistical_testing_and_experimentation.md)| A/B testi, deneysel tasarım, pratikte hipotez testi |
| [feature_engineering.md](feature_engineering.md)| Özellik oluşturma, seçme, dönüştürme, kodlama teknikleri |
| [ensemble_methods.md](ensemble_methods.md)| Paketleme, artırma, istifleme, oylama — daha iyi performans için modelleri birleştirme |
| [causal_inference.md](causal_inference.md)| Nedensel akıl yürütme, tedavi etkileri, karıştırıcılar, araçsal değişkenler |
| [data_ethics_and_privacy.md](data_ethics_and_privacy.md)| Makine öğreniminde etik yapay zeka, gizlilik düzenlemeleri, önyargı tespiti, adalet |
| [geospatial_analysis.md](geospatial_analysis.md)| Mekansal veriler, haritalama, GIS, coğrafi kodlama, mekansal istatistik |
## Önerilen Okuma Yolları
### **Matematiksel Temeller Yolu**
1.`mathematics/mathematics.md`— Temel matematik araç setini oluşturun
2.`mathematics/statistics_and_probability.md`— Verilerle mantık yürütmeyi öğrenin
3.`mathematics/logic_and_critical_thinking.md`— Mantığınızı keskinleştirin
4.`mathematics/discrete_mathematics.md`— Biçimsel yapılar ve sayma
5.`mathematics/real_analysis.md`— Analizin sağlam temelleri
### **Makine Öğrenimi Matematik Yolu**
1.`mathematics/mathematics.md`— Doğrusal cebir ve analizin temelleri
2.`mathematics/statistics_and_probability.md`— Olasılık ve regresyon
3.`mathematics/optimization.md`— Modeller nasıl öğrenir (gradyan inişi, dışbükeylik)
4.`mathematics/information_theory.md`— Kayıp fonksiyonları, entropi, KL ıraksaması
5.`mathematics/stochastic_processes.md`— Rastgele süreçler ve MCMC
6.`mathematics/numerical_methods.md`— Hesaplamayla ilgili hususlar
### **Veri Bilimi Yolu**
1.`mathematics/mathematics.md`— Matematik önkoşulları
2.`mathematics/statistics_and_probability.md`— İstatistiksel temeller
3.`data_science_and_analytics.md`— Veri bilimi iş akışı
4.`data_visualization.md`— Bulguları etkili bir şekilde iletin
5.`feature_engineering.md`— Verileri modelleme için hazırlayın
### **Makine Öğrenimi Yolu**
1.`mathematics/mathematics.md`— Doğrusal cebir ve analiz
2.`mathematics/statistics_and_probability.md`— Olasılık ve regresyon
3.`mathematics/optimization.md`— Eğitim için optimizasyon yöntemleri
4.`ensemble_methods.md`— Daha iyi performans için modelleri birleştirme
5.`data_science_and_analytics.md`— Uçtan uca makine öğrenimi ardışık düzenleri
### **Analiz ve Deneme Yolu**
1.`mathematics/statistics_and_probability.md`— İstatistiksel temeller
2.`statistical_testing_and_experimentation.md`— Deneyleri tasarlayın ve analiz edin
3.`causal_inference.md`— Korelasyonun ötesine geçip nedenselliğe gidin
4.`data_ethics_and_privacy.md`— Sorumlu veri uygulamaları
### **ML Yolu için Fizik**
1.`mathematics/mathematics.md`— Matematik ve doğrusal cebir
2.`mathematics/classical_mechanics.md`— Deterministik sistemler, Hamilton mekaniği
3.`mathematics/thermodynamics_and_statistical_mechanics.md`— Entropi ve olasılık
4.`mathematics/quantum_mechanics.md`— Kuantum hesaplamanın temelleri
5.`mathematics/information_theory.md`— Bilgi ve entropi bağlantıları
### **Sinyal İşleme ve Mühendislik Yolu**
1.`mathematics/mathematics.md`— Matematik ve karmaşık sayılar
2.`mathematics/optics_and_waves.md`— Dalganın temelleri
3.`mathematics/signal_processing.md`— Dönüşüm ve filtreleme teorisi
4.`mathematics/control_theory.md`— Geri bildirim ve kararlılık
5.`mathematics/dynamical_systems.md`— Zaman içindeki sistem davranışı