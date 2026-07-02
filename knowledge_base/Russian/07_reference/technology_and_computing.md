<!-- 
This file was automatically translated from English to Russian.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Технология и Вычисления

## What is a Computer?

A computer is an electronic device that processes Данные according to a set из instructions called a program. Modern computers are based on the von Neumann Архитектура, which consists из a central processing unit (CPU), memory, storage, и input/output devices. the CPU executes instructions. RAM (random access memory) stores Данные temporarily while the computer is running. Storage devices such as SSDs и hard drives store Данные permanently.

## Programming Languages

A programming Язык is a formal Язык used to write instructions для computers. Python is a high-level, interpreted, general-purpose programming Язык known для its simple Синтаксис и readability. It is widely used в Данные Наука, Машинное обучение, Веб Разработка, и automation. JavaScript is the primary Язык для Веб Разработка и runs в browsers. Java is a compiled, object-oriented Язык used widely в enterprise software и Android Разработка. C и C++ are lower-level languages that give fine-grained control over hardware и are used в system programming, game Разработка, и Производительность-critical applications. Rust is a modern Системы programming Язык focused on safety и Производительность.

## How the Internet Works

the internet is a global Сеть из interconnected computers that communicate using standardized protocols. the World Wide Веб is a system из websites и Веб pages accessed through the internet via browsers. HTTP (HyperText Transfer Protocol) и HTTPS (secure HTTP) are the protocols used to transfer Веб pages. An IP address is a unique numerical address assigned to each device on a Сеть. DNS (Domain Name System) translates human-readable domain names (like google.com) into IP addresses. A router directs Сеть traffic between devices и networks.

## Networking и Protocols

TCP/IP is the foundational protocol suite из the internet. IP (Internet Protocol) handles addressing и routing packets between networks, while TCP (Transmission Control Protocol) provides reliable, ordered delivery с retransmission и flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (для example в streaming, gaming, or DNS queries). HTTP is a stateless application-layer protocol для request/response Коммуникация between clients и servers. HTTPS is HTTP over TLS, adding encryption и integrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, standard HTTP verbs (GET, POST, PUT, PATCH, DELETE), и stateless interactions. WebSockets provide persistent, full-duplex connections so client и server can push messages в real time, which is useful для chat, live dashboards, и collaborative apps.

## Artificial Intelligence

Artificial intelligence (AI) is the simulation из human intelligence by machines, particularly computer Системы. Машинное обучение is a subset из AI в which Системы learn from Данные to make predictions or decisions without being explicitly programmed. Глубокое обучение is a subset из Машинное обучение that uses Нейронные сети с many layers. Нейронные сети are computational models loosely inspired by the structure из biological brains. Large Язык models (LLMs) are AI models trained on massive amounts из text to generate и understand natural Язык.

## Algorithms и Данные Structures

An algorithm is a step-by-step procedure для solving a problem. Данные structures are ways из organizing Данные в a computer so that it can be accessed и modified efficiently. Common Данные structures include arrays, linked lists, stacks, queues, trees, graphs, и hash tables. Sorting algorithms arrange items в a specified order; common Примеры are bubble sort, merge sort, и quicksort. Binary search is an efficient algorithm для finding an item в a sorted list by repeatedly halving the search range.

## Databases

A База данных is an organized collection из structured Данные stored electronically. A relational База данных stores Данные в tables с rows и columns. SQL (Structured Query Язык) is the standard Язык для managing и querying relational databases. NoSQL databases store Данные в formats other than tabular relations, such as documents, key-value pairs, or graphs. Common База данных Системы include PostgreSQL, MySQL, SQLite, MongoDB, и Redis. An index в a База данных speeds up Данные retrieval at the cost из extra storage.

## System Design Основы

System design focuses on building reliable, scalable, и maintainable software Системы. Load balancing distributes traffic across multiple servers to improve availability и reduce latency. Horizontal scaling adds more machines; vertical scaling adds more resources to one machine. Caching stores frequently accessed Данные в fast storage (для example Redis, Memcached, or CDN edge caches) to reduce База данных load и response time. Databases at scale require replication, partitioning (sharding), backup strategies, и careful consistency tradeoffs. Microservices split large applications into smaller independently deployable services, while monoliths keep most logic в one deployable unit; both approaches involve tradeoffs в complexity, Развертывание speed, debugging, и team autonomy.

