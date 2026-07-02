<!-- 
This file was automatically translated from English to Mandarin (Traditional Chinese).
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 技術 和 計算

## What is a Computer?

A computer is an electronic device that processes 資料 according to a set 的 instructions called a program. Modern computers are based on 這 von Neumann 架構, which consists 的 a central processing unit (CPU), memory, storage, 和 input/output devices. 這 CPU executes instructions. RAM (random access memory) stores 資料 temporarily while 這 computer is running. Storage devices such as SSDs 和 hard drives store 資料 permanently.

## Programming Languages

A programming 語言 is a formal 語言 used to write instructions 為 computers. Python is a high-level, interpreted, general-purpose programming 語言 known 為 its simple 語法 和 readability. It is widely used 在 資料 科學, 機器學習, 網路 開發, 和 automation. JavaScript is 這 primary 語言 為 網路 開發 和 runs 在 browsers. Java is a compiled, object-oriented 語言 used widely 在 enterprise software 和 Android 開發. C 和 C++ are lower-level languages that give fine-grained control over hardware 和 are used 在 system programming, game 開發, 和 效能-critical applications. Rust is a modern 系統 programming 語言 focused on safety 和 效能.

## How 這 Internet Works

這 internet is a global 網路 的 interconnected computers that communicate using standardized protocols. 這 World Wide 網路 is a system 的 websites 和 網路 pages accessed through 這 internet via browsers. HTTP (HyperText Transfer Protocol) 和 HTTPS (secure HTTP) are 這 protocols used to transfer 網路 pages. An IP address is a unique numerical address assigned to each device on a 網路. DNS (Domain Name System) translates human-readable domain names (like google.com) into IP addresses. A router directs 網路 traffic between devices 和 networks.

## Networking 和 Protocols

TCP/IP is 這 foundational protocol suite 的 這 internet. IP (Internet Protocol) handles addressing 和 routing packets between networks, while TCP (Transmission Control Protocol) provides reliable, ordered delivery 與 retransmission 和 flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (為 example 在 streaming, gaming, or DNS queries). HTTP is a stateless application-layer protocol 為 request/response 溝通 between clients 和 servers. HTTPS is HTTP over TLS, adding encryption 和 integrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, standard HTTP verbs (GET, POST, PUT, PATCH, DELETE), 和 stateless interactions. WebSockets provide persistent, full-duplex connections so client 和 server can push messages 在 real time, which is useful 為 chat, live dashboards, 和 collaborative apps.

## Artificial Intelligence

Artificial intelligence (AI) is 這 simulation 的 human intelligence by machines, particularly computer 系統. 機器學習 is a subset 的 AI 在 which 系統 learn from 資料 to make predictions or decisions without being explicitly programmed. 深度學習 is a subset 的 機器學習 that uses 神經網絡 與 many layers. 神經網絡 are computational models loosely inspired by 這 structure 的 biological brains. Large 語言 models (LLMs) are AI models trained on massive amounts 的 text to generate 和 understand natural 語言.

## Algorithms 和 資料 Structures

An algorithm is a step-by-step procedure 為 solving a problem. 資料 structures are ways 的 organizing 資料 在 a computer so that it can be accessed 和 modified efficiently. Common 資料 structures include arrays, linked lists, stacks, queues, trees, graphs, 和 hash tables. Sorting algorithms arrange items 在 a specified order; common 範例 are bubble sort, merge sort, 和 quicksort. Binary search is an efficient algorithm 為 finding an item 在 a sorted list by repeatedly halving 這 search range.

## Databases

A 資料庫 is an organized collection 的 structured 資料 stored electronically. A relational 資料庫 stores 資料 在 tables 與 rows 和 columns. SQL (Structured Query 語言) is 這 standard 語言 為 managing 和 querying relational databases. NoSQL databases store 資料 在 formats other than tabular relations, such as documents, key-value pairs, or graphs. Common 資料庫 系統 include PostgreSQL, MySQL, SQLite, MongoDB, 和 Redis. An index 在 a 資料庫 speeds up 資料 retrieval at 這 cost 的 extra storage.

## System Design 基礎

System design focuses on building reliable, scalable, 和 maintainable software 系統. Load balancing distributes traffic across multiple servers to improve availability 和 reduce latency. Horizontal scaling adds more machines; vertical scaling adds more resources to one machine. Caching stores frequently accessed 資料 在 fast storage (為 example Redis, Memcached, or CDN edge caches) to reduce 資料庫 load 和 response time. Databases at scale require replication, partitioning (sharding), backup strategies, 和 careful consistency tradeoffs. Microservices split large applications into smaller independently deployable services, while monoliths keep most logic 在 one deployable unit; both approaches involve tradeoffs 在 complexity, 部署 speed, debugging, 和 team autonomy.

