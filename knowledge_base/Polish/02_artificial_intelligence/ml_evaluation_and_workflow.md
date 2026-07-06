# Ocena uczenia maszynowego i przepływ pracy

Praktyczny przewodnik po cyklu życia uczenia maszynowego — od formułowania problemów po monitorowanie produkcji — ze szczególnym uwzględnieniem metryk, walidacji i debugowania.

---

## Przepływ pracy ML (CRISP-ML)

1. **Zrozumienie biznesu**: Zdefiniuj cel i kryteria sukcesu.
2. **Zrozumienie danych**: Przeglądaj dostępne dane, identyfikuj problemy z jakością.
3. **Przygotowanie danych**: Oczyść, przekształć i podziel dane.
4. **Modelowanie**: Trenuj modele, dostrajaj hiperparametry.
5. **Ocena**: Oceń wydajność na podstawie wskaźników.
6. **Wdrożenie**: Udostępnij model w środowisku produkcyjnym.
7. **Monitorowanie**: Dryft toru, wydajność i anomalie.

Jest to pętla iteracyjna — powrócisz do wcześniejszych kroków w oparciu o wyniki oceny.

---

## Dzielenie danych

### Trenuj / Walidacja / Podział testów
- **Zestaw treningowy** (~70%): Używany do dopasowania parametrów modelu.
- **Zestaw walidacyjny** (~15%): używany do dostrajania hiperparametrów i wybierania wariantów modelu.
- **Zbiór testowy** (~15%): Używany tylko raz na samym końcu w celu oszacowania wydajności generalizacji.

**Ważne:** Zestaw testowy musi pozostać w nienaruszonym stanie aż do końcowej oceny, aby uniknąć wycieku danych.

### Walidacja krzyżowa (k-krotna)
W przypadku małych zbiorów danych użyj k-krotnej walidacji krzyżowej: podziel dane na k części, trenuj na k-1, zweryfikuj pozostałe i powtórz k razy. Średnia wydajność. k=5 lub k=10 jest powszechne.

### Podział warstwowy
W przypadku klasyfikacji z niezrównoważonymi klasami należy zastosować podziały warstwowe, aby zachować proporcje klas w każdym podzbiorze.

### Podział na podstawie czasu
W przypadku danych szeregów czasowych dziel je chronologicznie (trenuj na przeszłości, testuj na przyszłości), a nie losowo.

---

## Metryki oceny

### Metryki klasyfikacji

| Metryczne | Co mierzy | Najlepiej stosować do |
|--------|----------------------|--------------|
| **Dokładność** | (TP + TN) / (TP + TN + FP + FN) | Zbilansowane zbiory danych |
| **Precyzja** | TP / (TP + FP) | Kiedy fałszywe alarmy są kosztowne (np. wykrywanie spamu) |
| **Przypomnijmy** | TP / (TP + FN) | Kiedy wyniki fałszywie negatywne są kosztowne (np. badania przesiewowe w kierunku raka) |
| **Wynik F1** | Harmoniczna średnia precyzji i zapamiętywania | Niezrównoważone zbiory danych, metryka jednoliczbowa |
| **AUC-ROC** | Pole pod krzywą ROC; kompromis pomiędzy TPR i FPR | Ogólna wydajność klasyfikatora niezależna od progu |
| **AUC-PR** | Obszar pod krzywą Precyzji-Przypomnienia | Wysoce niezrównoważone zbiory danych |

**Definicje:**
- TP = prawdziwie pozytywny
- TN = prawdziwie ujemny
- FP = fałszywie dodatni (błąd typu I)
- FN = fałszywie ujemny (błąd typu II)

### Metryki regresji

