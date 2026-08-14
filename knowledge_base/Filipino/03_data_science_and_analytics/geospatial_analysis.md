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
# Geospatial na Pagsusuri
Ang geospatial analysis ay ang proseso ng pagsusuri sa data na may bahaging heograpiko — mga coordinate, address, hangganan, o anumang data na nakatali sa isang lokasyon sa Earth. Sinasagot nito ang mga tanong tulad ng "nasaan ang aming mga customer?", "ano ang pinakamainam na ruta?", at "paano nagbabago ang paggamit ng lupa sa paglipas ng panahon?". Ang bawat dataset ay may spatial na dimensyon, at ang pag-unawa dito ay nagbubukas ng mga insight na napapalampas ng purong istatistikal na pagsusuri.
---

## Mga Pangunahing Konsepto
### Mga Coordinate System
| System | Paglalarawan | Use Case |
|--------|-------------|----------|
| **WGS 84 (EPSG:4326)** | Pandaigdigang pamantayan; latitude/longitude sa degrees | GPS; karamihan sa web mapping; GeoJSON |
| **Web Mercator (EPSG:3857)** | Projects globe papunta sa isang silindro; pinipihit ang lugar sa mga poste | Google Maps; Mapbox; karamihan sa mga serbisyo ng web tile |
| **UTM** (Universal Transverse Mercator) | Hinahati ang Earth sa 60 zone; nakabatay sa metro | Militar; pagsisiyasat; mataas na katumpakan lokal na gawain |
| **British National Grid (EPSG:27700)** | OSGB36 datum; nakabatay sa metro | Pagmamapa ng UK |
| **Mga lokal na projection** | Mga custom na projection para sa mga partikular na rehiyon | I-minimize ang distortion para sa isang partikular na lugar |
### Mga Uri ng Geometry
| Uri | Paglalarawan | Halimbawa |
|------|-------------|---------|
| **Punto** | Single coordinate | Isang restawran; isang sensor; isang customer |
| **LineString** | Inayos ang pagkakasunod-sunod ng mga puntos | Isang kalsada; isang ilog; isang ruta |
| **Polygon** | Nakasaradong hugis na may panloob na | Isang bansa; isang lawa; isang delivery zone |
| **MultiPoint** | Koleksyon ng mga puntos | Lahat ng bus stop sa isang lungsod |
| **MultiLineString** | Koleksyon ng mga linya | Lahat ng mga kalsada sa isang network |
| **MultiPolygon** | Koleksyon ng mga polygon | Isang arkipelago; isang bansang may mga isla |
| **GeometryCollection** | Mga pinaghalong uri | Isang bansa na may mga lungsod, kalsada, at ilog nito |
---

## Mga Format ng Data
| Format | Uri | Pangunahing Tampok |
|--------|------|-------------|
| **GeoJSON** | Text (JSON) | Nababasa ng tao; web-friendly; sumusuporta sa lahat ng uri ng geometry |
| **Shapefile** | Binary (maraming mga file) | Legacy na format mula sa ESRI; .shp + .shx + .dbf + .prj |
| **KML** | XML | Google Earth; sumusuporta sa 3D at oras |
| **Geopackage** | Nakabatay sa SQLite | Isang file; sumusuporta sa raster at vector; modernong pamantayan |
| **GeoParquet** | Columnar (Parquet) | Mahusay para sa malalaking dataset; isinasama sa mga tool sa data engineering |
| **WKT / WKB** | Teksto / Binary | Kilalang Teksto; Kilalang Binary; ginagamit para sa imbakan ng database |
| **MVT** | Binary | Mapbox Vector Tile; para sa paghahatid ng data ng mapa sa mga web client |
---

## Mga Spatial na Operasyon
### Mga Pangunahing Operasyon
| Operasyon | Paglalarawan | Halimbawa |
|-----------|-------------|---------|
| **Distansya** | Kalkulahin ang distansya sa pagitan ng mga geometries | "Hanapin ang lahat ng ospital sa loob ng 10 km" |
| **Buffer** | Lumikha ng polygon sa paligid ng isang geometry sa isang naibigay na distansya | "Ipakita ang 500m zone sa paligid ng isang paaralan" |
| **Kintersection** | Hanapin ang magkakapatong na lugar sa pagitan ng mga geometries | "Aling mga parsela ang nasa flood zone?" |
| **Union** | Pagsamahin ang mga geometries sa isang | "Pagsamahin ang lahat ng mga parsela ng lupa sa iisang rehiyon" |
| **Pagkakaiba** | Ibawas ang isang geometry mula sa isa pa | "Mabubuo na lugar hindi kasama ang mga protektadong zone" |
| **Naglalaman / Sa loob** | Subukan kung ang isang geometry ay nasa loob ng isa pang | "Sino ang mga customer sa loob ng delivery area na ito?" |
| **Pinakalapit na kapitbahay** | Hanapin ang pinakamalapit na geometry | "Ano ang pinakamalapit na istasyon ng bumbero?" |
| **Spatial na pagsali** | Sumali sa mga attribute batay sa spatial na relasyon | "Italaga ang bawat punto sa naglalaman ng census tract" |
### Spatial Indexing
| Uri ng Index | Paglalarawan | Use Case |
|-----------|-------------|----------|
| **R-tree** | Bounding-box hierarchy; pinakakaraniwan | PostGIS; SQLite; pangkalahatang layunin |
| **Quadtree** | Recursive subdivision sa mga quadrant | Point data; mga makina ng laro |
| **Geohash** | Hierarchical grid; nag-e-encode sa string | Paghahanap ng malapit; database sharding |
| **H3** (Uber) | Hexagonal hierarchical grid | Analytics; ride-sharing; unipormeng bins |
| **S2** (Google) | Cell-based hierarchy sa isang globo | Malaking spatial na pag-index |
---

