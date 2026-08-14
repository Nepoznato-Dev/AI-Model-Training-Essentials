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
# Genetica e genomica
La genetica è lo studio dell’ereditarietà: il modo in cui i tratti vengono trasmessi dai genitori alla prole attraverso il DNA. La genomica è lo studio di interi genomi: tutti i geni, le regioni non codificanti, come interagiscono e come variano tra individui e popolazioni. La transizione dalla genetica alla genomica è stata guidata dalla tecnologia di sequenziamento: siamo passati dallo studio di un gene alla volta alla lettura di interi genomi in poche ore, generando dati che stanno trasformando la medicina, l’agricoltura, la medicina legale e la nostra comprensione dell’evoluzione.
---

## Fondamenti del DNA
### Struttura del DNA
| Componente | Descrizione |
|-----------|-------------|
| **Nucleotide** | Elemento costitutivo del DNA; è costituito da uno zucchero (desossiribosio), un gruppo fosfato e una base azotata |
| **Basi** | Adenina (A), Timina (T), Guanina (G), Citosina (C) |
| **Accoppiamento di basi** | A si accoppia con T (2 legami idrogeno); G si accoppia con C (3 legami idrogeno) |
| **Doppia elica** | Due filamenti che corrono in modo antiparallelo (da 5' a 3' e da 3' a 5'); attorcigliato in un'elica |
| **Cromosoma** | Una singola, lunga molecola di DNA avvolta attorno alle proteine ​​istoniche; gli esseri umani ne hanno 46 (23 paia) |
| **Genoma** | L'insieme completo del DNA in un organismo; il genoma umano è di ~3,2 miliardi di paia di basi |
### Dogma centrale della biologia molecolare
| Passo | Processo | Posizione | Prodotto |
|------|---------|----------|---------|
| **Replica** | DNA → DNA | Nucleo | Due molecole di DNA identiche |
| **Trascrizione** | DNA → mRNA | Nucleo | RNA messaggero |
| **Traduzione** | mRNA → proteina | Ribosoma (citoplasma) | Catena polipeptidica (proteina) |
---

## Espressione genica
### Come sono regolati i geni
| Livello | Meccanismo | Esempio |
|-------|-----------|---------|
| **Epigenetico** | Metilazione del DNA; modificazione degli istoni; rimodellamento della cromatina | Silenziamento di un cromosoma X nelle femmine |
| **Trascrizione** | I fattori di trascrizione legano promotori/potenziatori; attivare o reprimere | operone Lac nei batteri; geni che rispondono agli ormoni |
| **Post-trascrizionale** | Splicing alternativo; stabilità dell'mRNA; microRNA | Un gene → molteplici varianti proteiche |
| **Traslazionale** | Disponibilità ribosomiale; regolazione del fattore di inizio | Regolazione del ferro tramite mRNA della ferritina |
| **Post-traduzionale** | Modificazione delle proteine ​​(fosforilazione, ubiquitinazione); degrado | Controllo del ciclo cellulare |
---

## Modelli di ereditarietà
### Genetica mendeliana
| Modello | Descrizione | Esempio |
|---------|-----|---------|
| **Autosomico dominante** | È sufficiente una copia dell'allele | La malattia di Huntington; acondroplasia |
| **Autosomico recessivo** | Sono necessarie due copie | Fibrosi cistica; anemia falciforme |
| **Dominante legata all'X** | Gene sul cromosoma X; è sufficiente una copia | Sindrome di Rett |
| **Recessivo legato all'X** | Gene sul cromosoma X; maschi più colpiti | Emofilia; daltonismo |
| **Codominanza** | Entrambi gli alleli si esprimono allo stesso modo | Gruppi sanguigni ABO (A e B) |
| **Dominanza incompleta** | L'eterozigote è intermedio | Fiori rosa da genitori rossi e bianchi |
| **Poligenico** | Più geni contribuiscono a un tratto | Altezza; colore della pelle; intelligenza |
| **Pleiotropia** | Un gene influenza più tratti | Sindrome di Marfan (tessuto connettivo, occhi, cuore) |
---

## Genomica
### Tipi di genomica
| Digitare | Messa a fuoco | Applicazione |
|------|-------|-----|
| **Genomica strutturale** | Struttura 3D di tutte le proteine ​​in un genoma | Progettazione di farmaci; ingegneria delle proteine ​​|
| **Genomica funzionale** | Cosa fanno i geni; interazioni genetiche; modelli di espressione | Comprendere i meccanismi della malattia |
| **Genomica comparativa** | Confronto dei genomi tra le specie | Relazioni evolutive; identificazione delle regioni conservate |
| **Metagenomica** | DNA da campioni ambientali (non coltivati) | Studi sul microbioma; scoprire nuovi organismi |
| **Farmacogenomica** | Come i geni influenzano la risposta ai farmaci | Medicina personalizzata; dosaggio dei farmaci |
| **Epigenomica** | Modifiche epigenetiche dell'intero genoma | Diagnosi del cancro; biologia dello sviluppo |
### Tecnologie di sequenziamento del DNA
| Generazione | Tecnologia | Leggi Lunghezza | Produttività | Caratteristica fondamentale |
|-----------|-----------|-----|----|-------------|
| **Prima generazione** | Sequenziamento di Sanger | ~1.000 punti base | Basso | Precisione standard di riferimento; utilizzato per la convalida |
| **Seconda generazione** | Illumina (Solexa) | 50–300 punti di partenza | Molto alto | Letture brevi; piattaforma dominante; basso costo per base |
| **Seconda generazione** | Ione Torrente | 200–400 punti di partenza | Alto | Basato su semiconduttori; nessuna ottica |
| **Terza generazione** | PacBio (SMRT) | 10.000–100.000 punti base | Moderato | Letture lunghe; risolve le regioni ripetitive |
| **Terza generazione** | Nanoporo di Oxford | Fino a milioni di bp | Da moderato ad alto | Letture ultra lunghe; portatile (MinION); in tempo reale |
---

