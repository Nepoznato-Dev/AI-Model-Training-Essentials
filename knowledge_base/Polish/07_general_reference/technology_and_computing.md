---
# Metadata
title: "Technology and Computing"
description: "Computing basics, internet, databases, cloud, security"
category: "General Reference"
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
reviewed_by: "General Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, computing, general-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Technologia i informatyka
Komputery są wszędzie — w telefonie, samochodzie, lodówce, urządzeniach medycznych i infrastrukturze, na której opiera się współczesne społeczeństwo. Nie musisz być programistą, aby czerpać korzyści ze zrozumienia, jak to wszystko działa. W tym pliku omówiono podstawy: czym jest komputer, jak działa Internet, jak zbudowane jest oprogramowanie i koncepcje kształtujące cyfrowy świat.
> **Chcesz zejść głębiej?** Ten plik zawiera ogólny przegląd. Aby uzyskać szczegółowe omówienie dowolnego tematu, zobacz dedykowane pliki w[`01_coding_and_technology/`](../01_coding_and_technology/)— w tym [database systems](../01_coding_and_technology/database_systems.md), [cloud architecture](../01_coding_and_technology/cloud_architecture.md),[networking](../01_coding_and_technology/networking_basics.md)i.
---

## Co to jest komputer?
W swej istocie każdy komputer — od smartfona po superkomputer — robi to samo: pobiera dane wejściowe, przetwarza je zgodnie z instrukcjami (program) i generuje dane wyjściowe. Magia tkwi w szybkości i skali.
### Architektura von Neumanna
Prawie wszystkie nowoczesne komputery mają tę podstawową konstrukcję:
| Składnik | Co to robi | Analogia |
|---------------|------------|--------|
| **CPU** (jednostka centralna) | Wykonuje instrukcje; „mózg” | Szef kuchni według przepisu |
| **RAM** (pamięć) | Przechowuje dane, z których aktywnie korzysta procesor; utracone po wyłączeniu zasilania | Blat — szybki dostęp, ograniczona przestrzeń |
| **Pamięć** (SSD/HDD) | Przechowuje dane trwale | Spiżarnia — wolniejszy dostęp, dużo więcej miejsca |
| **Wejście/Wyjście** | Klawiatura, mysz, ekran, sieć | Jak szef kuchni przyjmuje zamówienia i dostarcza jedzenie |
| **GPU** (jednostka przetwarzania grafiki) | Specjalistyczny procesor do zadań równoległych (grafika, AI) | Zespół asystentów wykonujących to samo zadanie jednocześnie |
**Kluczowy wniosek**: pamięć RAM jest szybka, ale tymczasowa. Przechowywanie jest powolne, ale trwałe. Kiedy komputer „wydaje się powolny”, często dzieje się tak dlatego, że kończy mu się pamięć RAM i musi używać pamięci jako pamięci tymczasowej (wymienianie), co jest znacznie wolniejsze.
---

## Języki programowania — rozmowa z komputerami
Język programowania to zestaw instrukcji, które może wykonać komputer. Różne języki są przeznaczone do różnych celów. Szczegółowe informacje na temat 34 poszczególnych języków można znaleźć w folderze [`programming_languages/`](../01_coding_and_technology/programming_languages/).
| Język | Najlepsze dla | Dlaczego to wybrać |
|---------|---------|--------------|
| **Pyton** | Analityka danych, sztuczna inteligencja, automatyzacja, backendy internetowe | Prosta składnia; ogromny ekosystem; świetne dla początkujących |
| **JavaScript** | Frontendy internetowe, full-stack (Node.js) | Działa w każdej przeglądarce; niezbędne do tworzenia stron internetowych |
| **Java** | Oprogramowanie dla przedsiębiorstw, aplikacje na Androida | Niezależny od platformy (JVM); duży ekosystem |
| **C/C++** | Programowanie systemów, gry, wbudowane | Maksymalna wydajność; bezpośrednia kontrola sprzętu |
| **Rdza** | Programowanie systemów z gwarancją bezpieczeństwa | Bezpieczeństwo pamięci bez usuwania śmieci |
| **Idź** | Usługi chmurowe, mikroserwisy, narzędzia CLI | Prosty; doskonała współbieżność; szybka kompilacja |
| **SQL** | Zapytania do bazy danych | Uniwersalny język pracy z danymi |
| **Maszynopis** | Wielkoskalowe aplikacje internetowe | JavaScript ze sprawdzaniem typów; wcześnie łapie błędy |
---

