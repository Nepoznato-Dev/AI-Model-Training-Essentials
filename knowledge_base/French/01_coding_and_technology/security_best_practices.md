---
# Metadata
title: "Security Best Practices"
description: "OWASP Top 10, input validation, auth, secrets management"
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
tags: [security, best, practices, coding-and-technology]
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
# Meilleures pratiques de sécurité
Un guide pratique pour sécuriser les applications, l'infrastructure et les données, du développement à la production.
---

## OWASP Top 10 (2021) — Aperçu
1. **Contrôle d'accès brisé** : les utilisateurs peuvent accéder à des ressources qu'ils ne devraient pas.
2. **Échecs cryptographiques** : cryptage faible ou manquant.
3. **Injection** : SQL, NoSQL, commande du système d'exploitation ou injection LDAP.
4. **Conception non sécurisée** : défauts architecturaux.
5. **Mauvaise configuration de sécurité** : mots de passe par défaut, ports ouverts, erreurs détaillées.
6. **Composants vulnérables et obsolètes** : CVE connus dans les dépendances.
7. **Échecs d'identification et d'authentification** : mots de passe faibles, mauvaise gestion de session.
8. **Défaillances d'intégrité des logiciels et des données** : attaques de la chaîne d'approvisionnement, mises à jour non signées.
9. **Échecs de journalisation et de surveillance de sécurité** : aucune détection de violations.
10. **Server-Side Request Forgery (SSRF)** : Abus du serveur pour envoyer des requêtes aux systèmes internes.
---

## Validation d'entrée et encodage de sortie
### Règles de validation
- **Liste blanche > Liste noire** : définissez les modèles autorisés (par exemple, regex pour les e-mails) plutôt que de bloquer les mauvais modèles connus.
- **Limites de longueur** : appliquez des longueurs maximales pour éviter les débordements de tampon et les DoS.
- **Vérification de type** : assurez-vous que les entiers sont des entiers et que les booléens sont des booléens.
- **Utilisez des bibliothèques bien testées** : pour la validation des e-mails, des URL et des dates, utilisez des bibliothèques standard (par exemple,`email-validator`en Python,`validator.js`dans Node).
### Encodage de sortie
- **Encodage HTML** : Encodez`<`,`>`,`&`,`"`,`'`pour empêcher XSS.
- **Paramétrage SQL** : ne concaténez jamais les entrées utilisateur dans les requêtes SQL. Utilisez des requêtes paramétrées (instructions préparées) ou un ORM.
- **Échappement du shell** : évitez de créer des commandes shell à partir de l'entrée de l'utilisateur ; si cela est inévitable, utilisez`shlex.quote()`ou similaire.
---

## Authentification et autorisation
### Gestion des mots de passe
- **Hashing** : stockez les mots de passe avec un algorithme de hachage puissant et lent : **Argon2id** (de préférence), **bcrypt**, **scrypt** ou **PBKDF2**.
- **Salage** : ajoutez un sel unique par utilisateur.
- **Longueur minimale** : imposez au moins 12 à 16 caractères.
- **MFA (Multi-Factor Authentication)** : Nécessite un deuxième facteur (TOTP, SMS, clé matérielle) pour les opérations sensibles.
- **Limitation du débit** : empêchez les tentatives de force brute sur les points de terminaison de connexion (par exemple, 5 tentatives toutes les 5 minutes par IP/utilisateur).
### Gestion des sessions
- Utilisez des cookies SameSite sécurisés, HTTP uniquement pour les jetons de session.
- Définissez des délais d'expiration appropriés.
- Invalider les sessions à la déconnexion et au changement de mot de passe.
- Évitez d'exposer les identifiants de session dans les URL.
### OAuth2/OIDC
- Utilisez des bibliothèques bien établies (par exemple Authlib, PyJWT, Passport.js, Spring Security).
- Validez minutieusement les jetons d'identification (signature, émetteur, audience, expiration).
- Utilisez les paramètres d'état pour empêcher CSRF.
- Gardez les secrets des clients confidentiels.
### JWT (jetons Web JSON)
- **Sign** : Utilisez RS256 ou ES256 (asymétrique) pour une meilleure sécurité ; HS256 (symétrique) est acceptable si les secrets partagés sont bien gérés.
- **Valider** : vérifiez toujours la signature, l'émetteur (`iss`), l'audience (`aud`) et l'expiration (`exp`).
- **Gardez une expiration courte** : 15 à 60 minutes pour les jetons d'accès ; utilisez des jetons d’actualisation pour les sessions plus longues.
- **Stocker en toute sécurité** : ne stockez jamais les JWT dans localStorage (vulnérable à XSS) ; utilisez plutôt des cookies HTTP uniquement.
---

