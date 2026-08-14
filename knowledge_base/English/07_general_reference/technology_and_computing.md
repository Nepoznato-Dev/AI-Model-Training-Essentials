---
# Metadata
title: "Technology and Computing"
description: "Computing basics, internet, databases, cloud, security"
category: "General Reference"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "General Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, computing, general-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Technology and Computing

Computing is everywhere — in your phone, your car, your refrigerator, your medical devices, and the infrastructure that runs modern society. You do not need to be a programmer to benefit from understanding how it all works. This file covers the fundamentals: what a computer is, how the internet works, how software is built, and the concepts that shape the digital world.

> **Want to go deeper?** This file is a broad overview. For detailed coverage of any topic, see the dedicated files in [`01_coding_and_technology/`](../01_coding_and_technology/) — including [database systems](../01_coding_and_technology/database_systems.md), [cloud architecture](../01_coding_and_technology/cloud_architecture.md), [networking](../01_coding_and_technology/networking_basics.md), and.

---

## What Is a Computer?

At its core, every computer — from a smartphone to a supercomputer — does the same thing: it takes input, processes it according to instructions (a program), and produces output. The magic is in the speed and scale.

### The Von Neumann Architecture

Almost all modern computers follow this basic design:

| Component | What It Does | Analogy |
|-----------|-------------|---------|
| **CPU** (Central Processing Unit) | Executes instructions; the "brain" | The chef following a recipe |
| **RAM** (Memory) | Stores data the CPU is actively using; lost when power is off | The countertop — fast access, limited space |
| **Storage** (SSD/HDD) | Stores data permanently | The pantry — slower access, much more space |
| **Input/Output** | Keyboard, mouse, screen, network | How the chef receives orders and delivers food |
| **GPU** (Graphics Processing Unit) | Specialized processor for parallel tasks (graphics, AI) | A team of assistants all doing the same task simultaneously |

**Key insight**: RAM is fast but temporary. Storage is slow but permanent. When your computer "feels slow," it is often because it is running out of RAM and has to use storage as temporary memory (swapping), which is much slower.

---

## Programming Languages — Talking to Computers

A programming language is a set of instructions that a computer can execute. Different languages are designed for different purposes. For detailed coverage of 34 individual languages, see the [`programming_languages/`](../01_coding_and_technology/programming_languages/) folder.

| Language | Best For | Why Choose It |
|----------|---------|---------------|
| **Python** | Data science, AI, automation, web backends | Simple syntax; huge ecosystem; great for beginners |
| **JavaScript** | Web frontends, full-stack (Node.js) | Runs in every browser; essential for web development |
| **Java** | Enterprise software, Android apps | Platform-independent (JVM); large ecosystem |
| **C/C++** | Systems programming, games, embedded | Maximum performance; direct hardware control |
| **Rust** | Systems programming with safety guarantees | Memory safety without garbage collection |
| **Go** | Cloud services, microservices, CLI tools | Simple; excellent concurrency; fast compilation |
| **SQL** | Database queries | The universal language for working with data |
| **TypeScript** | Large-scale web applications | JavaScript with type checking; catches bugs early |

---

## How the Internet Works

The internet is not the same thing as the web. The internet is the physical network — cables, routers, servers, and protocols that connect billions of devices. The World Wide Web is one service that runs on the internet (along with email, file transfer, streaming, gaming, etc.).

### The Journey of a Web Request

When you type `https://www.example.com` into your browser:

1. **DNS lookup**: Your browser asks a DNS server to translate "www.example.com" into an IP address (like 93.184.216.34).
2. **TCP connection**: Your device establishes a connection to that IP address using TCP (a protocol that guarantees reliable delivery).
3. **TLS handshake**: If using HTTPS, your browser and the server negotiate an encrypted connection.
4. **HTTP request**: Your browser sends a request: "Give me the page at /index.html."
5. **Server processing**: The web server finds the page, possibly queries a database, and prepares a response.
6. **HTTP response**: The server sends back HTML, CSS, and JavaScript.
7. **Rendering**: Your browser parses the HTML, applies CSS styles, and executes JavaScript to display the page.

This entire process typically takes less than a second.

### Key Protocols

| Protocol | What It Does | Layer |
|----------|-------------|-------|
| **IP** (Internet Protocol) | Routes packets between networks | Network |
| **TCP** | Reliable, ordered delivery (retransmits lost packets) | Transport |
| **UDP** | Fast, unreliable delivery (no retransmission) | Transport |
| **HTTP/HTTPS** | Web page transfer (HTTPS adds encryption) | Application |
| **DNS** | Translates domain names to IP addresses | Application |
| **SSH** | Secure remote access to computers | Application |
| **SMTP/IMAP** | Email sending and receiving | Application |

---

## Software Development — How Programs Get Built

### The Development Process

1. **Write code**: Developers write instructions in a programming language.
2. **Test code**: Run the code to verify it works correctly.
3. **Version control**: Track changes using Git — the universal standard.
4. **Review**: Other developers check the code for errors and quality.
5. **Build**: Convert source code into a runnable program (compilation).
6. **Deploy**: Release the program to users (servers, app stores, etc.).
7. **Monitor**: Watch for errors and performance issues in production.

### Key Concepts

| Concept | What It Means | Why It Matters |
|---------|---------------|----------------|
| **Version control (Git)** | Track every change to code over time | Collaboration; ability to undo mistakes |
| **API** (Application Programming Interface) | A defined way for software components to communicate | Allows different systems to work together |
| **Database** | Organized storage for data | Every application needs to store and retrieve data |
| **Testing** | Automated checks that code works correctly | Prevents bugs from reaching users |
| **CI/CD** (Continuous Integration/Delivery) | Automated pipeline from code commit to production | Faster, safer releases |
| **Containerization (Docker)** | Package an application with all its dependencies | "Works on my machine" becomes "works everywhere" |

