# คณิตศาสตร์
คอลเลกชันเอกสารอ้างอิงเชิงลึกที่ครอบคลุมซึ่งครอบคลุมถึงคณิตศาสตร์ล้วนๆ คณิตศาสตร์ประยุกต์ ฟิสิกส์ และคณิตศาสตร์วิศวกรรม ซึ่งเป็นรากฐานเชิงปริมาณที่จำเป็นสำหรับวิทยาศาสตร์ข้อมูล การเรียนรู้ของเครื่อง และการคำนวณทางวิทยาศาสตร์
## โครงสร้าง
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

## ไฟล์ตามหมวดหมู่
### มูลนิธิ
| ไฟล์ | คำอธิบาย | ความยาก |
|------|-------------|------------|
| [mathematics.md](mathematics.md)| ระบบจำนวน พีชคณิต เรขาคณิต แคลคูลัส ทฤษฎีเซต พีชคณิตเชิงเส้น ไบนารี | ระดับกลาง |
| [statistics_and_probability.md](statistics_and_probability.md)| ทฤษฎีความน่าจะเป็น การทดสอบสมมติฐาน การถดถอย สถิติแบบเบย์ | ระดับกลาง |
| [logic_and_critical_thinking.md](logic_and_critical_thinking.md)| ตรรกะเชิงประพจน์ พีชคณิตแบบบูลีน การเข้าใจผิดเชิงตรรกะ การประเมินข้อโต้แย้ง | ระดับเริ่มต้น |
### คณิตศาสตร์ล้วนๆ
| ไฟล์ | คำอธิบาย | ความยาก |
|------|-------------|------------|
| [discrete_mathematics.md](discrete_mathematics.md)| เซต ความสัมพันธ์ ฟังก์ชัน เชิงร่วม หลักการนกพิราบ ความสัมพันธ์การเกิดซ้ำ ฟังก์ชันการสร้าง | ระดับกลาง |
| [graph_theory.md](graph_theory.md)| การแสดงกราฟ ต้นไม้ การเคลื่อนที่ผ่าน เส้นทางที่สั้นที่สุด MST การไหลของเครือข่าย ทฤษฎีกราฟสเปกตรัม | ระดับกลาง |
| [number_theory.md](number_theory.md)| การหารลงตัว จำนวนเฉพาะ เลขคณิตโมดูลาร์ ทฤษฎีบทของออยเลอร์/แฟร์มาต์ ซีอาร์ที การเข้ารหัส | ขั้นสูง |
| [abstract_algebra.md](abstract_algebra.md)| หมู่ วงแหวน ฟิลด์ สเปซเวกเตอร์ แผนที่เชิงเส้น ทฤษฎีไอเจน การเชื่อมโยงทฤษฎีการเข้ารหัส | ขั้นสูง |
| [real_analysis.md](real_analysis.md)| ลำดับ อนุกรม ขีดจำกัด ความต่อเนื่อง การอินทิเกรตรีมันน์/เลอเบสก์ ปริภูมิเมตริก ทฤษฎีการวัด | ขั้นสูง |
### คณิตศาสตร์ประยุกต์
| ไฟล์ | คำอธิบาย | ความยาก |
|------|-------------|------------|
| [optimization.md](optimization.md)| การเพิ่มประสิทธิภาพเชิงเส้น/นูน, การไล่ระดับสี, ตัวคูณลากรองจ์, KKT, ความเป็นคู่, การโปรแกรมจำนวนเต็ม ระดับกลาง |
| [information_theory.md](information_theory.md)| เอนโทรปีของแชนนอน, ข้อมูลร่วมกัน, ความแตกต่างของ KL, ความจุของช่องสัญญาณ, การเข้ารหัสแหล่งที่มา, การเชื่อมต่อ ML ระดับกลาง |
| [numerical_methods.md](numerical_methods.md)| จุดทศนิยม, การค้นหารูท, การอินทิเกรตเชิงตัวเลข, ตัวแก้ปัญหา ODE, การประมาณค่า, ความเสถียร | ระดับกลาง |
| [dynamical_systems.md](dynamical_systems.md)| ODE, การถ่ายภาพบุคคลในเฟส, เสถียรภาพของ Lyapunov, ความโกลาหล, ตัวดึงดูด Lorenz, PDE | ขั้นสูง |
| [stochastic_processes.md](stochastic_processes.md)| โซ่มาร์คอฟ, การเดินแบบสุ่ม, การเคลื่อนที่แบบบราวเนียน, กระบวนการปัวซง, มาร์ติงเกล, MCMC | ขั้นสูง |
### ฟิสิกส์
| ไฟล์ | คำอธิบาย | ความยาก |
|------|-------------|------------|
| [classical_mechanics.md](classical_mechanics.md)| กฎของนิวตัน กลศาสตร์ลากรองจ์/แฮมิลโทเนียน กฎการอนุรักษ์ กลศาสตร์วงโคจร | ระดับกลาง |
| [electromagnetism.md](electromagnetism.md)| สนามไฟฟ้า/แม่เหล็ก สมการของแมกซ์เวลล์ คลื่นอีเอ็ม วงจรอาร์แอลซี | ขั้นสูง |
| [thermodynamics_and_statistical_mechanics.md](thermodynamics_and_statistical_mechanics.md)| กฎอุณหพลศาสตร์ เอนโทรปี พลังงานอิสระ การกระจายตัวของโบลต์ซมันน์ ฟังก์ชันพาร์ติชัน | ขั้นสูง |
| [quantum_mechanics.md](quantum_mechanics.md)| สมการชโรดิงเจอร์ ตัวดำเนินการ ความไม่แน่นอน การซ้อน การพัวพัน ควิบิต | ขั้นสูง |
| [relativity.md](relativity.md)| การแปลงแบบลอเรนซ์ การขยายเวลา ความเท่าเทียมกันของมวล-พลังงาน ทฤษฎีสัมพัทธภาพทั่วไปเบื้องต้น | ขั้นสูง |
| [optics_and_waves.md](optics_and_waves.md)| สมการคลื่น การรบกวน การเลี้ยวเบน โพลาไรซ์ เรขาคณิต/ฟูเรียร์ออพติค | ระดับกลาง |
### คณิตศาสตร์วิศวกรรมศาสตร์
| ไฟล์ | คำอธิบาย | ความยาก |
|------|-------------|------------|
| [signal_processing.md](signal_processing.md)| การแปลงฟูริเยร์/ลาปลาซ/Z, FFT, ตัวกรอง FIR/IIR, ทฤษฎีบทการสุ่มตัวอย่าง, เวฟเล็ต | ขั้นสูง |
| [control_theory.md](control_theory.md)| ฟังก์ชันถ่ายโอน, ตัวควบคุม PID, การวิเคราะห์ความเสถียร, พื้นที่สถานะ, การควบคุมที่เหมาะสม | ขั้นสูง |
| [operations_research.md](operations_research.md)| สูตร LP ปัญหาการขนส่ง โปรแกรมไดนามิก ทฤษฎีคิว การกำหนดเวลา ระดับกลาง |
| [game_theory.md](game_theory.md)| สมดุลของแนช, มินิแมกซ์, เกมร่วมมือ, ค่าแชปลีย์, การออกแบบกลไก, RL หลายเอเจนต์ ระดับกลาง |
## เส้นทางการอ่านที่แนะนำ
### เส้นทางพื้นฐานทางคณิตศาสตร์
1.`mathematics.md`— สร้างชุดเครื่องมือหลักทางคณิตศาสตร์
2.`statistics_and_probability.md`— เรียนรู้การใช้เหตุผลด้วยข้อมูล
3.`logic_and_critical_thinking.md`— ทำให้เหตุผลของคุณคมชัดขึ้น
4.`discrete_mathematics.md`— โครงสร้างที่เป็นทางการและการนับ
5.`real_analysis.md`— รากฐานแคลคูลัสที่เข้มงวด
### เส้นทางคณิตศาสตร์การเรียนรู้ของเครื่อง
1.`mathematics.md`— รากฐานพีชคณิตเชิงเส้นและแคลคูลัส
2.`statistics_and_probability.md`— ความน่าจะเป็นและการถดถอย
3.`optimization.md`— โมเดลเรียนรู้อย่างไร
4.`information_theory.md`— ฟังก์ชันและข้อมูลการสูญเสีย
5.`stochastic_processes.md`— กระบวนการสุ่มและ MCMC
6.`numerical_methods.md`— ข้อควรพิจารณาในการคำนวณ
### เส้นทางวิทยาศาสตร์ข้อมูลและอัลกอริทึม
1.`mathematics.md`— คณิตศาสตร์หลัก
2.`discrete_mathematics.md`— เชิงผสมผสานและโครงสร้าง
3.`graph_theory.md`— การวิเคราะห์เครือข่าย
4.`optimization.md`— วิธีการเพิ่มประสิทธิภาพ
5.`operations_research.md`— คณิตศาสตร์เพื่อการตัดสินใจ
### ฟิสิกส์สำหรับเส้นทาง ML
1.`mathematics.md`— แคลคูลัสและพีชคณิตเชิงเส้น
2.`classical_mechanics.md`— ระบบกำหนด
3.`thermodynamics_and_statistical_mechanics.md`— เอนโทรปีและความน่าจะเป็น
4.`quantum_mechanics.md`— รากฐานการคำนวณควอนตัม
5.`information_theory.md`— การเชื่อมต่อข้อมูลและเอนโทรปี
### เส้นทางการประมวลผลสัญญาณและวิศวกรรม
1.`mathematics.md`— แคลคูลัสและจำนวนเชิงซ้อน
2.`optics_and_waves.md`— ปัจจัยพื้นฐานของคลื่น
3.`signal_processing.md`— ทฤษฎีการแปลงและกรอง
4.`control_theory.md`— ข้อเสนอแนะและความเสถียร
5.`dynamical_systems.md`— พฤติกรรมของระบบเมื่อเวลาผ่านไป
## การอ้างอิงโยง
ไฟล์จำนวนมากซ้อนกัน สายการพึ่งพาที่สำคัญ:
- **การเพิ่มประสิทธิภาพ** สร้างขึ้นบน`mathematics.md`(แคลคูลัส, พีชคณิตเชิงเส้น) และ`real_analysis.md`(การบรรจบกัน)
- **ทฤษฎีสารสนเทศ** เชื่อมต่อกับ`statistics_and_probability.md`และ`thermodynamics_and_statistical_mechanics.md`(เอนโทรปี)
- **กลศาสตร์ควอนตัม** ต้องใช้`abstract_algebra.md`(ช่องว่างเวกเตอร์) และ`classical_mechanics.md`(การเปรียบเทียบแบบแฮมิลตัน)
- **การประมวลผลสัญญาณ** ขึ้นอยู่กับ`optics_and_waves.md`(ทฤษฎีคลื่น) และ`numerical_methods.md`(การคำนวณ FFT)
- **ทฤษฎีเกม** เชื่อมต่อกับ`optimization.md`และ`stochastic_processes.md`(กลยุทธ์แบบผสม พลวัตเชิงวิวัฒนาการ)