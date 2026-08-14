<!--
---
# Metadata
title: "Web Development"
description: "Frontend, backend, DevOps, security"
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
tags: [web, development, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "13 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Tworzenie stron internetowych
## Rozwój frontendu
### Podstawowe technologie
#### HTML (język znaczników hipertekstowych)
- **Semantyczny HTML**: Używanie znaczących tagów (`<header>`,`<nav>`,`<main>`,`<article>`,`<section>`,`<aside>`,`<footer>`)
- **Formularze**: Typy danych wejściowych, sprawdzanie poprawności, etykiety dostępności
- **Media**: Obrazy, wideo, osadzanie dźwięku
- **Metagi**: SEO, rzutnia, kodowanie znaków
- **Funkcje HTML5**: Canvas, SVG, pamięć lokalna, geolokalizacja, gniazda internetowe
#### CSS (kaskadowe arkusze stylów)
- **Model pudełka**: Treść, dopełnienie, obramowanie, margines
- **Systemy układu**:
  - **Flexbox**: Układy jednowymiarowe, justowanie treści, wyrównywanie elementów
  - **Siatka**: Układy dwuwymiarowe, szablon siatki, obszar siatki
  - **Pozycjonowanie**: Statyczne, względne, bezwzględne, stałe, lepkie
- **Responsywny projekt**: zapytania o media, podejście mobilne
- **Zmienne CSS**: Niestandardowe właściwości motywu
- **Animacje**: Przejścia, klatki kluczowe, transformacje
- **Preprocesory**: Sass, Less (zmienne, miksy, zagnieżdżanie)
#### JavaScript
- **Manipulacja DOM**: Wybieranie, tworzenie, modyfikowanie elementów
- **Wydarzenia**: kliknij, prześlij, klawiatura, zdarzenia niestandardowe, delegowanie wydarzeń
- **Funkcje ES6+**: Funkcje strzałek, destrukturyzacja, rozprzestrzenianie/reszta, moduły, asynchronizacja/oczekiwanie
- **API**: Fetch, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: pisanie statyczne, interfejsy, typy generyczne, dekoratory
### Nowoczesne frameworki frontendowe
#### Reaguj
- **Komponenty**: Komponenty funkcjonalne, komponenty klasowe
- **Hooki**: useState, useEffect, useContext, useReducer, niestandardowe hooki
- **Zarządzanie stanem**: API kontekstowe, Redux, Zustand, Recoil
- **Routing**: Reaguj Router (BrowserRouter, Trasy, Trasa, Link)
- **Ekosystem**: Next.js (SSR, SSG), Remix, Gatsby
- **Wirtualny DOM**: Wydajne renderowanie dzięki algorytmowi różnicowania
#### Vue.js
- **Opcje API**: dane, metody, obliczone, obserwowane
- **API składu**: setup(), ref, reaktywne, obliczone
- **Wytyczne**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: Zarządzanie państwowe
- **Vue Router**: Routing po stronie klienta
- **Nuxt.js**: Struktura renderowania po stronie serwera
#### Kątowy
- **Komponenty**: Dekoratory, szablony, haki cyklu życia
- **Usługi**: Wstrzykiwanie zależności, wzór singletonu
- **RxJS**: Programowanie reaktywne, obserwowalne
- **Routing**: Moduł Routera, osłony, resolwery
- **Formularze**: Reaktywne formularze oparte na szablonach
- **NgRx**: Zarządzanie stanem w stylu Redux
### Narzędzia do tworzenia pakietów i pakiety
- **Webpack**: łączenie modułów, dzielenie kodu, moduły ładujące, wtyczki
- **Vite**: Narzędzie do szybkiego budowania przy użyciu natywnych modułów ES
- **Parcel**: Pakiet o zerowej konfiguracji
- **Pakiet zbiorczy**: zoptymalizowany pod kątem bibliotek
- **esbuild**: Niezwykle szybki pakiet JavaScript
- **Babel**: Transpilator JavaScript zapewniający kompatybilność wsteczną
- **PostCSS**: przetwarzanie CSS za pomocą wtyczek
### Struktury i biblioteki CSS
- **Bootstrap**: biblioteka komponentów, system gridowy, narzędzia
- **Tailwind CSS**: Framework CSS oparty na użyteczności
- **Materiałowy interfejs użytkownika**: implementacja Material Design firmy Google
- ** Interfejs czakry**: Dostępna biblioteka komponentów
- **Ant Design**: Komponenty interfejsu użytkownika na poziomie korporacyjnym
- **Komponenty stylizowane**: biblioteka CSS w JS
- **Emotion**: CSS w JS z mapami źródłowymi
## Rozwój backendu
### Języki po stronie serwera
#### Node.js
- **Środowisko wykonawcze**: JavaScript na serwerze (silnik V8)
- **Express.js**: Minimalny framework sieciowy, architektura oprogramowania pośredniego
- **NestJS**: architektura inspirowana Angularem, TypeScript
- **Fastify**: Struktura o wysokiej wydajności
- **Koa**: Modern Express autorstwa tych samych twórców
- **Zarządzanie pakietami**: npm, przędza, pnpm
#### Pythona
- **Django**: W pełni funkcjonalny framework, ORM, panel administracyjny, baterie w zestawie
- **Flask**: Mikroframework, ekosystem rozszerzeń
- **FastAPI**: Nowoczesna, asynchroniczna, automatyczna dokumentacja API
- **Piramida**: Elastyczna, skalowalna platforma
#### Inne języki backendu
- **Ruby on Rails**: Konwencja dotycząca konfiguracji, ActiveRecord ORM
- **Java Spring**: Framework dla przedsiębiorstw, wstrzykiwanie zależności
- **PHP Laravel**: Elegancka składnia, wymowny ORM, szablony Blade
- **Go Gin**: Wysoka wydajność, minimalne ramy
- **Rust Actix**: Bezpieczeństwo pamięci, wydajność
- **C# ASP.NET Core**: funkcje wieloplatformowe dla przedsiębiorstw
### Integracja z bazą danych
#### ORM (mapowanie obiektowo-relacyjne)
- **Sequelize**: Node.js ORM dla baz danych SQL
- **Prisma**: Dostęp do bazy danych bezpieczny dla typu, klient generowany automatycznie
- **SQLAlchemy**: zestaw narzędzi Python SQL i ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Hibernacja**: Java ORM
- **Entity Framework**: .NET ORM
#### Sterowniki bazy danych
- **pg**: Klient PostgreSQL dla Node.js
- **mysql2**: Klient MySQL z obietnicami
- **pymongo**: sterownik MongoDB dla Pythona
- **redis**: Klient Redis dla wielu języków
### Rozwój API
#### Interfejsy API REST
- **Metody HTTP**: GET, POST, PUT, PATCH, DELETE
- **Kody stanu**: 200, 201, 400, 401, 403, 404, 500
- **Nazewnictwo zasobów**: Rzeczowniki w liczbie mnogiej, hierarchiczne
- **Wersjonowanie**: ścieżka URL, nagłówki, parametry zapytania
- **Uwierzytelnianie**: JWT, OAuth, klucze API
- **Dokumentacja**: OpenAPI/Swagger, Listonosz
#### GraphQL
- **Definicja schematu**: Typy, zapytania, mutacje, subskrypcje
- **Resolwery**: Pobieranie danych na poziomie pola
- **Serwer Apollo**: Implementacja serwera GraphQL
- **Relay**: klient GraphQL Facebooka
- **Zalety**: Brak nadmiernego pobierania, pojedynczy punkt końcowy, mocne pisanie
#### gRPC
- **Bufory protokołów**: Język definicji interfejsu
- **HTTP/2**: Dwukierunkowe przesyłanie strumieniowe
- **Przypadki użycia**: komunikacja mikrousług, aplikacje czasu rzeczywistego
### Uwierzytelnianie i autoryzacja
- **Oparte na sesji**: pliki cookie, sesje po stronie serwera
- **Oparte na tokenach**: JWT (tokeny sieciowe JSON), bezstanowe
- **OAuth 2.0**: Struktura autoryzacji, logowanie przez stronę trzecią
- **OpenID Connect**: Warstwa tożsamości w OAuth 2.0
- **SAML**: Jednokrotne logowanie w przedsiębiorstwie
- **Haszowanie hasła**: bcrypt, argon2, scrypt
- **Uwierzytelnianie wieloskładnikowe**: TOTP, SMS, kody e-mail
## DevOps i wdrożenie
### Kontrola wersji
- **Git**: Rozproszona kontrola wersji
- **GitHub/GitLab/Bitbucket**: Hosting repozytorium
- **Strategie rozgałęziania**: Git Flow, GitHub Flow, rozwój oparty na magistrali
- **CI/CD**: Zautomatyzowane potoki testowania i wdrażania
### Konteneryzacja
- **Docker**: środowisko uruchomieniowe kontenera, plik Dockerfile, obrazy
- **Docker Compose**: Orkiestracja wielu kontenerów
- **Rejestry kontenerów**: Docker Hub, AWS ECR, Google GCR
- **Najlepsze praktyki**: Kompilacje wieloetapowe, minimalne obrazy podstawowe
### Orkiestracja
- **Kubernetes**: orkiestracja kontenerów, pody, usługi, wdrożenia
- **Helm**: Menedżer pakietów Kubernetes
- **Service Mesh**: Istio, Linkerd dla sieci mikrousług
### Platformy chmurowe
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Compute Engine, przechowywanie w chmurze, funkcje w chmurze, GKE
- **Azure**: maszyny wirtualne, magazyn obiektów Blob, funkcje, AKS
- **Vercel**: wdrożenie frontonu, funkcje bezserwerowe
- **Netlify**: hosting witryn statycznych, funkcje bezserwerowe
- **Heroku**: Platforma jako usługa (PaaS)
- **DigitalOcean**: Uproszczona infrastruktura chmurowa
### Rurociągi CI/CD
- **Akcje GitHub**: Automatyzacja przepływu pracy
- **GitLab CI**: Wbudowana ciągła integracja
- **Jenkins**: Rozszerzalny serwer automatyzacji
- **CircleCI**: CI/CD w chmurze
- **Travis CI**: Usługa ciągłej integracji
- **ArgoCD**: ciągłe dostarczanie GitOps dla Kubernetes
### Monitorowanie i rejestrowanie
- **Wydajność aplikacji**: New Relic, Datadog, AppDynamics
- **Śledzenie błędów**: Sentry, Rollbar, Bugsnag
- **Logowanie**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Monitorowanie czasu działania**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude
## Wydajność sieci
### Techniki optymalizacji
- **Podział kodu**: Leniwe ładowanie, dynamiczny import
- **Tree Shaking**: Usuwanie nieużywanego kodu
- **Minifikacja**: Zmniejszanie rozmiarów plików
- **Kompresja**: Gzip, Brotli
- **Buforowanie**: pamięć podręczna przeglądarki, CDN, pracownicy usług
- **Optymalizacja obrazu**: WebP, AVIF, leniwe ładowanie, responsywne obrazy
- **Krytyczny CSS**: Podkreślanie stylów strony widocznej na ekranie
- **Optymalizacja bazy danych**: Indeksowanie, optymalizacja zapytań, łączenie połączeń
### Podstawowe wskaźniki internetowe
- **LCP (największa farba zawierająca zawartość)**: Wydajność ładowania (<2,5 s)
- **FID (opóźnienie pierwszego wejścia)**: interaktywność (<100 ms)
- **CLS (skumulowane przesunięcie układu)**: stabilność wizualna (<0,1)
- **INP (interakcja z następną farbą)**: Wskaźnik reakcji
### Sieci dostarczania treści (CDN)
- **Cloudflare**: Bezpieczeństwo, wydajność, DNS
- **Akamai**: Korporacyjny CDN
- **Amazon CloudFront**: AWS CDN
- **Szybko**: platforma chmurowa Edge
- **StackPath**: Usługi brzegowe
## Bezpieczeństwo sieciowe
### Typowe luki w zabezpieczeniach (10 najlepszych OWASP)
- **Wstrzykiwanie**: Wstrzykiwanie SQL, wstrzykiwanie poleceń
- **Zerwane uwierzytelnianie**: przejmowanie sesji, upychanie poświadczeń
- **Narażenie wrażliwych danych**: Nieszyfrowane dane, słaba kryptografia
- **Elementy zewnętrzne XML (XXE)**: Luki w zabezpieczeniach analizatora XML
- **Zepsuta kontrola dostępu**: Eskalacja uprawnień, nieautoryzowany dostęp
- **Błędna konfiguracja zabezpieczeń**: Domyślne poświadczenia, szczegółowe błędy
- **Skrypty między witrynami (XSS)**: odzwierciedlone, przechowywane, oparte na DOM
- **Niebezpieczna deserializacja**: Ataki polegające na wstrzykiwaniu obiektów
- **Używanie komponentów ze znanymi lukami**: Nieaktualne zależności
- **Niewystarczające rejestrowanie i monitorowanie**: Niewykryte naruszenia
### Najlepsze praktyki dotyczące bezpieczeństwa
- **HTTPS**: szyfrowanie TLS/SSL, HSTS
- **Polityka bezpieczeństwa treści (CSP)**: Zapobiegaj atakom XSS
- **Weryfikacja danych wejściowych**: Oczyść dane wejściowe użytkownika
- **Kodowanie wyjściowe**: Zapobieganie atakom polegającym na wstrzykiwaniu
- **Ochrona CSRF**: tokeny anty-CSRF, pliki cookie SameSite
- **Ograniczenie szybkości**: Zapobiegaj atakom brutalnej siły
- **Nagłówki zabezpieczeń**: Opcje X-Frame, Opcje typu zawartości X
- **Skanowanie zależności**: audyt npm, Snyk, Depabot
## Testowanie
### Typy testowania
- **Testowanie jednostkowe**: Poszczególne komponenty/funkcje
- **Testowanie integracyjne**: Interakcje komponentów
- **Kompleksowy (E2E)**: Pełny przepływ pracy użytkownika
- **Regresja wizualna**: Wykrywanie zmian w interfejsie użytkownika
- **Testowanie wydajności**: Testowanie obciążenia, obciążenia, skoków
- **Testowanie dostępności**: Zgodność z WCAG
### Ramy testowania
- **Jest**: Framework do testowania JavaScript
- **Mocha**: Elastyczny biegacz testowy
- **pytest**: framework do testowania Pythona
- **ROSpec**: Framework testowania Ruby
- **JUnit**: środowisko testowania Java
### Narzędzia testowe E2E
- **Selenium**: Automatyzacja przeglądarki
- **Cypress**: Nowoczesne testy E2E
- ** Dramaturg**: Automatyzacja w różnych przeglądarkach
- **Lalkarz**: Bezgłowa kontrola Chrome
## Dostępność (a11y)
### Wytyczne WCAG
- **Dostrzegalne**: alternatywy tekstowe, podpisy, treść, którą można dostosować
- **Działa**: Nawigacja za pomocą klawiatury, wystarczający czas, brak napadów
- **Zrozumiały**: Czytelny, przewidywalny, pomoc przy wprowadzaniu danych
- **Wytrzymały**: Kompatybilny z technologiami wspomagającymi
### Implementacja
- **Semantyczny HTML**: Prawidłowa hierarchia nagłówków, punkty orientacyjne
- **Atrybuty ARIA**: Role, stany, właściwości
- **Zarządzanie fokusem**: Widoczne wskaźniki skupienia, logiczna kolejność zakładek
- **Kontrast kolorów**: Minimalny współczynnik tekstu 4,5:1
- **Testowanie czytnika ekranu**: NVDA, JAWS, VoiceOver
- **Nawigacja za pomocą klawiatury**: Dostępne są wszystkie elementy interaktywne
## Progresywne aplikacje internetowe (PWA)
### Funkcje PWA
- **Service Workers**: funkcjonalność offline, synchronizacja w tle
- **Manifest aplikacji internetowej**: monit o instalację, ikony i kolory motywu
- **Powłoka aplikacji**: Szkielet interfejsu użytkownika w pamięci podręcznej
- **Powiadomienia push**: zaangażowanie użytkowników
- **Responsywny projekt**: Działa na wszystkich urządzeniach
- **Wymagany protokół HTTPS**: bezpieczny kontekst
### Narzędzia
- **Workbox**: Biblioteki Service Worker
- **Latarnia morska**: Audyt PWA
- **PWA Builder**: Generuj manifesty i ikony
## Nowe technologie
### Zespół sieciowy (Wasm)
- **Cel**: Uruchomienie skompilowanego kodu w przeglądarce z prędkością bliską natywnej
- **Języki**: C++, Rust, cele kompilacji Go
- **Przypadki użycia**: gry, edycja wideo, kryptografia, wnioskowanie ML
### Architektura bezserwerowa
- **Funkcje jako usługa**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Korzyści**: Brak zarządzania serwerem, automatyczne skalowanie, płatność za użycie
- **Rozważania**: Zimny start, uzależnienie od dostawcy, złożoność debugowania
### Architektura Jamstack
- **JavaScript**: Interakcja po stronie klienta
- **API**: funkcje bezserwerowe, usługi innych firm
- **Znacznik**: Gotowe pliki statyczne
- **Narzędzia**: Next.js, Gatsby, Hugo, Eleventy
- **Korzyści**: Wydajność, bezpieczeństwo, skalowalność, doświadczenie programisty
### Komunikacja w czasie rzeczywistym
- **WebSockets**: Komunikacja dwukierunkowa
- **Zdarzenia wysyłane przez serwer**: Przesyłanie strumieniowe z serwera do klienta
- **WebRTC**: wideo, audio i dane typu peer-to-peer
- **Przypadki użycia**: Czat, współpraca, transmisja na żywo, gry
### Mikronakładki
- **Koncepcja**: Rozszerzenie mikrousług na frontend
- **Podejścia**: integracja w czasie kompilacji, w czasie wykonywania, po stronie brzegowej
- **Korzyści**: Niezależne wdrożenia, autonomia zespołu
- **Wyzwania**: Spójność, wydajność, złożoność