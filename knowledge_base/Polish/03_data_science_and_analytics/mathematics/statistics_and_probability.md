---
# Metadata
title: "Statistics and Probability"
description: "Probability theory, statistical inference, hypothesis testing, regression, and Bayesian methods"
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [statistics, probability, hypothesis-testing, regression, bayesian-methods, data-analysis]
difficulty_level: "intermediate"
prerequisites:
  - "../mathematics/mathematics.md"
estimated_reading_time: "14 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Statystyka i prawdopodobieństwo
Prawdopodobieństwo i statystyka to matematyczne podstawy analityki danych, uczenia maszynowego i badań naukowych. Prawdopodobieństwo mówi Ci, jak prawdopodobne są zdarzenia; statystyki mówią, jak wyciągać wnioski z danych. Razem zamieniają niepewność w wymierną wiedzę, którą można zarządzać.
---

## Teoria prawdopodobieństwa
### Podstawowe pojęcia
| Koncepcja | Opis | Przykład |
|--------|-------------|--------|
| **Przykładowa przestrzeń** | Zestaw wszystkich możliwych wyników | Rzut kostką: {1, 2, 3, 4, 5, 6} |
| **Wydarzenie** | Podzbiór przestrzeni próbnej | Wyrzucenie liczby parzystej: {2, 4, 6} |
| **Prawdopodobieństwo** | Liczba od 0 do 1 pomiaru prawdopodobieństwa | P(rolling 6) = 1/6 |
| **Prawdopodobieństwo warunkowe** | P(A|B): prawdopodobieństwo A wystąpiło w przypadku danego B | P(deszcz | pochmurno) |
| **Niepodległość** | Wydarzenia, w których jedno nie wpływa na drugie | Rzuty monetą są niezależne |
### Reguły prawdopodobieństwa
| Zasada | Formuła | Przypadek użycia |
|------|---------|--------------|
| **Zasada dodawania** | P(A ∪ B) = P(A) + P(B) - P(A ∩ B) | Prawdopodobieństwo A lub B |
| **Zasada mnożenia** | P(A ∩ B) = P(A) × P(B|A) | Prawdopodobieństwo A i B |
| **Zasada uzupełniająca** | P(nie A) = 1 - P(A) | Prawdopodobieństwo niewystąpienia zdarzenia |
| **Prawo całkowitego prawdopodobieństwa** | P(A) = Σ P(A|Bᵢ) × P(Bᵢ) | Podział według wzajemnie wykluczających się zdarzeń |
| **Twierdzenie Bayesa** | P(A|B) = P(B|A) × P(A) / P(B) | Aktualizacja przekonań za pomocą dowodów |
### Rozkłady prawdopodobieństwa
| Dystrybucja | Wpisz | Kluczowe parametry | Przypadek użycia |
|------------|------|----------------|---------|
| **Normalny (Gaussa)** | Ciągłe | Średnia (μ), odchylenie standardowe (σ) | Zjawiska naturalne, błędy pomiarowe |
| **Dwumianowy** | Dyskretny | n (próby), p (prawdopodobieństwo) | Liczy się sukces/porażka |
| **Poissona** | Dyskretny | λ (stopa) | Rzadkie zdarzenia w czasie/przestrzeni |
| **Wykładniczy** | Ciągłe | λ (stopa) | Czas pomiędzy wydarzeniami |
| **Mundur** | Obydwa | a, b (granice) | Równie prawdopodobne wyniki |
| **Chi-kwadrat** | Ciągłe | k (stopnie swobody) | Testy dobroci dopasowania |
| **t-dystrybucja** | Ciągłe | ν (stopnie swobody) | Wnioskowanie z małej próbki |
### Kluczowe właściwości dystrybucji
| Nieruchomość | Opis |
|--------------|------------|
| **Średnia (wartość oczekiwana)** | Środek masy rozkładu: E[X] = Σ xᵢ × P(xᵢ) |
| **Wariancja** | Rozrzut wokół średniej: Var(X) = E[(X − μ)²] |
| **Odchylenie standardowe** | Pierwiastek kwadratowy z wariancji; te same jednostki co dane |
| **Skrzywienie** | Asymetria rozkładu |
| **Kurtoza** | „Ogon” — jak ciężkie są ogony |
---

