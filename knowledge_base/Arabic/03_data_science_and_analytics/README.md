# علم البيانات والتحليلات
مجموعة منظمة من المستندات المرجعية التي تغطي الأسس الرياضية، وسير عمل علوم البيانات، ومفاهيم التعلم الآلي، والممارسات التحليلية الضرورية للتدريب على نماذج الذكاء الاصطناعي واتخاذ القرارات المستندة إلى البيانات.
## بناء
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

## الملفات حسب الموضوع
### الرياضيات – الأسس
| ملف | الوصف |
|------|------------|
| [mathematics.md](mathematics/mathematics.md)| أنظمة الأعداد، الجبر، الهندسة، حساب التفاضل والتكامل، نظرية المجموعات، الجبر الخطي |
| [statistics_and_probability.md](mathematics/statistics_and_probability.md)| نظرية الاحتمالات، اختبار الفرضيات، الانحدار، إحصائيات بايزي |
| [logic_and_critical_thinking.md](mathematics/logic_and_critical_thinking.md)| المنطق الافتراضي، الجبر البوليني، المغالطات المنطقية، تقييم الحجة |
### الرياضيات — الرياضيات البحتة
| ملف | الوصف |
|------|------------|
| [discrete_mathematics.md](mathematics/discrete_mathematics.md)| المجموعات، العلاقات، الدوال، التوافقيات، علاقات التكرار، توليد الدوال |
| [graph_theory.md](mathematics/graph_theory.md)| الرسوم البيانية، الأشجار، عمليات الاجتياز، أقصر المسارات، MSTs، تدفقات الشبكة، نظرية الرسم البياني الطيفي |
| [number_theory.md](mathematics/number_theory.md)| الأعداد الأولية، الحساب المعياري، نظريات فيرما/أويلر، التشفير |
| [abstract_algebra.md](mathematics/abstract_algebra.md)| المجموعات، الحلقات، المجالات، الفضاءات المتجهة، نظرية الذات، نظرية الترميز |
| [real_analysis.md](mathematics/real_analysis.md)| المتتابعات، النهايات، الاستمرارية، تكامل ريمان/ليبيغ، الفضاءات المترية، نظرية القياس |
### الرياضيات — الرياضيات التطبيقية
| ملف | الوصف |
|------|------------|
| [optimization.md](mathematics/optimization.md)| التحسين الخطي / المحدب، نزول التدرج، مضاعفات لاغرانج، KKT، الازدواجية |
| [information_theory.md](mathematics/information_theory.md)| إنتروبيا شانون، تباعد KL، المعلومات المتبادلة، سعة القناة، الضغط |
| [numerical_methods.md](mathematics/numerical_methods.md)| النقطة العائمة، إيجاد الجذر، التكامل العددي، حلول ODE، الاستقرار |
| [dynamical_systems.md](mathematics/dynamical_systems.md)| ODEs، PDEs، صور الطور، الفوضى، جاذب لورنز، التشعبات |
| [stochastic_processes.md](mathematics/stochastic_processes.md)| سلاسل ماركوف، المشي العشوائي، الحركة البراونية، المارتينجال، MCMC |
### الرياضيات — الفيزياء
| ملف | الوصف |
|------|------------|
| [classical_mechanics.md](mathematics/classical_mechanics.md)| قوانين نيوتن، ميكانيكا لاغرانج/هاميلتون، قوانين الحفظ، ميكانيكا المدارات |
| [electromagnetism.md](mathematics/electromagnetism.md)| معادلات ماكسويل، المجالات الكهربائية والمغناطيسية، الموجات الكهرومغناطيسية، دوائر RLC |
| [thermodynamics_and_statistical_mechanics.md](mathematics/thermodynamics_and_statistical_mechanics.md)| قوانين الديناميكا الحرارية، الإنتروبيا، الطاقة الحرة، توزيع بولتزمان، دوال التقسيم |
| [quantum_mechanics.md](mathematics/quantum_mechanics.md)| معادلة شرودنجر، عدم اليقين، التراكب، التشابك، الكيوبتات، البوابات الكمومية |
| [relativity.md](mathematics/relativity.md)| النسبية العامة والخاصة، تحويلات لورنتز، انحناء الزمكان |
| [optics_and_waves.md](mathematics/optics_and_waves.md)| المعادلة الموجية، التداخل، الحيود، الاستقطاب، بصريات هندسية/فورييه |
### الرياضيات — الرياضيات الهندسية
| ملف | الوصف |
|------|------------|
| [signal_processing.md](mathematics/signal_processing.md)| محولات فورييه/لابلاس/Z، مرشحات FFT، FIR/IIR، نظرية أخذ العينات، المويجات |
| [control_theory.md](mathematics/control_theory.md)| دوال النقل، متحكمات PID، تحليل الاستقرار، مساحة الحالة، مرشح كالمان |
| [operations_research.md](mathematics/operations_research.md)| صيغ LP، مشاكل النقل، البرمجة الديناميكية، نظرية الطابور |
| [game_theory.md](mathematics/game_theory.md)| توازن ناش، المينيماكس، الألعاب التعاونية، قيمة شابلي، تصميم الآلية |
### علوم البيانات والتحليلات
| ملف | الوصف |
|------|------------|
| [data_science_and_analytics.md](data_science_and_analytics.md)| دورة حياة علم البيانات، تحليل البيانات الاستكشافية، هندسة الميزات، خطوط الأنابيب |
| [data_visualization.md](data_visualization.md)| اختيار الرسم البياني، والتشفير المرئي، وتصميم لوحة المعلومات، وسرد البيانات |
| [statistical_testing_and_experimentation.md](statistical_testing_and_experimentation.md)| اختبار أ/ب، التصميم التجريبي، اختبار الفرضيات في الممارسة العملية |
| [feature_engineering.md](feature_engineering.md)| إنشاء الميزات واختيارها وتحويلها وتقنيات التشفير |
| [ensemble_methods.md](ensemble_methods.md)| التعبئة، والتعزيز، والتكديس، والتصويت - الجمع بين النماذج لأداء أفضل |
| [causal_inference.md](causal_inference.md)| الاستدلال السببي، آثار العلاج، الإرباك، المتغيرات الآلية |
| [data_ethics_and_privacy.md](data_ethics_and_privacy.md)| الذكاء الاصطناعي الأخلاقي، ولوائح الخصوصية، واكتشاف التحيز، والعدالة في تعلم الآلة |
| [geospatial_analysis.md](geospatial_analysis.md)| البيانات المكانية، رسم الخرائط، نظم المعلومات الجغرافية، الترميز الجغرافي، الإحصاء المكاني |
## مسارات القراءة المقترحة
### **مسار الأسس الرياضية**
1.`mathematics/mathematics.md`— أنشئ مجموعة أدوات الرياضيات الأساسية
2.`mathematics/statistics_and_probability.md`— تعلم كيفية التفكير باستخدام البيانات
3.`mathematics/logic_and_critical_thinking.md`– شحذ تفكيرك
4.`mathematics/discrete_mathematics.md` — الهياكل الرسمية والعد
5.`mathematics/real_analysis.md`– أسس صارمة في حساب التفاضل والتكامل
### **مسار رياضيات التعلم الآلي**
1.`mathematics/mathematics.md`— الجبر الخطي وأسس حساب التفاضل والتكامل
2.`mathematics/statistics_and_probability.md` — الاحتمالية والانحدار
3.`mathematics/optimization.md`— كيف تتعلم النماذج (نسب التدرج، التحدب)
4.`mathematics/information_theory.md`— دوال الخسارة، الإنتروبيا، تباعد KL
5.`mathematics/stochastic_processes.md` — العمليات العشوائية وMCMC
6.`mathematics/numerical_methods.md` — الاعتبارات الحسابية
### **مسار علم البيانات**
1.`mathematics/mathematics.md` — متطلبات الرياضيات
2.`mathematics/statistics_and_probability.md` — الأسس الإحصائية
3.`data_science_and_analytics.md`— سير عمل علم البيانات
4.`data_visualization.md`— قم بتوصيل النتائج بشكل فعال
5.`feature_engineering.md`— تحضير البيانات للنمذجة
### **مسار التعلم الآلي**
1.`mathematics/mathematics.md`- الجبر الخطي وحساب التفاضل والتكامل
2.`mathematics/statistics_and_probability.md` — الاحتمالية والانحدار
3.`mathematics/optimization.md` — طرق تحسين التدريب
4.`ensemble_methods.md` — الجمع بين النماذج للحصول على أداء أفضل
5.`data_science_and_analytics.md`— خطوط أنابيب ML الشاملة
### **مسار التحليلات والتجريب**
1.`mathematics/statistics_and_probability.md` — الأسس الإحصائية
2.`statistical_testing_and_experimentation.md`- تصميم التجارب وتحليلها
3.`causal_inference.md`- تجاوز الارتباط إلى السببية
4.`data_ethics_and_privacy.md`— ممارسات البيانات المسؤولة
### **فيزياء مسار تعلم الآلة**
1.`mathematics/mathematics.md`— حساب التفاضل والتكامل والجبر الخطي
2.`mathematics/classical_mechanics.md`— الأنظمة الحتمية، الميكانيكا الهاملتونية
3.`mathematics/thermodynamics_and_statistical_mechanics.md` — الإنتروبيا والاحتمالية
4.`mathematics/quantum_mechanics.md`– أسس الحوسبة الكمومية
5.`mathematics/information_theory.md` — اتصالات المعلومات والإنتروبيا
### **معالجة الإشارات والمسار الهندسي**
1.`mathematics/mathematics.md` — حساب التفاضل والتكامل والأعداد المركبة
2.`mathematics/optics_and_waves.md` — أساسيات الموجة
3.`mathematics/signal_processing.md`- نظرية التحويل والتصفية
4.`mathematics/control_theory.md` - ردود الفعل والاستقرار
5.`mathematics/dynamical_systems.md` — سلوك النظام مع مرور الوقت