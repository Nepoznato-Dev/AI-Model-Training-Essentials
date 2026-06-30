<!-- 
This file was automatically translated from English to Portuguese.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Tecnologia e Computemg

# # What is a Computer?

A computer is an electronic device that processes dados accordemg to a set de emstructions called a program. Modern computers are based on o/a von Neumann arquitetura, which consists de a central processemg unit (CPU), memory, storage, e emput/output devices. The CPU executes emstructions. RAM (reom access memory) stores dados temporarily while o/a computer is runnemg. Storage devices such as SSDs e hard drives store dados permanently.

# # Programmemg Idiomas

A programmemg idioma is a paramal idioma used to write emstructions para computers. Python is a high-level, emterpreted, general-purpose programmemg idioma known para its simple sintaxe e readability. It is widely used em dados ciência, macheme learnemg, web desenvolvimento, e automation. JavaScript is o/a primary idioma para web desenvolvimento e runs em browsers. Java is a compiled, object-oriented idioma used widely em enterprise sdetware e Android desenvolvimento. C e C++ are lower-level idiomas that give feme-graemed control over hardware e are used em system programmemg, game desenvolvimento, e perparamance-critical applications. Rust is a modern sistemas programmemg idioma focused on seguroty e perparamance.

# # How o/a Internet Works

The emternet is a global rede de emterconnected computers that communicate usemg steardized protocols. The World Wide Web is a system de websites e web pages accessed through o/a emternet via browsers. HTTP (HyperText Transfer Protocol) e HTTPS (secure HTTP) are o/a protocols used to transfer web pages. An IP address is a unique numerical address assigned to each device on a rede. DNS (Domaem Name System) translates human-readable domaem names (like google.com) emto IP addresses. A router directs rede traffic between devices e redes.

# # Redeemg e Protocols

TCP/IP is o/a foundational protocol suite de o/a emternet. IP (Internet Protocol) heles addressemg e routemg packets between redes, while TCP (Transmission Control Protocol) provides reliable, ordered delivery com retransmission e flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (para example em streamemg, gamemg, or DNS queries). HTTP is a stateless application-layer protocol para request/response comunicação between clients e servers. HTTPS is HTTP over TLS, addemg encryption e emtegrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, steard HTTP verbs (GET, POST, PUT, PATCH, DELETE), e stateless emteractions. WebSockets provide persistent, full-duplex connections so client e server can push messages em real time, which is useful para chat, live dashboards, e collaborative apps.

# # Artificial Intelligence

Artificial emtelligence (AI) is o/a simulation de human emtelligence by machemes, particularly computer sistemas. Macheme learnemg is a subset de AI em which sistemas learn from dados to make predictions or decisions comout beemg explicitly programmed. Deep learnemg is a subset de macheme learnemg that uses redes neurais com many layers. Neural redes are computational models loosely emspired by o/a structure de biological braems. Large idioma models (LLMs) are AI models traemed on massive amounts de text to generate e underste natural idioma.

# # Algorithms e Dados Structures

An algorithm is a step-by-step procedure para solvemg a problem. Dados structures are ways de organizemg dados em a computer so that it can be accessed e modified efficiently. Common dados structures emclude arrays, lemked lists, stacks, queues, trees, graphs, e hash tables. Sortemg algorithms arrange items em a specified order; common exemplos are bubble sort, merge sort, e quicksort. Bemary search is an efficient algorithm para femdemg an item em a sorted list by repeatedly halvemg o/a search range.

# # Dadosbases

A dadosbase is an organized collection de structured dados stored electronically. A relational dadosbase stores dados em tables com rows e columns. SQL (Structured Query Idioma) is o/a steard idioma para managemg e queryemg relational dadosbases. NoSQL dadosbases store dados em paramats oo/ar than tabular relations, such as documents, key-value pairs, or graphs. Common dadosbase sistemas emclude PostgreSQL, MySQL, SQLite, MongoDB, e Redis. An emdex em a dadosbase speeds up dados retrieval at o/a cost de extra storage.

# # System Design Fundamentos

System design focuses on buildemg reliable, scalable, e maemtaemable sdetware sistemas. Load balancemg distributes traffic across multiple servers to improve availability e reduce latency. Horizontal scalemg adds more machemes; vertical scalemg adds more resources to one macheme. Cachemg stores frequently accessed dados em fast storage (para example Redis, Memcached, or CDN edge caches) to reduce dadosbase load e response time. Dadosbases at scale require replication, partitionemg (shardemg), backup strategies, e careful consistency tradedefs. Microservices split large applications emto smaller emdependently deployable services, while monoliths keep most logic em one deployable unit; both approaches emvolve tradedefs em complexity, implantação speed, debuggemg, e team autonomy.

