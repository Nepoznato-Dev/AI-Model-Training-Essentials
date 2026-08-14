# วิทยาศาสตร์ข้อมูลและการวิเคราะห์
คอลเลกชันเอกสารอ้างอิงที่มีโครงสร้างซึ่งครอบคลุมพื้นฐานทางคณิตศาสตร์ เวิร์กโฟลว์วิทยาศาสตร์ข้อมูล แนวคิดการเรียนรู้ของเครื่อง และแนวทางปฏิบัติในการวิเคราะห์ที่จำเป็นสำหรับการฝึกอบรมโมเดล AI และการตัดสินใจที่ขับเคลื่อนด้วยข้อมูล
## โครงสร้าง
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

## ไฟล์ตามหัวข้อ
### คณิตศาสตร์ — รากฐาน
| ไฟล์ | คำอธิบาย |
|-|-------------|
| [mathematics.md](mathematics/mathematics.md)| ระบบจำนวน พีชคณิต เรขาคณิต แคลคูลัส ทฤษฎีเซต พีชคณิตเชิงเส้น |
| [statistics_and_probability.md](mathematics/statistics_and_probability.md)| ทฤษฎีความน่าจะเป็น การทดสอบสมมติฐาน การถดถอย สถิติแบบเบย์ |
| [logic_and_critical_thinking.md](mathematics/logic_and_critical_thinking.md)| ตรรกะเชิงประพจน์ พีชคณิตแบบบูลีน การเข้าใจผิดเชิงตรรกะ การประเมินข้อโต้แย้ง |
### คณิตศาสตร์ — คณิตศาสตร์ล้วนๆ
| ไฟล์ | คำอธิบาย |
|-|-------------|
| [discrete_mathematics.md](mathematics/discrete_mathematics.md)| เซต ความสัมพันธ์ ฟังก์ชัน เชิงผสม ความสัมพันธ์การเกิดซ้ำ ฟังก์ชันการสร้าง |
| [graph_theory.md](mathematics/graph_theory.md)| กราฟ ต้นไม้ การสำรวจเส้นทางที่สั้นที่สุด MST การไหลของเครือข่าย ทฤษฎีกราฟสเปกตรัม |
| [number_theory.md](mathematics/number_theory.md)| ไพรม์, เลขคณิตโมดูลาร์, ทฤษฎีบทของแฟร์มาต์/ออยเลอร์, วิทยาการเข้ารหัสลับ |
| [abstract_algebra.md](mathematics/abstract_algebra.md)| หมู่ วงแหวน สนาม ปริภูมิเวกเตอร์ ทฤษฎีไอเกน ทฤษฎีการเข้ารหัส |
| [real_analysis.md](mathematics/real_analysis.md)| ลำดับ ขีดจำกัด ความต่อเนื่อง การบูรณาการรีมันน์/เลเบส ปริภูมิเมตริก ทฤษฎีการวัด |
### คณิตศาสตร์ — คณิตศาสตร์ประยุกต์
| ไฟล์ | คำอธิบาย |
|-|-------------|
| [optimization.md](mathematics/optimization.md)| การเพิ่มประสิทธิภาพเชิงเส้น/นูน, การไล่ระดับสี, ตัวคูณลากรองจ์, KKT, ความเป็นคู่ |
| [information_theory.md](mathematics/information_theory.md)| แชนนอนเอนโทรปี, ความแตกต่างของ KL, ข้อมูลร่วมกัน, ความจุของช่องสัญญาณ, การบีบอัด |
| [numerical_methods.md](mathematics/numerical_methods.md)| จุดทศนิยม, การค้นหารูท, การอินทิเกรตเชิงตัวเลข, ตัวแก้ปัญหา ODE, ความเสถียร |
| [dynamical_systems.md](mathematics/dynamical_systems.md)| ODE, PDE, ภาพบุคคลในเฟส, ความโกลาหล, ตัวดึงดูด Lorenz, การแยกส่วน |
| [stochastic_processes.md](mathematics/stochastic_processes.md)| โซ่มาร์คอฟ, การเดินแบบสุ่ม, การเคลื่อนที่แบบบราวเนียน, มาร์ติงเกล, MCMC |
### คณิตศาสตร์ — ฟิสิกส์
| ไฟล์ | คำอธิบาย |
|-|-------------|
| [classical_mechanics.md](mathematics/classical_mechanics.md)| กฎของนิวตัน กลศาสตร์ลากรองจ์/แฮมิลโทเนียน กฎการอนุรักษ์ กลศาสตร์วงโคจร |
| [electromagnetism.md](mathematics/electromagnetism.md)| สมการของแมกซ์เวลล์ สนามไฟฟ้า/แม่เหล็ก คลื่นอีเอ็ม วงจรอาร์แอลซี
| [thermodynamics_and_statistical_mechanics.md](mathematics/thermodynamics_and_statistical_mechanics.md)| กฎอุณหพลศาสตร์ เอนโทรปี พลังงานอิสระ การกระจายตัวของโบลต์ซมันน์ ฟังก์ชันพาร์ติชัน |
| [quantum_mechanics.md](mathematics/quantum_mechanics.md)| สมการชโรดิงเจอร์ ความไม่แน่นอน การซ้อน การพัวพัน ควิบิต ประตูควอนตัม |
| [relativity.md](mathematics/relativity.md)| ทฤษฎีสัมพัทธภาพพิเศษ/ทั่วไป การแปลงลอเรนซ์ ความโค้งของกาลอวกาศ |
| [optics_and_waves.md](mathematics/optics_and_waves.md)| สมการคลื่น การรบกวน การเลี้ยวเบน โพลาไรเซชัน เรขาคณิต/เลนส์ฟูเรียร์ |
### คณิตศาสตร์ — คณิตศาสตร์วิศวกรรม
| ไฟล์ | คำอธิบาย |
|-|-------------|
| [signal_processing.md](mathematics/signal_processing.md)| การแปลงฟูริเยร์/ลาปลาซ/Z, FFT, ตัวกรอง FIR/IIR, ทฤษฎีบทการสุ่มตัวอย่าง, เวฟเล็ต |
| [control_theory.md](mathematics/control_theory.md)| ฟังก์ชันถ่ายโอน, ตัวควบคุม PID, การวิเคราะห์ความเสถียร, พื้นที่สถานะ, ตัวกรองคาลมาน |
| [operations_research.md](mathematics/operations_research.md)| สูตรแอลพี ปัญหาการขนส่ง โปรแกรมไดนามิก ทฤษฎีคิว |
| [game_theory.md](mathematics/game_theory.md)| สมดุลของแนช มินิแมกซ์ เกมร่วมมือ ค่าแชปลีย์ การออกแบบกลไก
### วิทยาศาสตร์ข้อมูลและการวิเคราะห์
| ไฟล์ | คำอธิบาย |
|-|-------------|
| [data_science_and_analytics.md](data_science_and_analytics.md)| วงจรชีวิตวิทยาศาสตร์ข้อมูล การวิเคราะห์ข้อมูลเชิงสำรวจ วิศวกรรมเชิงคุณลักษณะ ไปป์ไลน์ |
| [data_visualization.md](data_visualization.md)| การเลือกแผนภูมิ การเข้ารหัสด้วยภาพ การออกแบบแดชบอร์ด การเล่าเรื่องของข้อมูล |
| [statistical_testing_and_experimentation.md](statistical_testing_and_experimentation.md)| การทดสอบ A/B การออกแบบการทดลอง การทดสอบสมมติฐานในทางปฏิบัติ |
| [feature_engineering.md](feature_engineering.md)| การสร้างคุณสมบัติ การเลือก การแปลง เทคนิคการเข้ารหัส |
| [ensemble_methods.md](ensemble_methods.md)| การบรรจุ การเพิ่ม การวางซ้อน การลงคะแนน — การรวมโมเดลเพื่อประสิทธิภาพที่ดีขึ้น |
| [causal_inference.md](causal_inference.md)| การใช้เหตุผลเชิงสาเหตุ ผลการรักษา สิ่งรบกวน ตัวแปรเครื่องมือ |
| [data_ethics_and_privacy.md](data_ethics_and_privacy.md)| AI ที่มีจริยธรรม, กฎระเบียบด้านความเป็นส่วนตัว, การตรวจจับอคติ, ความเป็นธรรมใน ML |
| [geospatial_analysis.md](geospatial_analysis.md)| ข้อมูลเชิงพื้นที่ การทำแผนที่ GIS การเข้ารหัสทางภูมิศาสตร์ สถิติเชิงพื้นที่ |
## เส้นทางการอ่านที่แนะนำ
### **เส้นทางพื้นฐานทางคณิตศาสตร์**
1.`mathematics/mathematics.md`— สร้างชุดเครื่องมือหลักทางคณิตศาสตร์
2.`mathematics/statistics_and_probability.md`— เรียนรู้การใช้เหตุผลด้วยข้อมูล
3.`mathematics/logic_and_critical_thinking.md`— ทำให้เหตุผลของคุณคมชัดขึ้น
4.`mathematics/discrete_mathematics.md`— โครงสร้างที่เป็นทางการและการนับ
5.`mathematics/real_analysis.md`— รากฐานแคลคูลัสที่เข้มงวด
### **เส้นทางคณิตศาสตร์การเรียนรู้ของเครื่อง**
1.`mathematics/mathematics.md`— รากฐานพีชคณิตเชิงเส้นและแคลคูลัส
2.`mathematics/statistics_and_probability.md`— ความน่าจะเป็นและการถดถอย
3.`mathematics/optimization.md`— โมเดลเรียนรู้อย่างไร (การไล่ระดับสี การนูน)
4.`mathematics/information_theory.md`- ฟังก์ชันการสูญเสีย, เอนโทรปี, ความแตกต่างของ KL
5.`mathematics/stochastic_processes.md`— กระบวนการสุ่มและ MCMC
6.`mathematics/numerical_methods.md`— ข้อควรพิจารณาในการคำนวณ
### **เส้นทางวิทยาศาสตร์ข้อมูล**
1.`mathematics/mathematics.md`— ข้อกำหนดเบื้องต้นทางคณิตศาสตร์
2.`mathematics/statistics_and_probability.md`— รากฐานทางสถิติ
3.`data_science_and_analytics.md`— ขั้นตอนการทำงานด้านวิทยาศาสตร์ข้อมูล
4.`data_visualization.md`— สื่อสารการค้นพบอย่างมีประสิทธิภาพ
5.`feature_engineering.md`— เตรียมข้อมูลสำหรับการสร้างแบบจำลอง
### **เส้นทางการเรียนรู้ของเครื่อง**
1.`mathematics/mathematics.md`— พีชคณิตเชิงเส้นและแคลคูลัส
2.`mathematics/statistics_and_probability.md`— ความน่าจะเป็นและการถดถอย
3.`mathematics/optimization.md`— วิธีการเพิ่มประสิทธิภาพสำหรับการฝึกอบรม
4.`ensemble_methods.md`— ผสมผสานรุ่นต่างๆ เพื่อประสิทธิภาพที่ดีขึ้น
5.`data_science_and_analytics.md`— ไปป์ไลน์ ML แบบ end-to-end
### **เส้นทางการวิเคราะห์และการทดลอง**
1.`mathematics/statistics_and_probability.md`— รากฐานทางสถิติ
2.`statistical_testing_and_experimentation.md`— ออกแบบและวิเคราะห์การทดลอง
3.`causal_inference.md`— ก้าวไปไกลกว่าความสัมพันธ์ถึงสาเหตุ
4.`data_ethics_and_privacy.md`— แนวทางปฏิบัติด้านข้อมูลที่มีความรับผิดชอบ
### **ฟิสิกส์สำหรับเส้นทาง ML**
1.`mathematics/mathematics.md`— แคลคูลัสและพีชคณิตเชิงเส้น
2.`mathematics/classical_mechanics.md`— ระบบกำหนด กลศาสตร์แฮมิลตัน
3.`mathematics/thermodynamics_and_statistical_mechanics.md`— เอนโทรปีและความน่าจะเป็น
4.`mathematics/quantum_mechanics.md`— รากฐานการคำนวณควอนตัม
5.`mathematics/information_theory.md`— การเชื่อมต่อข้อมูลและเอนโทรปี
### **เส้นทางการประมวลผลสัญญาณและวิศวกรรม**
1.`mathematics/mathematics.md`— แคลคูลัสและจำนวนเชิงซ้อน
2.`mathematics/optics_and_waves.md`— ปัจจัยพื้นฐานของคลื่น
3.`mathematics/signal_processing.md`— ทฤษฎีการแปลงและกรอง
4.`mathematics/control_theory.md`— ข้อเสนอแนะและความเสถียร
5.`mathematics/dynamical_systems.md`— พฤติกรรมของระบบเมื่อเวลาผ่านไป