## Operating 系統

An operating system (OS) is software that manages computer hardware 和 provides services 為 programs. Common operating 系統 include Windows, macOS, 和 Linux. Linux is an open-source OS kernel used 在 servers, embedded 系統, 和 Android. 這 OS manages processes (running programs), memory, file 系統, 和 input/output devices. A process is a running instance 的 a program. A thread is 這 smallest unit 的 execution within a process.

## Version Control

Version control 系統 track changes to code over time, allowing developers to collaborate 和 revert to previous states. Git is 這 most widely used version control system. A repository (repo) is a collection 的 files 和 their 歷史. A commit is a saved snapshot 的 changes. A branch is an independent line 的 開發. A pull request is a proposal to merge changes from one branch into another.

## Software 開發 Practices

Object-oriented programming (OOP) organizes code into objects that combine 資料 和 behavior. Key principles 的 OOP include encapsulation, inheritance, polymorphism, 和 abstraction. Test-driven 開發 (TDD) is a practice 的 writing tests before writing code. Agile is a set 的 software 開發 methodologies that emphasize iterative 開發, collaboration, 和 adaptability. DevOps combines software 開發 和 IT operations to shorten 這 開發 lifecycle. APIs (Application Programming Interfaces) allow different software 系統 to communicate 與 each other.

## Cloud 和 DevOps 基礎

Cloud 計算 provides on-demand infrastructure 和 managed services over 這 internet. 這 three major public cloud providers are AWS (Amazon 網路 Services), Microsoft Azure, 和 Google Cloud Platform (GCP). Common service models are IaaS (infrastructure), PaaS (platform), 和 SaaS (software). Core cloud building blocks include compute instances/containers, object storage, managed databases, networking, 和 IAM (Identity 和 Access 管理). CI/CD (Continuous Integration 和 Continuous Delivery/部署) automates build, test, 和 release pipelines so code can move safely from commit to production. Docker packages applications 和 dependencies into portable containers; 在 production these containers are typically deployed via orchestrators (such as Kubernetes), serverless platforms, or managed container services.

## 資料 Formats 和 Tooling

JSON (JavaScript Object Notation) is a lightweight text format built from objects (key/value pairs), arrays, strings, numbers, booleans, 和 null; it is widely used 在 APIs. YAML is a human-friendly configuration format that supports nested structures 和 comments, commonly used 在 CI/CD 和 infrastructure definitions. CSV (Comma-Separated Values) stores tabular 資料 as rows 的 delimited text 和 is common 為 資料 import/export pipelines. XML (eXtensible Markup 語言) is a tag-based structured format used 在 legacy 系統, configuration, 和 document workflows. Developers commonly validate 和 transform these formats 與 linters, schema validators (such as JSON Schema), query tools (`jq`, XPath), 和 parsing libraries 在 their programming 語言.

## Regular Expressions (Regex)

A regular expression is a pattern 語言 used to search, match, extract, 和 transform text. Core regex concepts include literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), 和 escaping special characters. Regex is heavily used 為 input validation, log parsing, text extraction, 和 find/replace automation. Different engines (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested 和 documented to avoid bugs.

## Cybersecurity

Cybersecurity is 這 practice 的 protecting computer 系統, networks, 和 資料 from digital attacks. Common threats include malware (malicious software), phishing (fraudulent 溝通 designed to steal information), ransomware (malware that encrypts 資料 和 demands payment), 和 denial-的-service attacks. Encryption transforms 資料 into an unreadable form that can only be decoded 與 a key. HTTPS uses TLS (Transport Layer 安全) to encrypt 網路 traffic. Strong, unique passwords 和 two-factor authentication are fundamental 安全 practices.

## 安全 Concepts 為 Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application without sharing credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 為 authentication. JWT (JSON 網路 Token) is a compact token format containing claims, often used 為 stateless auth, but it must be signed correctly 和 validated strictly (signature, expiration, issuer, audience). TLS secures 資料 在 transit by providing encryption, integrity, 和 server authentication through certificates. 這 OWASP Top 10 is a widely used list 的 common 網路 application 安全 risks, including broken access control, cryptographic failures, injection, insecure design, 安全 misconfiguration, vulnerable components, 和 insufficient logging/monitoring. Secure 開發 requires defense-在-depth: input validation, output encoding, least privilege, secret 管理, dependency patching, 和 regular 安全 測試.
