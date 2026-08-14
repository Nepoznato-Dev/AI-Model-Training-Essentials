# Datenwissenschaft und Analytik
Eine strukturierte Sammlung von Referenzdokumenten, die die mathematischen Grundlagen, datenwissenschaftlichen Arbeitsabläufe, Konzepte des maschinellen Lernens und Analysepraktiken abdecken, die für das Training von KI-Modellen und die datengesteuerte Entscheidungsfindung unerlässlich sind.
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

## Dateien nach Thema
### Mathematik – Grundlagen
| Datei | Beschreibung |
|------|-------------|
| [mathematics.md](mathematics/mathematics.md)| Zahlensysteme, Algebra, Geometrie, Infinitesimalrechnung, Mengenlehre, lineare Algebra |
| [statistics_and_probability.md](mathematics/statistics_and_probability.md)| Wahrscheinlichkeitstheorie, Hypothesentest, Regression, Bayes'sche Statistik |
| [logic_and_critical_thinking.md](mathematics/logic_and_critical_thinking.md)| Aussagenlogik, Boolesche Algebra, logische Irrtümer, Argumentbewertung |
### Mathematik – Reine Mathematik
| Datei | Beschreibung |
|------|-------------|
| [discrete_mathematics.md](mathematics/discrete_mathematics.md)| Mengen, Beziehungen, Funktionen, Kombinatorik, Wiederholungsbeziehungen, erzeugende Funktionen |
| [graph_theory.md](mathematics/graph_theory.md)| Graphen, Bäume, Durchquerungen, kürzeste Wege, MSTs, Netzwerkflüsse, Spektralgraphentheorie |
| [number_theory.md](mathematics/number_theory.md)| Primzahlen, modulare Arithmetik, Sätze von Fermat/Euler, Kryptographie |
| [abstract_algebra.md](mathematics/abstract_algebra.md)| Gruppen, Ringe, Körper, Vektorräume, Eigentheorie, Kodierungstheorie |
| [real_analysis.md](mathematics/real_analysis.md)| Folgen, Grenzen, Kontinuität, Riemann/Lebesgue-Integration, metrische Räume, Maßtheorie |
### Mathematik – Angewandte Mathematik
| Datei | Beschreibung |
|------|-------------|
| [optimization.md](mathematics/optimization.md)| Lineare/konvexe Optimierung, Gradientenabstieg, Lagrange-Multiplikatoren, KKT, Dualität |
| [information_theory.md](mathematics/information_theory.md)| Shannon-Entropie, KL-Divergenz, gegenseitige Information, Kanalkapazität, Komprimierung |
| [numerical_methods.md](mathematics/numerical_methods.md)| Gleitkomma, Wurzelfindung, numerische Integration, ODE-Löser, Stabilität |
| [dynamical_systems.md](mathematics/dynamical_systems.md)| ODEs, PDEs, Phasenporträts, Chaos, Lorenz-Attraktor, Bifurkationen |
| [stochastic_processes.md](mathematics/stochastic_processes.md)| Markov-Ketten, Random Walks, Brownsche Bewegung, Martingale, MCMC |
### Mathematik – Physik
| Datei | Beschreibung |
|------|-------------|
| [classical_mechanics.md](mathematics/classical_mechanics.md)| Newtonsche Gesetze, Lagrange-/Hamiltonsche Mechanik, Erhaltungssätze, Orbitalmechanik |
| [electromagnetism.md](mathematics/electromagnetism.md)| Maxwell-Gleichungen, elektrische/magnetische Felder, EM-Wellen, RLC-Schaltkreise |
| [thermodynamics_and_statistical_mechanics.md](mathematics/thermodynamics_and_statistical_mechanics.md)| Thermodynamische Gesetze, Entropie, freie Energie, Boltzmann-Verteilung, Zustandssummenfunktionen |
| [quantum_mechanics.md](mathematics/quantum_mechanics.md)| Schrödinger-Gleichung, Unsicherheit, Superposition, Verschränkung, Qubits, Quantengatter |
| [relativity.md](mathematics/relativity.md)| Spezielle/allgemeine Relativitätstheorie, Lorentz-Transformationen, Raumzeitkrümmung |
| [optics_and_waves.md](mathematics/optics_and_waves.md)| Wellengleichung, Interferenz, Beugung, Polarisation, geometrische/Fourier-Optik |
### Mathematik – Ingenieurmathematik
| Datei | Beschreibung |
|------|-------------|
| [signal_processing.md](mathematics/signal_processing.md)| Fourier/Laplace/Z-Transformationen, FFT, FIR/IIR-Filter, Abtasttheorem, Wavelets |
| [control_theory.md](mathematics/control_theory.md)| Übertragungsfunktionen, PID-Regler, Stabilitätsanalyse, Zustandsraum, Kalman-Filter |
| [operations_research.md](mathematics/operations_research.md)| LP-Formulierungen, Transportprobleme, dynamische Programmierung, Warteschlangentheorie |
| [game_theory.md](mathematics/game_theory.md)| Nash-Gleichgewicht, Minimax, kooperative Spiele, Shapley-Wert, Mechanismusdesign |
### Datenwissenschaft und Analyse
| Datei | Beschreibung |
|------|-------------|
| [data_science_and_analytics.md](data_science_and_analytics.md)| Datenwissenschaftlicher Lebenszyklus, explorative Datenanalyse, Feature Engineering, Pipelines |
| [data_visualization.md](data_visualization.md)| Diagrammauswahl, visuelle Kodierung, Dashboard-Design, Daten-Storytelling |
| [statistical_testing_and_experimentation.md](statistical_testing_and_experimentation.md)| A/B-Tests, experimentelles Design, Hypothesentests in der Praxis |
| [feature_engineering.md](feature_engineering.md)| Feature-Erstellung, Auswahl, Transformation, Kodierungstechniken |
| [ensemble_methods.md](ensemble_methods.md)| Einpacken, Boosten, Stapeln, Voting – Modelle kombinieren für bessere Leistung |
| [causal_inference.md](causal_inference.md)| Kausales Denken, Behandlungseffekte, Störfaktoren, instrumentelle Variablen |
| [data_ethics_and_privacy.md](data_ethics_and_privacy.md)| Ethische KI, Datenschutzbestimmungen, Voreingenommenheitserkennung, Fairness in ML |
| [geospatial_analysis.md](geospatial_analysis.md)| Raumdaten, Kartierung, GIS, Geokodierung, Raumstatistik |
## Empfohlene Lesepfade
### **Mathematischer Grundlagenpfad**
1.`mathematics/mathematics.md`– Erstellen Sie das grundlegende Mathematik-Toolkit
2.`mathematics/statistics_and_probability.md`– Lernen Sie, mit Daten zu argumentieren
3.`mathematics/logic_and_critical_thinking.md`– Schärfen Sie Ihre Argumentation
4.`mathematics/discrete_mathematics.md`– Formale Strukturen und Zählen
5.`mathematics/real_analysis.md`– Strenge Grundlagen der Infinitesimalrechnung
### **Mathematikpfad für maschinelles Lernen**
1.`mathematics/mathematics.md`– Grundlagen der linearen Algebra und Infinitesimalrechnung
2.`mathematics/statistics_and_probability.md`– Wahrscheinlichkeit und Regression
3.`mathematics/optimization.md`– Wie Modelle lernen (Gradientenabstieg, Konvexität)
4.`mathematics/information_theory.md`– Verlustfunktionen, Entropie, KL-Divergenz
5.`mathematics/stochastic_processes.md`– Zufällige Prozesse und MCMC
6.`mathematics/numerical_methods.md`– Berechnungsüberlegungen
### **Datenwissenschaftspfad**
1.`mathematics/mathematics.md`– Mathe-Voraussetzungen
2.`mathematics/statistics_and_probability.md`– Statistische Grundlagen
3.`data_science_and_analytics.md`– Der Data-Science-Workflow
4.`data_visualization.md`– Ergebnisse effektiv kommunizieren
5.`feature_engineering.md`– Daten für die Modellierung vorbereiten
### **Pfad für maschinelles Lernen**
1.`mathematics/mathematics.md`– Lineare Algebra und Infinitesimalrechnung
2.`mathematics/statistics_and_probability.md`– Wahrscheinlichkeit und Regression
3.`mathematics/optimization.md`– Optimierungsmethoden für das Training
4.`ensemble_methods.md`– Kombinieren von Modellen für bessere Leistung
5.`data_science_and_analytics.md`– End-to-End-ML-Pipelines
### **Analyse- und Experimentierpfad**
1.`mathematics/statistics_and_probability.md`– Statistische Grundlagen
2.`statistical_testing_and_experimentation.md`– Experimente entwerfen und analysieren
3.`causal_inference.md`– Gehen Sie über die Korrelation zur Kausalität hinaus
4.`data_ethics_and_privacy.md`– Verantwortungsvolle Datenpraktiken
### **Physik für ML-Pfad**
1.`mathematics/mathematics.md`– Analysis und lineare Algebra
2.`mathematics/classical_mechanics.md`– Deterministische Systeme, Hamiltonsche Mechanik
3.`mathematics/thermodynamics_and_statistical_mechanics.md`– Entropie und Wahrscheinlichkeit
4.`mathematics/quantum_mechanics.md`– Grundlagen des Quantencomputings
5.`mathematics/information_theory.md`– Informations- und Entropieverbindungen
### **Signalverarbeitungs- und Engineering-Pfad**
1.`mathematics/mathematics.md`– Analysis und komplexe Zahlen
2.`mathematics/optics_and_waves.md`– Wave-Grundlagen
3.`mathematics/signal_processing.md`– Transformations- und Filtertheorie
4.`mathematics/control_theory.md`– Feedback und Stabilität
5.`mathematics/dynamical_systems.md`– Systemverhalten im Zeitverlauf