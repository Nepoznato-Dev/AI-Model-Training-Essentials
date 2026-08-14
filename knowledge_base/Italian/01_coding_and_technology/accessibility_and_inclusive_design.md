<!--
---
# Metadata
title: "Accessibility and Inclusive Design"
description: "WCAG, inclusive UX, assistive technology, accessible coding"
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
tags: [accessibility, inclusive, design, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Accessibilità e progettazione inclusiva
L'accessibilità (spesso abbreviata in a11y) è la pratica di rendere il software utilizzabile da tutti, comprese le persone con disabilità visive, uditive, motorie, cognitive e neurologiche. Si tratta di un requisito legale in molte giurisdizioni e di una pratica ingegneristica standard. Il software accessibile è un software migliore per tutti, perché le decisioni di progettazione che supportano gli utenti disabili (struttura chiara, navigazione tramite tastiera, contrasto sufficiente, testo leggibile) migliorano l'esperienza per tutti gli utenti.
---

## Chi trae vantaggio dall'accessibilità?
| Tipo di disabilità | Esempi | Tecnologia assistiva |
|----------------|---------|---------------------|
| **Visivo** | Cecità, ipovisione, daltonismo | Lettori di schermo (JAWS, NVDA, VoiceOver); lenti di ingrandimento; modalità ad alto contrasto |
| **Uditivo** | Sordità, problemi di udito | Didascalie; trascrizioni; avvisi visivi |
| **Motore** | Destrezza limitata, paralisi, tremore | Navigazione solo tramite tastiera; controllo vocale; commutare i dispositivi; tracciamento oculare |
| **Cognitivo** | Dislessia, ADHD, autismo, disturbi della memoria | Linguaggio chiaro; navigazione coerente; distrazioni ridotte |
| **Temporaneo** | Braccio rotto, luce solare intensa, ambiente rumoroso | Stesse agevolazioni delle disabilità permanenti |
| **Situazionale** | Tenendo in braccio un bambino, guidando, con una mano occupata | Interfacce vocali; bersagli tattili di grandi dimensioni |
**Approfondimento chiave**: le funzionalità di accessibilità progettate per gli utenti disabili aiutano tutti. I cordoli (rampe sui marciapiedi) sono stati progettati per le sedie a rotelle ma sono utilizzati da genitori con passeggini, addetti alle consegne con carrelli e viaggiatori con bagagli.
---

## Accessibilità Web (WCAG)
Le Linee Guida per l’Accessibilità dei Contenuti Web (WCAG) sono lo standard internazionale per l’accessibilità del web.
### Principi WCAG (POUR)
| Principio | Requisito |
|-----------|-------------|
| **Percepibile** | Le informazioni devono essere presentabili in modo che gli utenti possano percepirle (alternative testuali, didascalie, layout adattabile) |
| **Operabile** | L'interfaccia deve essere navigabile e utilizzabile (accessibile dalla tastiera, tempo sufficiente, nessun contenuto che induca alle crisi) |
| **Comprensibile** | Le informazioni e il funzionamento devono essere comprensibili (leggibili, prevedibili, assistenza nell'immissione) |
| **Robusto** | Il contenuto deve funzionare con le tecnologie assistive attuali e future |
### Livelli di conformità WCAG
| Livello | Requisiti | Obiettivo tipico |
|-------|-------------|-------|
| **A** | Livello minimo; 30 criteri di successo | Minimo legale in alcune giurisdizioni |
| **AA** | Affronta gli ostacoli più comuni | Obiettivo standard per la maggior parte delle organizzazioni |
| **AAA** | Livello più alto; non tutti i contenuti possono raggiungerlo | Contenuti specializzati; siti educativi |
### Criteri chiave di successo (livello AA)
| Criterio | Requisito | Come raggiungere |
|-----------|-------------|---------------|
| **1.1.1 Contenuti non testuali** | Tutte le immagini hanno alternative di testo |  Attributi `alt`; `aria-label`per icone |
| **1.3.1 Informazioni e relazioni** | Struttura trasmessa a livello di codice | HTML semantico; intestazioni; elenchi; punti di riferimento |
| **1.4.3 Contrasto (minimo)** | Il testo ha un rapporto di contrasto di almeno 4,5:1 | Prova con pedine a contrasto; scegli tavolozze di colori accessibili |
| **1.4.4 Ridimensionare il testo** | Il testo può essere ridimensionato al 200% senza perdite | Utilizzare le unità relative (rem, em); design reattivo |
| **2.1.1 Tastiera** | Tutte le funzionalità disponibili tramite tastiera | Nessuna trappola per la tastiera; indicatori di messa a fuoco visibili |
| **2.4.3 Ordine del focus** | L'ordine del focus preserva significato e operabilità | Ordine di tabulazione logico; L'ordine DOM corrisponde all'ordine visivo |
| **2.4.7 Fuoco visibile** | Il focus della tastiera è indicato visivamente | Stili CSS `:focus-visible`; mai`outline: none`senza sostituzione |
| **3.3.2 Etichette o istruzioni** | Gli input hanno etichette |  Elementi `<label>`; `aria-label`|
| **4.1.2 Nome, ruolo, valore** | I componenti dell'interfaccia utente hanno nomi e ruoli accessibili | Attributi ARIA; HTML semantico |
---

## ARIA (Applicazioni Rich Internet accessibili)
ARIA aggiunge informazioni sull'accessibilità agli elementi HTML che non hanno una semantica incorporata.
### Ruoli di ARIA
| Ruolo | Scopo | Esempio |
|------|---------|---------|
| `button`| Identifica un elemento come pulsante | Un`<div>`disegnato come un pulsante |
| `dialog`| Dialogo modale o non modale | Componenti modali personalizzati |
| `tablist`/`tab`/`tabpanel`| Interfaccia a schede | Componenti della scheda personalizzata |
| `alert`| Messaggio importante che appare dinamicamente | Notifiche di errore |
| `progressbar`| Indicatore di progresso | Caricamento stati |
| `menu`/`menuitem`| Navigazione nel menu | Menù a tendina |
### Attributi ARIA
| Attributo | Scopo | Esempio |
|-----------|---------|---------|
| `aria-label`| Nome accessibile quando nessun testo visibile | Tasto solo icona:`aria-label="Search"`|
| `aria-describedby`| Collega l'elemento alla sua descrizione | Campo modulo con testo di aiuto |
| `aria-expanded`| Indica se una sezione viene espansa | Fisarmonica; discesa |
| `aria-hidden`| Nasconde l'elemento dalla tecnologia assistiva | Icone decorative |
| `aria-live`| Annuncia modifiche ai contenuti dinamici | Aggiornamenti in tempo reale; notifiche |
| `aria-disabled`| Indica che l'elemento è disabilitato | Pulsanti disattivati ​​|
### La Prima Regola di ARIA
> **Non utilizzare ARIA se puoi utilizzare invece HTML nativo.** Un`<button>`è già accessibile. Per`<div role="button">`è necessario aggiungere manualmente la gestione della tastiera, la gestione della messa a fuoco e il supporto dello screen reader. Utilizzare prima l'HTML semantico; ARIA solo quando gli elementi nativi non possono svolgere il lavoro.
---

## Navigazione tramite tastiera
| Chiave | Comportamento previsto |
|-----|-----|
| **Tab** | Sposta lo stato attivo sull'elemento interattivo successivo |
| **Maiusc+Tab** | Sposta lo stato attivo sull'elemento interattivo precedente |
| **Invio/Spazio** | Attiva l'elemento focalizzato (pulsante, collegamento) |
| **Tasti freccia** | Navigazione all'interno dei componenti (menu, schede, gruppi radio) |
| **Fuga** | Chiudere una finestra di dialogo, un menu o un popover |
| **Inizio / Fine** | Passa al primo/ultimo elemento dell'elenco |
### Trappole comuni per la tastiera
| Problema | Correzione |
|---------|-----|
| Il focus entra in un componente ma non può uscire | Assicurati che la scheda sposti lo stato attivo; gestire la fuga |
| Il modale non intrappola il focus | Il focus dovrebbe scorrere all'interno del modale; torna al trigger alla chiusura |
| I componenti personalizzati non rispondono alla tastiera | Aggiungi gestori di tasti per Invio, Spazio, frecce |
---

## Colore e design visivo
| Linea guida | Requisito |
|-----------|-------------|
| **Rapporto di contrasto** | 4,5:1 per testo normale; 3:1 per testo grande (18pt+ o 14pt+ grassetto) |
| **Non fare affidamento solo sul colore** | Utilizza icone, testo o motivi oltre al colore |
| **Indicatori di messa a fuoco** | Sempre visibile; contrasto elevato; mai rimosso senza sostituzione |
| **Ridimensionamento del testo** | Il layout deve funzionare con uno zoom del 200% |
| **Reattivo** | Il contenuto deve essere ridisposto con una larghezza di 320 px (mobile) |
### Considerazioni sul daltonismo
| Digitare | Colori interessati | Suggerimento per la progettazione |
|------|-----------|------------|
| **Deuteranopia** | Rosso-verde (più comune) | Non usare il rosso/verde per trasmettere lo status; usa icone + colore |
| **Protanopia** | Rosso-verde | Come sopra |
| **Tritanopia** | Blu-giallo | Non utilizzare il blu/giallo come unico elemento di differenziazione |
---

## Testare l'accessibilità
| Metodo | Strumento | Cosa cattura |
|--------|------|----------------|
| **Scansione automatica** | ascia, Faro, ONDA | Testo alternativo mancante; problemi di contrasto; Errori ARIA |
| **Test della tastiera** | Manuale: scollegare il mouse, utilizzare solo la tastiera | Ordine di messa a fuoco; trappole per tastiera; gestori mancanti |
| **Test del lettore di schermo** | NVDA (gratuito), VoiceOver (macOS), JAWS | Etichette mancanti; struttura scadente; modifiche senza preavviso |
| **Test zoom** | Zoom del browser al 200%, 400% | Rottura del layout; testo ritagliato; problemi di overflow |
| **Contrasto di colore** | Controllo del contrasto WebAIM, plug-in Stark | Rapporti di contrasto insufficienti |
| **Test utente** | Test con utenti disabili | Barriere del mondo reale che gli strumenti automatizzati non riescono a superare |
---

## Requisiti legali
| Legge | Regione | Requisiti |
|-----|--------|-----|
| **ADA** (Legge sugli americani con disabilità) | Stati Uniti | I siti web degli alloggi pubblici devono essere accessibili |
| **Articolo 508** | USA (federale) | Le TIC degli uffici federali devono essere accessibili |
| **EAA** (Atto europeo sull'accessibilità) | UE (2025+) | Prodotti e servizi devono soddisfare i requisiti di accessibilità |
| **EN 301 549** | UE | Norma tecnica per l'accessibilità alle ICT |
| **ACA** (Legge canadese sull'accessibilità) | Canada | Industrie governative e regolamentate |
| **Legge sull'uguaglianza del 2010** | Regno Unito | I fornitori di servizi devono apportare adeguamenti ragionevoli |
---

## Accessibilità mobile
| Piattaforma | Linee guida | Strumenti chiave |
|----------|-----------|-----------|
| **iOS** | Linee guida per l'interfaccia umana di Apple (sezione Accessibilità) | voce fuori campo; Tipo dinamico; Controllo interruttori |
| **Android** | Linee guida sull'accessibilità Android | TalkBack; Cambia accesso; Seleziona per parlare |
| Preoccupazione mobile | Soluzione |
|---------------|----------|
| **Tocca obiettivi** | Minimo 44×44 punti (iOS) / 48×48 dp (Android) |
| **Supporto per lettori di schermo** | Descrizioni dei contenuti; etichette di accessibilità |
| **Sensibilità al movimento** | Rispetto`prefers-reduced-motion`; evitare animazioni a riproduzione automatica |
| **Ridimensionamento dinamico del testo** | Supporta le dimensioni dei caratteri del sistema; utilizzare unità di testo scalabili |
---

## Riepilogo
L’accessibilità è un principio di progettazione che dovrebbe informare ogni decisione fin dall’inizio, non una funzionalità aggiunta alla fine. Utilizza HTML semantico. Assicurati che la navigazione tramite tastiera funzioni. Mantenere un contrasto cromatico sufficiente. Fornire alternative testuali per contenuti non testuali. Testare con lettori di schermo e utenti disabili. Il risultato è un software che funziona meglio per tutti, compresi quelli con disabilità temporanee, limitazioni situazionali, dispositivi più vecchi, connessioni lente e i molti modi in cui l'utilizzo nel mondo reale differisce da un ambiente di sviluppo controllato.