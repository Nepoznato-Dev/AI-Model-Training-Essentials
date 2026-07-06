# Matematyka i Logika

## Czym jest Matematyka?

Matematyka to badanie liczb, kształtów, wzorców i logicznych relacji. Jest zarówno nauką, jak i językiem używanym do opisywania wszechświata. Matematyka dzieli się na gałęzie obejmujące arytmetykę, algebrę, geometrię, rachunek różniczkowy i całkowy, statystykę i logikę. Matematyka jest fundamentem fizyki, inżynierii, informatyki, ekonomii i wielu innych dziedzin.

## Arytmetyka

Arytmetyka to gałąź matematyki zajmująca się podstawowymi działaniami na liczbach. Cztery podstawowe działania to dodawanie (+), odejmowanie (−), mnożenie (×) i dzielenie (÷). Kolejność działań określa sekwencję, w której obliczenia muszą być wykonane: Nawiasy, Wykładniki, Mnożenie i Dzielenie (od lewej do prawej), Dodawanie i Odejmowanie (od lewej do prawej). Często zapamiętywane jako **PEMDAS** lub **BODMAS**. Liczba pierwsza to liczba całkowita większa od 1, która nie ma dzielników oprócz 1 i samej siebie. Pierwsze liczby pierwsze to 2, 3, 5, 7, 11, 13, 17, 19, 23 i 29.

**Przykłady:**
- Rozkład na czynniki pierwsze: 84 = 2² × 3 × 7
- Największy wspólny dzielnik (NWD) 24 i 36: 12
- Najmniejsza wspólna wielokrotność (NWW) 4 i 6: 12

## Algebra

Algebra używa liter i symboli do reprezentowania liczb i wielkości w równaniach i formułach. **Zmienna** to symbol (zwykle litera) reprezentujący nieznaną lub zmieniającą się wielkość. **Równanie** stwierdza, że dwa wyrażenia są równe. Rozwiązanie równania oznacza znalezienie wartości zmiennej/zmiennych, które sprawiają, że równanie jest prawdziwe.

**Wzór kwadratowy** rozwiązuje równania postaci ax² + bx + c = 0: x = (−b ± √(b²−4ac)) / (2a)

**Funkcja** mapuje każde wejście do dokładnie jednego wyjścia. Typowe funkcje obejmują:
- Liniowa: y = mx + b (prosta linia, stała szybkość zmiany)
- Kwadratowa: y = ax² + bx + c (parabola, zakrzywiona)
- Wykładnicza: y = a × bˣ (wzrost lub zanik, szybka zmiana)
- Logarytmiczna: y = log_b(x) (odwrotność wykładniczej)

**Kluczowe koncepcje:**
- Dziedzina: zbiór wszystkich możliwych wartości wejściowych
- Przeciwdziedzina: zbiór wszystkich możliwych wartości wyjściowych
- Nachylenie: szybkość zmiany (m w y = mx + b)
- Przechwycenie: gdzie funkcja przecina oś y (b w y = mx + b)

## Geometria

Geometria to gałąź matematyki badająca kształty, rozmiary, pozycje i właściwości figur. Punkt nie ma rozmiaru; reprezentuje lokalizację. Linia rozciąga się nieskończenie w obu kierunkach. Odcinek ma dwa punkty końcowe. Kąt jest utworzony przez dwie półproste współdzielące punkt końcowy.

**Kluczowe zasady:**
- Suma kątów w trójkącie zawsze wynosi 180 stopni.
- Suma kątów w czworokącie zawsze wynosi 360 stopni.
- Twierdzenie Pitagorasa: w trójkącie prostokątnym, a² + b² = c² (gdzie c to przeciwprostokątna).
- Obwód koła: 2πr
- Pole koła: πr²
- Objętość kuli: (4/3)πr³

**π (pi)** to około 3.14159 i jest stosunkiem obwodu koła do jego średnicy.

**Typowe kształty geometryczne:**
- Trójkąt: 3 boki, suma kątów 180°
- Kwadrat: 4 równe boki, 4 kąty proste
- Prostokąt: 4 boki, przeciwległe boki równe, 4 kąty proste
- Koło: brak boków, ciągła zakrzywiona granica
- Pięciokąt: 5 boków, suma kątów 540°
- Sześciokąt: 6 boków, suma kątów 720°

## Statystyka i Prawdopodobieństwo

