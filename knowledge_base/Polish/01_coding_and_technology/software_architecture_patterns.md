<!--
---
# Metadata
title: "Software Architecture Patterns"
description: "Monolith, microservices, event-driven, DDD, caching, SOLID"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [software, architecture, patterns, coding-and-technology]
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

-->
# Wzorce architektury oprogramowania
Architektura to zbiór decyzji strukturalnych dotyczących organizacji systemu — jakie ma komponenty, w jaki sposób się komunikują i kto ponosi odpowiedzialność. Dobra architektura sprawia, że ​​system jest łatwy do zrozumienia, modyfikowania i skalowania. Zła architektura sprawia, że ​​każda zmiana jest walką. W tym pliku omówiono główne wzorce, kiedy należy ich używać i związane z nimi kompromisy.
---

## Monolit kontra mikrousługi
To najbardziej fundamentalna decyzja architektoniczna i warto podjąć właściwą decyzję.
| Aspekt | Monolit | Mikrousługi |
|--------|----------|-------------|
| **Struktura** | Pojedyncza jednostka do rozmieszczenia | Wiele małych, niezależnie wdrażanych usług |
| **Dane** | Wspólna baza danych | Każdy serwis jest właścicielem swoich danych |
| **Komunikacja** | Wywołania funkcji w procesie | Połączenia sieciowe (HTTP, gRPC, przesyłanie wiadomości) |
| **Skalowanie** | Skaluj całą aplikację | Skala poszczególnych usług |
| **Wdrożenie** | Pojedynczy cykl wydawniczy | Niezależne wdrożenia |
| **Złożoność** | Początkowo prostsze w opracowaniu | Złożoność operacyjna (sieciowanie, monitorowanie) |
| **Najlepsze dla** | Małe zespoły, produkty na wczesnym etapie | Duże zespoły, złożone domeny, duża skala |
### Kiedy zacząć od monolitu
Większość aplikacji powinna zaczynać się od monolitu. Łatwiej jest kompilować, testować, wdrażać i debugować. Zawsze możesz wyodrębnić usługi później, gdy będziesz mieć wyraźniejszy obraz granic swojej domeny. Nazywa się to czasami „monolitem modułowym” — monolitem z czystymi granicami wewnętrznymi, które ułatwiają późniejszą ekstrakcję.
### Kiedy zastosować mikrousługi
Rozważ mikrousługi, gdy:
- Zespoły są na tyle duże, że koordynacja staje się wąskim gardłem.
- Różne części systemu mają bardzo różne wymagania dotyczące skalowania.
- Potrzebujesz niezależnego wdrożenia komponentów.
- Twoja domena ma wyraźnie ograniczone konteksty (patrz DDD poniżej).
---

## Architektura warstwowa (N-poziom)
Najpopularniejszy wzór architektoniczny. Kod jest podzielony na warstwy, z których każda ma określoną odpowiedzialność.
```
â”Œ─────────────────────────┐
│   Presentation Layer    │  ← UI, controllers, API endpoints
├─────────────────────────┤
│   Application Layer     │  ← Use cases, orchestration
├─────────────────────────┤
│   Domain Layer          │  ← Business logic, entities
├─────────────────────────┤
│   Infrastructure Layer  │  ← Database, external services, file I/O
└─────────────────────────┘
```

| Warstwa | Odpowiedzialność | Zasada |
|-------|-------------|------|
| **Prezentacja** | Obsługa żądań użytkowników/HTTP | Można wywołać tylko warstwę aplikacji |
| **Aplikacja** | Organizuj przypadki użycia | Może wywołać warstwę domeny |
| **Domena** | Podstawowa logika biznesowa | Nie powinien zależeć od innych warstw |
| **Infrastruktura** | Kwestie techniczne | Implementuje interfejsy zdefiniowane w domenie |
**Kluczowa zasada**: zależności skierowane są do wewnątrz. Warstwa domeny nie wie o bazie danych ani frameworku sieciowym.
---

