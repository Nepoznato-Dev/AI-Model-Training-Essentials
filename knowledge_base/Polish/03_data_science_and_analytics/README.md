# Nauka o danych i analityka
Ustrukturyzowany zbiór dokumentów referencyjnych obejmujący podstawy matematyczne, przepływy pracy związane z nauką o danych, koncepcje uczenia maszynowego i praktyki analityczne niezbędne do szkolenia w zakresie modeli sztucznej inteligencji i podejmowania decyzji w oparciu o dane.
## Struktura
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

## Pliki według tematu
### Matematyka — podstawy
| Plik | Opis |
|------|------------|
| [mathematics.md](mathematics/mathematics.md)| Systemy liczbowe, algebra, geometria, rachunek różniczkowy, teoria mnogości, algebra liniowa |
| [statistics_and_probability.md](mathematics/statistics_and_probability.md)| Teoria prawdopodobieństwa, testowanie hipotez, regresja, statystyka Bayesa |
| [logic_and_critical_thinking.md](mathematics/logic_and_critical_thinking.md)| Logika zdań, algebra Boole’a, błędy logiczne, ocena argumentów |
### Matematyka — czysta matematyka
| Plik | Opis |
|------|------------|
| [discrete_mathematics.md](mathematics/discrete_mathematics.md)| Zbiory, relacje, funkcje, kombinatoryka, relacje rekurencyjne, funkcje generujące |
| [graph_theory.md](mathematics/graph_theory.md)| Wykresy, drzewa, przejścia, najkrótsze ścieżki, MST, przepływy sieciowe, teoria grafów spektralnych |
| [number_theory.md](mathematics/number_theory.md)| Liczby pierwsze, arytmetyka modułowa, twierdzenia Fermata/Eulera, kryptografia |
| [abstract_algebra.md](mathematics/abstract_algebra.md)| Grupy, pierścienie, pola, przestrzenie wektorowe, teoria własnych, teoria kodowania |
| [real_analysis.md](mathematics/real_analysis.md)| Ciągi, granice, ciągłość, całkowanie Riemanna/Lebesgue'a, przestrzenie metryczne, teoria miary |
### Matematyka — matematyka stosowana
| Plik | Opis |
|------|------------|
| [optimization.md](mathematics/optimization.md)| Optymalizacja liniowa/wypukła, opadanie gradientowe, mnożniki Lagrange'a, KKT, dualność |
| [information_theory.md](mathematics/information_theory.md)| Entropia Shannona, rozbieżność KL, wzajemna informacja, przepustowość kanału, kompresja |
| [numerical_methods.md](mathematics/numerical_methods.md)| Liczba zmiennoprzecinkowa, znajdowanie pierwiastków, całkowanie numeryczne, solwery ODE, stabilność |
| [dynamical_systems.md](mathematics/dynamical_systems.md)| ODE, PDE, portrety fazowe, chaos, atraktor Lorenza, rozwidlenia |
| [stochastic_processes.md](mathematics/stochastic_processes.md)| Łańcuchy Markowa, spacery losowe, ruchy Browna, martyngały, MCMC |
### Matematyka — Fizyka
| Plik | Opis |
|------|------------|
| [classical_mechanics.md](mathematics/classical_mechanics.md)| Prawa Newtona, mechanika Lagrangianu/Hamiltona, prawa zachowania, mechanika orbitalna |
| [electromagnetism.md](mathematics/electromagnetism.md)| Równania Maxwella, pola elektryczne/magnetyczne, fale EM, obwody RLC |
| [thermodynamics_and_statistical_mechanics.md](mathematics/thermodynamics_and_statistical_mechanics.md)| Prawa termodynamiki, entropia, energia swobodna, rozkład Boltzmanna, funkcje podziału |
| [quantum_mechanics.md](mathematics/quantum_mechanics.md)| Równanie Schrodingera, niepewność, superpozycja, splątanie, kubity, bramki kwantowe |
| [relativity.md](mathematics/relativity.md)| Szczególna/ogólna teoria względności, transformacje Lorentza, krzywizna czasoprzestrzeni |
| [optics_and_waves.md](mathematics/optics_and_waves.md)| Równanie falowe, interferencja, dyfrakcja, polaryzacja, optyka geometryczna/Fouriera |
### Matematyka — matematyka inżynierska
| Plik | Opis |
|------|------------|
| [signal_processing.md](mathematics/signal_processing.md)| Transformaty Fouriera/Laplace'a/Z, FFT, filtry FIR/IIR, twierdzenie o próbkowaniu, falki |
| [control_theory.md](mathematics/control_theory.md)| Funkcje przenoszenia, regulatory PID, analiza stabilności, przestrzeń stanów, filtr Kalmana |
| [operations_research.md](mathematics/operations_research.md)| Formuły LP, problemy transportowe, programowanie dynamiczne, teoria kolejkowania |
| [game_theory.md](mathematics/game_theory.md)| Równowaga Nasha, minimax, gry kooperacyjne, wartość Shapleya, konstrukcja mechanizmu |
### Nauka i analityka danych
| Plik | Opis |
|------|------------|
| [data_science_and_analytics.md](data_science_and_analytics.md)| Cykl życia nauki o danych, eksploracyjna analiza danych, inżynieria cech, potoki |
| [data_visualization.md](data_visualization.md)| Wybór wykresu, kodowanie wizualne, projekt dashboardu, opowiadanie historii |
| [statistical_testing_and_experimentation.md](statistical_testing_and_experimentation.md)| Testowanie A/B, projektowanie eksperymentów, testowanie hipotez w praktyce |
| [feature_engineering.md](feature_engineering.md)| Tworzenie cech, selekcja, transformacja, techniki kodowania |
| [ensemble_methods.md](ensemble_methods.md)| Pakowanie, wzmacnianie, układanie w stosy, głosowanie — łączenie modeli w celu uzyskania lepszej wydajności |
| [causal_inference.md](causal_inference.md)| Rozumowanie przyczynowe, skutki leczenia, czynniki zakłócające, zmienne instrumentalne |
| [data_ethics_and_privacy.md](data_ethics_and_privacy.md)| Etyczna sztuczna inteligencja, regulacje dotyczące prywatności, wykrywanie uprzedzeń, uczciwość w ML |
| [geospatial_analysis.md](geospatial_analysis.md)| Dane przestrzenne, kartografia, GIS, geokodowanie, statystyka przestrzenna |
## Sugerowane ścieżki czytania
### **Ścieżka podstaw matematycznych**
1.`mathematics/mathematics.md`— Zbuduj podstawowy zestaw narzędzi matematycznych
2.`mathematics/statistics_and_probability.md`— Naucz się rozumować na podstawie danych
3.`mathematics/logic_and_critical_thinking.md`— Wyostrz swoje rozumowanie
4.`mathematics/discrete_mathematics.md`— Struktury formalne i liczenie
5.`mathematics/real_analysis.md`— Rygorystyczne podstawy rachunku różniczkowego
### **Ścieżka uczenia maszynowego z matematyki**
1.`mathematics/mathematics.md`— Podstawy algebry liniowej i rachunku różniczkowego
2.`mathematics/statistics_and_probability.md`— Prawdopodobieństwo i regresja
3.`mathematics/optimization.md`— Jak modele się uczą (zejście gradientowe, wypukłość)
4.`mathematics/information_theory.md`— Funkcje straty, entropia, dywergencja KL
5.`mathematics/stochastic_processes.md`— Procesy losowe i MCMC
6.`mathematics/numerical_methods.md`— Rozważania obliczeniowe
### **Ścieżka nauki o danych**
1.`mathematics/mathematics.md`— Wymagania wstępne z matematyki
2.`mathematics/statistics_and_probability.md`— Podstawy statystyczne
3.`data_science_and_analytics.md`— Przepływ pracy w nauce danych
4.`data_visualization.md`— Skuteczne przekazywanie wniosków
5.`feature_engineering.md`— Przygotowanie danych do modelowania
### **Ścieżka uczenia maszynowego**
1.`mathematics/mathematics.md`— Algebra liniowa i rachunek różniczkowy
2.`mathematics/statistics_and_probability.md`— Prawdopodobieństwo i regresja
3.`mathematics/optimization.md`— Metody optymalizacji szkolenia
4.`ensemble_methods.md`— Łączenie modeli w celu uzyskania lepszej wydajności
5.`data_science_and_analytics.md`— kompleksowe potoki ML
### **Ścieżka analityki i eksperymentów**
1.`mathematics/statistics_and_probability.md`— Podstawy statystyczne
2.`statistical_testing_and_experimentation.md`— Projektowanie i analiza eksperymentów
3.`causal_inference.md`— Wyjdź poza korelację do związku przyczynowego
4.`data_ethics_and_privacy.md`— Odpowiedzialne praktyki dotyczące danych
### **Fizyka dla ścieżki ML**
1.`mathematics/mathematics.md`— Rachunek różniczkowy i algebra liniowa
2.`mathematics/classical_mechanics.md`— Układy deterministyczne, mechanika Hamiltona
3.`mathematics/thermodynamics_and_statistical_mechanics.md`— Entropia i prawdopodobieństwo
4.`mathematics/quantum_mechanics.md`— Podstawy obliczeń kwantowych
5.`mathematics/information_theory.md`— Połączenia informacyjne i entropijne
### **Ścieżka przetwarzania i inżynierii sygnału**
1.`mathematics/mathematics.md`— Liczby różniczkowe i zespolone
2.`mathematics/optics_and_waves.md`— Podstawy fal
3.`mathematics/signal_processing.md`— Teoria transformacji i filtrowania
4.`mathematics/control_theory.md`— Sprzężenie zwrotne i stabilność
5.`mathematics/dynamical_systems.md`— Zachowanie systemu w czasie