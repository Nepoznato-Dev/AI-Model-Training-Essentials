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

# Scienza dei materiali
La scienza dei materiali è lo studio di come la struttura di un materiale (su scala atomica, microscopica e macroscopica) ne determina le proprietà e di come i metodi di lavorazione possono essere utilizzati per controllare tale struttura per ottenere le prestazioni desiderate. È il campo che risponde a domande come: perché l'acciaio è forte ma pesante? Perché il vetro è trasparente ma fragile? Come possiamo rendere le batterie che si caricano più velocemente? Quali materiali sopravviveranno alle condizioni su Marte? Ogni strumento tecnologico che hai utilizzato è fatto di materiali e i progressi tecnologici richiedono quasi sempre progressi nei materiali.
---

## Il tetraedro della scienza dei materiali
I quattro elementi interconnessi che definiscono il campo:
| Elemento | Descrizione |
|---------|-----|
| **Struttura** | Come sono disposti gli atomi e le molecole (struttura cristallina; bordi di grano; difetti) |
| **Immobili** | Come si comporta il materiale (meccanico; elettrico; termico; ottico; magnetico) |
| **Elaborazione** | Come viene realizzato e modellato il materiale (colata; sinterizzazione; drogaggio; ricottura) |
| **Prestazioni** | Come funziona il materiale in un'applicazione reale |
L'intuizione chiave: cambiando l'elaborazione cambia la struttura, che cambia le proprietà, che cambia le prestazioni.
---

## Classi di materiali
### Panoramica
| Classe | Incollaggio | Proprietà chiave | Esempi |
|-------|---------|------|---------|
| **Metalli** | Metallici (elettroni delocalizzati) | Forte; duttile; conduttivo; opaco | Acciaio; alluminio; rame; titanio |
| **Ceramica** | Ionico/covalente | Difficile; fragile; resistente al calore; isolante | Allumina; carburo di silicio; bicchiere; porcellana |
| **Polimeri** | Covalenti (catene) + van der Waals | Leggero; flessibile; isolante; basso punto di fusione | polietilene; nylon; gomma; epossidico |
| **Compositi** | Combinazione di due o più classi | Immobili su misura; elevata resistenza/peso | Fibra di carbonio; fibra di vetro; calcestruzzo |
| **Semiconduttori** | Covalente (con impurezze controllate) | Conduttività sintonizzabile; base dell'elettronica | Silicio; germanio; Arseniuro di gallio |
| **Biomateriali** | Vari; biocompatibile richiesto | Interagire con i sistemi biologici | Impianti in titanio; collagene; idrossiapatite |
---

## Strutture cristalline
### Strutture cristalline metalliche comuni
| Struttura | Atomi per cella unitaria | Frazione di imballaggio | Esempi |
|-----------|---------------------------|-----------------|---------|
| **FCC** (cubico centrato sulla faccia) | 4| 0,74 (imballato più vicino) | Alluminio; rame; oro; nichel; austenite (ferro γ) |
| **BCC** (Cubico centrato sul corpo) | 2| 0,68| Ferro (ferro α); cromo; tungsteno; molibdeno |
| **HCP** (esagonale compatto) | 6| 0,74 (imballato più vicino) | Titanio; zinco; magnesio; cobalto |
### Perché la struttura cristallina è importante
| Immobile | Influenza della struttura cristallina |
|----------|-------------------------------|
| **Forza** | I sistemi di scorrimento (piani lungo i quali scorrono gli atomi) differiscono per struttura; I metalli FCC sono più duttili degli HCP |
| **Densità** | La frazione di impaccamento determina quanto strettamente sono impaccati gli atomi |
| **Trasformazioni di fase** | Il ferro si trasforma da BCC a FCC a 912°C: questa è la base del trattamento termico dell'acciaio |
| **Anisotropia** | Le proprietà possono variare con la direzione nei cristalli non cubici |
---

## Proprietà meccaniche
### Metriche chiave
| Immobile | Definizione | Unità | Valori tipici |
|----------|-----------|-------|----------------|
| **Modulo di Young (E)** | Rigidità; sforzo/deformazione in regione elastica | GPa | Acciaio: 200; Alluminio: 70; Gomma: 0,01–0,1 |
| **Servo di snervamento** | Sollecitazione alla quale inizia la deformazione permanente (plastica) | MPa | Acciaio: 250–1000; Alluminio: 40–500 |
| **Resistenza alla trazione (UTS)** | Sollecitazione massima prima del cedimento | MPa | Acciaio: 400–2000; Alluminio: 90–600 |
| **Duttilità (% allungamento)** | Quanto si allunga un materiale prima di rompersi | % | Acciaio: 10–50; Vetro: <1 |
| **Resistenza** | Energia assorbita prima della frattura (area sottoposta alla curva sforzo-deformazione) | MJ/m³ | Acciaio: alto; ceramica: bassa |
| **Durezza** | Resistenza all'impronta superficiale | Varie scale | Diamante: il più duro; talco: più morbido |
### Meccanismi di rafforzamento
| Meccanismo | Come funziona | Esempio |
|-----------|-------------|---------|
| **Affinazione del grano** | Grani più piccoli = bordi dei grani più numerosi = più difficile spostare le dislocazioni | Relazione Hall-Petch |
| **Rafforzamento della soluzione solida** | Gli atomi estranei distorcono il reticolo; impedire il movimento della dislocazione | Aggiunta di zinco al rame → ottone |
| **Indurimento delle precipitazioni** | Piccole particelle bloccano il movimento della dislocazione | Leghe di alluminio invecchiate |
| **Incrudimento (incrudimento)** | La deformazione plastica aumenta la densità delle dislocazioni; si aggrovigliano e si ostacolano | Acciaio laminato a freddo |
| **Rinforzo composito** | Fibre resistenti in una matrice più morbida sopportano il carico | Polimero rinforzato con fibra di carbonio |
---

