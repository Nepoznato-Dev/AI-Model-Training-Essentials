<!-- 
This file was automatically translated from English to Mandarin (Simplified Chinese).
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 技术 和 计算

## What is a Computer?

A computer is an electronic device that processes 数据 according to a set 的 instructions called a program. Modern computers are based on 这 von Neumann 架构, which consists 的 a central processing unit (CPU), memory, storage, 和 input/output devices. 这 CPU executes instructions. RAM (random access memory) stores 数据 temporarily while 这 computer is running. Storage devices such as SSDs 和 hard drives store 数据 permanently.

## Programming Languages

A programming 语言 is a formal 语言 used to write instructions 为 computers. Python is a high-level, interpreted, general-purpose programming 语言 known 为 its simple 语法 和 readability. It is widely used 在 数据 科学, 机器学习, 网络 开发, 和 automation. JavaScript is 这 primary 语言 为 网络 开发 和 runs 在 browsers. Java is a compiled, object-oriented 语言 used widely 在 enterprise software 和 Android 开发. C 和 C++ are lower-level languages that give fine-grained control over hardware 和 are used 在 system programming, game 开发, 和 性能-critical applications. Rust is a modern 系统 programming 语言 focused on safety 和 性能.

## How 这 Internet Works

这 internet is a global 网络 的 interconnected computers that communicate using standardized protocols. 这 World Wide 网络 is a system 的 websites 和 网络 pages accessed through 这 internet via browsers. HTTP (HyperText Transfer Protocol) 和 HTTPS (secure HTTP) are 这 protocols used to transfer 网络 pages. An IP address is a unique numerical address assigned to each device on a 网络. DNS (Domain Name System) translates human-readable domain names (like google.com) into IP addresses. A router directs 网络 traffic between devices 和 networks.

## Networking 和 Protocols

TCP/IP is 这 foundational protocol suite 的 这 internet. IP (Internet Protocol) handles addressing 和 routing packets between networks, while TCP (Transmission Control Protocol) provides reliable, ordered delivery 与 retransmission 和 flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (为 example 在 streaming, gaming, or DNS queries). HTTP is a stateless application-layer protocol 为 request/response 沟通 between clients 和 servers. HTTPS is HTTP over TLS, adding encryption 和 integrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, standard HTTP verbs (GET, POST, PUT, PATCH, DELETE), 和 stateless interactions. WebSockets provide persistent, full-duplex connections so client 和 server can push messages 在 real time, which is useful 为 chat, live dashboards, 和 collaborative apps.

## Artificial Intelligence

Artificial intelligence (AI) is 这 simulation 的 human intelligence by machines, particularly computer 系统. 机器学习 is a subset 的 AI 在 which 系统 learn from 数据 to make predictions or decisions without being explicitly programmed. 深度学习 is a subset 的 机器学习 that uses 神经网络 与 many layers. 神经网络 are computational models loosely inspired by 这 structure 的 biological brains. Large 语言 models (LLMs) are AI models trained on massive amounts 的 text to generate 和 understand natural 语言.

## Algorithms 和 数据 Structures

An algorithm is a step-by-step procedure 为 solving a problem. 数据 structures are ways 的 organizing 数据 在 a computer so that it can be accessed 和 modified efficiently. Common 数据 structures include arrays, linked lists, stacks, queues, trees, graphs, 和 hash tables. Sorting algorithms arrange items 在 a specified order; common 示例 are bubble sort, merge sort, 和 quicksort. Binary search is an efficient algorithm 为 finding an item 在 a sorted list by repeatedly halving 这 search range.

## Databases

A 数据库 is an organized collection 的 structured 数据 stored electronically. A relational 数据库 stores 数据 在 tables 与 rows 和 columns. SQL (Structured Query 语言) is 这 standard 语言 为 managing 和 querying relational databases. NoSQL databases store 数据 在 formats other than tabular relations, such as documents, key-value pairs, or graphs. Common 数据库 系统 include PostgreSQL, MySQL, SQLite, MongoDB, 和 Redis. An index 在 a 数据库 speeds up 数据 retrieval at 这 cost 的 extra storage.

## System Design 基础

System design focuses on building reliable, scalable, 和 maintainable software 系统. Load balancing distributes traffic across multiple servers to improve availability 和 reduce latency. Horizontal scaling adds more machines; vertical scaling adds more resources to one machine. Caching stores frequently accessed 数据 在 fast storage (为 example Redis, Memcached, or CDN edge caches) to reduce 数据库 load 和 response time. Databases at scale require replication, partitioning (sharding), backup strategies, 和 careful consistency tradeoffs. Microservices split large applications into smaller independently deployable services, while monoliths keep most logic 在 one deployable unit; both approaches involve tradeoffs 在 complexity, 部署 speed, debugging, 和 team autonomy.

