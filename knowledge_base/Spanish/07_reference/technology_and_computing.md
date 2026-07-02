<!-- 
This file was automatically translated from English to Spanish.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Tecnología y Informática

# # What is a Computer?

A computer is an electronic device that processes Datos according to a set de instructions called a program. Modern computers are based on el/la von Neumann Arquitectura, which consists de a central processing unit (CPU), memory, storage, y input/output devices. el/la CPU executes instructions. RAM (random access memory) stores Datos temporarily while el/la computer is running. Storage devices such as SSDs y hard drives store Datos permanently.

# # Programming Languages

A programming Idioma is a formal Idioma used to write instructions para computers. Python is a high-level, interpreted, general-purpose programming Idioma known para its simple Sintaxis y readability. It is widely used en Datos Ciencia, Aprendizaje automático, Web Desarrollo, y automation. JavaScript is el/la primary Idioma para Web Desarrollo y runs en browsers. Java is a compiled, object-oriented Idioma used widely en enterprise software y Android Desarrollo. C y C++ are lower-level languages that give fine-grained control over hardware y are used en system programming, game Desarrollo, y Rendimiento-critical applications. Rust is a modern Sistemas programming Idioma focused on safety y Rendimiento.

# # How el/la Internet Works

el/la internet is a global Red de interconnected computers that communicate using standardized protocols. el/la World Wide Web is a system de websites y Web pages accessed through el/la internet via browsers. HTTP (HyperText Transfer Protocol) y HTTPS (secure HTTP) are el/la protocols used to transfer Web pages. An IP address is a unique numerical address assigned to each device on a Red. DNS (Domain Name System) translates human-readable domain names (like google.com) into IP addresses. A router directs Red traffic between devices y networks.

# # Networking y Protocols

TCP/IP is el/la foundational protocol suite de el/la internet. IP (Internet Protocol) handles addressing y routing packets between networks, while TCP (Transmission Control Protocol) provides reliable, ordered delivery con retransmission y flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (para example en streaming, gaming, or DNS queries). HTTP is a stateless application-layer protocol para request/response Comunicación between clients y servers. HTTPS is HTTP over TLS, adding encryption y integrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, standard HTTP verbs (GET, POST, PUT, PATCH, DELETE), y stateless interactions. WebSockets provide persistent, full-duplex connections so client y server can push messages en real time, which is useful para chat, live dashboards, y collaborative apps.

# # Artificial Intelligence

Artificial intelligence (AI) is el/la simulation de human intelligence by machines, particularly computer Sistemas. Aprendizaje automático is a subset de AI en which Sistemas learn from Datos to make predictions or decisions without being explicitly programmed. Aprendizaje profundo is a subset de Aprendizaje automático that uses Redes neuronales con many layers. Redes neuronales are computational models loosely inspired by el/la structure de biological brains. Large Idioma models (LLMs) are AI models trained on massive amounts de text to generate y understand natural Idioma.

# # Algorithms y Datos Structures

An algorithm is a step-by-step procedure para solving a problem. Datos structures are ways de organizing Datos en a computer so that it can be accessed y modified efficiently. Common Datos structures include arrays, linked lists, stacks, queues, trees, graphs, y hash tables. Sorting algorithms arrange items en a specified order; common Ejemplos are bubble sort, merge sort, y quicksort. Binary search is an efficient algorithm para finding an item en a sorted list by repeatedly halving el/la search range.

# # Databases

A Base de datos is an organized collection de structured Datos stored electronically. A relational Base de datos stores Datos en tables con rows y columns. SQL (Structured Query Idioma) is el/la standard Idioma para managing y querying relational databases. NoSQL databases store Datos en formats other than tabular relations, such as documents, key-value pairs, or graphs. Common Base de datos Sistemas include PostgreSQL, MySQL, SQLite, MongoDB, y Redis. An index en a Base de datos speeds up Datos retrieval at el/la cost de extra storage.

# # System Design Fundamentos

System design focuses on building reliable, scalable, y maintainable software Sistemas. Load balancing distributes traffic across multiple servers to improve availability y reduce latency. Horizontal scaling adds more machines; vertical scaling adds more resources to one machine. Caching stores frequently accessed Datos en fast storage (para example Redis, Memcached, or CDN edge caches) to reduce Base de datos load y response time. Databases at scale require replication, partitioning (sharding), backup strategies, y careful consistency tradeoffs. Microservices split large applications into smaller independently deployable services, while monoliths keep most logic en one deployable unit; both approaches involve tradeoffs en complexity, Implementación speed, debugging, y team autonomy.

