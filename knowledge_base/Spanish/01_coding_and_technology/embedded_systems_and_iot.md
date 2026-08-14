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
# Sistemas integrados e IoT
Los sistemas integrados son computadoras ocultas dentro de otros dispositivos: la unidad de control del motor de su automóvil, el controlador de su lavadora, el microcontrolador de un termostato inteligente. A diferencia de las computadoras de uso general, están diseñadas para tareas específicas, a menudo con estrictas limitaciones de energía, memoria y velocidad de procesamiento. El Internet de las cosas (IoT) amplía los sistemas integrados conectándolos a redes, lo que permite la supervisión, el control y la recopilación de datos remotos. Juntos, representan miles de millones de dispositivos informáticos que interactúan con el mundo físico.
---

## Fundamentos de los sistemas integrados
### ¿Qué hace que Embedded sea diferente?
| Aspecto | Computadora de uso general | Sistema integrado |
|--------|------------------------|-----------------|
| **Propósito** | Ejecute cualquier software | Realizar tareas específicas |
| **Recursos** | Abundante CPU, RAM, almacenamiento | Limitado (KB a MB de RAM; MHz a GHz bajos) |
| **Poder** | Batería enchufada o grande | A menudo funcionan con baterías o con recolección de energía |
| **SO** | Sistema operativo completo (Windows, Linux, macOS) | RTOS, Linux bare-metal o integrado |
| **Interfaz de usuario** | Rico (pantalla, teclado, mouse) | Mínimo (LED, botones, sensores) o ninguno |
| **En tiempo real** | Mejor esfuerzo | A menudo, plazos estrictos en tiempo real |
| **Vida útil** | 3-7 años | 10-25+ años |
### Microcontroladores vs Microprocesadores
| Característica | Microcontrolador (MCU) | Microprocesador (MPU) |
|---------|----------------------|---------------------|
| **Integración** | CPU + RAM + Flash + periféricos en un chip | Sólo CPU; RAM y almacenamiento externos |
| **Rendimiento** | Baja a moderada (rango de MHz) | Alto (rango GHz) |
| **Poder** | Muy bajo (μA a mA) | Mayor (cientos de mA a amperios) |
| **Costo** | $0,10 - $10 | $5 - $100+ |
| **Ejemplos** | STM32, ESP32, Arduino (ATmega), nRF52 | Raspberry Pi (BCM2835), i.MX, Allwinner |
| **Caso de uso** | Sensores, actuadores y control sencillo | Pantallas, procesamiento complejo, Linux |
---

## Plataformas integradas comunes
| Plataforma | MCU/MPU | Característica clave | Mejor para |
|----------|---------|-------------|----------|
| **Arduino** | ATmega328P (y otros) | Simple; enorme comunidad | Aprendiendo; creación de prototipos |
| **ESP32** | Espressif de doble núcleo | Wi-Fi + Bluetooth; bajo costo | proyectos de IoT; dispositivos conectados |
| **Pi Pico de frambuesa** | RP2040 (BRAZO de doble núcleo) | Asequible; Soporte para MicroPython | Educación; proyectos de pasatiempos |
| **STM32** | Serie ARM Cortex-M | Grado industrial; amplia gama | Profesional integrado; industriales |
| **nRF52/nRF53** | Semiconductor nórdico | Especialista en Bluetooth de baja energía | Artículos portátiles; balizas |
| **Frambuesa Pi** | Broadcom BCM (ARM) | Linux completo; Pines GPIO | creación de prototipos; centros de medios; informática de borde ligero |
| **Hueso de Beagle** | TI Sitara (BRAZO) | Núcleos PRU en tiempo real | Industrial; aplicaciones en tiempo real |
| **ESP32-S3** | Expresivo | aceleración de la IA; USB | IA de vanguardia; aplicaciones de visión |
---