## Architektura sterowana zdarzeniami
Komponenty komunikują się poprzez emitowanie i reagowanie na **zdarzenia** — rzeczy, które się wydarzyły.
| Wzór | Opis |
|--------|------------|
| **Powiadomienie o wydarzeniu** | Usługa A emituje komunikat „OrderPlaced”; usługi B, C, D reagują |
| **Pozyskiwanie zdarzeń** | Przechowuj wszystkie zmiany stanu jako sekwencję zdarzeń (nie tylko stan bieżący) |
| **CQRS** | Oddziel model odczytu (zapytania) od modelu zapisu (polecenia) |
### Pozyskiwanie zdarzeń
Zamiast przechowywać „bieżący stan” w bazie danych, przechowuj każdą zmianę stanu jako zdarzenie:
```
OrderCreated(order_id=123, total=$50)
OrderPaid(order_id=123, payment_id=456)
OrderShipped(order_id=123, tracking=ABC)
```

Korzyści: pełna ścieżka audytu, możliwość rekonstrukcji dowolnego stanu z przeszłości, oddzieleni konsumenci. Wyzwania: ewolucja schematu zdarzeń, ostateczna spójność, złożoność debugowania.
### CQRS (oddzielenie odpowiedzialności za zapytania dotyczące poleceń)
| Strona | Cel | Baza danych |
|------|---------|--------------|
| **Polecenie (Zapis)** | Obsługuj mutacje; egzekwować zasady biznesowe | Zoptymalizowany pod kątem zapisu (znormalizowany) |
| **Zapytanie (Przeczytaj)** | Obsługuj żądania odczytu | Zoptymalizowany pod kątem odczytów (denormalizowany) |
CQRS naturalnie łączy się z Event Sourcing: zdarzenia ze strony zapisu są rzutowane na widoki zoptymalizowane pod kątem odczytu.
---

## Kolejki wiadomości i brokerzy zdarzeń
Gdy usługi muszą komunikować się asynchronicznie, podstawą są kolejki komunikatów.
| Narzędzie | Wpisz | Najlepsze dla |
|------|------|--------------|
| **Apache Kafka** | Rozproszony dziennik zdarzeń | Wysokoprzepustowe przesyłanie strumieniowe zdarzeń, pozyskiwanie zdarzeń |
| **KrólikMQ** | Broker wiadomości z routingiem | Kolejki zadań, złożone wzorce routingu |
| **AWS SQS** | Zarządzana kolejka | Natywne dla AWS, proste kolejkowanie |
| **AWS SNS** | Powiadomienie o pubie/subskrypcji | Fanout dla wielu subskrybentów |
| **Pub/Sub Google** | Zarządzany pub/subskrypcja | Strumieniowanie zdarzeń natywne dla GCP |
| **Strumienie Redis** | Lekki strumień | Proste rejestrowanie zdarzeń, buforowanie przypadków użycia |
### Wzorce przesyłania wiadomości
| Wzór | Opis |
|--------|------------|
| **Punkt-Punkt** | Jeden producent, jeden konsument na wiadomość |
| **Publikuj/Subskrybuj** | Jeden producent, wielu abonentów |
| **Prośba/Odpowiedź** | Styl synchroniczny zamiast transportu asynchronicznego |
| **Kolejka martwych listów** | Wiadomości, które nie zostały przetworzone, trafiają do osobnej kolejki do kontroli |
---

## Projekt oparty na domenie (DDD)
DDD to strategiczne podejście do projektowania oprogramowania, które koncentruje kod wokół koncepcji biznesowych, a nie problemów technicznych.
### Kluczowe pojęcia
| Koncepcja | Opis |
|--------|------------|
| **Ograniczony kontekst** | Granica, w ramach której model domeny jest spójny (np. „Zamawianie”, „Wysyłka”, „Rozliczenia”) |
| **Język wszechobecny** | Wspólne słownictwo pomiędzy programistami i ekspertami domenowymi |
| **Kruszywa** | Klastry powiązanych podmiotów traktowane jako pojedyncza jednostka dla zmian danych |
| **Podmioty** | Obiekty posiadające tożsamość (np. użytkownik z user_id) |
| **Obiekty wartości** | Przedmioty bez tożsamości; zdefiniowane przez ich atrybuty (np. Pieniądze, Adres) |
| **Wydarzenia domeny** | Coś, co wydarzyło się w domenie (np. OrderPlaced) |
| **Warstwa Antykorupcyjna** | Warstwa tłumaczeniowa pomiędzy Twoją domeną a systemami zewnętrznymi |
### Kiedy DDD pomaga
DDD jest najcenniejsze, gdy dziedzina biznesowa jest złożona – pomyśl o handlu elektronicznym, logistyce, usługach finansowych, opiece zdrowotnej. Jeśli Twoja domena jest prosta (blog, aplikacja typu „todo”), DDD będzie przesadą.
---

