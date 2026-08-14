---
# Metadata
title: "Security Best Practices"
description: "OWASP Top 10, input validation, auth, secrets management"
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
tags: [security, best, practices, coding-and-technology]
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
# Najlepsze praktyki dotyczące bezpieczeństwa
Praktyczny przewodnik po zabezpieczaniu aplikacji, infrastruktury i danych — od programowania po produkcję.
---

## OWASP Top 10 (2021) — przegląd
1. **Zepsuta kontrola dostępu**: Użytkownicy mogą uzyskać dostęp do zasobów, do których nie powinni.
2. **Awarie kryptograficzne**: Słabe lub brakujące szyfrowanie.
3. **Wstrzykiwanie**: SQL, NoSQL, polecenie systemu operacyjnego lub wstrzyknięcie LDAP.
4. **Niepewny projekt**: Wady architektoniczne.
5. **Błędna konfiguracja zabezpieczeń**: Domyślne hasła, otwarte porty, szczegółowe błędy.
6. **Wrażliwe i nieaktualne komponenty**: Znane CVE w zależnościach.
7. **Błędy identyfikacji i uwierzytelnienia**: Słabe hasła, złe zarządzanie sesją.
8. **Awarie integralności oprogramowania i danych**: Ataki na łańcuch dostaw, niepodpisane aktualizacje.
9. **Błędy rejestrowania i monitorowania bezpieczeństwa**: Brak wykrycia naruszeń.
10. **Fałszowanie żądań po stronie serwera (SSRF)**: Nadużycie serwera w celu wysyłania żądań do systemów wewnętrznych.
---

## Walidacja danych wejściowych i kodowanie wyjściowe
### Zasady walidacji
- **Biała lista > Czarna lista**: Zdefiniuj dozwolone wzorce (np. wyrażenie regularne dla wiadomości e-mail) zamiast blokować znane złe wzorce.
- **Ograniczenia długości**: wymuszaj maksymalne długości, aby zapobiec przepełnieniu bufora i DoS.
- **Sprawdzanie typu**: Upewnij się, że liczby całkowite są liczbami całkowitymi, a wartości logiczne są wartościami logicznymi.
- **Użyj dobrze przetestowanych bibliotek**: Do sprawdzania poprawności adresu e-mail, adresu URL i daty użyj bibliotek standardowych (np.`email-validator`w Pythonie,`validator.js`w węźle).
### Kodowanie wyjściowe
- **Kodowanie HTML**: Zakoduj `<`, `>`, `&`, `"`, `'`, aby zapobiec XSS.
- **Parametryzacja SQL**: Nigdy nie łącz danych wejściowych użytkownika z zapytaniami SQL. Użyj sparametryzowanych zapytań (przygotowanych instrukcji) lub ORM.
- **Ucieczka powłoki**: Unikaj tworzenia poleceń powłoki na podstawie danych wprowadzonych przez użytkownika; jeśli jest to nieuniknione, użyj`shlex.quote()`lub podobnego.
---

## Uwierzytelnianie i autoryzacja
### Zarządzanie hasłami
- **Haszowanie**: Przechowuj hasła przy użyciu silnego, powolnego algorytmu mieszania: **Argon2id** (preferowany), **bcrypt**, **scrypt** lub **PBKDF2**.
- **Solenie**: Dodaj unikalną sól dla każdego użytkownika.
- **Minimalna długość**: Wymuś co najmniej 12–16 znaków.
- **MFA (Uwierzytelnianie wieloskładnikowe)**: Wymaga drugiego czynnika (TOTP, SMS, klucz sprzętowy) w przypadku wrażliwych operacji.
- **Ograniczenie szybkości**: Zapobiegaj próbom użycia siły na punktach końcowych logowania (np. 5 prób na 5 minut na adres IP/użytkownika).
### Zarządzanie sesją
- Używaj bezpiecznych plików cookie SameSite obsługujących wyłącznie protokół HTTP dla tokenów sesji.
- Ustaw odpowiednie czasy ważności.
- Unieważnianie sesji w przypadku wylogowania i zmiany hasła.
- Unikaj ujawniania identyfikatorów sesji w adresach URL.
### OAuth2 / OIDC
- Korzystaj ze sprawdzonych bibliotek (np. Authlib, PyJWT, Passport.js, Spring Security).
- Dokładnie zweryfikuj tokeny identyfikacyjne (podpis, wydawca, odbiorcy, data ważności).
- Użyj parametrów stanu, aby zapobiec CSRF.
- Zachowaj tajemnicę klienta w tajemnicy.
### JWT (tokeny internetowe JSON)
- **Znak**: Użyj RS256 lub ES256 (asymetryczny) dla większego bezpieczeństwa; HS256 (symetryczny) jest akceptowalny, jeśli dobrze zarządza się wspólnymi sekretami.
- **Weryfikuj**: Zawsze sprawdzaj podpis, wystawcę (`iss`), odbiorców (`aud`) i datę ważności (`exp`).
- **Zachowaj krótki okres ważności**: 15–60 minut dla tokenów dostępu; używaj tokenów odświeżania w przypadku dłuższych sesji.
- **Przechowuj bezpiecznie**: Nigdy nie przechowuj JWT w localStorage (podatny na XSS); zamiast tego używaj plików cookie obsługujących wyłącznie protokół HTTP.
---