## Sistemas operativos en tiempo real (RTOS)
Un RTOS garantiza que las tareas críticas se completen dentro de un período de tiempo definido.
| RTOS | Licencia | Mejor para |
|------|---------|----------|
| **RTOS gratuitos** | MIT | Más común; amplio soporte MCU |
| **Céfiro** | Apache 2.0 | Moderno; Fundación Linux; ecosistema en crecimiento |
| **ThreadX (Azure RTOS)** | MIT | Certificado de seguridad; IoT |
| **embOS** | Comercial | Industrial; certificado |
| **Hilo RT** | Apache 2.0 | ecosistema chino; creciendo a nivel mundial |
### RTOS frente a metal desnudo
| Aspecto | Metal desnudo | RTOS |
|--------|-----------|------|
| **Complejidad** | Sencillo para tareas sencillas | Necesario para tareas complejas y simultáneas |
| **Programación** | Manual (bucle principal + interrupciones) | Programación preventiva con prioridades |
| **Escalabilidad** | Funciones difíciles de agregar | Tareas fáciles de agregar |
| **Memoria** | Gastos generales mínimos | Pequeños gastos generales (unos pocos KB) |
---

## Protocolos de comunicación
### Protocolos cableados
| Protocolo | Velocidad | Distancia | Caso de uso |
|----------|-------|----------|----------|
| **UART** | Hasta 1Mbps | Corto (a bordo) | Consola de depuración; Módulos GPS |
| **SPI** | Hasta 100 MHz | Corto (a bordo) | Periféricos de alta velocidad (pantallas, flash) |
| **I²C** | Hasta 3,4 MHz | Corto (a bordo) | Sensores; comunicación con bajo número de pines |
| **PUEDE** | Hasta 1Mbps | Hasta 1 km | Automotor; industriales |
| **Ethernet** | 10 Mbps - 100 Gbps | Hasta 100 metros | Establecimiento de redes; industrial (con ampliaciones) |
| **USB** | Hasta 40 Gbps (USB4) | Hasta 5 metros | Periféricos; cargando |
### Protocolos inalámbricos
| Protocolo | Gama | Poder | Velocidad | Caso de uso |
|----------|-------|-------|-------|----------|
| **Wifi** | ~100 metros | Alto | Hasta Wi-Fi 7 (46 Gbps teóricos) | IoT de gran ancho de banda; transmisión |
| **Bluetooth Clásico** | ~100 metros | Medio | 1-3Mbps | Audio; transferencia de archivos |
| **BLE** (Bluetooth de bajo consumo) | ~100 metros | Muy bajo | 1-2Mbps | Artículos portátiles; balizas; sensores |
| **Zigbee** | ~100 m (malla) | Bajo | 250 kbps | Domótica; sensores industriales |
| **Onda Z** | ~100 m (malla) | Bajo | 100 kbps | Domótica |
| **LoRa/LoRaWAN** | Hasta 15 kilómetros | Muy bajo | 0,3-50 kbps | Agricultura; servicios públicos; sensores para toda la ciudad |
| **NB-IoT** | Cobertura celular | Bajo | 250 kbps | Medida; seguimiento de activos |
| **Hilo / Materia** | ~100 m (malla) | Bajo | Moderado | Hogar inteligente (Apple, Google, Amazon) |
| **Celular (4G/5G)** | Mundial | Alto | Alto | Vehículos conectados; seguimiento remoto |
---

## Arquitectura de IoT
### La pila de IoT
| Capa | Función | Ejemplos |
|-------|----------|---------|
| **Dispositivos** | Sensores, actuadores, microcontroladores | ESP32, STM32, Frambuesa Pi |
| **Conectividad** | Protocolos de red | MQTT, HTTP, CoAP, LoRaWAN |
| **Computación de vanguardia** | Procesamiento cerca del dispositivo | AWS Greengrass, Azure IoT Edge |
| **Plataforma en la nube** | Ingestión, almacenamiento y procesamiento de datos | AWS IoT, Azure IoT Hub, Google Cloud IoT |
| **Solicitud** | Paneles, análisis, alertas | Grafana, aplicaciones web personalizadas |
### Protocolos de comunicación de IoT
| Protocolo | Patrón | Mejor para |
|----------|---------|----------|
| **MQTT** | Publicar/suscribirse; ligero | La mayoría de las aplicaciones de IoT; ancho de banda bajo |
| **HTTP/RESTO** | Solicitud/respuesta | Cuando la simplicidad importa; integración web |
| **CoAP** | Solicitud/respuesta; Basado en UDP | Dispositivos restringidos; baja potencia |
| **AMQP** | Cola de mensajes | IoT empresarial; entrega confiable |
| **WebSocket** | Bidireccional; conexión persistente | Paneles de control en tiempo real; datos en vivo |
### MQTT en detalle
| Concepto | Descripción |
|---------|-------------|
| **Corredor** | Servidor central que enruta mensajes (Mosquitto, EMQX, HiveMQ) |
| **Tema** | Dirección jerárquica (por ejemplo, `home/living-room/temperature`) |
| **QoS** | 0 (como máximo una vez), 1 (al menos una vez), 2 (exactamente una vez) |
| **Mensaje retenido** | Último mensaje sobre un tema; entregado a nuevos suscriptores |
| **Última voluntad** | Mensaje publicado cuando un cliente se desconecta inesperadamente |
---

