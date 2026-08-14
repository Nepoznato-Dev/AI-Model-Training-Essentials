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
# Geodatenanalyse
Bei der Geodatenanalyse werden Daten untersucht, die eine geografische Komponente haben – Koordinaten, Adressen, Grenzen oder andere Daten, die mit einem Standort auf der Erde verknüpft sind. Es beantwortet Fragen wie „Wo sind unsere Kunden?“, „Was ist die optimale Route?“ und „Wie verändert sich die Landnutzung im Laufe der Zeit?“. Jeder Datensatz hat eine räumliche Dimension, und wenn man diese versteht, erhält man Einblicke, die der reinen statistischen Analyse entgehen.
---

## Kernkonzepte
### Koordinatensysteme
| System | Beschreibung | Anwendungsfall |
|--------|-------------|----------|
| **WGS 84 (EPSG:4326)** | Globaler Standard; Breiten-/Längengrad in Grad | GPS; die meisten Web-Mappings; GeoJSON |
| **Web Mercator (EPSG:3857)** | Projiziert einen Globus auf einen Zylinder; verzerrt den Bereich an den Polen | Google Maps; Kartenbox; die meisten Web-Kachel-Dienste |
| **UTM** (Universal Transverse Mercator) | Teilt die Erde in 60 Zonen; Meterbasiert | Militär; Vermessung; hochpräzise lokale Arbeit |
| **British National Grid (EPSG:27700)** | OSGB36-Datum; Meterbasiert | UK-Kartierung |
| **Lokale Prognosen** | Benutzerdefinierte Projektionen für bestimmte Regionen | Verzerrung für einen bestimmten Bereich minimieren |
### Geometrietypen
| Geben Sie | ein Beschreibung | Beispiel |
|------|-------------|---------|
| **Punkt** | Einzelne Koordinate | Ein Restaurant; ein Sensor; ein Kunde |
| **LineString** | Geordnete Folge von Punkten | Eine Straße; ein Fluss; eine Route |
| **Polygon** | Geschlossene Form mit Innenraum | Ein Land; ein See; eine Lieferzone |
| **MultiPoint** | Punkte sammeln | Alle Bushaltestellen in einer Stadt |
| **MultiLineString** | Sammlung von Linien | Alle Straßen in einem Netzwerk |
| **MultiPolygon** | Sammlung von Polygonen | Ein Archipel; ein Land mit Inseln |
| **GeometryCollection** | Gemischte Typen | Ein Land mit seinen Städten, Straßen und Flüssen |
---

## Datenformate
| Formatieren | Geben Sie | ein Hauptmerkmal |
|--------|------|-------------|
| **GeoJSON** | Text (JSON) | Für Menschen lesbar; webfreundlich; unterstützt alle Geometrietypen |
| **Shapefile** | Binär (mehrere Dateien) | Legacy-Format von ESRI; .shp + .shx + .dbf + .prj |
| **KML** | XML | Google Earth; unterstützt 3D und Zeit |
| **Geopaket** | SQLite-basiert | Einzeldatei; unterstützt Raster und Vektor; moderner Standard |
| **GeoParkett** | Säulenförmig (Parkett) | Effizient für große Datensätze; lässt sich in Data-Engineering-Tools integrieren |
| **WKT / WKB** | Text / Binär | Bekannter Text; Bekannte Binärdatei; wird für die Datenbankspeicherung verwendet |
| **MVT** | Binär | Mapbox-Vektorkacheln; zur Bereitstellung von Kartendaten für Web-Clients |
---

## Raumoperationen
### Grundlegende Operationen
| Betrieb | Beschreibung | Beispiel |
|-----------|-------------|---------|
| **Entfernung** | Abstand zwischen Geometrien berechnen | „Alle Krankenhäuser im Umkreis von 10 km finden“ |
| **Puffer** | Erstellen Sie ein Polygon um eine Geometrie in einem bestimmten Abstand | „Zeigt die 500m-Zone um eine Schule“ |
| **Kreuzung** | Finden Sie den überlappenden Bereich zwischen Geometrien | „Welche Parzellen liegen im Überschwemmungsgebiet?“ |
| **Union** | Geometrien zu einer zusammenführen | „Alle Grundstücke zu einer einzigen Region zusammenfassen“ |
| **Unterschied** | Subtrahiere eine Geometrie von einer anderen | „Bebaubare Fläche ohne Schutzgebiete“ |
| **Enthält / Innerhalb** | Testen Sie, ob sich eine Geometrie in einer anderen befindet | „Welche Kunden befinden sich in diesem Liefergebiet?“ |
| **Nächster Nachbar** | Finden Sie die nächstgelegene Geometrie | „Was ist die nächste Feuerwache?“ |
| **Räumliche Verbindung** | Attribute basierend auf räumlicher Beziehung verbinden | „Weisen Sie jeden Punkt dem zugehörigen Zählbezirk zu“ |
### Räumliche Indizierung
| Indextyp | Beschreibung | Anwendungsfall |
|-----------|-------------|----------|
| **R-Baum** | Bounding-Box-Hierarchie; am häufigsten | PostGIS; SQLite; Allzweck |
| **Quadtree** | Rekursive Unterteilung in Quadranten | Punktdaten; Spiel-Engines |
| **Geohash** | Hierarchisches Raster; kodiert in Zeichenfolge | Umgebungssuche; Datenbank-Sharding |
| **H3** (Uber) | Sechseckiges hierarchisches Gitter | Analytik; Mitfahrgelegenheit; einheitliche Behälter |
| **S2** (Google) | Zellbasierte Hierarchie auf einer Kugel | Großräumige räumliche Indizierung |
---