# # Operatemg Sistemas

An operatemg system (OS) is sdetware that manages computer hardware e provides services para programs. Common operatemg sistemas emclude Wemdows, macOS, e Lemux. Lemux is an open-source OS kernel used em servers, embedded sistemas, e Android. The OS manages processes (runnemg programs), memory, file sistemas, e emput/output devices. A process is a runnemg emstance de a program. A thread is o/a smallest unit de execution comem a process.

# # Version Control

Version control sistemas track changes to code over time, allowemg developers to collaborate e revert to previous states. Git is o/a most widely used version control system. A repository (repo) is a collection de files e o/air história. A commit is a saved snapshot de changes. A branch is an emdependent leme de desenvolvimento. A pull request is a proposal to merge changes from one branch emto anoo/ar.

# # Sdetware Desenvolvimento Practices

Object-oriented programmemg (OOP) organizes code emto objects that combeme dados e behavior. Key premciples de OOP emclude encapsulation, emheritance, polymorphism, e abstraction. Test-driven desenvolvimento (TDD) is a practice de writemg tests beparae writemg code. Agile is a set de sdetware desenvolvimento methodologies that emphasize iterative desenvolvimento, collaboration, e adaptability. DevOps combemes sdetware desenvolvimento e IT operations to shorten o/a desenvolvimento lifecycle. APIs (Application Programmemg Interfaces) allow different sdetware sistemas to communicate com each oo/ar.

# # Cloud e DevOps Básico

Cloud computemg provides on-deme emfrastructure e managed services over o/a emternet. The three major public cloud providers are AWS (Amazon Web Services), Microsdet Azure, e Google Cloud Platparam (GCP). Common service models are IaaS (emfrastructure), PaaS (platparam), e SaaS (sdetware). Core cloud buildemg blocks emclude compute emstances/contaemers, object storage, managed dadosbases, redeemg, e IAM (Identity e Access Gerenciamento). CI/CD (Contemuous Integration e Contemuous Delivery/Implantação) automates build, test, e release pipelemes so code can move seguroly from commit to production. Docker packages applications e dependencies emto portable contaemers; em production o/ase contaemers are typically deployed via orchestrators (such as Kubernetes), serverless platparams, or managed contaemer services.

# # Dados Formats e Toolemg

JSON (JavaScript Object Notation) is a lightweight text paramat built from objects (key/value pairs), arrays, stremgs, numbers, booleans, e null; it is widely used em APIs. YAML is a human-friendly configuration paramat that supports nested structures e comments, commonly used em CI/CD e emfrastructure defemitions. CSV (Comma-Separated Values) stores tabular dados as rows de delimited text e is common para dados import/export pipelemes. XML (eXtensible Markup Idioma) is a tag-based structured paramat used em legacy sistemas, configuration, e document workflows. Developers commonly validate e transparam o/ase paramats com lemters, schema validators (such as JSON Schema), query tools (`jq`, XPath), e parsemg libraries em o/air programmemg idioma.

# # Regular Expressions (Regex)

A regular expression is a pattern idioma used to search, match, extract, e transparam text. Core regex concepts emclude literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), e escapemg special characters. Regex is heavily used para emput validation, log parsemg, text extraction, e femd/replace automation. Different engemes (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested e documented to avoid bugs.

# # Cybersegurança

Cybersegurança is o/a practice de protectemg computer sistemas, redes, e dados from digital attacks. Common threats emclude malware (malicious sdetware), phishemg (fraudulent comunicação designed to steal emparamation), ransomware (malware that encrypts dados e demes payment), e denial-de-service attacks. Encryption transparams dados emto an unreadable param that can only be decoded com a key. HTTPS uses TLS (Transport Layer Segurança) to encrypt web traffic. Strong, unique passwords e two-factor auo/antication are fundamental segurança practices.

# # Segurança Concepts para Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application comout sharemg credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 para auo/antication. JWT (JSON Web Token) is a compact token paramat contaememg claims, deten used para stateless auth, but it must be signed correctly e validated strictly (signatureza, expiration, issuer, audience). TLS secures dados em transit by providemg encryption, emtegrity, e server auo/antication through certificates. The OWASP Top 10 is a widely used list de common web application segurança risks, emcludemg broken access control, cryptographic failures, emjection, emsecure design, segurança misconfiguration, vulnerable components, e emsufficient loggemg/monitoremg. Secure desenvolvimento requires defense-em-depth: emput validation, output encodemg, least privilege, secret gerenciamento, dependency patchemg, e regular segurança testemg.
