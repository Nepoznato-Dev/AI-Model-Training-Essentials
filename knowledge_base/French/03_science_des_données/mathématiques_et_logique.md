<!-- 
This file was automatically translated from English to French.
Source: math_and_logic.md
Note: Technical terms, code examples, and proper nouns may remain in English.
For accuracy improvements, please contribute edits via pull requests.
-->

# Mathématiques et logique

## Qu'est-ce que les mathématiques ?

Les mathématiques sont l'étude des nombres, des formes, des motifs et des relations logiques. Elles sont à la fois une science et un langage permettant de décrire l'univers. Les mathématiques se divisent en plusieurs branches, notamment l'arithmétique, l'algèbre, la géométrie, l'analyse, les statistiques et la logique. Elles constituent le fondement de la physique, de l'ingénierie, de l'informatique, de l'économie et de nombreux autres domaines.

## Arithmétique

L'arithmétique est la branche des mathématiques qui traite des opérations de base sur les nombres. Les quatre opérations fondamentales sont l'addition (+), la soustraction (−), la multiplication (×) et la division (÷). L'ordre des opérations précise la séquence dans laquelle les calculs doivent être effectués : Parenthèses, Exposants, Multiplication et Division (de gauche à droite), Addition et Soustraction (de gauche à droite). On le retient souvent avec les acronymes **PEMDAS** ou **BODMAS**. Un nombre premier est un entier supérieur à 1 qui n'a pour diviseurs que 1 et lui-même. Les premiers nombres premiers sont 2, 3, 5, 7, 11, 13, 17, 19, 23 et 29.

**Exemples :**
- Décomposition en facteurs premiers : 84 = 2² × 3 × 7
- Plus grand commun diviseur (GCD) de 24 et 36 : 12
- Plus petit commun multiple (LCM) de 4 et 6 : 12

## Algèbre

L'algèbre utilise des lettres et des symboles pour représenter des nombres et des grandeurs dans des équations et des formules. Une **variable** est un symbole (souvent une lettre) qui représente une quantité inconnue ou changeante. Une **équation** affirme que deux expressions sont égales. Résoudre une équation consiste à trouver la ou les valeurs des variables qui la rendent vraie.

La **formule quadratique** résout les équations de la forme ax² + bx + c = 0 : x = (−b ± √(b²−4ac)) / (2a)

