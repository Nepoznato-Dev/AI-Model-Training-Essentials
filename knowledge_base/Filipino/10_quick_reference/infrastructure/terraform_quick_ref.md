---
# Metadata
title: "Terraform and Infrastructure as Code"
description: "IaC concepts, Terraform commands, state management, modules"
category: "Quick Reference"
subcategory: "Infrastructure"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [terraform, quick-reference]
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

# Terraform at Infrastructure bilang Code
Ang Terraform ay ang pinakalawak na ginagamit na tool na Infrastructure bilang Code (IaC) — hinahayaan ka nitong tukuyin ang cloud infrastructure (mga server, database, network, pahintulot) sa mga declarative configuration file na maaaring ma-bersyon, suriin, masuri, at awtomatiko. Sa halip na mag-click sa cloud console, magsusulat ka ng code na naglalarawan sa gustong estado ng iyong imprastraktura, at tinutukoy ng Terraform kung ano ang mga pagbabagong gagawin.
---

## Mga Pangunahing Konsepto
| Konsepto | Paglalarawan |
|---------|-------------|
| **Provider** | Plugin na namamahala sa isang partikular na cloud platform (AWS, Azure, GCP, atbp.) |
| **Resource** | Isang bagay sa imprastraktura (server, database, network) |
| **Estado** | Talaan ng Terraform kung anong imprastraktura ang umiiral; naka-imbak sa isang state file |
| **Plano** | Silipin kung anong mga pagbabago ang gagawin ng Terraform |
| **Mag-apply** | Isagawa ang plano; lumikha/mag-update/magsira ng imprastraktura |
| **Modyul** | Magagamit muli na koleksyon ng mga mapagkukunan |
| **Variable** | Parameter ng input para sa mga configuration |
| **Output** | Na-export ang halaga mula sa isang module o configuration |
| **Pinagmulan ng data** | Basahin ang impormasyon mula sa umiiral na imprastraktura |
---

## Pangunahing Daloy ng Trabaho
| Hakbang | Utos | Paglalarawan |
|------|---------|-------------|
| **1. Sumulat ng configuration** | Lumikha ng`.tf`file | Tukuyin ang mga provider, mapagkukunan, variable |
| **2. Magsimula** | `terraform init`| Mga provider ng pag-download; i-set up ang backend |
| **3. Format** | `terraform fmt`| I-standardize ang pag-format |
| **4. Patunayan** | `terraform validate`| Suriin ang syntax at configuration |
| **5. Plan** | `terraform plan`| I-preview ang mga pagbabago (dry run) |
| **6. Mag-apply** | `terraform apply`| Gumawa o mag-update ng imprastraktura |
| **7. Wasakin** | `terraform destroy`| Ibagsak ang lahat ng pinamamahalaang imprastraktura |
---

## Mga Karaniwang Utos
| Utos | Paglalarawan |
|---------|-------------|
| `terraform init`| Magsimula ng direktoryo ng pagtatrabaho; mag-download ng mga provider at module |
| `terraform plan`| Ipakita kung anong mga pagbabago ang gagawin |
| `terraform apply`| Ilapat ang mga pagbabago; idagdag ang`-auto-approve`upang laktawan ang kumpirmasyon |
| `terraform destroy`| Wasakin ang lahat ng pinamamahalaang mapagkukunan |
| `terraform fmt`| I-format ang mga configuration file sa karaniwang istilo |
| `terraform validate`| I-validate ang configuration syntax |
| `terraform output`| Ipakita ang mga halaga ng output |
| `terraform state list`| Ilista ang lahat ng mapagkukunan sa estado |
| `terraform state show <resource>`| Ipakita ang mga detalye ng isang partikular na mapagkukunan |
| `terraform import <resource> <id>`| Mag-import ng kasalukuyang imprastraktura sa estado |
| `terraform taint <resource>`| Markahan ang isang mapagkukunan para sa libangan sa susunod na ilapat |
| `terraform refresh`| I-update ang estado upang tumugma sa tunay na imprastraktura |
| `terraform graph`| Bumuo ng visual dependency graph (DOT format) |
| `terraform console`| Interactive console para sa pagsubok ng mga expression |
---

