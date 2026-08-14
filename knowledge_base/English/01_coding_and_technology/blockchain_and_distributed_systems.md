---
# Metadata
title: "Blockchain and Distributed Systems"
description: "Consensus, smart contracts, DeFi, Byzantine fault tolerance"
category: "Coding and Technology"
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
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [blockchain, distributed, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Blockchain and Distributed Systems

Blockchain is a specific type of distributed system — a decentralised, append-only ledger where records (blocks) are linked by cryptographic hashes. Distributed systems is the broader field of making multiple computers work together as one. Both concepts are important for understanding modern infrastructure, from cryptocurrency to distributed databases to consensus algorithms that power global services.

---

## Distributed Systems Fundamentals

### Why Distributed Systems?

| Motivation | Description |
|-----------|-------------|
| **Scalability** | Add more machines to handle more load |
| **Fault tolerance** | System continues working even if some machines fail |
| **Geographic distribution** | Serve users from nearby data centres |
| **Specialisation** | Different machines handle different tasks |

### Key Concepts

| Concept | Description | Challenge |
|---------|-------------|-----------|
| **Consensus** | Getting all nodes to agree on a value | Network partitions; Byzantine faults |
| **Replication** | Copying data across multiple nodes | Consistency vs availability |
| **Partitioning (sharding)** | Splitting data across nodes | Hot spots; cross-shard queries |
| **Consistency models** | Guarantees about what different readers see | Strong consistency is slow; eventual consistency can surprise users |
| **CAP theorem** | You can only have 2 of: Consistency, Availability, Partition tolerance | In practice, partition tolerance is required; choose C or A |

### The CAP Theorem

| Choice | What You Get | What You Give Up | Example |
|--------|-------------|-----------------|---------|
| **CP** | Consistent + partition-tolerant | Some nodes may be unavailable during partitions | HBase, MongoDB, Redis |
| **AP** | Available + partition-tolerant | Reads may return stale data | Cassandra, DynamoDB, CouchDB |
| **CA** | Consistent + available | Can't tolerate network partitions | Single-node databases (not truly distributed) |

---

## Consensus Algorithms

How do distributed nodes agree on the state of the system?

| Algorithm | Type | Fault Tolerance | Used In |
|-----------|------|----------------|---------|
| **Paxos** | Crash fault tolerant | Up to f failures with 2f+1 nodes | Google Chubby; foundational theory |
| **Raft** | Crash fault tolerant | Up to f failures with 2f+1 nodes | etcd, Consul, TiKV |
| **PBFT** | Byzantine fault tolerant | Up to f failures with 3f+1 nodes | Hyperledger Fabric |
| **Proof of Work** | Byzantine fault tolerant | Depends on hash power | Bitcoin |
| **Proof of Stake** | Byzantine fault tolerant | Depends on stake | Ethereum 2.0, Cardano |

### Raft (Simplified)

| Role | Responsibility |
|------|---------------|
| **Leader** | Handles all client requests; sends log entries to followers |
| **Follower** | Responds to leader's requests; votes in elections |
| **Candidate** | Requests votes to become leader |

1. All nodes start as followers
2. If a follower doesn't hear from the leader for an election timeout, it becomes a candidate
3. Candidates request votes; the one with the most votes becomes leader
4. The leader replicates log entries to followers
5. When a majority confirms, the entry is committed

---

## Blockchain

### How a Blockchain Works

| Component | Description |
|-----------|-------------|
| **Block** | A batch of transactions + metadata + hash of the previous block |
| **Hash** | Cryptographic fingerprint of the block's contents |
| **Chain** | Each block references the previous block's hash, creating an immutable chain |
| **Consensus** | Network participants agree on which blocks to add |
| **Merkle tree** | Tree of hashes summarising all transactions in a block |

### Why Blockchain Is Hard to Tamper With

1. Each block contains the hash of the previous block
2. Changing any transaction changes the block's hash
3. Changed hash breaks the chain — all subsequent blocks become invalid
4. An attacker would need to re-mine all subsequent blocks AND control >50% of the network

### Types of Blockchains

| Type | Access | Validator | Example |
|------|--------|-----------|---------|
| **Public (permissionless)** | Anyone can read and write | Open consensus (PoW, PoS) | Bitcoin, Ethereum |
| **Private (permissioned)** | Restricted access | Known validators | Hyperledger, Corda |
| **Consortium** | Governed by a group of organisations | Selected validators | R3 Corda for banking |

### Smart Contracts

Self-executing code stored on the blockchain that runs when predetermined conditions are met.

| Platform | Language | Notable Feature |
|----------|----------|-----------------|
| **Ethereum** | Solidity, Vyper | Largest smart contract ecosystem |
| **Solana** | Rust, C | High throughput; low fees |
| **Cardano** | Haskell (Plutus) | Peer-reviewed; formal verification |
| **Hyperledger** | Go, Java, JavaScript | Enterprise; permissioned |

---

## Cryptocurrency

| Currency | Consensus | Supply | Primary Use |
|----------|-----------|--------|-------------|
| **Bitcoin** | Proof of Work | 21 million (capped) | Store of value; digital gold |
| **Ethereum** | Proof of Stake | No hard cap | Smart contracts; DeFi; NFTs |
| **Solana** | Proof of Stake + Proof of History | No hard cap | High-speed transactions |
| **Cardano** | Proof of Stake (Ouroboros) | 45 billion (capped) | Academic approach; sustainability |

---

## Distributed Databases

| Database | Architecture | Consistency | Best For |
|----------|-------------|-------------|----------|
| **Cassandra** | Wide-column; peer-to-peer | Tunable (eventual to quorum) | High write throughput; time-series |
| **MongoDB** | Document; replica sets | Eventual (with causal consistency option) | Flexible schema; rapid development |
| **CockroachDB** | Distributed SQL; Raft consensus | Strong | Distributed SQL; global deployment |
| **TiDB** | Distributed SQL; Raft (via TiKV) | Strong | MySQL-compatible; horizontal scaling |
| **DynamoDB** | Key-value; managed | Eventual (or strong with consistent reads) | Serverless; AWS-integrated |
| **Spanner** | Distributed SQL; Paxos | Strong | Google Cloud; global consistency |

---

## Distributed System Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Leader election** | Choose one node to coordinate | Raft leader; ZooKeeper |
| **Replication** | Copy data for redundancy and read scaling | Database replicas; CDN |
| **Sharding** | Partition data by key range or hash | Large-scale databases |
| **MapReduce** | Split computation across nodes; aggregate results | Large data processing |
| **Gossip protocol** | Nodes periodically share state with random peers | Cluster membership; failure detection |
| **Two-phase commit** | Coordinate transactions across multiple nodes | Distributed databases |
| **Saga pattern** | Series of local transactions with compensating actions | Microservice transactions |
| **Circuit breaker** | Stop calling a failing service; fail fast | Resilience; prevent cascading failures |

---

## Challenges in Distributed Systems

| Challenge | Description | Mitigation |
|-----------|-------------|------------|
| **Network partitions** | Nodes can't communicate | CAP trade-off; retry with backoff |
| **Clock skew** | Different nodes have different clocks | Use logical clocks; NTP; avoid relying on wall-clock time |
| **Byzantine faults** | Nodes that lie or behave arbitrarily | BFT consensus; blockchain |
| **Split brain** | Two nodes both think they're the leader | Fencing; quorum-based decisions |
| **Cascading failures** | One failure triggers others | Circuit breakers; bulkheads; graceful degradation |
| **Data consistency** | Keeping replicas in sync | Consistency models; conflict resolution |

---

## Summary

Distributed systems are how modern software scales, survives failures, and serves users globally. Consensus algorithms (Raft, Paxos) ensure nodes agree. Blockchains add cryptographic verification and decentralisation to create trustless ledgers. Distributed databases (Cassandra, CockroachDB, DynamoDB) handle data at scale. The fundamental trade-off — captured by the CAP theorem — is between consistency and availability when the network is unreliable. Understanding these concepts is essential for building systems that work at internet scale.
