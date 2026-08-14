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
# Sistemi Embedded e IoT
I sistemi embedded sono computer nascosti all'interno di altri dispositivi: l'unità di controllo del motore della tua auto, il controller della tua lavatrice, il microcontrollore di un termostato intelligente. A differenza dei computer generici, sono progettati per compiti specifici, spesso con rigidi vincoli in termini di potenza, memoria e velocità di elaborazione. L'Internet delle cose (IoT) estende i sistemi integrati collegandoli alle reti, consentendo il monitoraggio, il controllo e la raccolta di dati da remoto. Insieme, rappresentano miliardi di dispositivi informatici che interagiscono con il mondo fisico.
---

## Fondamenti di sistemi embedded
### Cosa rende Embedded diverso
| Aspetto | Computer per uso generale | Sistema integrato |
|--------|-----------------------|-----------------|
| **Scopo** | Esegui qualsiasi software | Eseguire compiti specifici |
| **Risorse** | CPU, RAM e spazio di archiviazione abbondanti | Limitato (da KB a MB di RAM; da MHz a GHz basso) |
| **Potenza** | Batteria collegata o grande | Spesso alimentato a batteria o con raccolta di energia |
| **Sistema operativo** | Sistema operativo completo (Windows, Linux, macOS) | RTOS, bare metal o Linux incorporato |
| **Interfaccia utente** | Ricco (schermo, tastiera, mouse) | Minimo (LED, pulsanti, sensori) o nessuno |
| **In tempo reale** | Miglior sforzo | Spesso scadenze rigide in tempo reale |
| **A vita** | 3-7 anni | 10-25+ anni |
### Microcontrollori e microprocessori
| Caratteristica | Microcontrollore (MCU) | Microprocessore (MPU) |
|---------|----------------------|----------------------|
| **Integrazione** | CPU + RAM + Flash + periferiche su un chip | Solo CPU; RAM esterna e spazio di archiviazione |
| **Prestazioni** | Da basso a moderato (gamma MHz) | Alto (gamma GHz) |
| **Potenza** | Molto basso (da µA a mA) | Superiore (centinaia di mA in ampere) |
| **Costo** | $ 0,10 - $ 10 | $5 - $100+ |
| **Esempi** | STM32, ESP32, Arduino (ATmega), nRF52 | Raspberry Pi (BCM2835), i.MX, Allwinner |
| **Caso d'uso** | Sensori, attuatori, controllo semplice | Visualizzazioni, elaborazioni complesse, Linux |
---

## Piattaforme integrate comuni
| Piattaforma | MCU/MPU | Caratteristica fondamentale | Ideale per |
|----------|---------|-----|----------|
| **Arduino** | ATmega328P (e altri) | Semplice; comunità enorme | Apprendimento; prototipazione |
| **ESP32** | Espressivo dual-core | Wi-Fi+Bluetooth; basso costo | progetti IoT; dispositivi collegati |
| **Raspberry Pi Pico** | RP2040 (ARM dual-core) | Conveniente; Supporto MicroPython | Istruzione; progetti hobbistici |
| **STM32** | Serie ARM Cortex-M | Grado industriale; ampia gamma | Integrato professionale; industriale |
| **nRF52/nRF53** | Semiconduttore nordico | Specialista Bluetooth Low Energy | Indossabili; fari |
| **Lampone Pi** | Broadcom BCM (ARM) | Linux completo; Pin GPIO | Prototipazione; centri mediatici; elaborazione all'avanguardia |
| **Osso di Beagle** | TI Sitara (ARM) | Core PRU in tempo reale | Industriale; applicazioni in tempo reale |
| **ESP32-S3** | Espressivo | Accelerazione dell'IA; USB | IA bordo; applicazioni di visione |
---

