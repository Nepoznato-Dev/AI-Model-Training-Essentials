---
# Métadonnées
titre : "Méthodologies de test"
description : "Unité, intégration, E2E, TDD, BDD, pyramides de tests"
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
tags : [tests, méthodologies, codage et technologie]
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
# Méthodologies de test
Les tests vous permettent d'être sûr que votre code fonctionne et, plus important encore, que les modifications apportées à celui-ci n'altèrent pas ce qui fonctionne déjà. De bons tests détectent les bogues avant les utilisateurs, documentent le comportement attendu et permettent une refactorisation sans peur. Ce fichier couvre l'ensemble des stratégies de test, des tests unitaires aux tests de bout en bout, ainsi que les principes qui rendent les tests efficaces.
---

## La pyramide des tests
La pyramide des tests décrit la répartition idéale des tests dans un projet.
```
        /  E2E  \          ← Few; slow; expensive; test the whole system
       /─────────\
      / Integration\       ← Some; test how components work together
     /───────────────\
    /   Unit Tests    \    ← Many; fast; cheap; test individual functions
   /─────────────────────\
```

| Niveau | Comte | Vitesse | Coût | Ce qu'il teste |
|-------|-------|-------|------|--------------|
| **Unité** | Beaucoup | Rapide (ms) | Faible | Fonctions individuelles, classes, méthodes |
| **Intégration** | Certains | Moyen (100 ms-s) | Moyen | Comment les composants interagissent ; requêtes de base de données ; Appels API |
| **E2E** | Peu | Lent (secondes-minutes) | Élevé | L'utilisateur complet circule à travers le système réel |
---

## Tests unitaires
Tester des unités individuelles de code de manière isolée.
### Principes
| Principe | Descriptif |
|---------------|-------------|
| **Rapide** | Chaque test doit s'exécuter en millisecondes |
| **Isolé** | Les tests ne dépendent pas les uns des autres ; pas d'état partagé |
| **Déterministe** | Même entrée → même sortie à chaque fois (pas de caractère aléatoire, pas de dépendance temporelle) |
| **Auto-vérification** | Le test réussit ou échoue automatiquement ; pas d'inspection manuelle |
| **En temps opportun** | Écrit à côté ou avant le code (TDD) |
### Anatomie d'un test
| Phases | Descriptif |
|-------|-------------|
| **Organiser** | Configurer les données de test et les dépendances |
| **Agir** | Appeler la fonction ou la méthode testée |
| **Affirmer** | Vérifier que le résultat correspond aux attentes |
### Que tester
| Catégorie | Exemples |
|----------|---------|
| **Chemin heureux** | Les intrants normaux produisent les résultats attendus |
| **Cas extrêmes** | Entrée vide, nulle, zéro, valeurs maximales, élément unique |
| **Cas d'erreur** | Entrée invalide, données manquantes, autorisation refusée |
| **Conditions aux limites** | Un par un ; exactement aux limites |
### Moquerie et stubbing
| Terme | Descriptif | Quand utiliser |
|------|-------------|-------------|
| **Mock** | Un faux objet qui enregistre comment il s'appelait | Vérifier les interactions (cette méthode s'appelle-t-elle ?) |
| **Stub** | Un faux objet qui renvoie des valeurs prédéterminées | Fournir des données de test (renvoyer cet utilisateur de la base de données) |
| **Espion** | Un wrapper qui enregistre les appels vers un objet réel | Vérification partielle |
| **Faux** | Une implémentation simplifiée mais fonctionnelle | Base de données en mémoire pour les tests |
| Bibliothèque moqueuse | Langue |
|----------------|--------|
| **unittest.mock** | Python |
| **Blague** | JavaScript/TypeScript |
| **Mockito** | Java |
| **Moq** | C# |
| **témoigner / se moquer** | Aller |
---

