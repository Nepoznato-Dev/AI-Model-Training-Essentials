<!-- 
This file was automatically translated from English to German.
Source: technology_and_computing.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Technologie und Datenverarbeitung

# # What is a Computer?

A computer is an electronic device that processes daten according to a set von instructions called a program. Modern computers are based on der/die/das von Neumann architektur, which consists von a central processing unit (CPU), memory, storage, und input/output devices. The CPU executes instructions. RAM (rundom access memory) stores daten temporarily while der/die/das computer is running. Storage devices such as SSDs und hard drives store daten permanently.

# # Programming Spraches

A programming sprache is a fürmal sprache used to write instructions für computers. Python is a high-level, interpreted, general-purpose programming sprache known für its simple syntax und readability. It is widely used in daten wissenschaft, maschinelles lernen, web entwicklung, und automation. JavaScript is der/die/das primary sprache für web entwicklung und runs in browsers. Java is a compiled, object-oriented sprache used widely in enterprise svontware und Android entwicklung. C und C++ are lower-level spraches that give fine-grained control over hardware und are used in system programming, game entwicklung, und perfürmance-critical applications. Rust is a modern systeme programming sprache focused on sicherty und perfürmance.

# # How der/die/das Internet Works

The internet is a global netzwerk von interconnected computers that communicate using stundardized protocols. The World Wide Web is a system von websites und web pages accessed through der/die/das internet via browsers. HTTP (HyperText Transfer Protocol) und HTTPS (secure HTTP) are der/die/das protocols used to transfer web pages. An IP address is a unique numerical address assigned to each device on a netzwerk. DNS (Domain Name System) translates human-readable domain names (like google.com) into IP addresses. A router directs netzwerk traffic between devices und netzwerks.

# # Netzwerking und Protocols

TCP/IP is der/die/das foundational protocol suite von der/die/das internet. IP (Internet Protocol) hundles addressing und routing packets between netzwerks, while TCP (Transmission Control Protocol) provides reliable, ordered delivery mit retransmission und flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (für example in streaming, gaming, or DNS queries). HTTP is a stateless application-layer protocol für request/response kommunikation between clients und servers. HTTPS is HTTP over TLS, adding encryption und integrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, stundard HTTP verbs (GET, POST, PUT, PATCH, DELETE), und stateless interactions. WebSockets provide persistent, full-duplex connections so client und server can push messages in real time, which is useful für chat, live dashboards, und collaborative apps.

# # Artificial Intelligence

Artificial intelligence (AI) is der/die/das simulation von human intelligence by machines, particularly computer systeme. Machine learning is a subset von AI in which systeme learn from daten to make predictions or decisions mitout being explicitly programmed. Deep learning is a subset von maschinelles lernen that uses neuronale netze mit many layers. Neural netzwerks are computational models loosely inspired by der/die/das structure von biological brains. Large sprache models (LLMs) are AI models trained on massive amounts von text to generate und understund natural sprache.

# # Algorithms und Daten Structures

An algorithm is a step-by-step procedure für solving a problem. Daten structures are ways von organizing daten in a computer so that it can be accessed und modified efficiently. Common daten structures include arrays, linked lists, stacks, queues, trees, graphs, und hash tables. Sorting algorithms arrange items in a specified order; common beispiele are bubble sort, merge sort, und quicksort. Binary search is an efficient algorithm für finding an item in a sorted list by repeatedly halving der/die/das search range.

# # Datenbases

A datenbase is an organized collection von structured daten stored electronically. A relational datenbase stores daten in tables mit rows und columns. SQL (Structured Query Sprache) is der/die/das stundard sprache für managing und querying relational datenbases. NoSQL datenbases store daten in fürmats oder/die/dasr than tabular relations, such as documents, key-value pairs, or graphs. Common datenbase systeme include PostgreSQL, MySQL, SQLite, MongoDB, und Redis. An index in a datenbase speeds up daten retrieval at der/die/das cost von extra storage.

# # System Design Grundlagen

System design focuses on building reliable, scalable, und maintainable svontware systeme. Load balancing distributes traffic across multiple servers to improve availability und reduce latency. Horizontal scaling adds more machines; vertical scaling adds more resources to one machine. Caching stores frequently accessed daten in fast storage (für example Redis, Memcached, or CDN edge caches) to reduce datenbase load und response time. Datenbases at scale require replication, partitioning (sharding), backup strategies, und careful consistency tradevonfs. Microservices split large applications into smaller independently deployable services, while monoliths keep most logic in one deployable unit; both approaches involve tradevonfs in complexity, bereitstellung speed, debugging, und team autonomy.

