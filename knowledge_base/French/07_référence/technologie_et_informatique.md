<!-- 
This file was automatically translated from English to French.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Technologie et Informatique

## What is a Computer?

A computer is an electronic device that processes Données according to a set de instructions called a program. Modern computers are based on le/la von Neumann Architecture, which consists de a central processing unit (CPU), memory, storage, et input/output devices. le/la CPU executes instructions. RAM (random access memory) stores Données temporarily while le/la computer is running. Storage devices such as SSDs et hard drives store Données permanently.

## Programming Languages

A programming Langue is a formal Langue used to write instructions pour computers. Python is a high-level, interpreted, general-purpose programming Langue known pour its simple Syntaxe et readability. It is widely used dans Données Science, Apprentissage automatique, Web Développement, et automation. JavaScript is le/la primary Langue pour Web Développement et runs dans browsers. Java is a compiled, object-oriented Langue used widely dans enterprise software et Android Développement. C et C++ are lower-level languages that give fine-grained control over hardware et are used dans system programming, game Développement, et Performance-critical applications. Rust is a modern Systèmes programming Langue focused on safety et Performance.

## How le/la Internet Works

le/la internet is a global Réseau de interconnected computers that communicate using standardized protocols. le/la World Wide Web is a system de websites et Web pages accessed through le/la internet via browsers. HTTP (HyperText Transfer Protocol) et HTTPS (secure HTTP) are le/la protocols used to transfer Web pages. An IP address is a unique numerical address assigned to each device on a Réseau. DNS (Domain Name System) translates human-readable domain names (like google.com) into IP addresses. A router directs Réseau traffic between devices et networks.

## Networking et Protocols

TCP/IP is le/la foundational protocol suite de le/la internet. IP (Internet Protocol) handles addressing et routing packets between networks, while TCP (Transmission Control Protocol) provides reliable, ordered delivery avec retransmission et flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (pour example dans streaming, gaming, or DNS queries). HTTP is a stateless application-layer protocol pour request/response Communication between clients et servers. HTTPS is HTTP over TLS, adding encryption et integrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, standard HTTP verbs (GET, POST, PUT, PATCH, DELETE), et stateless interactions. WebSockets provide persistent, full-duplex connections so client et server can push messages dans real time, which is useful pour chat, live dashboards, et collaborative apps.

## Artificial Intelligence

Artificial intelligence (AI) is le/la simulation de human intelligence by machines, particularly computer Systèmes. Apprentissage automatique is a subset de AI dans which Systèmes learn from Données to make predictions or decisions without being explicitly programmed. Apprentissage profond is a subset de Apprentissage automatique that uses Réseaux de neurones avec many layers. Réseaux de neurones are computational models loosely inspired by le/la structure de biological brains. Large Langue models (LLMs) are AI models trained on massive amounts de text to generate et understand natural Langue.

## Algorithms et Données Structures

An algorithm is a step-by-step procedure pour solving a problem. Données structures are ways de organizing Données dans a computer so that it can be accessed et modified efficiently. Common Données structures include arrays, linked lists, stacks, queues, trees, graphs, et hash tables. Sorting algorithms arrange items dans a specified order; common Exemples are bubble sort, merge sort, et quicksort. Binary search is an efficient algorithm pour finding an item dans a sorted list by repeatedly halving le/la search range.

## Databases

A Base de données is an organized collection de structured Données stored electronically. A relational Base de données stores Données dans tables avec rows et columns. SQL (Structured Query Langue) is le/la standard Langue pour managing et querying relational databases. NoSQL databases store Données dans formats other than tabular relations, such as documents, key-value pairs, or graphs. Common Base de données Systèmes include PostgreSQL, MySQL, SQLite, MongoDB, et Redis. An index dans a Base de données speeds up Données retrieval at le/la cost de extra storage.

## System Design Fondamentaux

System design focuses on building reliable, scalable, et maintainable software Systèmes. Load balancing distributes traffic across multiple servers to improve availability et reduce latency. Horizontal scaling adds more machines; vertical scaling adds more resources to one machine. Caching stores frequently accessed Données dans fast storage (pour example Redis, Memcached, or CDN edge caches) to reduce Base de données load et response time. Databases at scale require replication, partitioning (sharding), backup strategies, et careful consistency tradeoffs. Microservices split large applications into smaller independently deployable services, while monoliths keep most logic dans one deployable unit; both approaches involve tradeoffs dans complexity, Déploiement speed, debugging, et team autonomy.

