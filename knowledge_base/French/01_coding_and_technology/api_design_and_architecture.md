---
# Métadonnées
titre : "Conception et architecture d'API"
description : "REST, GraphQL, gRPC, gestion des versions, authentification, passerelles API"
catégorie : "Codage et technologie"
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
review_by : "Équipe de base de connaissances en matière de codage et de technologie"
next_review : "2027-08-05"
#Classement
tags : [api, conception, architecture, codage et technologie]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "10 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Conception et architecture des API
Une API (Application Programming Interface) est la façon dont les composants logiciels communiquent entre eux. Une API bien conçue est intuitive, cohérente et agréable à utiliser. Un système mal conçu provoque de la confusion, des bugs et de la frustration. Ce fichier couvre les principes, modèles et pratiques de création d'API que les développeurs souhaitent réellement utiliser.
---

## Principes de l'API REST
REST (Representational State Transfer) est le style architectural dominant pour les API Web. Il traite les données comme des **ressources** identifiées par des URL et utilise des méthodes HTTP pour les exploiter.
### Principes fondamentaux
| Principe | Descriptif |
|---------------|-------------|
| **Ressources** | Tout est une ressource avec un URI (`/users/123`,`/orders/456`) |
| **Méthodes HTTP** | GET (lire), POST (créer), PUT (remplacer), PATCH (mise à jour partielle), DELETE (supprimer) |
| **Apatridie** | Chaque demande contient toutes les informations nécessaires ; aucun état de session côté serveur |
| **Interface uniforme** | Dénomination cohérente des ressources, méthodes standard, codes d'état standard |
| **Représentation** | Les ressources peuvent être représentées dans plusieurs formats (JSON, XML) |
### Conventions de dénomination des ressources
| Faire | Ne faites pas |
|----|-------|
| `/users`(nom pluriel) | `/user`(singulier) |
| `/users/123/orders`(imbriqué) | `/getOrdersForUser?id=123`|
| `/products?category=electronics`(paramètres de requête pour le filtrage) | `/productsByCategory/electronics`|
| Utilisez des tirets :`/user-profiles`| Utiliser des traits de soulignement :`/user_profiles`|
### Méthodes HTTP et idempotence
| Méthode | Objectif | Idempotent ? | Sûr? |
|--------|---------|-------------|-------|
| **OBTENIR** | Lire une ressource | ✅ Oui | ✅ Oui |
| **POST** | Créer une ressource | ❌ Non | ❌ Non |
| **METTRE** | Remplacer entièrement une ressource | ✅ Oui | ❌ Non |
| **PATCH** | Mettre à jour partiellement une ressource | ❌ Non* | ❌ Non |
| **SUPPRIMER** | Supprimer une ressource | ✅ Oui | ❌ Non |
*PATCH peut être rendu idempotent grâce à une conception soignée.
### Codes d'état HTTP
| Codes | Signification | Quand utiliser |
|------|---------|-------------|
| **200** | D'accord | GET, PUT, PATCH, DELETE réussi |
| **201** | Créé | POST réussi (ressource créée) |
| **204** | Aucun contenu | SUPPRESSION réussie (rien à retourner) |
| **400** | Mauvaise demande | Saisie invalide ou demande mal formée |
| **401** | Non autorisé | Authentification manquante ou invalide |
| **403** | Interdit | Authentifié mais non autorisé |
| **404** | Introuvable | La ressource n'existe pas |
| **409** | Conflit | Ressource en double ou conflit d'état |
| **422** | Entité non traitable | JSON valide mais erreurs sémantiques |
| **429** | Trop de demandes | Limite de débit dépassée |
| **500** | Erreur de serveur interne | Erreur de serveur inattendue |
| **502** | Mauvaise passerelle | Panne du service en amont |
| **503** | Service indisponible | Surcharge ou maintenance temporaire |
---