## Jak działa Internet
Internet to nie to samo co sieć. Internet to sieć fizyczna — kable, routery, serwery i protokoły łączące miliardy urządzeń. Sieć WWW to jedna usługa działająca w Internecie (wraz z pocztą elektroniczną, przesyłaniem plików, transmisją strumieniową, grami itp.).
### Podróż żądania internetowego
Po wpisaniu`https://www.example.com`w przeglądarce:
1. **Wyszukiwanie DNS**: Twoja przeglądarka prosi serwer DNS o przetłumaczenie „www.example.com” na adres IP (np. 93.184.216.34).
2. **Połączenie TCP**: Twoje urządzenie nawiązuje połączenie z tym adresem IP przy użyciu protokołu TCP (protokół gwarantujący niezawodne dostarczanie).
3. **Uzgadnianie TLS**: Jeśli korzystasz z protokołu HTTPS, Twoja przeglądarka i serwer negocjują szyfrowane połączenie.
4. **Żądanie HTTP**: Twoja przeglądarka wysyła żądanie: „Podaj mi stronę /index.html”.
5. **Przetwarzanie serwera**: Serwer WWW odnajduje stronę, ewentualnie wysyła zapytanie do bazy danych i przygotowuje odpowiedź.
6. **Odpowiedź HTTP**: Serwer odsyła HTML, CSS i JavaScript.
7. **Renderowanie**: Twoja przeglądarka analizuje kod HTML, stosuje style CSS i wykonuje JavaScript w celu wyświetlenia strony.
Cały ten proces trwa zwykle mniej niż sekundę.
### Kluczowe protokoły
| Protokół | Co to robi | Warstwa |
|---------|------------|-------|
| **IP** (protokół internetowy) | Trasuje pakiety pomiędzy sieciami | Sieć |
| **TCP** | Niezawodna, uporządkowana dostawa (retransmisja utraconych pakietów) | Transport |
| **UDP** | Szybka, zawodna dostawa (bez retransmisji) | Transport |
| **HTTP/HTTPS** | Transfer strony internetowej (HTTPS dodaje szyfrowanie) | Aplikacja |
| **DNS** | Tłumaczy nazwy domen na adresy IP | Aplikacja |
| **SSH** | Bezpieczny zdalny dostęp do komputerów | Aplikacja |
| **SMTP/IMAP** | Wysyłanie i odbieranie wiadomości e-mail | Aplikacja |
---

## Tworzenie oprogramowania — jak powstają programy
### Proces rozwoju
1. **Napisz kod**: Programiści piszą instrukcje w języku programowania.
2. **Kod testowy**: Uruchom kod, aby sprawdzić, czy działa poprawnie.
3. **Kontrola wersji**: Śledź zmiany za pomocą Git – uniwersalnego standardu.
4. **Recenzja**: Inni programiści sprawdzają kod pod kątem błędów i jakości.
5. **Buduj**: Konwertuj kod źródłowy na uruchamialny program (kompilacja).
6. **Wdrożenie**: udostępnienie programu użytkownikom (serwerom, sklepom z aplikacjami itp.).
7. **Monitor**: Obserwuj błędy i problemy z wydajnością w środowisku produkcyjnym.
### Kluczowe pojęcia
| Koncepcja | Co to znaczy | Dlaczego to ma znaczenie |
|--------|--------------|----------------|
| **Kontrola wersji (Git)** | Śledź każdą zmianę w kodzie w czasie | Współpraca; zdolność do cofania błędów |
| **API** (interfejs programowania aplikacji) | Zdefiniowany sposób komunikacji komponentów oprogramowania | Umożliwia współpracę różnych systemów |
| **Baza danych** | Zorganizowane przechowywanie danych | Każda aplikacja musi przechowywać i pobierać dane |
| **Testowanie** | Automatyczne sprawdza, czy kod działa poprawnie | Zapobiega przedostawaniu się błędów do użytkowników |
| **CI/CD** (Ciągła integracja/dostawa) | Zautomatyzowany potok od zatwierdzenia kodu do produkcji | Szybsze, bezpieczniejsze wydania |
| **Konteneryzacja (Docker)** | Spakuj aplikację ze wszystkimi jej zależnościami | „Działa na moim komputerze” zmienia się na „działa wszędzie” |
---

