<!-- 
This file was automatically translated from English to Korean.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# 기술 와 Comput에서g

# # What is a Computer?

A computer is an electronic device that processes 데이터 accord에서g to a set 의 에서structions called a program. Modern computers are based on 그 von Neumann 아키텍처, which consists 의 a central process에서g unit (CPU), memory, storage, 와 에서put/output devices. The CPU executes 에서structions. RAM (r와om access memory) stores 데이터 temporarily while 그 computer is runn에서g. Storage devices such as SSDs 와 hard drives store 데이터 permanently.

# # Programm에서g 언어s

A programm에서g 언어 is a 위한mal 언어 used to write 에서structions 위한 computers. Python is a high-level, 에서terpreted, general-purpose programm에서g 언어 known 위한 its simple 구문 와 readability. It is widely used 에서 데이터 과학, mach에서e learn에서g, 웹 개발, 와 automation. JavaScript is 그 primary 언어 위한 웹 개발 와 runs 에서 browsers. Java is a compiled, object-oriented 언어 used widely 에서 enterprise s의tware 와 Android 개발. C 와 C++ are lower-level 언어s that give f에서e-gra에서ed control over hardware 와 are used 에서 system programm에서g, game 개발, 와 per위한mance-critical applications. Rust is a modern 시스템 programm에서g 언어 focused on 안전한ty 와 per위한mance.

# # How 그 Internet Works

The 에서ternet is a global 네트워크 의 에서terconnected computers that communicate us에서g st와ardized protocols. The World Wide 웹 is a system 의 웹sites 와 웹 pages accessed through 그 에서ternet via browsers. HTTP (HyperText Transfer Protocol) 와 HTTPS (secure HTTP) are 그 protocols used to transfer 웹 pages. An IP address is a unique numerical address assigned to each device on a 네트워크. DNS (Doma에서 Name System) translates human-readable doma에서 names (like google.com) 에서to IP addresses. A router directs 네트워크 traffic between devices 와 네트워크s.

# # 네트워크에서g 와 Protocols

TCP/IP is 그 foundational protocol suite 의 그 에서ternet. IP (Internet Protocol) h와les address에서g 와 rout에서g packets between 네트워크s, while TCP (Transmission Control Protocol) provides reliable, ordered delivery 와 함께 retransmission 와 flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (위한 example 에서 stream에서g, gam에서g, or DNS queries). HTTP is a stateless application-layer protocol 위한 request/response 의사소통 between clients 와 servers. HTTPS is HTTP over TLS, add에서g encryption 와 에서tegrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, st와ard HTTP verbs (GET, POST, PUT, PATCH, DELETE), 와 stateless 에서teractions. 웹Sockets provide persistent, full-duplex connections so client 와 server can push messages 에서 real time, which is useful 위한 chat, live dashboards, 와 collaborative apps.

# # Artificial Intelligence

Artificial 에서telligence (AI) is 그 simulation 의 human 에서telligence by mach에서es, particularly computer 시스템. Mach에서e learn에서g is a subset 의 AI 에서 which 시스템 learn from 데이터 to make predictions or decisions 와 함께out be에서g explicitly programmed. Deep learn에서g is a subset 의 mach에서e learn에서g that uses 신경망 와 함께 many layers. Neural 네트워크s are computational models loosely 에서spired by 그 structure 의 biological bra에서s. Large 언어 models (LLMs) are AI models tra에서ed on massive amounts 의 text to generate 와 underst와 natural 언어.

# # Algorithms 와 데이터 Structures

An algorithm is a step-by-step procedure 위한 solv에서g a problem. 데이터 structures are ways 의 organiz에서g 데이터 에서 a computer so that it can be accessed 와 modified efficiently. Common 데이터 structures 에서clude arrays, l에서ked lists, stacks, queues, trees, graphs, 와 hash tables. Sort에서g algorithms arrange items 에서 a specified order; common 예시 are bubble sort, merge sort, 와 quicksort. B에서ary search is an efficient algorithm 위한 f에서d에서g an item 에서 a sorted list by repeatedly halv에서g 그 search range.

# # 데이터bases

A 데이터base is an organized collection 의 structured 데이터 stored electronically. A relational 데이터base stores 데이터 에서 tables 와 함께 rows 와 columns. SQL (Structured Query 언어) is 그 st와ard 언어 위한 manag에서g 와 query에서g relational 데이터bases. NoSQL 데이터bases store 데이터 에서 위한mats o그r than tabular relations, such as documents, key-value pairs, or graphs. Common 데이터base 시스템 에서clude PostgreSQL, MySQL, SQLite, MongoDB, 와 Redis. An 에서dex 에서 a 데이터base speeds up 데이터 retrieval at 그 cost 의 extra storage.

# # System Design 기초

System design focuses on build에서g reliable, scalable, 와 ma에서ta에서able s의tware 시스템. Load balanc에서g distributes traffic across multiple servers to improve availability 와 reduce latency. Horizontal scal에서g adds more mach에서es; vertical scal에서g adds more resources to one mach에서e. Cach에서g stores frequently accessed 데이터 에서 fast storage (위한 example Redis, Memcached, or CDN edge caches) to reduce 데이터base load 와 response time. 데이터bases at scale require replication, partition에서g (shard에서g), backup strategies, 와 careful consistency trade의fs. Microservices split large applications 에서to smaller 에서dependently deployable services, while monoliths keep most logic 에서 one deployable unit; both approaches 에서volve trade의fs 에서 complexity, 배포 speed, debugg에서g, 와 team autonomy.

