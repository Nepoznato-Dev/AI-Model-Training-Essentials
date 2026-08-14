---
# Metadata
title: "Genetics and Genomics"
description: "DNA, gene expression, CRISPR, GWAS, sequencing technologies"
category: "Natural Sciences"
subcategory: "Life Sciences"
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
# Genetics at Genomics
Ang genetika ay ang pag-aaral ng pagmamana — kung paano naipapasa ang mga katangian mula sa mga magulang patungo sa mga supling sa pamamagitan ng DNA. Ang genomics ay ang pag-aaral ng buong genome: lahat ng gene, ang mga non-coding na rehiyon, kung paano sila nakikipag-ugnayan, at kung paano sila nag-iiba-iba sa mga indibidwal at populasyon. Ang paglipat mula sa genetics patungo sa genomics ay hinimok ng sequencing technology — nagpunta kami mula sa pag-aaral ng isang gene sa isang pagkakataon sa pagbabasa ng buong genome sa mga oras, pagbuo ng data na nagbabago ng medisina, agrikultura, forensics, at ang aming pag-unawa sa ebolusyon.
---

## Mga Pangunahing Kaalaman sa DNA
### Istraktura ng DNA
| Bahagi | Paglalarawan |
|-----------|-------------|
| **Nucleotide** | Building block ng DNA; binubuo ng isang asukal (deoxyribose), isang phosphate group, at isang nitrogenous base |
| **Base** | Adenine (A), Thymine (T), Guanine (G), Cytosine (C) |
| **Base na pagpapares** | Isang pares na may T (2 hydrogen bond); G pares na may C (3 hydrogen bonds) |
| **Double helix** | Dalawang hibla na nagpapatakbo ng anti-parallel (5' hanggang 3' at 3' hanggang 5'); baluktot sa isang helix |
| **Chromosome** | Isang solong, mahabang molekula ng DNA na nakabalot sa mga protina ng histone; ang mga tao ay may 46 (23 pares) |
| **Genome** | Ang kumpletong hanay ng DNA sa isang organismo; ang genome ng tao ay ~3.2 bilyong base pairs |
### Central Dogma ng Molecular Biology
| Hakbang | Proseso | Lokasyon | Produkto |
|------|---------|----------|---------|
| **Replikasyon** | DNA → DNA | Nucleus | Dalawang magkaparehong molekula ng DNA |
| **Transkripsyon** | DNA → mRNA | Nucleus | Messenger RNA |
| **Pagsasalin** | mRNA → protina | Ribosome (cytoplasm) | Polypeptide chain (protina) |
---

## Gene Expression
### Paano Kinokontrol ang Mga Gene
| Antas | Mekanismo | Halimbawa |
|-------|-----------|---------|
| **Epigenetic** | DNA methylation; pagbabago ng histone; chromatin remodeling | Pagpapatahimik ng isang X chromosome sa mga babae |
| **Transkripsyon** | Ang mga salik ng transkripsyon ay nagbubuklod sa mga promotor/enhancer; buhayin o pigilan | Lac operon sa bakterya; mga gene na tumutugon sa hormone |
| **Post-transcriptional** | Alternatibong splicing; katatagan ng mRNA; mga microRNA | Isang gene → maraming variant ng protina |
| **Translational** | pagkakaroon ng ribosome; regulasyon sa kadahilanan ng pagsisimula | Regulasyon ng bakal sa pamamagitan ng ferritin mRNA |
| **Pagkatapos ng pagsasalin** | Pagbabago ng protina (phosphorylation, ubiquitination); pagkasira | Kontrol ng cell cycle |
---

