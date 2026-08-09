---
# Métadonnées
titre : "Analyse géospatiale"
description: "Systèmes de coordonnées, opérations spatiales, GeoPandas, analyse raster"
catégorie : "Science des données et analyse"
version : "1.0.0"
statut : "actif"
# Contribution
auteurs :
  - nom : « Équipe de formation des modèles IA »
    email: ""
    rôle : "original_author"
contributeurs : []
journal des modifications :
  - version : "1.0.0"
    date : "05/08/2026"
    auteur : « Équipe de formation des modèles IA »
    modifications : « Ajout des métadonnées de premier plan YAML pour le suivi des contributeurs »
# Révision
créé : "2026-08-05"
last_modified : "05/08/2026"
date_de_revue : "05/02/2027"
review_by : "Équipe de la base de connaissances sur la science des données et l'analyse"
next_review : "2027-08-05"
#Classement
Mots-clés : [géospatial, analyse, science des données et analytique]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "6 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Analyse géospatiale
L'analyse géospatiale est le processus d'examen des données comportant une composante géographique : coordonnées, adresses, limites ou toute donnée liée à un emplacement sur Terre. Il répond à des questions telles que « où sont nos clients ? », « quel est l'itinéraire optimal ? » et « comment l'utilisation des terres évolue-t-elle au fil du temps ? ». Chaque ensemble de données a une dimension spatiale, et sa compréhension permet d’obtenir des informations qui manquent à l’analyse statistique pure.
---

## Concepts de base
### Systèmes de coordonnées
| Système | Descriptif | Cas d'utilisation |
|--------|-------------|--------------|
| **WGS 84 (EPSG :4326)** | Norme mondiale ; latitude/longitude en degrés | GPS ; la plupart des cartographies Web ; GéoJSON |
| **Web Mercator (EPSG :3857)** | Projette le globe sur un cylindre ; déforme la zone aux pôles | Google Maps ; Boîte à cartes ; la plupart des services de tuiles Web |
| **UTM** (Mercerateur Transversal Universel) | Divise la Terre en 60 zones ; en mètres | Militaire; arpentage; travail local de haute précision |
| **Réseau national britannique (EPSG :27700)** | Données OSGB36 ; en mètres | Cartographie du Royaume-Uni |
| **Projections locales** | Projections personnalisées pour des régions spécifiques | Minimiser la distorsion pour une zone particulière |
### Types de géométrie
| Tapez | Descriptif | Exemple |
|------|-------------|--------------|
| **Point** | Coordonnée unique | Un restaurant ; un capteur ; un client |
| **LigneString** | Ordered sequence of points | Une route ; une rivière; un itinéraire |
| **Polygone** | Closed shape with interior | Un pays ; un lac ; une zone de livraison |
| **MultiPoint** | Collecte de points | All bus stops in a city |
| **MultiLineString** | Collection de lignes | Toutes les routes d'un réseau |
| **MultiPolygone** | Collection de polygones | Un archipel ; un pays avec des îles |
| **GéométrieCollection** | Types mixtes | Un pays avec ses villes, ses routes et ses rivières |
---

## Formats de données
| Formater | Tapez | Caractéristique clé |
|--------|------|-------------|
| **GéoJSON** | Texte (JSON) | Lisible par l'homme ; convivial pour le Web ; prend en charge tous les types de géométrie |
| **Fichier de formes** | Binaire (plusieurs fichiers) | Format hérité d'ESRI ; .shp + .shx + .dbf + .prj |
| **KML** | XML | Google Terre ; prend en charge la 3D et le temps |
| **Géopackage** | Basé sur SQLite | Fichier unique ; prend en charge le raster et le vecteur ; norme moderne |
| **GéoParquet** | Colonne (Parquet) | Efficace pour les grands ensembles de données ; s'intègre aux outils d'ingénierie des données |
| **WKT / WKB** | Texte / Binaire | Texte bien connu ; Binaire bien connu ; utilisé pour le stockage de bases de données |
| **MVT** | Binaire | Tuiles vectorielles Mapbox ; pour transmettre des données cartographiques aux clients Web |
---

## Opérations spatiales
### Opérations fondamentales
| Opération | Descriptif | Exemple |
|---------------|-------------|---------|
| **Distance** | Calculer la distance entre les géométries | "Trouver tous les hôpitaux dans un rayon de 10 km" |
| **Tampon** | Créer un polygone autour d'une géométrie à une distance donnée | "Afficher la zone de 500 m autour d'une école" |
| **Intersection** | Trouver la zone de chevauchement entre les géométries | « Quelles parcelles se trouvent dans la zone inondable ? |
| **Syndicat** | Fusionner les géométries en une seule | "Regroupez toutes les parcelles de terrain en une seule région" |
| **Différence** | Soustraire une géométrie d'une autre | "Superficie constructible hors zones protégées" |
| **Contient / Dans** | Tester si une géométrie est à l'intérieur d'une autre | « Quels clients se trouvent dans cette zone de livraison ? » |
| **Voisin le plus proche** | Trouver la géométrie la plus proche | "Quelle est la caserne de pompiers la plus proche ?" |
| **Jointure spatiale** | Joindre les attributs en fonction de la relation spatiale | "Attribuer chaque point au secteur de recensement qui le contient" |
### Indexation spatiale
| Type d'index | Descriptif | Cas d'utilisation |
|---------------|-------------|--------------|
| **Arbre R** | Hiérarchie du cadre de délimitation ; le plus courant | PostGIS ; SQLite ; usage général |
| **Quadarbre** | Subdivision récursive en quadrants | Données ponctuelles ; moteurs de jeux |
| **Géohash** | Grille hiérarchique ; encode en chaîne | Recherche de proximité ; partitionnement de base de données |
| **H3** (Uber) | Grille hiérarchique hexagonale | Analytique; covoiturage; bacs à uniformes |
| **S2** (Google) | Hiérarchie basée sur les cellules sur une sphère | Indexation spatiale à grande échelle |
---

