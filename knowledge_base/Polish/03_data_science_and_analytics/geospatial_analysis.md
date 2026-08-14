---
# Metadata
title: "Geospatial Analysis"
description: "Coordinate systems, spatial operations, GeoPandas, raster analysis"
category: "Data Science and Analytics"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [geospatial, analysis, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Analiza geoprzestrzenna
Analiza geoprzestrzenna to proces badania danych zawierających element geograficzny — współrzędne, adresy, granice lub dowolne dane powiązane z lokalizacją na Ziemi. Odpowiada na pytania takie jak „gdzie są nasi klienci?”, „jaka jest optymalna trasa?” i „jak zmienia się użytkowanie gruntów w czasie?”. Każdy zbiór danych ma wymiar przestrzenny, a jego zrozumienie pozwala uzyskać wiedzę, której brakuje czystej analizie statystycznej.
---

## Podstawowe pojęcia
### Układy współrzędnych
| Systemu | Opis | Przypadek użycia |
|------------|------------|---------|
| **WGS 84 (EPSG:4326)** | Globalny standard; szerokość/długość geograficzna w stopniach | GPS; większość map internetowych; GeoJSON |
| **Web Mercator (EPSG:3857)** | Rzutuje kulę ziemską na cylinder; zniekształca obszar na biegunach | Mapy Google; Mapbox; większość usług kafelkowych |
| **UTM** (Uniwersalny Merkator Poprzeczny) | Dzieli Ziemię na 60 stref; oparte na metrach | Wojskowy; geodezja; precyzyjna praca lokalna |
| **Brytyjska sieć krajowa (EPSG:27700)** | punkt odniesienia OSGB36; oparte na metrach | Mapa Wielkiej Brytanii |
| **Prognozy lokalne** | Projekcje niestandardowe dla konkretnych regionów | Minimalizuj zniekształcenia dla określonego obszaru |
### Typy geometrii
| Wpisz | Opis | Przykład |
|------|------------|--------|
| **Punkt** | Pojedyncza współrzędna | restauracja; czujnik; klient |
| **Ciąg Linii** | Uporządkowany ciąg punktów | Droga; rzeka; trasa |
| **Wielokąt** | Zamknięty kształt z wnętrzem | kraj; jezioro; strefa dostaw |
| **Wielopunktowe** | Zbiórka punktów | Wszystkie przystanki autobusowe w mieście |
| **Ciąg wieloliniowy** | Zbiór linii | Wszystkie drogi w sieci |
| **Wielokąt** | Zbiór wielokątów | Archipelag; kraj z wyspami |
| **Kolekcja geometrii** | Typy mieszane | Kraj ze swoimi miastami, drogami i rzekami |
---

##Formaty danych
| Formatuj | Wpisz | Kluczowa funkcja |
|------------|------|------------|
| **GeoJSON** | Tekst (JSON) | Czytelny dla człowieka; przyjazne dla sieci; obsługuje wszystkie typy geometrii |
| **Plik kształtu** | Binarny (wiele plików) | Starszy format firmy ESRI; .shp + .shx + .dbf + .prj |
| **KML** | XML | Google Earth; obsługuje 3D i czas |
| **Geopakiet** | Oparte na SQLite | Pojedynczy plik; obsługuje raster i wektor; nowoczesny standard |
| **GeoParkiet** | Kolumnowy (parkiet) | Wydajny w przypadku dużych zbiorów danych; integruje się z narzędziami inżynierii danych |
| **WKT/WKB** | Tekst / Binarny | Dobrze znany tekst; Dobrze znany plik binarny; używany do przechowywania baz danych |
| **MVT** | Binarny | Płytki wektorowe Mapbox; do udostępniania danych map klientom internetowym |
---

## Operacje przestrzenne
### Podstawowe operacje
| Operacja | Opis | Przykład |
|---------------|------------|--------|
| **Odległość** | Oblicz odległość między geometriami | „Znajdź wszystkie szpitale w promieniu 10 km” |
| **Bufor** | Utwórz wielokąt wokół geometrii w zadanej odległości | "Pokaż strefę 500m wokół szkoły" |
| **Skrzyżowanie** | Znajdź obszar nakładania się geometrii | „Jakie działki znajdują się w strefie zalewowej?” |
| **Unia** | Połącz geometrie w jedną | „Połącz wszystkie działki w jeden region” |
| **Różnica** | Odejmij jedną geometrię od drugiej | „Powierzchnia zabudowana z wyłączeniem stref chronionych” |
| **Zawiera / Wewnątrz** | Sprawdź, czy jedna geometria znajduje się wewnątrz drugiej | „Którzy klienci znajdują się w tym obszarze dostawy?” |
| **Najbliższy sąsiad** | Znajdź najbliższą geometrię | „Jaka jest najbliższa remiza strażacka?” |
| **Połączenie przestrzenne** | Połącz atrybuty w oparciu o relację przestrzenną | „Przypisz każdy punkt do zawierającego go obszaru spisowego” |
### Indeksowanie przestrzenne
| Typ indeksu | Opis | Przypadek użycia |
|----------|------------|---------|
| **Drzewo R** | Hierarchia obwiedni; najczęściej | PocztaGIS; SQLite; ogólnego przeznaczenia |
| **Czwodrzewo** | Podział rekurencyjny na ćwiartki | Dane punktowe; silniki gier |
| **Geohash** | Siatka hierarchiczna; koduje do ciągu | Wyszukiwanie bliskości; fragmentowanie bazy danych |
| **H3** (Ubera) | Sześciokątna siatka hierarchiczna | Analityka; wspólne przejazdy; jednolite kosze |
| **S2** (Google) | Hierarchia komórkowa na kuli | Indeksowanie przestrzenne na dużą skalę |
---

## Narzędzia i biblioteki
| Narzędzie / Biblioteka | Język | Opis |
|--------------|----------|------------|
| **PostGIS** | SQL (PostgreSQL) | Złoty standard dla baz danych przestrzennych; pełny przestrzenny SQL |
| **QGIS** | Pulpit (Python/C++) | Bezpłatny system GIS o otwartym kodzie źródłowym; Ekosystem wtyczek |
| **GeoPanda** | Pythona | Pandy + Zgrabna + Fiona; przestrzenne ramki danych |
| **Zgrabnie** | Pythona | Operacje na geometrii; w oparciu o GEOS |
| **Foli** | Pythona | Interaktywne mapy ulotek z Pythona |
| **Turf.js** | JavaScript | Analiza geoprzestrzenna po stronie klienta |
| **Deck.gl** | JavaScript | Wielkoskalowa wizualizacja danych na mapach |
| **GDAL** | C++ (z powiązaniami Pythona) | Tłumaczenie danych rastrowych i wektorowych; szwajcarski scyzoryk |
| **Raster** | Pythona | Odczyt/zapis danych rastrowych; na podstawie GDAL |
| **Kepler.gl** | JavaScript | Wizualizacja geoprzestrzenna oparta na WebGL |
---

## Wzorce analizy geoprzestrzennej
### Typowe typy analiz
| Wzór | Opis | Przypadek użycia |
|-------------|------------|---------|
| **Analiza układu punktów** | Zbadaj rozkład punktów | Mapowanie przestępczości; wykrywanie ognisk choroby |
| **Analiza hotspotów** | Znajdź statystycznie istotne skupienia | Lokalizacja detaliczna; przestępczość; epidemiologia |
| **Analiza sieci** | Optymalizacja tras; obszary usług | Logistyka; reagowanie w sytuacjach awaryjnych; narzędzia |
| **Interpolacja przestrzenna** | Oszacuj wartości w niepróbkowanych lokalizacjach | Jakość powietrza; właściwości gleby; pogoda |
| **Wykrywanie zmian w użytkowaniu gruntów** | Porównaj zdjęcia satelitarne w czasie | rozrost miast; wylesianie; rolnictwo |
| **Analiza przydatności** | Znajdź lokalizacje spełniające wiele kryteriów | Wybór miejsca; planowanie konserwatorskie |
| **Autokorelacja przestrzenna** | Zmierz, jak powiązane są pobliskie wartości | Ceny nieruchomości; rozprzestrzenianie się choroby |
### Problem modyfikowalnych jednostek powierzchni (MAUP)
| Aspekt | Problem |
|------------|--------|
| **Efekt skali** | Wyniki zmieniają się w zależności od wielkości jednostek analizy (obwody spisowe vs powiaty vs stany) |
| **Efekt strefowy** | Wyniki zmieniają się w zależności od sposobu narysowania granic, nawet w tej samej skali |
| **Implikacja** | Nigdy nie zakładaj, że wyniki na jednym poziomie agregacji mają zastosowanie na innym; zawsze testuj wrażliwość na granice |
---

## Rozważania praktyczne
| Obawa | Wskazówki |
|--------|----------|
| **Systemy odniesienia za pomocą współrzędnych** | Zawsze sprawdzaj CRS; nigdy nie mieszaj prognoz w obliczeniach; transformacja przed obliczeniem odległości |
| **Precyzja** | Precyzja zmiennoprzecinkowa ma znaczenie w małych skalach; użyj odpowiednich typów danych |
| **Wydajność** | Operacje przestrzenne są drogie; stosować indeksy przestrzenne; uprościć geometrię do wyświetlania |
| **Topologia** | Przed analizą upewnij się, że geometrie są prawidłowe (brak samoprzecięć, zamkniętych wielokątów).
| **Skala** | Web Mercator zniekształca obszar; nie używaj go do obliczeń powierzchni |
| **Jakość danych** | Sprawdź geometrię zerową, zduplikowane wierzchołki, wielokąty rozszczepione |
---

## Streszczenie
Analiza geoprzestrzenna przekształca dane o lokalizacji w przydatne informacje. Punkty, linie i wielokąty reprezentują elementy świata rzeczywistego. Operacje przestrzenne — odległość, bufor, przecięcie, połączenie — odpowiadają na pytania dotyczące bliskości, nakładania się i ograniczania. Dostępne narzędzia obejmują PostGIS do analizy w skali bazy danych, GeoPandas do przepływów pracy w języku Python, aż po Deck.gl do wizualizacji internetowej. Kluczowe wyzwania to wybór odpowiedniego układu współrzędnych, zarządzanie wydajnością w przypadku dużych zbiorów danych i świadomość MAUP — faktu, że wybór granic agregacji wpływa na wyniki. Niezależnie od tego, czy optymalizujesz trasy dostaw, analizujesz rozprzestrzenianie się chorób, czy mapujesz rozwój miast, analiza geoprzestrzenna zapewnia kontekst przestrzenny, którego nie da się uchwycić samymi liczbami.