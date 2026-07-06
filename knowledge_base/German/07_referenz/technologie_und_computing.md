<!-- 
This file was automatically translated from English to German.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Technologie und Datenverarbeitung

## What is a Computer?

A computer is an electronic device that processes Daten according to a set von instructions called a program. Modern computers are based on der/die/das von Neumann Architektur, which consists von a central processing unit (CPU), memory, storage, und input/output devices. der/die/das CPU executes instructions. RAM (random access memory) stores Daten temporarily while der/die/das computer is running. Storage devices such as SSDs und hard drives store Daten permanently.

## Programming Languages

A programming Sprache is a formal Sprache used to write instructions für computers. Python is a high-level, interpreted, general-purpose programming Sprache known für its simple Syntax und readability. It is widely used in Daten Wissenschaft, Maschinelles Lernen, Web Entwicklung, und automation. JavaScript is der/die/das primary Sprache für Web Entwicklung und runs in browsers. Java is a compiled, object-oriented Sprache used widely in enterprise software und Android Entwicklung. C und C++ are lower-level languages that give fine-grained control over hardware und are used in system programming, game Entwicklung, und Leistung-critical applications. Rust is a modern Systeme programming Sprache focused on safety und Leistung.

## How der/die/das Internet Works

der/die/das internet is a global Netzwerk von interconnected computers that communicate using standardized protocols. der/die/das World Wide Web is a system von websites und Web pages accessed through der/die/das internet via browsers. HTTP (HyperText Transfer Protocol) und HTTPS (secure HTTP) are der/die/das protocols used to transfer Web pages. An IP address is a unique numerical address assigned to each device on a Netzwerk. DNS (Domain Name System) translates human-readable domain names (like google.com) into IP addresses. A router directs Netzwerk traffic between devices und networks.

## Networking und Protocols

TCP/IP is der/die/das foundational protocol suite von der/die/das internet. IP (Internet Protocol) handles addressing und routing packets between networks, while TCP (Transmission Control Protocol) provides reliable, ordered delivery mit retransmission und flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (für example in streaming, gaming, or DNS queries). HTTP is a stateless application-layer protocol für request/response Kommunikation between clients und servers. HTTPS is HTTP over TLS, adding encryption und integrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, standard HTTP verbs (GET, POST, PUT, PATCH, DELETE), und stateless interactions. WebSockets provide persistent, full-duplex connections so client und server can push messages in real time, which is useful für chat, live dashboards, und collaborative apps.

## Artificial Intelligence

Artificial intelligence (AI) is der/die/das simulation von human intelligence by machines, particularly computer Systeme. Maschinelles Lernen is a subset von AI in which Systeme learn from Daten to make predictions or decisions without being explicitly programmed. Tiefes Lernen is a subset von Maschinelles Lernen that uses Neuronale Netze mit many layers. Neuronale Netze are computational models loosely inspired by der/die/das structure von biological brains. Large Sprache models (LLMs) are AI models trained on massive amounts von text to generate und understand natural Sprache.

## Algorithms und Daten Structures

An algorithm is a step-by-step procedure für solving a problem. Daten structures are ways von organizing Daten in a computer so that it can be accessed und modified efficiently. Common Daten structures include arrays, linked lists, stacks, queues, trees, graphs, und hash tables. Sorting algorithms arrange items in a specified order; common Beispiele are bubble sort, merge sort, und quicksort. Binary search is an efficient algorithm für finding an item in a sorted list by repeatedly halving der/die/das search range.

## Databases

A Datenbank is an organized collection von structured Daten stored electronically. A relational Datenbank stores Daten in tables mit rows und columns. SQL (Structured Query Sprache) is der/die/das standard Sprache für managing und querying relational databases. NoSQL databases store Daten in formats other than tabular relations, such as documents, key-value pairs, or graphs. Common Datenbank Systeme include PostgreSQL, MySQL, SQLite, MongoDB, und Redis. An index in a Datenbank speeds up Daten retrieval at der/die/das cost von extra storage.

## System Design Grundlagen

System design focuses on building reliable, scalable, und maintainable software Systeme. Load balancing distributes traffic across multiple servers to improve availability und reduce latency. Horizontal scaling adds more machines; vertical scaling adds more resources to one machine. Caching stores frequently accessed Daten in fast storage (für example Redis, Memcached, or CDN edge caches) to reduce Datenbank load und response time. Databases at scale require replication, partitioning (sharding), backup strategies, und careful consistency tradeoffs. Microservices split large applications into smaller independently deployable services, while monoliths keep most logic in one deployable unit; both approaches involve tradeoffs in complexity, Bereitstellung speed, debugging, und team autonomy.