| Metryczne | Co mierzy | Wrażliwość na wartości odstające |
|------------|--------------------------------|--------------------------------------|
| **MSE** (średni błąd kwadratowy) | Średnia kwadratowa różnica | Wysoki |
| **RMSE** (średnia kwadratowa błędu) | Pierwiastek kwadratowy z MSE (te same jednostki co wartość docelowa) | Wysoki |
| **MAE** (średni błąd bezwzględny) | Średnia różnica bezwzględna | Niski |
| **R²** (Współczynnik determinacji) | Proporcja wariancji wyjaśniona | Brak bezpośrednio, ale pośrednio wrażliwy na wartości odstające |

### Wskaźniki rankingu i wyszukiwania
- **Precision@k**: Część odpowiednich pozycji wśród rekomendacji z najwyższej półki.
- **Recall@k**: Ułamek wszystkich odpowiednich elementów, które pojawiają się na górze-k.
- **NDCG** (Znormalizowany zdyskontowany skumulowany zysk): Uwzględnia znaczenie pozycji.
- **Współczynnik trafień**: Określa, czy odpowiedni element pojawia się w górnym rogu.

### Metryki generatywne/LLM
- **Zaskoczenie**: Jak „zaskoczony” jest model przez wyciągnięty tekst (im niższy, tym lepszy).
- **BLEU**: n-gramowe nakładanie się na tłumaczenia referencyjne (koncentrujące się na precyzji).
- **ROUGE**: Nakładanie się zorientowane na przypomnienie w celu podsumowania.
- **BERTScore**: Podobieństwo semantyczne przy użyciu osadzania kontekstowego (bardziej niezawodne niż BLEU).
- **METEOR**: Wyrównuje synonimy i tematy w WordNet.

---

## Pułapki w ocenie

### Wyciek danych
Występuje, gdy informacje ze zbioru testowego w sposób niezamierzony wpływają na trening.
- **Zapobiegaj:** Nigdy nie używaj danych testowych do inżynierii funkcji, normalizacji lub dostrajania hiperparametrów.
- **Wykryj:** jeśli Twój model uzyska podejrzanie wysoki wynik, podejrzewaj wyciek.

### Nadmierne dopasowanie
Model działa dobrze na danych szkoleniowych, ale słabo na walidacji/testach.
- **Łagodzenie:** korzystaj z regularyzacji, wczesnego zatrzymywania, upraszczaj architekturę lub zbieraj więcej danych.

### Niedopasowanie
Model słabo radzi sobie zarówno ze szkoleniem, jak i walidacją.
- **Łagodzenie:** użyj bardziej złożonego modelu, dodaj funkcje lub ogranicz regularyzację.

### Niezrównoważone dane
- **Łagodzenie:** Użyj wag klas, nadpróbki (SMOTE), podpróbki lub użyj odpowiednich metryk (F1, AUC-PR) zamiast dokładności.

### Dryf czasowy (dryf koncepcji)
Zależność między cechami a celem zmienia się w czasie.
- **Łagodzenie:** Okresowo powtarzaj szkolenie, monitoruj wydajność, używaj algorytmów wykrywania dryfu.

---

## Strojenie hiperparametrów- **Wyszukiwanie siatki**: Wyczerpujące wypróbowanie wszystkich kombinacji predefiniowanego zestawu hiperparametrów. Proste, ale kosztowne obliczeniowo.
- **Wyszukiwanie losowe**: Przykładowe losowe kombinacje z dystrybucji. Bardziej wydajne niż przeszukiwanie siatki w przypadku przestrzeni wielowymiarowych.
- **Optymalizacja Bayesa**: Buduje probabilistyczny model funkcji celu i inteligentnie wybiera hiperparametry. Biblioteki: Optuna, Hyperopt, scikit-optimise.
- **Automatyczne strojenie**: Użyj narzędzi takich jak Optuna, Ray Tune lub Weights & Biases Sweeps do rozproszonego strojenia.

**Sugerowane zakresy wyszukiwania typowych hiperparametrów:**

| Parametr | Sugerowany zakres (skala logarytmiczna) |
|----------|----------------------------|
| Szybkość uczenia się | 1e-5 do 1e-1 |
| Wielkość partii | 16, 32, 64, 128, 256 |
| Liczba warstw (NN) | 2 do 6 |
| Liczba neuronów (NN) | 32 do 1024 |
| Regularyzacja (L2) | 1e-6 do 1e-2 |
| Głębokość drzewa (XGBoost) | 3 do 12 |

