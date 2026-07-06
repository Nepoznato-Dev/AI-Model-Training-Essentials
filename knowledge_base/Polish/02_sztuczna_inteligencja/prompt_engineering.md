# Szybka inżynieria

Szybka inżynieria to praktyka projektowania, udoskonalania i optymalizowania podpowiedzi wejściowych w celu uzyskania najlepszego możliwego wyniku z modelu językowego. Jest to zarówno sztuka, jak i nauka oraz podstawowy interfejs umożliwiający kontrolowanie zachowań LLM bez dostrajania.

---

## Podstawowe zasady

### Przejrzystość i specyfika
Jasny monit nie pozostawia miejsca na dwuznaczności. Określ dokładnie, czego chcesz, w tym format, długość i perspektywę.

**Niejasne:**
> „Opowiedz mi o Pythonie”.

**Specyficzne:**
> „Wyjaśnij globalną blokadę interpretera (GIL) języka Python. Opisz jej wpływ na wielowątkowość, podaj jedno obejście i nie pisz w odpowiedzi mniej niż 200 słów”.

### Podaj kontekst
Modele osiągają lepsze wyniki, gdy znają rolę, odbiorców i cel.

**Bez kontekstu:**
> „Napisz funkcję sortującą listę.”

**W kontekście:**
> "Jesteś starszym programistą Pythona. Napisz funkcję sortującą listę słowników według podanego klucza. Korzystaj ze wskazówek dotyczących typów i obsługuj przypadki Edge. Odbiorcami są młodsi programiści."

### Używaj pozytywnych instrukcji
Powiedz modelowi, co ma robić, a nie czego unikać. „Nie używaj żargonu” jest słabsze niż „Używaj prostego języka dostępnego dla 10-latka”.

---

## Struktury podpowiedzi

### Role systemowe/użytkownika/asystenta
Większość interfejsów API LLM obsługuje strukturę wieloobrotową:

- **Komunikat systemowy**: Ustawia zachowanie, osobowość i ograniczenia modelu (utrzymuje się przez całą sesję).
- **Wiadomość użytkownika**: Bieżące zapytanie lub instrukcja.
- **Wiadomość Asystenta**: Poprzednie odpowiedzi modela (używane w celu zachowania ciągłości).

**Przykład (styl OpenAI API):**
System: Jesteś pomocnym asystentem kodowania. W odpowiedzi przesyłasz zwięzłe przykłady kodu i krótkie wyjaśnienia. Nigdy nie podawaj niebezpiecznego kodu.
Użytkownik: Napisz funkcję Pythona, aby pobrać plik z adresu URL.

### Monit o kilka strzałów
Podaj 2–3 przykłady pożądanego formatu wejścia-wyjścia, zanim poprosisz model o wykonanie zadania. To uczy wzoru.

**Przykład:**
Użytkownik: Zamień te zdania na stronę bierną:
Tekst: Kot gonił mysz.
Wynik: Kot gonił mysz.
Wejście: Szef kuchni ugotował posiłek.
Wynik: Posiłek został ugotowany przez szefa kuchni.
Wejście: Burza zniszczyła dom.
Dane wyjściowe: (model zostaje ukończony)

### Łańcuch myślowy (CoT)
Zachęć model, aby krok po kroku pokazał swoje rozumowanie. Poprawia to dokładność zadań arytmetycznych, logicznych i wieloetapowych.

**Bez CoT:**
> „Co to jest 24 × 37?”

**Z CoT:**
> "Oblicz 24 × 37. Pokaż krok po kroku swoje rozumowanie."

Model wygeneruje kroki pośrednie, redukując błędy arytmetyczne.

### Ustrukturyzowane wyniki
Poproś o konkretny format, taki jak JSON, YAML lub tabele przecen, aby analiza była niezawodna.
Użytkownik: Wymień trzy zalety i trzy wady mikrousług. Zwróć tylko prawidłowy obiekt JSON z kluczami „plusy” i „cons”, każdy będący tablicą ciągów znaków.

---

## Zaawansowane techniki

### Konsekwencja w sobie
Wygeneruj wiele odpowiedzi na ten sam monit (z temperaturą > 0) i weź udział w głosowaniu większością nad ostateczną odpowiedzią. Jest to szczególnie skuteczne w przypadku zadań związanych z rozumowaniem.

### Drzewo myśli
Przeglądaj wiele ścieżek rozumowania równolegle, oceń każdą i wybierz najlepszą. Jest to technika na poziomie badawczym, ale można ją przybliżyć, prosząc model o „badanie alternatywnych rozwiązań”.

### ReAct (rozumowanie + działanie)
Niech model przeplata rozumowanie z wywołaniami narzędzi. Może pomyśleć, potem działać (np. przeszukać sieć, uruchomić kod), a potem ponownie pomyśleć w oparciu o wynik.

