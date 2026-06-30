<!-- 
This file was automatically translated from English to Korean.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 기술 Comput

# # What is a Computer?

A computer is an electronic device that processes 데이 터 accord to a set structions called a program. Modern computers are based on von Neumann 아키텍처, which consists a central process unit (CPU), memory, storage, put/output devices. The CPU executes structions. RAM (rom access memory) stores 데이 터 temporarily while computer is runn. Storage devices such as SSDs hard drives store 데이 터 permanently.

# # Programm 언어s

A programm 언어 is a mal 언어 used to write structions computers. Python is a high-level, terpreted, general-purpose programm 언어 known its simple 구문 readability. It is widely used 데이 터 과 학, mache learn, 웹 개발, automation. JavaScript is primary 언어 웹 개발 runs browsers. Java is a compiled, object-oriented 언어 used widely enterprise stware Android 개발. C C++ are lower-level 언어s that give fe-graed control over hardware are used system programm, game 개발, permance-critical applications. Rust is a modern 시스템 programm 언어 focused on 안전한ty permance.

# # How Internet Works

The ternet is a global 네트워크 terconnected computers that communicate us stardized protocols. The World Wide 웹 is a system 웹sites 웹 pages accessed through ternet via browsers. HTTP (HyperText Transfer Protocol) HTTPS (secure HTTP) are protocols used to transfer 웹 pages. An IP address is a unique numerical address assigned to each device on a 네트워크. DNS (Doma Name System) translates human-readable doma names (like google.com) 로 IP addresses. A router directs 네트워크 traffic between devices 네트워크s.

# # 네트워크 Protocols

TCP/IP is foundational protocol suite ternet. IP (Internet Protocol) hles address rout packets between 네트워크s, while TCP (Transmission Control Protocol) provides reliable, ordered delivery 함께 retransmission flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery ( example stream, gam, or DNS queries). HTTP is a stateless application-layer protocol request/response 사소통 between clients servers. HTTPS is HTTP over TLS, add encryption tegrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, stard HTTP verbs (GET, POST, PUT, PATCH, DELETE), stateless teractions. 웹Sockets provide persistent, full-duplex connections so client server can push messages real time, which is useful chat, live dashboards, collaborative apps.

# # Artificial Intelligence

Artificial 인텔리전스 (인공 지능) is simulation human 인텔리전스 by mach, particularly computer 시스템. Mache learn is a subset 인공 지능 which 시스템 learn from 데이 터 to make predictions or decisions 함께out be explicitly programmed. Deep learn is a subset mache learn that uses 신경망 함께 many layers. Neural 네트워크s are computational models loosely spired by structure biological bras. Large 언어 models (대규모 언어 모델) are 인공 지능 models traed on massive amounts text to generate underst natural 언어.

# # Algorithms 데이 터 Structures

An algorithm is a step-by-step procedure solv a problem. 데이 터 structures are ways organiz 데이 터 a computer so that it can be accessed modified efficiently. Common 데이 터 structures 포함하다 arrays, lked lists, stacks, queues, trees, graphs, hash 표. Sort algorithms arrange items a specified order; common 예시 are bubble sort, merge sort, quicksort. Bary search is an efficient algorithm fd an item a sorted list by repeatedly halv search range.

# # 데이 터bases

A 데이 터base is an organized collection 구조화된 데이 터 stored electronically. A relational 데이 터base stores 데이 터 표 함께 rows columns. SQL (Structured Query 언어) is stard 언어 manag query relational 데이 터bases. NoSQL 데이 터bases store 데이 터 mats or than tabular relations, such as documents, key-value pairs, or graphs. Common 데이 터base 시스템 포함하다 PostgreSQL, MySQL, SQLite, MongoDB, Redis. An dex a 데이 터base speeds up 데이 터 retrieval at cost extra storage.

# # System Design 기초

System design focuses on build reliable, scalable, mataable stware 시스템. Load balanc distributes traffic across multiple servers to improve availability reduce latency. Horizontal scal adds more mach; vertical scal adds more resources to one mache. Cach stores frequently accessed 데이 터 fast storage ( example Redis, Memcached, or CDN edge caches) to reduce 데이 터base load response time. 데이 터bases at scale require replication, partition (shard), backup strategies, careful consistency tradefs. Microservices split large applications 로 smaller dependently deployable services, while monoliths keep most logic one deployable unit; both approaches volve tradefs complexity, 배포 speed, debugg, team autonomy.