## Mga Pattern ng Pamana
### Mendelian Genetics
| Pattern | Paglalarawan | Halimbawa |
|---------|-------------|---------|
| **Autosomal dominant** | Ang isang kopya ng allele ay sapat na | Huntington's disease; achondroplasia |
| **Autosomal recessive** | Dalawang kopya ang kailangan | Cystic fibrosis; sickle cell anemia |
| **X-linked dominant** | Gene sa X chromosome; isang kopya sapat na | Rett syndrome |
| **X-linked recessive** | Gene sa X chromosome; mas apektado ang mga lalaki | Haemophilia; pagkabulag ng kulay |
| **Codominance** | Ang parehong mga alleles ay pantay na ipinahayag | Mga pangkat ng dugo ng ABO (A at B) |
| **Hindi kumpletong pangingibabaw** | Ang Heterozygote ay intermediate | Mga rosas na bulaklak mula sa pula at puting mga magulang |
| **Polygenic** | Maramihang mga gene ang nag-aambag sa isang katangian | Taas; kulay ng balat; katalinuhan |
| **Pleiotropy** | Nakakaapekto ang isang gene sa maraming katangian | Marfan syndrome (nag-uugnay na tissue, mata, puso) |
---

## Genomics
### Mga Uri ng Genomics
| Uri | Tumutok | Application |
|------|-------|-------------|
| **Structural genomics** | 3D na istraktura ng lahat ng mga protina sa isang genome | Disenyo ng droga; protina engineering |
| **Functional genomics** | Ano ang ginagawa ng mga gene; pakikipag-ugnayan ng gene; mga pattern ng expression | Pag-unawa sa mga mekanismo ng sakit |
| **Comparative genomics** | Paghahambing ng mga genome sa mga species | Ebolusyonaryong relasyon; pagtukoy sa mga conserved na rehiyon |
| **Metagenomics** | DNA mula sa mga sample ng kapaligiran (hindi kultura) | Pag-aaral ng microbiome; pagtuklas ng mga bagong organismo |
| **Pharmacogenomics** | Paano nakakaapekto ang mga gene sa pagtugon sa gamot | Personalized na gamot; dosing ng gamot |
| **Epigenomics** | Genome-wide epigenetic modifications | Diagnosis ng kanser; developmental biology |
### DNA Sequencing Technologies
| Henerasyon | Teknolohiya | Haba ng Pagbasa | Throughput | Pangunahing Tampok |
|-----------|-----------|-------------|------------|-------------|
| **Unang henerasyon** | Sanger sequencing | ~1,000 bp | Mababa | Gold standard na katumpakan; ginamit para sa pagpapatunay |
| **Ikalawang henerasyon** | Illumina (Solexa) | 50–300 bp | Napakataas | Maikling pagbabasa; nangingibabaw na plataporma; mababang gastos sa bawat base |
| **Ikalawang henerasyon** | Ion Torrent | 200–400 bp | Mataas | Nakabatay sa semiconductor; walang optika |
| **Ikatlong henerasyon** | PacBio (SMRT) | 10,000–100,000 bp | Katamtaman | Mahabang pagbabasa; niresolba ang mga paulit-ulit na rehiyon |
| **Ikatlong henerasyon** | Oxford Nanopore | Hanggang sa milyon-milyong bp | Katamtaman hanggang mataas | Mga ultra-mahabang pagbabasa; portable (MinION); real-time |
---

## Pagkakaiba-iba ng Genetic
### Mga Uri ng Variation
| Uri | Paglalarawan | Dalas |
|------|-------------|-----------|
| **SNP** (Single Nucleotide Polymorphism) | Pagbabago ng solong base | Pinaka-karaniwan; ~1 sa 1,000 base |
| **Pagpasok / Pagtanggal (indel)** | Pagdaragdag o pag-alis ng mga base | Maaaring magdulot ng mga frameshift mutations |
| **CNV** (Pagbabago ng Numero ng Kopya) | Nadoble o tinanggal na mga segment (1 kb – ilang Mb) | Nag-aambag sa sakit at ebolusyon |
| **Pagbabago ng istruktura** | Inversions; mga pagsasalin; malalaking muling pagsasaayos | Hindi gaanong karaniwan; maaaring pathogenic |
| **Microsatellite (STR)** | Mga maikling tandem na umuulit (2–6 bp inulit) | Forensics; pagsubok sa pagiging ama |
### GWAS (Genome-Wide Association Studies)
| Hakbang | Paglalarawan |
|------|-------------|
| **1. Mangolekta ng mga sample** | Mga kaso (may sakit) at kontrol (walang) |
| **2. Genotype** | Gumamit ng mga SNP array para mag-genotype ng daan-daang libong variant |
| **3. Pagsusulit sa istatistika** | Subukan ang bawat SNP para sa kaugnayan sa katangian |
| **4. Manhattan plot** | I-visualize ang mga resulta sa lahat ng chromosome |
| **5. Pagtitiklop** | Kumpirmahin ang mga natuklasan sa mga independiyenteng sample |
---

