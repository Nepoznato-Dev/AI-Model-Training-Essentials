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

# Terraform na Miundombinu kama Kanuni
Terraform ndio zana inayotumika sana ya Miundombinu kama Msimbo (IaC) - hukuruhusu kufafanua miundombinu ya wingu (seva, hifadhidata, mitandao, ruhusa) katika faili za usanidi zinazotangaza ambazo zinaweza kubadilishwa, kukaguliwa, kujaribiwa na kuendeshwa kiotomatiki. Badala ya kubofya kiweko cha wingu, unaandika msimbo unaoelezea hali unayotaka ya miundombinu yako, na Terraform inabainisha mabadiliko ya kufanya.
---

## Dhana za Msingi
| Dhana | Maelezo |
|---------|-------------|
| **Mtoa huduma** | Programu-jalizi inayodhibiti jukwaa mahususi la wingu (AWS, Azure, GCP, n.k.) |
| **Nyenzo** | Kitu cha miundombinu (seva, hifadhidata, mtandao) |
| **Jimbo** | Rekodi ya Terraform ya miundombinu iliyopo; iliyohifadhiwa katika faili ya hali |
| **Mpango** | Hakiki ya mabadiliko gani Terraform itafanya |
| **Tuma** | Tekeleza mpango; unda/sasisha/haribu miundombinu |
| **Moduli** | Mkusanyiko unaoweza kutumika tena wa rasilimali |
| **Kigezo** | Kigezo cha ingizo cha usanidi |
| **Pato** | Thamani iliyohamishwa kutoka kwa moduli au usanidi |
| **Chanzo cha data** | Soma habari kutoka kwa miundombinu iliyopo |
---

## Mtiririko wa Msingi wa Kazi
| Hatua | Amri | Maelezo |
|------|-----------------------|
| **1. Andika usanidi** | Unda faili za`.tf`| Bainisha watoa huduma, rasilimali, vigezo |
| **2. Anzisha** | `terraform init`| Pakua watoa huduma; weka mazingira ya nyuma |
| **3. Umbizo** | `terraform fmt`| Sawazisha umbizo |
| **4. Thibitisha** | `terraform validate`| Angalia sintaksia na usanidi |
| **5. Mpango** | `terraform plan`| Hakiki mabadiliko (kavu kukimbia) |
| **6. Tumia** | `terraform apply`| Unda au sasisha miundombinu |
| **7. Kuharibu ** | `terraform destroy`| Bomoa miundombinu yote inayosimamiwa |
---

## Amri za kawaida
| Amri | Maelezo |
|---------|-------------|
| `terraform init`| Anzisha saraka ya kufanya kazi; pakua watoa huduma na moduli |
| `terraform plan`| Onyesha mabadiliko gani yatafanywa |
| `terraform apply`| Omba mabadiliko; ongeza`-auto-approve`ili kuruka uthibitisho |
| `terraform destroy`| Kuharibu rasilimali zote zinazodhibitiwa |
| `terraform fmt`| Fomati faili za usanidi kwa mtindo wa kawaida |
| `terraform validate`| Thibitisha sintaksia ya usanidi |
| `terraform output`| Onyesha thamani za pato |
| `terraform state list`| Orodhesha rasilimali zote katika jimbo |
| `terraform state show <resource>`| Onyesha maelezo ya rasilimali mahususi |
| `terraform import <resource> <id>`| Ingiza miundombinu iliyopo katika hali |
| `terraform taint <resource>`| Weka alama kwenye nyenzo kwa ajili ya burudani kwenye maombi yanayofuata |
| `terraform refresh`| Sasisha hali ili ilingane na miundombinu halisi |
| `terraform graph`| Tengeneza grafu ya utegemezi inayoonekana (umbizo la DOT) |
| `terraform console`| Dashibodi inayoingiliana ya kujaribu misemo |
---

