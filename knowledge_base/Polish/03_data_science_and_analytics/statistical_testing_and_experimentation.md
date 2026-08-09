---
# Metadata
title: "Statistical Testing and Experimentation"
description: "Hypothesis testing, A/B testing, effect size, causal inference"
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
tags: [statistical, testing, experimentation, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Testy statystyczne i eksperymenty
Statystyka jest gramatyką nauki. Daje narzędzia umożliwiające odróżnienie rzeczywistych wzorców od przypadkowego szumu, zmierzenie, czy zmiana rzeczywiście poprawiła sytuację i podejmowanie decyzji w warunkach niepewności. W tym pliku omówiono podstawowe pojęcia związane z testowaniem hipotez, projektowaniem eksperymentów i typowymi pułapkami, w jakie wpadają ludzie.
---

## Ramy testowania hipotez
Każdy test statystyczny kieruje się tą samą logiką:
1. **Podać hipotezę zerową (H₀)**: Nie ma efektu / nie ma różnicy.
2. **Podać alternatywną hipotezę (H₁)**: Istnieje efekt/różnica.
3. **Wybierz poziom istotności (α)**: Zwykle 0,05 (5% szans na wynik fałszywie dodatni).
4. **Zbierz dane i oblicz statystykę testową**.
5. **Obliczyć wartość p**: Prawdopodobieństwo zaobserwowania tego wyniku (lub bardziej ekstremalnego), jeśli H₀ jest prawdziwe.
6. **Podejmij decyzję**: Jeśli p < α, odrzuć H₀ (istotne statystycznie). W przeciwnym razie nie odrzucaj H₀.
### Kluczowe pojęcia
| Koncepcja | Znaczenie | Powszechne błędne przekonanie |
|--------|---------|----------|
| **wartość p** | P(dane \| H₀ jest prawdziwe) | NIE „prawdopodobieństwo, że H₀ jest prawdziwe” |
| **α (poziom istotności)** | Próg odrzucenia H₀ | Nie jest miarą ważności efektu |
| **Istotność statystyczna** | Wynik mało prawdopodobny ze względu na przypadek | NIE oznacza praktycznie znaczącego |
| **Wielkość efektu** | Wielkość obserwowanego efektu | Oddzielne od wartości p; niewielki efekt może być znaczący przy dużym N |
| **Moc** | Prawdopodobieństwo prawidłowego odrzucenia fałszywego H₀ | Zwykle celuj w 80%+ |
| **Przedział ufności** | Zakres możliwych wartości parametru | 95% CI nie oznacza „95% prawdopodobieństwa, że ​​prawdziwa wartość mieści się w tym zakresie” |
---

## Rodzaje błędów
| | H₀ jest prawdą | H₀ jest fałszywe |
|---|-----------|------------|
| **Odrzuć H₀** | Błąd typu I (fałszywie dodatni) | ✅ Prawidłowe (prawdziwie pozytywne) |
| **Nie odrzucono H₀** | ✅ Prawidłowe (prawdziwie negatywne) | Błąd typu II (fałszywie ujemny) |
| Błąd | Symbol | Znaczenie |
|-------|--------|--------|
| **Typ I** | α | Wnioskowanie, że istnieje efekt, gdy go nie ma |
| **Typ II** | β | Brakuje prawdziwego efektu |
---

## Wybór odpowiedniego testu
| Scenariusz | Testuj | Założenia |
|---------|------|------------|
| Porównaj średnie z 2 grup | **test t** (niezależny) | Rozkład normalny, równa wariancja |
| Porównaj średnie sparowanych obserwacji | **Test t dla par** | Różnice mają rozkład normalny |
| Porównaj średnie z 3+ grup | **ANOVA** | Rozkład normalny, równa wariancja |
| Porównaj rozkłady kategoryczne | **Test chi-kwadrat** | Wystarczająca wielkość próbki na komórkę |
| Porównanie rozkładów (nieparametrycznych) | **Mann-Whitney U** | Brak założenia normalności |
| Porównaj ponad 3 grupy (nieparametryczne) | **Kruskal-Wallis** | Brak założenia normalności |
| Test korelacji | **Pearson** (liniowy) lub **Spearman** (monotoniczny) | Pearson: normalność; Spearman: w oparciu o rangę |
| Sprawdź, czy dane mają rozkład | **Kołmogorow-Smirnow** | Dane ciągłe |
### Parametryczny a nieparametryczny
| | Parametryczny | Nieparametryczny |
|---|-----------|--------------|
| **Założenia** | Dane mają określony rozkład (zwykle normalny) | Brak założenia dotyczącego rozkładu |
| **Moc** | Wyższe, gdy założenia zostały spełnione | Niższy, ale solidniejszy |
| **Kiedy stosować** | Duże próbki, w przybliżeniu normalne dane | Małe próbki, dane wypaczone, dane porządkowe |
---

## Szczegółowe testy szczegółowe
### Test t
Porównuje średnie dwóch grup.
| Wariant | Przypadek użycia |
|--------|----------|
| **Niezależny test t** | Dwie oddzielne grupy (leczenie vs kontrola) |
| **Test t dla par** | Ta sama grupa mierzona dwukrotnie (przed i po) |
| **Test t dla jednej próby** | Porównaj średnią próbki ze znaną wartością |
```python
from scipy import stats

# Independent t-test
t_stat, p_value = stats.ttest_ind(group_a, group_b)
```

### ANOVA (analiza wariancji)
Porównuje średnie z 3 lub więcej grup. Testuje, czy co najmniej jedna średnia grupowa różni się od pozostałych.
| Wpisz | Projekt |
|------|------------|
| **Jednokierunkowa ANOVA** | Jedna niezależna zmienna z ponad 3 poziomami |
| **Dwuczynnikowa ANOVA** | Dwie niezależne zmienne; testuje efekty interakcji |
| **ANOVA powtarzanych pomiarów** | Te same obiekty mierzone w różnych warunkach |
Jeśli analiza ANOVA jest istotna, wykonaj **testy post-hoc** (HSD Tukeya), aby dowiedzieć się, które konkretne grupy się różnią.
### Test chi-kwadrat
Testuje, czy dwie zmienne kategoryczne są niezależne.
| Przypadek użycia | Przykład |
|--------------|--------|
| **Test niezależności** | Czy płeć ma związek z preferencjami dotyczącymi produktu? |
| **Dobroć dopasowania** | Czy rzut kostką ma równomierny rozkład? |
**Ogólna zasada**: oczekiwana liczba każdej komórki powinna wynosić co najmniej 5.
---

## Testowanie A/B
Testowanie A/B polega na zastosowaniu testowania hipotez do decyzji biznesowych — zazwyczaj polega na porównaniu kontroli (A) z wariantem (B).
### Proces projektowania
| Krok | Opis |
|------|------------|
| **1. Zdefiniuj hipotezę** | „Zmiana koloru przycisku z niebieskiego na zielony zwiększy współczynnik klikalności” |
| **2. Wybierz metrykę** | Podstawowy: współczynnik klikalności. Drugorzędne: współczynnik konwersji, przychody. |
| **3. Oblicz wielkość próbki** | Na podstawie minimalnego wykrywalnego efektu, mocy (80%) i istotności (5%) |
| **4. Losuj** | Losowo przypisz użytkowników do kontroli i leczenia |
| **5. Uruchom eksperyment** | Zbieraj dane do momentu osiągnięcia docelowej wielkości próby |
| **6. Analiza** | Porównaj metryki za pomocą odpowiedniego testu statystycznego |
| **7. Zdecyduj** | Wdrożyć, jeśli jest to istotne statystycznie i praktycznie |
### Obliczanie wielkości próbki
Potrzebna wielkość próbki zależy od:
| Czynnik | Wpływ na wielkość próby |
|------------|----------------------|
| **Mniejszy efekt do wykrycia** | Potrzebujesz więcej próbek |
| **Wyższa moc** | Potrzebujesz więcej próbek |
| **Niższy poziom istotności** | Potrzebujesz więcej próbek |
| **Większa wariancja** | Potrzebujesz więcej próbek |
### Typowe błędy w testach A/B
| Błąd | Dlaczego jest źle |
|--------|--------------|
| **Zaglądam wcześnie** | Codzienne sprawdzanie wyników zwiększa odsetek wyników fałszywie pozytywnych |
| **Wiele wskaźników bez korekty** | Testowanie 20 metryk przy α=0,05 → przypadkowo spodziewaj się 1 fałszywie dodatniego wyniku |
| **Zatrzymanie przed celem N** | Test o zbyt małej mocy nie jest w stanie wykryć rzeczywistych efektów |
| **Ignorując sezonowość** | Przeprowadzanie testu w okresie wakacyjnym w porównaniu z normalnym tygodniem |
| **Przypisanie nielosowe** | Błąd selekcji (np. przydzielanie nowych użytkowników do leczenia) |
| **Mylisz znaczenie z ważnością** | Wzrost o 0,1% może być statystycznie istotny, ale nie warty wysyłki |
---

## Wiele porównań
Kiedy przeprowadzasz wiele testów jednocześnie, ryzyko wystąpienia co najmniej jednego fałszywie pozytywnego wyniku dramatycznie wzrasta.
| Liczba testów | Prawdopodobieństwo ≥1 wyniku fałszywie dodatniego (przy α=0,05) |
|----------------|------------------------------------------------------------|
| 1 | 5% |
| 5 | 23% |
| 10 | 40% |
| 20 | 64% |
### Poprawki
| Metoda | Jak to działa | Kiedy stosować |
|------------|------------|------------|
| **Bonferroni** | Podziel α przez liczbę testów (α/n) | Konserwatywny; kilka porównań |
| **Holm-Bonferroni** | Procedura stopniowego obniżania; mniej konserwatywny | Ogólne zastosowanie |
| **Benjamini-Hochberg (FDR)** | Kontroluje współczynnik fałszywych odkryć | Wiele testów; analiza eksploracyjna |
---

## Rozmiar efektu
Wartości P informują *czy* istnieje efekt. Rozmiar efektu mówi *jak duży* jest.
| Zmierz | Dla | Interpretacja |
|--------|-----|--------------|
| **K**wa Cohena** | Różnica między dwoma średnimi | 0,2 = mały, 0,5 = średni, 0,8 = duży |
| **Rz Pearsona** | Korelacja | 0,1 = mały, 0,3 = średni, 0,5 = duży |
| **η² (eta-kwadrat)** | ANOWA | 0,01 = mały, 0,06 = średni, 0,14 = duży |
| **Iloraz szans** | Wyniki kategoryczne | 1,0 = brak efektu; >1 lub <1 = efekt |
**Zawsze podawaj wielkość efektu wraz z wartościami p.** Wynik może być statystycznie istotny, ale praktycznie bez znaczenia.
---

## Bayesowski kontra częstość
| Aspekt | Częstotliwy | Bayesa |
|------------|------------|--------------|
| **Prawdopodobieństwo** | Długoterminowa częstotliwość zdarzeń | Stopień wiary |
| **Parametry** | Naprawiono, ale nieznane | Zmienne losowe z rozkładami |
| **Zastosowuje** | wartości p, przedziały ufności, testy hipotez | Rozkłady późniejsze, przedziały wiarygodne |
| **Wcześniej** | Nie uwzględniono żadnych wcześniejszych przekonań | Wyraźna wcześniejsza dystrybucja |
| **Interpretacja** | „Gdybyśmy powtórzyli ten eksperyment wiele razy…” | „Biorąc pod uwagę dane, prawdopodobieństwo, że…” |
| **Mocne strony** | Obiektywny, ugruntowany, prosty | Intuicyjna interpretacja, uwzględnia wcześniejszą wiedzę |
| **Słabości** | wartości p powszechnie źle rozumiane | Wybór przeora może być subiektywny |
---

## Podstawy wnioskowania przyczynowego
Korelacja nie jest przyczynowością. Ale czasami trzeba wiedzieć *czy X spowodowało Y*, a nie tylko, czy są one ze sobą powiązane.
| Metoda | Opis | Kiedy stosować |
|------------|------------|------------|
| **Losowe eksperymenty** | Złoty standard; losowe przypisanie eliminuje czynniki zakłócające | Kiedy możesz losowo |
| **Różnica w różnicach (DiD)** | Porównaj zmiany w czasie między leczeniem a grupą kontrolną | Zmiany polityki, naturalne eksperymenty |
| **Nieciągłość regresji (RDD)** | Wykorzystaj próg odcięcia | Stypendia, progi kwalifikacyjne |
| **Zmienne instrumentalne (IV)** | Użyj instrumentu, który wpływa na leczenie, ale nie bezpośrednio na wynik | Kiedy randomizacja nie jest możliwa |
| **Dopasowanie wyniku skłonności** | Dopasuj jednostki traktowane i kontrolne na podstawie obserwowanych cech | Badania obserwacyjne |
---

## Typowe błędy statystyczne
| Błąd | Opis |
|--------|------------|
| **p-hakowanie** | Próbujesz wielu analiz, aż znajdziesz p < 0,05 |
| **CZEKA** | Stawianie hipotez po poznaniu wyników |
| **Błąd przetrwania** | Patrzenie tylko na sukcesy (np. firmy odnoszące sukcesy) |
| **Paradoks Simpsona** | Trend odwraca się, gdy dane są agregowane lub dzielone według grup |
| **Zaniedbanie stopy bazowej** | Ignorowanie wcześniejszego prawdopodobieństwa przy interpretacji wyników |
| **Błąd ekologiczny** | Wnioskowanie o indywidualnych zachowaniach na podstawie danych na poziomie grupy |
| **Zagmatwane** | Trzecia zmienna wyjaśnia zaobserwowaną zależność |
| **Przedmierne dopasowanie** | Model przechwytuje szum, a nie sygnał |
---

## Streszczenie
Testowanie statystyczne polega na podejmowaniu decyzji w warunkach niepewności, zachowując uczciwość intelektualną. Przed zebraniem danych zawsze formułuj swoje hipotezy. Wybierz odpowiedni test dla swojego typu danych. Raportuj rozmiary efektów, a nie tylko wartości p. Poprawne w przypadku wielokrotnych porównań. I pamiętaj: znaczenie statystyczne to nie to samo, co znaczenie praktyczne.