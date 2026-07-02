<!-- 
This file was automatically translated from English to Korean.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 기술 와 컴퓨팅

## What is a Computer?

A computer is an electronic device that processes 데이터 according to a set 의 instructions called a program. Modern computers are based on 그 von Neumann 아키텍처, which consists 의 a central processing unit (CPU), memory, storage, 와 input/output devices. 그 CPU executes instructions. RAM (random access memory) stores 데이터 temporarily while 그 computer is running. Storage devices such as SSDs 와 hard drives store 데이터 permanently.

## Programming Languages

A programming 언어 is a formal 언어 used to write instructions 위한 computers. Python is a high-level, interpreted, general-purpose programming 언어 known 위한 its simple 구문 와 readability. It is widely used 에서 데이터 과학, 기계 학습, 웹 개발, 와 automation. JavaScript is 그 primary 언어 위한 웹 개발 와 runs 에서 browsers. Java is a compiled, object-oriented 언어 used widely 에서 enterprise software 와 Android 개발. C 와 C++ are lower-level languages that give fine-grained control over hardware 와 are used 에서 system programming, game 개발, 와 성능-critical applications. Rust is a modern 시스템 programming 언어 focused on safety 와 성능.

## How 그 Internet Works

그 internet is a global 네트워크 의 interconnected computers that communicate using standardized protocols. 그 World Wide 웹 is a system 의 websites 와 웹 pages accessed through 그 internet via browsers. HTTP (HyperText Transfer Protocol) 와 HTTPS (secure HTTP) are 그 protocols used to transfer 웹 pages. An IP address is a unique numerical address assigned to each device on a 네트워크. DNS (Domain Name System) translates human-readable domain names (like google.com) into IP addresses. A router directs 네트워크 traffic between devices 와 networks.

## Networking 와 Protocols

TCP/IP is 그 foundational protocol suite 의 그 internet. IP (Internet Protocol) handles addressing 와 routing packets between networks, while TCP (Transmission Control Protocol) provides reliable, ordered delivery 와 함께 retransmission 와 flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (위한 example 에서 streaming, gaming, or DNS queries). HTTP is a stateless application-layer protocol 위한 request/response 의사소통 between clients 와 servers. HTTPS is HTTP over TLS, adding encryption 와 integrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, standard HTTP verbs (GET, POST, PUT, PATCH, DELETE), 와 stateless interactions. WebSockets provide persistent, full-duplex connections so client 와 server can push messages 에서 real time, which is useful 위한 chat, live dashboards, 와 collaborative apps.

## Artificial Intelligence

Artificial intelligence (AI) is 그 simulation 의 human intelligence by machines, particularly computer 시스템. 기계 학습 is a subset 의 AI 에서 which 시스템 learn from 데이터 to make predictions or decisions without being explicitly programmed. 딥 러닝 is a subset 의 기계 학습 that uses 신경망 와 함께 many layers. 신경망 are computational models loosely inspired by 그 structure 의 biological brains. Large 언어 models (LLMs) are AI models trained on massive amounts 의 text to generate 와 understand natural 언어.

## Algorithms 와 데이터 Structures

An algorithm is a step-by-step procedure 위한 solving a problem. 데이터 structures are ways 의 organizing 데이터 에서 a computer so that it can be accessed 와 modified efficiently. Common 데이터 structures include arrays, linked lists, stacks, queues, trees, graphs, 와 hash tables. Sorting algorithms arrange items 에서 a specified order; common 예시 are bubble sort, merge sort, 와 quicksort. Binary search is an efficient algorithm 위한 finding an item 에서 a sorted list by repeatedly halving 그 search range.

## Databases

A 데이터베이스 is an organized collection 의 structured 데이터 stored electronically. A relational 데이터베이스 stores 데이터 에서 tables 와 함께 rows 와 columns. SQL (Structured Query 언어) is 그 standard 언어 위한 managing 와 querying relational databases. NoSQL databases store 데이터 에서 formats other than tabular relations, such as documents, key-value pairs, or graphs. Common 데이터베이스 시스템 include PostgreSQL, MySQL, SQLite, MongoDB, 와 Redis. An index 에서 a 데이터베이스 speeds up 데이터 retrieval at 그 cost 의 extra storage.

## System Design 기초

System design focuses on building reliable, scalable, 와 maintainable software 시스템. Load balancing distributes traffic across multiple servers to improve availability 와 reduce latency. Horizontal scaling adds more machines; vertical scaling adds more resources to one machine. Caching stores frequently accessed 데이터 에서 fast storage (위한 example Redis, Memcached, or CDN edge caches) to reduce 데이터베이스 load 와 response time. Databases at scale require replication, partitioning (sharding), backup strategies, 와 careful consistency tradeoffs. Microservices split large applications into smaller independently deployable services, while monoliths keep most logic 에서 one deployable unit; both approaches involve tradeoffs 에서 complexity, 배포 speed, debugging, 와 team autonomy.