## Bazy danych — miejsce przechowywania danych
Każda aplikacja musi przechowywać dane. Bazy danych to systemy, które robią to skutecznie i niezawodnie.
| Wpisz | Jak dane są przechowywane | Najlepsze dla | Przykłady |
|------|---------|----------|---------|
| **Relacyjny (SQL)** | Tabele z wierszami i kolumnami; ścisły schemat | Dane strukturalne; złożone zapytania; transakcje | PostgreSQL, MySQL, SQLite |
| **Dokument (NoSQL)** | dokumenty typu JSON; elastyczny schemat | Dane częściowo ustrukturyzowane; szybka iteracja | MongoDB, CouchDB |
| **Klucz-wartość** | Prosty klucz → pary wartości | Buforowanie; przechowywanie sesji; szybkie wyszukiwania | Redis, DynamoDB |
| **Wykres** | Węzły i krawędzie (relacje) | Sieci społecznościowe; silniki rekomendacji | Neo4j, JanusGraph |
| **Szereg czasowy** | Zoptymalizowany pod kątem danych ze znacznikiem czasu | Monitorowanie; analityka; Internet Rzeczy | InfluxDB, TimescaleDB |
**SQL** (Structured Query Language) to standardowy język relacyjnych baz danych. To jedna z najcenniejszych umiejętności technicznych, jakich możesz się nauczyć — prawie każda organizacja korzysta z baz danych, a SQL to sposób, w jaki z nimi rozmawiasz.
---

## Systemy operacyjne
System operacyjny (OS) to warstwa oprogramowania pomiędzy Tobą (i Twoimi programami) a sprzętem. Zarządza pamięcią, procesami, plikami i urządzeniami.
| system operacyjny | Gdzie dominuje | Kluczowa funkcja |
|--------|-----|------------|
| **Okna** | Komputery stacjonarne/laptopy (~72% udziału w rynku) | Najszersza kompatybilność oprogramowania/sprzętu |
| **macOS** | Kreatywni profesjonaliści, programiści | Oparty na systemie Unix; dopracowany interfejs użytkownika; Ekosystem jabłkowy |
| **Linux** | Serwery (~96%), superkomputery (100%), wbudowane, programiści | Otwarte źródło; bezpłatny; niezwykle konfigurowalny |
| **Android** | Urządzenia mobilne (~72% udziału w rynku światowym) | Oparty na jądrze Linuksa; otwarte źródło |
| **iOS** | Urządzenia mobilne (~27% globalnie, ale wyższe przychody) | Zamknięty ekosystem; błyszczący; zorientowany na prywatność |
Linux zasługuje na szczególną wzmiankę: obsługuje większość Internetu, każdy superkomputer z 500 najlepszych, większość infrastruktury chmurowej i wszystkie telefony z Androidem. Jest darmowy, open source i utrzymywany przez globalną społeczność.
---

## Przetwarzanie w chmurze
Przetwarzanie w chmurze oznacza wynajmowanie zasobów obliczeniowych (serwerów, pamięci masowej, baz danych itp.) przez Internet zamiast kupować i konserwować własny sprzęt. Obszerny przewodnik po architekturze chmury, modelach usług i porównaniach dostawców można znaleźć w artykule[cloud architecture](../01_coding_and_technology/cloud_architecture.md).
| Model usługi | Co dostajesz | Analogia | Przykłady |
|--------------|-------------|---------|-------------|
| **IaaS** (Infrastruktura) | Serwery wirtualne, pamięć masowa, sieci | Wynajmij działkę i buduj co chcesz | AWS EC2, Google Compute Engine |
| **PaaS** (platforma) | Środowisko wykonawcze; przynosisz kod | Wynajem umeblowanego mieszkania | Heroku, silnik aplikacji Google |
| **SaaS** (oprogramowanie) | Kompletna aplikacja; po prostu go używasz | Pobyt w hotelu | Gmail, Slack, Salesforce |
Trzej główni dostawcy usług w chmurze to **AWS** (Amazon, ~32% udziału w rynku), **Azure** (Microsoft, ~23%) i **GCP** (Google, ~10%). Oferują setki usług obejmujących obliczenia, pamięć masową, bazy danych, sztuczną inteligencję, sieci i nie tylko.
---

