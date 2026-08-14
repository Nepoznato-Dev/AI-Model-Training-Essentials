<!--
---
# Metadata
title: "Technology and Computing"
description: "Computing basics, internet, databases, cloud, security"
category: "General Reference"
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
reviewed_by: "General Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [technology, computing, general-reference]
difficulty_level: "beginner"
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
# Technologie et informatique
L'informatique est partout : dans votre téléphone, votre voiture, votre réfrigérateur, vos appareils médicaux et l'infrastructure qui gère la société moderne. Vous n’avez pas besoin d’être programmeur pour comprendre comment tout cela fonctionne. Ce dossier couvre les principes fondamentaux : ce qu'est un ordinateur, comment fonctionne Internet, comment les logiciels sont construits et les concepts qui façonnent le monde numérique.
> **Vous voulez approfondir ?** Ce fichier est un aperçu général. Pour une couverture détaillée de n'importe quel sujet, consultez les fichiers dédiés dans[`01_coding_and_technology/`](../01_coding_and_technology/)- y compris[database systems](../01_coding_and_technology/database_systems.md),[cloud architecture](../01_coding_and_technology/cloud_architecture.md),[networking](../01_coding_and_technology/networking_basics.md)et.
---

## Qu'est-ce qu'un ordinateur ?
À la base, chaque ordinateur – du smartphone au superordinateur – fait la même chose : il prend des entrées, les traite selon des instructions (un programme) et produit une sortie. La magie réside dans la vitesse et l’ampleur.
### L'architecture Von Neumann
Presque tous les ordinateurs modernes suivent cette conception de base :
| Composant | Ce qu'il fait | Analogie |
|---------------|-------------|---------|
| **CPU** (unité centrale de traitement) | Exécute les instructions ; le "cerveau" | Le chef suivant une recette |
| **RAM** (Mémoire) | Stocke les données que le processeur utilise activement ; perdu lorsque l'alimentation est coupée | Le comptoir — accès rapide, espace limité |
| **Stockage** (SSD/HDD) | Stocke les données en permanence | Le garde-manger — un accès plus lent, beaucoup plus d'espace |
| **Entrée/Sortie** | Clavier, souris, écran, réseau | Comment le chef reçoit les commandes et livre les plats |
| **GPU** (unité de traitement graphique) | Processeur spécialisé pour tâches parallèles (graphiques, IA) | Une équipe d'assistants effectuant tous la même tâche simultanément |
**Aperçu clé** : la RAM est rapide mais temporaire. Le stockage est lent mais permanent. Lorsque votre ordinateur « semble lent », c'est souvent parce qu'il manque de RAM et doit utiliser le stockage comme mémoire temporaire (échange), ce qui est beaucoup plus lent.
---

## Langages de programmation – Parler aux ordinateurs
Un langage de programmation est un ensemble d'instructions qu'un ordinateur peut exécuter. Différentes langues sont conçues à des fins différentes. Pour une couverture détaillée de 34 langues individuelles, consultez le dossier [`programming_languages/`](../01_coding_and_technology/programming_languages/).
| Langue | Idéal pour | Pourquoi le choisir |
|--------------|---------|--------------|
| **Python** | Science des données, IA, automatisation, backends Web | Syntaxe simple ; immense écosystème; idéal pour les débutants |
| **JavaScript** | Frontends Web, full-stack (Node.js) | Fonctionne dans tous les navigateurs ; essentiel pour le développement web |
| **Java** | Logiciels d'entreprise, applications Android | Indépendant de la plate-forme (JVM) ; grand écosystème |
| **C/C++** | Programmation de systèmes embarqués pour jeux | Performances maximales ; contrôle matériel direct |
| **Rouille** | Programmation de systèmes avec garanties de sécurité | Sécurité de la mémoire sans garbage collection |
| **Allez** | Services cloud, microservices, outils CLI | Simple; excellente simultanéité ; compilation rapide |
| **SQL** | Requêtes de base de données | Le langage universel pour travailler avec les données |
| **TypeScript** | Applications Web à grande échelle | JavaScript avec vérification de type ; attrape les bugs tôt |
---

