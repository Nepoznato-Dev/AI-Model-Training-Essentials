---
# Metadata
title: "Software Architecture Patterns"
description: "Monolith, microservices, event-driven, DDD, caching, SOLID"
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
tags: [software, architecture, patterns, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Modèles d'architecture logicielle
L'architecture est l'ensemble des décisions structurelles concernant la manière dont un système est organisé : quels sont ses composants, comment ils communiquent et où se situent les responsabilités. Une bonne architecture rend un système facile à comprendre, à modifier et à faire évoluer. Une mauvaise architecture fait de chaque changement un combat. Ce fichier couvre les principaux modèles, quand les utiliser et les compromis impliqués.
---

## Monolithe vs Microservices
Il s’agit de la décision architecturale la plus fondamentale, et elle vaut la peine d’être prise correctement.
| Aspects | Monolithe | Microservices |
|--------|----------|---------------|
| **Structure** | Unité déployable unique | De nombreux petits services déployables indépendamment |
| **Données** | Base de données partagée | Chaque service est propriétaire de ses données |
| **Communication** | Appels de fonctions en cours | Appels réseau (HTTP, gRPC, messagerie) |
| **Mise à l'échelle** | Mettre à l'échelle l'ensemble de l'application | Faire évoluer les services individuels |
| **Déploiement** | Cycle de version unique | Déploiements indépendants |
| **Complexité** | Plus simple à développer au départ | Complexité opérationnelle (mise en réseau, surveillance) |
| **Meilleur pour** | Petites équipes, produits en phase de démarrage | Grandes équipes, domaines complexes, à grande échelle |
### Quand commencer avec un monolithe
La plupart des applications devraient démarrer comme un monolithe. Il est plus simple de créer, tester, déployer et déboguer. Vous pourrez toujours extraire les services plus tard lorsque vous aurez une idée plus claire des limites de votre domaine. C'est ce qu'on appelle parfois le « monolithe modulaire » — un monolithe avec des limites internes propres qui facilitent l'extraction ultérieure.
### Quand utiliser les microservices
Envisagez les microservices lorsque :
- Les équipes sont suffisamment grandes pour que la coordination devienne un goulot d'étranglement.
- Différentes parties du système ont des exigences de mise à l'échelle très différentes.
- Vous avez besoin d'un déploiement indépendant de composants.
- Votre domaine a des contextes délimités clairs (voir DDD ci-dessous).
---

## Architecture en couches (N-Tier)
Le modèle d'architecture le plus courant. Le code est organisé en couches, chacune ayant une responsabilité spécifique.
```
â”Œ─────────────────────────┐
│   Presentation Layer    │  ← UI, controllers, API endpoints
├─────────────────────────┤
│   Application Layer     │  ← Use cases, orchestration
├─────────────────────────┤
│   Domain Layer          │  ← Business logic, entities
├─────────────────────────┤
│   Infrastructure Layer  │  ← Database, external services, file I/O
└─────────────────────────┘
```

| Couche | Responsabilité | Règle |
|-------|--------------|------|
| **Présentation** | Gérer les requêtes utilisateur/HTTP | Peut appeler la couche Application uniquement |
| **Candidature** | Orchestrer les cas d'utilisation | Peut appeler la couche de domaine |
| **Domaine** | Logique métier de base | Ne devrait pas dépendre d'autres couches |
| **Infrastructures** | Problèmes techniques | Implémente les interfaces définies dans Domaine |
**Règle clé** : les dépendances pointent vers l'intérieur. La couche Domaine ne connaît pas la base de données ou le framework Web.
---

## Architecture basée sur les événements
Les composants communiquent en émettant et en réagissant à des **événements** – des choses qui se sont produites.
| Modèle | Descriptif |
|---------|-------------|
| **Notification d'événement** | Le service A émet « OrderPlaced » ; les services B, C, D réagissent |
| **Recherche d'événements** | Stocker tous les changements d'état sous forme de séquence d'événements (pas seulement l'état actuel) |
| **CQRS** | Séparer le modèle de lecture (requêtes) du modèle d'écriture (commandes) |
### Recherche d'événements
Au lieu de stocker « l'état actuel » dans une base de données, stockez chaque changement d'état en tant qu'événement :
```
OrderCreated(order_id=123, total=$50)
OrderPaid(order_id=123, payment_id=456)
OrderShipped(order_id=123, tracking=ABC)
```

Avantages : piste d'audit complète, possibilité de reconstituer n'importe quel état passé, consommateurs découplés. Défis : évolution du schéma événementiel, cohérence éventuelle, complexité du débogage.
### CQRS (ségrégation des responsabilités des requêtes de commande)
| Côté | Objectif | Base de données |
|------|---------|--------------|
| **Commande (écrire)** | Gérer les mutations ; appliquer les règles métier | Optimisé pour les écritures (normalisé) |
| **Requête (lecture)** | Servir les demandes de lecture | Optimisé pour les lectures (dénormalisé) |
CQRS s'associe naturellement à Event Sourcing : les événements du côté écriture sont projetés dans des vues optimisées pour la lecture.
---

## Files d'attente de messages et courtiers d'événements
Lorsque les services doivent communiquer de manière asynchrone, les files d’attente de messages constituent l’épine dorsale.
| Outil | Tapez | Idéal pour |
|------|------|----------|
| **Apache Kafka** | Journal des événements distribués | Streaming d'événements à haut débit, sourcing d'événements |
| **LapinMQ** | Courtier de messages avec routage | Files d'attente de tâches, modèles de routage complexes |
| **AWSSQS** | File d'attente gérée | Mise en file d'attente simple et native pour AWS |
| **AWS SNS** | Notification de publication/sous-publication | Distribution à plusieurs abonnés |
| **Google Pub/Sub** | Pub/sub géré | Diffusion d'événements natifs GCP |
| **Flux Redis** | Flux léger | Journalisation simple des événements, cas d'utilisation de la mise en cache |
### Modèles de messagerie
| Modèle | Descriptif |
|---------|-------------|
| **Point à point** | Un producteur, un consommateur par message |
| **Publier/S'abonner** | Un producteur, plusieurs abonnés |
| **Demande/Réponse** | Style synchrone sur transport asynchrone |
| **File d'attente des lettres mortes** | Les messages dont le traitement échoue sont envoyés dans une file d'attente distincte pour inspection |
---