## Computación de borde
Procesar datos cerca de la fuente en lugar de enviar todo a la nube.
| Beneficio | Descripción |
|---------|-------------|
| **Latencia reducida** | Sin ida y vuelta a la nube; decisiones inmediatas |
| **Ahorro de ancho de banda** | Enviar sólo resúmenes o anomalías |
| **Privacidad** | Los datos confidenciales permanecen en las instalaciones |
| **Confiabilidad** | Funciona cuando Internet no funciona |
| Plataforma | Descripción |
|----------|-------------|
| **AWSGreengrass** | Ejecute funciones Lambda en dispositivos perimetrales |
| **Azure IoT Edge** | Ejecute contenedores en dispositivos perimetrales |
| **NVIDIA Supersónico** | IA de borde acelerada por GPU (Orin, Nano) |
| **Frambuesa Pi** | Computación de borde liviana |
---

## Actualización de firmware (OTA)
Las actualizaciones inalámbricas le permiten corregir errores y agregar funciones a los dispositivos implementados.
| Preocupación | Solución |
|---------|----------|
| **Confiabilidad** | Flash de doble banco; revertir el fracaso |
| **Seguridad** | Imágenes firmadas; transferencias cifradas |
| **Tamaño** | Actualizaciones delta (solo partes modificadas) |
| **Conectividad** | Cola de actualizaciones para cuando el dispositivo se conecte |
---

## Sistemas integrados críticos para la seguridad
| Dominio | Estándares | Ejemplos |
|--------|-----------|---------|
| **Automoción** | ISO 26262 (ASIL A-D) | Control del motor, frenado, airbags |
| **Médico** | CEI 62304 | Marcapasos, bombas de infusión |
| **Aeroespacial** | DO-178C (DAL A-E) | Control de vuelo, navegación |
| **Industriales** | IEC 61508 (SIL 1-4) | PLC, controladores de seguridad |
| **Ferrocarril** | EN 50128 (SIL 1-4) | Señalización y control de trenes |
---

## Herramientas y desarrollo
| Herramienta | Propósito |
|------|---------|
| **PlataformaIO** | Desarrollo embebido multiplataforma (Arduino, ESP32, STM32) |
| **STM32CubeIDE** | IDE oficial de ST para STM32 |
| **ArduinoIDE** | Desarrollo sencillo para Arduino y placas compatibles |
| **ESP-IDF** | SDK oficial de Espressif para ESP32 |
| **SDK de Zephyr** | Sistema de construcción West para Zephyr RTOS |
| **OpenOCD** | Depuración en chip |
| **Analizador lógico** | Depuración de protocolos SPI, I²C, UART |
| **Wireshark** | Análisis de protocolos de red |
---

## Resumen
Los sistemas integrados y el IoT representan la intersección del software y el mundo físico. Desde microcontroladores que controlan motores hasta redes de sensores conectados a la nube, requieren una mentalidad diferente a la del desarrollo web o de aplicaciones: recursos limitados, requisitos en tiempo real, vidas útiles prolongadas y consecuencias de los errores en el mundo físico. El ecosistema ha madurado enormemente: marcos como ESP-IDF y Zephyr hacen accesible el desarrollo profesional, mientras que plataformas como AWS IoT y Azure IoT Hub se encargan del lado de la nube. Las habilidades clave son comprender las interfaces de hardware, los protocolos de comunicación, la administración de energía y la disciplina para escribir software que debe funcionar de manera confiable durante años sin intervención.