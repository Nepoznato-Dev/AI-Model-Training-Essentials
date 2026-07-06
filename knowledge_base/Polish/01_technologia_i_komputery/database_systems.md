# Systemy baz danych

## Podstawy baz danych

### Co to jest baza danych?
Baza danych to zorganizowany zbiór ustrukturyzowanych informacji przechowywanych elektronicznie, zaprojektowany w celu wydajnego wyszukiwania, wstawiania, aktualizowania i usuwania danych.

### Systemy zarządzania bazami danych (DBMS)
Oprogramowanie współpracujące z użytkownikami końcowymi, aplikacjami i samą bazą danych w celu przechwytywania i analizowania danych. Przykłady: MySQL, PostgreSQL, Oracle, MongoDB.

### Kluczowe pojęcia
- **Schemat**: Struktura/organizacja bazy danych (tabele, pola, relacje)
- **Instancja**: Rzeczywiste dane przechowywane w określonym momencie
- **Właściwości KWASU**: Atomowość, Konsystencja, Izolacja, Trwałość
- **Twierdzenie CAP**: spójność, dostępność, tolerancja podziału (wybierz 2)
- **Normalizacja**: Organizowanie danych w celu zmniejszenia redundancji
- **Denormalizacja**: Dodanie redundancji w celu poprawy wydajności odczytu

## Relacyjne bazy danych (SQL)

### Podstawowe pojęcia
- **Tabele**: Wiersze (rekordy) i kolumny (pola)
- **Klucz podstawowy**: Unikalny identyfikator każdego wiersza
- **Klucz obcy**: Odniesienie do klucza podstawowego w innej tabeli
- **Indeksy**: Struktury danych poprawiające szybkość zapytań
- **Widoki**: Wirtualne tabele oparte na wynikach zapytań
- **Procedury składowane**: Prekompilowane bloki kodu SQL
- **Wyzwalacze**: Automatyczne działania w przypadku zmian danych

### Operacje SQL (CRUD)
```sql
-- Create
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Read
SELECT * FROM users WHERE id = 1;
SELECT name, email FROM users ORDER BY name LIMIT 10;

-- Update
UPDATE users SET email = 'new@example.com' WHERE id = 1;

-- Delete
DELETE FROM users WHERE id = 1;
```

### Dołącza
- **INNER JOIN**: Zwraca pasujące wiersze z obu tabel
- **LEFT JOIN**: Wszystkie wiersze z lewej tabeli, dopasowania z prawej
- **RIGHT JOIN**: Wszystkie wiersze z prawej tabeli, dopasowania z lewej
- **FULL OUTER JOIN**: Wszystkie wiersze z obu tabel
- **ŁĄCZENIE KRZYŻOWE**: Iloczyn kartezjański obu tabel
- **SELF JOIN**: Tabela połączona ze sobą

### Formularze normalizacyjne
- **1NF**: Wartości atomowe, bez powtarzających się grup
- **2NF**: 1NF + brak częściowych zależności (wszystkie atrybuty niekluczowe zależą od całego klucza podstawowego)
- **3NF**: 2NF + brak zależności przechodnich (atrybuty niekluczowe nie zależą od innych atrybutów niekluczowych)
- **BCNF**: Silniejszy 3NF, każdy wyznacznik jest kluczem kandydującym
- **4NF**: Brak zależności wielowartościowych
- **5NF**: Brak zależności przyłączania

### Popularny RDBMS
- **PostgreSQL**: Zaawansowane funkcje, rozszerzalne, zgodne z ACID
- **MySQL**: Szeroko stosowane, szybkie odczyty, aplikacje internetowe
- **Oracle**: funkcje korporacyjne, skalowalność, drogie
- **SQL Server**: Ekosystem Microsoft, zintegrowane narzędzia
- **SQLite**: wbudowany, bezserwerowy, lekki
- **MariaDB**: fork MySQL, open source

## Bazy danych NoSQL

### Typy baz danych NoSQL

