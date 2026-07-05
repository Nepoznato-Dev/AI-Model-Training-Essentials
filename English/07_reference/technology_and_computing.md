# Technology and Computing

## What is a Computer?

A computer is an electronic device that processes data according to a set of instructions called a program. Modern computers are based on the von Neumann architecture, which consists of a central processing unit (CPU), memory, storage, and input/output devices. The CPU executes instructions. RAM (random access memory) stores data temporarily while the computer is running. Storage devices such as SSDs and hard drives store data permanently.

## Programming Languages

A programming language is a formal language used to write instructions for computers. Python is a high-level, interpreted, general-purpose programming language known for its simple syntax and readability. It is widely used in data science, machine learning, web development, and automation. JavaScript is the primary language for web development and runs in browsers. Java is a compiled, object-oriented language used widely in enterprise software and Android development. C and C++ are lower-level languages that give fine-grained control over hardware and are used in system programming, game development, and performance-critical applications. Rust is a modern systems programming language focused on safety and performance.

## How the Internet Works

The internet is a global network of interconnected computers that communicate using standardized protocols. The World Wide Web is a system of websites and web pages accessed through the internet via browsers. HTTP (HyperText Transfer Protocol) and HTTPS (secure HTTP) are the protocols used to transfer web pages. An IP address is a unique numerical address assigned to each device on a network. DNS (Domain Name System) translates human-readable domain names (like google.com) into IP addresses. A router directs network traffic between devices and networks.

## Networking and Protocols

TCP/IP is the foundational protocol suite of the internet. IP (Internet Protocol) handles addressing and routing packets between networks, while TCP (Transmission Control Protocol) provides reliable, ordered delivery with retransmission and flow control. UDP is a connectionless alternative used when low latency matters more than guaranteed delivery (for example in streaming, gaming, or DNS queries). HTTP is a stateless application-layer protocol for request/response communication between clients and servers. HTTPS is HTTP over TLS, adding encryption and integrity protection. REST (Representational State Transfer) is an API architectural style that uses resources, standard HTTP verbs (GET, POST, PUT, PATCH, DELETE), and stateless interactions. WebSockets provide persistent, full-duplex connections so client and server can push messages in real time, which is useful for chat, live dashboards, and collaborative apps.

## Artificial Intelligence

Artificial intelligence (AI) is the simulation of human intelligence by machines, particularly computer systems. Machine learning is a subset of AI in which systems learn from data to make predictions or decisions without being explicitly programmed. Deep learning is a subset of machine learning that uses neural networks with many layers. Neural networks are computational models loosely inspired by the structure of biological brains. Large language models (LLMs) are AI models trained on massive amounts of text to generate and understand natural language.

## Algorithms and Data Structures

An algorithm is a step-by-step procedure for solving a problem. Data structures are ways of organizing data in a computer so that it can be accessed and modified efficiently. Common data structures include arrays, linked lists, stacks, queues, trees, graphs, and hash tables. Sorting algorithms arrange items in a specified order; common examples are bubble sort, merge sort, and quicksort. Binary search is an efficient algorithm for finding an item in a sorted list by repeatedly halving the search range.

## Databases

A database is an organized collection of structured data stored electronically. A relational database stores data in tables with rows and columns. SQL (Structured Query Language) is the standard language for managing and querying relational databases. NoSQL databases store data in formats other than tabular relations, such as documents, key-value pairs, or graphs. Common database systems include PostgreSQL, MySQL, SQLite, MongoDB, and Redis. An index in a database speeds up data retrieval at the cost of extra storage.

## System Design Fundamentals

System design focuses on building reliable, scalable, and maintainable software systems. Load balancing distributes traffic across multiple servers to improve availability and reduce latency. Horizontal scaling adds more machines; vertical scaling adds more resources to one machine. Caching stores frequently accessed data in fast storage (for example Redis, Memcached, or CDN edge caches) to reduce database load and response time. Databases at scale require replication, partitioning (sharding), backup strategies, and careful consistency tradeoffs. Microservices split large applications into smaller independently deployable services, while monoliths keep most logic in one deployable unit; both approaches involve tradeoffs in complexity, deployment speed, debugging, and team autonomy.