## Bezpieczeństwo API
### Uwierzytelnianie
- Zawsze uwierzytelniaj wywołania API (z wyjątkiem publicznych punktów końcowych).
- Preferuj klucze API lub tokeny OAuth2 zamiast uwierzytelniania podstawowego (które wysyła dane uwierzytelniające na każde żądanie).
### Ograniczanie szybkości i ograniczanie przepustowości
- Zastosuj limity szybkości dla użytkownika i adresu IP, aby zapobiec nadużyciom i DoS.
- Zwróć`429 Too Many Requests`z nagłówkiem `Retry-After`.
### CORS (współdzielenie zasobów między źródłami)
- Zezwalaj tylko na określone źródła (nigdy na`*`w produkcji).
- Sprawdź nagłówek`Origin`po stronie serwera.
### Walidacja danych wejściowych
- Sprawdź wszystkie parametry żądania, w tym nagłówki i treść.
- Odrzuć nieoczekiwane pola (`"strict": true` lub`additionalProperties: false`w schemacie JSON).
### HTTPS/TLS
— Wymuś protokół HTTPS w środowisku produkcyjnym.
- Użyj HSTS (HTTP Strict Transport Security), aby zmusić przeglądarki do korzystania z protokołu HTTPS.
- Użyj TLS 1.2 lub 1.3 (wyłącz TLS 1.0/1.1).
---

## Zarządzanie tajemnicami
### Nigdy nie ma sekretów kodowanych na stałe
- Nie przekazuj sekretów (kluczy API, haseł, adresów URL baz danych) kontroli źródła.
- Używaj zmiennych środowiskowych lub narzędzi do zarządzania sekretami.
### Narzędzia
| Narzędzie | Opis |
|------|------------|
| **Skarbiec HashiCorp** | Dynamiczne sekrety klasy korporacyjnej |
| **Menedżer tajnych wpisów AWS / Azure Key Vault / Menedżer tajnych kluczy GCP** | Natywny w chmurze |
| **SOPS** | Szyfruj sekrety w plikach i zatwierdzaj je (za pomocą KMS lub GPG) |
| **Tajemnice Dockera** | Dla trybu roju; Sekrety Kubernetes (rozważ zewnętrzny sterownik CSI Secrets Store) |
### Obrót
- Regularnie zmieniaj sekrety i konta usług.
- Automatyzuj rotację tam, gdzie to możliwe.
---

## Zarządzanie zależnościami
### Skanowanie pod kątem luk w zabezpieczeniach
| Język/platforma | Narzędzia |
|--------------------------------|-------|
| **Pyton** | `safety`,`pip-audit`,`bandit`|
| **Węzeł** | `npm audit`,`yarn audit`,`snyk`|
| **Rdza** | `cargo audit`|
| **Idź** | `govulncheck`|
| **Ogólne** | `Dependabot`(GitHub), `Renovate`,`Trivy`|
### Łatanie
- Aktualizuj zależności do poprawionych wersji.
- Skonfiguruj automatyczne żądania ściągnięcia dla mniejszych aktualizacji/poprawek.
- Przejrzyj dzienniki zmian pod kątem istotnych zmian.
### Integralność łańcucha dostaw
- Użyj plików blokujących pakiety (`package-lock.json`,`Cargo.lock`,`go.sum`), aby zapewnić powtarzalność kompilacji.
- Sprawdź sumy kontrolne pobranych zależności.
- Preferuj oficjalne rejestry i ufaj tylko zweryfikowanym wydawcom.
---

