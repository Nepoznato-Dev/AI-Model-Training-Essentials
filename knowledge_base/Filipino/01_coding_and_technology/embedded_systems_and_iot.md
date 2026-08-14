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
# Mga Naka-embed na System at IoT
Ang mga naka-embed na system ay mga computer na nakatago sa loob ng iba pang mga device — ang engine control unit ng iyong sasakyan, ang controller ng iyong washing machine, ang microcontroller sa isang smart thermostat. Hindi tulad ng mga computer na may pangkalahatang layunin, idinisenyo ang mga ito para sa mga partikular na gawain, kadalasang may mahigpit na limitasyon sa kapangyarihan, memorya, at bilis ng pagproseso. Pinapalawak ng Internet of Things (IoT) ang mga naka-embed na system sa pamamagitan ng pagkonekta sa mga ito sa mga network, na nagpapagana ng malayuang pagsubaybay, kontrol, at pagkolekta ng data. Magkasama, kinakatawan nila ang bilyun-bilyong mga computing device na nakikipag-ugnayan sa pisikal na mundo.
---

## Mga Pangunahing Kaalaman sa Mga Naka-embed na System
### Ano ang Naiiba sa Naka-embed
| Aspeto | Pangkalahatang Layunin na Computer | Naka-embed na System |
|----------------------|----------------------|----------------|
| **Layunin** | Magpatakbo ng anumang software | Magsagawa ng mga partikular na gawain |
| **Mga Mapagkukunan** | Masaganang CPU, RAM, storage | Limitado (KB hanggang MB ng RAM; MHz hanggang mababang GHz) |
| **Kapangyarihan** | Nakasaksak o malaking baterya | Kadalasang pinapagana ng baterya o pag-aani ng enerhiya |
| **OS** | Buong OS (Windows, Linux, macOS) | RTOS, bare-metal, o naka-embed na Linux |
| **User interface** | Rich (screen, keyboard, mouse) | Minimal (mga LED, button, sensor) o wala |
| **Real-time** | Pinakamahusay na pagsisikap | Kadalasan mahirap real-time na mga deadline |
| **Habang buhay** | 3-7 taon | 10-25+ taon |
### Mga Microcontroller kumpara sa Microprocessors
| Tampok | Microcontroller (MCU) | Microprocessor (MPU) |
|---------|----------------------|---------------------|
| **Pagsasama** | CPU + RAM + Flash + peripheral sa isang chip | CPU lamang; panlabas na RAM at storage |
| **Pagganap** | Mababa hanggang katamtaman (hanay ng MHz) | Mataas (hanay ng GHz) |
| **Kapangyarihan** | Napakababa (µA hanggang mA) | Mas mataas (daan-daang mA hanggang amps) |
| **Gastos** | $0.10 - $10 | $5 - $100+ |
| **Mga Halimbawa** | STM32, ESP32, Arduino (ATmega), nRF52 | Raspberry Pi (BCM2835), i.MX, Allwinner |
| **Kaso ng paggamit** | Mga sensor, actuator, simpleng kontrol | Mga display, kumplikadong pagproseso, Linux |
---

## Mga Karaniwang Naka-embed na Platform
| Platform | MCU/MPU | Pangunahing Tampok | Pinakamahusay Para sa |
|----------|---------|-------------|----------|
| **Arduino** | ATmega328P (at iba pa) | Simple; malaking komunidad | Pag-aaral; prototyping |
| **ESP32** | Espressif dual-core | Wi-Fi + Bluetooth; mababang halaga | mga proyekto ng IoT; mga nakakonektang device |
| **Raspberry Pi Pico** | RP2040 (dual-core ARM) | Abot-kayang; Suporta sa MicroPython | Edukasyon; mga proyekto sa libangan |
| **STM32** | ARM Cortex-M series | Pang-industriya na grado; malawak na hanay | Propesyonal na naka-embed; pang-industriya |
| **nRF52/nRF53** | Nordic Semiconductor | Espesyalista sa Bluetooth Low Energy | Mga nasusuot; mga beacon |
| **Raspberry Pi** | Broadcom BCM (ARM) | Buong Linux; Mga pin ng GPIO | Prototyping; mga sentro ng media; light edge computing |
| **BeagleBone** | TI Sitara (ARM) | Mga real-time na PRU core | Pang-industriya; mga real-time na application |
| **ESP32-S3** | Espressif | AI acceleration; USB | Edge AI; mga aplikasyon sa paningin |
---