## Tests d'intégration
Tester la façon dont plusieurs composants fonctionnent ensemble.
| Que tester | Exemple |
|-------------|---------|
| **Requêtes de base de données** | L’ORM produit-il du SQL correct ? Des index sont-ils utilisés ? |
| **Points de terminaison de l'API** | Le cycle complet demande-réponse fonctionne-t-il ? |
| **Interactions avec les services** | Le service A appelle-t-il correctement le service B ? |
| **Dépendances externes** | L'intégration de la passerelle de paiement fonctionne-t-elle ? |
### Stratégies
| Stratégie | Descriptif | Compromis |
|--------------|-------------|---------------|
| **Véritables dépendances** | Utilisez une vraie base de données, une vraie file d'attente de messages | Le plus réaliste ; Ralentissez; plus difficile à mettre en place |
| **Conteneurs de test** | Faites tourner les conteneurs Docker pour chaque exécution de test | Bon équilibre ; reproductible |
| **Alternatives en mémoire** | H2 au lieu de PostgreSQL ; bus de messages en mémoire | Rapide; peuvent manquer des problèmes du monde réel |
| **Tests sous contrat** | Vérifier que les services honorent leurs contrats API | Capture les modifications de l'interface |
---

## Tests de bout en bout (E2E)
Tester le système complet du point de vue de l'utilisateur.
| Outil | Tapez | Idéal pour |
|------|------|----------|
| **Dramaturge** | Automatisation du navigateur | Applications Web ; multi-navigateur |
| **Cyprès** | Automatisation du navigateur | Applications Web ; expérience développeur |
| **Sélénium** | Automatisation du navigateur | Héritage; prise en charge linguistique étendue |
| **Désintoxication** | Mobile E2E | Applications natives React |
| **Appium** | Mobile E2E | Applications mobiles natives et hybrides |
| **Maestro** | Mobile E2E | Applications mobiles ; syntaxe YAML simple |
| **k6 / Criquet** | Test de charge | Performances sous charge |
### Meilleures pratiques E2E
| Pratique | Pourquoi |
|----------|-----|
| **Tester les chemins critiques uniquement** | Les tests E2E sont lents ; concentrez-vous sur ce qui compte le plus |
| **Utiliser des usines de données de test** | Créer des données de test par programmation ; ne vous fiez pas aux données de départ |
| **Nettoyer après les tests** | Chaque test doit laisser le système dans un état connu |
| **Évitez de tester les détails de l'interface utilisateur** | Testez le comportement, pas les classes CSS ou les positions des éléments |
| **Exécuter en CI** | Les tests E2E doivent s'exécuter automatiquement à chaque modification |
---

## Développement piloté par les tests (TDD)
Écrivez d’abord le test, puis écrivez le code pour le faire réussir.
| Étape | Descriptif |
|------|-------------|
| **1. Rouge** | Écrivez un test d'échec qui décrit le comportement souhaité |
| **2. Vert** | Écrivez le code minimum pour réussir le test |
| **3. Refactoriser** | Nettoyer le code tout en gardant les tests verts |
| Avantage | Descriptif |
|---------|-------------|
| **Commentaires sur la conception** | Les tests obligent à réfléchir aux interfaces avant la mise en œuvre |
| **Sécurité de régression** | Chaque bug fait l'objet d'un test ; le bug ne peut jamais revenir |
| **Documentation** | Les tests servent de documentation vivante du comportement attendu |
| **Confiance** | Une couverture de test élevée permet une refactorisation sans peur |
---

## Développement axé sur le comportement (BDD)
BDD étend TDD en écrivant des tests en langage naturel qui décrivent le comportement du point de vue de l'utilisateur.
### Format donné-quand-alors
```
Given a user with an empty shopping cart
When they add a "Python Book" priced at $29.99
Then the cart total should be $29.99
And the cart should contain 1 item
```

| Outil | Langue |
|------|----------|
| **Concombre** | Java, JavaScript, Ruby et autres |
| **Comportez-vous** | Python |
| **SpecFlow** | C# |
| **Jest** (avec décrire) | JavaScript |
---

## Autres types de tests
| Tapez | Ce qu'il teste | Outils |
|------|--------------|-------|
| **Performances/Charge** | Comportement du système sous charge | k6, JMeter, Criquet, Gatling |
| **Sécurité** | Vulnérabilités et vecteurs d'attaque | OWASP ZAP, Burp Suite, Snyk |
| **Accessibilité** | Conformité WCAG | hache, phare, pa11y |
| **Contrat** | Compatibilité API entre services | Pacte, Contrat Spring Cloud |
| **Mutations** | Qualité de la suite de tests elle-même | Stryker, Mutmut, PIT |
| **Régression visuelle** | Modifications de l'interface utilisateur entre les versions | Percy, Chromatique, BackstopJS |
| **Chaos** | Résilience du système aux pannes | Singe du Chaos, Tournesol, Gremlin |
| **Fumée** | Fonctionnalité de base après déploiement | Scripts personnalisés ; bilans de santé |
| **Tremper** | Comportement du système sur une période prolongée | Tests de charge de longue durée |
---

