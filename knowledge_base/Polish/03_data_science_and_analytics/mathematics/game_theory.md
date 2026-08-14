<!--
---
# Metadata
title: "Game Theory"
description: "Strategic-form games, Nash equilibrium, dominant strategies, minimax theorem, cooperative games, Shapley value, mechanism design, auction theory, and connections to multi-agent reinforcement learning"
category: "Data Science and Analytics"
subcategory: "Mathematics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into game theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [game-theory, nash-equilibrium, minimax, cooperative-games, shapley-value, mechanism-design, auction-theory, multi-agent-rl]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "optimization.md"
  - "statistics_and_probability.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
#Teoria gier
Teoria gier to matematyka interakcji strategicznej — sytuacji, w których wynik zależy nie tylko od twoich własnych wyborów, ale od wyborów innych. Od wojen cenowych między firmami po wyścigi zbrojeń nuklearnych, od aukcji internetowych po biologię ewolucyjną – teoria gier dostarcza narzędzi do analizy konfliktów i współpracy. Staje się coraz bardziej istotna w uczeniu maszynowym poprzez wieloagentowe uczenie się przez wzmacnianie, generatywne sieci kontradyktoryjne (GAN) i projektowanie mechanizmów dla platform internetowych.
---

## Gry w formie strategicznej
### Definicja
**Gra w formie strategicznej (w formie normalnej)** składa się z:
- Zbiór graczy N = {1, 2, ..., n}
- Zestawy strategii S₁, S₂, ..., Sₙ dla każdego gracza
- Funkcje wypłat u₁, u₂, ..., uₙ mapujące profile strategii na liczby rzeczywiste
### Przykład: dylemat więźnia
| | Współpracuj (C) | Wada (D) |
|---|---------------|------------|
| **Współpraca (C)** | (-1, -1) | (-3, 0) |
| **Wada (D)** | (0, −3) | (-2, -2) |
| Analiza | Wynik |
|---------|--------|
| Strategia dominująca | Wada (D dominuje nad C dla obu graczy) |
| Równowaga Nasha | (D, D) z wypłatą (-2, -2) |
| Optimum społeczne | (C, C) z wypłatą (-1, -1) |
| Dylemat | Indywidualna racjonalność prowadzi do zbiorowej irracjonalności |
### Więcej klasycznych gier
**Wojna płci:**
| | Opera | Piłka nożna |
|---|-------|---------|
| Opera | (2, 1) | (0, 0) |
| Piłka nożna | (0, 0) | (1, 2) |
Dwie równowagi Nasha: (Opera, Opera) i (Piłka nożna, Piłka nożna).
**Kurczak (Jastrząb-Gołąb):**
| | Jastrząb | Gołąb |
|---|------|------|
| Jastrząb | (-10, -10) | (5, 0) |
| Gołąb | (0, 5) | (1, 1) |
Dwie równowagi Nasha: (Jastrząb, Gołąb) i (Gołąb, Jastrząb).
---

## Strategie dominujące
| Koncepcja | Definicja |
|------------|------------|
| **Ściśle dominujący** | Strategia sᵢ daje wyższą wypłatę niż jakakolwiek inna strategia, niezależnie od wyborów przeciwników |
| **Słabo dominujący** | Strategia sᵢ daje co najmniej tak wysoką wygraną jak każda inna, a w przypadku niektórych profili przeciwników znacznie wyższą |
| **Strategia zdominowana** | Strategia, która nigdy nie jest najlepszą odpowiedzią |
**Iteracyjna eliminacja strategii zdominowanych:**
1. Usuń wszelkie strategie ściśle zdominowane
2. Powtarzaj, aż nie będzie można już usunąć
3. Jeśli pozostaje jeden profil strategii, jest to unikalna równowaga Nasha
---

