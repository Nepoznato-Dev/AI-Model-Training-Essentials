<!-- 
Fichier traduit automatiquement de l'anglais vers le français.
Source: math_and_logic.md
Note: Les termes techniques, exemples de code et noms propres peuvent rester en anglais.
Pour améliorer la précision, veuillez contribuer via des pull requests.
-->

# Mathématiques et Logique

## Qu'est-ce que les Mathématiques ?

Les mathématiques sont l'étude des nombres, des formes, des motifs et des relations logiques. C'est à la fois une science et un langage utilisé pour décrire l'univers. Les mathématiques se divisent en plusieurs branches incluant l'arithmétique, l'algèbre, la géométrie, le calcul, les statistiques et la logique. Les mathématiques sont le fondement de la physique, de l'ingénierie, de l'informatique, de l'économie et de nombreux autres domaines.

## Arithmétique

L'arithmétique est la branche des mathématiques traitant des opérations de base sur les nombres. Les quatre opérations fondamentales sont l'addition (+), la soustraction (−), la multiplication (×) et la division (÷). L'ordre des opérations spécifie la séquence dans laquelle les calculs doivent être effectués : Parenthèses, Exposants, Multiplication et Division (de gauche à droite), Addition et Soustraction (de gauche à droite). Cela est souvent retenu comme **PEMDAS** ou **BODMAS**. Un nombre premier est un nombre entier supérieur à 1 qui n'a aucun diviseur autre que 1 et lui-même. Les premiers nombres premiers sont 2, 3, 5, 7, 11, 13, 17, 19, 23 et 29.

**Exemples:**
- Décomposition en facteurs premiers : 84 = 2² × 3 × 7
- Plus Grand Commun Diviseur (PGCD) de 24 et 36 : 12
- Plus Petit Commun Multiple (PPCM) de 4 et 6 : 12

## Algèbre

L'algèbre utilise des lettres et des symboles pour représenter des nombres et des quantités dans des équations et des formules. Une **variable** est un symbole (généralement une lettre) qui représente une quantité inconnue ou changeante. Une **équation** indique que deux expressions sont égales. Résoudre une équation signifie trouver la ou les valeur(s) de la ou des variable(s) qui rendent l'équation vraie.

La **formule quadratique** résout les équations de la forme ax² + bx + c = 0 : x = (−b ± √(b²−4ac)) / (2a)