## Sécurité des API
### Authentification
- Authentifiez toujours les appels API (sauf les points de terminaison publics).
- Préférez les clés API ou les jetons OAuth2 à l'authentification de base (qui envoie des informations d'identification à chaque demande).
### Limitation et limitation du débit
- Appliquez des limites de débit par utilisateur et par IP pour éviter les abus et les DoS.
- Renvoie`429 Too Many Requests`avec un en-tête `Retry-After`.
### CORS (partage de ressources inter-origines)
- Autoriser uniquement des origines spécifiques (jamais`*`en production).
- Validez l'en-tête`Origin`côté serveur.
### Validation des entrées
- Validez tous les paramètres de la demande, y compris les en-têtes et le corps.
- Rejetez les champs inattendus (`"strict": true`ou`additionalProperties: false`dans le schéma JSON).
### HTTPS/TLS
- Appliquer HTTPS en production.
- Utilisez HSTS (HTTP Strict Transport Security) pour forcer les navigateurs à utiliser HTTPS.
- Utilisez TLS 1.2 ou 1.3 (désactivez TLS 1.0/1.1).
---

## Gestion des secrets
### Ne jamais coder en dur les secrets
- Ne confiez pas de secrets (clés API, mots de passe, URL de base de données) au contrôle de code source.
- Utiliser des variables d'environnement ou des outils de gestion de secrets.
### Outils
| Outil | Descriptif |
|------|-------------|
| **Coffre-fort HashiCorp** | Secrets dynamiques de niveau entreprise |
| **AWS Secrets Manager/Azure Key Vault/GCP Secret Manager** | Natif du cloud |
| **SOPS** | Chiffrer les secrets des fichiers et les valider (avec KMS ou GPG) |
| **Secrets Docker** | Pour le mode Essaim ; Secrets Kubernetes (envisagez le pilote CSI externe Secrets Store) |
### Rotation
- Effectuez régulièrement une rotation des secrets et des comptes de service.
- Automatisez la rotation lorsque cela est possible.
---

## Gestion des dépendances
### Analyse des vulnérabilités
| Langue/Plateforme | Outils |
|---------|-------|
| **Python** | `safety`,`pip-audit`,`bandit`|
| **Nœud** | `npm audit`,`yarn audit`,`snyk`|
| **Rouille** | `cargo audit`|
| **Allez** | `govulncheck`|
| **Général** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Correction
- Gardez les dépendances à jour avec les versions corrigées.
- Configurer des demandes d'extraction automatisées pour les mises à jour mineures/correctives.
- Consultez les journaux des modifications pour détecter les modifications importantes.
### Intégrité de la chaîne d'approvisionnement
- Utilisez les fichiers de verrouillage du package (`package-lock.json`,`Cargo.lock`,`go.sum`) pour garantir des builds reproductibles.
- Vérifiez les sommes de contrôle des dépendances téléchargées.
- Préférez les registres officiels et faites confiance uniquement aux éditeurs vérifiés.
---