## Gestion des versions de l'API
Les API évoluent. Lorsque vous devez apporter des modifications majeures, la gestion des versions permet aux clients existants de continuer à fonctionner.
| Stratégie | Exemple | Avantages | Inconvénients |
|--------------|---------|------|------|
| **Chemin URL** | `/v1/users`,`/v2/users`| Simple, explicite | Modifications d'URL par version |
| **Paramètre de requête** | `/users?version=2`| Flexible | Facile à oublier |
| **En-tête** | `Accept: application/vnd.myapi.v2+json`| Nettoyer les URL | Moins découvrable |
| **Pas de versionnage** | Evolution du schéma uniquement | Le plus simple | Les changements radicaux affectent tout le monde |
**Bonne pratique** : utilisez la gestion des versions du chemin d'URL (`/v1/`) pour plus de clarté. Prend en charge au moins une version précédente. Déprécier les anciennes versions avec des délais clairs.
---

## Méthodes d'authentification
| Méthode | Comment ça marche | Idéal pour |
|--------|-------------|--------------|
| **Clés API** | Clé secrète dans l'en-tête (`X-API-Key: abc123`) | De serveur à serveur, intégrations simples |
| **OAuth2** | Délégation basée sur des jetons avec des étendues | Accès tiers, applications autorisées par l'utilisateur |
| **JWT** | Jeton autonome avec revendications | Authentification sans état entre les services |
| **Authentification de base** | Nom d'utilisateur codé en base64 : mot de passe | Développement uniquement – ​​jamais de production sans TLS |
| **Cookies de session** | ID de session côté serveur dans le cookie HTTP uniquement | Applications Web traditionnelles |
### Flux OAuth2 (simplifié)
1. Le client redirige l'utilisateur vers le serveur d'autorisation.
2. L'utilisateur se connecte et accorde l'autorisation.
3. Le serveur d'autorisation renvoie un code d'autorisation.
4. Le client échange le code contre un jeton d'accès (et éventuellement un jeton d'actualisation).
5. Le client utilise un jeton d'accès pour appeler l'API.
6. Lorsque le jeton d'accès expire, utilisez le jeton d'actualisation pour en obtenir un nouveau.
---

## Styles d'API : REST, GraphQL et gRPC
| Fonctionnalité | REPOS | GraphQL | gRPC |
|---------|------|---------|------|
| **Format des données** | JSON (généralement) | JSON | Protobuf (binaire) |
| **Points de terminaison** | Multiple (un par ressource) | Point final unique | Défini par le fichier .proto |
| **Surcharge** | Commun (obtenez plus que nécessaire) | Aucun (le client spécifie les champs) | Aucun (défini par le schéma) |
| **Sous-récupération** | Nécessite plusieurs appels | Aucun (obtenez exactement ce dont vous avez besoin) | Aucun |
| **En temps réel** | WebSockets nécessaires | Abonnements intégrés | Streaming intégré |
| **Mise en cache** | La mise en cache HTTP fonctionne naturellement | Plus difficile à mettre en cache | Limité |
| **Courbe d'apprentissage** | Faible | Moyen | Moyen–Élevé |
| **Meilleur pour** | API publiques, applications CRUD | Interfaces utilisateur complexes, applications mobiles | Microservices internes, performants |
---

## Pagination, filtrage et tri
Pour les points de terminaison qui renvoient des listes :
| Techniques | Exemple | Quand utiliser |
|-----------|---------|-------------|
| **Décalage/Limite** | `?offset=20&limit=10`| Simple; fonctionne pour les petits ensembles de données |
| **Basé sur un curseur** | `?cursor=abc123&limit=10`| Grands ensembles de données ; résultats cohérents |
| **Jeu de clés** | `?created_after=2024-01-01&limit=10`| Très efficace ; nécessite une clé unique |
```json
// Cursor-based response
{
  "data": [...],
  "pagination": {
    "next_cursor": "abc123",
    "has_more": true
  }
}
```

---

