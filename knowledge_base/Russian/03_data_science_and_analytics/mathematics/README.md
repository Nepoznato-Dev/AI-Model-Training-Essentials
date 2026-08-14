# Математика
Полная коллекция подробных справочных документов, охватывающих чистую математику, прикладную математику, физику и инженерную математику — количественные основы, необходимые для науки о данных, машинного обучения и научных вычислений.
## Структура
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

## Файлы по категориям
### Фундаменты
| Файл | Описание | Сложность |
|------|-------------|------------|
| [mathematics.md](mathematics.md)| Системы счисления, алгебра, геометрия, исчисление, теория множеств, линейная алгебра, двоичная | Средний |
| [statistics_and_probability.md](statistics_and_probability.md)| Теория вероятностей, проверка гипотез, регрессия, байесовская статистика | Средний |
| [logic_and_critical_thinking.md](logic_and_critical_thinking.md)| Логика высказываний, булева алгебра, логические ошибки, оценка аргументов | Новичок |
### Чистая математика
| Файл | Описание | Сложность |
|------|-------------|------------|
| [discrete_mathematics.md](discrete_mathematics.md)| Множества, отношения, функции, комбинаторика, принцип группировки, рекуррентные соотношения, производящие функции | Средний |
| [graph_theory.md](graph_theory.md)| Представления графов, деревья, обходы, кратчайшие пути, MST, сетевые потоки, теория спектральных графов | Средний |
| [number_theory.md](number_theory.md)| Делимость, простые числа, модульная арифметика, теоремы Эйлера/Ферма, ЭЛТ, криптография | Расширенный |
| [abstract_algebra.md](abstract_algebra.md)| Группы, кольца, поля, векторные пространства, линейные отображения, теория собственных чисел, связи теории кодирования | Расширенный |
| [real_analysis.md](real_analysis.md)| Последовательности, ряды, пределы, непрерывность, интегрирование Римана/Лебега, метрические пространства, теория меры | Расширенный |
### Прикладная математика
| Файл | Описание | Сложность |
|------|-------------|------------|
| [optimization.md](optimization.md)| Линейная/выпуклая оптимизация, градиентный спуск, множители Лагранжа, ККТ, двойственность, целочисленное программирование | Средний |
| [information_theory.md](information_theory.md)| Энтропия Шеннона, взаимная информация, расхождение KL, пропускная способность канала, исходное кодирование, связи ML | Средний |
| [numerical_methods.md](numerical_methods.md)| Плавающая запятая, поиск корня, численное интегрирование, решатели ОДУ, интерполяция, устойчивость | Средний |
| [dynamical_systems.md](dynamical_systems.md)| ОДУ, фазовые портреты, устойчивость по Ляпунову, хаос, аттрактор Лоренца, УЧП | Расширенный |
| [stochastic_processes.md](stochastic_processes.md)| Цепи Маркова, случайные блуждания, броуновское движение, процессы Пуассона, мартингалы, MCMC | Расширенный |
### Физика
| Файл | Описание | Сложность |
|------|-------------|------------|
| [classical_mechanics.md](classical_mechanics.md)| Законы Ньютона, механика Лагранжа/Гамильтона, законы сохранения, орбитальная механика | Средний |
| [electromagnetism.md](electromagnetism.md)| Электрические/магнитные поля, уравнения Максвелла, ЭМ волны, RLC-цепи | Расширенный |
| [thermodynamics_and_statistical_mechanics.md](thermodynamics_and_statistical_mechanics.md)| Законы термодинамики, энтропия, свободная энергия, распределение Больцмана, статистические суммы | Расширенный |
| [quantum_mechanics.md](quantum_mechanics.md)| Уравнение Шредингера, операторы, неопределенность, суперпозиция, запутанность, кубиты | Расширенный |
| [relativity.md](relativity.md)| Преобразования Лоренца, замедление времени, эквивалентность массы и энергии, введение в общую теорию относительности | Расширенный |
| [optics_and_waves.md](optics_and_waves.md)| Волновое уравнение, интерференция, дифракция, поляризация, геометрическая/Фурье-оптика | Средний |
### Инженерная математика
| Файл | Описание | Сложность |
|------|-------------|------------|
| [signal_processing.md](signal_processing.md)| Преобразования Фурье/Лапласа/Z, БПФ, КИХ/БИХ-фильтры, теорема дискретизации, вейвлеты | Расширенный |
| [control_theory.md](control_theory.md)| Передаточные функции, ПИД-регуляторы, анализ устойчивости, пространство состояний, оптимальное управление | Расширенный |
| [operations_research.md](operations_research.md)| ЛП-формулировки, транспортные задачи, динамическое программирование, теория массового обслуживания, планирование | Средний |
| [game_theory.md](game_theory.md)| Равновесие Нэша, минимакс, кооперативные игры, значение Шепли, проектирование механизмов, многоагентная RL | Средний |
## Рекомендуемые пути чтения
### Путь к основам математики
1.`mathematics.md`— Создайте основной набор математических инструментов.
2.`statistics_and_probability.md`— Научитесь рассуждать с данными
3.`logic_and_critical_thinking.md`— обострите свои рассуждения.
4.`discrete_mathematics.md`— Формальные структуры и подсчет
5.`real_analysis.md`— Строгие основы исчисления.
### Путь машинного обучения по математике
1.`mathematics.md`— Линейная алгебра и основы исчисления
2.`statistics_and_probability.md`— Вероятность и регрессия.
3.`optimization.md`— Как учатся модели
4.`information_theory.md`— Функции потерь и информация
5.`stochastic_processes.md`— Случайные процессы и MCMC
6.`numerical_methods.md`— Вычислительные соображения
### Путь к науке о данных и алгоритмам
1.`mathematics.md`— Основная математика
2.`discrete_mathematics.md`— Комбинаторика и структуры.
3.`graph_theory.md`— Сетевой анализ
4.`optimization.md`— Методы оптимизации
5.`operations_research.md`— Математика принятия решений
### Физика для ML Path
1.`mathematics.md`— Исчисление и линейная алгебра
2.`classical_mechanics.md`— Детерминированные системы
3.`thermodynamics_and_statistical_mechanics.md`— Энтропия и вероятность
4.`quantum_mechanics.md`— Основы квантовых вычислений
5.`information_theory.md`— Информационные и энтропийные связи.
### Обработка сигналов и инженерный путь
1.`mathematics.md`— Исчисление и комплексные числа.
2.`optics_and_waves.md`— Основы волн
3.`signal_processing.md`— Теория преобразований и фильтров.
4.`control_theory.md`— Обратная связь и стабильность
5.`dynamical_systems.md`— Поведение системы с течением времени.
## Перекрестные ссылки
Многие файлы основаны друг на друге. Ключевые цепочки зависимостей:
- **Оптимизация** основана на`mathematics.md`(исчисление, линейная алгебра) и`real_analysis.md`(сходимость).
- **Теория информации** связана с`statistics_and_probability.md`и`thermodynamics_and_statistical_mechanics.md`(энтропия).
- **Квантовая механика** требует`abstract_algebra.md`(векторные пространства) и`classical_mechanics.md`(гамильтонианская аналогия)
- **Обработка сигналов** основана на`optics_and_waves.md`(теория волн) и`numerical_methods.md`(вычисление БПФ).
- **Теория игр** связана с`optimization.md`и`stochastic_processes.md`(смешанные стратегии, эволюционная динамика).