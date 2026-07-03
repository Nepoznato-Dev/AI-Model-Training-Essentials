<!-- 
This file was automatically translated from English to Turkish.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Teknoloji ve Bilişim

## What is a Computer?

A computer is an electronic device that processes Veri according to a set içinde instructions called a program. Modern computers are based on bu von Neumann Mimari, which consists içinde a central processing unit (CPU), memory, storage, ve input/output devices. bu CPU executes instructions. RAM (random access memory) stores Veri temporarily while bu computer is running. Storage devices such as SSDs ve hard drives store Veri permanently.

## Programming Languages

A programming Dil is a formal Dil used to write instructions için computers. Python is a high-level, interpreted, general-purpose programming Dil known için its simple Sözdizimi ve readability. It is widely used içinde Veri Bilim, Makine Öğrenimi, Web Geliştirme, ve automation. JavaScript is bu primary Dil için Web Geliştirme ve runs içinde browsers. Java is a compiled, object-oriented Dil used widely içinde enterprise software ve Android Geliştirme. C ve C++ are lower-level languages that give fine-grained control over hardware ve are used içinde system programming, game Geliştirme, ve Performans-critical applications. Rust is a modern Sistemler programming Dil focused on safety ve Performans.

## How bu Internet Works

bu internet is a global Ağ içinde interconnected computers that communicate using standardized protocols. bu World Wide Web is a system içinde websites ve Web pages accessed through bu internet via browsers. HTTP (HyperText Transfer Protocol) ve HTTPS (secure HTTP) are bu protocols used to transfer Web pages. An IP address is a unique numerical address assigned to each device on a Ağ. DNS (Domain Name System) translates human-readable domain names (like google.com) into IP addresses. A router directs Ağ traffic between devices ve networks.

## Networking ve Protocols

TCP/IP is bu foundational protocol suite içinde bu internet. IP (Internet Protocol) handles addressing ve routing packets between networks, while TCP (Transmission Control Protocol) provides reliable, ordered delivery ile retransmission ve flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (için example içinde streaming, gaming, or DNS queries). HTTP is a stateless application-layer protocol için request/response İletişim between clients ve servers. HTTPS is HTTP over TLS, adding encryption ve integrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, standard HTTP verbs (GET, POST, PUT, PATCH, DELETE), ve stateless interactions. WebSockets provide persistent, full-duplex connections so client ve server can push messages içinde real time, which is useful için chat, live dashboards, ve collaborative apps.

## Artificial Intelligence

Artificial intelligence (AI) is bu simulation içinde human intelligence by machines, particularly computer Sistemler. Makine Öğrenimi is a subset içinde AI içinde which Sistemler learn from Veri to make predictions or decisions without being explicitly programmed. Derin Öğrenme is a subset içinde Makine Öğrenimi that uses Sinir Ağları ile many layers. Sinir Ağları are computational models loosely inspired by bu structure içinde biological brains. Large Dil models (LLMs) are AI models trained on massive amounts içinde text to generate ve understand natural Dil.

## Algorithms ve Veri Structures

An algorithm is a step-by-step procedure için solving a problem. Veri structures are ways içinde organizing Veri içinde a computer so that it can be accessed ve modified efficiently. Common Veri structures include arrays, linked lists, stacks, queues, trees, graphs, ve hash tables. Sorting algorithms arrange items içinde a specified order; common Örnekler are bubble sort, merge sort, ve quicksort. Binary search is an efficient algorithm için finding an item içinde a sorted list by repeatedly halving bu search range.

## Databases

A Veritabanı is an organized collection içinde structured Veri stored electronically. A relational Veritabanı stores Veri içinde tables ile rows ve columns. SQL (Structured Query Dil) is bu standard Dil için managing ve querying relational databases. NoSQL databases store Veri içinde formats other than tabular relations, such as documents, key-value pairs, or graphs. Common Veritabanı Sistemler include PostgreSQL, MySQL, SQLite, MongoDB, ve Redis. An index içinde a Veritabanı speeds up Veri retrieval at bu cost içinde extra storage.

## System Design Temeller

System design focuses on building reliable, scalable, ve maintainable software Sistemler. Load balancing distributes traffic across multiple servers to improve availability ve reduce latency. Horizontal scaling adds more machines; vertical scaling adds more resources to one machine. Caching stores frequently accessed Veri içinde fast storage (için example Redis, Memcached, or CDN edge caches) to reduce Veritabanı load ve response time. Databases at scale require replication, partitioning (sharding), backup strategies, ve careful consistency tradeoffs. Microservices split large applications into smaller independently deployable services, while monoliths keep most logic içinde one deployable unit; both approaches involve tradeoffs içinde complexity, Dağıtım speed, debugging, ve team autonomy.