# # Operating Sistemas

An operating system (OS) is software that manages computer hardware y provides services para programs. Common operating Sistemas include Windows, macOS, y Linux. Linux is an open-source OS kernel used en servers, embedded Sistemas, y Android. el/la OS manages processes (running programs), memory, file Sistemas, y input/output devices. A process is a running instance de a program. A thread is el/la smallest unit de execution within a process.

# # Version Control

Version control Sistemas track changes to code over time, allowing developers to collaborate y revert to previous states. Git is el/la most widely used version control system. A repository (repo) is a collection de files y their Historia. A commit is a saved snapshot de changes. A branch is an independent line de Desarrollo. A pull request is a proposal to merge changes from one branch into another.

# # Software Desarrollo Practices

Object-oriented programming (OOP) organizes code into objects that combine Datos y behavior. Key principles de OOP include encapsulation, inheritance, polymorphism, y abstraction. Test-driven Desarrollo (TDD) is a practice de writing tests before writing code. Agile is a set de software Desarrollo methodologies that emphasize iterative Desarrollo, collaboration, y adaptability. DevOps combines software Desarrollo y IT operations to shorten el/la Desarrollo lifecycle. APIs (Application Programming Interfaces) allow different software Sistemas to communicate con each other.

# # Cloud y DevOps Conceptos básicos

Cloud Informática provides on-demand infrastructure y managed services over el/la internet. el/la three major public cloud providers are AWS (Amazon Web Services), Microsoft Azure, y Google Cloud Platform (GCP). Common service models are IaaS (infrastructure), PaaS (platform), y SaaS (software). Core cloud building blocks include compute instances/containers, object storage, managed databases, networking, y IAM (Identity y Access Gestión). CI/CD (Continuous Integration y Continuous Delivery/Implementación) automates build, test, y release pipelines so code can move safely from commit to production. Docker packages applications y dependencies into portable containers; en production these containers are typically deployed via orchestrators (such as Kubernetes), serverless platforms, or managed container services.

# # Datos Formats y Tooling

JSON (JavaScript Object Notation) is a lightweight text format built from objects (key/value pairs), arrays, strings, numbers, booleans, y null; it is widely used en APIs. YAML is a human-friendly configuration format that supports nested structures y comments, commonly used en CI/CD y infrastructure definitions. CSV (Comma-Separated Values) stores tabular Datos as rows de delimited text y is common para Datos import/export pipelines. XML (eXtensible Markup Idioma) is a tag-based structured format used en legacy Sistemas, configuration, y document workflows. Developers commonly validate y transform these formats con linters, schema validators (such as JSON Schema), query tools (`jq`, XPath), y parsing libraries en their programming Idioma.

# # Regular Expressions (Regex)

A regular expression is a pattern Idioma used to search, match, extract, y transform text. Core regex concepts include literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), y escaping special characters. Regex is heavily used para input validation, log parsing, text extraction, y find/replace automation. Different engines (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested y documented to avoid bugs.

# # Cybersecurity

Cybersecurity is el/la practice de protecting computer Sistemas, networks, y Datos from digital attacks. Common threats include malware (malicious software), phishing (fraudulent Comunicación designed to steal information), ransomware (malware that encrypts Datos y demands payment), y denial-de-service attacks. Encryption transforms Datos into an unreadable form that can only be decoded con a key. HTTPS uses TLS (Transport Layer Seguridad) to encrypt Web traffic. Strong, unique passwords y two-factor authentication are fundamental Seguridad practices.

# # Seguridad Concepts para Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application without sharing credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 para authentication. JWT (JSON Web Token) is a compact token format containing claims, often used para stateless auth, but it must be signed correctly y validated strictly (signature, expiration, issuer, audience). TLS secures Datos en transit by providing encryption, integrity, y server authentication through certificates. el/la OWASP Top 10 is a widely used list de common Web application Seguridad risks, including broken access control, cryptographic failures, injection, insecure design, Seguridad misconfiguration, vulnerable components, y insufficient logging/monitoring. Secure Desarrollo requires defense-en-depth: input validation, output encoding, least privilege, secret Gestión, dependency patching, y regular Seguridad Pruebas.