## Pamamahala ng Estado
| Pinakamahusay na Kasanayan | Paglalarawan |
|--------------|-------------|
| **Remote state** | Katayuan ng tindahan sa S3, GCS, Azure Blob, o Terraform Cloud — hindi kailanman lokal |
| **Pagla-lock ng estado** | Gumamit ng DynamoDB (S3 backend) o native locking upang maiwasan ang mga sabay-sabay na pagbabago |
| **Pag-encrypt ng estado** | I-enable ang encryption at rest para sa mga state file (naglalaman sila ng sensitibong data) |
| **Paghihiwalay ng estado** | Gumamit ng hiwalay na mga state file para sa iba't ibang environment o team |
| **Back up ng estado** | Awtomatikong estado ng bersyon ang mga remote na backend; panatilihin itong pinagana |
| **Huwag kailanman manu-manong i-edit ang estado** | Gamitin ang`terraform state mv`,`rm`,`import`sa halip |
---

## Istraktura ng Module
```
module/
├── main.tf          # Primary resources
├── variables.tf     # Input variables
├── outputs.tf       # Output values
├── versions.tf      # Provider and Terraform version constraints
├── README.md        # Documentation
└── examples/        # Example usage
    └── basic/
        └── main.tf
```

---

## Mga Uri ng Variable
| Uri | Halimbawa | Use Case |
|------|---------|----------|
| **string** | `variable "region" { type = string }`| Iisang text value |
| **numero** | `variable "count" { type = number }`| Numeric na halaga |
| **bool** | `variable "enable" { type = bool }`| True/false flag |
| **listahan** | `variable "zones" { type = list(string) }`| Inorder na koleksyon |
| **mapa** | `variable "tags" { type = map(string) }`| Key-value pairs |
| **bagay** | `variable "config" { type = object({...}) }`| Nakabalangkas na configuration |
---

## Mga Karaniwang Pattern
| Pattern | Paglalarawan |
|---------|-------------|
| **Bilang** |  Lumilikha ang`count = 3`ng maraming pagkakataon ng isang mapagkukunan |
| **Para sa bawat** | `for_each = var.items`umuulit sa isang mapa o set |
| **Mga dynamic na bloke** | Bumuo ng paulit-ulit na nested block (hal., mga panuntunan sa pagpasok) |
| **Mga lokal na halaga** | `locals { ... }`para sa mga nakalkulang halaga at binabawasan ang pag-uulit |
| **Mga mapagkukunan ng data** | Basahin ang kasalukuyang imprastraktura (hal., humanap ng kasalukuyang VPC) |
| **Mga Tagapagbigay** | Magpatakbo ng mga script sa mga mapagkukunan pagkatapos ng paggawa (gamitin nang matipid) |
| **Mga Workspace** | Paghiwalayin ang estado para sa iba't ibang mga kapaligiran sa loob ng parehong config |
---

## Pag-troubleshoot
| Problema | Solusyon |
|---------|----------|
| **State drift** | Patakbuhin ang`terraform plan`upang makita ang mga pagkakaiba; `terraform apply`para magkasundo |
| **Naka-lock na estado** | Suriin kung sino ang may lock; gamitin ang`terraform force-unlock`kung ligtas |
| **Mga error sa provider** | Suriin ang mga kredensyal; i-update ang bersyon ng provider; suriin ang mga limitasyon ng API |
| **Mga salungatan sa pag-import** | Nasa estado na ang mapagkukunan; gamitin muna ang`terraform state rm`|
| **Mga pabilog na dependency** | Restructure resources; gamitin nang mabuti ang`depends_on`|
| **Malaking estado** | Hatiin sa mga module; gamitin ang`-target`para sa mga bahagyang pagpapatakbo |
---

## Buod
Pinamamahalaan ng Terraform ang imprastraktura sa pamamagitan ng mga declarative configuration file. Ang workflow ay: write configuration → init → plan → apply. Sinusubaybayan ng estado kung ano ang umiiral at dapat na naka-imbak nang malayuan na may pag-lock. Pinapagana ng mga module ang muling paggamit. Mga configuration ng parameterise ng mga variable. Ang mga pangunahing prinsipyo ay: ituring ang imprastraktura bilang code (kontrol sa bersyon; pagsusuri; pagsubok); huwag kailanman manu-manong i-edit ang estado; magplano bago mag-apply; gumamit ng malayuang estado na may pag-lock; at mga pagsasaayos ng istraktura na may mga module para sa pagpapanatili.