Une **fonction** associe chaque entrée à exactement une sortie. Les fonctions courantes incluent :
- Linéaire : y = mx + b (droite, taux de changement constant)
- Quadratique : y = ax² + bx + c (parabole, courbe)
- Exponentielle : y = a × bˣ (croissance ou décroissance, changement rapide)
- Logarithmique : y = log_b(x) (inverse de l'exponentielle)

**Concepts clés:**
- Domaine : l'ensemble de toutes les valeurs d'entrée possibles
- Image : l'ensemble de toutes les valeurs de sortie possibles
- Pente : taux de changement (m dans y = mx + b)
- Ordonnée à l'origine : où la fonction coupe l'axe des y (b dans y = mx + b)

## Géométrie

La géométrie est la branche des mathématiques qui étudie les formes, les tailles, les positions et les propriétés des figures. Un point n'a pas de taille ; il représente une position. Une droite s'étend indéfiniment dans les deux directions. Un segment de droite a deux extrémités. Un angle est formé par deux rayons partageant une extrémité.

**Règles clés:**
- La somme des angles dans un triangle est toujours de 180 degrés.
- La somme des angles dans un quadrilatère est toujours de 360 degrés.
- Théorème de Pythagore : dans un triangle rectangle, a² + b² = c² (où c est l'hypoténuse).
- Circonférence d'un cercle : 2πr
- Aire d'un cercle : πr²
- Volume d'une sphère : (4/3)πr³

**π (pi)** est approximativement 3.14159 et est le rapport entre la circonférence d'un cercle et son diamètre.

**Formes géométriques courantes:**
- Triangle : 3 côtés, somme des angles à 180°
- Carré : 4 côtés égaux, 4 angles droits
- Rectangle : 4 côtés, côtés opposés égaux, 4 angles droits
- Cercle : pas de côtés, frontière courbe continue
- Pentagone : 5 côtés, somme des angles à 540°
- Hexagone : 6 côtés, somme des angles à 720°

## Statistiques et Probabilités

Les statistiques sont la science de collecter, analyser, interpréter et présenter des données.

**Mesures de tendance centrale:**
- **Moyenne** (average) : somme de toutes les valeurs divisée par le nombre de valeurs
- **Médiane** : valeur du milieu lorsque les données sont triées (moins sensible aux valeurs aberrantes)
- **Mode** : valeur la plus fréquente (peut avoir plusieurs modes)

**Mesures de dispersion:**
- **Étendue** : maximum - minimum
- **Variance** : moyenne des carrés des écarts par rapport à la moyenne
- **Écart-type** : racine carrée de la variance (dans les mêmes unités que les données)

La probabilité mesure la vraisemblance qu'un événement se produise, allant de 0 (impossible) à 1 (certain). La probabilité que deux événements indépendants se produisent tous les deux est le produit de leurs probabilités individuelles.

**Exemple:** Probabilité d'obtenir un 6 sur un dé équilibré : 1/6. Probabilité d'obtenir deux 6 consécutifs : (1/6) × (1/6) = 1/36.

## Probabilités pour l'Informatique et le ML

Une **variable aléatoire** est une variable dont la valeur dépend du résultat d'un processus aléatoire. Une **distribution de probabilité** décrit la probabilité de chaque résultat.

**Distributions courantes:**
- **Bernoulli** : essai unique avec deux résultats (ex: lancer de pièce)
- **Binomiale** : nombre de succès dans n essais de Bernoulli indépendants
- **Normale (Gaussienne)** : courbe en cloche, symétrique autour de la moyenne (courante dans les phénomènes naturels)
- **Poisson** : nombre d'événements dans un intervalle fixe (ex: emails par heure)

**Espérance mathématique** est la moyenne à long terme d'une variable aléatoire. La **variance** mesure la dispersion autour de cette espérance.

**Probabilité conditionnelle** décrit la probabilité d'un événement sachant qu'un autre événement s'est produit : P(A|B) = P(A ∩ B) / P(B) [si P(B) > 0].

**Théorème de Bayes** met à jour les croyances en utilisant des preuves : P(A|B) = P(B|A) × P(A) / P(B).


Dans l'apprentissage automatique, les probabilités sous-tendent la confiance en classification, l'estimation d'incertitude, les méthodes bayésiennes et de nombreuses fonctions de perte (comme l'entropie croisée).

## Calcul

Le calcul est la branche des mathématiques qui étudie le changement continu.

Le **calcul différentiel** traite des taux de changement et des pentes de courbes, en utilisant les **dérivées**. La dérivée d'une fonction f(x) représente le taux de changement de f par rapport à x en un point. Notation : f'(x) ou df/dx.

**Dérivées courantes:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

Le **calcul intégral** traite de l'accumulation de quantités et des aires sous les courbes, en utilisant les **intégrales**. L'intégrale représente l'aire sous la courbe entre deux points.

Le **théorème fondamental du calcul** relie dérivation et intégration : la dérivation et l'intégration sont des opérations inverses.

Le calcul a été développé indépendamment par Isaac Newton et Gottfried Wilhelm Leibniz au 17e siècle.

## Systèmes de Nombres

- **Nombres naturels** : 1, 2, 3, 4, ... (nombres de comptage)
- **Nombres entiers naturels** : 0, 1, 2, 3, ... (nombres naturels plus zéro)
- **Entiers relatifs** : ..., −2, −1, 0, 1, 2, ... (tous les nombres entiers naturels et leurs négatifs)
- **Nombres rationnels** : nombres exprimables comme p/q où p et q sont des entiers et q ≠ 0 (ex: 1/2, 3/4, −5/3)
- **Nombres irrationnels** : ne peuvent pas être exprimés comme une fraction (ex: √2, π, e)
- **Nombres réels** : tous les nombres rationnels et irrationnels (la droite numérique)
- **Nombres imaginaires** : impliquent la racine carrée de nombres négatifs ; i = √(−1)
- **Nombres complexes** : combinent parties réelles et imaginaires (a + bi)

## Logique et Raisonnement

La logique est l'étude du raisonnement valide.

Le **raisonnement déductif** tire des conclusions spécifiques de prémisses générales. Si les prémisses sont vraies et l'argument est valide, la conclusion doit être vraie.
- **Exemple:** Tous les humains sont mortels. Socrate est humain. Donc, Socrate est mortel.

Le **raisonnement inductif** tire des conclusions générales d'observations spécifiques. Il ne garantit pas que la conclusion est vraie, mais la rend probable.
- **Exemple:** Tous les cygnes que j'ai vus sont blancs. Donc, tous les cygnes sont blancs. (Note: c'est faux; des cygnes noirs existent!)