## Mga Tool at Aklatan
| Tool / Library | Wika | Paglalarawan |
|--------------|----------|-------------|
| **PostGIS** | SQL (PostgreSQL) | Gold standard para sa spatial database; buong spatial SQL |
| **QGIS** | Desktop (Python/C++) | Libre, open-source na GIS; ecosystem ng plugin |
| **GeoPandas** | Python | Pandas + Shapely + Fiona; spatial na DataFrames |
| **Maganda** | Python | Mga operasyon ng geometry; batay sa GEOS |
| **Folium** | Python | Interactive Leaflet na mapa mula sa Python |
| **Turf.js** | JavaScript | Client-side geospatial analysis |
| **Deck.gl** | JavaScript | Malaking sukat na visualization ng data sa mga mapa |
| **GDAL** | C++ (na may Python bindings) | Pagsasalin ng data ng raster at vector; ang Swiss army knife |
| **Rasterio** | Python | Basahin/isulat ang data ng raster; batay sa GDAL |
| **Kepler.gl** | JavaScript | Geospatial visualization na pinapagana ng WebGL |
---

## Mga Pattern ng Geospatial na Pagsusuri
### Mga Karaniwang Uri ng Pagsusuri
| Pattern | Paglalarawan | Use Case |
|---------|-------------|----------|
| **Pagsusuri ng pattern ng punto** | Suriin ang pamamahagi ng mga puntos | Pagmamapa ng krimen; pagtuklas ng pagsiklab ng sakit |
| **Pagsusuri ng Hotspot** | Maghanap ng mga kumpol na makabuluhang istatistika | lokasyon ng tingi; krimen; epidemiology |
| **Pagsusuri sa network** | Pag-optimize ng ruta; mga lugar ng serbisyo | Logistics; tugon sa emerhensiya; mga kagamitan |
| **Spatial interpolation** | Tantyahin ang mga halaga sa mga hindi naka-sample na lokasyon | Kalidad ng hangin; mga katangian ng lupa; panahon |
| **Pagtukoy ng pagbabago sa paggamit ng lupa** | Ikumpara ang satellite imagery sa paglipas ng panahon | Urban sprawl; deforestation; agrikultura |
| **Pagsusuri sa pagiging angkop** | Maghanap ng mga lokasyon na nakakatugon sa maraming pamantayan | Pagpili ng site; pagpaplano ng konserbasyon |
| **Spatial na autocorrelation** | Sukatin kung paano nauugnay ang mga kalapit na halaga | Mga presyo ng ari-arian; pagkalat ng sakit |
### The Modifiable Areal Unit Problem (MAUP)
| Aspeto | Problema |
|--------|---------|
| **Epekto ng scale** | Nagbabago ang mga resulta depende sa laki ng mga yunit ng pagsusuri (mga census tract kumpara sa mga county kumpara sa mga estado) |
| **Epekto ng zoning** | Nagbabago ang mga resulta depende sa kung paano iguguhit ang mga hangganan, kahit na sa parehong sukat |
| **Implikasyon** | Huwag ipagpalagay na ang mga resulta sa isang antas ng pagsasama-sama ay nalalapat sa isa pa; palaging subukan ang sensitivity sa mga hangganan |
---

## Mga Praktikal na Pagsasaalang-alang
| Pag-aalala | Patnubay |
|---------|----------|
| **Coordinate reference system** | Palaging suriin ang CRS; huwag kailanman paghaluin ang mga projection sa mga kalkulasyon; mag-transform bago mag-compute ng mga distansya |
| **Katumpakan** | Ang katumpakan ng floating-point ay mahalaga sa maliliit na kaliskis; gumamit ng naaangkop na mga uri ng data |
| **Pagganap** | Ang mga spatial na operasyon ay mahal; gumamit ng spatial index; pasimplehin ang mga geometries para sa pagpapakita |
| **Topology** | Tiyaking wasto ang mga geometry (walang mga intersection sa sarili, mga saradong polygon) bago ang pagsusuri |
| **Scale** | Binabaluktot ng Web Mercator ang lugar; huwag gamitin ito para sa mga kalkulasyon ng lugar |
| **Kalidad ng data** | Suriin ang mga null geometries, duplicate na vertices, sliver polygons |
---

## Buod
Ginagawa ng geospatial analysis ang data ng lokasyon sa naaaksyunan na insight. Ang mga punto, linya, at polygon ay kumakatawan sa mga real-world na entity. Ang mga spatial na operasyon — distansya, buffer, intersection, pagsali — sagutin ang mga tanong tungkol sa lapit, overlap, at containment. Ang mga tool ay mula sa PostGIS para sa database-scale analysis hanggang sa GeoPandas para sa mga workflow ng Python hanggang sa Deck.gl para sa web visualization. Ang mga pangunahing hamon ay ang pagpili ng tamang coordinate system, pamamahala ng performance gamit ang malalaking dataset, at pagiging kamalayan sa MAUP — ang katotohanang ang pagpili mo ng mga hangganan ng pagsasama-sama ay nakakaapekto sa iyong mga resulta. Kung nag-o-optimize ka man ng mga ruta ng paghahatid, nagsusuri ng pagkalat ng sakit, o nagma-map sa paglago ng urban, ang geospatial analysis ay nagbibigay ng spatial na konteksto na hindi makuha ng mga pure number.