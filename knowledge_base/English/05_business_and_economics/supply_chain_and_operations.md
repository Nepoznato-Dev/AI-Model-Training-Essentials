---
# Metadata
title: "Supply Chain and Operations Management"
description: "Inventory management, lean manufacturing, logistics, bullwhip effect"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [supply, chain, operations, business-and-economics]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Supply Chain and Operations Management

Supply chain management is the coordination of all activities involved in sourcing, procurement, conversion, and logistics — from raw materials to the finished product in the customer's hands. Operations management is the day-to-day running of production systems. Together, they determine whether a company can deliver the right product, at the right time, at the right cost, with the right quality. The pandemic, chip shortages, and canal blockages have shown just how fragile and globally interconnected supply chains are.

---

## Supply Chain Fundamentals

### The Supply Chain Flow

| Stage | Activity | Key Concern |
|-------|----------|-------------|
| **Plan** | Demand forecasting; supply planning; S&OP | Accuracy; responsiveness |
| **Source** | Supplier selection; procurement; contracting | Cost; quality; reliability; ethics |
| **Make** | Production; assembly; quality control | Efficiency; flexibility; capacity |
| **Deliver** | Warehousing; order fulfilment; transportation | Speed; cost; accuracy |
| **Return** | Reverse logistics; returns; recycling | Customer satisfaction; cost recovery |

### Types of Supply Chains

| Type | Characteristics | Best For |
|------|----------------|----------|
| **Efficient** | High utilisation; low cost; predictable | Functional products with stable demand (groceries) |
| **Responsive** | Buffer capacity; flexible; fast | Innovative products with uncertain demand (fashion) |
| **Resilient** | Redundancy; visibility; adaptability | High-risk environments; critical goods |
| **Agile** | Postponement; mass customisation | Products with high variety and short life cycles |
| **Lean** | Eliminate waste; pull-based; just-in-time | High-volume; low-variety; stable demand |

---

## Inventory Management

### Inventory Types

| Type | Description | Purpose |
|------|-------------|---------|
| **Raw materials** | Unprocessed inputs | Buffer against supply variability |
| **Work-in-progress (WIP)** | Partially finished goods | Buffer between production stages |
| **Finished goods** | Ready to sell | Buffer against demand variability |
| **MRO** (Maintenance, Repair, Operations) | Supplies needed for operations | Keep production running |
| **Safety stock** | Extra inventory above expected demand | Protect against uncertainty |
| **Pipeline inventory** | In transit between locations | Unavoidable during transportation |

### Inventory Management Models

| Model | Description | When to Use |
|-------|-------------|-------------|
| **EOQ** (Economic Order Quantity) | Optimal order size that minimises total holding + ordering costs | Stable demand; constant lead time |
| **Reorder point (ROP)** | Order when inventory drops to a threshold | Continuous review; predictable demand |
| **ABC analysis** | Classify items by value: A (high), B (medium), C (low) | Prioritise management attention |
| **Just-in-Time (JIT)** | Receive goods only as needed in production | Stable supply chain; low variability |
| **Vendor-managed inventory (VMI)** | Supplier manages inventory levels | Strong supplier relationships |
| **Consignment** | Supplier owns inventory until used | Reduce buyer's carrying costs |

---

## Production Systems

### Manufacturing Approaches

| Approach | Description | Volume | Variety | Example |
|----------|-------------|--------|---------|---------|
| **Job shop** | Custom products; general-purpose equipment | Low | High | Machine shop; custom furniture |
| **Batch** | Produce in lots; changeover between batches | Medium | Medium | Bakeries; pharmaceuticals |
| **Mass production** | High-volume; dedicated equipment; assembly lines | High | Low | Automobiles; electronics |
| **Continuous flow** | Non-stop production; fully automated | Very high | Very low | Oil refining; chemicals; steel |
| **Mass customisation** | High volume + high variety; flexible automation | High | High | Dell computers; Nike By You |

### Lean Manufacturing

| Principle | Description |
|-----------|-------------|
| **Value** | Define what the customer considers valuable |
| **Value stream** | Map all steps; identify those that add value |
| **Flow** | Make value-creating steps flow smoothly without interruptions |
| **Pull** | Produce only when the customer requests it |
| **Perfection** | Continuously eliminate waste (muda) |

### The Seven Wastes (Muda)