#### Magazyny dokumentów
- **Struktura**: dokumenty typu JSON (BSON)
- **Przypadki użycia**: Zarządzanie treścią, katalogi, profile użytkowników
- **Przykłady**: MongoDB, CouchDB, DocumentDB
- **Przykład zapytania** (MongoDB):
```javascript
db.users.find({ age: { $gt: 25 } }).sort({ name: 1 });
```

#### Magazyny klucz-wartość
- **Struktura**: Proste pary klucz-wartość
- **Przypadki użycia**: buforowanie, sesje, koszyki
- **Przykłady**: Redis, DynamoDB, Riak
- **Charakterystyka**: Szybkie, proste, ograniczone zapytania

#### Sklepy rodzinne kolumnowe
- **Struktura**: Kolumny pogrupowane w rodziny
- **Przypadki użycia**: Big Data, analityka, szeregi czasowe
- **Przykłady**: Cassandra, HBase, ScyllaDB
- **Charakterystyka**: Zoptymalizowany pod kątem zapisu, rozproszony, skalowalny

#### Bazy danych grafów
- **Struktura**: Węzły, krawędzie, właściwości
- **Przypadki użycia**: sieci społecznościowe, wykrywanie oszustw, rekomendacje
- **Przykłady**: Neo4j, Amazon Neptune, ArangoDB
- **Język zapytań**: Cypher (Neo4j), Gremlin

### Kiedy używać NoSQL
- Elastyczny/ewoluujący schemat
- Wymagania dotyczące skalowania poziomego
- Wysoka przepustowość zapisu
- Dane hierarchiczne/zagnieżdżone
- Systemy rozproszone
- Aplikacje w czasie rzeczywistym

## Projekt bazy danych

### Modelowanie relacji między podmiotami
- **Podmioty**: Obiekty/koncepcje (Klient, Produkt, Zamówienie)
- **Atrybuty**: Właściwości podmiotów (nazwa, cena, data)
- **Relacje**: Połączenia między jednostkami (jeden do jednego, jeden do wielu, wiele do wielu)
- **Liczność**: Liczba instancji w relacji

### Wzorce projektowe schematów
- **Dziedziczenie pojedynczej tabeli**: Wszystkie typy w jednej tabeli z dyskryminatorem typów
- **Dziedziczenie tabeli klas**: Oddzielne tabele dla klas podstawowych i podklas
- **Dziedziczenie tabeli betonowej**: Oddzielna tabela dla każdej klasy betonu
- **Tabele połączeń**: Rozwiązywanie relacji wiele do wielu
- **Tabele audytu**: Śledź zmiany (created_at, zaktualizowane_at, usunięte_at)

### Strategie indeksowania
- **B-Tree**: Domyślne, zapytania o zakres, sortowanie
- **Hash**: Wyszukiwanie dokładnych dopasowań
- **Mapa bitowa**: Kolumny o niskiej kardynalności (płeć, status)
- **Pełny tekst**: Możliwości wyszukiwania tekstu
- **Przestrzenne**: dane geograficzne (GIS)
- **Złożony**: połączenie wielu kolumn
- **Pokrycie**: Zawiera wszystkie kolumny potrzebne do zapytania

## Optymalizacja zapytań

### Plany wykonania
- Zrozumienie sposobu, w jaki baza danych wykonuje zapytania
- Identyfikacja wąskich gardeł (skanowanie pełnych tabel, brakujące indeksy)
- Narzędzia: WYJAŚNIJ, WYJAŚNIJ, ANALIZUJ### Techniki optymalizacji
- **Wykorzystanie indeksu**: Upewnij się, że zapytania korzystają z odpowiednich indeksów
- **Przepisywanie zapytań**: Uprość złożone zapytania
- **Optymalizacja łączenia**: Wybierz odpowiednie typy łączenia i kolejność
- **Partycjonowanie**: Dzielenie dużych tabel (zakres, skrót, lista)
- **Widoki zmaterializowane**: Wstępnie obliczone wyniki zapytań
- **Buforowanie zapytań**: Przechowywanie częstych wyników zapytań