## Proprietà Elettriche e Termiche
### Conduttività elettrica
| Tipo materiale | Conducibilità (S/m) | Meccanismo |
|--------------|--------------------|-----------|
| **Conduttori** (rame, argento) | 10^7 – 10^8 | Elettroni liberi nei legami metallici |
| **Semiconduttori** (silicio, GaAs) | 10^-6 – 10^4 | Accordabile tramite doping; ingegneria del gap di banda |
| **Isolanti** (vetro, gomma) | 10^-12 – 10^-20 | Ampio gap di banda; elettroni legati |
| **Superconduttori** | Infinito (sotto la temperatura critica) | Resistenza elettrica nulla; Effetto Meissner |
### Proprietà termiche
| Immobile | Descrizione | Importante per |
|----------|-------------|---------------|
| **Conducibilità termica** | Quanto bene il calore fluisce attraverso il materiale | Dissipatori di calore; isolamento |
| **Espansione termica** | Quanto si espande un materiale quando viene riscaldato | Materiali abbinabili nei compositi; ponti; rotaie |
| **Capacità termica specifica** | Energia necessaria per aumentare la temperatura di 1°C | Accumulo di energia termica |
| **Punto di fusione** | Temperatura alla quale il solido diventa liquido | Applicazioni ad alta temperatura |
---

## Polimeri
### Tipi di polimeri
| Digitare | Struttura | Proprietà | Esempi |
|------|-----------|-----------|---------|
| **Termoplastici** | Catene lineari o ramificate; forze intermolecolari deboli | Sciogliere quando riscaldato; riciclabile | polietilene; polistirolo; nylon |
| **Termoindurenti** | Rete reticolata; legami covalenti tra catene | Non sciogliersi; decomporre ad alta temperatura | Epossidico; gomma vulcanizzata; Bachelite |
| **Elastomeri** | Leggermente reticolato; catene a spirale | Allunga e ritorna in forma | Gomma naturale; silicone; neoprene |
### Proprietà dei polimeri
| Immobile | Descrizione |
|----------|-------------|
| **Temperatura di transizione vetrosa (Tg)** | Sotto Tg: duro e fragile. Sopra Tg: morbido e flessibile |
| **Cristallinità** | I polimeri semicristallini sono più resistenti e più opachi; amorfi sono trasparenti |
| **Peso molecolare** | MW più alto = più forte; più difficile da elaborare |
| **Grado di polimerizzazione** | Numero di unità monomeriche; influisce sulle proprietà |
---

## Diagrammi di fase
### Diagramma di fase Ferro-Carbonio (semplificato)
| Fase | Contenuto di carbonio | Struttura | Proprietà |
|-------|---------------|-----------|-----------|
| **Ferrite (α)** | Fino allo 0,022% | Ferro BCC | Morbido; duttile; magnetico |
| **Austenite (γ)** | Fino al 2,14% | Ferro FCC | Non magnetico; formabile |
| **Cementite (Fe₃C)** | 6,67%| Ortorombico | Difficile; fragile |
| **Perlite** | 0,76% (eutettoide) | Strati alternati di ferrite e cementite | Forte; duro |
| **Martensite** | Qualsiasi (formato da tempra rapida) | BCT (tetragonale a corpo centrato) | Molto difficile; fragile |
---

## Materiali moderni ed emergenti
| Materiale | Descrizione | Applicazione |
|----------|-------------|-------------|
| **Grafene** | Singolo strato di atomi di carbonio; il materiale più resistente conosciuto; ottimo conduttore | Elettronica; compositi; sensori |
| **Nanotubi di carbonio** | Cilindri di grafene arrotolati; rapporto resistenza/peso estremo | compositi; elettronica; accumulo di energia |
| **Perovskiti** | Struttura cristallina ABX₃; band gap sintonizzabile | Celle solari; LED; rilevatori |
| **Strutture metallo-organiche (MOF)** | Materiali cristallini porosi; superficie enorme | Stoccaggio del gas; catalisi; consegna di farmaci |
| **Leghe a memoria di forma** | Ritorna alla forma originale quando riscaldato | Stent; attuatori; strutture autoriparanti |
| **Metamateriali** | La microstruttura ingegnerizzata conferisce proprietà non presenti in natura | Indice di rifrazione negativo; occultamento |
| **Leghe ad elevata entropia** | Elementi principali multipli; combinazioni insolite di proprietà | Ambienti estremi; aerospaziale |
---

## Riepilogo
La scienza dei materiali collega la struttura atomica di un materiale alle sue proprietà macroscopiche e alle prestazioni nel mondo reale. I metalli sono forti e conduttivi ma pesanti. La ceramica è dura e resistente al calore ma fragile. I polimeri sono leggeri e flessibili ma limitati dalla temperatura. I compositi combinano il meglio di classi diverse. La struttura cristallina determina il comportamento meccanico. La lavorazione (trattamento termico, lega, incrudimento) controlla la microstruttura e quindi le proprietà. Materiali moderni come grafene, perovskiti e MOF spingono i confini di ciò che è possibile. Il campo è fondamentalmente interdisciplinare: la fisica spiega i legami, la chimica spiega le reazioni, l’ingegneria spiega le prestazioni e tutto questo è importante per ogni tecnologia, dagli smartphone ai veicoli spaziali.