<!-- 
This file was automatically translated from English to Portuguese.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Tecnologia e Computação

## What is a Computer?

A computer is an electronic device that processes Dados according to a set de instructions called a program. Modern computers are based on o/a von Neumann Arquitetura, which consists de a central processing unit (CPU), memory, storage, e input/output devices. o/a CPU executes instructions. RAM (random access memory) stores Dados temporarily while o/a computer is running. Storage devices such as SSDs e hard drives store Dados permanently.

## Programming Languages

A programming Idioma is a formal Idioma used to write instructions para computers. Python is a high-level, interpreted, general-purpose programming Idioma known para its simple Sintaxe e readability. It is widely used em Dados Ciência, Aprendizado de máquina, Web Desenvolvimento, e automation. JavaScript is o/a primary Idioma para Web Desenvolvimento e runs em browsers. Java is a compiled, object-oriented Idioma used widely em enterprise software e Android Desenvolvimento. C e C++ are lower-level languages that give fine-grained control over hardware e are used em system programming, game Desenvolvimento, e Desempenho-critical applications. Rust is a modern Sistemas programming Idioma focused on safety e Desempenho.

## How o/a Internet Works

o/a internet is a global Rede de interconnected computers that communicate using standardized protocols. o/a World Wide Web is a system de websites e Web pages accessed through o/a internet via browsers. HTTP (HyperText Transfer Protocol) e HTTPS (secure HTTP) are o/a protocols used to transfer Web pages. An IP address is a unique numerical address assigned to each device on a Rede. DNS (Domain Name System) translates human-readable domain names (like google.com) into IP addresses. A router directs Rede traffic between devices e networks.

## Networking e Protocols

TCP/IP is o/a foundational protocol suite de o/a internet. IP (Internet Protocol) handles addressing e routing packets between networks, while TCP (Transmission Control Protocol) provides reliable, ordered delivery com retransmission e flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (para example em streaming, gaming, or DNS queries). HTTP is a stateless application-layer protocol para request/response Comunicação between clients e servers. HTTPS is HTTP over TLS, adding encryption e integrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, standard HTTP verbs (GET, POST, PUT, PATCH, DELETE), e stateless interactions. WebSockets provide persistent, full-duplex connections so client e server can push messages em real time, which is useful para chat, live dashboards, e collaborative apps.

## Artificial Intelligence

Artificial intelligence (AI) is o/a simulation de human intelligence by machines, particularly computer Sistemas. Aprendizado de máquina is a subset de AI em which Sistemas learn from Dados to make predictions or decisions without being explicitly programmed. Aprendizado profundo is a subset de Aprendizado de máquina that uses Redes neurais com many layers. Redes neurais are computational models loosely inspired by o/a structure de biological brains. Large Idioma models (LLMs) are AI models trained on massive amounts de text to generate e understand natural Idioma.

## Algorithms e Dados Structures

An algorithm is a step-by-step procedure para solving a problem. Dados structures are ways de organizing Dados em a computer so that it can be accessed e modified efficiently. Common Dados structures include arrays, linked lists, stacks, queues, trees, graphs, e hash tables. Sorting algorithms arrange items em a specified order; common Exemplos are bubble sort, merge sort, e quicksort. Binary search is an efficient algorithm para finding an item em a sorted list by repeatedly halving o/a search range.

## Databases

A Banco de dados is an organized collection de structured Dados stored electronically. A relational Banco de dados stores Dados em tables com rows e columns. SQL (Structured Query Idioma) is o/a standard Idioma para managing e querying relational databases. NoSQL databases store Dados em formats other than tabular relations, such as documents, key-value pairs, or graphs. Common Banco de dados Sistemas include PostgreSQL, MySQL, SQLite, MongoDB, e Redis. An index em a Banco de dados speeds up Dados retrieval at o/a cost de extra storage.

## System Design Fundamentos

System design focuses on building reliable, scalable, e maintainable software Sistemas. Load balancing distributes traffic across multiple servers to improve availability e reduce latency. Horizontal scaling adds more machines; vertical scaling adds more resources to one machine. Caching stores frequently accessed Dados em fast storage (para example Redis, Memcached, or CDN edge caches) to reduce Banco de dados load e response time. Databases at scale require replication, partitioning (sharding), backup strategies, e careful consistency tradeoffs. Microservices split large applications into smaller independently deployable services, while monoliths keep most logic em one deployable unit; both approaches involve tradeoffs em complexity, Implantação speed, debugging, e team autonomy.

