<!--
---
# Metadata
title: "Genetics and Genomics"
description: "DNA, gene expression, CRISPR, GWAS, sequencing technologies"
category: "Natural Sciences"
subcategory: "Life Sciences"
version: "1.0.1"
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
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to life_sciences/ subfolder; added subcategory field"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [genetics, genomics, natural-sciences]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "6 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Genetics and Genomics

Genetics is the study of heredity — how traits are passed from parents to offspring through DNA. Genomics is the study of entire genomes: all the genes, the non-coding regions, how they interact, and how they vary across individuals and populations. The transition from genetics to genomics was driven by sequencing technology — we went from studying one gene at a time to reading entire genomes in hours, generating data that is transforming medicine, agriculture, forensics, and our understanding of evolution.

---

## DNA Fundamentals

### DNA Structure

| Component | Description |
|-----------|-------------|
| **Nucleotide** | Building block of DNA; consists of a sugar (deoxyribose), a phosphate group, and a nitrogenous base |
| **Bases** | Adenine (A), Thymine (T), Guanine (G), Cytosine (C) |
| **Base pairing** | A pairs with T (2 hydrogen bonds); G pairs with C (3 hydrogen bonds) |
| **Double helix** | Two strands running anti-parallel (5' to 3' and 3' to 5'); twisted into a helix |
| **Chromosome** | A single, long DNA molecule wrapped around histone proteins; humans have 46 (23 pairs) |
| **Genome** | The complete set of DNA in an organism; human genome is ~3.2 billion base pairs |

### Central Dogma of Molecular Biology

| Step | Process | Location | Product |
|------|---------|----------|---------|
| **Replication** | DNA → DNA | Nucleus | Two identical DNA molecules |
| **Transcription** | DNA → mRNA | Nucleus | Messenger RNA |
| **Translation** | mRNA → protein | Ribosome (cytoplasm) | Polypeptide chain (protein) |

---

## Gene Expression

### How Genes Are Regulated

| Level | Mechanism | Example |
|-------|-----------|---------|
| **Epigenetic** | DNA methylation; histone modification; chromatin remodelling | Silencing of one X chromosome in females |
| **Transcriptional** | Transcription factors bind promoters/enhancers; activate or repress | Lac operon in bacteria; hormone-responsive genes |
| **Post-transcriptional** | Alternative splicing; mRNA stability; microRNAs | One gene → multiple protein variants |
| **Translational** | Ribosome availability; initiation factor regulation | Iron regulation via ferritin mRNA |
| **Post-translational** | Protein modification (phosphorylation, ubiquitination); degradation | Cell cycle control |

---

## Inheritance Patterns

### Mendelian Genetics

| Pattern | Description | Example |
|---------|-------------|---------|
| **Autosomal dominant** | One copy of the allele is sufficient | Huntington's disease; achondroplasia |
| **Autosomal recessive** | Two copies required | Cystic fibrosis; sickle cell anaemia |
| **X-linked dominant** | Gene on X chromosome; one copy sufficient | Rett syndrome |
| **X-linked recessive** | Gene on X chromosome; males more affected | Haemophilia; colour blindness |
| **Codominance** | Both alleles expressed equally | ABO blood groups (A and B) |
| **Incomplete dominance** | Heterozygote is intermediate | Pink flowers from red and white parents |
| **Polygenic** | Multiple genes contribute to one trait | Height; skin colour; intelligence |
| **Pleiotropy** | One gene affects multiple traits | Marfan syndrome (connective tissue, eyes, heart) |

---

## Genomics

### Types of Genomics

| Type | Focus | Application |
|------|-------|-------------|
| **Structural genomics** | 3D structure of all proteins in a genome | Drug design; protein engineering |
| **Functional genomics** | What genes do; gene interactions; expression patterns | Understanding disease mechanisms |
| **Comparative genomics** | Comparing genomes across species | Evolutionary relationships; identifying conserved regions |
| **Metagenomics** | DNA from environmental samples (not cultured) | Microbiome studies; discovering new organisms |
| **Pharmacogenomics** | How genes affect drug response | Personalised medicine; drug dosing |
| **Epigenomics** | Genome-wide epigenetic modifications | Cancer diagnosis; developmental biology |