## Real-Time Operating System (RTOS)
Ginagarantiyahan ng isang RTOS na makumpleto ang mga kritikal na gawain sa loob ng isang tinukoy na palugit ng oras.
| RTOS | Lisensya | Pinakamahusay Para sa |
|------|---------|----------|
| **LibrengRTOS** | MIT | Pinaka-karaniwan; malawak na suporta sa MCU |
| **Zephyr** | Apache 2.0 | Moderno; Linux Foundation; lumalagong ecosystem |
| **ThreadX (Azure RTOS)** | MIT | Sertipikadong kaligtasan; IoT |
| **embOS** | Komersyal | Pang-industriya; sertipikadong |
| **RT-Thread** | Apache 2.0 | ekosistem ng Tsino; lumalaki sa buong mundo |
### RTOS vs Bare Metal
| Aspeto | Hubad na Metal | RTOS |
|--------|-----------|------|
| **Pagiging kumplikado** | Simple para sa mga simpleng gawain | Kailangan para sa kumplikado, kasabay na mga gawain |
| **Pag-iiskedyul** | Manwal (pangunahing loop + mga interrupts) | Preemptive na pag-iiskedyul na may mga priyoridad |
| **Scalability** | Mahirap magdagdag ng mga feature | Madaling magdagdag ng mga gawain |
| **Memory** | Minimal na overhead | Maliit na overhead (ilang KB) |
---

## Mga Protokol ng Komunikasyon
### Mga Wired Protocol
| Protocol | Bilis | Distansya | Use Case |
|----------|-------|----------|----------|
| **UART** | Hanggang 1 Mbps | Maikli (on-board) | Debug console; Mga module ng GPS |
| **SPI** | Hanggang 100 MHz | Maikli (on-board) | Mga high-speed na peripheral (display, flash) |
| **I²C** | Hanggang 3.4 MHz | Maikli (on-board) | Mga sensor; low-pin-count na komunikasyon |
| **PWEDE** | Hanggang 1 Mbps | Hanggang 1 km | Automotive; pang-industriya |
| **Ethernet** | 10 Mbps - 100 Gbps | Hanggang 100 m | Networking; pang-industriya (na may mga extension) |
| **USB** | Hanggang 40 Gbps (USB4) | Hanggang 5 m | Mga peripheral; nagcha-charge |
### Mga Wireless Protocol
| Protocol | Saklaw | Kapangyarihan | Bilis | Use Case |
|----------|-------|-------|-------|----------|
| **Wi-Fi** | ~100 m | Mataas | Hanggang Wi-Fi 7 (46 Gbps theoretical) | High-bandwidth na IoT; streaming |
| **Bluetooth Classic** | ~100 m | Katamtaman | 1-3 Mbps | Audio; paglilipat ng file |
| **BLE** (Bluetooth Low Energy) | ~100 m | Napakababa | 1-2 Mbps | Mga nasusuot; mga beacon; mga sensor |
| **Zigbee** | ~100 m (mesh) | Mababa | 250 kbps | Home automation; pang-industriya na mga sensor |
| **Z-Wave** | ~100 m (mesh) | Mababa | 100 kbps | Home automation |
| **LoRa / LoRaWAN** | Hanggang 15 km | Napakababa | 0.3-50 kbps | Agrikultura; mga kagamitan; mga sensor sa buong lungsod |
| **NB-IoT** | Cellular coverage | Mababa | 250 kbps | Pagsusukat; pagsubaybay sa asset |
| **Thread / Matter** | ~100 m (mesh) | Mababa | Katamtaman | Smart home (Apple, Google, Amazon) |
| **Sellular (4G/5G)** | Global | Mataas | Mataas | Mga konektadong sasakyan; malayuang pagsubaybay |
---

## Arkitektura ng IoT
### Ang IoT Stack
| Layer | Function | Mga halimbawa |
|-------|----------|---------|
| **Mga Device** | Mga sensor, actuator, microcontroller | ESP32, STM32, Raspberry Pi |
| **Koneksyon** | Mga protocol ng network | MQTT, HTTP, CoAP, LoRaWAN |
| **Edge computing** | Pinoproseso malapit sa device | AWS Greengrass, Azure IoT Edge |
| **Cloud platform** | Pag-ingest ng data, imbakan, pagproseso | AWS IoT, Azure IoT Hub, Google Cloud IoT |
| **Aplikasyon** | Mga dashboard, analytics, alerto | Grafana, custom na web app |
### IoT Communication Protocols
| Protocol | Pattern | Pinakamahusay Para sa |
|----------|---------|----------|
| **MQTT** | Mag-publish/mag-subscribe; magaan | Karamihan sa mga application ng IoT; mababang bandwidth |
| **HTTP/REST** | Kahilingan/tugon | Kapag mahalaga ang pagiging simple; web integration |
| **CoAP** | Kahilingan/tugon; Nakabatay sa UDP | Pinilit na mga aparato; mababang kapangyarihan |
| **AMQP** | Nakapila ang mensahe | Enterprise IoT; maaasahang paghahatid |
| **WebSocket** | Bidirectional; paulit-ulit na koneksyon | Mga real-time na dashboard; live na data |
### MQTT sa Detalye
| Konsepto | Paglalarawan |
|---------|-------------|
| **Broker** | Central server na nagruruta ng mga mensahe (Mosquitto, EMQX, HiveMQ) |
| **Paksa** | Hierarchical na address (hal.,`home/living-room/temperature`) |
| **QoS** | 0 (kahit isang beses), 1 (kahit isang beses), 2 (eksaktong isang beses) |
| **Napanatili ang mensahe** | Huling mensahe sa isang paksa; naihatid sa mga bagong subscriber |
| **Huling Habilin** | Na-publish ang mensahe kapag hindi inaasahang nadiskonekta ang isang kliyente |
---

