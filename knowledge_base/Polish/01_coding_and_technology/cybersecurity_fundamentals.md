<!--
---
# Metadata
title: "Cybersecurity Fundamentals"
description: "Encryption, TLS, OWASP, secure coding, SDL"
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
tags: [cybersecurity, coding-and-technology]
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
# Podstawy cyberbezpieczeństwa
Bezpieczeństwo to dziedzina, którą należy zintegrować z każdą warstwą systemu od samego początku, a nie dodawać ją po namyśle. Niezależnie od tego, czy tworzysz aplikację internetową, zarządzasz infrastrukturą, czy udostępniasz interfejs API, zrozumienie krajobrazu zagrożeń i podstaw obrony jest niezbędne.
---

## Szyfrowanie i kryptografia
### Szyfrowanie symetryczne i asymetryczne
| Wpisz | Jak to działa | Prędkość | Dystrybucja kluczy | Przykłady |
|------|------------|-------|----------------|-------------|
| **Symetryczny** | Ten sam klucz do szyfrowania i deszyfrowania | Szybki | Wyzwanie: jak udostępnić klucz? | AES-256, ChaCha20 |
| **Asymetryczny** | Klucz publiczny szyfruje, klucz prywatny odszyfrowuje | Wolniej | Klucz publiczny można udostępniać otwarcie | RSA, ECC (krzywa eliptyczna) |
W praktyce większość systemów stosuje **oba**: szyfrowanie asymetryczne w celu bezpiecznej wymiany klucza symetrycznego, a następnie szyfrowanie symetryczne dla większości danych. Tak działa TLS/HTTPS.
### Haszowanie
Hashowanie jest funkcją jednokierunkową: konwertuje dane wejściowe na ciąg znaków o stałym rozmiarze. Nie można tego odwrócić, ale to samo wejście zawsze daje ten sam wynik.
| Przypadek użycia | Zalecany algorytm | Unikaj |
|---------|----------------------|-------|
| **Przechowywanie haseł** | Argon2id, bcrypt, skrypt | MD5, SHA-1, zwykły SHA-256 (za szybki) |
| **Integralność danych** | SHA-256, SHA-3 | MD5 (uszkodzony), SHA-1 (uszkodzony) |
| **Podpisy cyfrowe** | Ed25519, RSA-2048+ | DSA |
### TLS/HTTPS
HTTPS to HTTP przez TLS (Transport Layer Security). Zapewnia:
- **Szyfrowanie**: Przesyłane dane nie mogą zostać odczytane przez osoby podsłuchujące.
- **Uwierzytelnianie**: Serwer potwierdza swoją tożsamość za pomocą certyfikatu.
- **Integralność**: Dane nie mogą być modyfikowane podczas przesyłania bez wykrycia.
Użyj protokołu TLS 1.2 lub 1.3. Wyłącz TLS 1.0 i 1.1. Włącz HSTS (HTTP Strict Transport Security), aby zmusić przeglądarki do ciągłego korzystania z protokołu HTTPS.
---

## Uwierzytelnianie i autoryzacja
### Uwierzytelnianie: kim jesteś?
| Metoda | Poziom bezpieczeństwa | Przypadek użycia |
|--------|-------------------|---------|
| **Hasło** | Niski–Średni | Konta podstawowe (wymuszaj ponad 12 znaków, sprawdzaj naruszenia) |
| **MSZ (TOTP)** | Wysoki | Standard dla wrażliwych kont (Google Authenticator, Authy) |
| **Klucz sprzętowy (FIDO2/WebAuthn)** | Bardzo wysoki | Konta o wysokim poziomie bezpieczeństwa (YubiKey) |
| **Biometryczny** | Średnio-wysoki | Odblokowanie urządzenia (odcisk palca, twarz) — niezbyt dobre jako jedyny czynnik |
| **OAuth2 / OIDC** | Wysoki | Logowanie strony trzeciej („Zaloguj się za pomocą Google”) |
**Zasady dotyczące haseł**: wymuszaj minimalną długość (12–16 znaków), sprawdzaj listy naruszonych haseł, używaj Argon2id lub bcrypt do mieszania z solami poszczególnych użytkowników.
### Autoryzacja: co możesz zrobić?
| Modelka | Opis | Przykład |
|-------|------------|--------|
| **RBAC** (kontrola dostępu oparta na rolach) | Uprawnienia przypisane do ról; użytkownicy dostają role | Administrator, redaktor, przeglądający |
| **ABAC** (oparte na atrybutach) | Reguły oparte na atrybutach użytkownika, zasobach, środowisku | „Menedżerowie mogą zatwierdzać prośby swojego zespołu” |
| **ACL** (Lista kontroli dostępu) | Jawne uprawnienia na użytkownika/zasób | Uprawnienia do plików (odczyt/zapis/wykonanie) |
**Zasada najmniejszych uprawnień**: zapewnij każdemu użytkownikowi, usłudze i procesowi tylko minimalny dostęp, jakiego potrzebuje.
### JWT (tokeny internetowe JSON)
| Aspekt | Zalecenie |
|--------|-------------------|
| **Podpisywanie** | Preferowany RS256 lub ES256 (asymetryczny); HS256 akceptowalny z zarządzanymi sekretami |
| **Wygaśnięcie** | 15–60 minut w przypadku tokenów dostępu; użyj tokenów odświeżania dla dłuższych sesji |
| **Przechowywanie** | Pliki cookie tylko HTTP (nie localStorage — podatne na XSS) |
| **Weryfikacja** | Zawsze sprawdzaj podpis, wydawcę, odbiorców i datę ważności |
---

