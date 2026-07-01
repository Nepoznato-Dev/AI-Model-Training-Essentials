<!-- 
Este archivo fue traducido automáticamente del inglés al español.
Fuente: technology_and_computing.md
Nota: Los términos técnicos, ejemplos de código y nombres propios pueden permanecer en inglés.
Para mejorar la precisión, por favor contribuya con ediciones mediante pull requests.
-->

# Tecnología y Computación

## ¿Qué es una Computadora?

Una computadora es un dispositivo electrónico que procesa datos según un conjunto de instrucciones llamado programa. Las computadoras modernas se basan en la arquitectura de von Neumann, que consiste en una unidad central de procesamiento (CPU), memoria, almacenamiento y dispositivos de entrada/salida. La CPU ejecuta instrucciones. La RAM (memoria de acceso aleatorio) almacena datos temporalmente mientras la computadora está funcionando. Los dispositivos de almacenamiento como SSDs y discos duros almacenan datos permanentemente.

## Lenguajes de Programación

Un lenguaje de programación es un lenguaje formal utilizado para escribir instrucciones para computadoras. Python es un lenguaje de programación de alto nivel, interpretado y de propósito general, conocido por su sintaxis simple y legibilidad. Es ampliamente utilizado en ciencia de datos, aprendizaje automático, desarrollo web y automatización. JavaScript es el lenguaje principal para desarrollo web y se ejecuta en navegadores. Java es un lenguaje compilado y orientado a objetos, ampliamente utilizado en software empresarial y desarrollo para Android. C y C++ son lenguajes de nivel más bajo que dan control de grano fino sobre el hardware y se utilizan en programación de sistemas, desarrollo de videojuegos y aplicaciones críticas de rendimiento. Rust es un lenguaje moderno de programación de sistemas enfocado en seguridad y rendimiento.

## Cómo Funciona Internet

Internet es una red global de computadoras interconectadas que se comunican utilizando protocolos estandarizados. La World Wide Web es un sistema de sitios web y páginas web accesibles a través de Internet mediante navegadores. HTTP (Protocolo de Transferencia de Hipertexto) y HTTPS (HTTP seguro) son los protocolos utilizados para transferir páginas web. Una dirección IP es una dirección numérica única asignada a cada dispositivo en una red. DNS (Sistema de Nombres de Dominio) traduce nombres de dominio legibles por humanos (como google.com) a direcciones IP. Un router dirige el tráfico de red entre dispositivos y redes.

## Redes y Protocolos

TCP/IP es la suite de protocolos fundamental de Internet. IP (Protocolo de Internet) maneja el direccionamiento y enrutamiento de paquetes entre redes, mientras que TCP (Protocolo de Control de Transmisión) proporciona entrega confiable y ordenada con retransmisión y control de flujo. UDP es una alternativa sin conexión utilizada cuando la baja latencia es más importante que la entrega garantizada (por ejemplo, en streaming, juegos o consultas DNS). HTTP es un protocolo de capa de aplicación sin estado para comunicación de solicitud/respuesta entre clientes y servidores. HTTPS es HTTP sobre TLS, agregando cifrado y protección de integridad. REST (Transferencia de Estado Representacional) es un estilo arquitectónico de API que utiliza recursos, verbos HTTP estándar (GET, POST, PUT, PATCH, DELETE) e interacciones sin estado. WebSockets proporciona conexiones persistentes y dúplex completas para que cliente y servidor puedan enviar mensajes en tiempo real, lo cual es útil para chat, paneles en vivo y aplicaciones colaborativas.

## Inteligencia Artificial

La inteligencia artificial (IA) es la simulación de inteligencia humana por máquinas, particularmente sistemas informáticos. El aprendizaje automático es un subconjunto de IA en el cual los sistemas aprenden de datos para hacer predicciones o decisiones sin ser programados explícitamente. El aprendizaje profundo es un subconjunto del aprendizaje automático que utiliza redes neuronales con muchas capas. Las redes neuronales son modelos computacionales vagamente inspirados en la estructura de cerebros biológicos. Los modelos de lenguaje grandes (LLMs) son modelos de IA entrenados en cantidades masivas de texto para generar y comprender lenguaje natural.