## Comment fonctionne Internet
Internet n’est pas la même chose que le Web. Internet est le réseau physique composé de câbles, de routeurs, de serveurs et de protocoles qui connectent des milliards d'appareils. Le World Wide Web est un service qui fonctionne sur Internet (avec le courrier électronique, le transfert de fichiers, le streaming, les jeux, etc.).
### Le parcours d'une requête Web
Lorsque vous tapez`https://www.example.com`dans votre navigateur :
1. **Recherche DNS** : votre navigateur demande à un serveur DNS de traduire "www.example.com" en une adresse IP (comme 93.184.216.34).
2. **Connexion TCP** : votre appareil établit une connexion à cette adresse IP à l'aide de TCP (un protocole qui garantit une livraison fiable).
3. **Poignée de liaison TLS** : si vous utilisez HTTPS, votre navigateur et le serveur négocient une connexion cryptée.
4. **Requête HTTP** : Votre navigateur envoie une requête : "Donnez-moi la page à l'adresse /index.html."
5. **Traitement du serveur** : le serveur Web trouve la page, interroge éventuellement une base de données et prépare une réponse.
6. **Réponse HTTP** : le serveur renvoie HTML, CSS et JavaScript.
7. **Rendu** : votre navigateur analyse le code HTML, applique les styles CSS et exécute JavaScript pour afficher la page.
L’ensemble de ce processus prend généralement moins d’une seconde.
### Protocoles clés
| Protocole | Ce qu'il fait | Couche |
|--------------|-------------|-------|
| **IP** (Protocole Internet) | Achemine les paquets entre les réseaux | Réseau |
| **TCP** | Livraison fiable et ordonnée (retransmet les paquets perdus) | Transports |
| **UDP** | Livraison rapide et peu fiable (pas de retransmission) | Transports |
| **HTTP/HTTPS** | Transfert de pages Web (HTTPS ajoute le cryptage) | Demande |
| **DNS** | Traduit les noms de domaine en adresses IP | Demande |
| **SSH** | Accès à distance sécurisé aux ordinateurs | Demande |
| **SMTP/IMAP** | Envoi et réception d'e-mails | Demande |
---

