---
# Metadata
title: "Technology and Computing"
description: "Computing basics, internet, databases, cloud, security"
category: "General Reference"
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
# Tecnología y Computación
La informática está en todas partes: en su teléfono, su automóvil, su refrigerador, sus dispositivos médicos y la infraestructura que rige la sociedad moderna. No es necesario ser programador para comprender cómo funciona todo. Este archivo cubre los fundamentos: qué es una computadora, cómo funciona Internet, cómo se construye el software y los conceptos que dan forma al mundo digital.
> **¿Quieres profundizar más?** Este archivo es una descripción general amplia. Para obtener una cobertura detallada de cualquier tema, consulte los archivos dedicados en [`01_coding_and_technology/`](../01_coding_and_technology/), incluidos [database systems](../01_coding_and_technology/database_systems.md), [cloud architecture](../01_coding_and_technology/cloud_architecture.md),[networking](../01_coding_and_technology/networking_basics.md)y.
---

## ¿Qué es una computadora?
En esencia, cada computadora, desde un teléfono inteligente hasta una supercomputadora, hace lo mismo: toma información, la procesa de acuerdo con instrucciones (un programa) y produce una salida. La magia está en la velocidad y la escala.
### La arquitectura de Von Neumann
Casi todas las computadoras modernas siguen este diseño básico:
| Componente | Qué hace | Analogía |
|-----------|-------------|---------|
| **CPU** (Unidad central de procesamiento) | Ejecuta instrucciones; el "cerebro" | El chef siguiendo una receta |
| **RAM** (Memoria) | Almacena datos que la CPU está utilizando activamente; se pierde cuando se corta la energía | La encimera: acceso rápido, espacio limitado |
| **Almacenamiento** (SSD/HDD) | Almacena datos de forma permanente | La despensa: acceso más lento, mucho más espacio |
| **Entrada/Salida** | Teclado, ratón, pantalla, red | Cómo el chef recibe pedidos y entrega la comida |
| **GPU** (Unidad de procesamiento de gráficos) | Procesador especializado para tareas paralelas (gráficos, IA) | Un equipo de asistentes haciendo todos la misma tarea simultáneamente |
**Información clave**: la RAM es rápida pero temporal. El almacenamiento es lento pero permanente. Cuando su computadora "se siente lenta", a menudo se debe a que se está quedando sin RAM y tiene que usar el almacenamiento como memoria temporal (intercambio), que es mucho más lenta.
---

## Lenguajes de programación: hablar con las computadoras
Un lenguaje de programación es un conjunto de instrucciones que una computadora puede ejecutar. Diferentes idiomas están diseñados para diferentes propósitos. Para obtener una cobertura detallada de 34 idiomas individuales, consulte la carpeta [`programming_languages/`](../01_coding_and_technology/programming_languages/).
| Idioma | Mejor para | Por qué elegirlo |
|----------|---------|---------------|
| **Python** | Ciencia de datos, IA, automatización, backends web | Sintaxis sencilla; enorme ecosistema; ideal para principiantes |
| **JavaScript** | Interfaces web, pila completa (Node.js) | Se ejecuta en todos los navegadores; esencial para el desarrollo web |
| **Java** | Software empresarial, aplicaciones de Android | Independiente de plataforma (JVM); gran ecosistema |
| **C/C++** | Programación de sistemas, juegos embebidos | Máximo rendimiento; control directo de hardware |
| **Óxido** | Programación de sistemas con garantías de seguridad | Seguridad de la memoria sin recolección de basura |
| **Ir** | Servicios en la nube, microservicios, herramientas CLI | Simple; excelente concurrencia; compilación rápida |
| **SQL** | Consultas a bases de datos | El lenguaje universal para trabajar con datos |
| **Mecanografiado** | Aplicaciones web a gran escala | JavaScript con verificación de tipos; detecta errores temprano |
---

