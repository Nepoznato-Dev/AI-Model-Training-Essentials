---
# Metadata
title: "Materials Science"
description: "Crystal structures, polymers, alloys, semiconductors, nanomaterials"
category: "Natural Sciences"
subcategory: "Physical Sciences"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to physical_sciences/ subfolder; added subcategory field"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [materials, science, natural-sciences]
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

# Materials Science

Materials science is the study of how the structure of a material (at atomic, microscopic, and macroscopic scales) determines its properties, and how processing methods can be used to control that structure to achieve desired performance. It's the field that answers questions like: why is steel strong but heavy? Why is glass transparent but brittle? How can we make batteries that charge faster? What materials will survive the conditions on Mars? Every piece of technology you've ever used is made of materials, and advances in technology almost always require advances in materials.

---

## The Materials Science Tetrahedron

The four interconnected elements that define the field:

| Element | Description |
|---------|-------------|
| **Structure** | How atoms and molecules are arranged (crystal structure; grain boundaries; defects) |
| **Properties** | How the material behaves (mechanical; electrical; thermal; optical; magnetic) |
| **Processing** | How the material is made and shaped (casting; sintering; doping; annealing) |
| **Performance** | How the material functions in a real application |

The key insight: changing the processing changes the structure, which changes the properties, which changes the performance.

---

## Classes of Materials

### Overview

| Class | Bonding | Key Properties | Examples |
|-------|---------|---------------|---------|
| **Metals** | Metallic (delocalised electrons) | Strong; ductile; conductive; opaque | Steel; aluminium; copper; titanium |
| **Ceramics** | Ionic / covalent | Hard; brittle; heat-resistant; insulating | Alumina; silicon carbide; glass; porcelain |
| **Polymers** | Covalent (chains) + van der Waals | Lightweight; flexible; insulating; low melting point | Polyethylene; nylon; rubber; epoxy |
| **Composites** | Combination of two or more classes | Tailored properties; high strength-to-weight | Carbon fibre; fibreglass; concrete |
| **Semiconductors** | Covalent (with controlled impurities) | Tunable conductivity; basis of electronics | Silicon; germanium; gallium arsenide |
| **Biomaterials** | Various; biocompatible required | Interact with biological systems | Titanium implants; collagen; hydroxyapatite |

---

## Crystal Structures

### Common Metallic Crystal Structures

| Structure | Atoms per Unit Cell | Packing Fraction | Examples |
|-----------|-------------------|-----------------|---------|
| **FCC** (Face-Centred Cubic) | 4 | 0.74 (closest packed) | Aluminium; copper; gold; nickel; austenite (γ-iron) |
| **BCC** (Body-Centred Cubic) | 2 | 0.68 | Iron (α-iron); chromium; tungsten; molybdenum |
| **HCP** (Hexagonal Close-Packed) | 6 | 0.74 (closest packed) | Titanium; zinc; magnesium; cobalt |

### Why Crystal Structure Matters

| Property | Influence of Crystal Structure |
|----------|-------------------------------|
| **Strength** | Slip systems (planes along which atoms slide) differ by structure; FCC metals are more ductile than HCP |
| **Density** | Packing fraction determines how tightly atoms are packed |
| **Phase transformations** | Iron transforms from BCC to FCC at 912°C — this is the basis of steel heat treatment |
| **Anisotropy** | Properties can vary with direction in non-cubic crystals |

---

## Mechanical Properties

### Key Metrics

| Property | Definition | Units | Typical Values |
|----------|-----------|-------|----------------|
| **Young's modulus (E)** | Stiffness; stress / strain in elastic region | GPa | Steel: 200; Aluminium: 70; Rubber: 0.01–0.1 |
| **Yield strength** | Stress at which permanent (plastic) deformation begins | MPa | Steel: 250–1000; Aluminium: 40–500 |
| **Tensile strength (UTS)** | Maximum stress before failure | MPa | Steel: 400–2000; Aluminium: 90–600 |
| **Ductility (% elongation)** | How much a material stretches before breaking | % | Steel: 10–50; Glass: <1 |
| **Toughness** | Energy absorbed before fracture (area under stress-strain curve) | MJ/m³ | Steel: high; ceramics: low |
| **Hardness** | Resistance to surface indentation | Various scales | Diamond: hardest; talc: softest |

### Strengthening Mechanisms