## Cyberbezpieczeństwo — ochrona systemów cyfrowych
Cyberbezpieczeństwo to praktyka polegająca na ochronie komputerów, sieci i danych przed atakiem. Ma to znaczenie, ponieważ wszystko jest ze sobą połączone, a koszty naruszeń są ogromne. Aby zapoznać się z pełnym przewodnikiem dotyczącym 10 najlepszych rozwiązań OWASP, bezpiecznego cyklu życia oprogramowania i zarządzania wpisami tajnymi, zobacz.
### Typowe zagrożenia
| Zagrożenie | Co to jest | Zapobieganie |
|------------|-----------|------------|
| **Złośliwe oprogramowanie** | Złośliwe oprogramowanie (wirusy, robaki, trojany) | program antywirusowy; aktualizuj oprogramowanie |
| **Wyłudzanie informacji** | Fałszywe e-maile/wiadomości nakłaniające Cię do ujawnienia informacji | Szkolenie; filtrowanie poczty elektronicznej; sceptycyzm |
| **Oprogramowanie ransomowe** | Szyfruje Twoje dane; żąda zapłaty za klucz | Kopie zapasowe; systemy poprawek; nie płać |
| **DDoS** | Przytłacza usługę ruchem | Filtrowanie ruchu; Ochrona CDN |
| **Wstrzyknięcie SQL** | Wstawianie złośliwego kodu SQL do pól wejściowych | Zapytania parametryczne; walidacja danych wejściowych |
| **Człowiek pośrodku** | Przechwytywanie komunikacji pomiędzy dwiema stronami | Szyfrowanie HTTPS/TLS |
### Podstawy bezpieczeństwa
- **Szyfrowanie**: Szyfruj dane, aby tylko upoważnione osoby mogły je odczytać. HTTPS wykorzystuje TLS do szyfrowania ruchu internetowego.
- **Uwierzytelnianie**: Zweryfikuj tożsamość. Użyj uwierzytelniania wieloskładnikowego (MFA) — hasło + coś innego (kod, biometryczny).
- **Autoryzacja**: Sprawdź uprawnienia. To, że jesteś zalogowany, nie oznacza, że ​​masz dostęp do wszystkiego.
- **Zasada najmniejszych uprawnień**: Daj użytkownikom i systemom tylko taki dostęp, jakiego potrzebują, nic więcej.
- **Zarządzanie poprawkami**: Aktualizuj oprogramowanie. Większość naruszeń wykorzystuje znane luki, które mają już poprawki.
---

##Formaty danych
Programy wymieniają dane w określonych formatach. Najczęstsze:
| Formatuj | Struktura | Używany do |
|--------|-----------|---------|
| **JSON** | Pary klucz-wartość; czytelny dla człowieka | Pszczoła; konfiguracja; wymiana danych |
| **XML** | Oparte na tagach; gadatliwy, ale elastyczny | Starsze systemy; dokumenty; Interfejsy SOAP |
| **YAML** | Oparte na wcięciach; bardzo czytelny | Konfiguracja (Docker, Kubernetes, CI/CD) |
| **CSV** | Zwykłe wiersze i kolumny tekstu | Import/eksport danych; arkusze kalkulacyjne |
---

## Streszczenie
Informatyka to nie magia – to inżynieria. Komputery wykonują instrukcje z niewiarygodną szybkością. Internet łączy ich miliardy za pomocą standardowych protokołów. Oprogramowanie jest tworzone przez zespoły ludzi piszących, testujących i wdrażających kod w cyklach iteracyjnych. Bazy danych przechowują i pobierają dane. Przetwarzanie w chmurze umożliwia każdemu dostęp na żądanie do ogromnych zasobów obliczeniowych. Cyberbezpieczeństwo to ciągła walka o ochronę tego wszystkiego przed ludźmi, którzy chcą je wykorzystać. Zrozumienie tych podstaw pomoże Ci poruszać się po cyfrowym świecie — niezależnie od tego, czy jesteś użytkownikiem, programistą, czy po prostu osobą próbującą zrozumieć technologię, która kształtuje współczesne życie.