## Operating Systèmes

An operating system (OS) is software that manages computer hardware et provides services pour programs. Common operating Systèmes include Windows, macOS, et Linux. Linux is an open-source OS kernel used dans servers, embedded Systèmes, et Android. le/la OS manages processes (running programs), memory, file Systèmes, et input/output devices. A process is a running instance de a program. A thread is le/la smallest unit de execution within a process.

## Version Control

Version control Systèmes track changes to code over time, allowing developers to collaborate et revert to previous states. Git is le/la most widely used version control system. A repository (repo) is a collection de files et their Histoire. A commit is a saved snapshot de changes. A branch is an independent line de Développement. A pull request is a proposal to merge changes from one branch into another.

## Software Développement Practices

Object-oriented programming (OOP) organizes code into objects that combine Données et behavior. Key principles de OOP include encapsulation, inheritance, polymorphism, et abstraction. Test-driven Développement (TDD) is a practice de writing tests before writing code. Agile is a set de software Développement methodologies that emphasize iterative Développement, collaboration, et adaptability. DevOps combines software Développement et IT operations to shorten le/la Développement lifecycle. APIs (Application Programming Interfaces) allow different software Systèmes to communicate avec each other.

## Cloud et DevOps Bases

Cloud Informatique provides on-demand infrastructure et managed services over le/la internet. le/la three major public cloud providers are AWS (Amazon Web Services), Microsoft Azure, et Google Cloud Platform (GCP). Common service models are IaaS (infrastructure), PaaS (platform), et SaaS (software). Core cloud building blocks include compute instances/containers, object storage, managed databases, networking, et IAM (Identity et Access Gestion). CI/CD (Continuous Integration et Continuous Delivery/Déploiement) automates build, test, et release pipelines so code can move safely from commit to production. Docker packages applications et dependencies into portable containers; dans production these containers are typically deployed via orchestrators (such as Kubernetes), serverless platforms, or managed container services.

## Données Formats et Tooling

JSON (JavaScript Object Notation) is a lightweight text format built from objects (key/value pairs), arrays, strings, numbers, booleans, et null; it is widely used dans APIs. YAML is a human-friendly configuration format that supports nested structures et comments, commonly used dans CI/CD et infrastructure definitions. CSV (Comma-Separated Values) stores tabular Données as rows de delimited text et is common pour Données import/export pipelines. XML (eXtensible Markup Langue) is a tag-based structured format used dans legacy Systèmes, configuration, et document workflows. Developers commonly validate et transform these formats avec linters, schema validators (such as JSON Schema), query tools (`jq`, XPath), et parsing libraries dans their programming Langue.

## Regular Expressions (Regex)

A regular expression is a pattern Langue used to search, match, extract, et transform text. Core regex concepts include literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), et escaping special characters. Regex is heavily used pour input validation, log parsing, text extraction, et find/replace automation. Different engines (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested et documented to avoid bugs.

## Cybersecurity

Cybersecurity is le/la practice de protecting computer Systèmes, networks, et Données from digital attacks. Common threats include malware (malicious software), phishing (fraudulent Communication designed to steal information), ransomware (malware that encrypts Données et demands payment), et denial-de-service attacks. Encryption transforms Données into an unreadable form that can only be decoded avec a key. HTTPS uses TLS (Transport Layer Sécurité) to encrypt Web traffic. Strong, unique passwords et two-factor authentication are fundamental Sécurité practices.

## Sécurité Concepts pour Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application without sharing credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 pour authentication. JWT (JSON Web Token) is a compact token format containing claims, often used pour stateless auth, but it must be signed correctly et validated strictly (signature, expiration, issuer, audience). TLS secures Données dans transit by providing encryption, integrity, et server authentication through certificates. le/la OWASP Top 10 is a widely used list de common Web application Sécurité risks, including broken access control, cryptographic failures, injection, insecure design, Sécurité misconfiguration, vulnerable components, et insufficient logging/monitoring. Secure Développement requires defense-dans-depth: input validation, output encoding, least privilege, secret Gestion, dependency patching, et regular Sécurité Test.