## Sistemi operativi in ​​tempo reale (RTOS)
Un RTOS garantisce che le attività critiche vengano completate entro un intervallo di tempo definito.
| RTOS | Licenza | Ideale per |
|------|---------|----------|
| **FreeRTOS** | MIT | Più comune; ampio supporto MCU |
| **Zefiro** | Apache2.0 | Moderno; Fondazione Linux; ecosistema in crescita |
| **ThreadX (RTOS di Azure)** | MIT | Certificato di sicurezza; IoT |
| **embOS** | Commerciale | Industriale; certificato |
| **Discussione RT** | Apache2.0 | Ecosistema cinese; in crescita a livello globale |
### RTOS contro Bare Metal
| Aspetto | Metallo nudo | RTOS |
|--------|-----------|------|
| **Complessità** | Semplice per compiti semplici | Necessario per attività complesse e simultanee |
| **Programmazione** | Manuale (loop principale + interruzioni) | Schedulazione preventiva con priorità |
| **Scalabilità** | Difficile aggiungere funzionalità | Facile aggiungere attività |
| **Memoria** | Spese generali minime | Piccolo sovraccarico (pochi KB) |
---

## Protocolli di comunicazione
### Protocolli cablati
| Protocollo | Velocità | Distanza | Caso d'uso |
|----------|-------|----------|----------|
| **UART** | Fino a 1Mbps | Breve (a bordo) | Console di debug; Moduli GPS |
| **SPI** | Fino a 100 MHz | Breve (a bordo) | Periferiche ad alta velocità (display, flash) |
| **I²C** | Fino a 3,4 MHz | Breve (a bordo) | Sensori; comunicazione a basso numero di pin |
| **PUÒ** | Fino a 1Mbps | Fino a 1 km | automobilistico; industriale |
| **Ethernet** | 10Mbps - 100Gbps | Fino a 100 metri | Rete; industriale (con estensioni) |
| **USB** | Fino a 40 Gbps (USB4) | Fino a 5 metri | periferiche; ricarica |
### Protocolli wireless
| Protocollo | Gamma | Potenza | Velocità | Caso d'uso |
|----------|-------|-------|-------|----------|
| **Wi-Fi** | ~100 mt | Alto | Fino a Wi-Fi 7 (46 Gbps teorici) | IoT a larghezza di banda elevata; streaming |
| **Bluetooth classico** | ~100 mt | Medio | 1-3Mbps | Audio; trasferimento file |
| **BLE** (Bluetooth a basso consumo energetico) | ~100 mt | Molto basso | 1-2Mbps | Indossabili; fari; sensori |
| **Zigbee** | ~100 m (maglia) | Basso | 250 kbps | Domotica; sensori industriali |
| **Onda Z** | ~100 m (maglia) | Basso | 100 kbps | Domotica |
| **LoRa/LoRaWAN** | Fino a 15 km | Molto basso | 0,3-50 kbps | Agricoltura; utenze; sensori a livello cittadino |
| **NB-IoT** | Copertura cellulare | Basso | 250 kbps | Misurazione; monitoraggio delle risorse |
| **Discussione/argomento** | ~100 m (maglia) | Basso | Moderato | Casa intelligente (Apple, Google, Amazon) |
| **Cellulare (4G/5G)** | Globale | Alto | Alto | Veicoli connessi; monitoraggio remoto |
---

## Architettura IoT
### Lo stack IoT
| Strato | Funzione | Esempi |
|-------|----------|---------|
| **Dispositivi** | Sensori, attuatori, microcontrollori | ESP32, STM32, Raspberry Pi |
| **Connettività** | Protocolli di rete | MQTT, HTTP, CoAP, LoRaWAN |
| **Edge computing** | Elaborazione vicino al dispositivo | AWS Greengrass, Azure IoT Edge |
| **Piattaforma cloud** | Acquisizione, archiviazione, elaborazione dei dati | AWS IoT, Hub IoT di Azure, Google Cloud IoT |
| **Applicazione** | Cruscotti, analisi, avvisi | Grafana, app web personalizzate |
### Protocolli di comunicazione IoT
| Protocollo | Modello | Ideale per |
|----------|---------|----------|
| **MQTT** | Pubblica/sottoscrivi; leggero | La maggior parte delle applicazioni IoT; larghezza di banda ridotta |
| **HTTP/REST** | Richiesta/risposta | Quando la semplicità conta; integrazione web |
| **CoAP** | Richiesta/risposta; Basato su UDP | Dispositivi vincolati; bassa potenza |
| **AMQP** | Accodamento messaggi | IoT aziendale; consegna affidabile |
| **WebSocket** | Bidirezionale; connessione persistente | Cruscotti in tempo reale; dati in tempo reale |
### MQTT in dettaglio
| Concetto | Descrizione |
|---------|-----|
| **Intermediario** | Server centrale che instrada i messaggi (Mosquitto, EMQX, HiveMQ) |
| **Argomento** | Indirizzo gerarchico (ad esempio,`home/living-room/temperature`) |
| **QoS** | 0 (al massimo una volta), 1 (almeno una volta), 2 (esattamente una volta) |
| **Messaggio conservato** | Ultimo messaggio su un argomento; consegnato ai nuovi abbonati |
| **Ultimo testamento** | Messaggio pubblicato quando un client si disconnette inaspettatamente |
---

