# Matematik
Saf matematik, uygulamalı matematik, fizik ve mühendislik matematiğini (veri bilimi, makine öğrenimi ve bilimsel hesaplama için gerekli olan niceliksel temeller) kapsayan kapsamlı, derinlemesine referans belgelerinden oluşan bir koleksiyon.
## Yapı
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

## Kategoriye Göre Dosyalar
### Temeller
| Dosya | Açıklama | Zorluk |
|------|-------------|------------|
| [mathematics.md](mathematics.md)| Sayı sistemleri, cebir, geometri, analiz, küme teorisi, doğrusal cebir, ikili | Orta düzey |
| [statistics_and_probability.md](statistics_and_probability.md)| Olasılık teorisi, hipotez testi, regresyon, Bayes istatistikleri | Orta düzey |
| [logic_and_critical_thinking.md](logic_and_critical_thinking.md)| Önerme mantığı, Boole cebiri, mantıksal yanılgılar, argüman değerlendirmesi | Başlangıç ​​|
### Saf Matematik
| Dosya | Açıklama | Zorluk |
|------|-------------|------------|
| [discrete_mathematics.md](discrete_mathematics.md)| Kümeler, ilişkiler, fonksiyonlar, kombinatorik, güvercin yuvası ilkesi, yineleme ilişkileri, fonksiyon üretme | Orta düzey |
| [graph_theory.md](graph_theory.md)| Grafik gösterimleri, ağaçlar, geçişler, en kısa yollar, MST'ler, ağ akışları, spektral grafik teorisi | Orta düzey |
| [number_theory.md](number_theory.md)| Bölünebilirlik, asal sayılar, modüler aritmetik, Euler/Fermat teoremleri, CRT, kriptografi | Gelişmiş |
| [abstract_algebra.md](abstract_algebra.md)| Gruplar, halkalar, alanlar, vektör uzayları, doğrusal haritalar, öz teori, kodlama teorisi bağlantıları | Gelişmiş |
| [real_analysis.md](real_analysis.md)| Diziler, seriler, limitler, süreklilik, Riemann/Lebesgue entegrasyonu, metrik uzaylar, ölçü teorisi | Gelişmiş |
### Uygulamalı Matematik
| Dosya | Açıklama | Zorluk |
|------|-------------|------------|
| [optimization.md](optimization.md)| Doğrusal/dışbükey optimizasyon, gradyan iniş, Lagrange çarpanları, KKT, dualite, tamsayı programlama | Orta düzey |
| [information_theory.md](information_theory.md)| Shannon entropisi, karşılıklı bilgi, KL farklılığı, kanal kapasitesi, kaynak kodlama, ML bağlantıları | Orta düzey |
| [numerical_methods.md](numerical_methods.md)| Kayan nokta, kök bulma, sayısal entegrasyon, ODE çözücüler, enterpolasyon, kararlılık | Orta düzey |
| [dynamical_systems.md](dynamical_systems.md)| ODE'ler, faz portreleri, Lyapunov kararlılığı, kaos, Lorenz çekicisi, PDE'ler | Gelişmiş |
| [stochastic_processes.md](stochastic_processes.md)| Markov zincirleri, rastgele yürüyüşler, Brown hareketi, Poisson süreçleri, martingaller, MCMC | Gelişmiş |
### Fizik
| Dosya | Açıklama | Zorluk |
|------|-------------|------------|
| [classical_mechanics.md](classical_mechanics.md)| Newton yasaları, Lagrange/Hamilton mekaniği, korunum yasaları, yörünge mekaniği | Orta düzey |
| [electromagnetism.md](electromagnetism.md)| Elektrik/manyetik alanlar, Maxwell denklemleri, EM dalgalar, RLC devreleri | Gelişmiş |
| [thermodynamics_and_statistical_mechanics.md](thermodynamics_and_statistical_mechanics.md)| Termodinamik yasalar, entropi, serbest enerji, Boltzmann dağılımı, bölme fonksiyonları | Gelişmiş |
| [quantum_mechanics.md](quantum_mechanics.md)| Schrödinger denklemi, operatörler, belirsizlik, süperpozisyon, dolaşma, kübitler | Gelişmiş |
| [relativity.md](relativity.md)| Lorentz dönüşümleri, zaman genişlemesi, kütle-enerji denkliği, genel göreliliğe giriş | Gelişmiş |
| [optics_and_waves.md](optics_and_waves.md)| Dalga denklemi, girişim, kırınım, polarizasyon, geometrik/Fourier optiği | Orta düzey |
### Mühendislik Matematiği
| Dosya | Açıklama | Zorluk |
|------|-------------|------------|
| [signal_processing.md](signal_processing.md)| Fourier/Laplace/Z-dönüşümleri, FFT, FIR/IIR filtreleri, örnekleme teoremi, dalgacıklar | Gelişmiş |
| [control_theory.md](control_theory.md)| Transfer fonksiyonları, PID kontrolörleri, kararlılık analizi, durum uzayı, optimal kontrol | Gelişmiş |
| [operations_research.md](operations_research.md)| LP formülasyonları, taşıma problemleri, dinamik programlama, kuyruk teorisi, çizelgeleme | Orta düzey |
| [game_theory.md](game_theory.md)| Nash dengesi, minimax, işbirlikçi oyunlar, Shapley değeri, mekanizma tasarımı, çoklu ajan RL | Orta düzey |
## Önerilen Okuma Yolları
### Matematiksel Temeller Yolu
1.`mathematics.md`— Temel matematik araç setini oluşturun
2.`statistics_and_probability.md`— Verilerle mantık yürütmeyi öğrenin
3.`logic_and_critical_thinking.md`— Mantığınızı keskinleştirin
4.`discrete_mathematics.md`— Biçimsel yapılar ve sayma
5.`real_analysis.md`— Analizin sağlam temelleri
### Makine Öğrenimi Matematik Yolu
1.`mathematics.md`— Doğrusal cebir ve analizin temelleri
2.`statistics_and_probability.md`— Olasılık ve regresyon
3.`optimization.md`— Modeller nasıl öğrenir?
4.`information_theory.md`— Kayıp fonksiyonları ve bilgileri
5.`stochastic_processes.md`— Rastgele süreçler ve MCMC
6.`numerical_methods.md`— Hesaplamayla ilgili hususlar
### Veri Bilimi ve Algoritma Yolu
1.`mathematics.md`— Temel matematik
2.`discrete_mathematics.md`— Kombinatorikler ve yapılar
3.`graph_theory.md`— Ağ analizi
4.`optimization.md`— Optimizasyon yöntemleri
5.`operations_research.md`— Karar matematiği
### ML Yolu için Fizik
1.`mathematics.md`— Matematik ve doğrusal cebir
2.`classical_mechanics.md`— Deterministik sistemler
3.`thermodynamics_and_statistical_mechanics.md`— Entropi ve olasılık
4.`quantum_mechanics.md`— Kuantum hesaplamanın temelleri
5.`information_theory.md`— Bilgi ve entropi bağlantıları
### Sinyal İşleme ve Mühendislik Yolu
1.`mathematics.md`— Matematik ve karmaşık sayılar
2.`optics_and_waves.md`— Dalganın temelleri
3.`signal_processing.md`— Dönüşüm ve filtreleme teorisi
4.`control_theory.md`— Geri bildirim ve kararlılık
5.`dynamical_systems.md`— Zaman içindeki sistem davranışı
## Çapraz Referanslar
Birçok dosya birbirinin üzerine kuruludur. Anahtar bağımlılık zincirleri:
- **Optimizasyon**`mathematics.md`(matematik, doğrusal cebir) ve`real_analysis.md`(yakınsama) üzerine kurulmuştur
- **Bilgi Teorisi**`statistics_and_probability.md`ve `thermodynamics_and_statistical_mechanics.md`'ye (entropi) bağlanır
- **Kuantum Mekaniği**,`abstract_algebra.md`(vektör uzayları) ve`classical_mechanics.md`(Hamilton analojisi) gerektirir
- **Sinyal İşleme**`optics_and_waves.md`(dalga teorisi) ve `numerical_methods.md`'ye (FFT hesaplaması) dayanır
- **Oyun Teorisi**`optimization.md`ve `stochastic_processes.md`'ye bağlanır (karma stratejiler, evrimsel dinamikler)