## Operating Системы

An operating system (OS) is software that manages computer hardware и provides services для programs. Common operating Системы include Windows, macOS, и Linux. Linux is an open-source OS kernel used в servers, embedded Системы, и Android. the OS manages processes (running programs), memory, file Системы, и input/output devices. A process is a running instance из a program. A thread is the smallest unit из execution within a process.

## Version Control

Version control Системы track changes to code over time, allowing developers to collaborate и revert to previous states. Git is the most widely used version control system. A repository (repo) is a collection из files и their История. A commit is a saved snapshot из changes. A branch is an independent line из Разработка. A pull request is a proposal to merge changes from one branch into another.

## Software Разработка Practices

Object-oriented programming (OOP) organizes code into objects that combine Данные и behavior. Key principles из OOP include encapsulation, inheritance, polymorphism, и abstraction. Test-driven Разработка (TDD) is a practice из writing tests before writing code. Agile is a set из software Разработка methodologies that emphasize iterative Разработка, collaboration, и adaptability. DevOps combines software Разработка и IT operations to shorten the Разработка lifecycle. APIs (Application Programming Interfaces) allow different software Системы to communicate с each other.

## Cloud и DevOps Основы

Cloud Вычисления provides on-demand infrastructure и managed services over the internet. the three major public cloud providers are AWS (Amazon Веб Services), Microsoft Azure, и Google Cloud Platform (GCP). Common service models are IaaS (infrastructure), PaaS (platform), и SaaS (software). Core cloud building blocks include compute instances/containers, object storage, managed databases, networking, и IAM (Identity и Access Управление). CI/CD (Continuous Integration и Continuous Delivery/Развертывание) automates build, test, и release pipelines so code can move safely from commit to production. Docker packages applications и dependencies into portable containers; в production these containers are typically deployed via orchestrators (such as Kubernetes), serverless platforms, or managed container services.

## Данные Formats и Tooling

JSON (JavaScript Object Notation) is a lightweight text format built from objects (key/value pairs), arrays, strings, numbers, booleans, и null; it is widely used в APIs. YAML is a human-friendly configuration format that supports nested structures и comments, commonly used в CI/CD и infrastructure definitions. CSV (Comma-Separated Values) stores tabular Данные as rows из delimited text и is common для Данные import/export pipelines. XML (eXtensible Markup Язык) is a tag-based structured format used в legacy Системы, configuration, и document workflows. Developers commonly validate и transform these formats с linters, schema validators (such as JSON Schema), query tools (`jq`, XPath), и parsing libraries в their programming Язык.

## Regular Expressions (Regex)

A regular expression is a pattern Язык used to search, match, extract, и transform text. Core regex concepts include literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), и escaping special characters. Regex is heavily used для input validation, log parsing, text extraction, и find/replace automation. Different engines (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested и documented to avoid bugs.

## Cybersecurity

Cybersecurity is the practice из protecting computer Системы, networks, и Данные from digital attacks. Common threats include malware (malicious software), phishing (fraudulent Коммуникация designed to steal information), ransomware (malware that encrypts Данные и demands payment), и denial-из-service attacks. Encryption transforms Данные into an unreadable form that can only be decoded с a key. HTTPS uses TLS (Transport Layer Безопасность) to encrypt Веб traffic. Strong, unique passwords и two-factor authentication are fundamental Безопасность practices.

## Безопасность Concepts для Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application without sharing credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 для authentication. JWT (JSON Веб Token) is a compact token format containing claims, often used для stateless auth, but it must be signed correctly и validated strictly (signature, expiration, issuer, audience). TLS secures Данные в transit by providing encryption, integrity, и server authentication through certificates. the OWASP Top 10 is a widely used list из common Веб application Безопасность risks, including broken access control, cryptographic failures, injection, insecure design, Безопасность misconfiguration, vulnerable components, и insufficient logging/monitoring. Secure Разработка requires defense-в-depth: input validation, output encoding, least privilege, secret Управление, dependency patching, и regular Безопасность Тестирование.
