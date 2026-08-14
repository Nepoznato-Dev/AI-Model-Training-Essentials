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
# Geospatial Analysis

Geospatial analysis is the process of examining data that has a geographic component — coordinates, addresses, boundaries, or any data tied to a location on Earth. It answers questions like "where are our customers?", "what's the optimal route?", and "how is land use changing over time?". Every dataset has a spatial dimension, and understanding it unlocks insights that pure statistical analysis misses.

---

## Core Concepts

### Coordinate Systems

| System | Description | Use Case |
|--------|-------------|----------|
| **WGS 84 (EPSG:4326)** | Global standard; latitude/longitude in degrees | GPS; most web mapping; GeoJSON |
| **Web Mercator (EPSG:3857)** | Projects globe onto a cylinder; distorts area at poles | Google Maps; Mapbox; most web tile services |
| **UTM** (Universal Transverse Mercator) | Divides Earth into 60 zones; metres-based | Military; surveying; high-precision local work |
| **British National Grid (EPSG:27700)** | OSGB36 datum; metres-based | UK mapping |
| **Local projections** | Custom projections for specific regions | Minimise distortion for a particular area |

### Geometry Types

| Type | Description | Example |
|------|-------------|---------|
| **Point** | Single coordinate | A restaurant; a sensor; a customer |
| **LineString** | Ordered sequence of points | A road; a river; a route |
| **Polygon** | Closed shape with interior | A country; a lake; a delivery zone |
| **MultiPoint** | Collection of points | All bus stops in a city |
| **MultiLineString** | Collection of lines | All roads in a network |
| **MultiPolygon** | Collection of polygons | An archipelago; a country with islands |
| **GeometryCollection** | Mixed types | A country with its cities, roads, and rivers |

---

## Data Formats

| Format | Type | Key Feature |
|--------|------|-------------|
| **GeoJSON** | Text (JSON) | Human-readable; web-friendly; supports all geometry types |
| **Shapefile** | Binary (multiple files) | Legacy format from ESRI; .shp + .shx + .dbf + .prj |
| **KML** | XML | Google Earth; supports 3D and time |
| **Geopackage** | SQLite-based | Single file; supports raster and vector; modern standard |
| **GeoParquet** | Columnar (Parquet) | Efficient for large datasets; integrates with data engineering tools |
| **WKT / WKB** | Text / Binary | Well-Known Text; Well-Known Binary; used for database storage |
| **MVT** | Binary | Mapbox Vector Tiles; for serving map data to web clients |

---

## Spatial Operations

### Fundamental Operations

| Operation | Description | Example |
|-----------|-------------|---------|
| **Distance** | Calculate distance between geometries | "Find all hospitals within 10 km" |
| **Buffer** | Create a polygon around a geometry at a given distance | "Show the 500m zone around a school" |
| **Intersection** | Find the overlapping area between geometries | "Which parcels are in the flood zone?" |
| **Union** | Merge geometries into one | "Combine all land parcels into a single region" |
| **Difference** | Subtract one geometry from another | "Buildable area excluding protected zones" |
| **Contains / Within** | Test if one geometry is inside another | "Which customers are within this delivery area?" |
| **Nearest neighbour** | Find the closest geometry | "What's the nearest fire station?" |
| **Spatial join** | Join attributes based on spatial relationship | "Assign each point to its containing census tract" |

### Spatial Indexing

| Index Type | Description | Use Case |
|-----------|-------------|----------|
| **R-tree** | Bounding-box hierarchy; most common | PostGIS; SQLite; general-purpose |
| **Quadtree** | Recursive subdivision into quadrants | Point data; game engines |
| **Geohash** | Hierarchical grid; encodes to string | Proximity search; database sharding |
| **H3** (Uber) | Hexagonal hierarchical grid | Analytics; ride-sharing; uniform bins |
| **S2** (Google) | Cell-based hierarchy on a sphere | Large-scale spatial indexing |

---

## Tools and Libraries

| Tool / Library | Language | Description |
|---------------|----------|-------------|
| **PostGIS** | SQL (PostgreSQL) | Gold standard for spatial databases; full spatial SQL |
| **QGIS** | Desktop (Python/C++) | Free, open-source GIS; plugin ecosystem |
| **GeoPandas** | Python | Pandas + Shapely + Fiona; spatial DataFrames |
| **Shapely** | Python | Geometry operations; based on GEOS |
| **Folium** | Python | Interactive Leaflet maps from Python |
| **Turf.js** | JavaScript | Client-side geospatial analysis |
| **Deck.gl** | JavaScript | Large-scale data visualisation on maps |
| **GDAL** | C++ (with Python bindings) | Raster and vector data translation; the Swiss army knife |
| **Rasterio** | Python | Read/write raster data; based on GDAL |
| **Kepler.gl** | JavaScript | WebGL-powered geospatial visualisation |

---

## Geospatial Analysis Patterns

### Common Analysis Types

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Point pattern analysis** | Examine distribution of points | Crime mapping; disease outbreak detection |
| **Hotspot analysis** | Find statistically significant clusters | Retail location; crime; epidemiology |
| **Network analysis** | Route optimisation; service areas | Logistics; emergency response; utilities |
| **Spatial interpolation** | Estimate values at unsampled locations | Air quality; soil properties; weather |
| **Land use change detection** | Compare satellite imagery over time | Urban sprawl; deforestation; agriculture |
| **Suitability analysis** | Find locations meeting multiple criteria | Site selection; conservation planning |
| **Spatial autocorrelation** | Measure how nearby values are related | Property prices; disease spread |

### The Modifiable Areal Unit Problem (MAUP)

| Aspect | Problem |
|--------|---------|
| **Scale effect** | Results change depending on the size of the analysis units (census tracts vs counties vs states) |
| **Zoning effect** | Results change depending on how boundaries are drawn, even at the same scale |
| **Implication** | Never assume that results at one aggregation level apply at another; always test sensitivity to boundaries |

---

## Practical Considerations

| Concern | Guidance |
|---------|----------|
| **Coordinate reference systems** | Always check the CRS; never mix projections in calculations; transform before computing distances |
| **Precision** | Floating-point precision matters at small scales; use appropriate data types |
| **Performance** | Spatial operations are expensive; use spatial indexes; simplify geometries for display |
| **Topology** | Ensure geometries are valid (no self-intersections, closed polygons) before analysis |
| **Scale** | Web Mercator distorts area; don't use it for area calculations |
| **Data quality** | Check for null geometries, duplicate vertices, sliver polygons |

---

## Summary

Geospatial analysis turns location data into actionable insight. Points, lines, and polygons represent real-world entities. Spatial operations — distance, buffer, intersection, join — answer questions about proximity, overlap, and containment. Tools range from PostGIS for database-scale analysis to GeoPandas for Python workflows to Deck.gl for web visualisation. The key challenges are choosing the right coordinate system, managing performance with large datasets, and being aware of MAUP — the fact that your choice of aggregation boundaries affects your results. Whether you're optimising delivery routes, analysing disease spread, or mapping urban growth, geospatial analysis provides the spatial context that pure numbers can't capture.
