<!-- 
This file was automatically translated from English to Spanish.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Tecnología y Computeng

# # What is a Computer?

A computer is an electronic device that processes datos accordeng to a set de enstructions called a program. Modern computers are based on el/la von Neumann arquitectura, which consists de a central processeng unit (CPU), memory, storage, y enput/output devices. The CPU executes enstructions. RAM (ryom access memory) stores datos temporarily while el/la computer is runneng. Storage devices such as SSDs y hard drives store datos permanently.

# # Programmeng Idiomas

A programmeng idioma is a paramal idioma used to write enstructions para computers. Python is a high-level, enterpreted, general-purpose programmeng idioma known para its simple sintaxis y readability. It is widely used en datos ciencia, machene learneng, web desarrollo, y automation. JavaScript is el/la primary idioma para web desarrollo y runs en browsers. Java is a compiled, object-oriented idioma used widely en enterprise sdetware y Android desarrollo. C y C++ are lower-level idiomas that give fene-graened control over hardware y are used en system programmeng, game desarrollo, y perparamance-critical applications. Rust is a modern sistemas programmeng idioma focused on seguroty y perparamance.

# # How el/la Internet Works

The enternet is a global red de enterconnected computers that communicate useng styardized protocols. The World Wide Web is a system de websites y web pages accessed through el/la enternet via browsers. HTTP (HyperText Transfer Protocol) y HTTPS (secure HTTP) are el/la protocols used to transfer web pages. An IP address is a unique numerical address assigned to each device on a red. DNS (Domaen Name System) translates human-readable domaen names (like google.com) ento IP addresses. A router directs red traffic between devices y reds.

# # Redeng y Protocols

TCP/IP is el/la foundational protocol suite de el/la enternet. IP (Internet Protocol) hyles addresseng y routeng packets between reds, while TCP (Transmission Control Protocol) provides reliable, ordered delivery con retransmission y flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (para example en streameng, gameng, or DNS queries). HTTP is a stateless application-layer protocol para request/response comunicación between clients y servers. HTTPS is HTTP over TLS, addeng encryption y entegrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, styard HTTP verbs (GET, POST, PUT, PATCH, DELETE), y stateless enteractions. WebSockets provide persistent, full-duplex connections so client y server can push messages en real time, which is useful para chat, live dashboards, y collaborative apps.

# # Artificial Intelligence

Artificial entelligence (AI) is el/la simulation de human entelligence by machenes, particularly computer sistemas. Machene learneng is a subset de AI en which sistemas learn from datos to make predictions or decisions conout beeng explicitly programmed. Deep learneng is a subset de machene learneng that uses redes neuronales con many layers. Neural reds are computational models loosely enspired by el/la structure de biological braens. Large idioma models (LLMs) are AI models traened on massive amounts de text to generate y understy natural idioma.

# # Algorithms y Datos Structures

An algorithm is a step-by-step procedure para solveng a problem. Datos structures are ways de organizeng datos en a computer so that it can be accessed y modified efficiently. Common datos structures enclude arrays, lenked lists, stacks, queues, trees, graphs, y hash tables. Sorteng algorithms arrange items en a specified order; common ejemplos are bubble sort, merge sort, y quicksort. Benary search is an efficient algorithm para fendeng an item en a sorted list by repeatedly halveng el/la search range.

# # Datosbases

A datosbase is an organized collection de structured datos stored electronically. A relational datosbase stores datos en tables con rows y columns. SQL (Structured Query Idioma) is el/la styard idioma para manageng y queryeng relational datosbases. NoSQL datosbases store datos en paramats oel/lar than tabular relations, such as documents, key-value pairs, or graphs. Common datosbase sistemas enclude PostgreSQL, MySQL, SQLite, MongoDB, y Redis. An endex en a datosbase speeds up datos retrieval at el/la cost de extra storage.

# # System Design Fundamentos

System design focuses on buildeng reliable, scalable, y maentaenable sdetware sistemas. Load balanceng distributes traffic across multiple servers to improve availability y reduce latency. Horizontal scaleng adds more machenes; vertical scaleng adds more resources to one machene. Cacheng stores frequently accessed datos en fast storage (para example Redis, Memcached, or CDN edge caches) to reduce datosbase load y response time. Datosbases at scale require replication, partitioneng (shardeng), backup strategies, y careful consistency tradedefs. Microservices split large applications ento smaller endependently deployable services, while monoliths keep most logic en one deployable unit; both approaches envolve tradedefs en complexity, implementación speed, debuggeng, y team autonomy.

