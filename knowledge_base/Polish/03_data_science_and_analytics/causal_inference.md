---
# Metadata
title: "Causal Inference"
description: "DAGs, confounders, difference-in-differences, instrumental variables"
category: "Data Science and Analytics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [causal, inference, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "5 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Wnioskowanie przyczynowe
Wnioskowanie przyczynowe to nauka zajmująca się ustalaniem, czy jedna rzecz faktycznie powoduje drugą – a nie tylko to, czy są one skorelowane. Korelacja mówi, że dwie zmienne poruszają się razem. Przyczynowość mówi ci, że zmiana jednego spowoduje zmianę drugiego. To rozróżnienie ma ogromne znaczenie w medycynie (czy ten lek działa?), polityce (czy ta interwencja zmniejsza biedę?), biznesie (czy ta kampania reklamowa zwiększa sprzedaż?) i nauce (czy ten mechanizm wyjaśnia zjawisko?).
---

## Korelacja a przyczynowość
| Koncepcja | Opis | Przykład |
|--------|-------------|--------|
| **Korelacja** | Dwie zmienne poruszają się razem | Latem wzrasta sprzedaż lodów i liczba utonięć |
| **Przyczynowość** | Jedna zmienna wpływa bezpośrednio na inną | Palenie powoduje raka płuc |
| **Zagmatwane** | Trzecia zmienna powoduje oba | Gorąca pogoda powoduje zarówno sprzedaż lodów, jak i pływanie (i tonięcie) |
| **Odwrotna przyczyna** | Skutek faktycznie powoduje rzekomą przyczynę | Ludzie kupują suplementy zdrowotne, ponieważ są chorzy, a nie odwrotnie
| **Pozorna korelacja** | Przypadkowy związek | Spożycie sera na mieszkańca koreluje ze śmiercią w wyniku splątania prześcieradła |
---

## Ramy potencjalnych wyników
### Model przyczynowy Rubina
| Koncepcja | Opis |
|--------|------------|
| **Potencjalne wyniki** | Dla każdej jednostki istnieje wynik leczenia Y(1) i wynik braku leczenia Y(0) |
| **Efekt zabiegu** | Różnica: Y(1) - Y(0) dla danej jednostki |
| **Problem podstawowy** | Nigdy nie możemy zaobserwować jednocześnie Y(1) i Y(0) dla tej samej jednostki — możemy zobaczyć tylko jedną |
| **Średni efekt leczenia (ATE)** | Średnia indywidualnych efektów leczenia w populacji |
| **Kontrafakt** | Nieobserwowany wynik — co by się stało w innym warunku |
### Kluczowe założenia
| Założenie | Znaczenie | Jak zaspokoić |
|----------|-------|----------------|
| **Ignorowalność (bezzasadność)** | Przypisanie leczenia jest niezależne od potencjalnych wyników, biorąc pod uwagę obserwowane współzmienne | Randomizacja; zmierzyć wszystkie czynniki zakłócające |
| **Pozytywność (nakładanie się)** | Każda jednostka ma niezerowe prawdopodobieństwo otrzymania któregokolwiek leczenia | Sprawdź nakładanie się współzmiennych pomiędzy grupami |
| **SUTVA** (Założenie o stabilnej jednostkowej wartości leczniczej) | Leczenie jednej jednostki nie wpływa na wynik innej jednostki; leczenie jest spójne | Brak zakłóceń; brak ukrytych wersji leczenia |
| **Spójność** | Obserwowany wynik jest równy potencjalnemu wynikowi w ramach zastosowanego leczenia | Dobrze zdefiniowane leczenie |
---

## Metody wnioskowania przyczynowego
### Metody eksperymentalne
| Metoda | Opis | siła | Ograniczenie |
|------------|------------|---------------|------------|
| **Randomizowane badanie kontrolowane (RCT)** | Losowo przydziel jednostki do leczenia lub kontroli | Złoty standard; eliminuje zamieszanie | Drogi; czasami nieetyczne; nie może uogólniać |
| **Testy A/B** | RCT w kontekście biznesowym/technologicznym | Prosty; rygorystyczne | Wskaźniki krótkoterminowe; efekty nowości; zakłócenia |
| **Eksperymenty z przełączaniem** | Leczenie alternatywne w okresach czasu | Obsługuje zakłócenia na rynkach | Wymaga stabilnego środowiska |
### Metody quasi-eksperymentalne
| Metoda | Opis | Kluczowe założenie |
|------------|------------|----------------|
| **Różnica w różnicach (DiD)** | Porównaj zmianę wyników w czasie pomiędzy grupą leczoną i grupą kontrolną | Tendencje równoległe: grupy podążałyby tą samą trajektorią bez leczenia |
| **Nieciągłość regresji (RD)** | Porównaj jednostki tuż powyżej i tuż poniżej wartości odcięcia leczenia | Jednostki w pobliżu granicy są porównywalne (jak gdyby losowe) |
| **Zmienne instrumentalne (IV)** | Użyj zmiennej, która wpływa na leczenie, ale nie na wynik, chyba że poprzez leczenie | Instrument jest powiązany z leczeniem; wpływa na wynik tylko poprzez leczenie |
| **Kontrola syntetyczna** | Skonstruuj ważoną kombinację jednostek sterujących pasującą do leczonej jednostki | Kontrola syntetyczna dokładnie odzwierciedla scenariusz alternatywny leczonej jednostki |
| **Dopasowanie wyniku skłonności** | Dopasuj jednostki traktowane i kontrolne o podobnym prawdopodobieństwie leczenia | Wszystkie czynniki zakłócające są mierzone i uwzględniane w modelu skłonności |
### Różnica w różnicach (wizualizowana)
| Okres | Grupa leczona | Grupa kontrolna | Różnica |
|--------|-------------|--------------|------------|
| **Obróbka wstępna** | Y_t_pre | Y_c_pre | Y_t_pre - Y_c_pre |
| **Po zabiegu** | Y_t_post | Y_c_post | Y_t_post - Y_c_post |
| **DiD oszacował** | | | (Y_t_post - Y_t_pre) - (Y_c_post - Y_c_pre) |
---