## Równowaga Nasha
**Równowaga Nasha** to profil strategii, w którym żaden gracz nie może poprawić swojej wypłaty poprzez jednostronną zmianę swojej strategii.
### Definicja
(s₁*, s₂*, ..., sₙ*) jest równowagą Nasha, jeśli dla każdego gracza i:
uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*) dla wszystkich sᵢ ∈ Sᵢ
### Znajdowanie równowagi Nasha (gry 2×2)
**Najlepsza metoda odpowiedzi:**
1. W każdej kolumnie podkreśl najlepszą odpowiedź gracza 1
2. W każdym rzędzie podkreśl najlepszą odpowiedź gracza 2
3. Komórki, w których oba są podkreślone, to równowagi Nasha
### Istnienie (twierdzenie Nasha)
Każda skończona gra ma co najmniej jedną równowagę Nasha (prawdopodobnie w strategiach mieszanych).
### Strategie mieszane
**Strategia mieszana** to rozkład prawdopodobieństwa dla strategii czystych.
| Koncepcja | Definicja |
|------------|------------|
| Strategia mieszana σᵢ | Rozkład prawdopodobieństwa po Sᵢ |
| Strategia mieszana NE | Żaden gracz nie może poprawić oczekiwanej wypłaty, zmieniając swoją mieszankę |
| Wsparcie | Zestaw czystych strategii rozgrywanych z dodatnim prawdopodobieństwem |
**Przykład praktyczny: dopasowanie groszy**
| | Głowy | Ogony |
|---|-------|-------|
| Głowy | (1, -1) | (-1, 1) |
| Ogony | (-1, 1) | (1, -1) |
Brak czystej strategii NE. Mieszane NE: obaj grają H i T z prawdopodobieństwem ½ każdy.
---

## Twierdzenie o Minimaksie
### Gry o sumie zerowej
W **grze o sumie zerowej** zysk jednego gracza jest dokładnie stratą drugiego: u₁ + u₂ = 0.
### Twierdzenie o Minimaksie von Neumanna
Dla każdej skończonej gry dla dwóch graczy o sumie zerowej:
max_{σ₁} min_{σ₂} u₁(σ₁, σ₂) = min_{σ₂} max_{σ₁} u₁(σ₁, σ₂)
**maksymin** (najlepszy najgorszy przypadek dla gracza 1) równa się **minimaks** (najlepszy najgorszy przypadek dla gracza 2). Ta wspólna wartość to **wartość gry**.
### Rozwiązywanie gier o sumie zerowej
Dla gry o sumie zerowej 2×2 z macierzą:
| | L | R |
|---|---|---|
| T | | b |
| B | c | d |
Optymalna strategia mieszana gracza 1: zagraj w T z prawdopodobieństwem p = (d-c)/((a-b)+(d-c))
Wartość gry: v = (ad−bc)/((a−b)+(d−c))
---

## Gry w rozbudowanej formie
Gry z sekwencyjnymi ruchami są reprezentowane jako **drzewa gier**.
### Kluczowe pojęcia
| Koncepcja | Definicja |
|------------|------------|
| **Drzewo gry** | Drzewo pokazujące wszystkie możliwe sekwencje ruchów |
| **Zestaw informacji** | Zbiór węzłów, których gracz nie może rozróżnić |
| **Doskonała informacja** | Każdy zbiór informacji jest singletonem (wszystkie ruchy są obserwowalne) |
| **Podgra idealna NE** | Równowaga Nasha w każdej podgrze |
| **Indukcja wsteczna** | Rozwiązuj od końca drzewa do tyłu |
### Twierdzenie Zermelo
W grach dwuosobowych o skończonych informacjach i bez szans: albo jeden z graczy ma zwycięską strategię, albo obaj mogą wymusić remis (np. szachy).
---