Une **fonction** associe à chaque entrée exactement une sortie. Les fonctions courantes comprennent :
- Linéaire : y = mx + b (droite, taux de variation constant)
- Quadratique : y = ax² + bx + c (parabole, courbe)
- Exponentielle : y = a × bˣ (croissance ou décroissance rapide)
- Logarithmique : y = log_b(x) (fonction réciproque de l'exponentielle)

**Concepts clés :**
- Domaine : ensemble de toutes les valeurs d'entrée possibles
- Ensemble image : ensemble de toutes les valeurs de sortie possibles
- Pente : taux de variation (m dans y = mx + b)
- Ordonnée à l'origine : point où la fonction coupe l'axe des y (b dans y = mx + b)

## Géométrie

La géométrie est la branche des mathématiques qui étudie les formes, les dimensions, les positions et les propriétés des figures. Un point n'a pas de taille ; il représente une position. Une droite s'étend à l'infini dans les deux directions. Un segment a deux extrémités. Un angle est formé par deux demi-droites partageant une extrémité.

**Règles clés :**
- La somme des angles d'un triangle est toujours de 180 degrés.
- La somme des angles d'un quadrilatère est toujours de 360 degrés.
- Théorème de Pythagore : dans un triangle rectangle, a² + b² = c² (où c est l'hypoténuse).
- Circonférence d'un cercle : 2πr
- Aire d'un cercle : πr²
- Volume d'une sphère : (4/3)πr³

**π (pi)** vaut environ 3,14159 et représente le rapport entre la circonférence d'un cercle et son diamètre.

**Formes géométriques courantes :**
- Triangle : 3 côtés, somme des angles = 180°
- Carré : 4 côtés égaux, 4 angles droits
- Rectangle : 4 côtés, côtés opposés égaux, 4 angles droits
- Cercle : aucun côté, bordure courbe continue
- Pentagone : 5 côtés, somme des angles = 540°
- Hexagone : 6 côtés, somme des angles = 720°

## Statistiques et probabilités

Les statistiques sont la science de la collecte, de l'analyse, de l'interprétation et de la présentation des données.

**Mesures de tendance centrale :**
- **Mean** (moyenne) : somme de toutes les valeurs divisée par le nombre de valeurs
- **Median** : valeur centrale lorsque les données sont triées (moins sensible aux valeurs aberrantes)
- **Mode** : valeur apparaissant le plus fréquemment (il peut y en avoir plusieurs)

**Mesures de dispersion :**
- **Range** : maximum - minimum
- **Variance** : moyenne des écarts au carré par rapport à la moyenne
- **Standard deviation** : racine carrée de la variance (dans les mêmes unités que les données)

La probabilité mesure la vraisemblance qu'un événement se produise, sur une échelle allant de 0 (impossible) à 1 (certain). La probabilité que deux événements indépendants se produisent tous les deux est le produit de leurs probabilités individuelles.

**Exemple :** probabilité d'obtenir un 6 avec un dé équilibré : 1/6. Probabilité d'obtenir deux 6 d'affilée : (1/6) × (1/6) = 1/36.

## Probabilités pour l'informatique et le ML

Une **variable aléatoire** est une variable dont la valeur dépend de l'issue d'un processus aléatoire. Une **distribution de probabilité** décrit la probabilité de chaque issue.

**Distributions courantes :**
- **Bernoulli** : un seul essai avec deux issues (par exemple pile ou face)
- **Binomial** : nombre de succès dans n essais de Bernoulli indépendants
- **Normal (Gaussian)** : courbe en cloche, symétrique autour de la moyenne (courante dans les phénomènes naturels)
- **Poisson** : nombre d'événements dans un intervalle fixe (par exemple le nombre d'emails par heure)

L'**espérance** est la moyenne à long terme des résultats d'une variable aléatoire. La **variance** mesure la dispersion autour de cette espérance.

La **probabilité conditionnelle** décrit la probabilité d'un événement sachant qu'un autre événement s'est déjà produit : P(A|B) = P(A ∩ B) / P(B) [si P(B) > 0].

Le **théorème de Bayes** met à jour des croyances à partir d'éléments de preuve : P(A|B) = P(B|A) × P(A) / P(B).

En machine learning, les probabilités sous-tendent la confiance en classification, l'estimation de l'incertitude, les méthodes bayésiennes et de nombreuses fonctions de perte (comme la cross-entropy).

## Analyse

L'analyse est la branche des mathématiques qui étudie les variations continues.

L'**analyse différentielle** traite des taux de variation et des pentes des courbes à l'aide des **dérivées**. La dérivée d'une fonction f(x) représente le taux de variation de f par rapport à x en un point. Notation : f'(x) ou df/dx.

**Dérivées courantes :**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

L'**analyse intégrale** traite de l'accumulation de grandeurs et des aires sous les courbes, au moyen des **intégrales**. L'intégrale représente l'aire sous la courbe entre deux points.

Le **théorème fondamental de l'analyse** relie dérivation et intégration : ce sont des opérations inverses.

L'analyse a été développée indépendamment par Isaac Newton et Gottfried Wilhelm Leibniz au XVIIe siècle.

## Systèmes de nombres

- **Nombres naturels** : 1, 2, 3, 4, ... (nombres de comptage)
- **Nombres entiers naturels avec zéro** : 0, 1, 2, 3, ...
- **Entiers relatifs** : ..., −2, −1, 0, 1, 2, ...
- **Nombres rationnels** : nombres exprimables sous la forme p/q où p et q sont des entiers et q ≠ 0 (par exemple 1/2, 3/4, −5/3)
- **Nombres irrationnels** : ne peuvent pas s'écrire sous forme de fraction (par exemple √2, π, e)
- **Nombres réels** : tous les nombres rationnels et irrationnels (la droite des nombres)
- **Nombres imaginaires** : impliquent la racine carrée de nombres négatifs ; i = √(−1)
- **Nombres complexes** : combinent une partie réelle et une partie imaginaire (a + bi)

## Logique et raisonnement

La logique est l'étude du raisonnement valide.

Le **raisonnement déductif** tire des conclusions particulières à partir de prémisses générales. Si les prémisses sont vraies et que l'argument est valide, la conclusion doit être vraie.
- **Exemple :** Tous les humains sont mortels. Socrate est humain. Donc, Socrate est mortel.

Le **raisonnement inductif** tire des conclusions générales à partir d'observations particulières. Il ne garantit pas que la conclusion est vraie, mais la rend probable.
- **Exemple :** Tous les cygnes que j'ai vus sont blancs. Donc, tous les cygnes sont blancs. (Remarque : c'est faux ; les cygnes noirs existent !)

