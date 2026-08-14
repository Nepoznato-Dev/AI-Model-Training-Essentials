# علم داده و تجزیه و تحلیل
مجموعه ای ساختاریافته از اسناد مرجع که مبانی ریاضی، گردش کار علم داده، مفاهیم یادگیری ماشین و شیوه های تجزیه و تحلیل ضروری برای آموزش مدل هوش مصنوعی و تصمیم گیری مبتنی بر داده را پوشش می دهد.
## ساختار
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

## فایل ها بر اساس موضوع
### ریاضیات - مبانی
| فایل | توضیحات |
|------|-------------|
| [mathematics.md](mathematics/mathematics.md)| سیستم های اعداد، جبر، هندسه، حساب دیفرانسیل و انتگرال، نظریه مجموعه ها، جبر خطی |
| [statistics_and_probability.md](mathematics/statistics_and_probability.md)| نظریه احتمال، آزمون فرضیه، رگرسیون، آمار بیزی |
| [logic_and_critical_thinking.md](mathematics/logic_and_critical_thinking.md)| منطق گزاره ای، جبر بولی، مغالطات منطقی، ارزیابی استدلال |
### ریاضیات - ریاضیات محض
| فایل | توضیحات |
|------|-------------|
| [discrete_mathematics.md](mathematics/discrete_mathematics.md)| مجموعه ها، روابط، توابع، ترکیبات، روابط عود، توابع مولد |
| [graph_theory.md](mathematics/graph_theory.md)| نمودارها، درختان، پیمایش ها، کوتاه ترین مسیرها، MST ها، جریان های شبکه، نظریه گراف طیفی |
| [number_theory.md](mathematics/number_theory.md)| اعداد اول، حساب مدولار، قضایای فرما/اولر، رمزنگاری |
| [abstract_algebra.md](mathematics/abstract_algebra.md)| گروه ها، حلقه ها، میدان ها، فضاهای برداری، نظریه ویژه، نظریه کدگذاری |
| [real_analysis.md](mathematics/real_analysis.md)| دنباله ها، محدودیت ها، تداوم، ادغام ریمان/لبگ، فضاهای متریک، نظریه اندازه گیری |
### ریاضیات - ریاضیات کاربردی
| فایل | توضیحات |
|------|-------------|
| [optimization.md](mathematics/optimization.md)| بهینه سازی خطی/محدب، نزول گرادیان، ضرب کننده های لاگرانژ، KKT، دوگانگی |
| [information_theory.md](mathematics/information_theory.md)| آنتروپی شانون، واگرایی KL، اطلاعات متقابل، ظرفیت کانال، فشرده سازی |
| [numerical_methods.md](mathematics/numerical_methods.md)| نقطه شناور، ریشه یابی، ادغام عددی، حل کننده های ODE، پایداری |
| [dynamical_systems.md](mathematics/dynamical_systems.md)| ODE ها، PDE ها، پرتره های فاز، هرج و مرج، جاذب لورنز، دوشاخه ها |
| [stochastic_processes.md](mathematics/stochastic_processes.md)| زنجیر مارکوف، راه رفتن تصادفی، حرکت براونی، مارتینگل، MCMC |
### ریاضیات - فیزیک
| فایل | توضیحات |
|------|-------------|
| [classical_mechanics.md](mathematics/classical_mechanics.md)| قوانین نیوتن، مکانیک لاگرانژی/همیلتونی، قوانین بقای، مکانیک مداری |
| [electromagnetism.md](mathematics/electromagnetism.md)| معادلات ماکسول، میدان های الکتریکی/مغناطیسی، امواج EM، مدارهای RLC |
| [thermodynamics_and_statistical_mechanics.md](mathematics/thermodynamics_and_statistical_mechanics.md)| قوانین ترمودینامیکی، آنتروپی، انرژی آزاد، توزیع بولتزمن، توابع تقسیم |
| [quantum_mechanics.md](mathematics/quantum_mechanics.md)| معادله شرودینگر، عدم قطعیت، برهم نهی، درهم تنیدگی، کیوبیت، دروازه های کوانتومی |
| [relativity.md](mathematics/relativity.md)| نسبیت خاص/عام، تبدیلات لورنتس، انحنای فضازمان |
| [optics_and_waves.md](mathematics/optics_and_waves.md)| معادله موج، تداخل، پراش، قطبش، هندسی/اپتیک فوریه |
### ریاضیات - ریاضیات مهندسی
| فایل | توضیحات |
|------|-------------|
| [signal_processing.md](mathematics/signal_processing.md)| تبدیل فوریه/لاپلاس/Z، فیلترهای FFT، FIR/IIR، قضیه نمونه برداری، موجک |
| [control_theory.md](mathematics/control_theory.md)| توابع انتقال، کنترل کننده های PID، تجزیه و تحلیل پایداری، فضای حالت، فیلتر کالمن |
| [operations_research.md](mathematics/operations_research.md)| فرمولاسیون LP، مشکلات حمل و نقل، برنامه نویسی پویا، تئوری صف |
| [game_theory.md](mathematics/game_theory.md)| تعادل نش، مینی‌مکس، بازی‌های مشارکتی، ارزش شپلی، طراحی مکانیزم |
### علم داده و تجزیه و تحلیل
| فایل | توضیحات |
|------|-------------|
| [data_science_and_analytics.md](data_science_and_analytics.md)| چرخه حیات علم داده، تجزیه و تحلیل داده های اکتشافی، مهندسی ویژگی، خطوط لوله |
| [data_visualization.md](data_visualization.md)| انتخاب نمودار، رمزگذاری بصری، طراحی داشبورد، داستان سرایی داده |
| [statistical_testing_and_experimentation.md](statistical_testing_and_experimentation.md)| تست A/B، طراحی تجربی، آزمون فرضیه در عمل |
| [feature_engineering.md](feature_engineering.md)| تکنیک های ایجاد ویژگی، انتخاب، تبدیل، رمزگذاری |
| [ensemble_methods.md](ensemble_methods.md)| بسته بندی، تقویت، انباشته کردن، رای دادن — ترکیب مدل ها برای عملکرد بهتر |
| [causal_inference.md](causal_inference.md)| استدلال علّی، اثرات درمانی، عوامل مخدوش کننده، متغیرهای ابزاری |
| [data_ethics_and_privacy.md](data_ethics_and_privacy.md)| هوش مصنوعی اخلاقی، مقررات حفظ حریم خصوصی، تشخیص تعصب، انصاف در ML |
| [geospatial_analysis.md](geospatial_analysis.md)| داده های مکانی، نقشه برداری، GIS، ژئوکدینگ، آمار مکانی |
## مسیرهای خواندن پیشنهادی
### **مسیر مبانی ریاضی**
1.`mathematics/mathematics.md`- جعبه ابزار ریاضی هسته را بسازید
2.`mathematics/statistics_and_probability.md`- یاد بگیرید که با داده ها استدلال کنید
3.`mathematics/logic_and_critical_thinking.md`- استدلال خود را تیز کنید
4.`mathematics/discrete_mathematics.md`- ساختارهای رسمی و شمارش
5.`mathematics/real_analysis.md`- پایه های دقیق حساب
### **مسیر ریاضی یادگیری ماشین**
1.`mathematics/mathematics.md`- جبر خطی و مبانی حساب
2.`mathematics/statistics_and_probability.md`- احتمال و رگرسیون
3.`mathematics/optimization.md`- مدل‌ها چگونه یاد می‌گیرند (نزول گرادیان، تحدب)
4.`mathematics/information_theory.md`- توابع از دست دادن، آنتروپی، واگرایی KL
5.`mathematics/stochastic_processes.md`- فرآیندهای تصادفی و MCMC
6.`mathematics/numerical_methods.md`- ملاحظات محاسباتی
### **مسیر علم داده**
1.`mathematics/mathematics.md`- پیش نیازهای ریاضی
2.`mathematics/statistics_and_probability.md`- مبانی آماری
3.`data_science_and_analytics.md`- گردش کار علم داده
4.`data_visualization.md`- یافته ها را به طور مؤثر در میان بگذارید
5.`feature_engineering.md`- داده ها را برای مدل سازی آماده کنید
### **مسیر یادگیری ماشین**
1.`mathematics/mathematics.md`- جبر خطی و حساب دیفرانسیل و انتگرال
2.`mathematics/statistics_and_probability.md`- احتمال و رگرسیون
3.`mathematics/optimization.md`- روش های بهینه سازی برای آموزش
4.`ensemble_methods.md`- ترکیب مدل ها برای عملکرد بهتر
5.`data_science_and_analytics.md`- خطوط لوله ML سرتاسر
### **مسیر تحلیل و آزمایش**
1.`mathematics/statistics_and_probability.md`- مبانی آماری
2.`statistical_testing_and_experimentation.md`- طراحی و تجزیه و تحلیل آزمایش ها
3.`causal_inference.md`- فراتر از همبستگی به علیت بروید
4.`data_ethics_and_privacy.md`- شیوه های داده های مسئول
### **فیزیک برای مسیر ML**
1.`mathematics/mathematics.md`- حساب دیفرانسیل و انتگرال و جبر خطی
2.`mathematics/classical_mechanics.md`- سیستم های قطعی، مکانیک هامیلتونی
3.`mathematics/thermodynamics_and_statistical_mechanics.md`- آنتروپی و احتمال
4.`mathematics/quantum_mechanics.md`- مبانی محاسباتی کوانتومی
5.`mathematics/information_theory.md`- اطلاعات و اتصالات آنتروپی
### **مسیر پردازش سیگنال و مهندسی**
1.`mathematics/mathematics.md`- حساب دیفرانسیل و انتگرال و اعداد مختلط
2.`mathematics/optics_and_waves.md`- مبانی موج
3.`mathematics/signal_processing.md`- تئوری تبدیل و فیلتر
4.`mathematics/control_theory.md`- بازخورد و ثبات
5.`mathematics/dynamical_systems.md`- رفتار سیستم در طول زمان