**Sophismes logiques courants (erreurs de raisonnement):**
- **Ad hominem**: attaquer la personne plutôt que l'argument
- **Homme de paille**: déformer un argument pour le rendre plus facile à attaquer
- **Faux dilemme**: présenter seulement deux options quand il en existe plus
- **Raisonnement circulaire**: utiliser la conclusion comme prémisse
- **Appel à l'autorité**: affirmer que quelque chose est vrai parce qu'une autorité le dit
- **Sophisme post hoc**: supposer que parce que A s'est produit avant B, A a causé B

## Ensembles

Un **ensemble** est une collection d'objets distincts.
- **Union** (A ∪ B): tous les éléments des deux ensembles
- **Intersection** (A ∩ B): uniquement les éléments communs aux deux
- **Ensemble vide** (∅ ou {}): ne contient aucun élément
- **Sous-ensemble** (A ⊆ B): tous les éléments de A sont aussi dans B
- **Diagrammes de Venn**: représentent visuellement les relations entre ensembles

La théorie des ensembles est le fondement des mathématiques modernes et de la logique.

## Binaire et Bases Numériques

Les ordinateurs représentent les données en **binaire** (base 2), utilisant uniquement les chiffres 0 et 1. Chaque chiffre binaire est appelé un **bit**. Huit bits forment un **octet**.

Le **décimal** est le système de numération en base 10 que les humains utilisent généralement.

L'**hexadécimal** est la base 16, utilisant les chiffres 0–9 et les lettres A–F, souvent utilisé en informatique pour représenter les données binaires de manière compacte.

**Conversions:**
- Binaire 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (décimal)
- Hex A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (décimal)

La conversion entre bases numériques est un concept fondamental en informatique.

## Algèbre Linéaire pour Développeurs et ML

L'algèbre linéaire étudie les vecteurs, les matrices et les transformations linéaires.

Un **vecteur** est une liste ordonnée de nombres (ex: caractéristiques dans un échantillon ML).
- Exemple: [23, 1.8, 175] représente l'âge, la taille et le poids d'une personne

Une **matrice** est un tableau 2D de nombres (ex: poids de modèle ou lots de données).
- Exemple: [[1, 2], [3, 4]] est une matrice 2×2

La **multiplication matricielle** combine des transformations linéaires et est une opération centrale en infographie, simulation et réseaux de neurones.

Le **produit scalaire** mesure la similarité et la projection entre vecteurs:
- a·b = Σ(a_i × b_i)
- **Similarité cosinus** = (a·b) / (||a|| × ||b||)
- La similarité cosinus varie de -1 (opposé) à 1 (même direction)

Les **valeurs propres et vecteurs propres** décrivent les directions qui sont mises à l'échelle (non tournées) par une matrice et sont utilisées dans des méthodes telles que l'ACP (Analyse en Composantes Principales).

Le **rang** indique combien d'informations indépendantes une matrice contient. Les approximations de bas rang sont utiles pour la compression et la réduction de dimensionnalité.

La plupart des charges de travail ML modernes reposent fortement sur des bibliothèques d'algèbre linéaire optimisées et l'accélération matérielle.