## Sécurité des infrastructures
### Pare-feu
- Bloquez tous les ports entrants, à l'exception de ceux explicitement nécessaires (par exemple, 80, 443).
- Limitez l'accès SSH à des plages IP spécifiques (ou utilisez un hôte VPN/bastion).
- Utilisez des groupes de sécurité (AWS) ou des NSG (Azure) pour un contrôle précis.
### Renforcement du système d'exploitation
- Appliquez régulièrement les mises à jour de sécurité (`sudo apt upgrade`,`yum update`).
- Désactivez les services inutiles et les comptes par défaut.
- Utilisez fail2ban pour bloquer les tentatives de force brute sur SSH.
- Renforcez SSH : désactivez la connexion root, utilisez l'authentification par clé, modifiez le port par défaut (facultatif).
### Segmentation du réseau
- Placez les bases de données et les caches dans des sous-réseaux privés sans accès à Internet.
- Utilisez une DMZ pour les services destinés au public.
- Appliquer le principe du moindre privilège à l'accès au réseau.
### Secrets dans les infrastructures
- Ne stockez jamais de secrets dans des variables d'environnement CI/CD à moins qu'ils ne soient chiffrés.
- Utilisez les rôles IAM du fournisseur de cloud pour les instances EC2/VM au lieu de clés à longue durée de vie.
---

## Journalisation et surveillance
### Quoi enregistrer
- Événements d'authentification (succès/échec).
- Décisions de contrôle d'accès (échecs d'autorisation).
- Actions d'administration (création d'utilisateurs, suppression, modifications d'autorisations).
- Modifications du schéma de la base de données.
- Erreurs système et exceptions.
- Requêtes et réponses API (expurger les données sensibles).
### Ce qu'il ne faut pas enregistrer
- Mots de passe, secrets, jetons, PII (informations personnelles identifiables) à moins qu'ils ne soient hachés/expurgés.
- Numéros complets de carte de crédit.
### Alerte
- Configurer des alertes pour :
  - Plusieurs échecs de connexion (force brute potentielle).
  - Modèles d'accès inhabituels (par exemple, depuis de nouveaux emplacements, à des heures impaires).
  - Nouveaux comptes administrateur créés.
  - Taux d'erreur élevés ou pics de latence.
- Utiliser un SIEM (Security Information and Event Management) pour une corrélation avancée.
### Conservation des journaux
- Conservez les journaux pendant au moins 30 à 90 jours en fonction des exigences réglementaires.
- Stockez les journaux dans un système centralisé et inviolable (par exemple, ELK Stack, Splunk, Datadog).
---

## Cycle de vie de développement sécurisé (SDL)
1. **Formation** : assurez-vous que les développeurs comprennent les vulnérabilités courantes.
2. **Modélisation des menaces** : identifiez les menaces potentielles dès le début de la conception.
3. **Normes de codage sécurisées** : appliquer via des linters et des listes de contrôle de révision de code.
4. **SAST** (Static Application Security Testing) : analysez le code source à la recherche de vulnérabilités (SonarQube, CodeQL).
5. **DAST** (Dynamic Application Security Testing) : analyse les applications en cours d'exécution (OWASP ZAP, Burp Suite).
6. **SCA** (Software Composition Analysis) : analyser les dépendances.
7. **Tests d'intrusion** : exercices réguliers de piratage éthique.
8. **Bug bounty** : encouragez les chercheurs externes à rechercher les vulnérabilités de manière responsable.
9. **Plan de réponse aux incidents** : ayez un plan clair lorsqu'une violation est détectée.
---

## Liste de contrôle d'urgence (lorsqu'une violation est suspectée)
1. **Ne paniquez pas**, mais agissez rapidement.
2. **Isolez** les systèmes concernés (déconnectez-vous du réseau si nécessaire).
3. **Préservez les preuves** : capturez les journaux, les vidages de mémoire et les images disque.
4. **Identifier** le périmètre : quels systèmes, quelles données.
5. **Faites pivoter** tous les identifiants et secrets compromis.
6. **Corrigez** la vulnérabilité.
7. **Informer** les utilisateurs concernés et les organismes de réglementation si nécessaire (dans les délais légaux).
8. **Effectuer une autopsie** pour comprendre la cause profonde et améliorer les processus.