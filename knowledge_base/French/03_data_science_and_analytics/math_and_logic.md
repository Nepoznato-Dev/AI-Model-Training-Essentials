---
# Métadonnées
titre : "Mathématiques et logique"
description: "Mathématiques, logique, preuves"
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
tags : [mathématiques, logique, science des données et analyse]
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
# Mathématiques et Logique
Les mathématiques ne sont pas seulement une matière que vous étudiez à l'école : c'est le système d'exploitation qui sous-tend presque tous les domaines techniques. La physique l'utilise pour décrire l'univers. L'informatique l'utilise pour concevoir des algorithmes. L'apprentissage automatique l'utilise pour optimiser les poids. La finance l’utilise pour évaluer le risque. Vous n'avez pas besoin de maîtriser chaque branche, mais comprendre le paysage – et savoir où chaque branche apparaît – accélère tout le reste.
---

## Systèmes numériques
Avant toute chose, il est utile de comprendre les types de chiffres avec lesquels vous travaillez. Chaque couche étend la précédente pour résoudre un problème que l'ancienne couche ne pouvait pas résoudre.
| Type de numéro | Ce qu'il comprend | Pourquoi il a été inventé | Exemple |
|---|---|---|---|
| Nombres naturels | 1, 2, 3, 4, ... | Compter les choses | 5 pommes |
| Nombres entiers | 0, 1, 2, 3, ... | Représentant « rien » | 0 degrés |
| Entiers | ..., −2, −1, 0, 1, 2, ... | Dette, température en dessous de zéro | −15°C |
| Nombres rationnels | p/q où q ≠ 0 | Diviser les choses de manière inégale | 1/3, 0,75 |
| Nombres irrationnels | Ne peut pas être exprimé sous forme de fractions | Diagonales, cercles, croissance | √2, π, e |
| Chiffres réels | Tout rationnel + irrationnel | La droite numérique complète | 3.14159... |
| Nombres imaginaires | Multiples de i = √(−1) | Résolution de x² + 1 = 0 | 3i |
| Nombres complexes | a + bi (réel + imaginaire) | Génie électrique, mécanique quantique | 2 + 3i |
---

## Arithmétique et théorie des nombres
Les bases : l'addition, la soustraction, la multiplication, la division et les règles régissant leur ordre.
**Ordre des opérations** (PEMDAS/BODMAS) : Parenthèses → Exposants → Multiplication/Division (de gauche à droite) → Addition/Soustraction (de gauche à droite).
**Les nombres premiers** — nombres entiers supérieurs à 1 sans diviseur autre que 1 et eux-mêmes — sont les atomes de la théorie des nombres. Les premiers : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
Pourquoi les nombres premiers sont importants au-delà des cours de mathématiques : le chiffrement moderne (RSA) repose sur le fait que multiplier deux grands nombres premiers est facile, mais la prise en compte du résultat est brutale sur le plan informatique.
**Opérations utiles :**
- Factorisation première : 84 = 2² × 3 × 7
- Plus grand diviseur commun (PGCD) de 24 et 36 : 12
- Le Plus Petit Commun Multiple (LCM) de 4 et 6 : 12
---