| Waste | Description | Example |
|-------|-------------|---------|
| **Overproduction** | Making more than needed | Producing to forecast when demand is uncertain |
| **Waiting** | Idle time between steps | Parts waiting for the next machine |
| **Transportation** | Unnecessary movement of materials | Moving products between distant warehouses |
| **Over-processing** | Doing more work than necessary | Extra inspections; unnecessary features |
| **Inventory** | Excess stock beyond what's needed | Safety stock "just in case" |
| **Motion** | Unnecessary movement of people | Walking to fetch tools; reaching for parts |
| **Defects** | Products that don't meet specifications | Rework; scrap; warranty claims |

---

## Logistics and Transportation

### Transportation Modes

| Mode | Cost | Speed | Capacity | Best For |
|------|------|-------|----------|----------|
| **Road** (truck) | Medium | Medium | Medium | Last-mile; regional; flexible routing |
| **Rail** | Low | Medium | High | Bulk commodities; long-distance over land |
| **Maritime** (ship) | Very low | Very slow | Very high | International; bulk; containers |
| **Air** | Very high | Very fast | Low | High-value; urgent; perishable |
| **Pipeline** | Low (after construction) | Continuous | High | Oil; gas; water |
| **Intermodal** | Varies | Varies | High | Combining modes; containerised freight |

### Warehouse Design

| Decision | Options | Trade-Off |
|----------|---------|-----------|
| **Number of warehouses** | Few (centralised) vs many (regional) | Cost efficiency vs delivery speed |
| **Automation level** | Manual vs semi-automated vs fully automated | Capital cost vs labour cost and accuracy |
| **Layout** | U-flow vs through-flow | Space utilisation vs travel distance |
| **Storage system** | Shelving; racking; AS/RS; carousel | Density vs accessibility vs cost |

---

## Supply Chain Risk Management

### Common Risks

| Risk Category | Examples | Mitigation |
|--------------|----------|------------|
| **Demand risk** | Forecast errors; bullwhip effect | Better forecasting; demand sensing; safety stock |
| **Supply risk** | Supplier bankruptcy; quality failures | Dual sourcing; supplier audits; safety stock |
| **Logistics risk** | Port congestion; carrier failures | Multi-modal; alternative routes |
| **Geopolitical risk** | Tariffs; trade wars; sanctions | Nearshoring; diversifying sourcing countries |
| **Natural disaster** | Earthquake; flood; pandemic | Geographic diversification; business continuity plans |
| **Cyber risk** | Ransomware; data breach | IT security; backup systems |

### The Bullwhip Effect

| Cause | Description | Solution |
|-------|-------------|----------|
| **Demand forecast updating** | Each stage adds its own safety stock | Share point-of-sale data across the chain |
| **Order batching** | Periodic ordering creates demand spikes | Reduce order cycle times; EDI |
| **Price fluctuations** | Forward buying during promotions | Everyday low pricing; stable pricing |
| **Rationing and shortage gaming** | Over-ordering during shortages | Allocate based on past sales; share capacity info |

---

## Modern Supply Chain Trends

| Trend | Description | Impact |
|-------|-------------|--------|
| **Digital twins** | Virtual replica of the supply chain for simulation | Better planning; scenario analysis |
| **Supply chain control towers** | Centralised visibility across the entire chain | Faster response to disruptions |
| **Nearshoring / friendshoring** | Moving production closer to home or to allied countries | Reduced risk; higher cost |
| **Circular supply chains** | Design for reuse, remanufacturing, recycling | Sustainability; resource efficiency |
| **AI-driven demand sensing** | Machine learning on real-time data for short-term forecasts | More accurate; faster response |
| **Autonomous vehicles and drones** | Self-driving trucks; drone delivery | Lower cost; faster last-mile |

---

## Summary

Supply chain and operations management is about making the physical flow of goods efficient, responsive, and resilient. Inventory management balances the cost of holding stock against the risk of stockouts. Production systems range from job shops (custom, low volume) to continuous flow (commodity, high volume). Lean manufacturing eliminates waste to improve efficiency. Logistics decisions — transportation mode, warehouse location, automation level — determine cost and service quality. Risk management addresses the bullwhip effect, supplier failures, geopolitical disruptions, and natural disasters. Modern trends like digital twins, AI-driven demand sensing, and nearshoring reflect the industry's response to an increasingly volatile world. The best supply chains are not just efficient — they're visible, flexible, and prepared for disruption.