## Wnioskowanie statystyczne
### Statystyki opisowe a statystyki wnioskowane
| | Opisowy | Wnioskowanie |
|-------|------------|------------|
| **Cel** | Podsumuj i opisz dane | Wyciągnij wnioski na temat populacji z próby |
| **Narzędzia** | Średnia, mediana, tryb, odchylenie standardowe, wykresy | Testy hipotez, przedziały ufności, regresja |
| **Zakres** | Tylko dane, które posiadasz | Uogólnianie wykraczające poza twoją próbkę |
### Ramy testowania hipotez
| Krok | Opis |
|------|------------|
| 1. **Hipotezy stanu** | Hipoteza zerowa (H₀): brak efektu; Alternatywa (H₁): efekt istnieje |
| 2. **Wybierz poziom istotności** | α = 0,05 (konwencjonalnie) |
| 3. **Wybierz test** | Na podstawie typu danych, wielkości próby i założeń |
| 4. **Oblicz statystykę testową** | Zależy od wybranego testu |
| 5. **Znajdź wartość p** | Prawdopodobieństwo obserwacji danych, jeśli H₀ jest prawdziwe |
| 6. **Podejmij decyzję** | Jeśli p < α, odrzuć H₀; w przeciwnym razie nie odrzucaj H₀ |
### Typowe testy statystyczne
| Testuj | Kiedy stosować | Co porównuje |
|------|------------|--------------------------------|
| **test t** | Porównaj średnie z 1–2 grup | Grupuj środki do wartości lub do siebie nawzajem |
| **Test chi-kwadrat** | Dane kategoryczne | Częstotliwości zaobserwowane a oczekiwane |
| **ANOVA** | Porównaj średnie z 3+ grup | Wariancja międzygrupowa a wariancja wewnątrzgrupowa |
| **Mann-Whitney U** | Nieparametryczna alternatywa dla testu t | Rozkłady rang dwóch grup |
| **Korelacja Pearsona** | Liniowa zależność pomiędzy dwiema zmiennymi ciągłymi | r wartość od -1 do +1 |
| **Korelacja Spearmana** | Relacja monotoniczna (oparta na rangach) | wartość ρ dla danych porządkowych lub nienormalnych |
### Przedziały ufności
Przedział ufności podaje zakres wiarygodnych wartości parametru populacji:
- **95% CI dla średniej** (znane σ): x̄ ± 1,96 × (σ / √n)
- **Interpretacja**: „Mamy 95% pewności, że prawdziwa średnia populacji mieści się w tym przedziale”
- **Szerszy CI** = większa niepewność (mniejsza próba, większa zmienność lub wyższy poziom ufności)
---