## Strategie buforowania
Buforowanie jest jednym z najskuteczniejszych sposobów poprawy wydajności, ale wprowadza złożoność w zakresie spójności.
| Strategia | Opis | Kompromis |
|---------|-------------|----------|
| **Odkładając na bok** | Aplikacja najpierw sprawdza pamięć podręczną; ładuje z DB w przypadku braku | Prosty; ostateczna spójność |
| **Zapis** | Zapisuj jednocześnie do pamięci podręcznej i bazy danych | Spójny; wolniej pisze |
| **Zapis z tyłu** | Zapisz w pamięci podręcznej; asynchroniczny zapis do DB | Szybko pisze; ryzyko utraty danych |
| **Przeczytanie** | Cache ładuje z bazy danych w przypadku pominięcia w sposób przezroczysty | Prostsze niż przechowywanie w pamięci podręcznej |
### Co buforować
| Warstwa | Co | Narzędzia |
|-------|------|-------|
| **CDN** | Zasoby statyczne, odpowiedzi API | CloudFront, Cloudflare |
| **Aplikacja** | Obliczone wyniki, dane sesji | Redis, Memcached |
| **Baza danych** | Wyniki zapytania, często odwiedzane wiersze | Pamięć podręczna zapytań, zmaterializowane widoki |
**Unieważnianie pamięci podręcznej** jest niezwykle trudne. Typowe strategie: TTL (czas życia), unieważnianie sterowane zdarzeniami (czyszczenie pamięci podręcznej po zmianie danych) i eksmisja LRU (najmniej ostatnio używane).
---

## Wzorce projektowe
### SOLIDNE zasady
| Zasada | Co to znaczy |
|----------|-------------|
| **S** — Pojedyncza odpowiedzialność | Klasa powinna mieć jeden powód do zmiany |
| **O** — Otwarte/Zamknięte | Otwarte na rozbudowę, zamknięte na modyfikację |
| **L** — Zmiana Liskowa | Podtypy powinny być substytucyjne dla swoich typów podstawowych |
| **I** — Segregacja interfejsu | Wiele specyficznych interfejsów > jeden interfejs ogólnego przeznaczenia |
| **D** — Inwersja zależności | Polegaj na abstrakcjach, a nie konkretach |
### Typowe wzorce
| Wzór | Zamiar | Przykład |
|--------|--------|--------|
| **Singleton** | Upewnij się, że klasa ma tylko jedną instancję | Pula połączeń z bazą danych |
| **Fabryka** | Twórz obiekty bez określania dokładnej klasy | `UserFactory.create(type="admin")`|
| **Obserwator** | Powiadom osoby na utrzymaniu, gdy stan się zmieni | Słuchacze wydarzeń, pub/sub |
| **Strategia** | Zamień algorytmy w czasie wykonywania | Strategia płatności: karta kredytowa, PayPal, kryptowaluta |
| **Repozytorium** | Abstrakcyjny dostęp do danych za przejrzystym interfejsem | `UserRepository.find_by_id(123)`|
| **Dekorator** | Dodaj zachowanie dynamicznie | Dekorator logowania wokół usługi |
| **Adapter** | Spraw, aby niekompatybilne interfejsy współpracowały ze sobą | Starszy adapter API |
---

## Wybór odpowiedniej architektury
Nie ma uniwersalnie „najlepszej” architektury. Właściwy wybór zależy od:
| Czynnik | Preferuj Monolit, gdy... | Preferuj mikrousługi, gdy... |
|------------|----------------------------|--------------------------------------|
| **Wielkość zespołu** | < 10 developers | >20 programistów, wiele zespołów |
| **Złożoność domeny** | Proste lub dobrze zrozumiałe | Złożone, wiele ograniczonych kontekstów |
| **Wymagania dotyczące skali** | Jednolite potrzeby skalowania | Różne komponenty wymagają różnej skali |
| **Częstotliwość wdrażania** | Pojedynczy cykl wydawniczy | Potrzebne niezależne wdrożenia |
| **Różnorodność technologii** | Jeden stos wystarczy | Różne usługi wymagają różnych technologii |
**Praktyczna rada**: zacznij od modułowego monolitu. Wyodrębniaj usługi tylko wtedy, gdy masz wyraźną potrzebę i jasne granice domeny. Przedwczesne mikrousługi to jeden z najczęstszych błędów architektonicznych w branży.