## Edge Computing
Pinoproseso ang data malapit sa pinagmulan sa halip na ipadala ang lahat sa cloud.
| Benepisyo | Paglalarawan |
|---------|-------------|
| **Nabawasan ang latency** | Walang round-trip sa cloud; agarang desisyon |
| **Pagtitipid sa bandwidth** | Magpadala lamang ng mga buod o anomalya |
| **Privacy** | Nananatili ang sensitibong data sa nasasakupan |
| **Pagiging Maaasahan** | Gumagana kapag mahina ang internet |
| Platform | Paglalarawan |
|----------|-------------|
| **AWS Greengrass** | Patakbuhin ang mga function ng Lambda sa mga edge na device |
| **Azure IoT Edge** | Magpatakbo ng mga lalagyan sa mga device sa gilid |
| **NVIDIA Jetson** | GPU-accelerated edge AI (Orin, Nano) |
| **Raspberry Pi** | Magaang edge computing |
---

## Update ng Firmware (OTA)
Nagbibigay-daan sa iyo ang mga over-the-air na update na ayusin ang mga bug at magdagdag ng mga feature sa mga naka-deploy na device.
| Pag-aalala | Solusyon |
|---------|----------|
| **Pagiging Maaasahan** | Dual-bank flash; rollback sa kabiguan |
| **Seguridad** | Mga nilagdaang larawan; mga naka-encrypt na paglilipat |
| **Laki** | Mga update sa Delta (mga binago lang na bahagi) |
| **Koneksyon** | I-queue ang mga update para kapag online ang device |
---

## Safety-Critical na Naka-embed na System
| Domain | Mga Pamantayan | Mga halimbawa |
|--------|-----------|---------|
| **Sasakyan** | ISO 26262 (ASIL A-D) | Kontrol ng makina, pagpepreno, mga airbag |
| **Medical** | IEC 62304 | Mga pacemaker, infusion pump |
| **Aerospace** | DO-178C (DAL A-E) | Kontrol ng flight, nabigasyon |
| **Industriyal** | IEC 61508 (SIL 1-4) | Mga PLC, mga controller ng kaligtasan |
| **Riles** | EN 50128 (SIL 1-4) | Pagsenyas, kontrol ng tren |
---

## Mga Tool at Pag-unlad
| Tool | Layunin |
|------|---------|
| **PlatformIO** | Cross-platform na naka-embed na development (Arduino, ESP32, STM32) |
| **STM32CubeIDE** | Opisyal na IDE ng ST para sa STM32 |
| **Arduino IDE** | Simpleng pag-develop para sa Arduino at mga katugmang board |
| **ESP-IDF** | Opisyal na SDK ng ESP32 para sa ESP32 |
| **Zephyr SDK** | West build system para sa Zephyr RTOS |
| **OpenOCD** | On-chip debugging |
| **Logic analyzer** | I-debug ang mga protocol ng SPI, I²C, UART |
| **Wireshark** | Pagsusuri ng protocol ng network |
---

## Buod
Ang mga naka-embed na system at IoT ay kumakatawan sa intersection ng software at ng pisikal na mundo. Mula sa mga microcontroller na kumokontrol sa mga motor hanggang sa mga network ng sensor na nakakonekta sa cloud, nangangailangan sila ng ibang mindset mula sa pag-develop ng web o app: mga limitadong mapagkukunan, mga kinakailangan sa real-time, mahabang buhay, at mga pisikal na epekto ng mga bug. Ang ecosystem ay nag-mature nang husto — ang mga frameworks tulad ng ESP-IDF at Zephyr ay ginagawang naa-access ang propesyonal na pag-unlad, habang ang mga platform tulad ng AWS IoT at Azure IoT Hub ay humahawak sa cloud side. Ang mga pangunahing kasanayan ay ang pag-unawa sa mga interface ng hardware, mga protocol ng komunikasyon, pamamahala ng kapangyarihan, at ang disiplina sa pagsulat ng software na dapat tumakbo nang maaasahan sa loob ng maraming taon nang walang interbensyon.