## Conception basée sur le domaine (DDD)
DDD est une approche stratégique de la conception de logiciels qui centre le code autour de concepts commerciaux plutôt que de préoccupations techniques.
### Concepts clés
| Concepts | Descriptif |
|---------|-------------|
| **Contexte délimité** | Une limite à l'intérieur de laquelle un modèle de domaine est cohérent (par exemple, "Commande", "Expédition", "Facturation") |
| **Langue omniprésente** | Vocabulaire partagé entre développeurs et experts du domaine |
| **Agrégats** | Clusters d'entités liées traitées comme une seule unité pour les modifications de données |
| **Entités** | Objets avec identité (par exemple, un utilisateur avec un user_id) |
| **Objets de valeur** | Objets sans identité ; définis par leurs attributs (par exemple, Argent, Adresse) |
| **Événements de domaine** | Quelque chose qui s'est produit dans le domaine (par exemple, OrderPlaced) |
| **Couche anti-corruption** | Couche de traduction entre votre domaine et les systèmes externes |
### Quand DDD aide
DDD est particulièrement utile lorsque le domaine d'activité est complexe : pensez au commerce électronique, à la logistique, aux services financiers et à la santé. Si votre domaine est simple (un blog, une application de tâches), DDD est excessif.
---

## Stratégies de mise en cache
La mise en cache est l’un des moyens les plus efficaces d’améliorer les performances, mais elle introduit de la complexité en matière de cohérence.
| Stratégie | Descriptif | Compromis |
|--------------|-------------|---------------|
| **Cache réservé** | L'application vérifie d'abord le cache ; charges de DB en cas d'échec | Simple; cohérence éventuelle |
| **Écriture directe** | Écrire simultanément dans le cache et dans la base de données | Cohérent; écritures plus lentes |
| **Écriture derrière** | Écrire dans le cache ; écriture asynchrone dans la base de données | Écriture rapide ; risque de perte de données |
| **Lecture continue** | Le cache se charge de manière transparente à partir de la base de données en cas d'échec | Plus simple que le cache-côté |
### Que mettre en cache
| Couche | Quoi | Outils |
|-------|------|-------|
| **CAN** | Actifs statiques, réponses API | CloudFront, Cloudflare |
| **Candidature** | Résultats calculés, données de session | Redis, Memcached |
| **Base de données** | Résultats de la requête, lignes fréquemment consultées | Cache de requêtes, vues matérialisées |
**L'invalidation du cache** est notoirement difficile. Stratégies courantes : TTL (durée de vie), invalidation basée sur les événements (vider le cache en cas de modification des données) et expulsion LRU (la moins récemment utilisée).
---

## Modèles de conception
### Principes SOLIDES
| Principe | Ce que cela signifie |
|-----------|--------------|
| **S** — Responsabilité unique | Une classe devrait avoir une raison de changer |
| **O** — Ouvert/Fermé | Ouvert pour extension, fermé pour modification |
| **L** — Remplacement Liskov | Les sous-types doivent être substituables à leurs types de base |
| **I** — Ségrégation d'interface | De nombreuses interfaces spécifiques > une interface polyvalente |
| **D** — Inversion de dépendance | Dépendez des abstractions, pas des concrétions |
### Modèles courants
| Modèle | Intention | Exemple |
|---------|--------|---------|
| **Célibataire** | Assurez-vous qu'une classe n'a qu'une seule instance | Pool de connexions à la base de données |
| **Usine** | Créer des objets sans spécifier de classe exacte | `UserFactory.create(type="admin")`|
| **Observateur** | Avertir les personnes à charge lorsque l'état change | Écouteurs d'événements, pub/sub |
| **Stratégie** | Échanger les algorithmes au moment de l'exécution | Stratégie de paiement : carte de crédit, PayPal, crypto |
| **Dépôt** | Accès aux données abstraites derrière une interface épurée | `UserRepository.find_by_id(123)`|
| **Décorateur** | Ajouter un comportement dynamiquement | Décorateur forestier autour d'un service |
| **Adaptateur** | Faire fonctionner ensemble des interfaces incompatibles | Adaptateur API hérité |
---

## Choisir la bonne architecture
Il n’existe pas de « meilleure » architecture universelle. Le bon choix dépend :
| Facteur | Favorisez le monolithe quand... | Favoriser les microservices quand... |
|--------|------------------------|--------------------------------------------|
| **Taille de l'équipe** | < 10 developers | >20 développeurs, plusieurs équipes |
| **Complexité du domaine** | Simple ou bien compris | Contextes complexes et nombreux et délimités |
| **Exigences d'échelle** | Besoins de mise à l'échelle uniforme | Différents composants nécessitent une échelle différente |
| **Cadence de déploiement** | Cycle de version unique | Déploiements indépendants nécessaires |
| **Diversité technologique** | Une pile suffit | Différents services nécessitent des technologies différentes |
**Conseil pratique** : commencez par un monolithe modulaire. Extrayez les services uniquement lorsque vous avez un besoin clair et des limites de domaine claires. Les microservices prématurés sont l’une des erreurs architecturales les plus courantes dans l’industrie.