## Operating Sistemas

An operating system (OS) is software that manages computer hardware e provides services para programs. Common operating Sistemas include Windows, macOS, e Linux. Linux is an open-source OS kernel used em servers, embedded Sistemas, e Android. o/a OS manages processes (running programs), memory, file Sistemas, e input/output devices. A process is a running instance de a program. A thread is o/a smallest unit de execution within a process.

## Version Control

Version control Sistemas track changes to code over time, allowing developers to collaborate e revert to previous states. Git is o/a most widely used version control system. A repository (repo) is a collection de files e their História. A commit is a saved snapshot de changes. A branch is an independent line de Desenvolvimento. A pull request is a proposal to merge changes from one branch into another.

## Software Desenvolvimento Practices

Object-oriented programming (OOP) organizes code into objects that combine Dados e behavior. Key principles de OOP include encapsulation, inheritance, polymorphism, e abstraction. Test-driven Desenvolvimento (TDD) is a practice de writing tests before writing code. Agile is a set de software Desenvolvimento methodologies that emphasize iterative Desenvolvimento, collaboration, e adaptability. DevOps combines software Desenvolvimento e IT operations to shorten o/a Desenvolvimento lifecycle. APIs (Application Programming Interfaces) allow different software Sistemas to communicate com each other.

## Cloud e DevOps Básico

Cloud Computação provides on-demand infrastructure e managed services over o/a internet. o/a three major public cloud providers are AWS (Amazon Web Services), Microsoft Azure, e Google Cloud Platform (GCP). Common service models are IaaS (infrastructure), PaaS (platform), e SaaS (software). Core cloud building blocks include compute instances/containers, object storage, managed databases, networking, e IAM (Identity e Access Gerenciamento). CI/CD (Continuous Integration e Continuous Delivery/Implantação) automates build, test, e release pipelines so code can move safely from commit to production. Docker packages applications e dependencies into portable containers; em production these containers are typically deployed via orchestrators (such as Kubernetes), serverless platforms, or managed container services.

## Dados Formats e Tooling

JSON (JavaScript Object Notation) is a lightweight text format built from objects (key/value pairs), arrays, strings, numbers, booleans, e null; it is widely used em APIs. YAML is a human-friendly configuration format that supports nested structures e comments, commonly used em CI/CD e infrastructure definitions. CSV (Comma-Separated Values) stores tabular Dados as rows de delimited text e is common para Dados import/export pipelines. XML (eXtensible Markup Idioma) is a tag-based structured format used em legacy Sistemas, configuration, e document workflows. Developers commonly validate e transform these formats com linters, schema validators (such as JSON Schema), query tools (`jq`, XPath), e parsing libraries em their programming Idioma.

## Regular Expressions (Regex)

A regular expression is a pattern Idioma used to search, match, extract, e transform text. Core regex concepts include literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), e escaping special characters. Regex is heavily used para input validation, log parsing, text extraction, e find/replace automation. Different engines (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested e documented to avoid bugs.

## Cybersecurity

Cybersecurity is o/a practice de protecting computer Sistemas, networks, e Dados from digital attacks. Common threats include malware (malicious software), phishing (fraudulent Comunicação designed to steal information), ransomware (malware that encrypts Dados e demands payment), e denial-de-service attacks. Encryption transforms Dados into an unreadable form that can only be decoded com a key. HTTPS uses TLS (Transport Layer Segurança) to encrypt Web traffic. Strong, unique passwords e two-factor authentication are fundamental Segurança practices.

## Segurança Concepts para Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application without sharing credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 para authentication. JWT (JSON Web Token) is a compact token format containing claims, often used para stateless auth, but it must be signed correctly e validated strictly (signature, expiration, issuer, audience). TLS secures Dados em transit by providing encryption, integrity, e server authentication through certificates. o/a OWASP Top 10 is a widely used list de common Web application Segurança risks, including broken access control, cryptographic failures, injection, insecure design, Segurança misconfiguration, vulnerable components, e insufficient logging/monitoring. Secure Desenvolvimento requires defense-em-depth: input validation, output encoding, least privilege, secret Gerenciamento, dependency patching, e regular Segurança Teste.
