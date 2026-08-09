---
# Métadonnées
titre : « Fondamentaux de la cybersécurité »
description : "Chiffrement, TLS, OWASP, codage sécurisé, SDL"
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
tags : [cybersécurité, codage et technologie]
niveau de difficulté : "intermédiaire"
prérequis : []
estimate_reading_time : "9 min"
# Guide des contributions
apport :
  licence : "MIT"
  feedback_channel : "Problèmes GitHub"
  how_to_contribute : "Soumettez un PR avec les modifications et mettez à jour le journal des modifications"
  review_process : "Les modifications sont examinées par les responsables de la catégorie avant la fusion"
---
# Fondamentaux de la cybersécurité
La sécurité n'est pas une fonctionnalité que l'on adopte en fin de compte : c'est une discipline qui doit être intégrée à chaque couche d'un système dès le premier jour. Que vous créiez une application Web, gériez une infrastructure ou expédiiez une API, il est essentiel de comprendre le paysage des menaces et les principes fondamentaux de la défense.
---

## Chiffrement et cryptographie
### Chiffrement symétrique ou asymétrique
| Tapez | Comment ça marche | Vitesse | Distribution des clés | Exemples |
|------|-------------|-------|-------|----------|
| **Symétrique** | Même clé pour le cryptage et le déchiffrement | Rapide | Défi : comment partager la clé ? | AES-256, ChaCha20 |
| **Asymétrique** | Chiffrement par clé publique, déchiffrement par clé privée | Plus lent | La clé publique peut être partagée ouvertement | RSA, ECC (courbe elliptique) |
En pratique, la plupart des systèmes utilisent les **les deux** : le chiffrement asymétrique pour échanger de manière sécurisée une clé symétrique, puis le chiffrement symétrique pour l'essentiel des données. C'est ainsi que fonctionne TLS/HTTPS.
### Hachage
Le hachage est une fonction à sens unique : il convertit l'entrée en une chaîne de taille fixe. Vous ne pouvez pas l'inverser, mais la même entrée produit toujours la même sortie.
| Cas d'utilisation | Algorithme recommandé | Éviter |
|--------------|------------|-------|
| **Stockage du mot de passe** | Argon2id, bcrypt, scrypt | MD5, SHA-1, SHA-256 simple (trop rapide) |
| **Intégrité des données** | SHA-256, SHA-3 | MD5 (cassé), SHA-1 (cassé) |
| **Signatures numériques** | Ed25519, RSA-2048+ | DSA |
### TLS/HTTPS
HTTPS est HTTP sur TLS (Transport Layer Security). Il fournit :
- **Cryptage** : les données en transit ne peuvent pas être lues par des oreilles indiscrètes.
- **Authentification** : Le serveur prouve son identité via un certificat.
- **Intégrité** : les données ne peuvent pas être modifiées en transit sans détection.
Utilisez TLS 1.2 ou 1.3. Désactivez TLS 1.0 et 1.1. Activez HSTS (HTTP Strict Transport Security) pour forcer les navigateurs à toujours utiliser HTTPS.
---

