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

# Embedded Systems and IoT

Embedded systems are computers hidden inside other devices — your car's engine control unit, your washing machine's controller, the microcontroller in a smart thermostat. Unlike general-purpose computers, they're designed for specific tasks, often with tight constraints on power, memory, and processing speed. The Internet of Things (IoT) extends embedded systems by connecting them to networks, enabling remote monitoring, control, and data collection. Together, they represent billions of computing devices that interact with the physical world.

---

## Embedded Systems Fundamentals

### What Makes Embedded Different

| Aspect | General-Purpose Computer | Embedded System |
|--------|------------------------|-----------------|
| **Purpose** | Run any software | Perform specific tasks |
| **Resources** | Abundant CPU, RAM, storage | Limited (KB to MB of RAM; MHz to low GHz) |
| **Power** | Plugged in or large battery | Often battery-powered or energy-harvesting |
| **OS** | Full OS (Windows, Linux, macOS) | RTOS, bare-metal, or embedded Linux |
| **User interface** | Rich (screen, keyboard, mouse) | Minimal (LEDs, buttons, sensors) or none |
| **Real-time** | Best-effort | Often hard real-time deadlines |
| **Lifetime** | 3-7 years | 10-25+ years |

### Microcontrollers vs Microprocessors

| Feature | Microcontroller (MCU) | Microprocessor (MPU) |
|---------|----------------------|---------------------|
| **Integration** | CPU + RAM + Flash + peripherals on one chip | CPU only; external RAM and storage |
| **Performance** | Low to moderate (MHz range) | High (GHz range) |
| **Power** | Very low (µA to mA) | Higher (hundreds of mA to amps) |
| **Cost** | $0.10 - $10 | $5 - $100+ |
| **Examples** | STM32, ESP32, Arduino (ATmega), nRF52 | Raspberry Pi (BCM2835), i.MX, Allwinner |
| **Use case** | Sensors, actuators, simple control | Displays, complex processing, Linux |

---

## Common Embedded Platforms

| Platform | MCU/MPU | Key Feature | Best For |
|----------|---------|-------------|----------|
| **Arduino** | ATmega328P (and others) | Simple; huge community | Learning; prototyping |
| **ESP32** | Espressif dual-core | Wi-Fi + Bluetooth; low cost | IoT projects; connected devices |
| **Raspberry Pi Pico** | RP2040 (dual-core ARM) | Affordable; MicroPython support | Education; hobby projects |
| **STM32** | ARM Cortex-M series | Industrial grade; wide range | Professional embedded; industrial |
| **nRF52/nRF53** | Nordic Semiconductor | Bluetooth Low Energy specialist | Wearables; beacons |
| **Raspberry Pi** | Broadcom BCM (ARM) | Full Linux; GPIO pins | Prototyping; media centres; light edge computing |
| **BeagleBone** | TI Sitara (ARM) | Real-time PRU cores | Industrial; real-time applications |
| **ESP32-S3** | Espressif | AI acceleration; USB | Edge AI; vision applications |

---

## Real-Time Operating Systems (RTOS)

An RTOS guarantees that critical tasks complete within a defined time window.

| RTOS | Licence | Best For |
|------|---------|----------|
| **FreeRTOS** | MIT | Most common; wide MCU support |
| **Zephyr** | Apache 2.0 | Modern; Linux Foundation; growing ecosystem |
| **ThreadX (Azure RTOS)** | MIT | Safety-certified; IoT |
| **embOS** | Commercial | Industrial; certified |
| **RT-Thread** | Apache 2.0 | Chinese ecosystem; growing globally |

### RTOS vs Bare Metal

| Aspect | Bare Metal | RTOS |
|--------|-----------|------|
| **Complexity** | Simple for simple tasks | Needed for complex, concurrent tasks |
| **Scheduling** | Manual (main loop + interrupts) | Preemptive scheduling with priorities |
| **Scalability** | Hard to add features | Easy to add tasks |
| **Memory** | Minimal overhead | Small overhead (a few KB) |

---

## Communication Protocols

### Wired Protocols

| Protocol | Speed | Distance | Use Case |
|----------|-------|----------|----------|
| **UART** | Up to 1 Mbps | Short (on-board) | Debug console; GPS modules |
| **SPI** | Up to 100 MHz | Short (on-board) | High-speed peripherals (displays, flash) |
| **I²C** | Up to 3.4 MHz | Short (on-board) | Sensors; low-pin-count communication |
| **CAN** | Up to 1 Mbps | Up to 1 km | Automotive; industrial |
| **Ethernet** | 10 Mbps - 100 Gbps | Up to 100 m | Networking; industrial (with extensions) |
| **USB** | Up to 40 Gbps (USB4) | Up to 5 m | Peripherals; charging |

### Wireless Protocols