## Operating Systems

An operating system (OS) is software that manages computer hardware and provides services for programs. Common operating systems include Windows, macOS, and Linux. Linux is an open-source OS kernel used in servers, embedded systems, and Android. The OS manages processes (running programs), memory, file systems, and input/output devices. A process is a running instance of a program. A thread is the smallest unit of execution within a process.

## Version Control

Version control systems track changes to code over time, allowing developers to collaborate and revert to previous states. Git is the most widely used version control system. A repository (repo) is a collection of files and their history. A commit is a saved snapshot of changes. A branch is an independent line of development. A pull request is a proposal to merge changes from one branch into another.

## Software Development Practices

Object-oriented programming (OOP) organizes code into objects that combine data and behavior. Key principles of OOP include encapsulation, inheritance, polymorphism, and abstraction. Test-driven development (TDD) is a practice of writing tests before writing code. Agile is a set of software development methodologies that emphasize iterative development, collaboration, and adaptability. DevOps combines software development and IT operations to shorten the development lifecycle. APIs (Application Programming Interfaces) allow different software systems to communicate with each other.

## Cloud and DevOps Basics

Cloud computing provides on-demand infrastructure and managed services over the internet. The three major public cloud providers are AWS (Amazon Web Services), Microsoft Azure, and Google Cloud Platform (GCP). Common service models are IaaS (infrastructure), PaaS (platform), and SaaS (software). Core cloud building blocks include compute instances/containers, object storage, managed databases, networking, and IAM (Identity and Access Management). CI/CD (Continuous Integration and Continuous Delivery/Deployment) automates build, test, and release pipelines so code can move safely from commit to production. Docker packages applications and dependencies into portable containers; in production these containers are typically deployed via orchestrators (such as Kubernetes), serverless platforms, or managed container services.

## Data Formats and Tooling

JSON (JavaScript Object Notation) is a lightweight text format built from objects (key/value pairs), arrays, strings, numbers, booleans, and null; it is widely used in APIs. YAML is a human-friendly configuration format that supports nested structures and comments, commonly used in CI/CD and infrastructure definitions. CSV (Comma-Separated Values) stores tabular data as rows of delimited text and is common for data import/export pipelines. XML (eXtensible Markup Language) is a tag-based structured format used in legacy systems, configuration, and document workflows. Developers commonly validate and transform these formats with linters, schema validators (such as JSON Schema), query tools (`jq`, XPath), and parsing libraries in their programming language.

## Regular Expressions (Regex)

A regular expression is a pattern language used to search, match, extract, and transform text. Core regex concepts include literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), and escaping special characters. Regex is heavily used for input validation, log parsing, text extraction, and find/replace automation. Different engines (PCRE, JavaScript, Python `re`, RE2) have different feature sets, so behavior may vary between tools. Regex is powerful but can become hard to read; complex patterns should be tested and documented to avoid bugs.

## Cybersecurity

Cybersecurity is the practice of protecting computer systems, networks, and data from digital attacks. Common threats include malware (malicious software), phishing (fraudulent communication designed to steal information), ransomware (malware that encrypts data and demands payment), and denial-of-service attacks. Encryption transforms data into an unreadable form that can only be decoded with a key. HTTPS uses TLS (Transport Layer Security) to encrypt web traffic. Strong, unique passwords and two-factor authentication are fundamental security practices.

## Security Concepts for Developers

OAuth 2.0 is an authorization framework that lets users grant limited access to an application without sharing credentials directly. OpenID Connect (OIDC) is an identity layer built on OAuth 2.0 for authentication. JWT (JSON Web Token) is a compact token format containing claims, often used for stateless auth, but it must be signed correctly and validated strictly (signature, expiration, issuer, audience). TLS secures data in transit by providing encryption, integrity, and server authentication through certificates. The OWASP Top 10 is a widely used list of common web application security risks, including broken access control, cryptographic failures, injection, insecure design, security misconfiguration, vulnerable components, and insufficient logging/monitoring. Secure development requires defense-in-depth: input validation, output encoding, least privilege, secret management, dependency patching, and regular security testing.