## Operating 시스템

An operating system (OS) is software that manages computer hardware 와 provides services 위한 programs. Common operating 시스템 include Windows, macOS, 와 Linux. Linux is an open-source OS kernel used 에서 servers, embedded 시스템, 와 Android. 그 OS manages processes (running programs), memory, file 시스템, 와 input/output devices. A process is a running instance 의 a program. A thread is 그 smallest unit 의 execution within a process.

## Version Control

Version control 시스템 track changes to code over time, allowing developers to collaborate 와 revert to previous states. Git is 그 most widely used version control system. A repository (repo) is a collection 의 files 와 their 역사. A commit is a saved snapshot 의 changes. A branch is an independent line 의 개발. A pull request is a proposal to merge changes from one branch into another.

## Software 개발 Practices

Object-oriented programming (OOP) organizes code into objects that combine 데이터 와 behavior. Key principles 의 OOP include encapsulation, inheritance, polymorphism, 와 abstraction. Test-driven 개발 (TDD) is a practice 의 writing tests before writing code. Agile is a set 의 software 개발 methodologies that emphasize iterative 개발, collaboration, 와 adaptability. DevOps combines software 개발 와 IT operations to shorten 그 개발 lifecycle. APIs (Application Programming Interfaces) allow different software 시스템 to communicate 와 함께 each other.

## Cloud 와 DevOps 기본

Cloud 컴퓨팅 provides on-demand infrastructure 와 managed services over 그 internet. 그 three major public cloud providers are AWS (Amazon 웹 Services), Microsoft Azure, 와 Google Cloud Platform (GCP). Common service models are IaaS (infrastructure), PaaS (platform), 와 SaaS (software). Core cloud building blocks include compute instances/containers, object storage, managed databases, networking, 와 IAM (Identity 와 Access 관리). CI/CD (Continuous Integration 와 Continuous Delivery/배포) automates build, test, 와 release pipelines so code can move safely from commit to production. Docker packages applications 와 dependencies into portable containers; 에서 production these containers are typically deployed via orchestrators (such as Kubernetes), serverless platforms, or managed container services.

## 데이터 Formats 와 Tooling

JSON (JavaScript Object Notation) is a lightweight text format built from objects (key/value pairs), arrays, strings, numbers, booleans, 와 null; it is widely used 에서 APIs. YAML is a human-friendly configuration format that supports nested structures 와 comments, commonly used 에서 CI/CD 와 infrastructure definitions. CSV (Comma-Separated Values) stores tabular 데이터 as rows 의 delimited text 와 is common 위한 데이터 import/export pipelines. XML (eXtensible Markup 언어) is a tag-based structured format used 에서 legacy 시스템, configuration, 와 document workflows. Developers commonly validate 와 transform these formats 와 함께 linters, schema validators (such as JSON Schema), query tools (`jq`, XPath), 와 parsing libraries 에서 their programming 언어.

## Regular Expressions (Regex)

A regular expression is a pattern 언어 used to search, match, extract, 와 transform text. Core regex concepts include literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), 와 escaping special characters. Regex is heavily used 위한 input validation, log parsing, text extraction, 와 find/replace automation. Different engines (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested 와 documented to avoid bugs.

## Cybersecurity

Cybersecurity is 그 practice 의 protecting computer 시스템, networks, 와 데이터 from digital attacks. Common threats include malware (malicious software), phishing (fraudulent 의사소통 designed to steal information), ransomware (malware that encrypts 데이터 와 demands payment), 와 denial-의-service attacks. Encryption transforms 데이터 into an unreadable form that can only be decoded 와 함께 a key. HTTPS uses TLS (Transport Layer 보안) to encrypt 웹 traffic. Strong, unique passwords 와 two-factor authentication are fundamental 보안 practices.

## 보안 Concepts 위한 Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application without sharing credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 위한 authentication. JWT (JSON 웹 Token) is a compact token format containing claims, often used 위한 stateless auth, but it must be signed correctly 와 validated strictly (signature, expiration, issuer, audience). TLS secures 데이터 에서 transit by providing encryption, integrity, 와 server authentication through certificates. 그 OWASP Top 10 is a widely used list 의 common 웹 application 보안 risks, including broken access control, cryptographic failures, injection, insecure design, 보안 misconfiguration, vulnerable components, 와 insufficient logging/monitoring. Secure 개발 requires defense-에서-depth: input validation, output encoding, least privilege, secret 관리, dependency patching, 와 regular 보안 테스트.