## Tools und Bibliotheken
| Werkzeug / Bibliothek | Sprache | Beschreibung |
|---------------|----------|-------------|
| **PostGIS** | SQL (PostgreSQL) | Goldstandard für räumliche Datenbanken; vollständiges räumliches SQL |
| **QGIS** | Desktop (Python/C++) | Kostenloses Open-Source-GIS; Plugin-Ökosystem |
| **GeoPandas** | Python | Pandas + Shapely + Fiona; räumliche DataFrames |
| **Formschön** | Python | Geometrieoperationen; basierend auf GEOS |
| **Folien** | Python | Interaktive Leaflet-Karten von Python |
| **Turf.js** | JavaScript | Kundenseitige Geodatenanalyse |
| **Deck.gl** | JavaScript | Großflächige Datenvisualisierung auf Karten |
| **GDAL** | C++ (mit Python-Bindungen) | Übersetzung von Raster- und Vektordaten; das Schweizer Taschenmesser |
| **Rasterio** | Python | Rasterdaten lesen/schreiben; basierend auf GDAL |
| **Kepler.gl** | JavaScript | WebGL-gestützte Geodatenvisualisierung |
---

## Geodatenanalysemuster
### Gängige Analysetypen
| Muster | Beschreibung | Anwendungsfall |
|---------|-------------|----------|
| **Punktmusteranalyse** | Punkteverteilung untersuchen | Kriminalitätskartierung; Erkennung von Krankheitsausbrüchen |
| **Hotspot-Analyse** | Finden Sie statistisch signifikante Cluster | Einzelhandelsstandort; Verbrechen; Epidemiologie |
| **Netzwerkanalyse** | Routenoptimierung; Servicebereiche | Logistik; Notfallreaktion; Versorgungsunternehmen |
| **Räumliche Interpolation** | Schätzwerte an nicht beprobten Standorten | Luftqualität; Bodeneigenschaften; Wetter |
| **Erkennung von Landnutzungsänderungen** | Vergleichen Sie Satellitenbilder im Zeitverlauf | Zersiedelung; Abholzung; Landwirtschaft |
| **Eignungsanalyse** | Finden Sie Standorte, die mehrere Kriterien erfüllen | Standortauswahl; Naturschutzplanung |
| **Räumliche Autokorrelation** | Messen Sie, wie benachbarte Werte zusammenhängen | Immobilienpreise; Krankheitsausbreitung |
### Das Problem der modifizierbaren Flächeneinheiten (MAUP)
| Aspekt | Problem |
|--------|---------|
| **Skaleneffekt** | Die Ergebnisse ändern sich je nach Größe der Analyseeinheiten (Volkszählungsbezirke vs. Landkreise vs. Bundesstaaten) |
| **Zoneneffekt** | Die Ergebnisse ändern sich je nachdem, wie die Grenzen gezogen werden, auch im gleichen Maßstab |
| **Implikation** | Gehen Sie niemals davon aus, dass Ergebnisse auf einer Aggregationsebene auch auf einer anderen zutreffen; Testen Sie immer die Sensibilität für Grenzen |
---

## Praktische Überlegungen
| Sorge | Anleitung |
|---------|----------|
| **Koordinatenreferenzsysteme** | Überprüfen Sie immer das CRS; Mischen Sie niemals Prognosen in Berechnungen. transformieren, bevor Entfernungen berechnet werden |
| **Präzision** | Gleitkomma-Präzision ist in kleinen Maßstäben wichtig; Verwenden Sie geeignete Datentypen |
| **Leistung** | Weltraumoperationen sind teuer; räumliche Indizes verwenden; Vereinfachen Sie Geometrien für die Anzeige |
| **Topologie** | Stellen Sie vor der Analyse sicher, dass die Geometrien gültig sind (keine Selbstüberschneidungen, geschlossene Polygone).
| **Maßstab** | Web Mercator verzerrt den Bereich; nicht für Flächenberechnungen verwenden |
| **Datenqualität** | Auf Nullgeometrien, doppelte Scheitelpunkte und Splitterpolygone prüfen |
---

## Zusammenfassung
Geodatenanalysen verwandeln Standortdaten in umsetzbare Erkenntnisse. Punkte, Linien und Polygone repräsentieren Objekte der realen Welt. Räumliche Operationen – Abstand, Puffer, Schnittpunkt, Verbindung – beantworten Fragen zu Nähe, Überlappung und Eindämmung. Die Tools reichen von PostGIS für die Analyse im Datenbankmaßstab über GeoPandas für Python-Workflows bis hin zu Deck.gl für die Webvisualisierung. Die größten Herausforderungen bestehen darin, das richtige Koordinatensystem auszuwählen, die Leistung bei großen Datensätzen zu verwalten und sich des MAUP bewusst zu sein – der Tatsache, dass Ihre Wahl der Aggregationsgrenzen Ihre Ergebnisse beeinflusst. Ganz gleich, ob Sie Lieferrouten optimieren, die Ausbreitung von Krankheiten analysieren oder das Stadtwachstum kartieren, Geodatenanalysen liefern den räumlichen Kontext, den reine Zahlen nicht erfassen können.