### Typowe problemy z wydajnością
- **Problem z zapytaniem N+1**: Nieefektywne pobieranie powiązanych danych
- **Brakujące indeksy**: Skany pełnych tabel w przypadku dużych tabel
- **Nadmierne indeksowanie**: Wolny zapis z powodu zbyt wielu indeksów
- **Konkurencja o blokadę**: Transakcje oczekujące na blokady
- **Nieefektywne zapytania**: WYBIERZ *, niepotrzebne połączenia

## Transakcje i współbieżność

### Poziomy izolacji transakcji
- **READ UNCOMMITTED**: Najniższa izolacja, możliwe błędne odczyty
- **READ COMMITTED**: Widoczne są tylko zatwierdzone dane (domyślnie w większości baz danych)
- **POWTARZALNY CZYT**: To samo zapytanie zwraca te same wyniki w ramach transakcji
- **SERIALIZABLE**: Najwyższa izolacja, transakcje są wykonywane sekwencyjnie

### Kontrola współbieżności
- **Pesymistyczne blokowanie**: Blokuj zasoby przed dostępem
- **Blokowanie optymistyczne**: Sprawdź wersję przed zatwierdzeniem
- **MVCC (kontrola współbieżności wielu wersji)**: Utrzymuj wiele wersji wierszy
- **Blokowanie na poziomie wiersza**: Blokowanie określonych wierszy
- **Blokowanie na poziomie stołu**: Zablokuj cały stół

### Zakleszczenia
- Zależność cykliczna, w której transakcje czekają na siebie
- Zapobieganie: spójne uporządkowanie blokad, przekroczenia limitu czasu, wykrywanie zakleszczenia
- Rozwiązanie: Przerwij jedną transakcję

## Replikacja i skalowanie

### Typy replikacji
- **Master-Slave**: Jedna główna replika z wieloma odczytami
- **Master-Master**: Wiele prawyborów, replikacja dwukierunkowa
- **Multi-Master**: N prawyborów, potrzebne rozwiązanie konfliktu
- **Replikacja łańcuchowa**: Replikacja sekwencyjna przez węzły

### Podejścia skalujące
- **Skalowanie pionowe**: Zwiększ zasoby serwera (procesor, pamięć RAM, pamięć masowa)
- **Skalowanie poziome**: Dodaj więcej serwerów (sharding, partycjonowanie)
- **Repliki odczytu**: Odciąż ruch związany z odczytem
- **Sharding**: Dzielenie danych pomiędzy serwerami według klucza/zakresu/skrótu
- **Federacja**: Podział według funkcji/usługi

### Modele spójności
- **Silna spójność**: Wszystkie węzły widzą te same dane w tym samym czasie
- **Ostateczna spójność**: Węzły zbiegają się w czasie
- **Spójność przyczynowa**: Zachowane są związki przyczynowo-skutkowe
- **Przeczytaj swoje teksty**: Użytkownik natychmiast widzi swoje aktualizacje

## Kopia zapasowa i odzyskiwanie

### Strategie tworzenia kopii zapasowych
- **Pełna kopia zapasowa**: Pełna kopia bazy danych
- **Przyrostowa kopia zapasowa**: Zmiany od ostatniej kopii zapasowej
- **Różnicowa kopia zapasowa**: Zmiany od ostatniej pełnej kopii zapasowej
- **Odzyskiwanie do określonego momentu**: Przywracanie do określonego momentu
- **Ciągła kopia zapasowa**: Replikacja w czasie rzeczywistym do kopii zapasowej

### Procedury odzyskiwania
- **RTO (docelowy czas odzyskiwania)**: Maksymalny akceptowalny czas przestoju
- **RPO (cel punktu odzyskiwania)**: Maksymalna akceptowalna utrata danych
- **Plan odzyskiwania po awarii**: Udokumentowane procedury w przypadku awarii
- **Testowanie**: Regularne ćwiczenia regeneracyjne

## Bezpieczeństwo

### Kontrola dostępu
- **Uwierzytelnianie**: Zweryfikuj tożsamość użytkownika
- **Autoryzacja**: Przyznaj uprawnienia (PRZYZNAJ, ODWOŁAJ)
- **Role**: Uprawnienia grupowe ułatwiające zarządzanie
- **Zasada najmniejszych uprawnień**: Minimalny niezbędny dostęp