# # Operat 시스템

An operat system (OS) is stware that manages computer hardware provides services programs. Common operat 시스템 포함하다 Wdows, macOS, Lux. Lux is an open-source OS kernel used servers, embedded 시스템, Android. The OS manages processes (runn programs), memory, file 시스템, put/output devices. A process is a runn stance a program. A thread is smallest unit execution 함께 a process.

# # Version Control

Version control 시스템 track changes to code over time, allow developers to collaborate revert to previous states. Git is most widely used version control system. A repository (repo) is a collection files ir 역사. A commit is a saved snapshot changes. A branch is an dependent le 개발. A pull request is a proposal to merge changes from one branch 로 anor.

# # Stware 개발 Practices

Object-oriented programm (OOP) organizes code 로 objects that combe 데이 터 behavior. Key prciples OOP 포함하다 encapsulation, heritance, polymorphism, abstraction. Test-driven 개발 (TDD) is a practice writ tests 전에 writ code. Agile is a set stware 개발 methodologies that emphasize iterative 개발, collaboration, adaptability. DevOps comb stware 개발 IT operations to shorten 개발 lifecycle. APIs (Application Programm Interfaces) allow different stware 시스템 to communicate 함께 each or.

# # Cloud DevOps 기본

Cloud comput provides on-dem frastructure managed services over ternet. The three major public 클라우드 providers are AWS (Amazon 웹 Services), Microst Azure, Google Cloud Platm (GCP). Common service models are IaaS (frastructure), PaaS (platm), SaaS (stware). Core 클라우드 build blocks 포함하다 compute stances/contaers, object storage, managed 데이 터bases, 네트워크, IAM (Identity Access 관리). CI/CD (Contuous Integration Contuous Delivery/배포) automates build, test, release pipel so code can move 안전한ly from commit to production. Docker packages applications dependencies 로 portable contaers; production se contaers are typically deployed via orchestrators (such as Kubernetes), serverless platms, or managed contaer services.

# # 데이 터 Formats Tool

JSON (JavaScript Object Notation) is a lightweight text mat built from objects (key/value pairs), arrays, strs, numbers, booleans, null; it is widely used APIs. YA기계 학습 is a human-friendly configuration mat that supports nested structures comments, commonly used CI/CD frastructure defitions. CSV (Comma-Separated Values) stores tabular 데이 터 as rows delimited text is common 데이 터 import/export pipel. X기계 학습 (eXtensible Markup 언어) is a tag-based 구조화된 mat used legacy 시스템, configuration, document workflows. Developers commonly validate transm se mats 함께 lters, schema validators (such as JSON Schema), query tools (`jq`, XPath), pars libraries ir programm 언어.

# # Regular Expressions (Regex)

A regular expression is a pattern 언어 used to search, match, extract, transm text. Core regex concepts 포함하다 literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), escap special characters. Regex is heavily used put validation, log pars, text extraction, fd/replace automation. Different eng (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested documented to avoid bugs.

# # Cyber보안

Cyber보안 is practice protect computer 시스템, 네트워크s, 데이 터 from digital attacks. Common threats 포함하다 malware (malicious stware), phish (fraudulent 사소통 designed to steal mation), ransomware (malware that encrypts 데이 터 dems payment), denial--service attacks. Encryption transms 데이 터 로 an unreadable m that can only be decoded 함께 a key. HTTPS uses TLS (Transport Layer 보안) to encrypt 웹 traffic. Strong, unique passwords two-factor auntication are fundamental 보안 practices.

# # 보안 Concepts Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application 함께out shar credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 auntication. JWT (JSON 웹 Token) is a compact token mat conta claims, ten used stateless auth, but it must be signed correctly validated strictly (sig자연, expiration, issuer, 독자). TLS secures 데이 터 transit by provid encryption, tegrity, server auntication through certificates. The OWASP Top 10 is a widely used list common 웹 application 보안 risks, clud broken access control, cryptographic failures, jection, secure design, 보안 misconfiguration, vulnerable components, sufficient logg/monitor. Secure 개발 requires defense--depth: put validation, output encod, least privilege, secret 관리, dependency patch, regular 보안 test.
