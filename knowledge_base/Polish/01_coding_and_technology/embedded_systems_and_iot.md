---
# Metadata
title: "Embedded Systems and IoT"
description: "Microcontrollers, sensors, RTOS, IoT protocols, edge computing"
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
tags: [embedded, systems, iot, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Systemy wbudowane i IoT
Systemy wbudowane to komputery ukryte w innych urządzeniach – sterowniku silnika w samochodzie, sterowniku pralki, mikrokontrolerze w inteligentnym termostacie. W przeciwieństwie do komputerów ogólnego przeznaczenia, są one przeznaczone do określonych zadań, często z dużymi ograniczeniami dotyczącymi mocy, pamięci i szybkości przetwarzania. Internet rzeczy (IoT) rozszerza systemy wbudowane, łącząc je z sieciami, umożliwiając zdalne monitorowanie, kontrolę i gromadzenie danych. Razem reprezentują miliardy urządzeń komputerowych, które wchodzą w interakcję ze światem fizycznym.
---

## Podstawy systemów wbudowanych
### Co wyróżnia rozwiązania osadzone
| Aspekt | Komputer ogólnego przeznaczenia | System wbudowany |
|--------|----------------------------|--------------------------------|
| **Cel** | Uruchom dowolne oprogramowanie | Wykonaj określone zadania |
| **Zasoby** | Obfity procesor, pamięć RAM, pamięć | Ograniczone (KB do MB pamięci RAM; MHz do niskiego GHz) |
| **Moc** | Podłączony lub duży akumulator | Często zasilane bateryjnie lub zbierające energię |
| **System operacyjny** | Pełny system operacyjny (Windows, Linux, macOS) | RTOS, bare-metal lub wbudowany Linux |
| **Interfejs użytkownika** | Rich (ekran, klawiatura, mysz) | Minimalne (diody LED, przyciski, czujniki) lub żadne |
| **W czasie rzeczywistym** | Najlepszy wysiłek | Często trudne terminy w czasie rzeczywistym |
| **Dożywotnie** | 3-7 lat | 10-25+ lat |
### Mikrokontrolery kontra mikroprocesory
| Funkcja | Mikrokontroler (MCU) | Mikroprocesor (MPU) |
|--------|----------------------|--------------------------------------|
| **Integracja** | Procesor + RAM + Flash + urządzenia peryferyjne na jednym chipie | Tylko procesor; zewnętrzna pamięć RAM i pamięć |
| **Wydajność** | Niski do umiarkowanego (zakres MHz) | Wysoka (zakres GHz) |
| **Moc** | Bardzo niski (µA do mA) | Wyższa (setki mA do amperów) |
| **Koszt** | 0,10 USD - 10 USD | 5 dolarów - 100 dolarów + |
| **Przykłady** | STM32, ESP32, Arduino (ATmega), nRF52 | Raspberry Pi (BCM2835), i.MX, Allwinner |
| **Przypadek użycia** | Czujniki, elementy wykonawcze, proste sterowanie | Wyświetlacze, złożone przetwarzanie, Linux |
---

## Wspólne platformy wbudowane
| Platforma | MCU/MPU | Kluczowa funkcja | Najlepsze dla |
|---------|---------|-------------|--------------|
| **Arduino** | ATmega328P (i inne) | Prosty; ogromna społeczność | Nauka; prototypowanie |
| **ESP32** | Dwurdzeniowy Espressif | Wi-Fi + Bluetooth; niski koszt | projekty IoT; podłączone urządzenia |
| **Malinowe Pico** | RP2040 (dwurdzeniowy ARM) | Przystępny; Obsługa MicroPythona | Edukacja; projekty hobbystyczne |
| **STM32** | Seria ARM Cortex-M | klasa przemysłowa; szeroki zakres | Profesjonalny osadzony; przemysłowy |
| **nRF52/nRF53** | Nordycki półprzewodnik | Specjalista Bluetooth Low Energy | Urządzenia do noszenia; latarnie |
| **Malinowe Pi** | Broadcom BCM (ARM) | Pełny Linux; Piny GPIO | Prototypowanie; centra medialne; lekkie przetwarzanie brzegowe |
| **Kość Beagle** | TI Sitara (ARM) | Rdzenie PRU w czasie rzeczywistym | Przemysłowy; aplikacje czasu rzeczywistego |
| **ESP32-S3** | Espressif | Przyspieszenie AI; USB | Krawędziowa sztuczna inteligencja; aplikacje wizyjne |
---

## Systemy operacyjne czasu rzeczywistego (RTOS)
RTOS gwarantuje, że krytyczne zadania zostaną ukończone w określonym oknie czasowym.
| RTOS | Licencja | Najlepsze dla |
|------|---------|--------------|
| **BezpłatnyRTOS** | MIT | Najczęściej; szeroka obsługa MCU |
| **Zefir** | Apache 2.0 | Nowoczesny; Fundacja Linuksa; rosnący ekosystem |
| **ThreadX (Azure RTOS)** | MIT | Certyfikat bezpieczeństwa; Internet Rzeczy |
| **embOS** | Komercyjne | Przemysłowy; certyfikowany |
| **Wątek RT** | Apache 2.0 | chiński ekosystem; rośnie na całym świecie |
### RTOS kontra Bare Metal
| Aspekt | Goły metal | RTOS |
|--------|-----------|------|
| **Złożoność** | Proste do prostych zadań | Potrzebne do złożonych, współbieżnych zadań |
| **Planowanie** | Ręczny (pętla główna + przerwania) | Planowanie wyprzedzające z priorytetami |
| **Skalowalność** | Trudno dodać funkcje | Łatwe dodawanie zadań |
| **Pamięć** | Minimalne koszty ogólne | Mały narzut (kilka KB) |
---

## Protokoły komunikacyjne
### Protokoły przewodowe
| Protokół | Prędkość | Odległość | Przypadek użycia |
|----------|-------|----------|----------|
| **UART** | Do 1 Mb/s | Krótki (na pokładzie) | Konsola debugowania; GPS modules |
| **SPI** | Do 100 MHz | Krótki (na pokładzie) | High-speed peripherals (displays, flash) |
| **I²C** | Do 3,4 MHz | Short (on-board) | Czujniki; low-pin-count communication |
| **MOŻE** | Up to 1 Mbps | Do 1 km | Automobilowy; przemysłowy |
| **Ethernet** | 10 Mbps - 100 Gbps | Up to 100 m | Networking; industrial (with extensions) |
| **USB** | Do 40 Gb/s (USB4) | Up to 5 m | Peripherals; charging |
### Protokoły bezprzewodowe
| Protokół | Zakres | Moc | Prędkość | Przypadek użycia |
|--------------|-------|-------|-------|--------------|
| **Wi-Fi** | ~100 m | Wysoki | Do Wi-Fi 7 (teoretycznie 46 Gb/s) | Internet rzeczy o dużej przepustowości; przesyłanie strumieniowe |
| **Bluetooth Classic** | ~100 m | Średni | 1-3 Mb/s | Audio; file transfer |
| **BLE** (Bluetooth o niskim zużyciu energii) | ~100 m | Very low | 1-2 Mb/s | Urządzenia do noszenia; latarnie; sensors |
| **Zigbee** | ~100 m (mesh) | Niski | 250 kbps | Automatyka domowa; industrial sensors |
| **Z-Wave** | ~100 m (mesh) | Niski | 100 kbps | Home automation |
| **LoRa / LoRaWAN** | Do 15 km | Very low | 0.3-50 kbps | Rolnictwo; utilities; czujniki ogólnomiejskie |
| **NB-IoT** | Zasięg komórkowy | Niski | 250 kbps | Dozowanie; śledzenie aktywów |
| **Wątek / Materia** | ~100 m (siatka) | Niski | Umiarkowany | Inteligentny dom (Apple, Google, Amazon) |
| **Komórkowa (4G/5G)** | Globalny | Wysoki | Wysoki | Połączone pojazdy; zdalne monitorowanie |
---

## Architektura IoT
### Stos IoT
| Warstwa | Funkcja | Przykłady |
|-------|----------|--------|
| **Urządzenia** | Czujniki, elementy wykonawcze, mikrokontrolery | ESP32, STM32, Raspberry Pi |
| **Łączność** | Protokoły sieciowe | MQTT, HTTP, CoAP, LoRaWAN |
| **Przetwarzanie brzegowe** | Przetwarzanie w pobliżu urządzenia | AWS Greengrass, Azure IoT Edge |
| **Platforma chmurowa** | Pozyskiwanie, przechowywanie, przetwarzanie danych | AWS IoT, Azure IoT Hub, Google Cloud IoT |
| **Aplikacja** | Panele, analityka, alerty | Grafana, niestandardowe aplikacje internetowe |
### Protokoły komunikacyjne IoT
| Protokół | Wzór | Najlepsze dla |
|---------|---------|---------|
| **MQTT** | Publikuj/subskrybuj; lekki | Większość aplikacji IoT; niska przepustowość |
| **HTTP/REST** | Prośba/odpowiedź | Kiedy liczy się prostota; integracja z siecią |
| **CoAP** | Żądanie/odpowiedź; oparty na UDP | Urządzenia ograniczone; mała moc |
| **AMQP** | Kolejkowanie wiadomości | Internet Rzeczy w przedsiębiorstwie; niezawodna dostawa |
| **WebSocket** | Dwukierunkowy; trwałe połączenie | Pulpity nawigacyjne w czasie rzeczywistym; dane na żywo |
### Szczegóły MQTT
| Koncepcja | Opis |
|--------|------------|
| **Broker** | Centralny serwer kierujący wiadomości (Mosquitto, EMQX, HiveMQ) |
| **Temat** | Adres hierarchiczny (np.`home/living-room/temperature`) |
| **Jakość usług** | 0 (najwyżej raz), 1 (przynajmniej raz), 2 (dokładnie raz) |
| **Zatrzymana wiadomość** | Ostatnia wiadomość na dany temat; dostarczony do nowych abonentów |
| **Ostatnia wola** | Wiadomość opublikowana w przypadku nieoczekiwanego rozłączenia klienta |
---

## Przetwarzanie brzegowe
Przetwarzanie danych blisko źródła zamiast wysyłania wszystkiego do chmury.
| Korzyści | Opis |
|--------|------------|
| **Zmniejszone opóźnienie** | Żadnej podróży w obie strony do chmury; natychmiastowe decyzje |
| **Oszczędność przepustowości** | Wysyłaj tylko podsumowania lub anomalie |
| **Prywatność** | Wrażliwe dane pozostają lokalnie |
| **Niezawodność** | Działa, gdy internet nie działa |
| Platforma | Opis |
|--------------|------------|
| **AWS Zielona trawa** | Uruchom funkcje Lambda na urządzeniach brzegowych |
| **Azure IoT Edge** | Uruchamiaj kontenery na urządzeniach brzegowych |
| **NVIDIA Jetson** | Akcelerowana przez GPU krawędziowa sztuczna inteligencja (Orin, Nano) |
| **Malinowe Pi** | Lekkie przetwarzanie brzegowe |
---

## Aktualizacja oprogramowania sprzętowego (OTA)
Aktualizacje bezprzewodowe umożliwiają naprawianie błędów i dodawanie funkcji do wdrożonych urządzeń.
| Obawa | Rozwiązanie |
|--------|----------|
| **Niezawodność** | Dwubankowa lampa błyskowa; wycofanie w przypadku niepowodzenia |
| **Bezpieczeństwo** | Podpisane obrazy; szyfrowane przelewy |
| **Rozmiar** | Aktualizacje Delta (tylko zmienione fragmenty) |
| **Łączność** | Aktualizacje kolejki, gdy urządzenie przejdzie w tryb online |
---

## Systemy wbudowane o krytycznym znaczeniu dla bezpieczeństwa
| Domena | Standardy | Przykłady |
|--------|-----------|--------|
| **Motoryzacja** | ISO 26262 (ASIL A-D) | Sterowanie silnikiem, hamowanie, poduszki powietrzne |
| **Medyczne** | IEC 62304 | Rozruszniki serca, pompy infuzyjne |
| **Przestrzeń kosmiczna** | DO-178C (DAL A–E) | Sterowanie lotem, nawigacja |
| **Przemysłowe** | IEC 61508 (SIL 1-4) | sterowniki PLC, sterowniki bezpieczeństwa |
| **Kolej** | EN 50128 (SIL 1-4) | Sygnalizacja, kontrola pociągu |
---

## Narzędzia i rozwój
| Narzędzie | Cel |
|------|-------------|
| **PlatformaIO** | Wieloplatformowy rozwój wbudowany (Arduino, ESP32, STM32) |
| **STM32CubeIDE** | Oficjalne IDE ST dla STM32 |
| **ArduinoIDE** | Prosty rozwój dla Arduino i kompatybilnych płytek |
| **ESP-IDF** | Oficjalny zestaw SDK firmy Espressif dla ESP32 |
| **zephyr SDK** | System kompilacji Westa dla Zephyr RTOS |
| **OpenOCD** | Debugowanie na chipie |
| **Analizator logiczny** | Debugowanie protokołów SPI, I²C, UART |
| **Wireshark** | Analiza protokołu sieciowego |
---

## Streszczenie
Systemy wbudowane i IoT stanowią skrzyżowanie oprogramowania i świata fizycznego. Od mikrokontrolerów sterujących silnikami po sieci czujników połączone z chmurą — wymagają one innego sposobu myślenia niż tworzenie stron internetowych lub aplikacji: ograniczone zasoby, wymagania w czasie rzeczywistym, długi czas życia i konsekwencje błędów w świecie fizycznym. Ekosystem ogromnie się rozwinął — platformy takie jak ESP-IDF i Zephyr umożliwiają rozwój zawodowy, a platformy takie jak AWS IoT i Azure IoT Hub obsługują chmurę. Kluczowe umiejętności to zrozumienie interfejsów sprzętowych, protokołów komunikacyjnych, zarządzanie energią i dyscyplina w pisaniu oprogramowania, które musi działać niezawodnie przez lata bez interwencji.