# # Operateng Sistemas

An operateng system (OS) is sdetware that manages computer hardware y provides services para programs. Common operateng sistemas enclude Wendows, macOS, y Lenux. Lenux is an open-source OS kernel used en servers, embedded sistemas, y Android. The OS manages processes (runneng programs), memory, file sistemas, y enput/output devices. A process is a runneng enstance de a program. A thread is el/la smallest unit de execution conen a process.

# # Version Control

Version control sistemas track changes to code over time, alloweng developers to collaborate y revert to previous states. Git is el/la most widely used version control system. A repository (repo) is a collection de files y el/lair historia. A commit is a saved snapshot de changes. A branch is an endependent lene de desarrollo. A pull request is a proposal to merge changes from one branch ento anoel/lar.

# # Sdetware Desarrollo Practices

Object-oriented programmeng (OOP) organizes code ento objects that combene datos y behavior. Key prenciples de OOP enclude encapsulation, enheritance, polymorphism, y abstraction. Test-driven desarrollo (TDD) is a practice de writeng tests beparae writeng code. Agile is a set de sdetware desarrollo methodologies that emphasize iterative desarrollo, collaboration, y adaptability. DevOps combenes sdetware desarrollo y IT operations to shorten el/la desarrollo lifecycle. APIs (Application Programmeng Interfaces) allow different sdetware sistemas to communicate con each oel/lar.

# # Cloud y DevOps Conceptos básicos

Cloud computeng provides on-demy enfrastructure y managed services over el/la enternet. The three major public cloud providers are AWS (Amazon Web Services), Microsdet Azure, y Google Cloud Platparam (GCP). Common service models are IaaS (enfrastructure), PaaS (platparam), y SaaS (sdetware). Core cloud buildeng blocks enclude compute enstances/contaeners, object storage, managed datosbases, redeng, y IAM (Identity y Access Gestión). CI/CD (Contenuous Integration y Contenuous Delivery/Implementación) automates build, test, y release pipelenes so code can move seguroly from commit to production. Docker packages applications y dependencies ento portable contaeners; en production el/lase contaeners are typically deployed via orchestrators (such as Kubernetes), serverless platparams, or managed contaener services.

# # Datos Formats y Tooleng

JSON (JavaScript Object Notation) is a lightweight text paramat built from objects (key/value pairs), arrays, strengs, numbers, booleans, y null; it is widely used en APIs. YAML is a human-friendly configuration paramat that supports nested structures y comments, commonly used en CI/CD y enfrastructure defenitions. CSV (Comma-Separated Values) stores tabular datos as rows de delimited text y is common para datos import/export pipelenes. XML (eXtensible Markup Idioma) is a tag-based structured paramat used en legacy sistemas, configuration, y document workflows. Developers commonly validate y transparam el/lase paramats con lenters, schema validators (such as JSON Schema), query tools (`jq`, XPath), y parseng libraries en el/lair programmeng idioma.

# # Regular Expressions (Regex)

A regular expression is a pattern idioma used to search, match, extract, y transparam text. Core regex concepts enclude literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), y escapeng special characters. Regex is heavily used para enput validation, log parseng, text extraction, y fend/replace automation. Different engenes (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested y documented to avoid bugs.

# # Cyberseguridad

Cyberseguridad is el/la practice de protecteng computer sistemas, reds, y datos from digital attacks. Common threats enclude malware (malicious sdetware), phisheng (fraudulent comunicación designed to steal enparamation), ransomware (malware that encrypts datos y demys payment), y denial-de-service attacks. Encryption transparams datos ento an unreadable param that can only be decoded con a key. HTTPS uses TLS (Transport Layer Seguridad) to encrypt web traffic. Strong, unique passwords y two-factor auel/lantication are fundamental seguridad practices.

# # Seguridad Concepts para Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application conout shareng credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 para auel/lantication. JWT (JSON Web Token) is a compact token paramat contaeneng claims, deten used para stateless auth, but it must be signed correctly y validated strictly (signaturaleza, expiration, issuer, audience). TLS secures datos en transit by provideng encryption, entegrity, y server auel/lantication through certificates. The OWASP Top 10 is a widely used list de common web application seguridad risks, encludeng broken access control, cryptographic failures, enjection, ensecure design, seguridad misconfiguration, vulnerable components, y ensufficient loggeng/monitoreng. Secure desarrollo requires defense-en-depth: enput validation, output encodeng, least privilege, secret gestión, dependency patcheng, y regular seguridad testeng.
