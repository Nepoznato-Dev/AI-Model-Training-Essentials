---
# Metadata
title: "Reinforcement Learning"
description: "MDPs, Q-learning, policy gradients, RLHF, multi-agent systems"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [reinforcement, learning, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Uczenie się przez wzmacnianie
Uczenie się przez wzmacnianie (RL) to sposób, w jaki maszyny uczą się podejmować sekwencje decyzji metodą prób i błędów. W przeciwieństwie do uczenia się nadzorowanego, gdzie dla każdego przykładu jest podana poprawna odpowiedź, RL daje agentowi jedynie sygnał nagrody, a agent musi dowiedzieć się, które działania prowadzą z biegiem czasu do najlepszych wyników. Jest to podejście leżące u podstaw AlphaGo, sterowania robotycznego, sztucznej inteligencji w grach i – co najważniejsze – RLHF, techniki stosowanej do dostosowywania nowoczesnych modeli wielkojęzykowych do ludzkich preferencji.
---

## Podstawowe pojęcia
RL postrzega podejmowanie decyzji jako pętlę pomiędzy **agentem** i **środowiskiem**.
| Składnik | Rola | Przykład |
|----------|------|--------|
| **Agencie** | Osoba podejmująca decyzję | Program szachowy, robot, model językowy |
| **Środowisko** | Świat, z którym agent wchodzi w interakcję | Szachownica, magazyn, rozmowa |
| **Stan** | Obecna sytuacja | Pozycja tablicy, odczyty czujników robota, historia czatów |
| **Akcja** | Co może zrobić agent | Przesuń element, skręć w lewo, wygeneruj token |
| **Nagroda** | Sygnał zwrotny (liczba skalarna) | +1 za wygraną, -1 za awarię, wynik preferencji ludzkich |
| **Zasady** | Strategia mapująca stany na działania | „Jeśli królowi grozi zagrożenie, przesuń go” |
| **Funkcja wartości** | Oczekiwana skumulowana nagroda od stanu | „Ta pozycja w zarządzie jest warta około +3 punkty” |
### Pętla RL
```
Agent observes State → chooses Action → Environment returns new State + Reward
        ↑                                                                         |
        └─────────────────────────────────────────────────────────────────────────┘
```

Celem agenta jest maksymalizacja **skumulowanej nagrody** w czasie, a nie tylko nagrody natychmiastowej. To właśnie sprawia, że ​​RL zasadniczo różni się od uczenia się pod nadzorem.
---

## Kluczowe różnice w stosunku do innych paradygmatów uczenia się
| Aspekt | Nauka nadzorowana | Uczenie się bez nadzoru | Uczenie się przez wzmacnianie |
|--------|-----|---------------------|----------------------|
| **Sygnał** | Prawidłowe etykiety dla każdego przykładu | Brak etykiet; znajdź strukturę | Nagroda skalarna, często opóźniona |
| **Opinia** | Natychmiastowe | Brak | Opóźnione i rzadkie |
| **Sekwencja** | Każdy przykład jest niezależny | Każdy przykład jest niezależny | Działania wpływają na przyszłe stany |
| **Cel** | Minimalizuj błąd przewidywania | Odkryj wzory | Maksymalizuj skumulowaną nagrodę |
---

## Procesy decyzyjne Markowa (MDP)
MDP stanowią ramy matematyczne dla RL. Zakładają, że przyszłość zależy tylko od obecnego stanu, a nie od historii, jak się tam dostałeś (**własność Markowa**).
| Składnik | Notacja | Znaczenie |
|----------|----------|---------|
| **Stany** | S | Wszystkie możliwe sytuacje, w jakich może znaleźć się agent |
| **Działania** | | Wszystko, co może zrobić agent |
| **Funkcja przejścia** | P(s' \| s, a) | Prawdopodobieństwo osiągnięcia stanu s po podjęciu działania a w stanie s |
| **Funkcja nagrody** | R(s, a, s') | Nagroda otrzymana za przejście |
| **Współczynnik rabatowy** | γ (gamma) | Jak bardzo cenić przyszłe nagrody w porównaniu z natychmiastowymi (0 do 1) |
**Zwrot** (całkowita obniżona nagroda) wynosi:
```
G = R₁ + γR₂ + γ²R₃ + ...
```

Wysoki współczynnik dyskonta (γ bliski 1) oznacza, że ​​agent jest dalekowzroczny. Niska oznacza, że ​​jest krótkowzroczna.
---

## Klasyczne algorytmy RL
### Metody oparte na wartościach
Uczą się, jak dobry jest każdy stan (lub para stan-akcja).
| Algorytm | Kluczowa idea | Ograniczenie |
|----------|----------|------------|
| **Q-learning** | Poznaj tabelę wartości Q: Q(stan, akcja) = oczekiwana nagroda | Nie skaluje się do dużych przestrzeni stanów |
| **Głęboka sieć Q (DQN)** | Użyj sieci neuronowej do przybliżenia wartości Q | Obsługuje tylko dyskretne działania; może być niestabilny |
| **Podwójne DQN** | Napraw błąd przeszacowania Q-learningu | Wciąż ograniczone do dyskretnych działań |
Zasada aktualizacji Q-learningu:
```
Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]
```

### Metody oparte na zasadach
Uczą się one bezpośrednio polityki (strategii) bez szacowania wartości.
| Algorytm | Kluczowa idea | Zaleta |
|----------|----------|----------|
| **WZMOCNIENIE** | gradient polityki Monte Carlo; aktualizacja polityki w kierunku dobrych wyników | Prosty; współpracuje z ciągłymi działaniami |
| **PPO** (Proksymalna optymalizacja polityki) | Aktualizacje zasad klipu, aby zapobiec dużym, destabilizującym zmianom | Stabilny; szeroko stosowane; dobre ustawienie |
| **TRPO** | Metoda regionu zaufania w przypadku aktualizacji zasad | Bardziej pryncypialny niż PPO; trudniejsze do wdrożenia |
### Metody aktora-krytyka
Połącz to, co najlepsze z obu: **aktora** (polityka) i **krytyka** (funkcja wartości).
| Algorytm | Kluczowa idea |
|----------|----------|
| **A2C / A3C** | Przewaga aktora-krytyka; wykorzystuje estymację korzyści w celu zmniejszenia wariancji |
| **SAC** (krytyk-aktor miękki) | Maksymalizuj nagrodę, utrzymując eksplorację (regulacja entropii) |
| **TD3** (podwójny opóźniony DDPG) | Rozwiązanie problemu przeszacowania w przestrzeniach ciągłego działania |
---

## RLHF: Uczenie się przez wzmocnienie na podstawie informacji zwrotnej od ludzi
RLHF to technika, która umożliwiła ChatGPT. Wypełnia lukę między modelem, który potrafi przewidzieć tekst, a modelem, który generuje wyniki, które ludzie faktycznie uznają za przydatne.
### Trzy kroki
| Krok | Co się dzieje | Wyjście |
|------|------------|-------|
| **1. Nadzorowane dostrajanie (SFT)** | Dostosuj wstępnie wytrenowany model na wysokiej jakości przykładach napisanych przez ludzi | Model, który dość dobrze postępuje zgodnie z instrukcjami |
| **2. Szkolenie w zakresie modelu nagrody** | Ludzie porównują pary wyników modelu; wytrenuj model do przewidywania ludzkich preferencji | Model nagrody oceniający jakość wydruku |
| **3. Optymalizacja RL** | Użyj PPO, aby dostroić model SFT, aby zmaksymalizować wyniki modelu nagrody | Model zgodny z ludzkimi preferencjami |
### Dlaczego RLHF ma znaczenie
Bez RLHF model językowy jest jak uczeń, który przeczytał każdą książkę, ale nie wie, jak się zachować podczas rozmowy. Może generować tekst, ale może on być nieprzydatny, toksyczny lub całkowicie mijać się z sednem. RLHF uczy modelu *czego chcą ludzie* — a nie tylko tego, jak wygląda tekst.
### Warianty i alternatywy
| Metoda | Opis | Zaleta |
|------------|------------|---------------|
| **DPO** (bezpośrednia optymalizacja preferencji) | Pomiń model nagrody; bezpośrednio optymalizuj politykę na podstawie ludzkich preferencji | Prostsze; brak osobnego modelu nagrody do trenowania |
| **RLAIF** | Użyj sztucznej inteligencji (a nie ludzi), aby wygenerować etykiety preferencji | Tańsze niż etykietowanie przez ludzi |
| **Konstytucyjna sztuczna inteligencja** | Użyj zestawu zasad, aby kierować zachowaniem modelu bez ludzkich etykiet | Bardziej skalowalny; Podejście Antropiczne |
| **GRPO** (Optymalizacja polityki względnej grupy) | Porównaj wyniki w ramach grupy, a nie z oddzielnym modelem | Używany w DeepSeek-R1; zmniejsza zapotrzebowanie na sieć wartości |
---

## Eksploracja a eksploatacja
To jest główne napięcie w RL. **Wykorzystywanie** oznacza wybieranie działań, o których wiesz, że są skuteczne. **Eksploracja** oznacza próbowanie nowych rzeczy w celu odkrycia potencjalnie lepszych strategii.
| Strategia | Jak to działa | Kompromis |
|---------|-------------|----------|
| **ε-chciwy** | W większości przypadków wybieraj najlepszą akcję; losowe działanie z prawdopodobieństwem ε | Proste, ale nieefektywne |
| **Eksploracja Boltzmanna** | Wybierz działania probabilistycznie na podstawie ich szacunkowych wartości | Gładszy niż ε-chciwy |
| **UCB** (górna granica ufności) | Preferuj działania o dużej niepewności (optymizm w obliczu niepewności) | Dobre gwarancje teoretyczne |
| **Regularyzacja entropii** | Dodaj bonus za odwiedzenie różnych stanów (stosowany w SOO, PPO) | Zachęca do eksploracji przyrody |
---

## Wieloagentowe uczenie się ze wzmocnieniem
Gdy wielu agentów uczy się jednocześnie, dynamika staje się znacznie bardziej złożona.
| Scenariusz | Wyzwanie | Przykład |
|---------|-----------|---------|
| **Spółdzielnia** | Agenci muszą koordynować; cesja kredytu jest trudna | Robotyczne drużyny piłkarskie; rozproszone sieci czujników |
| **Konkurencyjny** | Przeciwnicy dostosowują się; środowisko jest niestacjonarne | Gra AI (poker, StarCraft); cyberbezpieczeństwo |
| **Mieszane** | Niektórzy agenci współpracują, inni konkurują | rynki aukcyjne; systemy ruchu |
| Algorytm | Opis |
|---------------|------------|
| **MADDPG** | Wersja wieloagentowa DDPG; scentralizowany krytyk, zdecentralizowani aktorzy |
| **MAPPO** | Wieloagentowy PPO; powszechnie stosowane w praktyce |
| **Gra własna** | Agenci trenują przeciwko swoim kopiom (AlphaGo, AlphaStar) |
---

## Transfer z Sima do Realu
Szkolenie robotów w prawdziwym świecie jest powolne i niebezpieczne. Zamiast tego agenci szkolą się w symulacji i przenoszą się do rzeczywistości.
| Wyzwanie | Rozwiązanie |
|----------|----------|
| **Luka w rzeczywistości** (symulacja ≠ świat rzeczywisty) | Randomizacja domeny: zmieniaj parametry fizyczne podczas treningu |
| **Nieefektywność próbki** | Użyj RL opartego na modelu lub trenuj duże równoległe symulacje |
| **Bezpieczeństwo** | Ograniczone RL: karaj niebezpieczne działania podczas treningu |
| **Częściowa obserwowalność** | Pociąg z hałaśliwymi czujnikami i opóźnionymi obserwacjami |
Firmy takie jak Boston Dynamics i Tesla szeroko korzystają z symulacji, ale różnica między wydajnością symulowaną a wydajnością fizyczną pozostaje jednym z największych wyzwań w tej dziedzinie.
---

## Narzędzia i struktury
| Narzędzie | Cel | Najlepsze dla |
|------|---------|--------------|
| **Stabilne linie bazowe3** | Czyste implementacje Pythona PPO, SAC, TD3, DQN | Uczenie się i prototypowanie |
| **RLlib** | Skalowalna biblioteka RL zbudowana na platformie Ray | Szkolenia rozproszone na dużą skalę |
| **WyczyśćRL** | Implementacje jednoplikowe do celów badawczych | Głębokie zrozumienie algorytmów |
| **Gimnazjum (OpenAI)** | Standaryzowany interfejs środowiska | Definiowanie problemów RL |
| **Siłownia Izaaka / Laboratorium Izaaka** | Symulacja fizyki akcelerowana przez GPU | Robotyka, od symulacji do rzeczywistości |
| **TRL** (Biblioteka RL transformatora) | RLHF, DPO, PPO dla modeli językowych | Dopasowywanie LLM |
| **OpenRLHF** | Rozproszona struktura RLHF | Trening dużych modeli z RLHF |
---

## Praktyczne wskazówki
- **Zacznij od PPO.** To najbardziej niezawodny algorytm ogólnego przeznaczenia. Jeśli nie masz pewności, czego użyć, ustawieniem domyślnym jest PPO.
- **Normalizuj swoje nagrody.** Skalowanie nagród znacząco wpływa na stabilność treningu.
- **Używaj środowisk wektorowych.** Równoległe uruchamianie wielu środowisk (np. 8–64) stabilizuje szacunki gradientu i ogromnie przyspiesza trening.
- **Monitoruj zarówno nagrodę, jak i entropię.** Jeśli entropia spadnie do zera, Twój agent przestał eksplorować i może utknąć w lokalnym minimum.
- **Kształtowanie nagrody to sztuka.** Zaprojektowanie odpowiedniej funkcji nagrody jest często najtrudniejszą częścią. Nieliczne nagrody (tylko na końcu) sprawiają, że nauka jest wyjątkowo powolna. Gęste, dobrze ukształtowane nagrody kierują agentem, ale mogą powodować niezamierzone zachowanie.
- **RLHF jest delikatny.** Małe zmiany w modelu nagrody lub hiperparametrach PPO mogą powodować duże spadki jakości. DPO jest bardziej stabilną alternatywą, jeśli nie potrzebujesz pełnego rurociągu RLHF.
---

## Streszczenie
Uczenie się przez wzmacnianie to nauka o tym, jak agenci uczą się podejmować decyzje poprzez interakcję. Obejmuje ona klasyczne algorytmy, takie jak Q-learning, po nowoczesne metody głębokiego RL, takie jak PPO i SAC, i stanowi podstawę niektórych z najważniejszych najnowszych osiągnięć w dziedzinie sztucznej inteligencji — od grania w gry po dopasowywanie modelu językowego. Podstawowe wyzwanie pozostaje takie samo: jak nauczyć się optymalnego zachowania, gdy informacja zwrotna jest opóźniona, rzadka i zaszumiona? Odpowiedź — metodą prób i błędów, kierując się sprytną matematyką — okazuje się jedną z najpotężniejszych idei w całej sztucznej inteligencji.