## Pag-edit ng Gene
### CRISPR-Cas9
| Bahagi | Function |
|-----------|----------|
| **Gabay sa RNA (gRNA)** | ~20 nucleotides; tumutugma sa target na DNA sequence |
| **Cas9 protein** | Molekular na gunting; pinutol ang DNA sa target na site |
| **PAM sequence** | Maikling motif (NGG) sa tabi ng target; kinakailangan para sa Cas9 binding |
| **HDR** (Homology-Directed Repair) | Tumpak na pag-edit gamit ang template ng donor |
| **NHEJ** (Non-Homologous End Joining) | Pagkumpuni na madaling kapitan ng error; lumilikha ng mga pagpapasok/pagtanggal (knockout) |
### Mga Application sa Pag-edit ng Gene
| Application | Paglalarawan |
|-------------|-------------|
| **Therapeutic** | Iwasto ang mga mutasyon na nagdudulot ng sakit (sickle cell; beta-thalassemia) |
| **Agrikultura** | Mga pananim na lumalaban sa sakit; pinahusay na hayop |
| **Pananaliksik** | Lumikha ng mga modelo ng knockout; pag-aralan ang function ng gene |
| **Gene drive** | Ikalat ang isang genetic modification sa pamamagitan ng isang populasyon (hal., malaria-resistant na mga lamok) |
---

## Mga Etikal na Pagsasaalang-alang
| Isyu | Pag-aalala |
|-------|---------|
| **Genetic privacy** | Sino ang nagmamay-ari ng iyong genome data? Magagamit ba ito ng mga employer o insurer? |
| **Pag-edit ng gene sa mga embryo** | Mga pagbabagong namamana; mga sanggol na taga-disenyo; hindi sinasadyang off-target na mga epekto |
| **Henetikong diskriminasyon** | Ang GINA (US) ay nagpoprotekta laban sa ilang diskriminasyon ngunit may mga puwang |
| **Informed consent** | Ang genomic data ay nagpapakita ng impormasyon tungkol sa mga kamag-anak na hindi pumayag |
| **Imbakan ng data** | Ang mga genome ay malaki (~200 GB raw); pangmatagalang imbakan at mga hamon sa seguridad |
| **Equity** | Ang genomic na gamot ay nanganganib sa pagpapalawak ng mga pagkakaiba sa kalusugan kung magagamit lamang sa mayayamang populasyon |
---

## Buod
Pinag-aaralan ng genetika kung paano gumagana at namamana ang mga indibidwal na gene. Pinag-aaralan ng Genomics ang buong genome — lahat ng gene, ang kanilang mga pakikipag-ugnayan, at ang kanilang pagkakaiba-iba. Ang DNA ay na-transcribe sa RNA, na isinalin sa mga protina. Ang expression ng gene ay kinokontrol sa maraming antas: epigenetic, transcriptional, post-transcriptional, translational, at post-translational. Ang mana ay sumusunod sa mga pattern (dominant, recessive, polygenic) na tumutukoy kung paano pumasa ang mga katangian sa pagitan ng mga henerasyon. Ang mga modernong teknolohiya sa pagkakasunud-sunod (Illumina, PacBio, Nanopore) ay makakapagbasa ng buong genome nang mabilis at mura. Ang CRISPR-Cas9 ay nagbibigay-daan sa tumpak na pag-edit ng gene na may potensyal na pagbabago sa medisina at agrikultura. Ang pinakamalaking hamon ay etikal: sino ang kumokontrol sa genomic data, kung paano i-regulate ang pag-edit ng gene sa mga embryo, at kung paano matiyak na ang genomic na gamot ay nakikinabang sa lahat, hindi lamang sa mga may pribilehiyo.