## Authentification et autorisation
### Authentification : qui êtes-vous ?
| Méthode | Niveau de sécurité | Cas d'utilisation |
|--------|---------------|--------------|
| **Mot de passe** | Faible-Moyen | Comptes de base (appliquer plus de 12 caractères, vérifier les violations) |
| **AMF (TOTP)** | Élevé | Standard pour les comptes sensibles (Google Authenticator, Authy) |
| **Clé matérielle (FIDO2/WebAuthn)** | Très élevé | Comptes haute sécurité (YubiKey) |
| **Biométrique** | Moyen–Élevé | Déverrouillage de l'appareil (empreinte digitale, visage) – pas génial comme seul facteur |
| **OAuth2 / OIDC** | Élevé | Connexion tierce (« Connectez-vous avec Google ») |
**Règles de mot de passe** : appliquez une longueur minimale (12 à 16 caractères), vérifiez les listes de mots de passe violés, utilisez Argon2id ou bcrypt pour le hachage avec des sels par utilisateur.
### Autorisation : que pouvez-vous faire ?
| Modèle | Descriptif | Exemple |
|-------|-------------|---------|
| **RBAC** (Contrôle d'accès basé sur les rôles) | Autorisations attribuées aux rôles ; les utilisateurs obtiennent des rôles | Administrateur, éditeur, visualiseur |
| **ABAC** (basé sur les attributs) | Règles basées sur les attributs utilisateur, la ressource, l'environnement | "Les managers peuvent approuver les demandes de leur équipe" |
| **ACL** (Liste de contrôle d'accès) | Autorisations explicites par utilisateur/ressource | Autorisations de fichiers (lecture/écriture/exécution) |
**Principe du moindre privilège** : accordez à chaque utilisateur, service et processus uniquement l'accès minimum dont il a besoin.
### JWT (jetons Web JSON)
| Aspects | Recommandation |
|--------|---------------|
| **Signature** | RS256 ou ES256 (asymétrique) préféré ; HS256 acceptable avec secrets gérés |
| **Expiration** | 15 à 60 minutes pour les jetons d'accès ; utiliser des jetons d'actualisation pour les sessions plus longues |
| **Stockage** | Cookies HTTP uniquement (pas localStorage — vulnérables à XSS) |
| **Validation** | Vérifiez toujours la signature, l'émetteur, l'audience et l'expiration |
---

## OWASP Top 10 (2021)
L'OWASP Top 10 est le document standard de sensibilisation à la sécurité des applications Web. Il représente les risques les plus critiques :
| # | Risque | Ce que cela signifie |
|---|------|--------------|
| 1 | **Contrôle d'accès cassé** | Les utilisateurs peuvent accéder à des ressources qu'ils ne devraient pas |
| 2 | **Échecs cryptographiques** | Chiffrement faible ou manquant pour les données sensibles |
| 3 | **Injection** | SQL, NoSQL, commande OS ou injection LDAP |
| 4 | **Conception non sécurisée** | Défauts architecturaux qui ne peuvent pas être corrigés avec la mise en œuvre |
| 5 | **Mauvaise configuration de la sécurité** | Mots de passe par défaut, ports ouverts, messages d'erreur détaillés |
| 6 | **Composants vulnérables** | CVE connus dans les dépendances |
| 7 | **Échecs d'authentification** | Mots de passe faibles, mauvaise gestion de session |
| 8 | **Échecs d'intégrité** | Attaques de la chaîne d'approvisionnement, mises à jour non signées |
| 9 | **Échecs de journalisation/surveillance** | Aucune détection de violations |
| 10 | **SSRF** | serveur trompé pour qu'il envoie des requêtes aux systèmes internes |
---

## Pratiques de codage sécurisées
### Validation des entrées
| Règle | Pourquoi |
|------|-----|
| **Liste blanche > Liste noire** | Définir ce qui est autorisé et non ce qui est bloqué |
| **Requêtes paramétrées** | Ne concaténez jamais les entrées utilisateur dans SQL – utilisez des instructions préparées ou ORM |
| **Encodage HTML** | Encodez`<`,`>`,`&`,`"`,`'`pour empêcher XSS |
| **Coquille s'échappant** | Évitez de créer des commandes shell à partir des entrées de l'utilisateur ; utiliser`shlex.quote()`|
| **Limites de longueur** | Appliquer des longueurs maximales pour éviter les débordements de tampon et les DoS |
| **Vérification du type** | Assurez-vous que les entiers sont des entiers et que les booléens sont des booléens |
### Vulnérabilités courantes
| Vulnérabilité | Attaque | Défense |
|--------------|--------|---------|
| **Injection SQL** | `' OR 1=1 --`dans le formulaire de connexion | Requêtes paramétrées |
| **XSS** | `<script>alert('hacked')</script>`dans le champ de commentaire | Encodage de sortie, politique de sécurité du contenu |
| **CSRF** | Tromper le navigateur de l'utilisateur pour qu'il fasse une demande non autorisée | Jetons CSRF, cookies SameSite |
| ** Traversée du chemin ** | `../../etc/passwd`dans le paramètre du fichier | Valider et nettoyer les chemins de fichiers |
| **IDEUR** | Remplacez`/user/123`par`/user/124`pour voir les données de quelqu'un d'autre | Contrôles d'autorisation à chaque demande |
---

## Sécurité du réseau
### Pare-feu
| Tapez | Descriptif |
|------|-------------|
| ** Filtrage de paquets ** | Règles basées sur IP, port, protocole |
| **Avec état** | Suit les états de connexion ; filtrage plus intelligent |
| **Niveau application (WAF)** | Inspecte le trafic HTTP ; bloque l'injection SQL, XSS, etc. |
| **Groupes de sécurité cloud** | Pare-feu virtuels pour les instances cloud (AWS SG, Azure NSG) |
**Règle générale** : bloquez tout le trafic entrant par défaut ; n'ouvrez que ce qui est explicitement nécessaire (80, 443 pour le Web).
### Segmentation du réseau
Placez les bases de données et les caches dans des sous-réseaux privés sans accès direct à Internet. Utilisez une DMZ pour les services publics (serveurs Web, équilibreurs de charge). Appliquez le principe du moindre privilège à l’accès au réseau.
---

## Gestion des secrets
### La règle d'or
**Ne codez jamais de secrets en dur.** Aucune clé API, mot de passe ou URL de base de données dans le code source. Aucun secret dans les variables d'environnement validées dans Git. Aucun secret dans les images Docker.
### Outils
| Outil | Tapez | Idéal pour |
|------|------|----------|
| **Coffre-fort HashiCorp** | Gestionnaire de secrets d'entreprise | Secrets dynamiques, chiffrement en tant que service |
| **Gestionnaire de secrets AWS** | Natif du cloud | Environnements AWS |
| **Coffre de clés Azure** | Natif du cloud | Environnements Azure |
| **SOPS** | Fichiers cryptés | Chiffrer les secrets dans Git (avec KMS ou GPG) |
| **Secrets Docker** | Natif du conteneur | Docker Swarm (pour les K8, pensez à Secrets Store CSI) |
| **dotenv (.env)** | Développement local | Développement uniquement – ​​jamais en production ni engagé |
### Rotation
Faites pivoter les secrets régulièrement et automatiquement. Si un secret est divulgué (par exemple, s'il est déposé dans un dépôt public), faites-le immédiatement pivoter, même si vous pensez que personne ne l'a vu.
---

## Sécurité des dépendances
Votre application est aussi sécurisée que sa dépendance la plus faible.
### Outils d'analyse
| Langue | Outils |
|--------------|-------|
| **Python** | `safety`,`pip-audit`,`bandit`|
| **Node.js** | `npm audit`,`yarn audit`,`snyk`|
| **Rouille** | `cargo audit`|
| **Allez** | `govulncheck`|
| **Général** | `Dependabot`(GitHub),`Renovate`,`Trivy`|
### Intégrité de la chaîne d'approvisionnement
- Utilisez des fichiers de verrouillage (`package-lock.json`,`Cargo.lock`,`go.sum`) pour des builds reproductibles.
- Vérifiez les sommes de contrôle des dépendances téléchargées.
- Préférez les registres officiels et les éditeurs vérifiés.
- Automatisez les mises à jour mineures/correctives via Dependabot ou Renovate.
---

## Cycle de vie du développement de la sécurité (SDL)
| Phases | Activité |
|-------|--------------|
| **Formation** | Assurez-vous que les développeurs comprennent les vulnérabilités courantes |
| **Modélisation des menaces** | Identifier les menaces potentielles lors de la conception |
| **Normes de codage sécurisé** | Appliquer via des linters et des listes de contrôle de révision de code |
| **SAST** | Analyse statique du code source (SonarQube, CodeQL) |
| **DAST** | Analyse dynamique de l'application en cours d'exécution (OWASP ZAP, Burp Suite) |
| **SCA** | Analyse de la composition logicielle — analyser les dépendances |
| **Tests d'intrusion** | Exercices réguliers de hacking éthique |
| **Bug Bounty** | Encourager les chercheurs externes à trouver des vulnérabilités |
| **Plan de réponse aux incidents** | Avoir un plan clair lorsqu'une violation est détectée |
---

## Liste de contrôle d'urgence
Lorsque vous soupçonnez une violation :
1. **Ne paniquez pas**, mais agissez rapidement.
2. **Isolez** les systèmes concernés (déconnectez-vous du réseau si nécessaire).
3. **Préserver les preuves** : capturez les journaux, les vidages de mémoire, les images disque.
4. **Identifier le périmètre** : quels systèmes, quelles données ?
5. **Faites pivoter** tous les identifiants et secrets compromis.
6. **Corrigez** la vulnérabilité.
7. **Informer** les utilisateurs et les régulateurs concernés si nécessaire (dans les délais légaux).
8. **Post-mortem** : documentez la cause première et les mesures à prendre dans les 24 à 48 heures.