## Cómo funciona Internet
Internet no es lo mismo que la web. Internet es la red física: cables, enrutadores, servidores y protocolos que conectan miles de millones de dispositivos. La World Wide Web es un servicio que se ejecuta en Internet (junto con el correo electrónico, la transferencia de archivos, la transmisión por secuencias, los juegos, etc.).
### El viaje de una solicitud web
Cuando escribes`https://www.example.com`en tu navegador:
1. **Búsqueda de DNS**: su navegador solicita a un servidor DNS que traduzca "www.example.com" a una dirección IP (como 93.184.216.34).
2. **Conexión TCP**: Su dispositivo establece una conexión a esa dirección IP mediante TCP (un protocolo que garantiza una entrega confiable).
3. **Apretón de manos TLS**: si utiliza HTTPS, su navegador y el servidor negocian una conexión cifrada.
4. **Solicitud HTTP**: su navegador envía una solicitud: "Dame la página en /index.html".
5. **Procesamiento del servidor**: el servidor web encuentra la página, posiblemente consulta una base de datos y prepara una respuesta.
6. **Respuesta HTTP**: el servidor devuelve HTML, CSS y JavaScript.
7. **Representación**: su navegador analiza el HTML, aplica estilos CSS y ejecuta JavaScript para mostrar la página.
Todo este proceso suele tardar menos de un segundo.
### Protocolos clave
| Protocolo | Qué hace | Capa |
|----------|-------------|-------|
| **IP** (Protocolo de Internet) | Enruta paquetes entre redes | Red |
| **TCP** | Entrega confiable y ordenada (retransmite paquetes perdidos) | Transporte |
| **UDP** | Entrega rápida y poco fiable (sin retransmisión) | Transporte |
| **HTTP/HTTPS** | Transferencia de páginas web (HTTPS agrega cifrado) | Solicitud |
| **DNS** | Traduce nombres de dominio a direcciones IP | Solicitud |
| **SSH** | Acceso remoto seguro a ordenadores | Solicitud |
| **SMTP/IMAP** | Envío y recepción de correo electrónico | Solicitud |
---

## Desarrollo de software: cómo se crean los programas
### El proceso de desarrollo
1. **Escribir código**: los desarrolladores escriben instrucciones en un lenguaje de programación.
2. **Código de prueba**: ejecute el código para verificar que funciona correctamente.
3. **Control de versiones**: realice un seguimiento de los cambios utilizando Git, el estándar universal.
4. **Revisión**: Otros desarrolladores verifican el código en busca de errores y calidad.
5. **Compilar**: convierte el código fuente en un programa ejecutable (compilación).
6. **Implementar**: Lanzar el programa a los usuarios (servidores, tiendas de aplicaciones, etc.).
7. **Monitorear**: esté atento a errores y problemas de rendimiento en producción.
### Conceptos clave
| Concepto | Lo que significa | Por qué es importante |
|---------|---------------|----------------|
| **Control de versiones (Git)** | Realice un seguimiento de cada cambio en el código a lo largo del tiempo | Colaboración; capacidad de deshacer errores |
| **API** (Interfaz de programación de aplicaciones) | Una forma definida para que los componentes de software se comuniquen | Permite que diferentes sistemas trabajen juntos |
| **Base de datos** | Almacenamiento organizado de datos | Cada aplicación necesita almacenar y recuperar datos |
| **Pruebas** | Comprobaciones automatizadas de que el código funciona correctamente | Evita que los errores lleguen a los usuarios |
| **CI/CD** (Integración/entrega continua) | Canalización automatizada desde el compromiso del código hasta la producción | Lanzamientos más rápidos y seguros |
| **Contenedorización (Docker)** | Empaquetar una aplicación con todas sus dependencias | "Funciona en mi máquina" se convierte en "funciona en todas partes" |
---

## Bases de datos: dónde residen los datos
Cada aplicación necesita almacenar datos. Las bases de datos son los sistemas que hacen esto de manera eficiente y confiable.
| Tipo | Cómo se almacenan los datos | Mejor para | Ejemplos |
|------|-------------------|----------|---------|
| **Relacional (SQL)** | Tablas con filas y columnas; esquema estricto | Datos estructurados; consultas complejas; transacciones | PostgreSQL, MySQL, SQLite |
| **Documento (NoSQL)** | Documentos tipo JSON; esquema flexible | Datos semiestructurados; iteración rápida | MongoDB, CouchDB |
| **Clave-valor** | Clave simple → pares de valores | Almacenamiento en caché; almacenamiento de sesiones; búsquedas rápidas | Redis, DynamoDB |
| **Gráfico** | Nodos y aristas (relaciones) | Redes sociales; motores de recomendación | Neo4j, JanusGraph |
| **Series temporales** | Optimizado para datos con marca de tiempo | Escucha; analítica; IoT | InfluxDB, escala de tiempoDB |
**SQL** (lenguaje de consulta estructurado) es el lenguaje estándar para bases de datos relacionales. Es una de las habilidades técnicas más valiosas que puede aprender: casi todas las organizaciones utilizan bases de datos y SQL es la forma de hablar con ellas.
---

## Sistemas operativos
El sistema operativo (SO) es la capa de software entre usted (y sus programas) y el hardware. Gestiona memoria, procesos, archivos y dispositivos.
| SO | Donde domina | Característica clave |
|----|-------------------|-------------|
| **Windows** | PC de escritorio/portátiles (~72% de participación de mercado) | La más amplia compatibilidad de software/hardware |
| **macOS** | Profesionales creativos, desarrolladores | Basado en Unix; interfaz de usuario pulida; Ecosistema de Apple |
| **Linux** | Servidores (~96%), supercomputadoras (100%), integrados, desarrolladores | Código abierto; gratis; extremadamente personalizable |
| **Android** | Móvil (~72% de cuota de mercado global) | Basado en el kernel de Linux; código abierto |
| **iOS** | Móvil (~27% global, pero mayores ingresos) | Ecosistema cerrado; pulido; centrado en la privacidad |
Linux merece una mención especial: impulsa la mayor parte de Internet, todas las 500 supercomputadoras principales, la mayor parte de la infraestructura en la nube y todos los teléfonos Android. Es gratuito, de código abierto y mantenido por una comunidad global.
---