## Développement de logiciels – Comment les programmes sont construits
### Le processus de développement
1. **Écrire du code** : les développeurs écrivent des instructions dans un langage de programmation.
2. **Test du code** : exécutez le code pour vérifier qu'il fonctionne correctement.
3. **Contrôle de version** : suivez les modifications à l'aide de Git, la norme universelle.
4. **Révision** : d'autres développeurs vérifient le code pour détecter les erreurs et la qualité.
5. **Build** : convertissez le code source en un programme exécutable (compilation).
6. **Déployer** : diffusez le programme aux utilisateurs (serveurs, magasins d'applications, etc.).
7. **Surveiller** : surveillez les erreurs et les problèmes de performances en production.
### Concepts clés
| Concepts | Ce que cela signifie | Pourquoi c'est important |
|---------|---------------|----------------|
| **Contrôle de version (Git)** | Suivez chaque modification du code au fil du temps | Collaboration; capacité à réparer les erreurs |
| **API** (interface de programmation d'applications) | Une manière définie pour les composants logiciels de communiquer | Permet à différents systèmes de fonctionner ensemble |
| **Base de données** | Stockage organisé des données | Chaque application doit stocker et récupérer des données |
| **Tests** | Vérifications automatisées du bon fonctionnement du code | Empêche les bugs d'atteindre les utilisateurs |
| **CI/CD** (Intégration/Livraison continue) | Pipeline automatisé depuis la validation du code jusqu'à la production | Des versions plus rapides et plus sûres |
| **Conteneurisation (Docker)** | Packager une application avec toutes ses dépendances | "Fonctionne sur ma machine" devient "fonctionne partout" |
---

## Bases de données – Où vivent les données
Chaque application doit stocker des données. Les bases de données sont les systèmes qui le font de manière efficace et fiable.
| Tapez | Comment les données sont stockées | Idéal pour | Exemples |
|------|---------|----------|---------|
| **Relationnel (SQL)** | Tableaux avec lignes et colonnes ; schéma strict | Données structurées ; requêtes complexes ; transactions | PostgreSQL, MySQL, SQLite |
| **Document (NoSQL)** | Documents de type JSON ; schéma flexible | Données semi-structurées ; itération rapide | MongoDB, CouchDB |
| **Valeur-clé** | Paires clé → valeur simples | Mise en cache ; stockage de sessions ; recherches rapides | Redis, DynamoDB |
| **Graphique** | Nœuds et arêtes (relations) | Réseaux sociaux ; moteurs de recommandation | Neo4j, JanusGraph |
| **Série chronologique** | Optimisé pour les données horodatées | Surveillance; analytique; IdO | InfluxDB, TimescaleDB |
**SQL** (Structured Query Language) est le langage standard des bases de données relationnelles. Il s'agit de l'une des compétences techniques les plus précieuses que vous puissiez acquérir : presque toutes les organisations utilisent des bases de données et SQL est la manière dont vous leur communiquez.
---

## Systèmes d'exploitation
Le système d'exploitation (OS) est la couche logicielle entre vous (et vos programmes) et le matériel. Il gère la mémoire, les processus, les fichiers et les appareils.
| Système d'exploitation | Où il domine | Caractéristique clé |
|----|---------|-------------|
| **Windows** | Ordinateurs de bureau/portables (~ 72 % de part de marché) | Compatibilité logicielle/matérielle la plus étendue |
| **macOS** | Professionnels de la création, développeurs | Basé sur Unix ; interface utilisateur raffinée ; Écosystème Apple |
| **Linux** | Serveurs (~96 %), supercalculateurs (100 %), embarqués, développeurs | Source ouverte ; gratuit; extrêmement personnalisable |
| **Android** | Mobile (~ 72 % de part de marché mondial) | Basé sur le noyau Linux ; source ouverte |
| **iOS** | Mobile (~ 27 % au niveau mondial, mais revenus plus élevés) | Écosystème fermé ; brillant; axé sur la confidentialité |
Linux mérite une mention spéciale : il alimente la majeure partie d'Internet, tous les 500 meilleurs superordinateurs, la plupart des infrastructures cloud et tous les téléphones Android. Il est gratuit, open source et maintenu par une communauté mondiale.
---

## Informatique en nuage
Le cloud computing consiste à louer des ressources informatiques (serveurs, stockage, bases de données, etc.) sur Internet au lieu d'acheter et d'entretenir votre propre matériel. Pour un guide complet sur l'architecture cloud, les modèles de service et les comparaisons de fournisseurs, consultez[cloud architecture](../01_coding_and_technology/cloud_architecture.md).
| Modèle de service | Ce que vous obtenez | Analogie | Exemples |
|---------------|-------------|---------|---------|
| **IaaS** (Infrastructures) | Serveurs virtuels, stockage, réseau | Louer un terrain et construire ce que vous voulez | AWS EC2, Google Compute Engine |
| **PaaS** (Plateforme) | Environnement d'exécution ; vous apportez du code | Louer un appartement meublé | Heroku, Google App Engine |
| **SaaS** (Logiciel) | Demande complète ; vous venez de l'utiliser | Séjourner dans un hôtel | Gmail, Slack, Salesforce |
Les trois principaux fournisseurs de cloud sont **AWS** (Amazon, ~32 % de part de marché), **Azure** (Microsoft, ~23 %) et **GCP** (Google, ~10 %). Ils offrent des centaines de services couvrant le calcul, le stockage, les bases de données, l'IA, la mise en réseau, etc.
---

## Cybersécurité – Protéger les systèmes numériques
La cybersécurité est la pratique consistant à défendre les ordinateurs, les réseaux et les données contre les attaques. C’est important parce que tout est connecté et que le coût des violations est énorme. Pour un guide complet couvrant le Top 10 OWASP, le cycle de vie de développement sécurisé et la gestion des secrets, voir.
### Menaces courantes
| Menace | Qu'est-ce que c'est | Prévention |
|--------|-----------|------------|
| **Logiciels malveillants** | Logiciels malveillants (virus, vers, chevaux de Troie) | Antivirus ; garder le logiciel à jour |
| **Phishing** | Faux e-mails/messages vous incitant à révéler des informations | Entraînement; filtrage des e-mails ; scepticisme |
| **Rançongiciel** | Chiffre vos données ; exige le paiement de la clé | Sauvegardes ; systèmes de correctifs ; ne payez pas |
| **DDoS** | Submerge un service de trafic | Filtrage du trafic ; Protection CDN |
| **Injection SQL** | Insertion de SQL malveillant dans les champs de saisie | Requêtes paramétrées ; validation des entrées |
| **L'homme du milieu** | Interception de communication entre deux parties | Cryptage HTTPS/TLS |
### Fondamentaux de la sécurité
- **Cryptage** : brouillez les données afin que seules les parties autorisées puissent les lire. HTTPS utilise TLS pour chiffrer le trafic Web.
- **Authentification** : Vérifiez l'identité. Utilisez l'authentification multifacteur (MFA) : mot de passe + autre chose (code, biométrique).
- **Autorisation** : Vérifiez les autorisations. Ce n’est pas parce que vous êtes connecté que vous devez accéder à tout.
- **Principe du moindre privilège** : accordez aux utilisateurs et aux systèmes uniquement l'accès dont ils ont besoin, rien de plus.
- **Gestion des correctifs** : gardez le logiciel à jour. La plupart des violations exploitent des vulnérabilités connues qui disposent déjà de correctifs.
---

## Formats de données
Les programmes échangent des données dans des formats spécifiques. Les plus courants :
| Formater | Structure | Utilisé pour |
|--------|-----------|--------------|
| **JSON** | Paires clé-valeur ; lisible par l'homme | Apis; configuration; échange de données |
| **XML** | Basé sur des balises ; verbeux mais flexible | Systèmes hérités ; documents; API SOAP |
| **YAML** | Basé sur l'indentation ; très lisible | Configuration (Docker, Kubernetes, CI/CD) |
| **CSV** | Lignes et colonnes de texte brut | Import/export de données ; feuilles de calcul |
---

## Résumé
L'informatique n'est pas magique, c'est de l'ingénierie. Les ordinateurs suivent les instructions à une vitesse incroyable. Internet connecte des milliards d’entre eux à l’aide de protocoles standardisés. Les logiciels sont construits par des équipes de personnes qui écrivent, testent et déploient du code selon des cycles itératifs. Les bases de données stockent et récupèrent des données. Le cloud computing permet à chacun d'accéder à des ressources informatiques massives à la demande. Et la cybersécurité est la bataille permanente pour garder tout cela à l’abri des personnes souhaitant l’exploiter. Comprendre ces principes fondamentaux vous aide à naviguer dans le monde numérique, que vous soyez un utilisateur, un développeur ou simplement quelqu'un qui essaie de donner un sens à la technologie qui façonne la vie moderne.