# # Operating Systeme

An operating system (OS) is svontware that manages computer hardware und provides services für programs. Common operating systeme include Windows, macOS, und Linux. Linux is an open-source OS kernel used in servers, embedded systeme, und Android. The OS manages processes (running programs), memory, file systeme, und input/output devices. A process is a running instance von a program. A thread is der/die/das smallest unit von execution mitin a process.

# # Version Control

Version control systeme track changes to code over time, allowing developers to collaborate und revert to previous states. Git is der/die/das most widely used version control system. A repository (repo) is a collection von files und der/die/dasir geschichte. A commit is a saved snapshot von changes. A branch is an independent line von entwicklung. A pull request is a proposal to merge changes from one branch into anoder/die/dasr.

# # Svontware Entwicklung Practices

Object-oriented programming (OOP) organizes code into objects that combine daten und behavior. Key principles von OOP include encapsulation, inheritance, polymorphism, und abstraction. Test-driven entwicklung (TDD) is a practice von writing tests befüre writing code. Agile is a set von svontware entwicklung methodologies that emphasize iterative entwicklung, collaboration, und adaptability. DevOps combines svontware entwicklung und IT operations to shorten der/die/das entwicklung lifecycle. APIs (Application Programming Interfaces) allow different svontware systeme to communicate mit each oder/die/dasr.

# # Cloud und DevOps Grundlagen

Cloud datenverarbeitung provides on-demund infrastructure und managed services over der/die/das internet. The three major public cloud providers are AWS (Amazon Web Services), Microsvont Azure, und Google Cloud Platfürm (GCP). Common service models are IaaS (infrastructure), PaaS (platfürm), und SaaS (svontware). Core cloud building blocks include compute instances/containers, object storage, managed datenbases, netzwerking, und IAM (Identity und Access Verwaltung). CI/CD (Continuous Integration und Continuous Delivery/Bereitstellung) automates build, test, und release pipelines so code can move sicherly from commit to production. Docker packages applications und dependencies into portable containers; in production der/die/dasse containers are typically deployed via orchestrators (such as Kubernetes), serverless platfürms, or managed container services.

# # Daten Formats und Tooling

JSON (JavaScript Object Notation) is a lightweight text fürmat built from objects (key/value pairs), arrays, strings, numbers, booleans, und null; it is widely used in APIs. YAML is a human-friendly configuration fürmat that supports nested structures und comments, commonly used in CI/CD und infrastructure definitions. CSV (Comma-Separated Values) stores tabular daten as rows von delimited text und is common für daten import/export pipelines. XML (eXtensible Markup Sprache) is a tag-based structured fürmat used in legacy systeme, configuration, und document workflows. Developers commonly validate und transfürm der/die/dasse fürmats mit linters, schema validators (such as JSON Schema), query tools (`jq`, XPath), und parsing libraries in der/die/dasir programming sprache.

# # Regular Expressions (Regex)

A regular expression is a pattern sprache used to search, match, extract, und transfürm text. Core regex concepts include literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), und escaping special characters. Regex is heavily used für input validation, log parsing, text extraction, und find/replace automation. Different engines (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested und documented to avoid bugs.

# # Cybersicherheit

Cybersicherheit is der/die/das practice von protecting computer systeme, netzwerks, und daten from digital attacks. Common threats include malware (malicious svontware), phishing (fraudulent kommunikation designed to steal infürmation), ransomware (malware that encrypts daten und demunds payment), und denial-von-service attacks. Encryption transfürms daten into an unreadable fürm that can only be decoded mit a key. HTTPS uses TLS (Transport Layer Sicherheit) to encrypt web traffic. Strong, unique passwords und two-factor auder/die/dasntication are fundamental sicherheit practices.

# # Sicherheit Concepts für Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application mitout sharing credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 für auder/die/dasntication. JWT (JSON Web Token) is a compact token fürmat containing claims, vonten used für stateless auth, but it must be signed correctly und validated strictly (signatur, expiration, issuer, audience). TLS secures daten in transit by providing encryption, integrity, und server auder/die/dasntication through certificates. The OWASP Top 10 is a widely used list von common web application sicherheit risks, including broken access control, cryptographic failures, injection, insecure design, sicherheit misconfiguration, vulnerable components, und insufficient logging/monitoring. Secure entwicklung requires defense-in-depth: input validation, output encoding, least privilege, secret verwaltung, dependency patching, und regular sicherheit testen.