## Algèbre
L'algèbre est l'endroit où vous arrêtez de travailler avec des nombres spécifiques et commencez à travailler avec des *relations*. Une variable comme`x`n'a pas de valeur fixe : elle représente tout ce qui rend l'équation vraie.
**La formule quadratique** résout ax² + bx + c = 0 :
x = (−b ± √(b² − 4ac)) / 2a
**Types de fonctions courants et où ils apparaissent :**
| Fonction | Formule | Forme | Exemple concret |
|---|---|---|---|
| Linéaire | y = mx + b | Ligne droite | Coût unitaire au forfait |
| Quadratique | y = ax² + bx + c | Parabole | Mouvement du projectile, distance de freinage |
| Exponentiel | y = une × b² | Croissance/décroissance rapide | Intérêts composés, croissance démographique, propagation virale |
| Logarithmique | y = log_b(x) | Croissance lente, inverse de l'exponentielle | Échelle de décibels, échelle de pH, complexité de l'algorithme |
**Vocabulaire clé :**
- **Domaine** : toutes les entrées valides (par exemple, ne peut pas diviser par zéro, ne peut pas prendre √ d'un négatif en réels)
- **Plage** : toutes les sorties possibles
- **Pente** (m) : taux de changement — "pour chaque unité de x, y change de m"
- **Intercept** : où la fonction traverse un axe
---

## Géométrie
La géométrie étudie les formes, les tailles et les relations spatiales. On le retrouve partout : les moteurs de jeux l'utilisent pour le rendu, la robotique l'utilise pour la planification des trajectoires, l'architecture l'utilise pour la conception structurelle.
**Formules essentielles :**
| Forme | Propriété | Formule |
|---|---|---|
| Triangle | Somme des angles | 180° |
| Quadrilatère | Somme des angles | 360° |
| Cercle | Circonférence | 2πr |
| Cercle | Zone | πr² |
| Sphère | Volume | (4/3)πr³ |
| Triangle rectangle | Théorème de Pythagore | a² + b² = c² |
**π (pi)** ≈ 3,14159 — le rapport entre la circonférence d'un cercle et son diamètre. Cela apparaît dans des endroits inattendus : probabilité (distribution normale), ingénierie (traitement du signal), même l'équation du principe d'incertitude de Heisenberg.
---

## Statistiques et probabilités
Les statistiques vous permettent de donner un sens aux données. C'est la différence entre « Je pense que cela fonctionne » et « J'ai des preuves que cela fonctionne ».
**Mesures de la tendance centrale — ce qui est « typique » :**
| Mesurer | Comment c'est calculé | Quand l'utiliser |
|---|---|---|
| Moyenne (moyenne) | Somme ÷ compter | Choix par défaut ; sensible aux valeurs aberrantes |
| Médiane | Valeur moyenne une fois triée | Données faussées (par exemple, prix de l'immobilier, salaires) |
| Mode | Valeur la plus fréquente | Données catégorielles (par exemple, couleur la plus populaire) |
**Mesures de propagation — dans quelle mesure les données sont « variées » :**
| Mesurer | Idée de formule | Ce qu'il vous dit |
|---|---|---|
| Gamme | max − min | Spread total, mais sensible aux valeurs aberrantes |
| Écart | Écart carré moyen par rapport à la moyenne | En unités carrées (difficile à interpréter directement) |
| Écart type | √écart | Mêmes unités que les données – la mesure de propagation incontournable |
**Bases des probabilités :**
- Va de 0 (impossible) à 1 (certain)
- Événements indépendants : P(A et B) = P(A) × P(B)
- Exemple : lancer deux 6 d'affilée = (1/6) × (1/6) = 1/36
**Distributions de probabilité que vous rencontrerez en ML :**
| Distribution | Ce qu'il modélise | Exemple |
|---|---|---|
| Bernoulli | Essai unique, deux résultats | Un tirage au sort |
| Binôme | Succès dans n essais | Réponses correctes à un QCM de 10 questions |
| Normal (gaussien) | Courbe en cloche, phénomènes naturels | Hauteurs, résultats aux tests, bruit de mesure |
| Poisson | Événements à intervalle fixe | E-mails par heure, défauts par lot |
**Théorème de Bayes** — mise à jour des croyances avec des preuves :
P(UNE|B) = P(B|UNE) × P(UNE) / P(B)
Il s’agit de l’épine dorsale des filtres anti-spam, des diagnostics médicaux et des modèles bayésiens de ML. Il indique : votre croyance mise à jour = (dans quelle mesure les preuves correspondent à votre hypothèse × votre croyance antérieure) / quelle est la probabilité globale des preuves.
---

## Calcul
Études de calcul *changement* et *accumulation*. Si l’algèbre gère les instantanés, le calcul gère les films.
**Calcul différentiel** — taux de changement. La dérivée f'(x) vous indique à quelle vitesse f change à tout moment.
| Fonction f(x) | Dérivée f'(x) | Intuitions |
|---|---|---|
| xⁿ | n·xⁿâ»¹ | Règle de puissance |
| e² | e² | La seule fonction égale à sa propre dérivée |
| ln(x) | 1/x | Le taux de croissance ralentit à mesure que x augmente |
| péché(x) | cos(x) | Taux de changement d'oscillation |
Pourquoi les dérivées sont importantes en ML : la descente de gradient – ​​l'algorithme qui entraîne la plupart des réseaux de neurones – fonctionne en calculant les dérivées de la fonction de perte et en allant dans la direction qui réduit les erreurs.
**Calcul intégral** — accumulation. L'intégrale représente l'aire sous une courbe. Si les dérivées répondent « à quelle vitesse cela change-t-il ? », les intégrales répondent « combien s'est accumulé ?
Le **théorème fondamental du calcul** relie les deux : la différenciation et l'intégration sont des opérations inverses.
---

## Logique et raisonnement
La logique est l'étude du raisonnement *valable* - non pas si une conclusion *semble* juste, mais si elle *désuit* des prémisses.
**Raisonnement déductif** (conclusion garantie si les prémisses sont vraies) :
- Tous les humains sont mortels. Socrate est humain. → Socrate est mortel.
**Raisonnement inductif** (conclusion probable, non garantie) :
- Tous les cygnes que j'ai vus sont blancs. → Tous les cygnes sont probablement blancs. (Mais les cygnes noirs existent.)
**Erreurs logiques courants : erreurs qui ressemblent à du raisonnement mais n'en sont pas :**
| Erreur | Qu'est-ce que c'est | Exemple |
|---|---|---|
| Ad hominem | Attaquer la personne, pas l'argumentation | "Vous ne pouvez pas faire confiance à ses idées politiques – elle est jeune." |
| Homme de paille | Déformer un argument pour le faire tomber | "Il veut réduire les dépenses militaires ? Il veut nous laisser sans défense !" |
| Fausse dichotomie | Présenter deux options lorsqu'il en existe d'autres | "Soit vous êtes avec nous, soit vous êtes contre nous." |
| Raisonnement circulaire | Utiliser la conclusion comme sa propre prémisse | "Cette loi est injuste parce qu'elle est injuste." |
| Appel à l'autorité | "C'est vrai parce qu'un expert l'a dit" | "Ce titre va augmenter – un investisseur célèbre l'a dit." |
| Post-hoc | En supposant que A a causé B parce que A est venu en premier | "J'ai pris ce supplément, puis mon rhume a disparu. Le supplément m'a guéri." |
---

## Ensembles
Un **ensemble** est une collection d'objets distincts — le fondement des mathématiques modernes.
| Opération | Symbole | Signification | Exemple (A={1,2,3}, B={2,4}) |
|---|---|---|---|
| Syndicat | UNE ∪B | Éléments de l'un ou l'autre ensemble | {1, 2, 3, 4} |
| Intersection | UNE ∩B | Éléments des deux ensembles | {2} |
| Différence | A\B | Éléments dans A mais pas dans B | {1, 3} |
| Ensemble vide | ∅ | Ne contient rien | {} |
| Sous-ensemble | UNE ⊂ B | Tous les éléments de A sont dans B | {1,2} ⊂ {1,2,3} |
La théorie des ensembles apparaît dans les bases de données (les SQL JOIN sont essentiellement des opérations sur des ensembles), les probabilités (les événements sont des ensembles de résultats) et la programmation (ensembles, cartes de hachage).
---

## Bases binaires et numériques
Les ordinateurs pensent en binaire (base 2) : seulement des 0 et des 1. Les humains pensent en décimal (base 10). Les programmeurs utilisent souvent l'hexadécimal (base 16) comme moyen compact de représenter le binaire.
| Socle | Chiffres utilisés | Exemple | Équivalent décimal |
|---|---|---|---|
| Binaire (base 2) | 0, 1 | 1011 | 8 + 0 + 2 + 1 = 11 |
| Décimal (base 10) | 0-9 | 11 | 11 |
| Hexadécimal (base 16) | 0-9, A-F | B | 11 |
| Hexadécimal | 0-9, A-F | A3 | 160 + 3 = 163 |
**Pourquoi c'est important :** chaque élément de données d'un ordinateur (texte, images, audio, vidéo) n'est en fin de compte que binaire. Un octet (8 bits) peut représenter 256 valeurs distinctes. Les couleurs en CSS (#FF5733), les adresses mémoire (0x7FFF) et les adresses IP utilisent toutes l'hexadécimal car elles compressent les longues chaînes binaires en quelque chose de lisible.
---

## Algèbre linéaire pour le ML et les graphiques
L'algèbre linéaire (vecteurs, matrices et transformations) est le moteur mathématique derrière l'apprentissage automatique, l'infographie, les simulations physiques et les moteurs de recherche.
**Les vecteurs** sont des listes ordonnées de nombres. En ML, chaque point de données est un vecteur de fonctionnalités :
- [23, 1,8, 75] pourrait représenter l'âge, la taille en mètres et le poids d'une personne en kg.
Les **matrices** sont des tableaux de nombres 2D. Les poids d'un réseau neuronal sont stockés sous forme de matrices. Un lot de 100 images peut être une matrice de forme (100, 784) — 100 lignes, chacune avec 784 valeurs de pixels.
**Opérations clés :**
| Opération | Ce qu'il fait | Où il apparaît |
|---|---|---|
| Produit scalaire | Mesure la similarité entre deux vecteurs | Systèmes de recommandation, similarité cosinus |
| Multiplication matricielle | Combine des transformations linéaires | Chaque couche d'un réseau neuronal |
| Valeurs propres/vecteurs propres | Directions d'une matrice mise à l'échelle (pas de rotation) | Réduction de dimensionnalité PCA, PageRank |
| Rang matriciel | Quantité d'informations indépendantes | Compression, approximation de bas rang |
**Similitude cosinus** = (a·b) / (||a|| × ||b||) — va de −1 (opposé) à 1 (même direction). C’est ainsi que les moteurs de recherche mesurent si deux documents « concernent la même chose » et comment les modèles d’intégration comparent la similarité sémantique.
---

## Résumé
| Branche | Question fondamentale | Application clé |
|---|---|---|
| Arithmétique et théorie des nombres | Comment se comportent les chiffres ? | Cryptographie, hachage |
| Algèbre | Quel est le rapport entre les inconnues ? | Modélisation, équations |
| Géométrie | Comment fonctionnent les formes et les espaces ? | Graphique, robotique, architecture |
| Statistiques et probabilités | Que disent les données ? | ML, tests A/B, analyse des risques |
| Calcul | Comment les choses changent-elles ? | Formation aux réseaux de neurones, physique |
| Logique | Ce raisonnement est-il valable ? | Programmation, preuves, analyse d'arguments |
| Théorie des ensembles | Quel est le rapport entre les collections ? | Bases de données, probabilités |
| Algèbre linéaire | Comment fonctionnent les transformations ? | ML, graphiques, moteurs de recherche |
Vous n’avez pas besoin de tout cela dès le premier jour. Mais au fur et à mesure que vous approfondissez un domaine technique, vous reviendrez sans cesse à ces fondations. La bonne nouvelle : chaque branche a beaucoup plus de sens une fois que vous voyez *pourquoi* elle a été inventée – quel problème elle essayait de résoudre.