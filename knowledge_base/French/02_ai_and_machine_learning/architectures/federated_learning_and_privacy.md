---
# Metadata
title: "Federated Learning and Privacy"
description: "Decentralised training, differential privacy, secure aggregation"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [federated, learning, privacy, ai-and-machine-learning]
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

# Apprentissage fédéré et confidentialité
L'apprentissage fédéré est une technique permettant de former des modèles d'apprentissage automatique sur plusieurs appareils ou organisations sans partager les données brutes. Au lieu d'envoyer des données à un serveur central, chaque appareil entraîne un modèle local et partage uniquement les mises à jour du modèle (dégradés ou poids). Le serveur central regroupe ces mises à jour pour produire un modèle global. Il a été conçu par Google pour entraîner des modèles de langage de clavier sur les téléphones Android – et est depuis devenu une technique clé pour l’IA préservant la confidentialité.
---

## Pourquoi l'apprentissage fédéré ?
| Motivation | Descriptif | Exemple |
|------------|-------------|---------|
| **Confidentialité des données** | Les données brutes ne quittent jamais l'appareil | Les dossiers médicaux restent à l’hôpital ; les photos restent au téléphone |
| **Conformité réglementaire** | Le RGPD, la HIPAA et d'autres réglementations restreignent le partage de données | Les banques peuvent collaborer sans partager les données des clients |
| **Volume de données** | Le déplacement de données est coûteux et lent | La formation sur des milliards de téléphones n'est pas pratique si les données doivent être téléchargées |
| **Sensibilité des données** | Certaines données sont trop sensibles pour être partagées, même avec consentement | Renseignement gouvernemental ; données personnelles de santé |
---

## Comment fonctionne l'apprentissage fédéré
### Le protocole de base (FedAvg)
| Étape | Que se passe-t-il |
|------|-------------|
| **1. Initialiser** | Le serveur central crée un modèle global avec des poids aléatoires |
| **2. Distribuer** | Le serveur envoie le modèle global actuel aux appareils sélectionnés |
| **3. Formation locale** | Chaque appareil entraîne le modèle sur ses données locales pendant plusieurs époques |
| **4. Télécharger** | Les appareils renvoient leurs poids de modèle mis à jour (et non leurs données) au serveur |
| **5. Agrégat** | Le serveur fait la moyenne des pondérations (Federated Averaging) pour créer un nouveau modèle global |
| **6. Répéter** | Revenez à l'étape 2 jusqu'à ce que le modèle converge |
```
Server: global_model = average(local_model_1, local_model_2, ..., local_model_n)
```

### Propriétés clés
| Propriété | Descriptif |
|--------------|-------------|
| **Données non IID** | Chaque appareil a des distributions de données différentes (non indépendantes et distribuées de manière identique) |
| **Données déséquilibrées** | Certains appareils contiennent beaucoup de données, d'autres très peu |
| **Participation partielle** | Tous les appareils ne sont pas disponibles à chaque tour |
| **Efficacité de la communication** | Le goulot d'étranglement est la communication, pas le calcul |
---

## Variantes d'apprentissage fédéré
| Variante | Descriptif | Avantage |
|---------|-------------|---------------|
| **Moyenne Fed** | Poids moyens des modèles sur tous les appareils | Simple; fonctionne bien pour les données IID |
| **FedProx** | Ajoute un terme proximal à la formation locale | Mieux pour les données non-IID |
| **ÉCHAFAUDAGE** | Utilise des variables de contrôle pour corriger l'hétérogénéité des données | Convergence plus rapide sur les données non-IID |
| **FedSGD** | Comme FedAvg mais avec un pas de dégradé par tour | Coût de communication réduit par tour |
| **FL personnalisé** | Chaque appareil conserve un modèle personnalisé parallèlement au modèle global | Meilleures performances par appareil |
| **FL vertical** | Différentes fonctionnalités (et non des échantillons différents) selon les parties | Lorsque les parties détiennent différents aspects des mêmes données |
---

