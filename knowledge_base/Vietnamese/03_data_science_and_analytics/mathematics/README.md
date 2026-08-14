# Toán học
Một bộ sưu tập toàn diện các tài liệu tham khảo chuyên sâu bao gồm toán học thuần túy, toán ứng dụng, vật lý và toán kỹ thuật - nền tảng định lượng cần thiết cho khoa học dữ liệu, học máy và tính toán khoa học.
## Kết cấu
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

## Tệp theo danh mục
### Nền móng
| Tập tin | Mô tả | Độ khó |
|------|-----------------|-------------|
| [mathematics.md](mathematics.md)| Hệ thống số, đại số, hình học, giải tích, lý thuyết tập hợp, đại số tuyến tính, nhị phân | Trung cấp |
| [statistics_and_probability.md](statistics_and_probability.md)| Lý thuyết xác suất, kiểm định giả thuyết, hồi quy, thống kê Bayes | Trung cấp |
| [logic_and_critical_thinking.md](logic_and_critical_thinking.md)| Logic mệnh đề, đại số Boolean, ngụy biện logic, đánh giá lập luận | Người mới bắt đầu |
### Toán học thuần túy
| Tập tin | Mô tả | Độ khó |
|------|-----------------|-------------|
| [discrete_mathematics.md](discrete_mathematics.md)| Tập hợp, quan hệ, hàm số, tổ hợp, nguyên lý chuồng chim, quan hệ truy hồi, hàm sinh | Trung cấp |
| [graph_theory.md](graph_theory.md)| Biểu diễn đồ thị, cây, truyền tải, đường đi ngắn nhất, MST, luồng mạng, lý thuyết đồ thị phổ | Trung cấp |
| [number_theory.md](number_theory.md)| Tính chia hết, số nguyên tố, số học mô đun, định lý Euler/Fermat, CRT, mật mã | Nâng cao |
| [abstract_algebra.md](abstract_algebra.md)| Nhóm, vành, trường, không gian vectơ, bản đồ tuyến tính, lý thuyết riêng, lý thuyết mã hóa kết nối | Nâng cao |
| [real_analysis.md](real_analysis.md)| Dãy số, chuỗi, giới hạn, tính liên tục, tích phân Riemann/Lebesgue, không gian mêtric, lý thuyết độ đo | Nâng cao |
###Toán ứng dụng
| Tập tin | Mô tả | Độ khó |
|------|-----------------|-------------|
| [optimization.md](optimization.md)| Tối ưu hóa tuyến tính/lồi, giảm độ dốc, hệ số nhân Lagrange, KKT, đối ngẫu, lập trình số nguyên | Trung cấp |
| [information_theory.md](information_theory.md)| Entropy của Shannon, thông tin lẫn nhau, phân kỳ KL, dung lượng kênh, mã hóa nguồn, kết nối ML | Trung cấp |
| [numerical_methods.md](numerical_methods.md)| Dấu phẩy động, tìm nghiệm, tích phân số, bộ giải ODE, nội suy, tính ổn định | Trung cấp |
| [dynamical_systems.md](dynamical_systems.md)| ODE, chân dung pha, độ ổn định Lyapunov, hỗn loạn, lực hút Lorenz, PDE | Nâng cao |
| [stochastic_processes.md](stochastic_processes.md)| Chuỗi Markov, bước đi ngẫu nhiên, chuyển động Brown, quá trình Poisson, martingales, MCMC | Nâng cao |
### Vật lý
| Tập tin | Mô tả | Độ khó |
|------|-----------------|-------------|
| [classical_mechanics.md](classical_mechanics.md)| Định luật Newton, cơ học Lagrange/Hamilton, định luật bảo toàn, cơ học quỹ đạo | Trung cấp |
| [electromagnetism.md](electromagnetism.md)| Điện/từ trường, phương trình Maxwell, sóng EM, mạch RLC | Nâng cao |
| [thermodynamics_and_statistical_mechanics.md](thermodynamics_and_statistical_mechanics.md)| Các định luật nhiệt động lực học, entropy, năng lượng tự do, phân bố Boltzmann, hàm phân vùng | Nâng cao |
| [quantum_mechanics.md](quantum_mechanics.md)| Phương trình Schrodinger, toán tử, độ bất định, sự chồng chất, sự vướng víu, qubit | Nâng cao |
| [relativity.md](relativity.md)| Phép biến đổi Lorentz, sự giãn nở thời gian, sự tương đương khối lượng-năng lượng, giới thiệu về thuyết tương đối rộng | Nâng cao |
| [optics_and_waves.md](optics_and_waves.md)| Phương trình sóng, giao thoa, nhiễu xạ, phân cực, quang học hình học/Fourier | Trung cấp |
### Toán kỹ thuật
| Tập tin | Mô tả | Độ khó |
|------|-----------------|-------------|
| [signal_processing.md](signal_processing.md)| Biến đổi Fourier/Laplace/Z, bộ lọc FFT, FIR/IIR, định lý lấy mẫu, wavelet | Nâng cao |
| [control_theory.md](control_theory.md)| Hàm truyền, bộ điều khiển PID, phân tích độ ổn định, không gian trạng thái, điều khiển tối ưu | Nâng cao |
| [operations_research.md](operations_research.md)| Công thức LP, bài toán vận chuyển, quy hoạch động, lý thuyết xếp hàng, lập lịch | Trung cấp |
| [game_theory.md](game_theory.md)| Cân bằng Nash, minimax, trò chơi hợp tác, giá trị Shapley, thiết kế cơ chế, RL đa tác nhân | Trung cấp |
## Đường dẫn đọc được đề xuất
### Đường dẫn nền tảng toán học
1.`mathematics.md`— Xây dựng bộ công cụ toán học cốt lõi
2.`statistics_and_probability.md`— Học cách suy luận với dữ liệu
3.`logic_and_critical_thinking.md`— Rèn luyện khả năng lập luận của bạn
4.`discrete_mathematics.md`— Cấu trúc hình thức và cách đếm
5.`real_analysis.md`— Nền tảng vững chắc của phép tính
### Lộ trình Toán học Machine Learning
1.`mathematics.md`— Đại số tuyến tính và cơ sở giải tích
2.`statistics_and_probability.md`- Xác suất và hồi quy
3.`optimization.md`— Cách học của mô hình
4.`information_theory.md`— Mất chức năng và thông tin
5.`stochastic_processes.md`— Quy trình ngẫu nhiên và MCMC
6.`numerical_methods.md`— Các cân nhắc tính toán
### Đường dẫn thuật toán và khoa học dữ liệu
1.`mathematics.md`- Toán học cốt lõi
2.`discrete_mathematics.md`— Tổ hợp và cấu trúc
3.`graph_theory.md`— Phân tích mạng
4.`optimization.md`— Phương pháp tối ưu hóa
5.`operations_research.md`— Toán học quyết định
### Vật lý cho đường dẫn ML
1.`mathematics.md`— Phép tính và đại số tuyến tính
2.`classical_mechanics.md`- Hệ thống xác định
3.`thermodynamics_and_statistical_mechanics.md`— Entropy và xác suất
4.`quantum_mechanics.md`— Nền tảng điện toán lượng tử
5.`information_theory.md`— Kết nối thông tin và entropy
### Đường dẫn kỹ thuật và xử lý tín hiệu
1.`mathematics.md`- Phép tính và số phức
2.`optics_and_waves.md`— Nguyên tắc cơ bản về sóng
3.`signal_processing.md`— Lý thuyết biến đổi và lọc
4.`control_theory.md`— Phản hồi và ổn định
5.`dynamical_systems.md`— Hoạt động của hệ thống theo thời gian
## Tài liệu tham khảo chéo
Nhiều tập tin xây dựng trên nhau. Chuỗi phụ thuộc chính:
- **Tối ưu hóa** được xây dựng trên`mathematics.md`(phép tính, đại số tuyến tính) và`real_analysis.md`(hội tụ)
- **Lý thuyết thông tin** kết nối với`statistics_and_probability.md`và`thermodynamics_and_statistical_mechanics.md`(entropy)
- **Cơ học lượng tử** yêu cầu`abstract_algebra.md`(không gian vectơ) và`classical_mechanics.md`(tương tự Hamilton)
- **Xử lý tín hiệu** dựa trên`optics_and_waves.md`(lý thuyết sóng) và`numerical_methods.md`(tính toán FFT)
- **Lý thuyết trò chơi** kết nối với`optimization.md`và`stochastic_processes.md`(chiến lược hỗn hợp, động lực tiến hóa)