## Operating 系统

An operating system (OS) is software that manages computer hardware 和 provides services 为 programs. Common operating 系统 include Windows, macOS, 和 Linux. Linux is an open-source OS kernel used 在 servers, embedded 系统, 和 Android. 这 OS manages processes (running programs), memory, file 系统, 和 input/output devices. A process is a running instance 的 a program. A thread is 这 smallest unit 的 execution within a process.

## Version Control

Version control 系统 track changes to code over time, allowing developers to collaborate 和 revert to previous states. Git is 这 most widely used version control system. A repository (repo) is a collection 的 files 和 their 历史. A commit is a saved snapshot 的 changes. A branch is an independent line 的 开发. A pull request is a proposal to merge changes from one branch into another.

## Software 开发 Practices

Object-oriented programming (OOP) organizes code into objects that combine 数据 和 behavior. Key principles 的 OOP include encapsulation, inheritance, polymorphism, 和 abstraction. Test-driven 开发 (TDD) is a practice 的 writing tests before writing code. Agile is a set 的 software 开发 methodologies that emphasize iterative 开发, collaboration, 和 adaptability. DevOps combines software 开发 和 IT operations to shorten 这 开发 lifecycle. APIs (Application Programming Interfaces) allow different software 系统 to communicate 与 each other.

## Cloud 和 DevOps 基础

Cloud 计算 provides on-demand infrastructure 和 managed services over 这 internet. 这 three major public cloud providers are AWS (Amazon 网络 Services), Microsoft Azure, 和 Google Cloud Platform (GCP). Common service models are IaaS (infrastructure), PaaS (platform), 和 SaaS (software). Core cloud building blocks include compute instances/containers, object storage, managed databases, networking, 和 IAM (Identity 和 Access 管理). CI/CD (Continuous Integration 和 Continuous Delivery/部署) automates build, test, 和 release pipelines so code can move safely from commit to production. Docker packages applications 和 dependencies into portable containers; 在 production these containers are typically deployed via orchestrators (such as Kubernetes), serverless platforms, or managed container services.

## 数据 Formats 和 Tooling

JSON (JavaScript Object Notation) is a lightweight text format built from objects (key/value pairs), arrays, strings, numbers, booleans, 和 null; it is widely used 在 APIs. YAML is a human-friendly configuration format that supports nested structures 和 comments, commonly used 在 CI/CD 和 infrastructure definitions. CSV (Comma-Separated Values) stores tabular 数据 as rows 的 delimited text 和 is common 为 数据 import/export pipelines. XML (eXtensible Markup 语言) is a tag-based structured format used 在 legacy 系统, configuration, 和 document workflows. Developers commonly validate 和 transform these formats 与 linters, schema validators (such as JSON Schema), query tools (`jq`, XPath), 和 parsing libraries 在 their programming 语言.

## Regular Expressions (Regex)

A regular expression is a pattern 语言 used to search, match, extract, 和 transform text. Core regex concepts include literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), 和 escaping special characters. Regex is heavily used 为 input validation, log parsing, text extraction, 和 find/replace automation. Different engines (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested 和 documented to avoid bugs.

## Cybersecurity

Cybersecurity is 这 practice 的 protecting computer 系统, networks, 和 数据 from digital attacks. Common threats include malware (malicious software), phishing (fraudulent 沟通 designed to steal information), ransomware (malware that encrypts 数据 和 demands payment), 和 denial-的-service attacks. Encryption transforms 数据 into an unreadable form that can only be decoded 与 a key. HTTPS uses TLS (Transport Layer 安全) to encrypt 网络 traffic. Strong, unique passwords 和 two-factor authentication are fundamental 安全 practices.

## 安全 Concepts 为 Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application without sharing credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 为 authentication. JWT (JSON 网络 Token) is a compact token format containing claims, often used 为 stateless auth, but it must be signed correctly 和 validated strictly (signature, expiration, issuer, audience). TLS secures 数据 在 transit by providing encryption, integrity, 和 server authentication through certificates. 这 OWASP Top 10 is a widely used list 的 common 网络 application 安全 risks, including broken access control, cryptographic failures, injection, insecure design, 安全 misconfiguration, vulnerable components, 和 insufficient logging/monitoring. Secure 开发 requires defense-在-depth: input validation, output encoding, least privilege, secret 管理, dependency patching, 和 regular 安全 测试.