## Algoritmos y Estructuras de Datos

Un algoritmo es un procedimiento paso a paso para resolver un problema. Las estructuras de datos son formas de organizar datos en una computadora para que puedan accederse y modificarse eficientemente. Las estructuras de datos comunes incluyen arreglos, listas enlazadas, pilas, colas, árboles, grafos y tablas hash. Los algoritmos de ordenamiento organizan elementos en un orden especificado; ejemplos comunes son bubble sort, merge sort y quicksort. La búsqueda binaria es un algoritmo eficiente para encontrar un elemento en una lista ordenada dividiendo repetidamente el rango de búsqueda a la mitad.

## Bases de Datos

Una base de datos es una colección organizada de datos estructurados almacenados electrónicamente. Una base de datos relacional almacena datos en tablas con filas y columnas. SQL (Lenguaje de Consulta Estructurado) es el lenguaje estándar para gestionar y consultar bases de datos relacionales. Las bases de datos NoSQL almacenan datos en formatos distintos a las relaciones tabulares, como documentos, pares clave-valor o grafos. Los sistemas de bases de datos comunes incluyen PostgreSQL, MySQL, SQLite, MongoDB y Redis. Un índice en una base de datos acelera la recuperación de datos a costa de almacenamiento adicional.

## Fundamentos de Diseño de Sistemas

El diseño de sistemas se enfoca en construir sistemas de software confiables, escalables y mantenibles. El balanceo de carga distribuye el tráfico entre múltiples servidores para mejorar la disponibilidad y reducir la latencia. El escalado horizontal agrega más máquinas; el escalado vertical agrega más recursos a una máquina. El caché almacena datos frecuentemente accedidos en almacenamiento rápido (por ejemplo Redis, Memcached o cachés de borde CDN) para reducir la carga de la base de datos y el tiempo de respuesta. Las bases de datos a escala requieren replicación, particionamiento (sharding), estrategias de respaldo y compensaciones cuidadosas de consistencia. Los microservicios dividen aplicaciones grandes en servicios más pequeños e independientemente desplegables, mientras que los monolitos mantienen la mayor parte de la lógica en una unidad desplegable; ambos enfoques involucran compensaciones en complejidad, velocidad de implementación, depuración y autonomía del equipo.

## Sistemas Operativos

Un sistema operativo (SO) es software que gestiona el hardware de la computadora y proporciona servicios para programas. Los sistemas operativos comunes incluyen Windows, macOS y Linux. Linux es un kernel de SO de código abierto utilizado en servidores, sistemas embebidos y Android. El SO gestiona procesos (programas en ejecución), memoria, sistemas de archivos y dispositivos de entrada/salida. Un proceso es una instancia en ejecución de un programa. Un hilo es la unidad más pequeña de ejecución dentro de un proceso.

## Control de Versiones

Los sistemas de control de versiones rastrean cambios en el código a lo largo del tiempo, permitiendo a los desarrolladores colaborar y revertir a estados anteriores. Git es el sistema de control de versiones más ampliamente utilizado. Un repositorio (repo) es una colección de archivos y su historial. Un commit es una instantánea guardada de cambios. Una rama es una línea de desarrollo independiente. Una pull request es una propuesta para fusionar cambios de una rama a otra.

## Prácticas de Desarrollo de Software

La programación orientada a objetos (POO) organiza el código en objetos que combinan datos y comportamiento. Los principios clave de POO incluyen encapsulamiento, herencia, polimorfismo y abstracción. El desarrollo guiado por pruebas (TDD) es una práctica de escribir pruebas antes de escribir código. Agile es un conjunto de metodologías de desarrollo de software que enfatizan el desarrollo iterativo, la colaboración y la adaptabilidad. DevOps combina el desarrollo de software y las operaciones de TI para acortar el ciclo de vida del desarrollo. Las APIs (Interfaces de Programación de Aplicaciones) permiten que diferentes sistemas de software se comuniquen entre sí.

## Conceptos Básicos de Cloud y DevOps