| Mechanism | How It Works | Example |
|-----------|-------------|---------|
| **Grain refinement** | Smaller grains = more grain boundaries = harder for dislocations to move | Hall-Petch relationship |
| **Solid solution strengthening** | Foreign atoms distort the lattice; impede dislocation motion | Adding zinc to copper → brass |
| **Precipitation hardening** | Small particles block dislocation movement | Age-hardened aluminium alloys |
| **Work hardening (strain hardening)** | Plastic deformation increases dislocation density; they tangle and impede each other | Cold-rolling steel |
| **Composite strengthening** | Strong fibres in a softer matrix carry the load | Carbon fibre reinforced polymer |

---

## Electrical and Thermal Properties

### Electrical Conductivity

| Material Type | Conductivity (S/m) | Mechanism |
|--------------|--------------------|-----------|
| **Conductors** (copper, silver) | 10^7 – 10^8 | Free electrons in metallic bonds |
| **Semiconductors** (silicon, GaAs) | 10^-6 – 10^4 | Tunable by doping; band gap engineering |
| **Insulators** (glass, rubber) | 10^-12 – 10^-20 | Large band gap; electrons bound |
| **Superconductors** | Infinite (below critical temperature) | Zero electrical resistance; Meissner effect |

### Thermal Properties

| Property | Description | Important For |
|----------|-------------|---------------|
| **Thermal conductivity** | How well heat flows through the material | Heat sinks; insulation |
| **Thermal expansion** | How much a material expands when heated | Matching materials in composites; bridges; rails |
| **Specific heat capacity** | Energy needed to raise temperature by 1°C | Thermal energy storage |
| **Melting point** | Temperature at which solid becomes liquid | High-temperature applications |

---

## Polymers

### Types of Polymers

| Type | Structure | Properties | Examples |
|------|-----------|-----------|---------|
| **Thermoplastics** | Linear or branched chains; weak intermolecular forces | Melt when heated; recyclable | Polyethylene; polystyrene; nylon |
| **Thermosets** | Cross-linked network; covalent bonds between chains | Don't melt; decompose at high temperature | Epoxy; vulcanised rubber; Bakelite |
| **Elastomers** | Lightly cross-linked; coiled chains | Stretch and return to shape | Natural rubber; silicone; neoprene |

### Polymer Properties

| Property | Description |
|----------|-------------|
| **Glass transition temperature (Tg)** | Below Tg: hard and brittle. Above Tg: soft and flexible |
| **Crystallinity** | Semi-crystalline polymers are stronger and more opaque; amorphous are transparent |
| **Molecular weight** | Higher MW = stronger; harder to process |
| **Degree of polymerisation** | Number of monomer units; affects properties |

---

## Phase Diagrams

### Iron-Carbon Phase Diagram (Simplified)

| Phase | Carbon Content | Structure | Properties |
|-------|---------------|-----------|-----------|
| **Ferrite (α)** | Up to 0.022% | BCC iron | Soft; ductile; magnetic |
| **Austenite (γ)** | Up to 2.14% | FCC iron | Non-magnetic; formable |
| **Cementite (Fe₃C)** | 6.67% | Orthorhombic | Hard; brittle |
| **Pearlite** | 0.76% (eutectoid) | Alternating layers of ferrite and cementite | Strong; tough |
| **Martensite** | Any (formed by rapid quenching) | BCT (body-centred tetragonal) | Very hard; brittle |

---

## Modern and Emerging Materials

| Material | Description | Application |
|----------|-------------|-------------|
| **Graphene** | Single layer of carbon atoms; strongest material known; excellent conductor | Electronics; composites; sensors |
| **Carbon nanotubes** | Rolled-up graphene cylinders; extreme strength-to-weight ratio | Composites; electronics; energy storage |
| **Perovskites** | Crystal structure ABX₃; tunable band gap | Solar cells; LEDs; detectors |
| **Metal-organic frameworks (MOFs)** | Porous crystalline materials; enormous surface area | Gas storage; catalysis; drug delivery |
| **Shape-memory alloys** | Return to original shape when heated | Stents; actuators; self-repairing structures |
| **Metamaterials** | Engineered microstructure gives properties not found in nature | Negative refractive index; cloaking |
| **High-entropy alloys** | Multiple principal elements; unusual combinations of properties | Extreme environments; aerospace |

---

## Summary

Materials science connects the atomic structure of a material to its macroscopic properties and real-world performance. Metals are strong and conductive but heavy. Ceramics are hard and heat-resistant but brittle. Polymers are lightweight and flexible but limited by temperature. Composites combine the best of different classes. Crystal structure determines mechanical behaviour. Processing — heat treatment, alloying, work hardening — controls the microstructure and therefore the properties. Modern materials like graphene, perovskites, and MOFs push the boundaries of what's possible. The field is fundamentally interdisciplinary: physics explains bonding, chemistry explains reactions, engineering explains performance, and all of it matters for every technology from smartphones to spacecraft.