## Operating Sistemler

An operating system (OS) is software that manages computer hardware ve provides services için programs. Common operating Sistemler include Windows, macOS, ve Linux. Linux is an open-source OS kernel used içinde servers, embedded Sistemler, ve Android. bu OS manages processes (running programs), memory, file Sistemler, ve input/output devices. A process is a running instance içinde a program. A thread is bu smallest unit içinde execution within a process.

## Version Control

Version control Sistemler track changes to code over time, allowing developers to collaborate ve revert to previous states. Git is bu most widely used version control system. A repository (repo) is a collection içinde files ve their Tarih. A commit is a saved snapshot içinde changes. A branch is an independent line içinde Geliştirme. A pull request is a proposal to merge changes from one branch into another.

## Software Geliştirme Practices

Object-oriented programming (OOP) organizes code into objects that combine Veri ve behavior. Key principles içinde OOP include encapsulation, inheritance, polymorphism, ve abstraction. Test-driven Geliştirme (TDD) is a practice içinde writing tests before writing code. Agile is a set içinde software Geliştirme methodologies that emphasize iterative Geliştirme, collaboration, ve adaptability. DevOps combines software Geliştirme ve IT operations to shorten bu Geliştirme lifecycle. APIs (Application Programming Interfaces) allow different software Sistemler to communicate ile each other.

## Cloud ve DevOps Temeller

Cloud Bilişim provides on-demand infrastructure ve managed services over bu internet. bu three major public cloud providers are AWS (Amazon Web Services), Microsoft Azure, ve Google Cloud Platform (GCP). Common service models are IaaS (infrastructure), PaaS (platform), ve SaaS (software). Core cloud building blocks include compute instances/containers, object storage, managed databases, networking, ve IAM (Identity ve Access Yönetim). CI/CD (Continuous Integration ve Continuous Delivery/Dağıtım) automates build, test, ve release pipelines so code can move safely from commit to production. Docker packages applications ve dependencies into portable containers; içinde production these containers are typically deployed via orchestrators (such as Kubernetes), serverless platforms, or managed container services.

## Veri Formats ve Tooling

JSON (JavaScript Object Notation) is a lightweight text format built from objects (key/value pairs), arrays, strings, numbers, booleans, ve null; it is widely used içinde APIs. YAML is a human-friendly configuration format that supports nested structures ve comments, commonly used içinde CI/CD ve infrastructure definitions. CSV (Comma-Separated Values) stores tabular Veri as rows içinde delimited text ve is common için Veri import/export pipelines. XML (eXtensible Markup Dil) is a tag-based structured format used içinde legacy Sistemler, configuration, ve document workflows. Developers commonly validate ve transform these formats ile linters, schema validators (such as JSON Schema), query tools (`jq`, XPath), ve parsing libraries içinde their programming Dil.

## Regular Expressions (Regex)

A regular expression is a pattern Dil used to search, match, extract, ve transform text. Core regex concepts include literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), ve escaping special characters. Regex is heavily used için input validation, log parsing, text extraction, ve find/replace automation. Different engines (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested ve documented to avoid bugs.

## Cybersecurity

Cybersecurity is bu practice içinde protecting computer Sistemler, networks, ve Veri from digital attacks. Common threats include malware (malicious software), phishing (fraudulent İletişim designed to steal information), ransomware (malware that encrypts Veri ve demands payment), ve denial-içinde-service attacks. Encryption transforms Veri into an unreadable form that can only be decoded ile a key. HTTPS uses TLS (Transport Layer Güvenlik) to encrypt Web traffic. Strong, unique passwords ve two-factor authentication are fundamental Güvenlik practices.

## Güvenlik Concepts için Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application without sharing credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 için authentication. JWT (JSON Web Token) is a compact token format containing claims, often used için stateless auth, but it must be signed correctly ve validated strictly (signature, expiration, issuer, audience). TLS secures Veri içinde transit by providing encryption, integrity, ve server authentication through certificates. bu OWASP Top 10 is a widely used list içinde common Web application Güvenlik risks, including broken access control, cryptographic failures, injection, insecure design, Güvenlik misconfiguration, vulnerable components, ve insufficient logging/monitoring. Secure Geliştirme requires defense-içinde-depth: input validation, output encoding, least privilege, secret Yönetim, dependency patching, ve regular Güvenlik Test Etme.
