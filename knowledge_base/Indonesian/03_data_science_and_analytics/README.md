# Ilmu Data dan Analisis
Kumpulan dokumen referensi terstruktur yang mencakup dasar matematika, alur kerja ilmu data, konsep pembelajaran mesin, dan praktik analitik yang penting untuk pelatihan model AI dan pengambilan keputusan berdasarkan data.
## Struktur
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

## File berdasarkan Topik
### Matematika — Yayasan
| Berkas | Deskripsi |
|------|-------------|
| [mathematics.md](mathematics/mathematics.md)| Sistem bilangan, aljabar, geometri, kalkulus, teori himpunan, aljabar linier |
| [statistics_and_probability.md](mathematics/statistics_and_probability.md)| Teori probabilitas, pengujian hipotesis, regresi, statistik Bayesian |
| [logic_and_critical_thinking.md](mathematics/logic_and_critical_thinking.md)| Logika proposisional, aljabar Boolean, kesalahan logika, evaluasi argumen |
### Matematika — Matematika Murni
| Berkas | Deskripsi |
|------|-------------|
| [discrete_mathematics.md](mathematics/discrete_mathematics.md)| Himpunan, relasi, fungsi, kombinatorik, relasi perulangan, fungsi pembangkit |
| [graph_theory.md](mathematics/graph_theory.md)| Grafik, pohon, traversal, jalur terpendek, MST, aliran jaringan, teori grafik spektral |
| [number_theory.md](mathematics/number_theory.md)| Bilangan prima, aritmatika modular, teorema Fermat/Euler, kriptografi |
| [abstract_algebra.md](mathematics/abstract_algebra.md)| Grup, cincin, bidang, ruang vektor, teori eigen, teori pengkodean |
| [real_analysis.md](mathematics/real_analysis.md)| Barisan, limit, kontinuitas, integrasi Riemann/Lebesgue, ruang metrik, teori ukuran |
### Matematika — Matematika Terapan
| Berkas | Deskripsi |
|------|-------------|
| [optimization.md](mathematics/optimization.md)| Optimalisasi linier/cembung, penurunan gradien, pengali Lagrange, KKT, dualitas |
| [information_theory.md](mathematics/information_theory.md)| Entropi Shannon, divergensi KL, informasi timbal balik, kapasitas saluran, kompresi |
| [numerical_methods.md](mathematics/numerical_methods.md)| Titik mengambang, pencarian akar, integrasi numerik, pemecah ODE, stabilitas |
| [dynamical_systems.md](mathematics/dynamical_systems.md)| ODE, PDE, potret fase, kekacauan, penarik Lorenz, percabangan |
| [stochastic_processes.md](mathematics/stochastic_processes.md)| Rantai Markov, jalan acak, gerak Brown, martingales, MCMC |
### Matematika — Fisika
| Berkas | Deskripsi |
|------|-------------|
| [classical_mechanics.md](mathematics/classical_mechanics.md)| Hukum Newton, Mekanika Lagrangian/Hamiltonian, Hukum Kekekalan, Mekanika Orbital |
| [electromagnetism.md](mathematics/electromagnetism.md)| Persamaan Maxwell, medan listrik/magnet, gelombang EM, rangkaian RLC |
| [thermodynamics_and_statistical_mechanics.md](mathematics/thermodynamics_and_statistical_mechanics.md)| Hukum termodinamika, entropi, energi bebas, distribusi Boltzmann, fungsi partisi |
| [quantum_mechanics.md](mathematics/quantum_mechanics.md)| Persamaan Schrodinger, ketidakpastian, superposisi, belitan, qubit, gerbang kuantum |
| [relativity.md](mathematics/relativity.md)| Relativitas khusus/umum, transformasi Lorentz, kelengkungan ruangwaktu |
| [optics_and_waves.md](mathematics/optics_and_waves.md)| Persamaan gelombang, interferensi, difraksi, polarisasi, optik geometri/Fourier |
### Matematika — Matematika Teknik
| Berkas | Deskripsi |
|------|-------------|
| [signal_processing.md](mathematics/signal_processing.md)| Transformasi Fourier/Laplace/Z, FFT, filter FIR/IIR, teorema pengambilan sampel, wavelet |
| [control_theory.md](mathematics/control_theory.md)| Fungsi transfer, pengontrol PID, analisis stabilitas, ruang keadaan, filter Kalman |
| [operations_research.md](mathematics/operations_research.md)| Rumusan LP, Masalah Transportasi, Pemrograman Dinamis, Teori Antrian |
| [game_theory.md](mathematics/game_theory.md)| Ekuilibrium Nash, minimax, permainan kooperatif, nilai Shapley, desain mekanisme |
### Ilmu Data & Analisis
| Berkas | Deskripsi |
|------|-------------|
| [data_science_and_analytics.md](data_science_and_analytics.md)| Siklus hidup ilmu data, analisis data eksplorasi, rekayasa fitur, saluran pipa |
| [data_visualization.md](data_visualization.md)| Pemilihan bagan, pengkodean visual, desain dasbor, pengisahan data |
| [statistical_testing_and_experimentation.md](statistical_testing_and_experimentation.md)| Pengujian A/B, desain eksperimental, pengujian hipotesis dalam praktik |
| [feature_engineering.md](feature_engineering.md)| Pembuatan fitur, seleksi, transformasi, teknik pengkodean |
| [ensemble_methods.md](ensemble_methods.md)| Mengantongi, meningkatkan, menumpuk, memilih — menggabungkan model untuk kinerja yang lebih baik |
| [causal_inference.md](causal_inference.md)| Penalaran kausal, efek pengobatan, perancu, variabel instrumental |
| [data_ethics_and_privacy.md](data_ethics_and_privacy.md)| AI etis, peraturan privasi, deteksi bias, keadilan dalam ML |
| [geospatial_analysis.md](geospatial_analysis.md)| Data spasial, pemetaan, GIS, geocoding, statistik spasial |
## Jalur Bacaan yang Disarankan
### **Jalur Landasan Matematika**
1.`mathematics/mathematics.md`- Membangun perangkat matematika inti
2.`mathematics/statistics_and_probability.md`- Belajar bernalar dengan data
3.`mathematics/logic_and_critical_thinking.md`- Pertajam alasan Anda
4.`mathematics/discrete_mathematics.md`— Struktur formal dan penghitungan
5.`mathematics/real_analysis.md`- Dasar kalkulus yang kuat
### **Jalur Matematika Pembelajaran Mesin**
1.`mathematics/mathematics.md`- Aljabar linier dan landasan kalkulus
2.`mathematics/statistics_and_probability.md`— Probabilitas dan regresi
3.`mathematics/optimization.md`- Cara model belajar (penurunan gradien, konveksitas)
4.`mathematics/information_theory.md`- Fungsi kerugian, entropi, divergensi KL
5.`mathematics/stochastic_processes.md`— Proses acak dan MCMC
6.`mathematics/numerical_methods.md`— Pertimbangan komputasi
### **Jalur Ilmu Data**
1.`mathematics/mathematics.md`— Prasyarat matematika
2.`mathematics/statistics_and_probability.md`— Fondasi statistik
3.`data_science_and_analytics.md`— Alur kerja ilmu data
4.`data_visualization.md`— Komunikasikan temuan secara efektif
5.`feature_engineering.md`— Mempersiapkan data untuk pemodelan
### **Jalur Pembelajaran Mesin**
1.`mathematics/mathematics.md`- Aljabar dan kalkulus linier
2.`mathematics/statistics_and_probability.md`— Probabilitas dan regresi
3.`mathematics/optimization.md`— Metode optimasi untuk pelatihan
4.`ensemble_methods.md`— Menggabungkan model untuk performa yang lebih baik
5.`data_science_and_analytics.md`— Saluran ML ujung ke ujung
### **Jalur Analisis dan Eksperimen**
1.`mathematics/statistics_and_probability.md`— Fondasi statistik
2.`statistical_testing_and_experimentation.md`- Merancang dan menganalisis eksperimen
3.`causal_inference.md`- Melampaui korelasi hingga sebab akibat
4.`data_ethics_and_privacy.md`— Praktik data yang bertanggung jawab
### **Fisika untuk Jalur ML**
1.`mathematics/mathematics.md`- Kalkulus dan aljabar linier
2.`mathematics/classical_mechanics.md`- Sistem deterministik, mekanika Hamilton
3.`mathematics/thermodynamics_and_statistical_mechanics.md`— Entropi dan probabilitas
4.`mathematics/quantum_mechanics.md`— Fondasi komputasi kuantum
5.`mathematics/information_theory.md`— Koneksi informasi dan entropi
### **Jalur Rekayasa dan Pemrosesan Sinyal**
1.`mathematics/mathematics.md`- Kalkulus dan bilangan kompleks
2.`mathematics/optics_and_waves.md`— Fundamental gelombang
3.`mathematics/signal_processing.md`- Transformasi dan filter teori
4.`mathematics/control_theory.md`— Umpan balik dan stabilitas
5.`mathematics/dynamical_systems.md`— Perilaku sistem dari waktu ke waktu