## Variazione genetica
### Tipi di variazione
| Digitare | Descrizione | Frequenza |
|------|-------------|-----------|
| **SNP** (Polimorfismo a singolo nucleotide) | Cambio di base singola | Più comune; ~1 su 1.000 basi |
| **Inserimento/Cancellazione (indel)** | Aggiunta o rimozione di basi | Può causare mutazioni frameshift |
| **CNV** (Variazione numero copie) | Segmenti duplicati o cancellati (1 kb – diversi Mb) | Contribuisce alla malattia e all'evoluzione |
| **Variazione strutturale** | Inversioni; traslocazioni; grandi riarrangiamenti | Meno comune; può essere patogeno |
| **Microsatellite (STR)** | Brevi ripetizioni in tandem (2–6 bp ripetute) | medicina legale; test di paternità |
### GWAS (studi sull'associazione su tutto il genoma)
| Passo | Descrizione |
|------|-------------|
| **1. Raccogliere campioni** | Casi (con malattia) e controlli (senza) |
| **2. Genotipo** | Utilizza gli array SNP per genotipizzare centinaia di migliaia di varianti |
| **3. Test statistico** | Testare ogni SNP per l'associazione con il tratto |
| **4. Trama di Manhattan** | Visualizza i risultati su tutti i cromosomi |
| **5. Replica** | Confermare i risultati in campioni indipendenti |
---

## Modifica genetica
### CRISPR-Cas9
| Componente | Funzione |
|-----------|----------|
| **RNA guida (gRNA)** | ~20 nucleotidi; corrisponde alla sequenza di DNA target |
| **Proteina Cas9** | Forbici molecolari; taglia il DNA nel sito bersaglio |
| **Sequenza PAM** | Motivo breve (NGG) accanto al bersaglio; richiesto per la rilegatura Cas9 |
| **HDR** (riparazione diretta dall'omologia) | Modifica precisa utilizzando un modello di donatore |
| **NHEJ** (Unione finale non omologa) | Riparazione soggetta a errori; crea inserimenti/eliminazioni (knockout) |
### Applicazioni di modifica genetica
| Applicazione | Descrizione |
|-------------|-------------|
| **Terapeutico** | Correggere le mutazioni patogenetiche (anemia falciforme; beta-talassemia) |
| **Agricoltura** | Colture resistenti alle malattie; bestiame migliorato |
| **Ricerca** | Creare modelli ad eliminazione diretta; studiare la funzione del gene |
| **Genedrive** | Diffondere una modificazione genetica in una popolazione (ad esempio, zanzare resistenti alla malaria) |
---

## Considerazioni etiche
| Problema | Preoccupazione |
|-------|---------|
| **Privacy genetica** | Chi possiede i dati del tuo genoma? Possono utilizzarlo i datori di lavoro o gli assicuratori? |
| **Modifica genetica negli embrioni** | Cambiamenti ereditari; bambini firmati; effetti indesiderati fuori bersaglio |
| **Discriminazione genetica** | GINA (USA) protegge da alcune discriminazioni ma presenta lacune |
| **Consenso informato** | I dati genomici rivelano informazioni su parenti che non hanno acconsentito |
| **Archiviazione dei dati** | I genomi sono grandi (~200 GB grezzi); sfide di archiviazione e sicurezza a lungo termine |
| **Patrimonio netto** | La medicina genomica rischia di ampliare le disparità sanitarie se disponibile solo per le popolazioni benestanti |
---

## Riepilogo
La genetica studia il modo in cui i singoli geni funzionano e vengono ereditati. La genomica studia interi genomi: tutti i geni, le loro interazioni e la loro variazione. Il DNA viene trascritto in RNA, che viene tradotto in proteine. L'espressione genica è regolata a più livelli: epigenetico, trascrizionale, post-trascrizionale, traduzionale e post-traduzionale. L'ereditarietà segue modelli (dominante, recessivo, poligenico) che determinano il modo in cui i tratti passano tra le generazioni. Le moderne tecnologie di sequenziamento (Illumina, PacBio, Nanopore) possono leggere interi genomi in modo rapido ed economico. CRISPR-Cas9 consente un editing genetico preciso con potenziale di trasformazione in medicina e agricoltura. Le sfide più grandi sono di natura etica: chi controlla i dati genomici, come regolare l’editing genetico negli embrioni e come garantire che la medicina genomica avvantaggi tutti, non solo i privilegiati.