La computación en la nube proporciona infraestructura bajo demanda y servicios gestionados a través de Internet. Los tres principales proveedores de nube pública son AWS (Amazon Web Services), Microsoft Azure y Google Cloud Platform (GCP). Los modelos de servicio comunes son IaaS (infraestructura), PaaS (plataforma) y SaaS (software). Los bloques de construcción fundamentales de la nube incluyen instancias de cómputo/contenedores, almacenamiento de objetos, bases de datos gestionadas, redes e IAM (Gestión de Identidad y Acceso). CI/CD (Integración Continua y Entrega/Despliegue Continuo) automatiza las tuberías de construcción, prueba y lanzamiento para que el código pueda moverse seguramente desde commit a producción. Docker empaqueta aplicaciones y dependencias en contenedores portátiles; en producción estos contenedores generalmente se despliegan mediante orquestadores (como Kubernetes), plataformas serverless o servicios de contenedores gestionados.

## Formatos de Datos y Herramientas

JSON (Notación de Objetos de JavaScript) es un formato de texto ligero construido a partir de objetos (pares clave/valor), arreglos, cadenas, números, booleanos y null; es ampliamente utilizado en APIs. YAML es un formato de configuración amigable para humanos que soporta estructuras anidadas y comentarios, comúnmente utilizado en CI/CD y definiciones de infraestructura. CSV (Valores Separados por Comas) almacena datos tabulares como filas de texto delimitado y es común para tuberías de importación/exportación de datos. XML (Lenguaje de Marcado Extensible) es un formato estructurado basado en etiquetas utilizado en sistemas heredados, configuración y flujos de trabajo de documentos. Los desarrolladores comúnmente validan y transforman estos formatos con linters, validadores de esquema (como JSON Schema), herramientas de consulta (`jq`, XPath) y bibliotecas de análisis en su lenguaje de programación.

## Expresiones Regulares (Regex)

Una expresión regular es un lenguaje de patrones utilizado para buscar, coincidir, extraer y transformar texto. Los conceptos centrales de regex incluyen literales (`cat`), clases de caracteres (`[a-z]`, `\\d`), cuantificadores (`*`, `+`, `?`, `{n,m}`), anclajes (`^`, `$`), grupos (`(...)`), alternación (`a|b`) y escape de caracteres especiales. Regex se utiliza intensivamente para validación de entrada, análisis de registros, extracción de texto y automatización de búsqueda/reemplazo. Diferentes motores (PCRE, JavaScript, Python `re`, RE2) tienen diferentes conjuntos de características, por lo que el comportamiento puede variar entre herramientas. Regex es poderoso pero puede volverse difícil de leer; los patrones complejos deben probarse y documentarse para evitar errores.

## Ciberseguridad

La ciberseguridad es la práctica de proteger sistemas informáticos, redes y datos de ataques digitales. Las amenazas comunes incluyen malware (software malicioso), phishing (comunicación fraudulenta diseñada para robar información), ransomware (malware que cifra datos y exige pago) y ataques de denegación de servicio. El cifrado transforma datos en un formato ilegible que solo puede decodificarse con una clave. HTTPS utiliza TLS (Seguridad de Capa de Transporte) para cifrar el tráfico web. Contraseñas fuertes y únicas junto con autenticación de dos factores son prácticas fundamentales de seguridad.

## Conceptos de Seguridad para Desarrolladores

OAuth 2.0 es un marco de autorización que permite a los usuarios otorgar acceso limitado a una aplicación sin compartir credenciales directamente. OpenID Connect (OIDC) es una capa de identidad construida sobre OAuth 2.0 para autenticación. JWT (Token Web JSON) es un formato de token compacto que contiene reclamaciones, utilizado para autenticación sin estado, pero debe firmarse correctamente y validarse estrictamente (firma, expiración, emisor, audiencia). TLS asegura datos en tránsito proporcionando cifrado, integridad y autenticación del servidor mediante certificados. El OWASP Top 10 es una lista ampliamente utilizada de riesgos comunes de seguridad en aplicaciones web, incluyendo control de acceso roto, fallos criptográficos, inyección, diseño inseguro, configuración incorrecta de seguridad, componentes vulnerables y registro/monitoreo insuficiente. El desarrollo seguro requiere defensa en profundidad: validación de entrada, codificación de salida, mínimo privilegio, gestión de secretos, parcheo de dependencias y pruebas de seguridad regulares.