## Skierowane grafy acykliczne (DAG)
DAG to wizualne narzędzia do kodowania założeń przyczynowych i identyfikowania czynników zakłócających.
### Podstawowe struktury
| Struktura | Wzór | Implikacja |
|----------|---------|------------|
| **Łańcuch** | A → B → C | A i C są powiązane poprzez B; kontrolowanie B blokuje ścieżkę |
| **Widelec** | A ← B → C | A i C są pomylone przez B; kontrolowanie B blokuje ścieżkę |
| **Zderzacz** | A → B ← C | A i C są niezależne; kontrolowanie B otwiera ścieżkę (tworzy fałszywe skojarzenie) |
### Zasady dla DAG
| Zasada | Opis |
|------|------------|
| **Kryterium backdoora** | Aby oszacować przyczynowy wpływ X na Y, zablokuj wszystkie ścieżki backdoora (ścieżki ze strzałką prowadzącą do X), warunkowując odpowiednie zmienne |
| **Kryterium frontowe** | Jeśli nie można zablokować ścieżek backdoora, użyj mediatorów: oszacuj X → M → Y w dwóch etapach |
| **Nie uzależniaj od zderzaczy** | Kontrolowanie dla wspólnego efektu otwiera fałszywą ścieżkę |
| **Nie uzależniaj od potomków zderzaczy** | Ten sam problem, co kondycjonowanie samego zderzacza |
---

## Typowe pułapki
| Pułapka | Opis | Przykład |
|--------|-------------|--------|
| **Pominięte zmienne odchylenie** | Brak kontroli ze względu na czynnik zakłócający | Szacowanie wykształcenia → zarobki bez kontroli zdolności |
| **Nadmierna kontrola** | Kondycjonowanie na mediatorze lub zderzaczu | Kontrolowanie stanowiska przy szacowaniu wykształcenia → zarobki |
| **Błąd selekcji** | Uwarunkowanie zmiennej, na którą ma wpływ leczenie | Analizując jedynie osoby zatrudnione przy badaniu szkoleń → płace |
| **Nieśmiertelny błąd czasu** | Błędna klasyfikacja osoboczasu w badaniach kohortowych | Pacjenci muszą przeżyć wystarczająco długo, aby otrzymać leczenie |
| **Regresja do średniej** | Wartości ekstremalne mają tendencję do przesuwania się w stronę średniej | Chorzy pacjenci poprawiają się po leczeniu niezależnie od |
| **Błąd po leczeniu** | Uwarunkowanie zmiennych występujących po leczeniu | Kontrola zdarzeń niepożądanych przy szacowaniu skuteczności leku |
---

## Narzędzia i biblioteki
| Narzędzie | Język | Opis |
|------|----------|------------|
| **Dlaczego** | Pythona | Biblioteka Microsoftu; Wnioskowanie przyczynowe na podstawie DAG |
| **PrzyczynowyML** | Pythona | Biblioteka firmy Uber do modelowania wzrostu i przyczynowego uczenia maszynowego |
| **EconML** | Pythona | Double ML, lasy przyczynowe, zmienne instrumentalne |
| **modele liniowe** | Pythona | IV, modele danych panelowych, DiD |
| **Dopasuj** | R | Dopasowanie wyniku skłonności |
| **digit** | R / internet | analiza DAG; zidentyfikować zestawy dostosowawcze |
| **Wpływ przyczynowy** | R/Pyton | Bayesowskie szeregi czasowe strukturalne dla wnioskowania przyczynowego |
---

## Streszczenie
Wnioskowanie przyczynowe polega na wyjściu poza „to, co się stało” i skupieniu się na tym, „co by się stało, gdyby sprawy potoczyły się inaczej”. Podstawowym wyzwaniem jest to, że nigdy nie możemy zaobserwować zarówno wyników leczenia, jak i braku leczenia w tej samej jednostce – zawsze brakuje scenariusza alternatywnego. Randomizowane eksperymenty rozwiązują ten problem poprzez porównywalność grup leczonych i kontrolnych. Gdy randomizacja nie jest możliwa, metody quasi-eksperymentalne – DiD, nieciągłość regresji, zmienne instrumentalne, kontrola syntetyczna – próbują zrekonstruować scenariusz alternatywny na podstawie danych obserwacyjnych. DAG pomagają jasno określić założenia i zidentyfikować odpowiednie zmienne, które należy kontrolować. Kluczową umiejętnością jest dokładne przemyślenie procesu generowania danych: co jest przyczyną, co jest czynnikiem zakłócającym, co jest zderzaczem i co by się stało w przypadku rozwiązania alternatywnego.