## OWASP Top 10 (2021)
OWASP Top 10 to standardowy dokument uświadamiający w zakresie bezpieczeństwa aplikacji internetowych. Reprezentuje najbardziej krytyczne zagrożenia:
| # | Ryzyko | Co to znaczy |
|---|------|-------------|
| 1 | **Zepsuta kontrola dostępu** | Użytkownicy mają dostęp do zasobów, do których nie powinni |
| 2 | **Awarie kryptograficzne** | Słabe lub brakujące szyfrowanie danych wrażliwych |
| 3 | **Wtrysk** | SQL, NoSQL, polecenie systemu operacyjnego lub wstrzyknięcie LDAP |
| 4 | **Niebezpieczny projekt** | Wady architektoniczne, których nie da się naprawić poprzez wdrożenie |
| 5 | **Błędna konfiguracja zabezpieczeń** | Domyślne hasła, otwarte porty, szczegółowe komunikaty o błędach |
| 6 | **Wrażliwe komponenty** | Znane CVE w zależnościach |
| 7 | **Błędy uwierzytelniania** | Słabe hasła, złe zarządzanie sesją |
| 8 | **Błędy integralności** | Ataki na łańcuch dostaw, niepodpisane aktualizacje |
| 9 | **Błędy rejestrowania/monitorowania** | Brak wykrycia naruszeń |
| 10 | **SSRF** | Serwer oszukany, aby wysyłał żądania do systemów wewnętrznych |
---

## Bezpieczne praktyki kodowania
### Walidacja danych wejściowych
| Zasada | Dlaczego |
|------|-----|
| **Biała lista > Czarna lista** | Zdefiniuj, co jest dozwolone, a nie to, co jest blokowane |
| **Zapytania sparametryzowane** | Nigdy nie łącz danych wejściowych użytkownika z SQL — używaj przygotowanych instrukcji lub ORM |
| **Kodowanie HTML** | Zakoduj `<`, `>`, `&`, `"`, `'`, aby zapobiec XSS |
| **Ucieczka powłoki** | Unikaj tworzenia poleceń powłoki na podstawie danych wejściowych użytkownika; użyj`shlex.quote()`|
| **Ograniczenia długości** | Wymuś maksymalne długości, aby zapobiec przepełnieniu bufora i DoS |
| **Sprawdzanie typu** | Upewnij się, że liczby całkowite są liczbami całkowitymi, wartości logiczne są wartościami logicznymi |
### Typowe luki w zabezpieczeniach
| Luka | Atak | Obrona |
|-------------|--------|--------|
| **Wstrzyknięcie SQL** | `' OR 1=1 --`w formularzu logowania | Zapytania parametryczne |
| **XSS** | `<script>alert('hacked')</script>`w polu komentarza | Kodowanie wyjściowe, Polityka bezpieczeństwa treści |
| **CSRF** | Oszukać przeglądarkę użytkownika, aby wykonała nieautoryzowane żądanie | Tokeny CSRF, pliki cookie SameSite |
| **Przemierzanie ścieżki** | `../../etc/passwd`w parametrze pliku | Sprawdź i oczyść ścieżki plików |
| **IDOR** | Zmień`/user/123`na `/user/124`, aby zobaczyć dane innej osoby | Kontrole autoryzacyjne na każdym żądaniu |
---

## Bezpieczeństwo sieci
### Zapory sieciowe
| Wpisz | Opis |
|------|------------|
| **Filtrowanie pakietów** | Reguły oparte na IP, porcie, protokole |
| **Stanowy** | Śledzi stany połączeń; bardziej inteligentne filtrowanie |
| **Poziom aplikacji (WAF)** | Sprawdza ruch HTTP; blokuje wstrzykiwanie SQL, XSS itp. |
| **Grupy bezpieczeństwa w chmurze** | Wirtualne zapory ogniowe dla instancji chmurowych (AWS SG, Azure NSG) |
**Ogólna zasada**: domyślnie blokuj cały ruch przychodzący; otwieraj tylko to, co jest wyraźnie potrzebne (80, 443 dla sieci).
### Segmentacja sieci
Umieść bazy danych i pamięci podręczne w prywatnych podsieciach bez bezpośredniego dostępu do Internetu. Użyj strefy DMZ dla usług publicznych (serwery internetowe, moduły równoważenia obciążenia). Zastosuj zasadę najmniejszych uprawnień w dostępie do sieci.
---

