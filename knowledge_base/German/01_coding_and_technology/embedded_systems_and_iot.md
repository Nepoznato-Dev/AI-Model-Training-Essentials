<!--
---
# Metadata
title: "Embedded Systems and IoT"
description: "Microcontrollers, sensors, RTOS, IoT protocols, edge computing"
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

-->
# Eingebettete Systeme und IoT
Eingebettete Systeme sind Computer, die in anderen Geräten versteckt sind – dem Motorsteuergerät Ihres Autos, dem Controller Ihrer Waschmaschine, dem Mikrocontroller in einem intelligenten Thermostat. Im Gegensatz zu Allzweckcomputern sind sie für bestimmte Aufgaben konzipiert, oft mit strengen Einschränkungen hinsichtlich Leistung, Speicher und Verarbeitungsgeschwindigkeit. Das Internet der Dinge (IoT) erweitert eingebettete Systeme, indem es sie mit Netzwerken verbindet und so Fernüberwachung, Steuerung und Datenerfassung ermöglicht. Zusammen stellen sie Milliarden von Computergeräten dar, die mit der physischen Welt interagieren.
---

## Grundlagen eingebetteter Systeme
### Was Embedded anders macht
| Aspekt | Allzweckcomputer | Eingebettetes System |
|--------|---------|-----------------|
| **Zweck** | Führen Sie eine beliebige Software aus | Bestimmte Aufgaben ausführen |
| **Ressourcen** | Reichlich CPU, RAM, Speicher | Begrenzt (KB bis MB RAM; MHz bis niedriges GHz) |
| **Leistung** | Eingesteckt oder großer Akku | Oft batteriebetrieben oder Energy-Harvesting |
| **Betriebssystem** | Vollständiges Betriebssystem (Windows, Linux, macOS) | RTOS, Bare-Metal oder eingebettetes Linux |
| **Benutzeroberfläche** | Rich (Bildschirm, Tastatur, Maus) | Minimal (LEDs, Tasten, Sensoren) oder keine |
| **Echtzeit** | Best-effort | Oft schwierige Echtzeitfristen |
| **Lebenslang** | 3-7 Jahre | 10-25+ Jahre |
### Mikrocontroller vs. Mikroprozessoren
| Funktion | Mikrocontroller (MCU) | Mikroprozessor (MPU) |
|---------|--------|---------------------|
| **Integration** | CPU + RAM + Flash + Peripherie auf einem Chip | Nur CPU; externer RAM und Speicher |
| **Leistung** | Niedrig bis mäßig (MHz-Bereich) | Hoch (GHz-Bereich) |
| **Leistung** | Sehr niedrig (µA zu mA) | Höher (Hunderte von mA zu Ampere) |
| **Kosten** | 0,10 $ - 10 $ | 5 $ - 100 $+ |
| **Beispiele** | STM32, ESP32, Arduino (ATmega), nRF52 | Raspberry Pi (BCM2835), i.MX, Allwinner |
| **Anwendungsfall** | Sensoren, Aktoren, einfache Steuerung | Anzeigen, komplexe Verarbeitung, Linux |
---

## Gängige eingebettete Plattformen
| Plattform | MCU/MPU | Hauptmerkmal | Am besten für |
|----------|---------|-------------|----------|
| **Arduino** | ATmega328P (und andere) | Einfach; riesige Community | Lernen; Prototyping |
| **ESP32** | Espressif Dual-Core | WLAN + Bluetooth; niedrige Kosten | IoT-Projekte; angeschlossene Geräte |
| **Raspberry Pi Pico** | RP2040 (Dual-Core-ARM) | Erschwinglich; MicroPython-Unterstützung | Ausbildung; Hobbyprojekte |
| **STM32** | ARM Cortex-M-Serie | Industriequalität; breites Sortiment | Professionell eingebettet; industriell |
| **nRF52/nRF53** | Nordic Semiconductor | Spezialist für Bluetooth Low Energy | Wearables; Leuchtfeuer |
| **Himbeer-Pi** | Broadcom BCM (ARM) | Vollständiges Linux; GPIO-Pins | Prototyping; Medienzentren; Light-Edge-Computing |
| **BeagleBone** | TI Sitara (ARM) | Echtzeit-PRU-Kerne | Industriell; Echtzeitanwendungen |
| **ESP32-S3** | Espresso | KI-Beschleunigung; USB | Edge-KI; Vision-Anwendungen |
---

