---
# Metadata
title: "Discrete Mathematics"
description: "Sets in depth, relations, functions, combinatorics, pigeonhole principle, recurrence relations, and generating functions"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into discrete mathematics"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [discrete-mathematics, set-theory, relations, combinatorics, pigeonhole-principle, recurrence-relations, generating-functions]
difficulty_level: "intermediate"
prerequisites:
  - "mathematics.md"
  - "../logic_and_critical_thinking.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Mathématiques discrètes
Les mathématiques discrètes sont l'étude de structures mathématiques qui sont fondamentalement dénombrables ou séparées, par opposition aux mathématiques continues (calcul, analyse réelle), qui traitent de quantités lisses et ininterrompues. Les mathématiques discrètes sous-tendent l’informatique, la cryptographie, la conception d’algorithmes et les structures de données. Si les mathématiques continues décrivent le monde physique, les mathématiques discrètes décrivent le monde informatique.
---

## Définir la théorie en profondeur
Les ensembles constituent la base sur laquelle reposent presque toutes les mathématiques modernes. Un **ensemble** est une collection non ordonnée d'objets distincts, appelés **éléments** ou **membres**.
### Fondements axiomatiques (ZFC)
La théorie des ensembles moderne repose sur les **axiomes de Zermelo-Fraenkel avec l'Axiome du Choix (ZFC)**. Ces axiomes résolvent des paradoxes comme le paradoxe de Russell (« l'ensemble de tous les ensembles qui ne se contiennent pas eux-mêmes ») en limitant la manière dont les ensembles peuvent être formés.
| Axiome | Déclaration informelle |
|-------|--------------------|
| Extensionnalité | Deux ensembles sont égaux s'ils ont les mêmes éléments |
| Ensemble vide | Il existe un ensemble sans éléments : ∅ |
| Appariement | Pour tout a, b, il existe {a, b} |
| Syndicat | Pour toute famille d'ensembles, leur union existe |
| Ensemble de puissance | Pour tout ensemble S, l'ensemble de tous les sous-ensembles de S existe : P(S) |
| Infini | Il existe un ensemble infini |
| Spécification | Pour tout ensemble A et propriété P, {x ∈ A : P(x)} existe |
| Remplacement | L'image d'un ensemble sous une fonction définissable est un ensemble |
| Régularité | Chaque ensemble non vide contient un élément disjoint (empêche l'auto-appartenance) |
| Choix | Pour toute famille d'ensembles disjoints par paires non vides, une fonction de choix existe |
### Cardinalité et taille des ensembles
La **cardinalité** d'un ensemble, notée |S|, mesure sa « taille ».
| Concepts | Définition | Exemple |
|---------|------------|---------|
| Ensemble fini | A un nombre naturel comme cardinalité | |{une,b,c}| = 3 |
| Dénombrablement infini | Même cardinalité que ℕ | ℤ, ℚ sont dénombrables |
| Indénombrable | Plus grand que ℕ | ℝ, P(ℕ), l'ensemble de toutes les fonctions ℕ → {0,1} |
| Théorème de Cantor | Pour tout ensemble S, |P(S)| > |S| | |P(ℕ)| > |ℕ| |
**L'argument diagonal de Cantor** prouve que ℝ est indénombrable : supposons que vous puissiez lister tous les réels dans [0,1], puis construisez un nouveau réel qui diffère du nième réel répertorié à la nième décimale - contradiction.
### Opérations sur les ensembles
| Opération | Notations | Définition | Propriété |
|-----------|----------|------------|----------|
| Syndicat | UNE ∪B | {x : x ∈ A ou x ∈ B} | Commutatif, associatif |
| Intersection | UNE ∩B | {x : x ∈ A et x ∈ B} | Commutatif, associatif |
| Différence | A\B | {x : x ∈ A et x ∉ B} | Non commutatif |
| Différence symétrique | UNE△B | (UNE \ B) ∪ (B \ UNE) | Commutatif, associatif |
| Complément | Aᶜ | U \ A (où U est un ensemble universel) | (UNEᶜ)ᶜ = UNE |
| Produit cartésien | UNE×B | {(une,b) : une ∈ UNE, b ∈ B} | |A × B| = |UNE| · |B| |
**Les lois de De Morgan :**
- (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ
- (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
**Principe d'inclusion-exclusion** (pour les ensembles finis) :
|UNE₁ ∪ UNE₂ ∪ ... ∪ UNEₙ| = Σ|Aᵢ| − Σ|Aᵢ ∩ Aⱼ| + Σ|Aᵢ ∩ Aⱼ ∩ Aₖ| − ... + (−1)ⁿ⁺¹|A₁ ∩ ... ∩ Aₙ|
---

## Relations
Une **relation** R sur les ensembles A et B est un sous-ensemble de A × B. Lorsque (a, b) ∈ R, on écrit aRb.
### Types de relations
Une relation R sur un ensemble A peut avoir ces propriétés :
| Propriété | Définition | Exemple |
|--------------|------------|--------------|
| Réflexif | ∀a ∈ A : aRa | ≤ sur ℤ |
| Irréflexif | ∀a ∈ A : ¬(aRa) | < le ℤ |
| Symétrique | ∀a,b : aRb → bRa | = sur n'importe quel ensemble |
| Antisymétrique | ∀a,b : aRb ∧ bRa → a = b | ≤ sur ℤ |
| Transitif | ∀a,b,c : aRb ∧ bRc → aRc | <, ≤, = sur ℤ |
### Relations d'équivalence
Une **relation d'équivalence** est réflexive, symétrique et transitive. Il divise un ensemble en **classes d'équivalence** disjointes.
**Exemple :** Arithmétique modulaire. Définissez a ~ b ssi a ≡ b (mod n). Les classes d'équivalence sont [0], [1], ..., [n−1], qui divisent ℤ en n classes.
**Exemple pratique :** Sur ℤ × ℤ, définissez (a,b) ~ (c,d) ssi a + d = b + c. Il s'agit d'une relation d'équivalence. La classe [(0,0)] = {(n,n) : n ∈ ℤ}. La classe [(1,0)] = {(n+1,n) : n ∈ ℤ}. Cette construction définit en fait les entiers à partir des nombres naturels.
### Commandes partielles
Un **ordre partiel** est réflexif, antisymétrique et transitif. Un ensemble avec un ordre partiel est appelé un **ensemble partiellement ordonné (poset)**.
| Concepts | Définition | Exemple |
|---------|------------|---------|
| Poset | (S, ≤) avec ≤ un ordre partiel | (P(A), ⊆) — sous-ensembles ordonnés par inclusion |
| Chaîne | Un sous-ensemble totalement ordonné | {∅, {a}, {a,b}} dans P({a,b,c}) |
| Antichaîne | Un sous-ensemble où aucun élément n'est comparable | {{a}, {b}} dans P({a,b}) |
| Diagramme de Hasse | Représentation visuelle d'un poset | Dessiner des arêtes uniquement pour les relations de recouvrement |
| Limite supérieure | Un élément ≥ chaque élément d'un sous-ensemble | sup({2,3}) = 6 dans (ℤ, \|) (divisibilité) |
| Moins limite supérieure (sup) | Plus petite limite supérieure | sup({2,3}) dans (ℕ, ≤) est 3 |
| Plus grande limite inférieure (inf) | Plus grande limite inférieure | inf({4,6}) dans (ℕ, \|) est 2 |
---

## Fonctions
A **fonction** f : A → B attribue à chaque élément de A exactement un élément de B.
### Classification des fonctions
| Tapez | Définition | Exemple |
|------|------------|--------------|
| Injectif (un-à-un) | f(une) = f(b) → une = b | f(x) = 2x de ℤ → ℤ |
| Surjectif (sur) | ∀b ∈ B, ∃a ∈ A : f(a) = b | f(x) = x mod 2 de ℤ → {0,1} |
| Bijectif | À la fois injectif et surjectif | f(x) = x + 1 de ℤ → ℤ |
### Concepts de fonctions importants
| Concepts | Définition | Cas d'utilisation |
|---------|------------|----------|
| Fonction inverse | f⁻¹ existe si et seulement si f est bijectif | Décryptage des données cryptées |
| Composition | (g ∘ f)(x) = g(f(x)) | Enchaînement des transformations |
| Fonction d'identité | identifiant(x) = x | Élément neutre pour la composition |
| Point fixe | f(x) = x | Définitions récursives, sémantique |
| Permutations | Une bijection d'un ensemble vers lui-même | Réorganisation des données, brassage |
### Fonctions de comptage
Étant donné des ensembles finis |A| = m et |B| = n :
| Tapez | Comte |
|------|-------|
| Toutes les fonctions A → B | nᵐ |
| Fonctions injectives | n! / (n−m) ! (si n ≥ m, sinon 0) |
| Fonctions surjectives | Σₖ₌₀ⁿ (−1)ᵏ · C(n,k) · (n−k)ᵐ (par inclusion-exclusion) |
| Fonctions bijectives | n! (quand m = n) |
---

## Combinatoire
La combinatoire est la mathématique du comptage, de l’arrangement et de la sélection.
### Principes fondamentaux de comptage
| Principe | Déclaration | Exemple |
|-----------|-----------|--------------|
| Règle de somme | Si A et B sont disjoints, |A ∪ B| = |UNE| + |B| | Choisir un fruit : 3 pommes + 4 oranges = 7 options |
| Règle du produit | |A × B| = |UNE| · |B| | Tenue : 3 chemises × 4 pantalons = 12 tenues |
| Règle de bijection | Si f : A → B est une bijection, |A| = |B| | Compter les sous-ensembles en comptant les chaînes binaires |
| Complément | |UNE| = |U| − |Aᶜ| | Comptez "au moins un" comme total moins "aucun" |
### Permutations et combinaisons
| Notations | Nom | Formule | Signification |
|--------------|------|---------|---------|
| C(n, k) ou (n k) | Coefficient binomial | n! / (k!(n−k)!) | Façons de choisir k éléments parmi n (l’ordre n’a pas d’importance) |
| P(n,k) | k-permutations de n | n! / (n−k) ! | Façons d'organiser k éléments à partir de n (l'ordre compte) |
| n! | Factorielle | n × (n−1) × ... × 1 | Façons d'organiser les n éléments |
| (n k) avec répétition | Choix multiples | C(n+k−1, k) | Choisissez k parmi n avec répétition autorisée |
**Théorème binomial :**
(x + y)ⁿ = Σₖ₌₀ⁿ C(n,k) · xᵏ · yⁿ⁻ᵏ
**Identité de Pascal :** C(n,k) = C(n−1,k−1) + C(n−1,k)
### Le principe du pigeonnier
**Forme de base :** Si n+1 objets sont placés dans n cases, au moins une case contient ≥ 2 objets.
**Forme générale :** Si N objets sont placés dans k boîtes, au moins une boîte contient ≥ ⌈N/k⌉ objets.
**Exemples concrets :**
1. Parmi 13 personnes, au moins 2 partagent un mois de naissance. (13 personnes, 12 mois → casier.)
2. Montrer que parmi 5 entiers quelconques, il en existe 3 dont la somme est divisible par 3.
   - Considérons les résidus mod 3 : {0, 1, 2}. Avec 5 entiers et 3 classes de résidus, par casier généralisé, au moins ⌈5/3⌉ = 2 partagent un résidu.
   - Si 3 partagent un résidu r : leur somme ≡ 3r ≡ 0 (mod 3).
   - Si 2 partagent le résidu 0 et 2 partagent le résidu 1 : choisissez-en un dans chaque paire plus un élément résidu-0 → somme ≡ 0 (mod 3).
3. **Application dans CS :** Tout algorithme de compression sans perte doit étendre certaines entrées. (Si chaque chaîne de n bits est compressée en <n bits, vous mapperez 2ⁿ chaînes en moins de 2ⁿ chaînes compressées, ce qui violerait l'injectivité.)
### Numéros catalans
Le nième **nombre catalan** Cₙ = C(2n, n) / (n+1) compte :
| Structure | Exemple |
|-----------|---------|
| Séquences de parenthèses valides | ()(), (()) pour n = 2 |
| Arbres binaires à n nœuds internes | 2 arbres pour n = 2 |
| Chemins ne traversant pas la diagonale | Chemins de grille de (0,0) à (n,n) restant en dessous de y = x |
| Triangulations d'un polygone | Façons de diviser un (n+2)-gon en triangles |
Premiers : C₀ = 1, C₁ = 1, C₂ = 2, C₃ = 5, C₄ = 14, C₅ = 42.
Récurrence : Cₙ₊₁ = Σᵢ₌₀ⁿ Cᵢ · Cₙ₋ᵢ
---

## Relations de récurrence
Une **relation de récurrence** définit chaque terme d'une séquence en fonction des termes précédents.
### Types et solutions
| Tapez | Formulaire | Méthode de résolution |
|------|------|-----------------|
| Linéaire homogène (coeff. constant) | uneₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ | Équation caractéristique |
| Linéaire non homogène | uneₙ = c₁aₙ₋₁ + ... + f(n) | Solution particulière + solution homogène |
| Diviser et conquérir | T(n) = aT(n/b) + f(n) | Théorème principal |
### Méthode d'équation caractéristique
Pour aₙ = c₁aₙ₋₁ + c₂aₙ₋₂, former l'équation caractéristique :
r² − c₁r − c₂ = 0
| Cas | Racines | Solution générale |
|------|-------|------------------|
| Deux racines réelles distinctes r₁, r₂ | r₁ ≠ r₂ | aₙ = A·r₁ⁿ + B·r₂ⁿ |
| Racine répétée r | r₁ = r₂ = r | aₙ = (A + Bn)·rⁿ |
| Racines complexes α ± βi | Convertir en polaire : r·e^(±iθ) | uneₙ = rⁿ(UNE cos(nθ) + B sin(nθ)) |
**Exemple concret :** Séquence de Fibonacci Fₙ = Fₙ₋₁ + Fₙ₋₂, F₀ = 0, F₁ = 1.
- Équation caractéristique : r² − r − 1 = 0
- Racines : r = (1 ± √5) / 2 → φ = (1+√5)/2 ≈ 1,618, ψ = (1−√5)/2 ≈ −0,618
- Solution générale : Fₙ = A·φⁿ + B·ψⁿ
- A partir des conditions initiales : A = 1/√5, B = −1/√5
- **Forme fermée :** Fₙ = (φⁿ − ψⁿ) / √5 (formule de Binet)
### Le théorème principal
Pour les récurrences de la forme T(n) = aT(n/b) + f(n) où a ≥ 1, b > 1 :
Soit c = log_b(a).
| Cas | État | Solutions |
|------|-----------|--------------|
| 1 | f(n) = O(nᵈ) où d< c | T(n) = Θ(nᶜ) |
| 2 | f(n) = Θ(nᶜ) | T(n) = Θ(nᶜ log n) |
| 3 | f(n) = Θ(nᵈ) where d >c, et af(n/b) ≤ kf(n) pour certains k < 1 | T(n) = Θ(nᵈ) |
**Exemples :**
- Tri par fusion : T(n) = 2T(n/2) + O(n). Ici a=2, b=2, c=1, f(n)=n=Θ(n¹). Cas 2 : T(n) = Θ(n log n).
- Recherche binaire : T(n) = T(n/2) + O(1). Ici a=1, b=2, c=0, f(n)=1=Θ(n⁰). Cas 2 : T(n) = Θ(log n).
---

## Génération de fonctions
Une **fonction génératrice** code une séquence (aₙ) sous forme de coefficients d'une série de puissances formelle.
###Type
| Tapez | Formulaire | Cas d'utilisation |
|------|------|----------|
| Ordinaire (OGF) | G(x) = Σₙ₌₀^∞ aₙxⁿ | Structures, compositions sans étiquette |
| Exponentiel (EGF) | E(x) = Σₙ₌₀^∞ aₙxⁿ/n ! | Structures étiquetées, permutations |
### Fonctions de génération communes
| Séquence aₙ | OGF G(x) |
|-------------|-----------|
| 1, 1, 1, 1, ... | 1/(1−x) |
| 1, 2, 3, 4, ... | 1/(1−x)² |
| 1, r, r², r³, ... | 1/(1−rx) |
| C(n,k) pour k fixe | xᵏ/(1−x)ᵏ⁺¹ |
| Fibonacci Fₙ | x/(1−x−x²) |
| Catalan Cₙ | (1 − √(1−4x)) / (2x) |
### Utiliser des fonctions de génération pour résoudre les récurrences
**Exemple pratique :** Résolvez aₙ = 3aₙ₋₁ − 2aₙ₋₂, a₀ = 1, a₁ = 3.
1. Soit G(x) = Σ aₙxⁿ.
2. De la récurrence : G(x) − a₀ − a₁x = 3x(G(x) − a₀) − 2x²G(x)
3. Substitut : G(x) − 1 − 3x = 3x(G(x) − 1) − 2x²G(x)
4. G(x)(1 − 3x + 2x²) = 1
5. G(x) = 1 / (1 − 3x + 2x²) = 1 / ((1−x)(1−2x))
6. Fractions partielles : G(x) = 2/(1−2x) − 1/(1−x)
7. Extraire les coefficients : aₙ = 2·2ⁿ − 1 = 2ⁿ⁺¹ − 1
**Vérification :** a₀ = 2−1 = 1, a₁ = 4−1 = 3, a₂ = 8−1 = 7. Vérifiez : 3(3) − 2(1) = 7.
---

## Algèbre booléenne et logique propositionnelle
L'algèbre booléenne est l'algèbre de deux valeurs de vérité : **Vrai (1)** et **Faux (0)**. C'est le fondement mathématique des circuits numériques, des requêtes de bases de données et des conditions de programmation.
### Opérations et lois
| Opération | Symbole | Signification | Table de vérité |
|-----------|--------|---------|-------------|
| ET | p ∧ q | Vrai seulement lorsque les deux sont vrais | T∧T=T, T∧F=F, F∧T=F, F∧F=F |
| OU | p ∨ q | Vrai quand au moins un est vrai | T∨T=T, T∨F=T, F∨T=T, F∨F=F |
| PAS | ¬p | Négation | ¬T=F, ¬F=T |
| XOR | p ⊕ q | Vrai quand exactement un est vrai | T⊕T=F, T⊕F=T, F⊕T=T, F⊕F=F |
| IMPLIQUE | p → q | Faux uniquement lorsque p=T et q=F | T → T = T, T → F = F, F → T = T, F → F = T |
| BICONDITIONNEL | p ↔ q | Vrai lorsque les deux ont la même valeur | T↔T=T, T↔F=F, F↔T=F, F↔F=T |
### Identités booléennes clés
| Droit | Formule |
|-----|--------|
| Commutativité | p ∧ q = q ∧ p; p ∨ q = q ∨ p |
| Associativité | (p ∧ q) ∧ r = p ∧ (q ∧ r) |
| Distributivité | p ∧ (q ∨ r) = (p ∧ q) ∨ (p ∧ r) |
| Les lois de De Morgan | ¬(p ∧ q) = ¬p ∨ ¬q; ¬(p ∨ q) = ¬p ∧ ¬q |
| Double négation | ¬(¬p) = p |
| Idempotence | p ∧ p = p; p ∨ p = p |
| Absorption | p ∨ (p ∧ q) = p; p ∧ (p ∨ q) = p |
| Contrapositif | (p → q) ≡ (¬q → ¬p) |
### Formes normales
| Formulaire | Structure | Cas d'utilisation |
|------|-----------|--------------|
| Forme Conjonctive Normale (CNF) | ET des OU : (A∨B) ∧ (C∨D) | Solveurs SAT, preuve du théorème de résolution |
| Forme normale disjonctive (DNF) | OU des ET : (A∧B) ∨ (C∧D) | Conception de circuits, systèmes basés sur des règles |
**Conversion en CNF :** Appliquez les lois de De Morgan, distribuez OU sur ET, éliminez les doubles négations.
---

## Arithmétique modulaire et congruences
L'arithmétique modulaire étudie les nombres entiers sous l'opération du « reste après division ». Il est essentiel pour la cryptographie, le hachage et la théorie des nombres.
### Définitions de base
| Concepts | Notations | Définition |
|---------|----------|------------|
| Congruence | une ≡ b (mod n) | n divise (a − b) |
| Classe de résidus | [une]ₙ | L'ensemble {a + kn : k ∈ ℤ} |
| Inverse modulaire | a⁻¹ mod n | Valeur x telle que ax ≡ 1 (mod n) |
| Le totient d'Euler | (n) | Nombre d'entiers dans {1,...,n} premiers à n |
### Propriétés clés
| Propriété | Déclaration |
|----------|----------|
| Ajout | Si a ≡ b et c ≡ d (mod n), alors a+c ≡ b+d (mod n) |
| Multiplications | Si a ≡ b et c ≡ d (mod n), alors ac ≡ bd (mod n) |
| Le petit théorème de Fermat | Si p est premier et pgcd(a,p) = 1, alors aᵖ⁻¹ ≡ 1 (mod p) |
| Théorème d'Euler | Si pgcd(a,n) = 1, alors a^φ(n) ≡ 1 (mod n) |
| Théorème des restes chinois | Si pgcd(m,n) = 1, le système x ≡ a (mod m), x ≡ b (mod n) a une solution unique mod mn |
### Calcul du Totient d'Euler
Pour n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ (factorisation première) :
φ(n) = n · (1 − 1/p₁) · (1 − 1/p₂) · ... · (1 − 1/pₖ)
**Exemple :** φ(12) = 12 · (1 − 1/2) · (1 − 1/3) = 12 · 1/2 · 2/3 = 4. En effet, {1, 5, 7, 11} sont premiers à 12.
### Application : Cryptographie RSA (présentation)
1. Choisissez de grands nombres premiers p, q. Calculez n = pq, φ(n) = (p−1)(q−1).
2. Choisissez e tel que pgcd(e, φ(n)) = 1 (exposant public).
3. Calculez d ≡ e⁻¹ (mod φ(n)) (exposant privé).
4. Chiffrer : c = mᵉ mod n. Décrypter : m = cᵈ mod n.
5. La sécurité repose sur la difficulté de factoriser n pour trouver p et q.
---

## Induction mathématique
**L'induction mathématique** est la principale technique de preuve pour les déclarations sur tous les nombres naturels.
### Structure d'une preuve par induction
1. **Cas de base :** Prouvez l'énoncé pour n = 0 (ou n = 1).
2. **Étape inductive :** Supposons que l'énoncé soit valable pour n = k (hypothèse inductive), puis prouvez-le pour n = k + 1.
### Variantes
| Variante | Quand utiliser |
|---------|-------------|
| Induction simple | Prouver P(k) → P(k+1) |
| Forte induction | Supposons que P(0), P(1), ..., P(k) prouvent P(k+1) |
| Induction structurelle | Prouver les propriétés de structures définies récursivement (arbres, formules) |
| Induction transfinie | Étendre l'induction à des ensembles bien ordonnés au-delà de ℕ |
**Exemple pratique (induction forte) :** Montrer que tout entier n ≥ 2 peut être écrit comme un produit de nombres premiers.
- Base : n = 2 est premier, c'est donc un produit de nombres premiers (lui-même).
- Étape inductive : Supposons vrai pour tous les entiers de 2 à k. Considérons k+1.
  - Si k+1 est premier, c'est fait.
  - Si k+1 est composite, k+1 = ab où 2 ≤ a, b ≤ k. D’après l’hypothèse inductive, a et b sont tous deux des produits de nombres premiers, donc k+1 est un produit de nombres premiers.
---

## Pertinence pour l'apprentissage automatique et la science des données
| Concept mathématique discret | Application en ML / Science des données |
|-----------------------|----------------------------------|
| Théorie des ensembles | Opérations de base de données (SQL JOIN), manipulation d'ensembles de fonctionnalités, événements de probabilité |
| Relations | Schémas de bases de données, modélisation entité-relation, graphiques de connaissances |
| Fonctions | Fonctions d'activation, transformations de fonctionnalités, mappages entre espaces |
| Combinatoire | Sélection de fonctionnalités (choix de k parmi n), dimensionnement de la recherche de grille d'hyperparamètres |
| Principe du casier | Collisions de hachage, limites inférieures de la compression, preuves de la théorie de l'information |
| Relations de récurrence | Programmation dynamique, analyse de la complexité des algorithmes, modèles de séries chronologiques |
| Génération de fonctions | Fonctions génératrices de probabilités, résolution de problèmes combinatoires dans l'ingénierie des fonctionnalités |
| Numéros catalans | Comptage des structures arborescentes (arbres de décision), analyse d'expressions, opérations de pile |
| Théorie des graphes (voir fichier suivant) | Analyse des réseaux sociaux, systèmes de recommandation, représentation des connaissances |
---

## Résumé
| Sujet | Idée de base | Outil clé |
|-------|-----------|--------------|
| Théorie des ensembles | Collections d'objets distincts | Axiomes ZFC, cardinalité, opérations |
| Relations | Connexions entre éléments | Relations d'équivalence, ordres partiels |
| Fonctions | Mappages entre ensembles | Injectivité, surjectivité, bijection |
| Combinatoire | Dispositions de comptage | Coefficients binomiaux, principe du casier |
| Relations de récurrence | Séquences définies récursivement | Equations caractéristiques, Théorème principal |
| Génération de fonctions | Séquences sous forme de séries entières | OGF/EGF, résolution algébrique des récurrences |
Les mathématiques discrètes fournissent le langage et les outils nécessaires au raisonnement sur des structures finies ou dénombrables – ce que manipulent précisément les ordinateurs. Chaque algorithme, structure de données, requête de base de données et protocole cryptographique repose sur des fondations discrètes. La maîtrise de ces sujets aiguise la capacité de résolution de problèmes et fournit le vocabulaire nécessaire à des études avancées en algorithmique, en théorie de la complexité et en apprentissage automatique.