## Outils et bibliothèques
| Outil / Bibliothèque | Langue | Descriptif |
|---------------|----------|-------------|
| **PostGIS** | SQL (PostgreSQL) | La référence en matière de bases de données spatiales ; SQL spatial complet |
| **QGIS** | Bureau (Python/C++) | SIG gratuit et open source ; écosystème de plugins |
| **GéoPandas** | Python | Pandas + Galbés + Fiona ; DataFrames spatiaux |
| ** Galbé ** | Python | Opérations de géométrie ; basé sur GEOS |
| **Folium** | Python | Cartes de brochures interactives de Python |
| **Turf.js** | JavaScript | Analyse géospatiale côté client |
| **Deck.gl** | JavaScript | Visualisation de données à grande échelle sur des cartes |
| **GDAL** | C++ (avec liaisons Python) | Traduction de données raster et vectorielles ; le couteau suisse |
| **Rasterio** | Python | Lecture/écriture de données raster ; basé sur GDAL |
| **Kepler.gl** | JavaScript | Visualisation géospatiale basée sur WebGL |
---

## Modèles d'analyse géospatiale
### Types d'analyse courants
| Modèle | Descriptif | Cas d'utilisation |
|---------|-------------|--------------|
| **Analyse de configuration de points** | Examiner la répartition des points | Cartographie de la criminalité ; détection des épidémies |
| **Analyse des points chauds** | Trouver des clusters statistiquement significatifs | Emplacement de vente au détail ; crime; épidémiologie |
| **Analyse du réseau** | Optimisation des itinéraires ; zones de service | Logistique; intervention d'urgence; utilitaires |
| **Interpolation spatiale** | Estimer les valeurs à des emplacements non échantillonnés | Qualité de l'air ; propriétés du sol ; météo |
| **Détection des changements d'affectation des terres** | Comparez les images satellite au fil du temps | L'étalement urbain ; déboisement; agriculture |
| **Analyse d'adéquation** | Trouver des emplacements répondant à plusieurs critères | Sélection du site ; planification de la conservation |
| **Autocorrélation spatiale** | Mesurer la relation entre les valeurs proches | Prix ​​de l'immobilier ; propagation de la maladie |
### Le problème des unités surfaciques modifiables (MAUP)
| Aspects | Problème |
|--------|---------|
| **Effet d'échelle** | Les résultats changent en fonction de la taille des unités d'analyse (secteurs de recensement, comtés ou États) |
| **Effet de zonage** | Les résultats changent en fonction de la manière dont les limites sont tracées, même à la même échelle |
| **Implication** | Ne présumez jamais que les résultats d’un niveau d’agrégation s’appliquent à un autre ; toujours tester la sensibilité aux limites |
---

## Considérations pratiques
| Préoccupation | Orientation |
|---------|----------|
| **Systèmes de référence de coordonnées** | Vérifiez toujours le CRS ; ne mélangez jamais les projections dans les calculs ; transformer avant de calculer les distances |
| **Précision** | La précision en virgule flottante est importante à petite échelle ; utiliser les types de données appropriés |
| **Performances** | Les opérations spatiales coûtent cher ; utiliser des index spatiaux ; simplifier les géométries pour l'affichage |
| **Topologie** | Assurez-vous que les géométries sont valides (pas d'auto-intersections, de polygones fermés) avant l'analyse |
| **Échelle** | Web Mercator déforme la zone ; ne l'utilisez pas pour les calculs de superficie |
| **Qualité des données** | Vérifiez les géométries nulles, les sommets en double, les polygones de ruban |
---

## Résumé
L'analyse géospatiale transforme les données de localisation en informations exploitables. Les points, lignes et polygones représentent des entités du monde réel. Les opérations spatiales (distance, zone tampon, intersection, jointure) répondent aux questions sur la proximité, le chevauchement et le confinement. Les outils vont de PostGIS pour l'analyse à l'échelle de la base de données à GeoPandas pour les flux de travail Python en passant par Deck.gl pour la visualisation Web. Les principaux défis consistent à choisir le bon système de coordonnées, à gérer les performances avec de grands ensembles de données et à connaître MAUP, c'est-à-dire le fait que votre choix de limites d'agrégation affecte vos résultats. Qu'il s'agisse d'optimiser les itinéraires de livraison, d'analyser la propagation d'une maladie ou de cartographier la croissance urbaine, l'analyse géospatiale fournit le contexte spatial que les chiffres purs ne peuvent pas capturer.