| Protocol | Range | Power | Speed | Use Case |
|----------|-------|-------|-------|----------|
| **Wi-Fi** | ~100 m | High | Up to Wi-Fi 7 (46 Gbps theoretical) | High-bandwidth IoT; streaming |
| **Bluetooth Classic** | ~100 m | Medium | 1-3 Mbps | Audio; file transfer |
| **BLE** (Bluetooth Low Energy) | ~100 m | Very low | 1-2 Mbps | Wearables; beacons; sensors |
| **Zigbee** | ~100 m (mesh) | Low | 250 kbps | Home automation; industrial sensors |
| **Z-Wave** | ~100 m (mesh) | Low | 100 kbps | Home automation |
| **LoRa / LoRaWAN** | Up to 15 km | Very low | 0.3-50 kbps | Agriculture; utilities; city-wide sensors |
| **NB-IoT** | Cellular coverage | Low | 250 kbps | Metering; asset tracking |
| **Thread / Matter** | ~100 m (mesh) | Low | Moderate | Smart home (Apple, Google, Amazon) |
| **Cellular (4G/5G)** | Global | High | High | Connected vehicles; remote monitoring |

---

## IoT Architecture

### The IoT Stack

| Layer | Function | Examples |
|-------|----------|---------|
| **Devices** | Sensors, actuators, microcontrollers | ESP32, STM32, Raspberry Pi |
| **Connectivity** | Network protocols | MQTT, HTTP, CoAP, LoRaWAN |
| **Edge computing** | Processing near the device | AWS Greengrass, Azure IoT Edge |
| **Cloud platform** | Data ingestion, storage, processing | AWS IoT, Azure IoT Hub, Google Cloud IoT |
| **Application** | Dashboards, analytics, alerts | Grafana, custom web apps |

### IoT Communication Protocols

| Protocol | Pattern | Best For |
|----------|---------|----------|
| **MQTT** | Publish/subscribe; lightweight | Most IoT applications; low bandwidth |
| **HTTP/REST** | Request/response | When simplicity matters; web integration |
| **CoAP** | Request/response; UDP-based | Constrained devices; low power |
| **AMQP** | Message queuing | Enterprise IoT; reliable delivery |
| **WebSocket** | Bidirectional; persistent connection | Real-time dashboards; live data |

### MQTT in Detail

| Concept | Description |
|---------|-------------|
| **Broker** | Central server that routes messages (Mosquitto, EMQX, HiveMQ) |
| **Topic** | Hierarchical address (e.g., `home/living-room/temperature`) |
| **QoS** | 0 (at most once), 1 (at least once), 2 (exactly once) |
| **Retained message** | Last message on a topic; delivered to new subscribers |
| **Last Will** | Message published when a client disconnects unexpectedly |

---

## Edge Computing

Processing data near the source instead of sending everything to the cloud.

| Benefit | Description |
|---------|-------------|
| **Reduced latency** | No round-trip to cloud; immediate decisions |
| **Bandwidth savings** | Only send summaries or anomalies |
| **Privacy** | Sensitive data stays on-premise |
| **Reliability** | Works when internet is down |

| Platform | Description |
|----------|-------------|
| **AWS Greengrass** | Run Lambda functions on edge devices |
| **Azure IoT Edge** | Run containers on edge devices |
| **NVIDIA Jetson** | GPU-accelerated edge AI (Orin, Nano) |
| **Raspberry Pi** | Lightweight edge computing |

---

## Firmware Update (OTA)

Over-the-air updates let you fix bugs and add features to deployed devices.

| Concern | Solution |
|---------|----------|
| **Reliability** | Dual-bank flash; rollback on failure |
| **Security** | Signed images; encrypted transfers |
| **Size** | Delta updates (only changed portions) |
| **Connectivity** | Queue updates for when device comes online |

---

## Safety-Critical Embedded Systems

| Domain | Standards | Examples |
|--------|-----------|---------|
| **Automotive** | ISO 26262 (ASIL A-D) | Engine control, braking, airbags |
| **Medical** | IEC 62304 | Pacemakers, infusion pumps |
| **Aerospace** | DO-178C (DAL A-E) | Flight control, navigation |
| **Industrial** | IEC 61508 (SIL 1-4) | PLCs, safety controllers |
| **Railway** | EN 50128 (SIL 1-4) | Signalling, train control |

---

## Tools and Development

| Tool | Purpose |
|------|---------|
| **PlatformIO** | Cross-platform embedded development (Arduino, ESP32, STM32) |
| **STM32CubeIDE** | ST's official IDE for STM32 |
| **Arduino IDE** | Simple development for Arduino and compatible boards |
| **ESP-IDF** | Espressif's official SDK for ESP32 |
| **Zephyr SDK** | West build system for Zephyr RTOS |
| **OpenOCD** | On-chip debugging |
| **Logic analyser** | Debug SPI, I²C, UART protocols |
| **Wireshark** | Network protocol analysis |

---

## Summary

Embedded systems and IoT represent the intersection of software and the physical world. From microcontrollers controlling motors to cloud-connected sensor networks, they require a different mindset from web or app development: constrained resources, real-time requirements, long lifetimes, and physical-world consequences of bugs. The ecosystem has matured enormously — frameworks like ESP-IDF and Zephyr make professional development accessible, while platforms like AWS IoT and Azure IoT Hub handle the cloud side. The key skills are understanding hardware interfaces, communication protocols, power management, and the discipline to write software that must run reliably for years without intervention.
