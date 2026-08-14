---
# Metadata
title: "Blockchain and Distributed Systems"
description: "Consensus, smart contracts, DeFi, Byzantine fault tolerance"
category: "Coding and Technology"
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

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [blockchain, distributed, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Blockchain et systèmes distribués
La blockchain est un type spécifique de système distribué : un registre décentralisé à ajout uniquement dans lequel les enregistrements (blocs) sont liés par des hachages cryptographiques. Les systèmes distribués constituent le domaine plus large permettant à plusieurs ordinateurs de fonctionner ensemble comme un seul. Ces deux concepts sont importants pour comprendre les infrastructures modernes, depuis les cryptomonnaies jusqu’aux bases de données distribuées en passant par les algorithmes de consensus qui alimentent les services mondiaux.
---

## Fondamentaux des systèmes distribués
### Pourquoi des systèmes distribués ?
| Motivation | Descriptif |
|---------------|-------------|
| **Évolutivité** | Ajouter plus de machines pour gérer plus de charge |
| **Tolérance aux pannes** | Le système continue de fonctionner même si certaines machines tombent en panne |
| **Répartition géographique** | Servir les utilisateurs des centres de données à proximité |
| **Spécialisation** | Différentes machines gèrent différentes tâches |
### Concepts clés
| Concepts | Descriptif | Défi |
|---------|-------------|---------------|
| **Consensus** | Faire en sorte que tous les nœuds se mettent d'accord sur une valeur | Partitions réseau ; Failles byzantines |
| **Réplication** | Copie de données sur plusieurs nœuds | Cohérence vs disponibilité |
| **Partitionnement (partage)** | Répartition des données entre les nœuds | Points chauds ; requêtes entre fragments |
| **Modèles de cohérence** | Garanties sur ce que voient les différents lecteurs | Une consistance forte est lente ; une éventuelle cohérence peut surprendre les utilisateurs |
| **Théorème CAP** | Vous ne pouvez en avoir que 2 parmi : Cohérence, Disponibilité, Tolérance de partition | En pratique, une tolérance de partition est requise ; choisissez C ou A |
### Le théorème CAP
| Choix | Ce que vous obtenez | Ce à quoi vous abandonnez | Exemple |
|--------|-------------|-------|---------|
| **PC** | Cohérent + tolérant aux partitions | Certains nœuds peuvent être indisponibles pendant les partitions | HBase, MongoDB, Redis |
| **PA** | Disponible + tolérant aux partitions | Les lectures peuvent renvoyer des données obsolètes | Cassandra, DynamoDB, CouchDB |
| **CA** | Cohérent + disponible | Je ne peux pas tolérer les partitions réseau | Bases de données à nœud unique (pas véritablement distribuées) |
---

## Algorithmes de consensus
Comment les nœuds distribués s’accordent-ils sur l’état du système ?
| Algorithme | Tapez | Tolérance aux pannes | Utilisé dans |
|---------------|------|----------------|---------|
| **Paxos** | Tolérant aux pannes | Jusqu'à f échecs avec 2f+1 nœuds | Google Chubby ; théorie fondamentale |
| **Radeau** | Tolérant aux pannes | Jusqu'à f échecs avec 2f+1 nœuds | etcd, Consul, TiKV |
| **PBFT** | Tolérant aux pannes byzantines | Jusqu'à f échecs avec 3f+1 nœuds | Tissu Hyperledger |
| **Preuve de travail** | Tolérant aux pannes byzantines | Dépend de la puissance de hachage | Bitcoin |
| **Preuve de participation** | Tolérant aux pannes byzantines | Dépend de l'enjeu | Ethereum 2.0, Cardano |
### Radeau (simplifié)
| Rôle | Responsabilité |
|------|--------------------|
| **Chef** | Gère toutes les demandes des clients ; envoie des entrées de journal aux abonnés |
| **Suiveur** | Répond aux demandes du leader; votes aux élections |
| **Candidat** | Demande des votes pour devenir leader |
1. Tous les nœuds commencent en tant que suiveurs
2. Si un partisan n'entend pas le chef pendant un délai d'attente électoral, il devient candidat
3. Les candidats demandent des votes ; celui qui a le plus de voix devient leader
4. Le leader réplique les entrées du journal aux abonnés
5. Lorsqu'une majorité confirme, l'entrée est engagée
---

## Blockchain
### Comment fonctionne une blockchain
| Composant | Descriptif |
|---------------|-------------|
| **Bloquer** | Un lot de transactions + métadonnées + hachage du bloc précédent |
| **Hachage** | Empreinte cryptographique du contenu du bloc |
| **Chaîne** | Chaque bloc fait référence au hachage du bloc précédent, créant une chaîne immuable |
| **Consensus** | Les participants au réseau se mettent d'accord sur les blocs à ajouter |
| **Arbre Merkle** | Arbre de hachages résumant toutes les transactions d'un bloc |
### Pourquoi la blockchain est difficile à falsifier
1. Chaque bloc contient le hachage du bloc précédent
2. La modification d'une transaction modifie le hachage du bloc
3. Le hachage modifié brise la chaîne — tous les blocs suivants deviennent invalides
4. Un attaquant devrait ré-exploiter tous les blocs suivants ET contrôler > 50 % du réseau
### Types de blockchains
| Tapez | Accès | Validateur | Exemple |
|------|--------|-----------|---------|
| **Public (sans autorisation)** | Tout le monde peut lire et écrire | Consensus ouvert (PoW, PoS) | Bitcoin, Ethereum |
| **Privé (autorisé)** | Accès restreint | Validateurs connus | Hyperledger, Corda |
| **Consortium** | Gouverné par un groupe d'organisations | Validateurs sélectionnés | R3 Corda pour le secteur bancaire |
### Contrats intelligents
Code auto-exécutable stocké sur la blockchain qui s'exécute lorsque des conditions prédéterminées sont remplies.
| Plateforme | Langue | Caractéristique notable |
|----------|----------|------------------|
| **Éthéré** | Solidité, Vyper | Le plus grand écosystème de contrats intelligents |
| **Solana** | Rouille, C | Débit élevé ; frais bas |
| **Cardano** | Haskell (Plutus) | Évalué par les pairs ; vérification formelle |
| **Hyperledger** | Allez, Java, JavaScript | Entreprise; autorisé |
---

## Crypto-monnaie
| Monnaie | Consensus | Approvisionnement | Utilisation principale |
|----------|-----------|--------|-------------|
| **Bitcoin** | Preuve de travail | 21 millions (plafonné) | Réserve de valeur ; or numérique |
| **Éthéré** | Preuve de participation | Pas de plafond rigide | Contrats intelligents ; DéFi ; NFT |
| **Solana** | Preuve d'enjeu + Preuve d'historique | Pas de plafond rigide | Transactions à grande vitesse |
| **Cardano** | Preuve de participation (Ouroboros) | 45 milliards (plafonné) | Approche académique ; durabilité |
---

## Bases de données distribuées
| Base de données | Architecture | Cohérence | Idéal pour |
|--------------|-------------|-------------|----------|
| **Cassandre** | Colonne large ; peer-to-peer | Ajustable (éventuellement au quorum) | Débit d'écriture élevé ; séries chronologiques |
| **MongoDB** | Document; jeux de répliques | Éventuel (avec option de cohérence causale) | Schéma flexible ; développement rapide |
| **CafardDB** | SQL distribué ; Consensus du radeau | Fort | SQL distribué ; déploiement mondial |
| **TiDB** | SQL distribué ; Radeau (via TiKV) | Fort | Compatible MySQL ; mise à l'échelle horizontale |
| **DynamoDB** | Valeur-clé ; géré | Éventuel (ou fort avec des lectures cohérentes) | Sans serveur ; Intégré à AWS |
| **Clé** | SQL distribué ; Paxos | Fort | Google Cloud ; cohérence globale |
---

## Modèles de système distribué
| Modèle | Descriptif | Cas d'utilisation |
|---------|-------------|--------------|
| **Élection du chef** | Choisissez un nœud à coordonner | Chef de radeau ; Gardien de zoo |
| **Réplication** | Copier les données pour la redondance et la mise à l'échelle de lecture | Réplicas de bases de données ; Canada |
| **Partage** | Partitionner les données par plage de clés ou hachage | Bases de données à grande échelle |
| **MapRéduire** | Diviser le calcul entre les nœuds ; résultats agrégés | Traitement de données volumineuses |
| **Protocole des potins** | Les nœuds partagent périodiquement leur état avec des pairs aléatoires | Adhésion au cluster ; détection de panne |
| **Engagement en deux phases** | Coordonner les transactions sur plusieurs nœuds | Bases de données distribuées |
| **Modèle Saga** | Série de transactions locales avec actions compensatoires | Transactions de microservices |
| **Disjoncteur** | Arrêtez d'appeler un service défaillant ; échouer rapidement | Résilience; éviter les pannes en cascade |
---

## Défis dans les systèmes distribués
| Défi | Descriptif | Atténuation |
|---------------|-------------|------------|
| **Partitions réseau** | Les nœuds ne peuvent pas communiquer | Compromis avec la PAC ; réessayez avec interruption |
| **Décalage de l'horloge** | Différents nœuds ont des horloges différentes | Utilisez des horloges logiques ; NTP ; évitez de vous fier à l'heure de l'horloge murale |
| **Failles byzantines** | Nœuds qui mentent ou se comportent arbitrairement | consensus sur le thon rouge ; blockchain |
| **Cerveau divisé** | Deux nœuds pensent tous les deux qu'ils sont le leader | Escrime; décisions basées sur le quorum |
| **Échecs en cascade** | Un échec en déclenche d'autres | Disjoncteurs ; cloisons; dégradation gracieuse |
| **Cohérence des données** | Synchroniser les répliques | Modèles de cohérence ; résolution des conflits |
---

## Résumé
Les systèmes distribués permettent aux logiciels modernes d'évoluer, de survivre aux pannes et de servir les utilisateurs du monde entier. Les algorithmes de consensus (Raft, Paxos) garantissent que les nœuds sont d'accord. Les blockchains ajoutent une vérification cryptographique et une décentralisation pour créer des registres sans confiance. Les bases de données distribuées (Cassandra, CockroachDB, DynamoDB) gèrent les données à grande échelle. Le compromis fondamental – capturé par le théorème CAP – se situe entre cohérence et disponibilité lorsque le réseau n’est pas fiable. Comprendre ces concepts est essentiel pour créer des systèmes qui fonctionnent à l’échelle d’Internet.