##Edge computing
Elaborare i dati vicino alla fonte invece di inviare tutto al cloud.
| Vantaggio | Descrizione |
|---------|-----|
| **Latenza ridotta** | Nessun viaggio di andata e ritorno verso il cloud; decisioni immediate |
| **Risparmio di larghezza di banda** | Inviare solo riepiloghi o anomalie |
| **Privacy** | I dati sensibili rimangono in sede |
| **Affidabilità** | Funziona quando Internet non è disponibile |
| Piattaforma | Descrizione |
|----------|-------------|
| **AWS Greengrass** | Esegui le funzioni Lambda sui dispositivi edge |
| **IoT Edge di Azure** | Esegui contenitori su dispositivi periferici |
| **NVIDIA Jetson** | AI edge accelerata dalla GPU (Orin, Nano) |
| **Lampone Pi** | Edge computing leggero |
---

## Aggiornamento firmware (OTA)
Gli aggiornamenti over-the-air ti consentono di correggere bug e aggiungere funzionalità ai dispositivi distribuiti.
| Preoccupazione | Soluzione |
|---------|----------|
| **Affidabilità** | Flash a doppio banco; rollback in caso di fallimento |
| **Sicurezza** | Immagini firmate; trasferimenti crittografati |
| **Taglia** | Aggiornamenti Delta (solo parti modificate) |
| **Connettività** | Aggiornamenti in coda per quando il dispositivo è online |
---

## Sistemi integrati critici per la sicurezza
| Dominio | Norme | Esempi |
|--------|-----------|---------|
| **Automobilistico** | ISO 26262 (ASIL A-D) | Controllo motore, frenata, airbag |
| **Medico** | CEI 62304| Pacemaker, pompe per infusione |
| **Aerospaziale** | DO-178C (DAL A-E) | Controllo del volo, navigazione |
| **Industriale** | IEC 61508 (SIL 1-4) | PLC, controllori di sicurezza |
| **Ferrovia** | EN 50128 (SIL 1-4) | Segnalamento, controllo treni |
---

## Strumenti e sviluppo
| Strumento | Scopo |
|------|---------|
| **PiattaformaIO** | Sviluppo embedded multipiattaforma (Arduino, ESP32, STM32) |
| **STM32CubeIDE** | IDE ufficiale della ST per STM32 |
| **IDE Arduino** | Sviluppo semplice per Arduino e schede compatibili |
| **ESP-IDF** | SDK ufficiale di Espressif per ESP32 |
| **SDK Zephyr** | Sistema di build occidentale per Zephyr RTOS |
| **OpenOCD** | Debug su chip |
| **Analizzatore logico** | Debug dei protocolli SPI, I²C, UART |
| **Wireshark** | Analisi del protocollo di rete |
---

## Riepilogo
I sistemi embedded e l’IoT rappresentano l’intersezione tra il software e il mondo fisico. Dai microcontrollori che controllano i motori alle reti di sensori connesse al cloud, richiedono una mentalità diversa dallo sviluppo web o di app: risorse limitate, requisiti in tempo reale, lunga durata e conseguenze dei bug nel mondo fisico. L'ecosistema è maturato enormemente: framework come ESP-IDF e Zephyr rendono accessibile lo sviluppo professionale, mentre piattaforme come AWS IoT e Azure IoT Hub gestiscono il lato cloud. Le competenze chiave consistono nella comprensione delle interfacce hardware, dei protocolli di comunicazione, della gestione dell'alimentazione e della disciplina necessaria per scrivere software che deve funzionare in modo affidabile per anni senza interventi.