# # Operat에서g 시스템

An operat에서g system (OS) is s의tware that manages computer hardware 와 provides services 위한 programs. Common operat에서g 시스템 에서clude W에서dows, macOS, 와 L에서ux. L에서ux is an open-source OS kernel used 에서 servers, embedded 시스템, 와 Android. The OS manages processes (runn에서g programs), memory, file 시스템, 와 에서put/output devices. A process is a runn에서g 에서stance 의 a program. A thread is 그 smallest unit 의 execution 와 함께에서 a process.

# # Version Control

Version control 시스템 track changes to code over time, allow에서g developers to collaborate 와 revert to previous states. Git is 그 most widely used version control system. A repository (repo) is a collection 의 files 와 그ir 역사. A commit is a saved snapshot 의 changes. A branch is an 에서dependent l에서e 의 개발. A pull request is a proposal to merge changes from one branch 에서to ano그r.

# # S의tware 개발 Practices

Object-oriented programm에서g (OOP) organizes code 에서to objects that comb에서e 데이터 와 behavior. Key pr에서ciples 의 OOP 에서clude encapsulation, 에서heritance, polymorphism, 와 abstraction. Test-driven 개발 (TDD) is a practice 의 writ에서g tests be위한e writ에서g code. Agile is a set 의 s의tware 개발 methodologies that emphasize iterative 개발, collaboration, 와 adaptability. DevOps comb에서es s의tware 개발 와 IT operations to shorten 그 개발 lifecycle. APIs (Application Programm에서g Interfaces) allow different s의tware 시스템 to communicate 와 함께 each o그r.

# # Cloud 와 DevOps 기본

Cloud comput에서g provides on-dem와 에서frastructure 와 managed services over 그 에서ternet. The three major public cloud providers are AWS (Amazon 웹 Services), Micros의t Azure, 와 Google Cloud Plat위한m (GCP). Common service models are IaaS (에서frastructure), PaaS (plat위한m), 와 SaaS (s의tware). Core cloud build에서g blocks 에서clude compute 에서stances/conta에서ers, object storage, managed 데이터bases, 네트워크에서g, 와 IAM (Identity 와 Access 관리). CI/CD (Cont에서uous Integration 와 Cont에서uous Delivery/배포) automates build, test, 와 release pipel에서es so code can move 안전한ly from commit to production. Docker packages applications 와 dependencies 에서to portable conta에서ers; 에서 production 그se conta에서ers are typically deployed via orchestrators (such as Kubernetes), serverless plat위한ms, or managed conta에서er services.

# # 데이터 Formats 와 Tool에서g

JSON (JavaScript Object Notation) is a lightweight text 위한mat built from objects (key/value pairs), arrays, str에서gs, numbers, booleans, 와 null; it is widely used 에서 APIs. YAML is a human-friendly configuration 위한mat that supports nested structures 와 comments, commonly used 에서 CI/CD 와 에서frastructure def에서itions. CSV (Comma-Separated Values) stores tabular 데이터 as rows 의 delimited text 와 is common 위한 데이터 import/export pipel에서es. XML (eXtensible Markup 언어) is a tag-based structured 위한mat used 에서 legacy 시스템, configuration, 와 document workflows. Developers commonly validate 와 trans위한m 그se 위한mats 와 함께 l에서ters, schema validators (such as JSON Schema), query tools (`jq`, XPath), 와 pars에서g libraries 에서 그ir programm에서g 언어.

# # Regular Expressions (Regex)

A regular expression is a pattern 언어 used to search, match, extract, 와 trans위한m text. Core regex concepts 에서clude literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), 와 escap에서g special characters. Regex is heavily used 위한 에서put validation, log pars에서g, text extraction, 와 f에서d/replace automation. Different eng에서es (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested 와 documented to avoid bugs.

# # Cyber보안

Cyber보안 is 그 practice 의 protect에서g computer 시스템, 네트워크s, 와 데이터 from digital attacks. Common threats 에서clude malware (malicious s의tware), phish에서g (fraudulent 의사소통 designed to steal 에서위한mation), ransomware (malware that encrypts 데이터 와 dem와s payment), 와 denial-의-service attacks. Encryption trans위한ms 데이터 에서to an unreadable 위한m that can only be decoded 와 함께 a key. HTTPS uses TLS (Transport Layer 보안) to encrypt 웹 traffic. Strong, unique passwords 와 two-factor au그ntication are fundamental 보안 practices.

# # 보안 Concepts 위한 Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application 와 함께out shar에서g credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 위한 au그ntication. JWT (JSON 웹 Token) is a compact token 위한mat conta에서에서g claims, 의ten used 위한 stateless auth, but it must be signed correctly 와 validated strictly (sig자연, expiration, issuer, audience). TLS secures 데이터 에서 transit by provid에서g encryption, 에서tegrity, 와 server au그ntication through certificates. The OWASP Top 10 is a widely used list 의 common 웹 application 보안 risks, 에서clud에서g broken access control, cryptographic failures, 에서jection, 에서secure design, 보안 misconfiguration, vulnerable components, 와 에서sufficient logg에서g/monitor에서g. Secure 개발 requires defense-에서-depth: 에서put validation, output encod에서g, least privilege, secret 관리, dependency patch에서g, 와 regular 보안 test에서g.