## Gry kooperacyjne
W **grach kooperacyjnych** gracze mogą zawierać wiążące umowy i koalicje.
### Funkcja charakterystyczna
Gra kooperacyjna jest definiowana przez **funkcję charakterystyczną** v: 2^N → ℝ, gdzie v(S) to wartość, jaką koalicja S może osiągnąć.
| Nieruchomość | Definicja |
|-------------|------------|
| **Superaddytywny** | v(S ∪ T) ≥ v(S) + v(T) dla rozłącznego S, T |
| **Wypukły** | v(S ∪ {i}) - v(S) ≤ v(T ∪ {i}) - v(T) dla S ⊂ T |
### Rdzeń
**Rdzeń** to zbiór przydziałów, w przypadku których żadna koalicja nie może poprawić się poprzez oderwanie się:
Rdzeń = {x ∈ ℝⁿ : Σᵢ∈N xᵢ = v(N), Σᵢ∈S xᵢ ≥ v(S) dla wszystkich S ⊂ N}
Rdzeń może być pusty – w takim przypadku nie istnieje stabilna alokacja.
### Wartość Shapleya
**Wartość Shapleya** zapewnia wyjątkową sprawiedliwą alokację w oparciu o wkłady krańcowe:
φᵢ = Σ_{S ⊂ N\{i}} (|S|!(n−|S|−1)!/n!) · [v(S ∪ {i}) − v(S)]
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Wydajność | Σ φᵢ = v(N) (cała wartość jest rozdzielona) |
| Symetria | Równi współpracownicy otrzymują równe wypłaty |
| Manekin gracza | Osoby niebędące współautorami otrzymują zero |
| Addytywność | φ(v + w) = φ(v) + φ(w) |
**Interpretacja:** Wartość Shapleya każdego gracza to jego średni marginalny wkład we wszystkich możliwych porządkach tworzenia koalicji.
### Sprawdzony przykład
Trzej gracze: v(∅) = 0, v({1}) = 0, v({2}) = 0, v({3}) = 0, v({1,2}) = 50, v({1,3}) = 70, v({2,3}) = 60, v({1,2,3}) = 100.
| Gracz | Wkłady marginalne (uśrednione w stosunku do zamówień) | Wartość Shapleya |
|------------|----------------------------------------------------------------|----------------------------|
| 1 | (100+50+70+70+50+0)/6 = 56,7 | 37,5 |
| 2 | (100+50+60+60+50+0)/6 | 27,5 |
| 3 | (100+70+60+70+60+0)/6 | 35,0 |
(Obliczone dokładnie przy użyciu wzoru Shapleya dla każdej permutacji.)
---

## Projekt mechanizmu
**Projekt mechanizmu** to „teoria gier odwrotnych” — zamiast analizować dane gry, projektuj gry, które dają pożądane wyniki.
### Zasada objawienia
Każdy mechanizm, który osiąga pożądany rezultat, można zastąpić **mechanizmem bezpośredniego objawienia**, w którym mówienie prawdy jest równowagą Nasha.
### Teoria aukcji
| Typ aukcji | Zasady | Równoważność przychodów |
|------------|-------|-------------------------|
| **Zapieczętowana oferta pierwszej ceny** | Osoba, która zaoferuje najwyższą cenę, wygrywa i płaci swoją ofertę | Wszystkie aukcje standardowe przynoszą takie same oczekiwane przychody |
| **Zapieczętowana oferta drugiej ceny (Vickrey)** | Wygrywa licytant, który zaoferuje najwyższą cenę, płaci drugą najwyższą ofertę | (pod niezależnymi wartościami prywatnymi) |
| **Angielski (rosnąco)** | Ceny rosną; pierwszy, który zaakceptuje wygrywa | — |
| **Holenderski (malejąco)** | Cena spada; pierwszy, który zaakceptuje wygrywa | — |
### Aukcja Vickreya (druga cena)
**Strategia dominująca:** Licytuj swoją prawdziwą wartość.
| Nieruchomość | Oświadczenie |
|---------|-----------|
| Wierna licytacja | Strategia słabo dominująca |
| Wydajność | Przedmiot trafia do licytanta, który zaoferuje najwyższą wartość |
| Przychody | Taki sam oczekiwany dochód jak w przypadku pierwszej ceny (twierdzenie o równoważności przychodów) |
### Optymalny projekt aukcji (Myerson)
Aukcja maksymalizująca przychody:
- Przydziela oferentowi z najwyższą **wirtualną wyceną**
- Ustala cenę minimalną
- Wirtualna wycena: ψ(v) = v − (1−F(v))/f(v)
---