**Sophismes courants (erreurs de raisonnement) :**
- **Ad hominem** : attaquer la personne plutôt que l'argument
- **Straw man** : déformer l'argument pour le rendre plus facile à attaquer
- **False dichotomy** : ne présenter que deux options alors qu'il en existe davantage
- **Circular reasoning** : utiliser la conclusion comme prémisse
- **Appeal to authority** : affirmer qu'une chose est vraie parce qu'une autorité l'a dit
- **Post hoc fallacy** : supposer que parce que A s'est produit avant B, A a causé B

## Ensembles

Un **ensemble** est une collection d'objets distincts.
- **Union** (A ∪ B) : tous les éléments des deux ensembles
- **Intersection** (A ∩ B) : uniquement les éléments communs aux deux ensembles
- **Ensemble vide** (∅ ou {}) : ne contient aucun élément
- **Sous-ensemble** (A ⊆ B) : tous les éléments de A sont aussi dans B
- **Diagrammes de Venn** : représentent visuellement les relations entre ensembles

La théorie des ensembles constitue le fondement des mathématiques et de la logique modernes.

## Binaire et bases numériques

Les ordinateurs représentent les données en **binaire** (base 2), en utilisant uniquement les chiffres 0 et 1. Chaque chiffre binaire s'appelle un **bit**. Huit bits forment un **byte**.

Le **décimal** est le système en base 10 que les humains utilisent habituellement.

L'**hexadécimal** est en base 16, avec les chiffres 0–9 et les lettres A–F ; il est souvent utilisé en informatique pour représenter les données binaires de manière compacte.

**Conversions :**
- Binaire 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (decimal)
- Hex A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (decimal)

La conversion entre bases numériques est un concept fondamental en informatique.

## Algèbre linéaire pour les développeurs et le ML

L'algèbre linéaire étudie les vecteurs, les matrices et les transformations linéaires.

Un **vecteur** est une liste ordonnée de nombres (par exemple des features dans un échantillon ML).
- Exemple : [23, 1.8, 175] représente l'âge, la taille et le poids d'une personne

Une **matrice** est un tableau 2D de nombres (par exemple des poids de modèle ou des lots de jeux de données).
- Exemple : [[1, 2], [3, 4]] est une matrice 2×2

La **multiplication matricielle** combine des transformations linéaires et constitue une opération centrale en graphisme, en simulation et dans les réseaux de neurones.

Le **produit scalaire** mesure la similarité et la projection entre vecteurs :
- a·b = Σ(a_i × b_i)
- **Cosine similarity** = (a·b) / (||a|| × ||b||)
- La similarité cosinus varie de -1 (directions opposées) à 1 (même direction)

Les **eigenvalues** et **eigenvectors** décrivent des directions qu'une matrice dilate sans les faire tourner, et sont utilisés dans des méthodes telles que la PCA (Principal Component Analysis).

Le **rang** indique la quantité d'information indépendante contenue dans une matrice. Les approximations de faible rang sont utiles pour la compression et la réduction de dimension.

La plupart des charges de travail ML modernes reposent fortement sur des bibliothèques d'algèbre linéaire optimisées et sur l'accélération matérielle.