## Analiza regresji
### Rodzaje regresji
| Wpisz | Zmienna zależna | Przypadek użycia |
|------|---------|--------------|
| **Regresja liniowa** | Ciągłe | Przewidywanie cen domów, sprzedaży |
| **Regresja logistyczna** | Binarny (0/1) | Klasyfikacja: wykrywanie spamu, diagnostyka chorób |
| **Regresja wielomianowa** | Ciągły (zakrzywiony) | Krzywe wzrostu, trendy nieliniowe |
| **Regresja wielokrotna** | Ciągły (2+ predyktorów) | Sterowanie dla czynników zakłócających |
| **Grzbiet / Lasso** | Ciągły (uregulowany) | Zapobieganie nadmiernemu dopasowaniu, wybór cech |
### Podstawy regresji liniowej
Model: **y = β₀ + β₁x + ε**
| Składnik | Znaczenie |
|---------------|--------|
| β₀ (przecięcie) | Wartość y, gdy x = 0 |
| β₁ (nachylenie) | Zmień y, aby uzyskać jednojednostkową zmianę x |
| ε (termin błędu) | Niewyjaśniona zmienność |
**Kluczowe wskaźniki:**
- **R² (współczynnik determinacji)**: Proporcja wariancji wyjaśniona przez model (0 do 1)
- **Skorygowany R²**: R² ukarany za liczbę predyktorów
- **RMSE**: Średniokwadratowy błąd — średni błąd przewidywania w tych samych jednostkach co y
### Założenia regresji liniowej
| Założenie | Co to znaczy | Jak sprawdzić |
|----------|-------------|-------------|
| **Liniowość** | Zależność pomiędzy X i Y jest liniowa | Wykresy punktowe |
| **Niepodległość** | Obserwacje są niezależne | Projekt badania |
| **Homoscedastyczność** | Stała wariancja reszt | Pozostałe działki |
| **Normalność** | Reszty mają rozkład normalny | Wykres Q-Q, test Shapiro-Wilka |
| **Brak współliniowości** | Predyktory nie są silnie skorelowane | VIF (współczynnik inflacji wariancji) |
---

## Statystyka Bayesa
### Częstotliwość kontra Bayesowski
| | Częstotliwy | Bayesa |
|---|------------|---------|
| **Prawdopodobieństwo oznacza** | Częstotliwość długookresowa | Stopień wiary |
| **Parametry są** | Naprawiono, ale nieznane | Zmienne losowe z rozkładami |
| **Zastosowuje** | wartości p, przedziały ufności | Rozkłady późniejsze, przedziały wiarygodne |
| **Mocne strony** | Obiektywny, ugruntowany | Zawiera wcześniejszą wiedzę, intuicyjną interpretację |
### Twierdzenie Bayesa w praktyce
**Późniejsze = (Prawdopodobieństwo × Wcześniejsze) / Dowód**
Przykład — badania lekarskie:
- Częstość występowania choroby: 1% (wcześniej)
- Czułość testu: 95% (prawdziwie dodatni współczynnik)
- Specyficzność testu: 90% (wskaźnik prawdziwie ujemny)
- Jeśli wynik testu będzie pozytywny: P(choroba | dodatni) = (0,95 × 0,01) / (0,95 × 0,01 + 0,10 × 0,99) ≈ 8,8%
Ten sprzeczny z intuicją wynik – większość pozytywnych wyników to wyniki fałszywie dodatnie, gdy choroba jest rzadka – jest **błędem dotyczącym stawki podstawowej** i pokazuje, dlaczego myślenie bayesowskie ma znaczenie.
---

## Praktyczne wskazówki
- **Zawsze wizualizuj swoje dane** przed wykonaniem jakiegokolwiek testu statystycznego
- **Sprawdź założenia** — naruszenia mogą unieważnić wyniki
- **Wielkość efektu ma znaczenie** — wynik istotny statystycznie może być praktycznie bez znaczenia
- **Korelacja nie jest związkiem przyczynowym** — nawet silne korelacje mogą powodować czynniki zakłócające
- **Wielokrotne porównania** zawyżają odsetek wyników fałszywie dodatnich – zastosuj poprawki (Bonferroni, FDR)
- **Podawaj przedziały ufności**, a nie tylko wartości p
---

## Dlaczego to ma znaczenie
Statystyka jest podstawą badań naukowych, analityki biznesowej i uczenia maszynowego. Bez tego nie można odróżnić sygnału od szumu, zidentyfikować rzeczywistych skutków od przypadkowych wahań ani dokonać prognoz z niepewnością ilościową. Niezależnie od tego, czy analizujesz testy A/B, szkolisz modele uczenia maszynowego, czy czytasz artykuły badawcze, umiejętność posługiwania się statystyką jest niezbędna.