## Computación en la nube
La computación en la nube significa alquilar recursos informáticos (servidores, almacenamiento, bases de datos, etc.) a través de Internet en lugar de comprar y mantener su propio hardware. Para obtener una guía completa sobre la arquitectura de la nube, los modelos de servicios y las comparaciones de proveedores, consulte [cloud architecture](../01_coding_and_technology/cloud_architecture.md).
| Modelo de Servicio | Lo que obtienes | Analogía | Ejemplos |
|---------------|-------------|---------|---------|
| **IaaS** (Infraestructura) | Servidores virtuales, almacenamiento, redes | Alquilar un terreno y construir lo que quieras | AWS EC2, Google Compute Engine |
| **PaaS** (Plataforma) | Entorno de ejecución; traes codigo | Alquilar un apartamento amueblado | Heroku, motor de aplicaciones de Google |
| **SaaS** (Software) | Solicitud completa; solo lo usas | Alojarse en un hotel | Gmail, Slack, Salesforce |
Los tres principales proveedores de nube son **AWS** (Amazon, ~32 % de participación de mercado), **Azure** (Microsoft, ~23 %) y **GCP** (Google, ~10 %). Ofrecen cientos de servicios que cubren computación, almacenamiento, bases de datos, inteligencia artificial, redes y más.
---

## Ciberseguridad: protección de los sistemas digitales
La ciberseguridad es la práctica de defender las computadoras, las redes y los datos de los ataques. Es importante porque todo está conectado y el costo de las infracciones es enorme. Para obtener una guía completa que cubre OWASP Top 10, el ciclo de vida de desarrollo seguro y la gestión de secretos, consulte.
### Amenazas comunes
| Amenaza | Qué es | Prevención |
|--------|-----------|------------|
| **Malware** | Software malicioso (virus, gusanos, troyanos) | antivirus; mantener el software actualizado |
| **Suplantación de identidad** | Correos electrónicos/mensajes falsos que te engañan para que reveles información | Capacitación; filtrado de correo electrónico; escepticismo |
| **Ransomware** | Cifra sus datos; exige pago por la llave | Copias de seguridad; sistemas de parches; no pagues |
| **DDoS** | Abruma un servicio con tráfico | Filtrado de tráfico; Protección CDN |
| **Inyección SQL** | Insertar SQL malicioso en campos de entrada | Consultas parametrizadas; validación de entrada |
| **Hombre en el medio** | Interceptar la comunicación entre dos partes | Cifrado HTTPS/TLS |
### Fundamentos de seguridad
- **Cifrado**: codifica los datos para que solo las personas autorizadas puedan leerlos. HTTPS utiliza TLS para cifrar el tráfico web.
- **Autenticación**: Verificar identidad. Utilice autenticación multifactor (MFA): contraseña + algo más (código, biométrico).
- **Autorización**: Verificar permisos. El hecho de que haya iniciado sesión no significa que deba acceder a todo.
- **Principio de privilegio mínimo**: brinde a los usuarios y sistemas solo el acceso que necesitan, nada más.
- **Gestión de parches**: mantenga el software actualizado. La mayoría de las infracciones aprovechan vulnerabilidades conocidas que ya cuentan con parches.
---

## Formatos de datos
Los programas intercambian datos en formatos específicos. Los más comunes:
| Formato | Estructura | Utilizado para |
|--------|-----------|----------|
| **JSON** | Pares clave-valor; legible por humanos | API; configuración; intercambio de datos |
| **XML** | Basado en etiquetas; detallado pero flexible | Sistemas heredados; documentos; API de SOAP |
| **YAML** | Basado en sangría; muy legible | Configuración (Docker, Kubernetes, CI/CD) |
| **CSV** | Filas y columnas de texto sin formato | Importación/exportación de datos; hojas de cálculo |
---

## Resumen
La informática no es magia, es ingeniería. Las computadoras siguen instrucciones a una velocidad increíble. Internet conecta a miles de millones de ellos mediante protocolos estandarizados. El software lo crean equipos de personas que escriben, prueban e implementan código en ciclos iterativos. Las bases de datos almacenan y recuperan datos. La computación en la nube permite a cualquiera acceder a recursos informáticos masivos bajo demanda. Y la ciberseguridad es la batalla constante para mantener todo esto a salvo de las personas que quieren explotarlo. Comprender estos fundamentos le ayuda a navegar en el mundo digital, ya sea que sea un usuario, un desarrollador o simplemente alguien que intenta darle sentido a la tecnología que da forma a la vida moderna.