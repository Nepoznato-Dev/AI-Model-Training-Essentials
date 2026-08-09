---
# Metadata
title: "API Design and Architecture"
description: "REST, GraphQL, gRPC, versioning, auth, API gateways"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [api, design, architecture, coding-and-technology]
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

# Projektowanie i architektura API
API (interfejs programowania aplikacji) to sposób, w jaki komponenty oprogramowania komunikują się ze sobą. Dobrze zaprojektowane API jest intuicyjne, spójne, a praca z nim to przyjemność. Źle zaprojektowany powoduje zamieszanie, błędy i frustrację. Ten plik opisuje zasady, wzorce i praktyki tworzenia interfejsów API, z których programiści faktycznie chcą korzystać.
---

## Zasady API REST
REST (Representational State Transfer) to dominujący styl architektoniczny internetowych interfejsów API. Traktuje dane jako **zasoby** identyfikowane poprzez adresy URL i wykorzystuje metody HTTP do operowania na nich.
### Podstawowe zasady
| Zasada | Opis |
|---------------|------------|
| **Zasoby** | Wszystko jest zasobem z URI (`/users/123`, `/orders/456`) |
| **Metody HTTP** | GET (odczyt), POST (utwórz), PUT (zamień), PATCH (częściowa aktualizacja), DELETE (usuń) |
| **Bezpaństwowość** | Każde żądanie zawiera wszystkie potrzebne informacje; brak stanu sesji po stronie serwera |
| **Jednolity interfejs** | Spójne nazewnictwo zasobów, standardowe metody, standardowe kody statusu |
| **Reprezentacja** | Zasoby mogą być reprezentowane w wielu formatach (JSON, XML) |
### Konwencje nazewnictwa zasobów
| Zrób | Nie |
|----|-------|
| `/users`(rzeczownik w liczbie mnogiej) | `/user`(liczba pojedyncza) |
| `/users/123/orders`(zagnieżdżony) | `/getOrdersForUser?id=123`|
| `/products?category=electronics`(parametry zapytania do filtrowania) | `/productsByCategory/electronics`|
| Użyj łączników:`/user-profiles`| Użyj podkreśleń:`/user_profiles`|
### Metody HTTP i idempotencja
| Metoda | Cel | Idempotentny? | Bezpieczna? |
|--------|---------|------------|------|
| **DOBIERZ** | Przeczytaj zasób | ✅Tak | ✅Tak |
| **POST** | Utwórz zasób | ❌ Nie | ❌ Nie |
| **UMIEŚĆ** | Całkowicie zastąp zasób | ✅Tak | ❌ Nie |
| **ŁATKA** | Częściowo zaktualizuj zasób | ❌ Nie* | ❌ Nie |
| **USUŃ** | Usuń zasób | ✅Tak | ❌ Nie |
*PATCH można uczynić idempotentnym przy starannym projektowaniu.
### Kody stanu HTTP
| Kod | Znaczenie | Kiedy stosować |
|------|---------|------------|
| **200** | OK | Pomyślne POBIERZ, PUT, PATCH, USUŃ |
| **201** | Utworzono | Pomyślny POST (utworzono zasób) |
| **204** | Brak treści | Pomyślne USUŃ (nic nie można zwrócić) |
| **400** | Złe żądanie | Nieprawidłowe dane wejściowe lub źle sformułowane żądanie |
| **401** | Nieautoryzowane | Brakujące lub nieprawidłowe uwierzytelnienie |
| **403** | Zabronione | Uwierzytelniony, ale nieautoryzowany |
| **404** | Nie znaleziono | Zasób nie istnieje |
| **409** | Konflikt | Zduplikowany konflikt zasobów lub stanu |
| **422** | Podmiot nieprzetwarzalny | Prawidłowy JSON, ale błędy semantyczne |
| **429** | Zbyt wiele żądań | Przekroczono limit stawki |
| **500** | Wewnętrzny błąd serwera | Nieoczekiwany błąd serwera |
| **502** | Zła brama | Awaria usługi upstream |
| **503** | Usługa niedostępna | Tymczasowe przeciążenie lub konserwacja |
---