**Prosta struktura:**
Masz dostęp do kalkulatora i wyszukiwarki. Dla każdego kroku wynik:
Myśl: (twoje rozumowanie)
Akcja: (nazwa narzędzia, dane wejściowe)
Obserwacja: (wyjście narzędzia)
...kontynuuj, aż uzyskasz ostateczną odpowiedź.

### Przypisanie osoby
Przypisz konkretną osobę, aby sformułować odpowiedź.

**Przykłady:**
- „Jesteś programistą jądra Linuksa i wyjaśniasz nowemu absolwentowi zarządzanie pamięcią.”
- "Jesteś sympatycznym dietetykiem udzielającym klientowi ogólnych porad."
- „Jesteś cynicznym krytykiem technologii recenzującym nowy gadżet”.

---

## Dostrajanie parametrów

- **Temperatura** (0,0 – 1,0+): Kontroluje losowość. Niższy = bardziej deterministyczny, wyższy = bardziej kreatywny. Użyj 0,0–0,3 w przypadku odpowiedzi opartych na faktach; 0,7–1,0 za kreatywne pisanie.
- **Top-p** (próbkowanie jądra): Odcina masę prawdopodobieństwa przy pewnym skumulowanym progu. 0,9 oznacza próbki modelu z górnych 90% prawdopodobnych tokenów. Zwykle dostosowuj temperaturę lub górne-p, a nie oba.
- **Maks. tokenów**: Ustawia maksymalną długość wyjściową. Pamiętaj, aby zarezerwować miejsce na odpowiedź w oknie kontekstowym.
- **Kara za częstotliwość**: Zmniejsza powtarzanie tych samych żetonów.
- **Kara za obecność**: Zachęca modelkę do wprowadzenia nowych tematów.

---

## Typowe pułapki i poprawki| Problem | Prawdopodobna przyczyna | Napraw |
|--------|-------------|-----|
| Model ignoruje części znaku zachęty | Podpowiedź jest zbyt długa lub przeciążona | Skracać; umieść najważniejszą instrukcję na końcu |
| Dane wyjściowe są zbyt szczegółowe | Brak ograniczenia długości | Dodaj „Ogranicz do 3 zdań” lub ustaw max_tokens |
| Dane wyjściowe są zbyt zwięzłe | Zbyt restrykcyjne | Dodaj „Wyjaśnij szczegółowo” lub niższą temperaturę |
| Faktyczne halucynacje | Niewystarczający kontekst lub niejednoznaczne pytanie | Dodaj „Jeśli nie jesteś pewien, powiedz „nie wiem”” i podaj kontekst RAG |
| Niespójne formatowanie | Brak wyraźnej instrukcji formatu | Poproś o JSON, tabelę przecen lub listę punktowaną |
| Modelowe odpowiedzi w złym języku | Brak instrukcji językowych | Wyraźnie zaznacz „Odpowiedz po angielsku” (lub w języku docelowym) |

---

## Szablony podpowiedzi dla typowych zadań

### Podsumowanie
Streść poniższy tekst w 3 punktach. Skoncentruj się na głównych argumentach i unikaj szczegółów.

Tekst: [wstaw tekst]


### Generowanie kodu
Napisz funkcję [język], która [wykonuje X].
Wymagania:

Skorzystaj ze wskazówek dotyczących typów.

Dołącz dokument.

Obsługuj przypadki Edge: [lista].

Nie używaj bibliotek zewnętrznych, chyba że określono inaczej.


### Wyjaśnienie
Wyjaśnij [koncepcję] [nie-ekspertowi / studentowi / dziecku]. W stosownych przypadkach użyj analogii.

### Burza mózgów
Wygeneruj 10 pomysłów na [temat]. Do każdego pomysłu podaj jednozdaniowy opis i jedno potencjalne wyzwanie.

tekst

### Klasyfikacja
Klasyfikuj następujące opinie klientów jako [pozytywne, neutralne, negatywne].
Podaj poziom pewności (0–100) i krótki powód.

Opinia: [wstaw tekst]

### Tłumaczenie ze stylem
Przetłumacz poniższy tekst z języka angielskiego na język hiszpański. Używaj nieformalnego tonu odpowiedniego dla postu w mediach społecznościowych.
Tekst: [wstaw tekst]

---

## Ocena podpowiedzi

Traktuj podpowiedzi jak kod: wprowadź je do wersji, przetestuj i wykonaj iterację.

- **Test A/B** różne warianty podpowiedzi na wybranym zestawie zapytań.
- **Mierz sukces** za pomocą oceny dokonywanej przez człowieka lub wskaźników automatycznych (np. dokładne dopasowanie, BLEU, punktacja niestandardowa).
- **Prowadź rejestr zapytań** (prosty plik tekstowy lub arkusz kalkulacyjny) zawierający monit, wersję i zaobserwowaną wydajność.

---