## Organisation des tests
| Modèle | Descriptif | Quand utiliser |
|---------|-------------|-------------|
| **Co-localisé** | Tests à côté du code qu'ils testent (`src/utils.test.ts`) | La plupart des projets ; facile à trouver |
| **Répertoire séparé** | Tests dans un dossier`tests/`ou`__tests__/`| Grands projets ; séparation claire |
| **Montages de test** | Données de test partagées dans un répertoire`fixtures/`| Lorsque plusieurs tests nécessitent les mêmes données |
| **Utilitaires de test** | Assistants partagés dans un répertoire`test-utils/`| Quand la logique de configuration est complexe |
---

## Couverture des codes
| Métrique | Ce qu'il mesure | Limitation |
|--------|-------|------------|
| **Couverture de ligne** | Pourcentage de lignes de code exécutées par les tests | Ne mesure pas la qualité des assertions |
| **Couverture des succursales** | Pourcentage de succursales (si/sinon) prises | Mieux que la couverture en ligne ; ne détecte toujours pas tous les bugs |
| **Couverture du chemin** | Pourcentage de chemins d'exécution empruntés | Le plus minutieux ; exponentielle dans un code complexe |
| **Score de mutation** | Pourcentage de mutations détectées par les tests | Meilleure mesure de la qualité des tests |
**Cible** : une couverture de ligne de 80 % est une valeur par défaut raisonnable. Mais la couverture est un guide, pas un objectif : une couverture à 100 % avec des assertions faibles est pire qu’une couverture à 70 % avec des tests approfondis.
---

## Intégration continue et tests
| Pratique | Descriptif |
|--------------|-------------|
| **Exécutez tous les tests unitaires à chaque commit** | Commentaires rapides ; détecte immédiatement les régressions |
| **Exécuter des tests d'intégration sur PR** | Détecte les problèmes manqués par les tests unitaires |
| **Exécutez les tests E2E tous les soirs ou lors de la fusion vers le principal** | Lent mais minutieux |
| **Échouer rapidement** | Arrêtez le pipeline au premier échec pour gagner du temps |
| **Politique de test instable** | Mettez en quarantaine ou supprimez immédiatement les tests instables ; ne jamais ignorer |
| **Test de parallélisation** | Exécutez des tests en parallèle pour réduire le temps de CI |
---

## Conseils pratiques
- **Nommez clairement les tests.**`test_calculates_tax_for_high_earner`vous indique ce qui s'est cassé. `test_1`ne vous dit rien.
- **Une assertion par test (si possible).** Facilite le diagnostic des pannes.
- **Ne testez pas les détails de l'implémentation.** Testez le comportement. Si vous refactorisez les composants internes, les tests ne devraient pas échouer.
- **Évitez de tester du code tiers.** Simulez des bibliothèques externes ; testez l'interaction de votre code avec eux.
- **Faites des tests rapidement.** Si votre suite de tests prend 10 minutes, les développeurs cesseront de l'exécuter. Optimisez sans relâche.
- **Supprimer les tests morts.** Les tests qui réussissent toujours ou qui testent le code supprimé sont du bruit.
- **Traitez le code de test comme le code de production.** Il doit être lisible, maintenable et bien structuré.
---

## Résumé
Les tests ne sont pas facultatifs : c'est la façon dont vous créez un logiciel qui ne tombe pas en panne. La pyramide de tests vous guide vers de nombreux tests unitaires rapides, certains tests d'intégration et quelques tests E2E. TDD et BDD proposent des approches structurées. La moquerie isole les unités à tester. La couverture du code mesure la largeur mais pas la profondeur. Le principe le plus important est le suivant : si ce n’est pas testé, c’est cassé – vous ne le savez tout simplement pas encore.