### Ochrona danych
- **Szyfrowanie w stanie spoczynku**: Szyfruj przechowywane dane
- **Szyfrowanie w transporcie**: TLS/SSL dla połączeń
- **Maskowanie**: Ukryj wrażliwe dane w środowisku nieprodukcyjnym
- **Tokenizacja**: Zamień wrażliwe dane na tokeny

### Typowe luki w zabezpieczeniach
- **Wstrzykiwanie SQL**: Złośliwy kod SQL wprowadzony przez użytkownika
- **Eskalacja uprawnień**: Uzyskanie nieautoryzowanego dostępu
- **Rejestrowanie audytu**: Śledź wszystkie działania w bazie danych
- **Zgodność**: wymagania RODO, HIPAA, PCI-DSS

## Nowoczesne technologie baz danych

### Bazy danych w chmurze
- **AWS**: RDS, Aurora, DynamoDB, przesunięcie ku czerwieni
- **Google Cloud**: Cloud SQL, Spanner, Bigtable, Firestore
- **Azure**: baza danych SQL, Cosmos DB, Synapse
- **Korzyści**: Usługa zarządzana, automatyczne skalowanie, kopie zapasowe w cenie

### Bazy danych NewSQL
- Połącz spójność SQL ze skalowalnością NoSQL
- **Przykłady**: CockroachDB, TiDB, YugabyteDB, Google Spanner
- **Funkcje**: Rozproszone, transakcje ACID, skalowanie poziome

### Bazy danych szeregów czasowych
- Zoptymalizowany pod kątem danych ze znacznikiem czasu
- **Przykłady**: InfluxDB, TimescaleDB, Prometheus
- **Przypadki użycia**: IoT, monitorowanie, dane finansowe

### Wektorowe bazy danych
- Przechowuj i przeglądaj wektory osadzania
- **Przykłady**: szyszka, Milvus, Weaviate, Qdrant
- **Przypadki użycia**: wyszukiwanie semantyczne, systemy rekomendacji, aplikacje AI

### Bazy danych zawierające wiele modeli
- Obsługa wielu modeli danych w jednym systemie
- **Przykłady**: ArangoDB, OrientDB, Azure Cosmos DB
- **Korzyść**: Elastyczność bez wielu baz danych

## ORM i dostęp do danych

### Mapowanie obiektowo-relacyjne
- **Cel**: Mapowanie tabel bazy danych na obiekty programistyczne
- **Popularne ORM**:
  - Python: SQLAlchemy, Django ORM, Peewee
  - JavaScript: Sequelize, Prisma, TypeORM
  - Java: Hibernacja, JPA
  - Ruby: ActiveRecord
  - .NET: Entity Framework### Korzyści
- Abstrakcja z SQL
- Bezpieczeństwo typu
- Zarządzanie migracjami
- API budowania zapytań

### Wady
- Narzut wydajności
- Złożone zapytania trudniejsze do napisania
- Problemy z zapytaniami N+1
- Krzywa uczenia się

## Administracja bazą danych

### Obowiązki administratora bazy danych
- Instalacja i konfiguracja
- Strojenie wydajności
- Tworzenie kopii zapasowych i odzyskiwanie
- Zarządzanie bezpieczeństwem
- Planowanie wydajności
- Monitorowanie i alarmowanie
- Zarządzanie poprawkami

### Wskaźniki monitorowania
- Czas odpowiedzi na zapytanie
- Przepustowość (transakcje na sekundę)
- Liczba połączeń
- Współczynnik trafień w pamięci podręcznej
- We/wy dysku
- Zablokuj czas oczekiwania
- Opóźnienie replikacji

### Zadania konserwacyjne
- **Odkurzanie/Analiza**: Aktualizuj statystyki, odzyskuj miejsce
- **Odbudowa indeksu**: Defragmentacja indeksów
- **Aktualizacje statystyk**: Informuj optymalizatora zapytań
- **Obrót dziennika**: Zarządzaj rozmiarami plików dziennika
- **Planowanie wydajności**: Przewiduj rozwój, planuj aktualizacje