## Zarządzanie tajemnicami
### Złota zasada
**Nigdy nie koduj tajemnic na stałe.** Żadnych kluczy API, haseł ani adresów URL baz danych w kodzie źródłowym. Żadnych tajemnic w zmiennych środowiskowych przypisanych do Gita. Żadnych tajemnic w obrazach Dockera.
### Narzędzia
| Narzędzie | Wpisz | Najlepsze dla |
|------|------|--------------|
| **Skarbiec HashiCorp** | Menedżer tajemnic przedsiębiorstwa | Sekrety dynamiczne, szyfrowanie jako usługa |
| **Menedżer tajemnic AWS** | Natywny w chmurze | Środowiska AWS |
| **Azure Key Vault** | Natywny w chmurze | Środowiska Azure |
| **SOPS** | Zaszyfrowane pliki | Szyfruj sekrety w Git (za pomocą KMS lub GPG) |
| **Tajemnice Dockera** | Natywny dla kontenera | Docker Swarm (w przypadku K8 rozważ CSI Secrets Store) |
| **dotenv (.env)** | Rozwój lokalny | Tylko rozwój — nigdy w produkcji ani nie zaangażowany |
### Obrót
Rotuj sekrety regularnie i automatycznie. Jeśli wycieknie sekret (np. zostanie przekazany do publicznego repo), natychmiast go zmień — nawet jeśli myślisz, że nikt go nie widział.
---

## Bezpieczeństwo zależności
Twoja aplikacja jest tak bezpieczna, jak jej najsłabsza zależność.
### Narzędzia do skanowania
| Język | Narzędzia |
|---------|-------|
| **Pyton** | `safety`,`pip-audit`,`bandit`|
| **Node.js** | `npm audit`,`yarn audit`,`snyk`|
| **Rdza** | `cargo audit`|
| **Idź** | `govulncheck`|
| **Ogólne** | `Dependabot`(GitHub), `Renovate`,`Trivy`|
### Integralność łańcucha dostaw
- Użyj plików blokujących (`package-lock.json`,`Cargo.lock`,`go.sum`) dla powtarzalnych kompilacji.
- Sprawdź sumy kontrolne pobranych zależności.
- Preferuj oficjalne rejestry i zweryfikowanych wydawców.
- Automatyzuj drobne aktualizacje/poprawki za pomocą programu Depabot lub Renovate.
---

## Cykl życia rozwoju zabezpieczeń (SDL)
| Faza | Aktywność |
|-------|--------------|
| **Szkolenie** | Upewnij się, że programiści rozumieją typowe luki w zabezpieczeniach |
| **Modelowanie zagrożeń** | Identyfikacja potencjalnych zagrożeń na etapie projektowania |
| **Standardy bezpiecznego kodowania** | Egzekwuj za pomocą lintersów i list kontrolnych przeglądu kodu |
| **SOB** | Analiza statyczna kodu źródłowego (SonarQube, CodeQL) |
| **KONIEC** | Analiza dynamiczna działającej aplikacji (OWASP ZAP, Burp Suite) |
| **SKA** | Analiza składu oprogramowania — zależności skanowania |
| **Testy penetracyjne** | Regularne ćwiczenia etycznego hakowania |
| **Nagroda za błąd** | Zachęcaj badaczy zewnętrznych do znalezienia luk w zabezpieczeniach |
| **Plan reagowania na incydenty** | Miej jasny plan na wypadek wykrycia naruszenia |
---

## Lista kontrolna sytuacji awaryjnych
Kiedy podejrzewasz naruszenie:
1. **Nie panikuj** – ale działaj szybko.
2. **Odizoluj** dotknięte systemy (w razie potrzeby odłącz od sieci).
3. **Zachowaj dowody**: przechwytywanie dzienników, zrzutów pamięci, obrazów dysków.
4. **Określ zakres**: jakie systemy, jakie dane?
5. **Obróć** wszystkie skompromitowane dane uwierzytelniające i sekrety.
6. **Załataj** lukę.
7. **Powiadom** zainteresowanych użytkowników i organy regulacyjne, jeśli jest to wymagane (w terminach prawnych).
8. **Sekcja zwłok**: udokumentowanie pierwotnej przyczyny i działań w ciągu 24–48 godzin.