#ریاضی
مجموعه ای جامع از اسناد مرجع غواصی عمیق که ریاضیات محض، ریاضیات کاربردی، فیزیک و ریاضیات مهندسی را پوشش می دهد - مبانی کمی ضروری برای علم داده، یادگیری ماشین و محاسبات علمی.
## ساختار
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

## فایل ها بر اساس دسته
### پایه ها
| فایل | توضیحات | سختی |
|------|-------------|------------|
| [mathematics.md](mathematics.md)| سیستم های اعداد، جبر، هندسه، حساب دیفرانسیل و انتگرال، نظریه مجموعه ها، جبر خطی، باینری | متوسط ​​|
| [statistics_and_probability.md](statistics_and_probability.md)| نظریه احتمال، آزمون فرضیه، رگرسیون، آمار بیزی | متوسط ​​|
| [logic_and_critical_thinking.md](logic_and_critical_thinking.md)| منطق گزاره ای، جبر بولی، مغالطات منطقی، ارزیابی استدلال | مبتدی |
### ریاضیات محض
| فایل | توضیحات | سختی |
|------|-------------|------------|
| [discrete_mathematics.md](discrete_mathematics.md)| مجموعه ها، روابط، توابع، ترکیبات، اصل کبوتر، روابط عود، توابع مولد | متوسط ​​|
| [graph_theory.md](graph_theory.md)| نمایش گراف، درختان، پیمایش ها، کوتاه ترین مسیرها، MST ها، جریان های شبکه، نظریه گراف طیفی | متوسط ​​|
| [number_theory.md](number_theory.md)| تقسیم پذیری، اعداد اول، محاسبات مدولار، قضایای اویلر/فرمات، CRT، رمزنگاری | پیشرفته |
| [abstract_algebra.md](abstract_algebra.md)| گروه ها، حلقه ها، فیلدها، فضاهای برداری، نقشه های خطی، تئوری ویژه، اتصالات تئوری کدگذاری | پیشرفته |
| [real_analysis.md](real_analysis.md)| دنباله ها، سری ها، محدودیت ها، تداوم، ادغام ریمان/لبگ، فضاهای متریک، نظریه اندازه گیری | پیشرفته |
### ریاضیات کاربردی
| فایل | توضیحات | سختی |
|------|-------------|------------|
| [optimization.md](optimization.md)| بهینه سازی خطی/محدب، نزول گرادیان، ضرب کننده های لاگرانژ، KKT، دوگانگی، برنامه ریزی عدد صحیح | متوسط ​​|
| [information_theory.md](information_theory.md)| آنتروپی شانون، اطلاعات متقابل، واگرایی KL، ظرفیت کانال، کدگذاری منبع، اتصالات ML | متوسط ​​|
| [numerical_methods.md](numerical_methods.md)| نقطه شناور، ریشه یابی، ادغام عددی، حل کننده های ODE، درون یابی، پایداری | متوسط ​​|
| [dynamical_systems.md](dynamical_systems.md)| ODE ها، پرتره های فاز، پایداری لیاپانوف، هرج و مرج، جاذبه لورنز، PDEs | پیشرفته |
| [stochastic_processes.md](stochastic_processes.md)| زنجیر مارکوف، راه رفتن تصادفی، حرکت براونی، فرآیندهای پواسون، مارتینگالس، MCMC | پیشرفته |
### فیزیک
| فایل | توضیحات | سختی |
|------|-------------|------------|
| [classical_mechanics.md](classical_mechanics.md)| قوانین نیوتن، مکانیک لاگرانژی/همیلتونی، قوانین بقای، مکانیک مداری | متوسط ​​|
| [electromagnetism.md](electromagnetism.md)| میدان های الکتریکی/مغناطیسی، معادلات ماکسول، امواج EM، مدارهای RLC | پیشرفته |
| [thermodynamics_and_statistical_mechanics.md](thermodynamics_and_statistical_mechanics.md)| قوانین ترمودینامیکی، آنتروپی، انرژی آزاد، توزیع بولتزمن، توابع تقسیم | پیشرفته |
| [quantum_mechanics.md](quantum_mechanics.md)| معادله شرودینگر، عملگرها، عدم قطعیت، برهم نهی، درهم تنیدگی، کیوبیت | پیشرفته |
| [relativity.md](relativity.md)| تبدیلات لورنتس، اتساع زمان، هم ارزی جرم-انرژی، مقدمه ای بر نسبیت عام | پیشرفته |
| [optics_and_waves.md](optics_and_waves.md)| معادله موج، تداخل، پراش، پلاریزاسیون، هندسی/اپتیک فوریه | متوسط ​​|
### ریاضیات مهندسی
| فایل | توضیحات | سختی |
|------|-------------|------------|
| [signal_processing.md](signal_processing.md)| تبدیل فوریه/لاپلاس/Z، فیلترهای FFT، FIR/IIR، قضیه نمونه برداری، موجک | پیشرفته |
| [control_theory.md](control_theory.md)| توابع انتقال، کنترل کننده های PID، تجزیه و تحلیل پایداری، فضای حالت، کنترل بهینه | پیشرفته |
| [operations_research.md](operations_research.md)| فرمولاسیون LP، مشکلات حمل و نقل، برنامه نویسی پویا، تئوری صف، زمان بندی | متوسط ​​|
| [game_theory.md](game_theory.md)| تعادل نش، مینیمکس، بازی های مشارکتی، ارزش شپلی، طراحی مکانیزم، چند عامل RL | متوسط ​​|
## مسیرهای خواندن پیشنهادی
### مسیر مبانی ریاضی
1.`mathematics.md`- جعبه ابزار ریاضی هسته را بسازید
2.`statistics_and_probability.md`- یاد بگیرید که با داده ها استدلال کنید
3.`logic_and_critical_thinking.md`- استدلال خود را تیز کنید
4.`discrete_mathematics.md`- ساختارهای رسمی و شمارش
5.`real_analysis.md`- پایه های دقیق حساب
### مسیر ریاضیات یادگیری ماشین
1.`mathematics.md`- جبر خطی و مبانی حساب
2.`statistics_and_probability.md`- احتمال و رگرسیون
3.`optimization.md`- مدل ها چگونه یاد می گیرند
4.`information_theory.md`- از دست دادن توابع و اطلاعات
5.`stochastic_processes.md`- فرآیندهای تصادفی و MCMC
6.`numerical_methods.md`- ملاحظات محاسباتی
### مسیر علم داده و الگوریتم
1.`mathematics.md`- ریاضی اصلی
2.`discrete_mathematics.md`- ترکیبات و ساختارها
3.`graph_theory.md`- تجزیه و تحلیل شبکه
4.`optimization.md`- روش های بهینه سازی
5.`operations_research.md`- ریاضیات تصمیم
### فیزیک برای مسیر ML
1.`mathematics.md`- حساب دیفرانسیل و انتگرال و جبر خطی
2.`classical_mechanics.md`- سیستم های قطعی
3.`thermodynamics_and_statistical_mechanics.md`- آنتروپی و احتمال
4.`quantum_mechanics.md`- مبانی محاسباتی کوانتومی
5.`information_theory.md`- اطلاعات و اتصالات آنتروپی
### پردازش سیگنال و مسیر مهندسی
1.`mathematics.md`- حساب دیفرانسیل و انتگرال و اعداد مختلط
2.`optics_and_waves.md`- مبانی موج
3.`signal_processing.md`- تئوری تبدیل و فیلتر
4.`control_theory.md`- بازخورد و ثبات
5.`dynamical_systems.md`- رفتار سیستم در طول زمان
## ارجاعات متقابل
بسیاری از فایل ها بر روی یکدیگر ساخته می شوند. زنجیره های وابستگی کلیدی:
- **بهینه سازی** مبتنی بر`mathematics.md`(حساب حساب، جبر خطی) و`real_analysis.md`(همگرایی)
- **نظریه اطلاعات** به`statistics_and_probability.md`و`thermodynamics_and_statistical_mechanics.md`(آنتروپی) متصل می شود
- **مکانیک کوانتومی** به`abstract_algebra.md`(فضاهای برداری) و`classical_mechanics.md`(قیاس همیلتونی) نیاز دارد.
- **پردازش سیگنال** متکی بر`optics_and_waves.md`(تئوری موج) و`numerical_methods.md`(محاسبات FFT) است.
- **نظریه بازی** به`optimization.md`و`stochastic_processes.md`متصل می شود (استراتژی های ترکیبی، پویایی تکاملی)