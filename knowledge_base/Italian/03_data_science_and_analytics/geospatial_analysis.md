<!--
---
# Metadata
title: "Geospatial Analysis"
description: "Coordinate systems, spatial operations, GeoPandas, raster analysis"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [geospatial, analysis, data-science-and-analytics]
difficulty_level: "intermediate"
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
# Analisi geospaziale
L'analisi geospaziale è il processo di esame dei dati che hanno una componente geografica: coordinate, indirizzi, confini o qualsiasi dato legato a una posizione sulla Terra. Risponde a domande come "dove sono i nostri clienti?", "qual è il percorso ottimale?" e "come cambia l'uso del territorio nel tempo?". Ogni set di dati ha una dimensione spaziale e la sua comprensione fornisce informazioni che la pura analisi statistica non riesce a cogliere.
---

## Concetti fondamentali
### Sistemi di coordinate
| Sistema | Descrizione | Caso d'uso |
|--------|-------------|----------|
| **WGS84 (EPSG:4326)** | Norma globale; latitudine/longitudine in gradi | GPS; la maggior parte della mappatura web; GeoJSON |
| **Web Mercatore (EPSG:3857)** | Proietta il globo su un cilindro; distorce l'area ai poli | Google Maps; casella di mappa; la maggior parte dei servizi di piastrelle Web |
| **UTM** (Universale Trasversa di Mercatore) | Divide la Terra in 60 zone; basato sui metri | Militare; rilevamento; lavoro locale di alta precisione |
| **Griglia nazionale britannica (EPSG:27700)** | Dato OSGB36; basato sui metri | Mappatura del Regno Unito |
| **Proiezioni locali** | Proiezioni personalizzate per regioni specifiche | Ridurre al minimo la distorsione per un'area particolare |
### Tipi di geometria
| Digitare | Descrizione | Esempio |
|------|-------------|---------|
| **Punto** | Coordinata singola | Un ristorante; un sensore; un cliente |
| **LineString** | Sequenza ordinata di punti | Una strada; un fiume; un percorso |
| **Poligono** | Forma chiusa con interno | Un paese; un lago; una zona di consegna |
| **Multipunto** | Raccolta punti | Tutte le fermate dell'autobus in una città |
| **MultiLineString** | Raccolta di linee | Tutte le strade di una rete |
| **Multipoligono** | Raccolta di poligoni | Un arcipelago; un paese con isole |
| **Collezione Geometria** | Tipi misti | Un paese con le sue città, strade e fiumi |
---

## Formati di dati
| Formato | Digitare | Caratteristica fondamentale |
|--------|------|-----|
| **GeoJSON** | Testo (JSON) | Leggibile dall'uomo; web-friendly; supporta tutti i tipi di geometria |
| **Shapefile** | Binario (file multipli) | Formato legacy da ESRI; .shp + .shx + .dbf + .prj |
| **KML** | XML | Google Terra; supporta 3D e tempo |
| **Pacchetto geografico** | Basato su SQLite | File singolo; supporta raster e vettoriale; standard moderno |
| **GeoParquet** | Colonnare (Parquet) | Efficiente per set di dati di grandi dimensioni; si integra con strumenti di ingegneria dei dati |
| **WKT/WKB** | Testo/Binario | Testo ben noto; Binario ben noto; utilizzato per l'archiviazione del database |
| **MVT** | Binario | Piastrelle vettoriali Mapbox; per fornire dati cartografici ai client Web |
---

## Operazioni spaziali
### Operazioni fondamentali
| Operazione | Descrizione | Esempio |
|-----------|-------------|---------|
| **Distanza** | Calcolare la distanza tra le geometrie | "Trova tutti gli ospedali nel raggio di 10 km" |
| **Buffer** | Crea un poligono attorno ad una geometria ad una data distanza | "Mostra la zona di 500 m intorno a una scuola" |
| **Intersezione** | Trova l'area di sovrapposizione tra le geometrie | "Quali pacchi si trovano nella zona alluvionale?" |
| **Unione** | Unisci le geometrie in una | "Unire tutte le parcelle fondiarie in un'unica regione" |
| **Differenza** | Sottrarre una geometria da un'altra | "Superficie edificabile escluse le zone protette" |
| **Contiene/All'interno** | Verifica se una geometria è all'interno di un'altra | "Quali clienti si trovano in questa zona di consegna?" |
| **Il vicino più vicino** | Trova la geometria più vicina | "Qual è la stazione dei vigili del fuoco più vicina?" |
| **Unione spaziale** | Unisci gli attributi in base alla relazione spaziale | "Assegna ogni punto al tratto di censimento che lo contiene" |
### Indicizzazione spaziale
| Tipo indice | Descrizione | Caso d'uso |
|-----------|-------------|----------|
| **R-albero** | Gerarchia del riquadro di delimitazione; più comune | PostGIS; SQLite; uso generale |
| **Quadalbero** | Suddivisione ricorsiva in quadranti | Dati puntuali; motori di gioco |
| **Geohash** | Griglia gerarchica; codifica in stringa | Ricerca di prossimità; partizionamento del database |
| **H3** (Uber) | Griglia gerarchica esagonale | Analitica; condivisione del viaggio; contenitori uniformi |
| **S2** (Google) | Gerarchia basata su celle su una sfera | Indicizzazione spaziale su larga scala |
---