## Połączenia z uczeniem maszynowym
### Generacyjne sieci przeciwstawne (GAN)
Sieci GAN to gra dla dwóch graczy pomiędzy generatorem G i dyskryminatorem D:
min_G max_D V(D, G) = E[log D(x)] + E[log(1 − D(G(z)))]
| Koncepcja teorii gier | Odpowiednik GAN |
|---------------------------------|--------------------------------|
| Gra dla dwóch graczy o sumie zerowej | Generator vs dyskryminator |
| Równowaga Nasha | G generuje dane rzeczywiste, D wyprowadza ½ wszędzie |
| Minimaks | Funkcja celu GAN |
| Załamanie trybu | Nieosiągnięcie równowagi |
### Wieloagentowe uczenie się ze wzmocnieniem (MARL)
| Koncepcja | Aplikacja MARL |
|--------|--------------------------------|
| Równowaga Nasha | Stabilne zasady w ustawieniach wielu agentów |
| Minimaks | Solidna polityka wobec wrogich przeciwników |
| Gry kooperacyjne | Tworzenie koalicji, podział zadań |
| Wartość Shapleya | Cesja kredytowa (który agent wniósł jaki wkład?) |
| Projekt mechanizmu | Projektowanie zachęt w systemach wieloagentowych |
| Fikcyjna gra | Algorytm uczenia zbieżny do równowagi Nasha |
### Inne połączenia ML
| Aplikacja | Narzędzie teorii gier |
|------------|--------------------------------|
| Projekt aukcji reklam (Google, Facebook) | Projekt mechanizmu, teoria aukcji |
| Projekt marketplace (Uber, Airbnb) | Teoria dopasowania, konstrukcja mechanizmu |
| Odporność przeciwna | Gry o sumie zerowej pomiędzy atakującym a obrońcą |
| Sprawiedliwy podział | Wartość Shapleya, przydział bez zazdrości |
| Uczenie się stowarzyszone | Teoria gier kooperacyjnych do pomiaru wkładu |
| Systemy rekomendacji | Projekt mechanizmu ujawniania prawdziwych preferencji |
---

## Streszczenie
| Koncepcja | Podstawowy pomysł | Kluczowy wynik |
|--------|-----------|------------|
| Gry strategiczne | Gracze, strategie, wypłaty | Reprezentacja macierzy gier |
| Dominujące strategie | Najlepszy bez względu na innych | Iterowana eliminacja |
| Równowaga Nasha | Brak korzystnego jednostronnego odchylenia | Istnieje w każdej skończonej grze |
| Strategie mieszane | Losuj działania | Twierdzenie Nasha o istnieniu |
| Minimaks | Najlepszy najgorszy przypadek (o sumie zerowej) | Twierdzenie o minimaksie von Neumanna |
| Forma rozszerzona | Ruchy sekwencyjne | Indukcja wsteczna, doskonałość podgry |
| Gry kooperacyjne | Wiążące koalicje | Rdzeń, wartość Shapleya |
| Projekt mechanizmu | Projektuj gry pod kątem wyników | Zasada objawienia, aukcje optymalne |
| Teoria aukcji | Sprzedaż poprzez konkurencję | Równoważność przychodów, aukcja Vickrey |
Teoria gier to matematyka myślenia strategicznego. W świecie coraz bardziej zaludnionym przez wchodzących w interakcje agentów AI, zautomatyzowane rynki i systemy kontradyktoryjne teoria gier zapewnia niezbędny zestaw narzędzi do przewidywania zachowań, projektowania mechanizmów i budowania solidnych systemów wieloagentowych. Analitykom danych wyjaśnia, jak działają sieci GAN, w jaki sposób aukcje internetowe generują miliardy przychodów i jak budować systemy sztucznej inteligencji, które dobrze radzą sobie w konkurencyjnych środowiskach.