Statystyka to nauka zbierania, analizowania, interpretowania i prezentowania danych.

**Miary tendencji centralnej:**
- **Średnia** (średnia arytmetyczna): suma wszystkich wartości podzielona przez liczbę wartości
- **Mediana**: środkowa wartość po posortowaniu danych (mniej wrażliwa na outliers)
- **Dominanta**: najczęściej występująca wartość (może mieć wiele dominant)

**Miary rozproszenia:**
- **Zakres**: maksimum - minimum
- **Wariancja**: średnia kwadratów odchyleń od średniej
- **Odchylenie standardowe**: pierwiastek kwadratowy wariancji (w tych samych jednostkach co dane)

Prawdopodobieństwo mierzy szansę wystąpienia zdarzenia, od 0 (niemożliwe) do 1 (pewne). Prawdopodobieństwo wystąpienia dwóch niezależnych zdarzeń to iloczyn ich indywidualnych prawdopodobieństw.

**Przykład:** Prawdopodobieństwo wyrzucenia 6 na uczciwej kostce: 1/6. Prawdopodobieństwo wyrzucenia dwóch 6 z rzędu: (1/6) × (1/6) = 1/36.

## Prawdopodobieństwo dla Informatyki i ML

**Zmienna losowa** to zmienna, której wartość zależy od wyniku procesu losowego. **Rozkład prawdopodobieństwa** opisuje, jak prawdopodobny jest każdy wynik.

**Typowe rozkłady:**
- **Bernoulliego**: pojedyncza próba z dwoma wynikami (np. rzut monetą)
- **Dwumianowy**: liczba sukcesów w n niezależnych próbach Bernoulliego
- **Normalny (Gaussa)**: krzywa dzwonowa, symetryczna wokół średniej (częsty w zjawiskach naturalnych)
- **Poissona**: liczba zdarzeń w ustalonym przedziale (np. emaile na godzinę)

**Wartość oczekiwana** to długoterminowa średnia wyników zmiennej losowej. **Wariancja** mierzy rozproszenie wokół tego oczekiwania.

**Prawdopodobieństwo warunkowe** opisuje prawdopodobieństwo zdarzenia pod warunkiem, że inne zdarzenie wystąpiło: P(A|B) = P(A ∩ B) / P(B) [jeśli P(B) > 0].

**Twierdzenie Bayesa** aktualizuje przekonania używając dowodów: P(A|B) = P(B|A) × P(A) / P(B).

W uczeniu maszynowym, prawdopodobieństwo stanowi podstawę pewności klasyfikacji, estymacji niepewności, metod bayesowskich i wielu funkcji straty (takich jak cross-entropy).

## Rachunek Różniczkowy i Całkowy

Rachunek różniczkowy i całkowy to gałąź matematyki badająca ciągłą zmianę.

**Rachunek różniczkowy** zajmuje się szybkościami zmian i nachyleniami krzywych, używając **pochodnych**. Pochodna funkcji f(x) reprezentuje szybkość zmiany f względem x w punkcie. Notacja: f'(x) lub df/dx.

**Typowe pochodne:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

**Rachunek całkowy** zajmuje się akumulacją wielkości i polami pod krzywymi, używając **całek**. Całka reprezentuje pole pod krzywą między dwoma punktami.

**Twierdzenie podstawowe rachunku** łączy różniczkowanie i całkowanie: różniczkowanie i całkowanie to operacje odwrotne.

Rachunek został rozwinięty niezależnie przez Isaaca Newtona i Gottfrieda Wilhelma Leibniza w XVII wieku.

## Systemy Liczbowe

- **Liczby naturalne**: 1, 2, 3, 4, ... (liczby do liczenia)
- **Liczby całkowite nieujemne**: 0, 1, 2, 3, ... (liczby naturalne plus zero)
- **Liczby całkowite**: ..., −2, −1, 0, 1, 2, ... (wszystkie liczby całkowite nieujemne i ich negatywy)
- **Liczby wymierne**: liczby wyrażalne jako p/q gdzie p i q to liczby całkowite i q ≠ 0 (np. 1/2, 3/4, −5/3)
- **Liczby niewymierne**: nie mogą być wyrażone jako ułamek (np. √2, π, e)
- **Liczby rzeczywiste**: wszystkie liczby wymierne i niewymierne (oś liczbowa)
- **Liczby urojone**: obejmują pierwiastek kwadratowy z liczb ujemnych; i = √(−1)
- **Liczby zespolone**: łączą części rzeczywiste i urojone (a + bi)