## Confidentialité différentielle
La confidentialité différentielle (DP) fournit une garantie mathématique que le résultat d'un algorithme ne révèle pas si les données d'un individu ont été incluses.
### Définition de base
Un mécanisme M satisfait à la confidentialité différentielle (ε, δ) si pour deux ensembles de données D et D' qui diffèrent dans un enregistrement :
```
P(M(D) ∈ S) ≤ e^ε × P(M(D') ∈ S) + Î´
```

| Paramètre | Signification |
|-----------|---------|
| **ε (epsilon)** | Budget de confidentialité. Plus petit = plus privé. Valeurs typiques : 0,1 à 10. |
| **δ (delta)** | Probabilité d’échec de la garantie de confidentialité. Généralement défini sur 1/N (inverse de la taille de l'ensemble de données). |
### Mécanismes pour ajouter de la confidentialité
| Mécanisme | Comment ça marche | Cas d'utilisation |
|---------------|-------------|--------------|
| **Mécanisme gaussien** | Ajouter du bruit gaussien calibré à la sensibilité de la requête | Valeurs continues (poids du modèle) |
| **Mécanisme Laplace** | Ajouter du bruit de Laplace | Comptage des requêtes |
| **Mécanisme exponentiel** | Sélectionner les résultats avec une probabilité proportionnelle à leur utilité | Choix discrets |
### DP-SGD (Descente de gradient stochastique différentiellement privée)
| Étape | Descriptif |
|------|-------------|
| 1. Calculer les dégradés par échantillon | Au lieu de dégradés par lots |
| 2. Dégradés de clips | Lier la norme maximale de chaque gradient (limite l'influence de tout échantillon unique) |
| 3. Ajouter du bruit | Ajouter un bruit gaussien calibré au gradient agrégé |
| 4. Mettre à jour les paramètres | Marche de descente de pente standard |
| Compromis | Descriptif |
|---------------|-------------|
| **Confidentialité vs précision** | Une confidentialité plus forte (ε inférieur) nécessite plus de bruit, ce qui réduit la précision du modèle |
| **Confidentialité par rapport au temps de formation** | Plus de bruit signifie une convergence plus lente |
| **Suivi du budget de confidentialité** | Chaque étape de formation consomme une partie du budget de confidentialité ; une fois dépensé, il ne peut pas être récupéré |
---

## Combiner l'apprentissage fédéré avec une confidentialité différentielle
| Couche | Protection |
|-------|---------------|
| **Apprentissage fédéré** | Les données brutes restent sur les appareils |
| **Confidentialité différentielle** | Même les mises à jour des modèles sont bruyantes, protégeant les contributions individuelles |
| **Agrégation sécurisée** | Le serveur ne voit que l'ensemble de toutes les mises à jour, pas les mises à jour individuelles |
Cette combinaison offre de solides garanties de confidentialité : même si le serveur est compromis, il ne peut pas déterminer si les données d'un individu spécifique ont été utilisées dans le cadre de la formation.
---

## Autres techniques de préservation de la confidentialité
### Calcul multipartite sécurisé (SMPC)
Plusieurs parties calculent une fonction sur leurs données combinées sans révéler leurs entrées individuelles.
| Fonctionnalité | Descriptif |
|---------|-------------|
| **Comment ça marche** | Les données sont divisées en partages répartis entre les parties ; le calcul s'effectue sur les actions |
| **Garantie** | Aucun parti n'apprend rien des contributions des autres |
| **Frais généraux** | Coût de communication et de calcul important |
| **Cas d'utilisation** | Les banques calculent des modèles de risque communs sans partager les données des clients |
### Cryptage homomorphe (HE)
Effectuez des calculs directement sur des données cryptées.
| Tapez | Ce qu'il prend en charge | Frais généraux |
|------|-----------------|----------|
| **Partiellement HE** | Une opération (addition OU multiplication) | Faible |
| **Un peu IL** | Nombre limité des deux opérations | Moyen |
| **Entièrement IL** | Calculs arbitraires | Très élevé (ralentissement 100-1000x) |
| Demande | Descriptif |
|-------------|-------------|
| **Inférence privée** | Exécutez des modèles ML sur des données chiffrées ; renvoyer des prédictions cryptées |
| **Formation cryptée** | Se former sur des données chiffrées (encore majoritairement théorique pour le deep learning) |
| **Requêtes privées** | Interroger une base de données sans révéler la requête ou les données |
### Environnements d'exécution de confiance (TEE)
Isolation matérielle (Intel SGX, ARM Trustzone) qui protège les données même du système d'exploitation.
| Avantage | Limitation |
|---------------|------------|
| Performances quasi natives | Nécessite du matériel spécifique |
| De fortes garanties de sécurité | Mémoire limitée (taille de l'enclave) |
| Aucune surcharge cryptographique | Attaques par canal secondaire possibles |
---

## Règlements de confidentialité et ML
| Réglementation | Région | Impact sur le ML |
|------------|--------|-------------|
| **RGPD** | UE | Droit à l’explication ; minimisation des données ; consentement au traitement ; droit à l'effacement |
| **CCPA** | Californie | Droit de connaître, de supprimer et de refuser la vente de données |
| **HIPAA** | États-Unis (soins de santé) | Des contrôles stricts sur les données de santé ; exigences de désidentification |
| **PIPL** | Chine | Localisation des données ; les exigences en matière de consentement ; règles de transfert transfrontalier |
| **Loi sur l'IA** | UE | Exigences de transparence ; classification des risques ; pratiques interdites |
### Impact sur les workflows ML
| Principe RGPD | Implications du ML |
|----------------|--------------------|
| **Minimisation des données** | Collectez uniquement ce qui est nécessaire ; l'apprentissage fédéré aide |
| **Limitation de l'objectif** | Impossible de réutiliser les données sans un nouveau consentement |
| **Droit à l'effacement** | Doit être capable de supprimer les données d'une personne d'un modèle entraîné (désapprentissage automatique) |
| **Droit à l'explication** | Les modèles doivent être suffisamment interprétables pour expliquer les prédictions individuelles |
| **Confidentialité dès la conception** | La confidentialité doit être intégrée dès le départ aux systèmes |
---

## Défis
| Défi | Descriptif |
|---------------|-------------|
| **Coût de communication** | L'envoi de mises à jour de modèles sur des millions d'appareils coûte cher |
| **Données non IID** | Les appareils ont des distributions de données très différentes, ce qui nuit à la convergence |
| **Retardateurs** | Les appareils lents retardent tout le tour |
| **Compromis entre confidentialité et utilité** | Une confidentialité plus forte signifie de moins bonnes performances du modèle |
| **Attaques d'empoisonnement** | Des participants malveillants peuvent corrompre le modèle mondial |
| **Extraction de modèle** | Même les mises à jour de modèles partagés peuvent divulguer des informations sur les données d'entraînement |
| **Hétérogénéité matérielle** | Différents appareils ont des capacités de calcul différentes |
---

## Outils et cadres
| Outil | Objectif |
|------|--------------|
| **Fleur** | Cadre d'apprentissage fédéré open source ; indépendant du framework |
| **TensorFlow fédéré** | Framework FL de Google pour les modèles TensorFlow |
| **PySyft** (OpenMined) | ML préservant la confidentialité dans PyTorch |
| **SORT** (Webank) | Plateforme d'apprentissage fédérée de qualité industrielle |
| **FEUILLE** | Suite de référence pour la recherche sur l'apprentissage fédéré |
| **Opacus** (Méta) | Confidentialité différentielle pour PyTorch |
| **Confidentialité TF de Google** | Confidentialité différentielle pour TensorFlow |
---

## Résumé
Les techniques d’apprentissage fédéré et de préservation de la confidentialité répondent à une tension fondamentale : comment créer des modèles d’IA puissants lorsque les données sont distribuées, sensibles ou réglementées ? L'apprentissage fédéré conserve les données sur les appareils et partage uniquement les mises à jour des modèles. La confidentialité différentielle ajoute des garanties mathématiques selon lesquelles les contributions individuelles ne peuvent pas être détectées. Le calcul sécurisé et le cryptage homomorphe vont plus loin, permettant le calcul sur des données cryptées. Chaque technique a des coûts – frais de communication, précision réduite, dépenses de calcul – mais ensemble, elles forment une boîte à outils pour créer une IA qui respecte la confidentialité tout en apprenant des données du monde.