---

## Databases — Where Data Lives

Every application needs to store data. Databases are the systems that do this efficiently and reliably.

| Type | How Data Is Stored | Best For | Examples |
|------|-------------------|----------|---------|
| **Relational (SQL)** | Tables with rows and columns; strict schema | Structured data; complex queries; transactions | PostgreSQL, MySQL, SQLite |
| **Document (NoSQL)** | JSON-like documents; flexible schema | Semi-structured data; rapid iteration | MongoDB, CouchDB |
| **Key-value** | Simple key → value pairs | Caching; session storage; fast lookups | Redis, DynamoDB |
| **Graph** | Nodes and edges (relationships) | Social networks; recommendation engines | Neo4j, JanusGraph |
| **Time-series** | Optimized for time-stamped data | Monitoring; analytics; IoT | InfluxDB, TimescaleDB |

**SQL** (Structured Query Language) is the standard language for relational databases. It is one of the most valuable technical skills you can learn — almost every organization uses databases, and SQL is how you talk to them.

---

## Operating Systems

The operating system (OS) is the software layer between you (and your programs) and the hardware. It manages memory, processes, files, and devices.

| OS | Where It Dominates | Key Feature |
|----|-------------------|-------------|
| **Windows** | Desktop/laptop PCs (~72% market share) | Broadest software/hardware compatibility |
| **macOS** | Creative professionals, developers | Unix-based; polished UI; Apple ecosystem |
| **Linux** | Servers (~96%), supercomputers (100%), embedded, developers | Open source; free; extremely customizable |
| **Android** | Mobile (~72% global market share) | Based on Linux kernel; open source |
| **iOS** | Mobile (~27% global, but higher revenue) | Closed ecosystem; polished; privacy-focused |

Linux deserves special mention: it powers most of the internet, every top-500 supercomputer, most cloud infrastructure, and all Android phones. It is free, open source, and maintained by a global community.

---

## Cloud Computing

Cloud computing means renting computing resources (servers, storage, databases, etc.) over the internet instead of buying and maintaining your own hardware. For a comprehensive guide to cloud architecture, service models, and provider comparisons, see [cloud architecture](../01_coding_and_technology/cloud_architecture.md).

| Service Model | What You Get | Analogy | Examples |
|---------------|-------------|---------|---------|
| **IaaS** (Infrastructure) | Virtual servers, storage, networking | Renting a plot of land and building what you want | AWS EC2, Google Compute Engine |
| **PaaS** (Platform) | Runtime environment; you bring code | Renting a furnished apartment | Heroku, Google App Engine |
| **SaaS** (Software) | Complete application; you just use it | Staying at a hotel | Gmail, Slack, Salesforce |

The three major cloud providers are **AWS** (Amazon, ~32% market share), **Azure** (Microsoft, ~23%), and **GCP** (Google, ~10%). They offer hundreds of services covering compute, storage, databases, AI, networking, and more.

---

## Cybersecurity — Protecting Digital Systems

Cybersecurity is the practice of defending computers, networks, and data from attack. It matters because everything is connected, and the cost of breaches is enormous. For a full guide covering OWASP Top 10, secure development lifecycle, and secrets management, see.

### Common Threats

| Threat | What It Is | Prevention |
|--------|-----------|------------|
| **Malware** | Malicious software (viruses, worms, trojans) | Antivirus; keep software updated |
| **Phishing** | Fake emails/messages tricking you into revealing information | Training; email filtering; skepticism |
| **Ransomware** | Encrypts your data; demands payment for the key | Backups; patch systems; do not pay |
| **DDoS** | Overwhelms a service with traffic | Traffic filtering; CDN protection |
| **SQL injection** | Inserting malicious SQL into input fields | Parameterized queries; input validation |
| **Man-in-the-middle** | Intercepting communication between two parties | HTTPS/TLS encryption |

### Security Fundamentals

- **Encryption**: Scramble data so only authorized parties can read it. HTTPS uses TLS to encrypt web traffic.
- **Authentication**: Verify identity. Use multi-factor authentication (MFA) — password + something else (code, biometric).
- **Authorization**: Verify permissions. Just because you are logged in does not mean you should access everything.
- **Principle of least privilege**: Give users and systems only the access they need, nothing more.
- **Patch management**: Keep software updated. Most breaches exploit known vulnerabilities that already have patches.

---

## Data Formats

Programs exchange data in specific formats. The most common:

| Format | Structure | Used For |
|--------|-----------|----------|
| **JSON** | Key-value pairs; human-readable | APIs; configuration; data exchange |
| **XML** | Tag-based; verbose but flexible | Legacy systems; documents; SOAP APIs |
| **YAML** | Indentation-based; very readable | Configuration (Docker, Kubernetes, CI/CD) |
| **CSV** | Plain text rows and columns | Data import/export; spreadsheets |

---

## Summary

Computing is engineering, not magic. Computers follow instructions at high speed. The internet connects billions of them using standardized protocols. Software is built by teams of people writing, testing, and deploying code in iterative cycles. Databases store and retrieve data. Cloud computing lets anyone access large-scale computing resources on demand. And cybersecurity is the ongoing effort to protect these systems from exploitation. Understanding these fundamentals helps inform decisions in the digital world — whether as a user, a developer, or an observer of modern technology.