## Operating Systeme

An operating system (OS) is software that manages computer hardware und provides services für programs. Common operating Systeme include Windows, macOS, und Linux. Linux is an open-source OS kernel used in servers, embedded Systeme, und Android. der/die/das OS manages processes (running programs), memory, file Systeme, und input/output devices. A process is a running instance von a program. A thread is der/die/das smallest unit von execution within a process.

## Version Control

Version control Systeme track changes to code over time, allowing developers to collaborate und revert to previous states. Git is der/die/das most widely used version control system. A repository (repo) is a collection von files und their Geschichte. A commit is a saved snapshot von changes. A branch is an independent line von Entwicklung. A pull request is a proposal to merge changes from one branch into another.

## Software Entwicklung Practices

Object-oriented programming (OOP) organizes code into objects that combine Daten und behavior. Key principles von OOP include encapsulation, inheritance, polymorphism, und abstraction. Test-driven Entwicklung (TDD) is a practice von writing tests before writing code. Agile is a set von software Entwicklung methodologies that emphasize iterative Entwicklung, collaboration, und adaptability. DevOps combines software Entwicklung und IT operations to shorten der/die/das Entwicklung lifecycle. APIs (Application Programming Interfaces) allow different software Systeme to communicate mit each other.

## Cloud und DevOps Grundlagen

Cloud Datenverarbeitung provides on-demand infrastructure und managed services über das Internet. der/die/das three major public cloud providers are AWS (Amazon Web Services), Microsoft Azure, und Google Cloud Platform (GCP). Common service models are IaaS (infrastructure), PaaS (platform), und SaaS (software). Core cloud building blocks include compute instances/containers, object storage, managed databases, networking, und IAM (Identity und Access Verwaltung). CI/CD (Continuous Integration und Continuous Delivery/Bereitstellung) automates build, test, und release pipelines so code can move safely from commit to production. Docker packages applications und dependencies into portable containers; in production these containers are typically deployed via orchestrators (such as Kubernetes), serverless platforms, or managed container services.

## Daten Formats und Tooling

JSON (JavaScript Object Notation) is a lightweight text format built from objects (key/value pairs), arrays, strings, numbers, booleans, und null; it is widely used in APIs. YAML is a human-friendly configuration format that supports nested structures und comments, commonly used in CI/CD und infrastructure definitions. CSV (Comma-Separated Values) stores tabular Daten as rows von delimited text und is common für Daten import/export pipelines. XML (eXtensible Markup Sprache) is a tag-based structured format used in legacy Systeme, configuration, und document workflows. Developers commonly validate und transform these formats mit linters, schema validators (such as JSON Schema), query tools (`jq`, XPath), und parsing libraries in their programming Sprache.

## Regular Expressions (Regex)

A regular expression is a pattern Sprache used to search, match, extract, und transform text. Core regex concepts include literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), und escaping special characters. Regex is heavily used für input validation, log parsing, text extraction, und find/replace automation. Different engines (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested und documented to avoid bugs.

## Cybersecurity

Cybersecurity is der/die/das practice von protecting computer Systeme, networks, und Daten from digital attacks. Common threats include malware (malicious software), phishing (fraudulent Kommunikation designed to steal information), ransomware (malware that encrypts Daten und demands payment), und denial-von-service attacks. Encryption transforms Daten into an unreadable form that can only be decoded mit a key. HTTPS uses TLS (Transport Layer Sicherheit) to encrypt Web traffic. Strong, unique passwords und two-factor authentication are fundamental Sicherheit practices.

## Sicherheit Concepts für Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application without sharing credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 für authentication. JWT (JSON Web Token) is a compact token format containing claims, often used für stateless auth, but it must be signed correctly und validated strictly (signature, expiration, issuer, audience). TLS secures Daten in transit by providing encryption, integrity, und server authentication through certificates. der/die/das OWASP Top 10 is a widely used list von common Web application Sicherheit risks, including broken access control, cryptographic failures, injection, insecure design, Sicherheit misconfiguration, vulnerable components, und insufficient logging/monitoring. Secure Entwicklung requires defense-in-depth: input validation, output encoding, least privilege, secret Verwaltung, dependency patching, und regular Sicherheit Testen.
