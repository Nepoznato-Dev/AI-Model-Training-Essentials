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

# Terraform e infrastruttura come codice
Terraform è lo strumento Infrastructure as Code (IaC) più utilizzato: consente di definire l'infrastruttura cloud (server, database, reti, autorizzazioni) in file di configurazione dichiarativi che possono essere sottoposti a controllo della versione, revisionati, testati e automatizzati. Invece di fare clic su una console cloud, scrivi il codice che descrive lo stato desiderato della tua infrastruttura e Terraform capisce quali modifiche apportare.
---

## Concetti fondamentali
| Concetto | Descrizione |
|---------|-----|
| **Fornitore** | Plugin che gestisce una specifica piattaforma cloud (AWS, Azure, GCP, ecc.) |
| **Risorsa** | Un oggetto infrastrutturale (server, database, rete) |
| **Stato** | Il registro di Terraform dell'infrastruttura esistente; memorizzato in un file di stato |
| **Piano** | Anteprima delle modifiche apportate da Terraform |
| **Applica** | Eseguire il piano; creare/aggiornare/distruggere infrastrutture |
| **Modulo** | Raccolta riutilizzabile di risorse |
| **Variabile** | Parametro di input per configurazioni |
| **Uscita** | Valore esportato da un modulo o configurazione |
| **Fonte dati** | Leggi le informazioni dalle infrastrutture esistenti |
---

## Flusso di lavoro di base
| Passo | Comando | Descrizione |
|------|---------|-----|
| **1. Scrivi configurazione** | Crea file`.tf`| Definire fornitori, risorse, variabili |
| **2. Inizializza** | `terraform init`| Fornitori di download; impostare il backend |
| **3. Formato** | `terraform fmt`| Standardizzare la formattazione |
| **4. Convalida** | `terraform validate`| Controlla la sintassi e la configurazione |
| **5. Piano** | `terraform plan`| Anteprima delle modifiche (prova) |
| **6. Applica** | `terraform apply`| Creare o aggiornare l'infrastruttura |
| **7. Distruggi** | `terraform destroy`| Abbattere tutta l'infrastruttura gestita |
---

## Comandi comuni
| Comando | Descrizione |
|---------|-----|
| `terraform init`| Inizializza la directory di lavoro; download di fornitori e moduli |
| `terraform plan`| Mostra quali modifiche verranno apportate |
| `terraform apply`| Applicare le modifiche; aggiungi`-auto-approve`per saltare la conferma |
| `terraform destroy`| Distruggi tutte le risorse gestite |
| `terraform fmt`| Formatta i file di configurazione nello stile standard |
| `terraform validate`| Convalida la sintassi di configurazione |
| `terraform output`| Mostra valori di output |
| `terraform state list`| Elenca tutte le risorse nello stato |
| `terraform state show <resource>`| Mostra i dettagli di una risorsa specifica |
| `terraform import <resource> <id>`| Importare le infrastrutture esistenti nello stato |
| `terraform taint <resource>`| Contrassegna una risorsa per la ricreazione alla prossima applicazione |
| `terraform refresh`| Aggiorna lo stato per adattarlo all'infrastruttura reale |
| `terraform graph`| Genera un grafico delle dipendenze visivo (formato DOT) |
| `terraform console`| Console interattiva per testare le espressioni |
---

## Gestione statale
| Migliori pratiche | Descrizione |
|--------------|-------------|
| **Stato remoto** | Archivia lo stato in S3, GCS, BLOB di Azure o Terraform Cloud, mai localmente |
| **Blocco dello stato** | Utilizza DynamoDB (backend S3) o il blocco nativo per impedire modifiche simultanee |
| **Crittografia dello stato** | Abilita la crittografia dei dati inattivi per i file di stato (contengono dati sensibili) |
| **Separazione degli Stati** | Utilizza file di stato separati per ambienti o team diversi |
| **Backup dello stato** | Stato della versione dei backend remoti automaticamente; mantienilo abilitato |
| **Non modificare mai lo stato manualmente** | Utilizza invece`terraform state mv`,`rm`,`import`|
---

## Struttura del modulo
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

## Tipi di variabili
| Digitare | Esempio | Caso d'uso |
|------|---------|----------|
| **stringa** | `variable "region" { type = string }`| Valore di testo singolo |
| **numero** | `variable "count" { type = number }`| Valore numerico |
| **bool** | `variable "enable" { type = bool }`| Flag vero/falso |
| **elenco** | `variable "zones" { type = list(string) }`| Raccolta ordinata |
| **mappa** | `variable "tags" { type = map(string) }`| Coppie chiave-valore |
| **oggetto** | `variable "config" { type = object({...}) }`| Configurazione strutturata |
---

## Modelli comuni
| Modello | Descrizione |
|---------|-----|
| **Conta** | `count = 3`crea più istanze di una risorsa |
| **Per ciascuno** | `for_each = var.items`scorre su una mappa o imposta |
| **Blocchi dinamici** | Genera blocchi nidificati ripetuti (ad esempio, regole di ingresso) |
| **Valori locali** | `locals { ... }`per valori calcolati e riduzione della ripetizione |
| **Fonti dati** | Leggere l'infrastruttura esistente (ad esempio, trovare un VPC esistente) |
| **Fornitori** | Esegui script sulle risorse dopo la creazione (usa con parsimonia) |
| **Spazi di lavoro** | Stato separato per ambienti diversi all'interno della stessa configurazione |
---

## Risoluzione dei problemi
| Problema | Soluzione |
|---------|----------|
| **Deriva dello stato** | Esegui`terraform plan`per vedere le differenze; `terraform apply`per riconciliare |
| **Stato bloccato** | Controlla chi ha la serratura; usa`terraform force-unlock`se sicuro |
| **Errori del provider** | Verificare le credenziali; aggiornare la versione del provider; controlla i limiti API |
| **Conflitti di importazione** | Risorsa già nello stato; usa prima`terraform state rm`|
| **Dipendenze circolari** | Ristrutturare le risorse; utilizzare`depends_on`con attenzione |
| **Grande stato** | Suddiviso in moduli; utilizzare`-target`per operazioni parziali |
---

## Riepilogo
Terraform gestisce l'infrastruttura tramite file di configurazione dichiarativi. Il flusso di lavoro è: scrivi configurazione → init → pianifica → applica. Lo stato tiene traccia di ciò che esiste e deve essere archiviato in remoto con blocco. I moduli consentono il riutilizzo. Le variabili parametrizzano le configurazioni. I principi chiave sono: trattare l'infrastruttura come codice (controllo della versione, revisione, test); non modificare mai lo stato manualmente; pianificare prima di applicare; utilizzare lo stato remoto con blocco; e configurazioni della struttura con moduli per la manutenibilità.