### DNA Sequencing Technologies

| Generation | Technology | Read Length | Throughput | Key Feature |
|-----------|-----------|-------------|------------|-------------|
| **First generation** | Sanger sequencing | ~1,000 bp | Low | Gold standard accuracy; used for validation |
| **Second generation** | Illumina (Solexa) | 50–300 bp | Very high | Short reads; dominant platform; low cost per base |
| **Second generation** | Ion Torrent | 200–400 bp | High | Semiconductor-based; no optics |
| **Third generation** | PacBio (SMRT) | 10,000–100,000 bp | Moderate | Long reads; resolves repetitive regions |
| **Third generation** | Oxford Nanopore | Up to millions of bp | Moderate to high | Ultra-long reads; portable (MinION); real-time |

---

## Genetic Variation

### Types of Variation

| Type | Description | Frequency |
|------|-------------|-----------|
| **SNP** (Single Nucleotide Polymorphism) | Single base change | Most common; ~1 in 1,000 bases |
| **Insertion / Deletion (indel)** | Addition or removal of bases | Can cause frameshift mutations |
| **CNV** (Copy Number Variation) | Duplicated or deleted segments (1 kb – several Mb) | Contributes to disease and evolution |
| **Structural variation** | Inversions; translocations; large rearrangements | Less common; can be pathogenic |
| **Microsatellite (STR)** | Short tandem repeats (2–6 bp repeated) | Forensics; paternity testing |

### GWAS (Genome-Wide Association Studies)

| Step | Description |
|------|-------------|
| **1. Collect samples** | Cases (with disease) and controls (without) |
| **2. Genotype** | Use SNP arrays to genotype hundreds of thousands of variants |
| **3. Statistical test** | Test each SNP for association with the trait |
| **4. Manhattan plot** | Visualise results across all chromosomes |
| **5. Replication** | Confirm findings in independent samples |

---

## Gene Editing

### CRISPR-Cas9

| Component | Function |
|-----------|----------|
| **Guide RNA (gRNA)** | ~20 nucleotides; matches target DNA sequence |
| **Cas9 protein** | Molecular scissors; cuts DNA at the target site |
| **PAM sequence** | Short motif (NGG) next to target; required for Cas9 binding |
| **HDR** (Homology-Directed Repair) | Precise editing using a donor template |
| **NHEJ** (Non-Homologous End Joining) | Error-prone repair; creates insertions/deletions (knockout) |

### Gene Editing Applications

| Application | Description |
|-------------|-------------|
| **Therapeutic** | Correct disease-causing mutations (sickle cell; beta-thalassaemia) |
| **Agriculture** | Disease-resistant crops; improved livestock |
| **Research** | Create knockout models; study gene function |
| **Gene drive** | Spread a genetic modification through a population (e.g., malaria-resistant mosquitoes) |

---

## Ethical Considerations

| Issue | Concern |
|-------|---------|
| **Genetic privacy** | Who owns your genome data? Can employers or insurers use it? |
| **Gene editing in embryos** | Heritable changes; designer babies; unintended off-target effects |
| **Genetic discrimination** | GINA (US) protects against some discrimination but has gaps |
| **Informed consent** | Genomic data reveals information about relatives who haven't consented |
| **Data storage** | Genomes are large (~200 GB raw); long-term storage and security challenges |
| **Equity** | Genomic medicine risks widening health disparities if only available to wealthy populations |

---

## Summary

Genetics studies how individual genes work and are inherited. Genomics studies entire genomes — all genes, their interactions, and their variation. DNA is transcribed into RNA, which is translated into proteins. Gene expression is regulated at multiple levels: epigenetic, transcriptional, post-transcriptional, translational, and post-translational. Inheritance follows patterns (dominant, recessive, polygenic) that determine how traits pass between generations. Modern sequencing technologies (Illumina, PacBio, Nanopore) can read entire genomes quickly and cheaply. CRISPR-Cas9 enables precise gene editing with transformative potential in medicine and agriculture. The biggest challenges are ethical: who controls genomic data, how to regulate gene editing in embryos, and how to ensure genomic medicine benefits everyone, not just the privileged.