## Wersja API
Interfejsy API ewoluują. Kiedy trzeba wprowadzić istotne zmiany, wersjonowanie pozwala istniejącym klientom kontynuować pracę.
| Strategia | Przykład | Plusy | Wady |
|---------|---------|------|------|
| **Ścieżka adresu URL** | `/v1/users`,`/v2/users`| Proste, jednoznaczne | Zmiany adresu URL według wersji |
| **Parametr zapytania** | `/users?version=2`| Elastyczny | Łatwo zapomnieć |
| **Nagłówek** | `Accept: application/vnd.myapi.v2+json`| Czyste adresy URL | Mniej wykrywalne |
| **Brak wersjonowania** | Tylko ewolucja schematu | Najprostszy | Przełomowe zmiany wpływają na wszystkich |
**Najlepsza praktyka**: dla przejrzystości użyj wersji ścieżki URL (`/v1/`). Obsługuj co najmniej jedną poprzednią wersję. Wycofaj stare wersje z jasnymi harmonogramami.
---

## Metody uwierzytelniania
| Metoda | Jak to działa | Najlepsze dla |
|------------|------------|---------|
| **Klucze API** | Tajny klucz w nagłówku (`X-API-Key: abc123`) | Serwer-serwer, proste integracje |
| **OAuth2** | Delegowanie oparte na tokenach z zakresami | Dostęp stron trzecich, aplikacje autoryzowane przez użytkownika |
| **JWT** | Samodzielny token z oświadczeniami | Uwierzytelnianie bezstanowe w usługach |
| **Podstawowe uwierzytelnianie** | Nazwa użytkownika zakodowana w formacie Base64:hasło | Tylko rozwój — nigdy produkcja bez TLS |
| **Ciasteczka sesyjne** | Identyfikator sesji po stronie serwera w pliku cookie tylko HTTP | Tradycyjne aplikacje internetowe |
### Przepływ OAuth2 (uproszczony)
1. Klient przekierowuje użytkownika do serwera autoryzacyjnego.
2. Użytkownik loguje się i udziela uprawnień.
3. Serwer autoryzacyjny zwraca kod autoryzacyjny.
4. Klient wymienia kod na token dostępu (i opcjonalnie token odświeżający).
5. Klient wykorzystuje token dostępowy do wywołania API.
6. Gdy token dostępu wygaśnie, użyj tokena odświeżenia, aby uzyskać nowy.
---

## Style API: REST vs GraphQL vs gRPC
| Funkcja | ODPOCZYNEK | WykresQL | gRPC |
|--------|------|---------|------|
| **Format danych** | JSON (zazwyczaj) | JSON | Protobuf (binarny) |
| **Punkty końcowe** | Wiele (jeden na zasób) | Pojedynczy punkt końcowy | Zdefiniowane przez plik .proto |
| **Przesadne pobieranie** | Wspólne (zdobądź więcej niż potrzeba) | Brak (klient określa pola) | Brak (zdefiniowany według schematu) |
| **Za mało** | Wymaga wielu połączeń | Brak (uzyskaj dokładnie to, czego potrzebujesz) | Brak |
| **W czasie rzeczywistym** | Potrzebne WebSockety | Wbudowane subskrypcje | Wbudowane przesyłanie strumieniowe |
| **Buforowanie** | Buforowanie HTTP działa naturalnie | Trudniejsze do buforowania | ograniczona |
| **Krzywa uczenia się** | Niski | Średni | Średnio-wysoki |
| **Najlepsze dla** | Publiczne API, aplikacje CRUD | Złożone interfejsy użytkownika, aplikacje mobilne | Wewnętrzne mikroserwisy, wysoka wydajność |
---

## Paginacja, filtrowanie i sortowanie
W przypadku punktów końcowych zwracających listy:
| Technika | Przykład | Kiedy stosować |
|----------|---------|------------|
| **Przesunięcie/Limit** | `?offset=20&limit=10`| Prosty; działa dla małych zbiorów danych |
| **Oparta na kursorze** | `?cursor=abc123&limit=10`| Duże zbiory danych; spójne wyniki |
| **Zestaw kluczy** | `?created_after=2024-01-01&limit=10`| Bardzo wydajny; wymaga unikalnego klucza |
```json
// Cursor-based response
{
  "data": [...],
  "pagination": {
    "next_cursor": "abc123",
    "has_more": true
  }
}
```

---

## Ograniczenie szybkości
Chroń swoje API przed nadużyciami i zapewnij uczciwe użytkowanie.
| Strategia | Jak to działa |
|--------------|------------|
| **Naprawiono okno** | N żądań na okno czasowe (np. 100/godzinę) |
| **Przesuwane okno** | Bardziej ziarnisty; zlicza żądania w przewijanym oknie |
| **Wiaderko na żetony** | Tokeny dodawane po stałej stawce; każde żądanie zużywa token |
Zwróć`429 Too Many Requests`z nagłówkami:```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## Obsługa błędów
Spójne reakcje na błędy znacznie ułatwiają pracę z interfejsami API:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "issue": "Invalid email format"
      }
    ]
  }
}
```