---

## Wybór i weryfikacja modelu

1. **Model bazowy**: Rozpocznij od prostego modelu heurystycznego lub prostego (np. regresji logistycznej, predyktora średniej), aby ustalić dolną granicę.
2. **Modele kandydujące**: Trenuj wiele rodzin modeli (np. Random Forest, XGBoost, Neural Network).
3. **Weryfikacja krzyżowa** każdego kandydata w zestawie walidacyjnym.
4. **Porównaj dane** (z przedziałami ufności) i wybierz najlepszego kandydata.
5. **Ocena końcowa** na wystawionym zestawie testowym.
6. **Analiza błędów**: Przyjrzyj się przykładom, w których model się myli. Identyfikuj wzorce (np. rzadkie klasy, niejednoznaczne dane wejściowe) i przekazuj spostrzeżenia z powrotem do przygotowywania danych lub inżynierii funkcji.

---

## Wdrażanie i monitorowanie

### Wzory serwowania
- **Wnioskowanie zbiorcze**: przetwarzaj duże ilości danych w trybie offline (np. rekomendacje nocne).
- **Wnioskowanie online**: prognozy w czasie rzeczywistym za pośrednictwem interfejsu API (np. ocena zdolności kredytowej, wykrywanie oszustw).
- **Wnioskowanie o transmisji strumieniowej**: sterowane zdarzeniami, w czasie rzeczywistym i z niskim opóźnieniem (np. alerty czujnika IoT).

### Monitorowanie modelu
- **Monitorowanie wydajności**: Dokładność śledzenia/F1 w czasie na podstawie danych na żywo (jeśli dostępna jest podstawowa informacja).
- **Dryft danych**: Monitoruj zmiany w rozkładach cech wejściowych (np. za pomocą PSI – wskaźnika stabilności populacji).
- **Dryf koncepcji**: Monitoruj zmiany w relacjach między wejściami i wynikami.
- **Dryf przewidywania**: Śledź rozkład przewidywanych wyników.
- **Opóźnienie i przepustowość**: Upewnij się, że spełnione są umowy SLA (umowy dotyczące poziomu usług).

### Rejestrowanie i alarmowanie
- Rejestruj wszystkie żądania i odpowiedzi dotyczące prognoz (z anonimizacją).
- Ustaw alerty dla:
  - Znaczący spadek wydajności.
  - Wysoki procent brakujących lub nieprawidłowych danych wejściowych.
  - Dane wyjściowe modelu wykraczają poza oczekiwane granice.

### Wersjonowanie modelu i rejestracja
- Używaj rejestru modeli (np. MLflow, Weights & Biases, Sagemaker Model Registry) do przechowywania i wersjonowania modeli, metadanych i wyników oceny.
- Przechowuj kod szkoleniowy i wersję danych (przez DVC lub Git LFS) obok modelu.

---

## Praktyczna lista kontrolna przepływu pracy

- [ ] Problem sformułowany i zdefiniowany miernik sukcesu.
- [ ] Przeprowadzono eksplorację danych (brakujące wartości, wartości odstające, rozkład).
- [ ] Utworzono podział pociągu/walidacji/testu (w razie potrzeby stratyfikowany).
- [ ] Ustalono model bazowy.
- [ ] Modele kandydatów przeszkolone i zweryfikowane.
- [ ] Dostrojono hiperparametry.
- [ ] Najlepszy model wybrany w drodze walidacji krzyżowej.
- [ ] Ocena końcowa zestawu testowego.
- [ ] Przeprowadzono analizę błędów.
- [ ] Gotowy plan wdrożenia (infrastruktura obsługująca).
- [ ] Konfiguracja panelu monitorowania.
- [ ] Dokumentacja (karta danych, karta modelu) skompletowana.