## Echtzeitbetriebssysteme (RTOS)
Ein RTOS garantiert, dass kritische Aufgaben innerhalb eines definierten Zeitfensters abgeschlossen werden.
| RTOS | Lizenz | Am besten für |
|------|---------|----------|
| **FreeRTOS** | MIT | Am häufigsten; breite MCU-Unterstützung |
| **Zephyr** | Apache 2.0 | Modern; Linux Foundation; wachsendes Ökosystem |
| **ThreadX (Azure RTOS)** | MIT | Sicherheitszertifiziert; IoT |
| **embOS** | Kommerziell | Industriell; zertifiziert |
| **RT-Thread** | Apache 2.0 | Chinesisches Ökosystem; weltweit wachsend |
### RTOS vs. Bare Metal
| Aspekt | Bare-Metal | RTOS |
|--------|-----------|------|
| **Komplexität** | Einfach für einfache Aufgaben | Wird für komplexe, gleichzeitige Aufgaben benötigt |
| **Planung** | Manuell (Hauptschleife + Interrupts) | Präventive Planung mit Prioritäten |
| **Skalierbarkeit** | Schwierig, Funktionen hinzuzufügen | Einfaches Hinzufügen von Aufgaben |
| **Speicher** | Minimaler Overhead | Geringer Overhead (einige KB) |
---

## Kommunikationsprotokolle
### Kabelgebundene Protokolle
| Protokoll | Geschwindigkeit | Entfernung | Anwendungsfall |
|----------|-------|----------|----------|
| **UART** | Bis zu 1 Mbit/s | Kurz (an Bord) | Debug-Konsole; GPS-Module |
| **SPI** | Bis zu 100 MHz | Kurz (an Bord) | Hochgeschwindigkeits-Peripheriegeräte (Displays, Blitz) |
| **I²C** | Bis zu 3,4 MHz | Kurz (an Bord) | Sensoren; Kommunikation mit geringer Pinzahl |
| **KANN** | Bis zu 1 Mbit/s | Bis zu 1 km | Automobil; industriell |
| **Ethernet** | 10 Mbit/s - 100 Gbit/s | Bis zu 100 m | Vernetzung; Industrie (mit Erweiterungen) |
| **USB** | Bis zu 40 Gbit/s (USB4) | Bis zu 5 m | Peripheriegeräte; Aufladen |
### Drahtlose Protokolle
| Protokoll | Reichweite | Macht | Geschwindigkeit | Anwendungsfall |
|----------|-------|-------|-------|----------|
| **WLAN** | ~100 m | Hoch | Bis zu Wi-Fi 7 (46 Gbit/s theoretisch) | IoT mit hoher Bandbreite; Streaming |
| **Bluetooth Classic** | ~100 m | Mittel | 1-3 Mbit/s | Audio; Dateiübertragung |
| **BLE** (Bluetooth Low Energy) | ~100 m | Sehr niedrig | 1-2 Mbit/s | Wearables; Leuchtfeuer; Sensoren |
| **Zigbee** | ~100 m (Masche) | Niedrig | 250 kbit/s | Hausautomation; Industriesensoren |
| **Z-Welle** | ~100 m (Masche) | Niedrig | 100 kbit/s | Hausautomation |
| **LoRa / LoRaWAN** | Bis zu 15 km | Sehr niedrig | 0,3-50 kbit/s | Landwirtschaft; Versorgungsunternehmen; stadtweite Sensoren |
| **NB-IoT** | Mobilfunkabdeckung | Niedrig | 250 kbit/s | Dosierung; Vermögensverfolgung |
| **Faden / Materie** | ~100 m (Masche) | Niedrig | Mäßig | Smart Home (Apple, Google, Amazon) |
| **Mobilfunk (4G/5G)** | Global | Hoch | Hoch | Vernetzte Fahrzeuge; Fernüberwachung |
---

## IoT-Architektur
### Der IoT-Stack
| Schicht | Funktion | Beispiele |
|-------|----------|---------|
| **Geräte** | Sensoren, Aktoren, Mikrocontroller | ESP32, STM32, Raspberry Pi |
| **Konnektivität** | Netzwerkprotokolle | MQTT, HTTP, CoAP, LoRaWAN |
| **Edge-Computing** | Verarbeitung in Gerätenähe | AWS Greengrass, Azure IoT Edge |
| **Cloud-Plattform** | Datenaufnahme, Speicherung, Verarbeitung | AWS IoT, Azure IoT Hub, Google Cloud IoT |
| **Bewerbung** | Dashboards, Analysen, Warnungen | Grafana, benutzerdefinierte Web-Apps |
### IoT-Kommunikationsprotokolle
| Protokoll | Muster | Am besten für |
|----------|---------|----------|
| **MQTT** | Veröffentlichen/Abonnieren; leicht | Die meisten IoT-Anwendungen; geringe Bandbreite |
| **HTTP/REST** | Anfrage/Antwort | Wenn es auf Einfachheit ankommt; Web-Integration |
| **CoAP** | Anfrage/Antwort; UDP-basiert | Eingeschränkte Geräte; geringer Stromverbrauch |
| **AMQP** | Nachrichtenwarteschlange | Unternehmens-IoT; zuverlässige Lieferung |
| **WebSocket** | Bidirektional; dauerhafte Verbindung | Echtzeit-Dashboards; Live-Daten |
### MQTT im Detail
| Konzept | Beschreibung |
|---------|-------------|
| **Makler** | Zentraler Server, der Nachrichten weiterleitet (Mosquitto, EMQX, HiveMQ) |
| **Thema** | Hierarchische Adresse (z. B.`home/living-room/temperature`) |
| **QoS** | 0 (höchstens einmal), 1 (mindestens einmal), 2 (genau einmal) |
| **Beibehaltene Nachricht** | Letzte Nachricht zu einem Thema; an neue Abonnenten geliefert |
| **Letzter Wille** | Nachricht veröffentlicht, wenn ein Client unerwartet die Verbindung trennt |
---