## Logika i Rozumowanie

Logika to badanie poprawnego rozumowania.

**Rozumowanie dedukcyjne** wyciąga szczegółowe wnioski z ogólnych przesłanek. Jeśli przesłanki są prawdziwe i argument jest poprawny, wniosek musi być prawdziwy.
- **Przykład:** Wszyscy ludzie są śmiertelni. Sokrates jest człowiekiem. Zatem Sokrates jest śmiertelny.

**Rozumowanie indukcyjne** wyciąga ogólne wnioski ze szczegółowych obserwacji. Nie gwarantuje, że wniosek jest prawdziwy, ale czyni go prawdopodobnym.
- **Przykład:** Każdy łabędź, którego widziałem, jest biały. Zatem wszystkie łabędzie są białe. (Uwaga: to fałsz; czarne łabędzie istnieją!)

**Typowe błędy logiczne (błędy w rozumowaniu):**
- **Ad hominem**: atakowanie osoby zamiast argumentu
- **Straw man**: przeinaczanie argumentu, aby ułatwić atak
- **Fałszywy dylemat**: przedstawianie tylko dwóch opcji, gdy istnieje więcej
- **Błędne koło**: używanie wniosku jako przesłanki
- **Odwołanie do autorytetu**: twierdzenie, że coś jest prawdziwe, bo autorytet tak mówi
- **Post hoc**: zakładanie, że ponieważ A wydarzyło się przed B, A spowodowało B

## Zbiory

**Zbiór** to kolekcja odrębnych obiektów.
- **Suma** (A ∪ B): wszystkie elementy z obu zbiorów
- **Iloczyn** (A ∩ B): tylko elementy wspólne dla obu
- **Zbiór pusty** (∅ lub {}): nie zawiera żadnych elementów
- **Podzbiór** (A ⊆ B): wszystkie elementy A są również w B
- **Diagramy Venna**: wizualnie reprezentują relacje między zbiorami

Teoria zbiorów jest fundamentem nowoczesnej matematyki i logiki.

## System Binarny i Podstawy Liczb

Komputery reprezentują dane w **systemie binarnym** (podstawa 2), używając tylko cyfr 0 i 1. Każda cyfra binarna to **bit**. Osiem bitów tworzy jeden **bajt**.

**Dziesiętny** to system liczbowy podstawy 10, którego ludzie typowo używają.

**Szesnastkowy** to podstawa 16, używająca cyfr 0–9 i liter A–F, często używana w informatyce do kompaktowej reprezentacji danych binarnych.

**Konwersje:**
- Binarnie 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (dziesiętnie)
- Szesnastkowo A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (dziesiętnie)

Konwertowanie między podstawami liczb to fundamentalna koncepcja w informatyce.

## Algebra Liniowa dla Deweloperów i ML

Algebra liniowa bada wektory, macierze i transformacje liniowe.

**Wektor** to uporządkowana lista liczb (np. cechy w próbce ML).
- Przykład: [23, 1.8, 175] reprezentuje wiek, wzrost i wagę osoby

**Macierz** to 2D tablica liczb (np. wagi modelu lub batche datasetu).
- Przykład: [[1, 2], [3, 4]] to macierz 2×2

**Mnożenie macierzy** łączy transformacje liniowe i jest podstawową operacją w grafice, symulacji i sieciach neuronowych.

**Iloczyn skalarny** mierzy podobieństwo i projekcję między wektorami:
- a·b = Σ(a_i × b_i)
- **Podobieństwo kosinusowe** = (a·b) / (||a|| × ||b||)
- Podobieństwo kosinusowe waha się od -1 (przeciwne) do 1 (ten sam kierunek)

**Wartości własne i wektory własne** opisują kierunki, które są skalowane (nie obracane) przez macierz i są używane w metodach takich jak PCA (Analiza Głównych Składowych).

**Rząd** wskazuje, ile niezależnych informacji zawiera macierz. Aproksymacje niskorzędowe są przydatne do kompresji i redukcji wymiarowości.

Większość nowoczesnych obciążeń pracy ML mocno polega na zoptymalizowanych bibliotekach algebry liniowej i akceleracji sprzętowej.