## Limitation du débit
Protégez votre API contre les abus et garantissez une utilisation équitable.
| Stratégie | Comment ça marche |
|--------------|-------------|
| **Fenêtre fixe** | N requêtes par fenêtre horaire (par exemple, 100/heure) |
| **Fenêtre coulissante** | Plus granulaire ; compte les demandes dans la fenêtre glissante |
| **Seau à jetons** | Jetons ajoutés à taux fixe ; chaque requête consomme un jeton |
Renvoie`429 Too Many Requests`avec les en-têtes :```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1625097600
Retry-After: 60
```

---

## Gestion des erreurs
Des réponses d'erreur cohérentes facilitent grandement l'utilisation des API :
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "issue": "Invalid email format"
      }
    ]
  }
}
```

**Principes** : utilisez une structure d'erreur cohérente, incluez des messages exploitables, utilisez des codes d'état HTTP standard, enregistrez les erreurs côté serveur avec des ID de corrélation et n'exposez jamais les traces de pile ou les détails internes.
---

##Documentation API
| Outil | Descriptif |
|------|-------------|
| **OpenAPI (Swagger)** | Norme industrielle pour la documentation de l'API REST |
| **Interface utilisateur Swagger** | Documentation API interactive de la spécification OpenAPI |
| **Facteur** | Tests d'API, documentation et partage de collections |
| **Rédoc** | Magnifiques documents de référence API issus de la spécification OpenAPI |
| **Aire de jeu GraphQL / GraphiQL** | Exploration interactive de GraphQL |
**Meilleure pratique** : écrivez d'abord la spécification OpenAPI (développement basé sur les spécifications), puis générez de la documentation et des SDK client à partir de celle-ci.
---

## Modèles de passerelle API
Une passerelle API se situe entre les clients et les services backend, fournissant un point d'entrée unique.
| Responsabilité | Descriptif |
|---------------|-------------|
| **Routage** | Demandes directes aux services backend appropriés |
| **Authentification** | Valider les jetons au niveau de la passerelle |
| **Limitation de taux** | Appliquer des limites globales ou par client |
| **Transformation** | Convertir entre protocoles (REST ↔ gRPC) |
| **Mise en cache** | Mettre en cache les réponses courantes |
| **Surveillance** | Journalisation et métriques centralisées |
| **Équilibrage de charge** | Répartir le trafic entre les instances de service |
| Outil | Tapez |
|------|------|
| **Kong** | Passerelle API open source (basée sur Nginx) |
| **Passerelle API AWS** | Entièrement géré, intégré à AWS |
| **Gestion des API Azure** | Passerelle gérée avec portail développeur |
| **Envoyé / Istio** | Maillage de services avec fonctionnalités de passerelle API |
| **Traefik** | Découverte automatique, intégration Let's Encrypt |
---

## Webhooks
Les webhooks permettent à votre API de transmettre des événements aux clients en temps réel, plutôt que de demander aux clients de rechercher des modifications.
| Aspects | Meilleure pratique |
|--------|--------------|
| **Livraison** | Requête POST avec charge utile JSON vers l'URL du client |
| **Sécurité** | Signer les charges utiles avec HMAC ; le client vérifie la signature |
| **Fiabilité** | Réessayez les livraisons ayant échoué avec une interruption exponentielle |
| **Idempotence** | Incluez un ID d'événement unique ; client gère les doublons |
| **Gestion des versions** | Inclure la version de l'API dans la charge utile du webhook |
---

## Liste de contrôle de conception
-[ ] Les ressources sont des noms au pluriel (`/users`, pas`/getUser`)
- [ ] Méthodes HTTP utilisées correctement (GET pour les lectures, POST pour les créations, etc.)
- [ ] Format de réponse d'erreur cohérent
- [ ] Pagination pour tous les points de terminaison de la liste
- [ ] Limitation de débit avec des en-têtes clairs
- [ ] Définition de la stratégie de versioning de l'API
- [ ] Authentification et autorisation en place
- [ ] Validation des entrées sur tous les points de terminaison
-[ ] Documentation OpenAPI/Swagger maintenue
- [ ] CORS configuré correctement
- [ ] HTTPS appliqué en production
- [ ] Clés d'idempotence pour les opérations POST si nécessaire