## Edge Computing
Verarbeiten Sie Daten nahe der Quelle, anstatt alles in die Cloud zu senden.
| Nutzen | Beschreibung |
|---------|-------------|
| **Reduzierte Latenz** | Kein Hin- und Rückflug in die Cloud; sofortige Entscheidungen |
| **Bandbreiteneinsparungen** | Nur Zusammenfassungen oder Anomalien senden |
| **Datenschutz** | Sensible Daten bleiben vor Ort |
| **Zuverlässigkeit** | Funktioniert, wenn das Internet ausfällt |
| Plattform | Beschreibung |
|----------|-------------|
| **AWS Greengrass** | Lambda-Funktionen auf Edge-Geräten ausführen |
| **Azure IoT Edge** | Container auf Edge-Geräten ausführen |
| **NVIDIA Jetson** | GPU-beschleunigte Edge-KI (Orin, Nano) |
| **Himbeer-Pi** | Leichtes Edge-Computing |
---

## Firmware-Update (OTA)
Mit Over-the-Air-Updates können Sie Fehler beheben und Funktionen zu bereitgestellten Geräten hinzufügen.
| Sorge | Lösung |
|---------|----------|
| **Zuverlässigkeit** | Dual-Bank-Blitz; Rollback bei Fehler |
| **Sicherheit** | Signierte Bilder; verschlüsselte Übertragungen |
| **Größe** | Delta-Updates (nur geänderte Teile) |
| **Konnektivität** | Warteschlangenaktualisierungen, wenn das Gerät online geht |
---

## Sicherheitskritische eingebettete Systeme
| Domäne | Standards | Beispiele |
|--------|-----------|---------|
| **Automobil** | ISO 26262 (ASIL A-D) | Motorsteuerung, Bremsen, Airbags |
| **Medizinisch** | IEC 62304 | Herzschrittmacher, Infusionspumpen |
| **Luft- und Raumfahrt** | DO-178C (DAL A-E) | Flugsteuerung, Navigation |
| **Industriell** | IEC 61508 (SIL 1-4) | SPS, Sicherheitssteuerungen |
| **Eisenbahn** | EN 50128 (SIL 1-4) | Signaltechnik, Zugsteuerung |
---

## Tools und Entwicklung
| Werkzeug | Zweck |
|------|---------|
| **PlatformIO** | Plattformübergreifende eingebettete Entwicklung (Arduino, ESP32, STM32) |
| **STM32CubeIDE** | STs offizielle IDE für STM32 |
| **Arduino-IDE** | Einfache Entwicklung für Arduino und kompatible Boards |
| **ESP-IDF** | Espressifs offizielles SDK für ESP32 |
| **Zephyr SDK** | West-Build-System für Zephyr RTOS |
| **OpenOCD** | On-Chip-Debugging |
| **Logikanalysator** | SPI-, I²C- und UART-Protokolle debuggen |
| **Wireshark** | Netzwerkprotokollanalyse |
---

## Zusammenfassung
Eingebettete Systeme und IoT stellen die Schnittstelle zwischen Software und der physischen Welt dar. Von Mikrocontrollern, die Motoren steuern, bis hin zu mit der Cloud verbundenen Sensornetzwerken erfordern sie eine andere Denkweise als die Web- oder App-Entwicklung: begrenzte Ressourcen, Echtzeitanforderungen, lange Lebensdauern und Auswirkungen von Fehlern auf die physische Welt. Das Ökosystem ist enorm ausgereift – Frameworks wie ESP-IDF und Zephyr machen die berufliche Weiterentwicklung zugänglich, während Plattformen wie AWS IoT und Azure IoT Hub die Cloud-Seite übernehmen. Die Schlüsselkompetenzen sind das Verständnis von Hardwareschnittstellen, Kommunikationsprotokollen, Energieverwaltung und die Disziplin, Software zu schreiben, die jahrelang ohne Eingriffe zuverlässig laufen muss.