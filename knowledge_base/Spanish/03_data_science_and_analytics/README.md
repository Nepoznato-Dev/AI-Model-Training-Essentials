# Ciencia de datos y análisis
Una colección estructurada de documentos de referencia que cubren los fundamentos matemáticos, los flujos de trabajo de la ciencia de datos, los conceptos de aprendizaje automático y las prácticas de análisis esenciales para el entrenamiento de modelos de IA y la toma de decisiones basada en datos.
## Estructura
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

## Archivos por tema
### Matemáticas: fundamentos
| Archivo | Descripción |
|------|-------------|
| [mathematics.md](mathematics/mathematics.md)| Sistemas numéricos, álgebra, geometría, cálculo, teoría de conjuntos, álgebra lineal |
| [statistics_and_probability.md](mathematics/statistics_and_probability.md)| Teoría de la probabilidad, prueba de hipótesis, regresión, estadística bayesiana |
| [logic_and_critical_thinking.md](mathematics/logic_and_critical_thinking.md)| Lógica proposicional, álgebra booleana, falacias lógicas, evaluación de argumentos |
### Matemáticas — Matemáticas puras
| Archivo | Descripción |
|------|-------------|
| [discrete_mathematics.md](mathematics/discrete_mathematics.md)| Conjuntos, relaciones, funciones, combinatoria, relaciones de recurrencia, funciones generadoras |
| [graph_theory.md](mathematics/graph_theory.md)| Gráficos, árboles, recorridos, caminos más cortos, MST, flujos de red, teoría de grafos espectrales |
| [number_theory.md](mathematics/number_theory.md)| Primos, aritmética modular, teoremas de Fermat/Euler, criptografía |
| [abstract_algebra.md](mathematics/abstract_algebra.md)| Grupos, anillos, campos, espacios vectoriales, teoría propia, teoría de codificación |
| [real_analysis.md](mathematics/real_analysis.md)| Secuencias, límites, continuidad, integración de Riemann/Lebesgue, espacios métricos, teoría de la medida |
### Matemáticas — Matemáticas Aplicadas
| Archivo | Descripción |
|------|-------------|
| [optimization.md](mathematics/optimization.md)| Optimización lineal/convexa, descenso de gradiente, multiplicadores de Lagrange, KKT, dualidad |
| [information_theory.md](mathematics/information_theory.md)| Entropía de Shannon, divergencia KL, información mutua, capacidad del canal, compresión |
| [numerical_methods.md](mathematics/numerical_methods.md)| Punto flotante, búsqueda de raíces, integración numérica, solucionadores de EDO, estabilidad |
| [dynamical_systems.md](mathematics/dynamical_systems.md)| EDO, EDP, retratos de fase, caos, atractor de Lorenz, bifurcaciones |
| [stochastic_processes.md](mathematics/stochastic_processes.md)| Cadenas de Markov, paseos aleatorios, movimiento browniano, martingalas, MCMC |
### Matemáticas — Física
| Archivo | Descripción |
|------|-------------|
| [classical_mechanics.md](mathematics/classical_mechanics.md)| Leyes de Newton, mecánica lagrangiana/hamiltoniana, leyes de conservación, mecánica orbital |
| [electromagnetism.md](mathematics/electromagnetism.md)| Ecuaciones de Maxwell, campos eléctricos/magnéticos, ondas EM, circuitos RLC |
| [thermodynamics_and_statistical_mechanics.md](mathematics/thermodynamics_and_statistical_mechanics.md)| Leyes termodinámicas, entropía, energía libre, distribución de Boltzmann, funciones de partición |
| [quantum_mechanics.md](mathematics/quantum_mechanics.md)| Ecuación de Schrodinger, incertidumbre, superposición, entrelazamiento, qubits, puertas cuánticas |
| [relativity.md](mathematics/relativity.md)| Relatividad especial/general, transformaciones de Lorentz, curvatura espacio-temporal |
| [optics_and_waves.md](mathematics/optics_and_waves.md)| Ecuación de ondas, interferencia, difracción, polarización, óptica geométrica/Fourier |
### Matemáticas — Matemáticas de ingeniería
| Archivo | Descripción |
|------|-------------|
| [signal_processing.md](mathematics/signal_processing.md)| Transformadas de Fourier/Laplace/Z, FFT, filtros FIR/IIR, teorema de muestreo, wavelets |
| [control_theory.md](mathematics/control_theory.md)| Funciones de transferencia, controladores PID, análisis de estabilidad, espacio de estados, filtro de Kalman |
| [operations_research.md](mathematics/operations_research.md)| Formulaciones de LP, problemas de transporte, programación dinámica, teoría de colas |
| [game_theory.md](mathematics/game_theory.md)| Equilibrio de Nash, minimax, juegos cooperativos, valor de Shapley, diseño de mecanismos |
### Ciencia de datos y análisis
| Archivo | Descripción |
|------|-------------|
| [data_science_and_analytics.md](data_science_and_analytics.md)| Ciclo de vida de la ciencia de datos, análisis exploratorio de datos, ingeniería de características, canalizaciones |
| [data_visualization.md](data_visualization.md)| Selección de gráficos, codificación visual, diseño de paneles, narración de datos |
| [statistical_testing_and_experimentation.md](statistical_testing_and_experimentation.md)| Pruebas A/B, diseño experimental, prueba de hipótesis en la práctica |
| [feature_engineering.md](feature_engineering.md)| Creación de características, selección, transformación, técnicas de codificación |
| [ensemble_methods.md](ensemble_methods.md)| Embolsado, impulso, apilamiento, votación: combinación de modelos para un mejor rendimiento |
| [causal_inference.md](causal_inference.md)| Razonamiento causal, efectos del tratamiento, factores de confusión, variables instrumentales |
| [data_ethics_and_privacy.md](data_ethics_and_privacy.md)| IA ética, regulaciones de privacidad, detección de sesgos, equidad en ML |
| [geospatial_analysis.md](geospatial_analysis.md)| Datos espaciales, cartografía, SIG, geocodificación, estadísticas espaciales |
## Rutas de lectura sugeridas
### **Ruta de los fundamentos matemáticos**
1. `mathematics/mathematics.md`: cree el conjunto de herramientas matemáticas básico
2. `mathematics/statistics_and_probability.md`: aprenda a razonar con datos
3. `mathematics/logic_and_critical_thinking.md`: afina tu razonamiento
4.`mathematics/discrete_mathematics.md`— Estructuras formales y conteo
5. `mathematics/real_analysis.md`: fundamentos rigurosos del cálculo
### **Ruta de Matemáticas de Aprendizaje Automático**
1.`mathematics/mathematics.md`— Fundamentos de cálculo y álgebra lineal
2. `mathematics/statistics_and_probability.md`: probabilidad y regresión
3. `mathematics/optimization.md`: cómo aprenden los modelos (descenso de gradiente, convexidad)
4. `mathematics/information_theory.md`: funciones de pérdida, entropía, divergencia KL
5. `mathematics/stochastic_processes.md`: procesos aleatorios y MCMC
6. `mathematics/numerical_methods.md`: consideraciones computacionales
### **Ruta de la ciencia de datos**
1. `mathematics/mathematics.md`: requisitos previos de matemáticas
2.`mathematics/statistics_and_probability.md`— Fundamentos estadísticos
3. `data_science_and_analytics.md`: el flujo de trabajo de la ciencia de datos
4. `data_visualization.md`: comunicar los hallazgos de forma eficaz
5. `feature_engineering.md`: preparar datos para modelar
### **Ruta de aprendizaje automático**
1.`mathematics/mathematics.md`— Álgebra lineal y cálculo
2. `mathematics/statistics_and_probability.md`: probabilidad y regresión
3. `mathematics/optimization.md`: métodos de optimización para el entrenamiento
4. `ensemble_methods.md`: combinación de modelos para un mejor rendimiento
5. `data_science_and_analytics.md`: canalizaciones de aprendizaje automático de un extremo a otro
### **Ruta de análisis y experimentación**
1.`mathematics/statistics_and_probability.md`— Fundamentos estadísticos
2. `statistical_testing_and_experimentation.md`: diseñar y analizar experimentos
3. `causal_inference.md`: vaya más allá de la correlación y llegue a la causalidad
4. `data_ethics_and_privacy.md`: prácticas de datos responsables
### **Física para ML Path**
1.`mathematics/mathematics.md`— Cálculo y álgebra lineal
2.`mathematics/classical_mechanics.md`- Sistemas deterministas, mecánica hamiltoniana
3. `mathematics/thermodynamics_and_statistical_mechanics.md`: entropía y probabilidad
4. `mathematics/quantum_mechanics.md`: fundamentos de la computación cuántica
5. `mathematics/information_theory.md`: información y conexiones de entropía
### **Ruta de ingeniería y procesamiento de señales**
1.`mathematics/mathematics.md`— Cálculo y números complejos
2. `mathematics/optics_and_waves.md`: fundamentos de las ondas
3. `mathematics/signal_processing.md`: teoría de transformaciones y filtros
4. `mathematics/control_theory.md`: retroalimentación y estabilidad
5. `mathematics/dynamical_systems.md`: comportamiento del sistema a lo largo del tiempo