**Zasady**: używaj spójnej struktury błędów, dołączaj komunikaty, na których można podjąć działania, używaj standardowych kodów stanu HTTP, rejestruj błędy po stronie serwera z identyfikatorami korelacji i nigdy nie ujawniaj śladów stosu ani szczegółów wewnętrznych.
---

## Dokumentacja API
| Narzędzie | Opis |
|------|------------|
| **OpenAPI (Swagger)** | Standard branżowy dotyczący dokumentacji API REST |
| **Przechylony interfejs użytkownika** | Dokumentacja interaktywnego API ze specyfikacji OpenAPI |
| **Listonosz** | Testowanie API, dokumentacja i udostępnianie kolekcji |
| **Przeróbka** | Piękne dokumenty referencyjne API ze specyfikacji OpenAPI |
| **GraphQL Plac zabaw / GraphiQL** | Interaktywna eksploracja GraphQL |
**Najlepsza praktyka**: najpierw napisz specyfikację OpenAPI (programowanie oparte na specyfikacjach), a następnie wygeneruj z niej dokumentację i zestawy SDK klienta.
---

## Wzorce bram API
Brama API znajduje się pomiędzy klientami a usługami zaplecza, zapewniając pojedynczy punkt wejścia.
| Odpowiedzialność | Opis |
|--------------|------------|
| **Trasowanie** | Kieruj żądania do odpowiednich usług backendowych |
| **Uwierzytelnianie** | Zweryfikuj tokeny na poziomie bramy |
| **Ograniczenie szybkości** | Zastosuj limity globalne lub na klienta |
| **Transformacja** | Konwersja między protokołami (REST ↔ gRPC) |
| **Buforowanie** | Buforuj typowe odpowiedzi |
| **Monitorowanie** | Scentralizowane rejestrowanie i metryki |
| **Równoważenie obciążenia** | Rozłóż ruch pomiędzy instancjami usługi |
| Narzędzie | Wpisz |
|------|------|
| **Kong** | Brama API typu open source (oparta na Nginx) |
| **Brama API AWS** | W pełni zarządzany, zintegrowany z AWS |
| **Zarządzanie interfejsami API platformy Azure** | Zarządzana brama z portalem dla programistów |
| **Wysłannik / Istio** | Siatka usług z możliwościami bramy API |
| **Traefik** | Automatyczne wykrywanie, integracja Let's Encrypt |
---

## Haki internetowe
Elementy webhook umożliwiają interfejsowi API wypychanie zdarzeń do klientów w czasie rzeczywistym, zamiast zmuszać klientów do sondowania zmian.
| Aspekt | Najlepsza praktyka |
|--------|-------------|
| **Dostawa** | Żądanie POST z ładunkiem JSON na adres URL klienta |
| **Bezpieczeństwo** | Podpisuj ładunki za pomocą HMAC; klient weryfikuje podpis |
| **Niezawodność** | Ponów próbę nieudanych dostaw z wykładniczym wycofywaniem |
| **Idempotencja** | Dołącz unikalny identyfikator wydarzenia; klient obsługuje duplikaty |
| **Wersjonowanie** | Uwzględnij wersję API w ładunku elementu webhook |
---

## Lista kontrolna projektu
- [ ] Zasoby to rzeczowniki w liczbie mnogiej (`/users`, a nie`/getUser`)
- [ ] Metody HTTP używane poprawnie (GET do odczytów, POST do tworzenia itp.)
- [ ] Spójny format reakcji na błąd
- [ ] Paginacja dla wszystkich punktów końcowych listy
- [ ] Ograniczenie szybkości z przejrzystymi nagłówkami
- [ ] Zdefiniowano strategię wersjonowania API
- [ ] Uwierzytelnienie i autoryzacja na miejscu
- [ ] Walidacja danych wejściowych na wszystkich punktach końcowych
- [ ] Utrzymana dokumentacja OpenAPI/Swagger
- [ ] CORS skonfigurowany poprawnie
- [ ] HTTPS wymuszony w produkcji
- [ ] Klucze idempotencji dla operacji POST, jeśli są potrzebne