## Usimamizi wa Jimbo
| Mazoezi Bora | Maelezo |
|----------------------------|
| **Jimbo la mbali** | Hifadhi hali katika S3, GCS, Azure Blob, au Terraform Cloud — kamwe ndani ya nchi |
| **Kufunga hali** | Tumia DynamoDB (Nyuma ya nyuma ya S3) au kufunga asili ili kuzuia marekebisho yanayofanyika kwa wakati mmoja |
| **Usimbaji fiche wa serikali** | Washa usimbaji fiche wakati wa mapumziko kwa faili za serikali (zina data nyeti) |
| **Kutengana kwa serikali** | Tumia faili za hali tofauti kwa mazingira au timu tofauti |
| **Chelezo ya serikali** | Backends za mbali hali ya toleo la kiotomatiki; weka hii kuwezeshwa |
| **Usiwahi kuhariri hali wewe mwenyewe** | Tumia`terraform state mv`,`rm`,`import`badala yake |
---

## Muundo wa Moduli
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

## Aina Zinazobadilika
| Aina | Mfano | Tumia Kesi |
|------|---------------------|
| **kamba** | `variable "region" { type = string }`| Nakala moja ya thamani |
| **namba** | `variable "count" { type = number }`| Thamani ya nambari |
| **bool** | `variable "enable" { type = bool }`| Bendera ya kweli/uongo |
| **orodha** | `variable "zones" { type = list(string) }`| Mkusanyiko ulioagizwa |
| **ramani** | `variable "tags" { type = map(string) }`| Jozi za thamani-muhimu |
| **kitu** | `variable "config" { type = object({...}) }`| Usanidi uliopangwa |
---

## Miundo ya Kawaida
| Muundo | Maelezo |
|---------|-------------|
| **Hesabu** | `count = 3`huunda mifano mingi ya rasilimali |
| **Kwa kila** | `for_each = var.items`inasisitiza juu ya ramani au seti |
| **Vizuizi vinavyobadilika** | Tengeneza vizuizi vilivyowekwa mara kwa mara (k.m., sheria za kuingilia) |
| **Thamani za ndani** | `locals { ... }`kwa thamani zilizokokotwa na kupunguza marudio |
| **Vyanzo vya data** | Soma miundombinu iliyopo (k.m., pata VPC iliyopo) |
| **Watoa huduma** | Endesha maandishi kwenye rasilimali baada ya kuunda (tumia kwa uangalifu) |
| **Nafasi za kazi** | Hali tofauti kwa mazingira tofauti ndani ya usanidi sawa |
---

## Utatuzi wa matatizo
| Tatizo | Suluhisho |
|---------|----------|
| **State drift** | Endesha`terraform plan`ili kuona tofauti; `terraform apply`kupatanisha |
| **Hali iliyofungwa** | Angalia ni nani aliye na kufuli; tumia`terraform force-unlock`ikiwa salama |
| **Makosa ya mtoa huduma** | Angalia vitambulisho; sasisha toleo la mtoaji; angalia mipaka ya API |
| **Ingiza migogoro** | Rasilimali tayari katika hali; tumia`terraform state rm`kwanza |
| **Vitegemezi vya mduara** | Rasilimali za urekebishaji; tumia`depends_on`kwa uangalifu |
| **Jimbo kubwa** | Gawanya katika moduli; tumia`-target`kwa shughuli za sehemu |
---

## Muhtasari
Terraform inasimamia miundombinu kupitia faili za usanidi zinazotangaza. Mtiririko wa kazi ni: andika usanidi → init → panga → tuma. Jimbo hufuatilia kilichopo na lazima kihifadhiwe kwa mbali kwa kufunga. Moduli huwezesha matumizi tena. Vigezo vinaweka usanidi. Kanuni kuu ni: kuchukulia miundombinu kama kanuni (udhibiti wa toleo; hakiki; jaribio); usiwahi kuhariri hali mwenyewe; kupanga kabla ya kuomba; tumia hali ya mbali na kufuli; na usanidi wa muundo na moduli za kudumisha.