## Strumenti e librerie
| Strumento/Libreria | Lingua | Descrizione |
|---------------|----------|-------------|
| **PostGIS** | SQL (PostgreSQL) | Gold standard per i database spaziali; SQL spaziale completo |
| **QGIS** | Desktop (Python/C++) | GIS gratuito e open source; Ecosistema di plug-in |
| **GeoPanda** | Pitone | Panda + Formosa + Fiona; DataFram spaziali |
| **Formosa** | Pitone | Operazioni di geometria; basato su GEOS |
| **Foglio** | Pitone | Mappe di volantini interattivi da Python |
| **Turf.js** | JavaScript | Analisi geospaziale lato client |
| **Mazzo.gl** | JavaScript | Visualizzazione di dati su larga scala su mappe |
| **GDAL** | C++ (con collegamenti Python) | Traduzione di dati raster e vettoriali; il coltellino svizzero |
| **Rasterio** | Pitone | Leggere/scrivere dati raster; basato su GDAL |
| **Kepler.gl** | JavaScript | Visualizzazione geospaziale basata su WebGL |
---

## Modelli di analisi geospaziale
### Tipi di analisi comuni
| Modello | Descrizione | Caso d'uso |
|---------|-------------|----------|
| **Analisi del modello di punti** | Esaminare la distribuzione dei punti | Mappatura del crimine; rilevamento di epidemie |
| **Analisi hotspot** | Trova cluster statisticamente significativi | Luogo di vendita al dettaglio; crimine; epidemiologia |
| **Analisi della rete** | Ottimizzazione del percorso; aree di servizio | Logistica; risposta alle emergenze; utilità |
| **Interpolazione spaziale** | Valori stimati in località non campionate | Qualità dell'aria; proprietà del suolo; tempo |
| **Rilevamento dei cambiamenti nell'uso del territorio** | Confronta le immagini satellitari nel tempo | Espansione urbana; deforestazione; agricoltura |
| **Analisi di idoneità** | Trova località che soddisfano più criteri | Selezione del sito; pianificazione della conservazione |
| **Autocorrelazione spaziale** | Misura la relazione tra i valori vicini | Prezzi degli immobili; diffusione della malattia |
### Il problema dell'unità areale modificabile (MAUP)
| Aspetto | Problema |
|--------|---------|
| **Effetto scala** | I risultati cambiano a seconda della dimensione delle unità di analisi (tratti censuari vs contee vs stati) |
| **Effetto zonizzazione** | I risultati cambiano a seconda di come vengono tracciati i confini, anche alla stessa scala |
| **Implicazione** | Non dare mai per scontato che i risultati a un livello di aggregazione si applichino a un altro; testare sempre la sensibilità ai confini |
---

## Considerazioni pratiche
| Preoccupazione | Guida |
|---------|----------|
| **Sistemi di riferimento di coordinate** | Controlla sempre il CRS; non mescolare mai le proiezioni nei calcoli; trasformare prima di calcolare le distanze |
| **Precisione** | La precisione in virgola mobile è importante su piccola scala; utilizzare tipi di dati appropriati |
| **Prestazioni** | Le operazioni spaziali sono costose; utilizzare indici spaziali; semplificare le geometrie per la visualizzazione |
| **Topologia** | Assicurarsi che le geometrie siano valide (nessuna autointersezione, poligoni chiusi) prima dell'analisi |
| **Scala** | Web Mercator distorce l'area; non usarlo per i calcoli dell'area |
| **Qualità dei dati** | Verifica la presenza di geometrie nulle, vertici duplicati, poligoni scheggiati |
---

## Riepilogo
L'analisi geospaziale trasforma i dati sulla posizione in informazioni utili. Punti, linee e poligoni rappresentano entità del mondo reale. Le operazioni spaziali (distanza, buffer, intersezione, unione) rispondono a domande su prossimità, sovrapposizione e contenimento. Gli strumenti spaziano da PostGIS per l'analisi su scala di database a GeoPandas per flussi di lavoro Python a Deck.gl per la visualizzazione web. Le sfide principali sono la scelta del giusto sistema di coordinate, la gestione delle prestazioni con set di dati di grandi dimensioni e la consapevolezza del MAUP: il fatto che la scelta dei confini di aggregazione influisce sui risultati. Che tu stia ottimizzando i percorsi di consegna, analizzando la diffusione delle malattie o mappando la crescita urbana, l'analisi geospaziale fornisce il contesto spaziale che i numeri puri non possono catturare.