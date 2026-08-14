# Khoa học dữ liệu và phân tích
Một bộ sưu tập có cấu trúc gồm các tài liệu tham khảo bao gồm các nền tảng toán học, quy trình công việc khoa học dữ liệu, khái niệm học máy và thực tiễn phân tích cần thiết cho việc đào tạo mô hình AI và ra quyết định dựa trên dữ liệu.
## Kết cấu
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

## Tệp theo chủ đề
### Toán học — Nền tảng
| Tập tin | Mô tả |
|------|-------------|
| [mathematics.md](mathematics/mathematics.md)| Hệ thống số, đại số, hình học, giải tích, lý thuyết tập hợp, đại số tuyến tính |
| [statistics_and_probability.md](mathematics/statistics_and_probability.md)| Lý thuyết xác suất, kiểm định giả thuyết, hồi quy, thống kê Bayes |
| [logic_and_critical_thinking.md](mathematics/logic_and_critical_thinking.md)| Logic mệnh đề, đại số Boolean, ngụy biện logic, đánh giá lập luận |
### Toán học — Toán học thuần túy
| Tập tin | Mô tả |
|------|-------------|
| [discrete_mathematics.md](mathematics/discrete_mathematics.md)| Tập hợp, quan hệ, hàm, tổ hợp, quan hệ truy hồi, hàm sinh |
| [graph_theory.md](mathematics/graph_theory.md)| Đồ thị, cây, đường đi, đường đi ngắn nhất, MST, luồng mạng, lý thuyết đồ thị phổ |
| [number_theory.md](mathematics/number_theory.md)| Số nguyên tố, số học mô đun, định lý Fermat/Euler, mật mã |
| [abstract_algebra.md](mathematics/abstract_algebra.md)| Nhóm, vành, trường, không gian vectơ, lý thuyết riêng, lý thuyết mã hóa |
| [real_analysis.md](mathematics/real_analysis.md)| Chuỗi, giới hạn, tính liên tục, tích phân Riemann/Lebesgue, không gian mêtric, lý thuyết độ đo |
### Toán — Toán ứng dụng
| Tập tin | Mô tả |
|------|-------------|
| [optimization.md](mathematics/optimization.md)| Tối ưu hóa tuyến tính/lồi, giảm độ dốc, hệ số nhân Lagrange, KKT, đối ngẫu |
| [information_theory.md](mathematics/information_theory.md)| Entropy Shannon, phân kỳ KL, thông tin lẫn nhau, dung lượng kênh, nén |
| [numerical_methods.md](mathematics/numerical_methods.md)| Dấu phẩy động, tìm nghiệm, tích phân số, bộ giải ODE, độ ổn định |
| [dynamical_systems.md](mathematics/dynamical_systems.md)| ODE, PDE, chân dung pha, hỗn loạn, lực hút Lorenz, phân nhánh |
| [stochastic_processes.md](mathematics/stochastic_processes.md)| Chuỗi Markov, bước đi ngẫu nhiên, chuyển động Brown, martingales, MCMC |
### Toán — Vật lý
| Tập tin | Mô tả |
|------|-------------|
| [classical_mechanics.md](mathematics/classical_mechanics.md)| Định luật Newton, cơ học Lagrange/Hamilton, định luật bảo toàn, cơ học quỹ đạo |
| [electromagnetism.md](mathematics/electromagnetism.md)| Phương trình Maxwell, điện trường/từ trường, sóng EM, mạch RLC |
| [thermodynamics_and_statistical_mechanics.md](mathematics/thermodynamics_and_statistical_mechanics.md)| Các định luật nhiệt động lực học, entropy, năng lượng tự do, phân bố Boltzmann, hàm phân vùng |
| [quantum_mechanics.md](mathematics/quantum_mechanics.md)| Phương trình Schrodinger, độ bất định, sự chồng chất, sự vướng víu, qubit, cổng lượng tử |
| [relativity.md](mathematics/relativity.md)| Thuyết tương đối đặc biệt/tổng ​​quát, phép biến đổi Lorentz, độ cong không thời gian |
| [optics_and_waves.md](mathematics/optics_and_waves.md)| Phương trình sóng, giao thoa, nhiễu xạ, phân cực, quang học hình học/Fourier |
### Toán học — Toán kỹ thuật
| Tập tin | Mô tả |
|------|-------------|
| [signal_processing.md](mathematics/signal_processing.md)| Biến đổi Fourier/Laplace/Z, bộ lọc FFT, FIR/IIR, định lý lấy mẫu, wavelet |
| [control_theory.md](mathematics/control_theory.md)| Hàm truyền, bộ điều khiển PID, phân tích độ ổn định, không gian trạng thái, bộ lọc Kalman |
| [operations_research.md](mathematics/operations_research.md)| Công thức LP, bài toán vận chuyển, quy hoạch động, lý thuyết xếp hàng |
| [game_theory.md](mathematics/game_theory.md)| Cân bằng Nash, minimax, trò chơi hợp tác, giá trị Shapley, thiết kế cơ chế |
### Khoa học dữ liệu & Phân tích
| Tập tin | Mô tả |
|------|-------------|
| [data_science_and_analytics.md](data_science_and_analytics.md)| Vòng đời khoa học dữ liệu, phân tích dữ liệu khám phá, kỹ thuật tính năng, quy trình |
| [data_visualization.md](data_visualization.md)| Lựa chọn biểu đồ, mã hóa trực quan, thiết kế bảng điều khiển, kể chuyện dữ liệu |
| [statistical_testing_and_experimentation.md](statistical_testing_and_experimentation.md)| A/B testing, thiết kế thử nghiệm, thử nghiệm giả thuyết trong thực tế |
| [feature_engineering.md](feature_engineering.md)| Kỹ thuật tạo, lựa chọn, chuyển đổi, mã hóa tính năng |
| [ensemble_methods.md](ensemble_methods.md)| Đóng gói, tăng cường, xếp chồng, biểu quyết - kết hợp các mô hình để có hiệu suất tốt hơn |
| [causal_inference.md](causal_inference.md)| Lý luận nhân quả, tác dụng điều trị, yếu tố gây nhiễu, biến công cụ |
| [data_ethics_and_privacy.md](data_ethics_and_privacy.md)| AI có đạo đức, quy định về quyền riêng tư, phát hiện sai lệch, tính công bằng trong ML |
| [geospatial_analysis.md](geospatial_analysis.md)| Dữ liệu không gian, lập bản đồ, GIS, mã hóa địa lý, thống kê không gian |
## Đường dẫn đọc được đề xuất
### **Con đường nền tảng toán học**
1.`mathematics/mathematics.md`— Xây dựng bộ công cụ toán học cốt lõi
2.`mathematics/statistics_and_probability.md`— Học cách suy luận với dữ liệu
3.`mathematics/logic_and_critical_thinking.md`— Rèn luyện khả năng lập luận của bạn
4.`mathematics/discrete_mathematics.md`— Cấu trúc hình thức và cách đếm
5.`mathematics/real_analysis.md`— Nền tảng vững chắc của phép tính
### **Lộ trình toán học máy học**
1.`mathematics/mathematics.md`— Đại số tuyến tính và cơ sở giải tích
2.`mathematics/statistics_and_probability.md`- Xác suất và hồi quy
3.`mathematics/optimization.md`- Cách mô hình học (giảm độ dốc, độ lồi)
4.`mathematics/information_theory.md`— Hàm mất mát, entropy, phân kỳ KL
5.`mathematics/stochastic_processes.md`— Quy trình ngẫu nhiên và MCMC
6.`mathematics/numerical_methods.md`— Các cân nhắc tính toán
### **Con đường khoa học dữ liệu**
1.`mathematics/mathematics.md`— Điều kiện tiên quyết về toán
2.`mathematics/statistics_and_probability.md`— Cơ sở thống kê
3.`data_science_and_analytics.md`- Quy trình làm việc của khoa học dữ liệu
4.`data_visualization.md`— Truyền đạt kết quả một cách hiệu quả
5.`feature_engineering.md`— Chuẩn bị dữ liệu cho mô hình hóa
### **Lộ trình học máy**
1.`mathematics/mathematics.md`— Đại số tuyến tính và phép tính
2.`mathematics/statistics_and_probability.md`- Xác suất và hồi quy
3.`mathematics/optimization.md`— Phương pháp tối ưu hóa cho đào tạo
4.`ensemble_methods.md`— Kết hợp các mô hình để có hiệu suất tốt hơn
5.`data_science_and_analytics.md`— Đường dẫn ML từ đầu đến cuối
### **Đường dẫn phân tích và thử nghiệm**
1.`mathematics/statistics_and_probability.md`— Cơ sở thống kê
2.`statistical_testing_and_experimentation.md`— Thiết kế và phân tích thí nghiệm
3.`causal_inference.md`— Vượt xa mối tương quan với quan hệ nhân quả
4.`data_ethics_and_privacy.md`— Thực hành dữ liệu có trách nhiệm
### **Vật lý cho đường dẫn ML**
1.`mathematics/mathematics.md`— Phép tính và đại số tuyến tính
2.`mathematics/classical_mechanics.md`— Hệ thống tất định, cơ học Hamilton
3.`mathematics/thermodynamics_and_statistical_mechanics.md`— Entropy và xác suất
4.`mathematics/quantum_mechanics.md`— Nền tảng điện toán lượng tử
5.`mathematics/information_theory.md`— Kết nối thông tin và entropy
### **Đường dẫn kỹ thuật và xử lý tín hiệu**
1.`mathematics/mathematics.md`- Phép tính và số phức
2.`mathematics/optics_and_waves.md`— Nguyên tắc cơ bản về sóng
3.`mathematics/signal_processing.md`— Lý thuyết biến đổi và lọc
4.`mathematics/control_theory.md`— Phản hồi và ổn định
5.`mathematics/dynamical_systems.md`— Hoạt động của hệ thống theo thời gian