## Bezpieczeństwo infrastruktury
### Zapory sieciowe
- Blokuj wszystkie porty przychodzące z wyjątkiem tych wyraźnie potrzebnych (np. 80, 443).
- Ogranicz dostęp SSH do określonych zakresów IP (lub użyj hosta VPN/bastionu).
— Użyj grup zabezpieczeń (AWS) lub sieciowych grup zabezpieczeń (Azure), aby uzyskać precyzyjną kontrolę.
### Hartowanie systemu operacyjnego
- Regularnie stosuj aktualizacje zabezpieczeń (`sudo apt upgrade`,`yum update`).
- Wyłącz niepotrzebne usługi i konta domyślne.
- Użyj funkcji Fail2ban, aby zablokować próby użycia siły na SSH.
- Wzmocnij SSH: wyłącz logowanie roota, użyj uwierzytelniania na podstawie klucza, zmień domyślny port (opcjonalnie).
### Segmentacja sieci
- Umieść bazy danych i pamięci podręczne w prywatnych podsieciach bez dostępu do Internetu.
- Korzystaj ze strefy DMZ dla usług publicznych.
- Zastosuj zasadę najmniejszych uprawnień w dostępie do sieci.
### Sekrety infrastruktury
- Nigdy nie przechowuj sekretów w zmiennych środowiskowych CI/CD, chyba że są one zaszyfrowane.
- Używaj ról IAM dostawcy chmury dla instancji EC2/VM zamiast kluczy długotrwałych.
---

## Rejestrowanie i monitorowanie
### Co rejestrować
- Zdarzenia uwierzytelniające (sukces/niepowodzenie).
- Decyzje dotyczące kontroli dostępu (błędy autoryzacyjne).
- Działania administracyjne (tworzenie użytkowników, usuwanie, zmiany uprawnień).
- Zmiany schematu bazy danych.
- Błędy systemowe i wyjątki.
- Żądania i odpowiedzi API (redagowanie wrażliwych danych).
### Czego nie rejestrować
- Hasła, tajemnice, tokeny, PII (dane osobowe), chyba że zostały zaszyfrowane/zredagowane.
- Pełne numery kart kredytowych.
### Alarmowanie
- Skonfiguruj alerty dla:
  - Wiele nieudanych logowań (potencjalna brutalna siła).
  - Nietypowe wzorce dostępu (np. z nowych lokalizacji, w nieparzystych godzinach).
  - Utworzono nowe konta administratorów.
  - Wysoki poziom błędów lub skoki opóźnień.
- Użyj SIEM (zarządzanie informacjami o bezpieczeństwie i zdarzeniami) w celu uzyskania zaawansowanej korelacji.
### Przechowywanie dziennika
- Przechowuj dzienniki przez co najmniej 30–90 dni, w zależności od wymogów prawnych.
- Przechowuj logi w scentralizowanym systemie zabezpieczającym przed manipulacją (np. ELK Stack, Splunk, Datadog).
---

## Bezpieczny cykl życia oprogramowania (SDL)
1. **Szkolenie**: Upewnij się, że programiści rozumieją typowe luki w zabezpieczeniach.
2. **Modelowanie zagrożeń**: Zidentyfikuj potencjalne zagrożenia na wczesnym etapie projektowania.
3. **Bezpieczne standardy kodowania**: Egzekwuj za pomocą lintersów i list kontrolnych przeglądu kodu.
4. **SAST** (statyczne testowanie bezpieczeństwa aplikacji): Skanuj kod źródłowy pod kątem luk w zabezpieczeniach (SonarQube, CodeQL).
5. **DAST** (Dynamiczne testowanie bezpieczeństwa aplikacji): Skanuj uruchomione aplikacje (OWASP ZAP, Burp Suite).
6. **SCA** (Analiza składu oprogramowania): Zależności skanowania.
7. **Testy penetracyjne**: Regularne ćwiczenia etycznego hakowania.
8. **Nagroda za błąd**: Zachęcaj zewnętrznych badaczy do odpowiedzialnego wyszukiwania luk w zabezpieczeniach.
9. **Plan reagowania na incydenty**: Miej jasny plan na wypadek wykrycia naruszenia.
---

## Awaryjna lista kontrolna (w przypadku podejrzenia naruszenia)
1. **Nie panikuj** – ale działaj szybko.
2. **Odizoluj** systemy, których dotyczy problem (w razie potrzeby odłącz od sieci).
3. **Zachowaj dowody**: Przechwytuj dzienniki, zrzuty pamięci i obrazy dysków.
4. **Określ** zakres: które systemy, jakie dane.
5. **Obróć** wszystkie skompromitowane dane uwierzytelniające i sekrety.
6. **Załataj** lukę.
7. **Powiadom** zainteresowanych użytkowników i organy regulacyjne, jeśli jest to wymagane (w terminach prawnych).
8. **Przeprowadź sekcję zwłok**, aby poznać pierwotną przyczynę i ulepszyć procesy.