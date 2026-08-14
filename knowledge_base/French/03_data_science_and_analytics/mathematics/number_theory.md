---
# Metadata
title: "Number Theory"
description: "Divisibility, primes, modular arithmetic, Euler's theorem, Fermat's little theorem, Chinese Remainder Theorem, and applications to cryptography"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into number theory"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [number-theory, primes, divisibility, modular-arithmetic, cryptography, euler-theorem, fermat, chinese-remainder-theorem]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "discrete_mathematics.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Théorie des nombres
La théorie des nombres est l'étude des nombres entiers, c'est-à-dire des nombres entiers et de leurs propriétés. Gauss l'appelait « la reine des mathématiques ». Même si elle étudie les objets les plus simples (1, 2, 3, ...), la théorie des nombres produit certains des problèmes les plus profonds et les plus difficiles de toutes les mathématiques. Aujourd’hui, il sous-tend la cryptographie moderne, les algorithmes de hachage, les codes correcteurs d’erreurs et la génération de nombres aléatoires.
---

## Divisibilité et algorithme de division
### Définitions de base
| Terme | Définition | Exemple |
|------|------------|--------------|
| **Divisions** | un \| b signifie ∃k ∈ ℤ : b = ak | 3 \| 12 (puisque 12 = 3 × 4) |
| **Diviseur** | Un nombre qui en divise un autre | Diviseurs de 12 : 1, 2, 3, 4, 6, 12 |
| **Plusieurs** | b est un multiple de a si a \| b | 15 est un multiple de 5 |
| **Quotient** | Le résultat de la division | 17 ÷ 5 = quotient 3 |
| **Reste** | Que reste-t-il après la division | 17 ÷ 5 = reste 2 |
### L'algorithme de division
Pour tout entier a et b avec b > 0, il existe des entiers uniques q (quotient) et r (reste) tels que :
a = bq + r, où 0 ≤ r < b
**Exemple :** 23 = 5 × 4 + 3. Quotient q = 4, reste r = 3.
### Propriétés de la divisibilité
| Propriété | Déclaration |
|--------------|---------------|
| Transitivité | Si un \| b et b \| c, puis un \| c |
| Linéarité | Si un \| b et un \| c, puis un \| (bx + cy) pour tous les entiers x, y |
| Comparaison | Si un \| b et b > 0, alors a ≤ b |
| Trivial | un \| 0 pour tout a ; 1 \| un pour tout un ; un \| une pour tout une ≠ 0 |
---

## Plus grand diviseur commun (PGCD)
Le **plus grand diviseur commun** de a et b, noté pgcd(a, b), est le plus grand entier positif divisant a et b.
### L'algorithme euclidien
L'algorithme classique le plus efficace pour calculer le GCD.
**Aperçu clé :** pgcd(a, b) = pgcd(b, a mod b)
**Algorithme:**```
function gcd(a, b):
    while b ≠ 0:
        t = b
        b = a mod b
        a = t
    return a
```

**Exemple pratique :** gcd(252, 105)
- 252 = 105 × 2 + 42 → pgcd(105, 42)
- 105 = 42 × 2 + 21 → pgcd(42, 21)
- 42 = 21 × 2 + 0 → pgcd(21, 0)
- Résultat : pgcd(252, 105) = 21
| Propriété | Valeur |
|--------------|-------|
| Complexité temporelle | O(log(min(a, b))) |
| Complexité spatiale | O(1) itératif |
### L'identité de Bézout
Pour tout entier a, b, il existe des entiers x, y tels que :
hache + par = pgcd(a, b)
**Algorithme euclidien étendu** calcule simultanément pgcd(a, b) et les coefficients x, y.
**Exemple concret :** Trouvez x, y tels que 252x + 105y = 21.
- Rétro-substitution à partir de l'algorithme euclidien :
  - 21 = 105 − 42 × 2
  - 42 = 252 − 105 × 2
  - 21 = 105 − (252 − 105 × 2) × 2 = 105 × 5 − 252 × 2
- Donc x = −2, y = 5. Vérifiez : 252(−2) + 105(5) = −504 + 525 = 21.
### Propriétés clés de GCD
| Propriété | Déclaration |
|--------------|---------------|
| pgcd(a, 0) | = une |
| pgcd(a, 1) | = 1 (a et 1 sont toujours premiers entre eux) |
| pgcd(une, b) = pgcd(b, une) | Commutatif |
| pgcd(une, b) = pgcd(une, b + ka) | L'ajout de multiples ne change pas GCD |
| pgcd(ca, cb) | = c · pgcd(une, b) |
| Coprime | pgcd(a, b) = 1 signifie que a et b ne partagent aucun facteur commun |
---

## Nombres premiers
Un **premier** est un entier supérieur à 1 dont les seuls diviseurs positifs sont 1 et lui-même.
### Propriétés fondamentales
| Propriété | Déclaration |
|--------------|---------------|
| **Théorème fondamental de l'arithmétique** | Chaque entier n > 1 a une factorisation première unique |
| **Infinité de nombres premiers** | Il existe une infinité de nombres premiers (Euclide, ~ 300 avant JC) |
| **Théorème des nombres premiers** | Le nombre de nombres premiers ≤ n est approximativement n / ln(n) |
| **Postulat de Bertrand** | Pour tout n > 1, il existe un premier p avec n < p < 2n |
### Les premiers nombres premiers
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...

### Factorisation première
Tout entier n > 1 peut s’écrire de manière unique sous la forme :
n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ
où p₁ < p₂ < ... < pₖ sont des nombres premiers et aᵢ ≥ 1.
**Exemples :**
- 60 = 2² × 3 × 5
- 360 = 2³ × 3² × 5
- 1001 = 7 × 11 × 13
**Utilisation de la factorisation pour calculer GCD et LCM :**
- pgcd(a, b) = produit des puissances minimales des nombres premiers partagés
- lcm(a, b) = produit des puissances maximales de tous les nombres premiers
**Exemple :** a = 12 = 2² × 3, b = 18 = 2 × 3²
- pgcd(12, 18) = 2¹ × 3¹ = 6
- lcm(12, 18) = 2² × 3² = 36
### Tamis d'Ératosthène
L'algorithme classique pour trouver tous les nombres premiers jusqu'à une limite N.
| Propriété | Valeur |
|--------------|-------|
| Complexité temporelle | O(N journal journal N) |
| Complexité spatiale | O(N) |
**Algorithme :**
1. Listez tous les entiers de 2 à N.
2. Commencez par p = 2. Rayez tous les multiples de p (en commençant par p²).
3. Recherchez le prochain numéro non barré > p. Réglez p sur ce nombre.
4. Répétez jusqu'à ce que p² > N. Tous les nombres non croisés sont premiers.
### Test de primalité
| Méthode | Tapez | Temps | Cas d'utilisation |
|--------|------|------|--------------|
| Division de première instance | Déterministe | O(√n) | Petits nombres |
| Test de Fermat | Probabiliste | O(klog²n) | Dépistage rapide |
| Miller-Rabin | Probabiliste | O(klog²n) | Usage général |
| AKS | Déterministe | O(log⁶n) | Importance théorique |
**Test de primalité de Fermat :** Si p est premier et pgcd(a, p) = 1, alors aᵖ⁻¹ ≡ 1 (mod p). Si cela échoue pour certains a, alors p est définitivement composite. S'il correspond à de nombreuses valeurs a aléatoires, p est probablement premier.
**Attention :** Les nombres de Carmichael (par exemple, 561) réussissent le test de Fermat pour toutes les bases premières entre elles, mais sont composites. Miller-Rabin évite ce problème.
---

## Arithmétique modulaire
L'arithmétique modulaire étudie les entiers sous « wraparound » – l'arithmétique sur un cadran d'horloge.
### Relations de congruence
a ≡ b (mod n) signifie n | (a − b), c'est-à-dire que a et b laissent le même reste lorsqu'ils sont divisés par n.
### Propriétés arithmétiques
| Opération | Règle |
|---------------|------|
| Ajout | (a + b) mod n = ((a mod n) + (b mod n)) mod n |
| Multiplications | (une × b) mod n = ((une mod n) × (b mod n)) mod n |
| Exponentiation | aᵇ mod n peut être calculé efficacement par quadrature répétée |
| Négation | (−une) mod n = n − (une mod n) |
### Exponentiation modulaire
Calculer efficacement aᵇ mod n en utilisant **la quadrature répétée** :
**Exemple travaillé :** 3¹³ mod 7
- 13 en binaire : 1101
- 3¹ = 3 mod 7 = 3
- 3² = 9 mod 7 = 2
- 3⁴ = 4 mod 7 = 4
- 3⁸ = 16 mod 7 = 2
- 3¹³ = 3⁸ × 3⁴ × 3¹ = 2 × 4 × 3 = 24 mod 7 = 3
| Propriété | Valeur |
|--------------|-------|
| Complexité temporelle | O(log b · log² n) |
| Complexité spatiale | O(1) |
### Fonction Totient d'Euler
φ(n) compte les entiers de 1 à n qui sont premiers entre eux à n.
| n | (n) | Entiers premiers entre eux |
|---|------|------------------|
| 1 | 1 | {1} |
| 2 | 1 | {1} |
| 6 | 2 | {1, 5} |
| 7 | 6 | {1, 2, 3, 4, 5, 6} (7 est premier) |
| 10 | 4 | {1, 3, 7, 9} |
| 12 | 4 | {1, 5, 7, 11} |
**Formules :**
- Si p est premier : φ(p) = p − 1
- Si p est premier : φ(pᵏ) = pᵏ − pᵏ⁻¹ = pᵏ⁻¹(p − 1)
- Si pgcd(m, n) = 1 : φ(mn) = φ(m) · φ(n) (multiplicativité)
- Général : φ(n) = n · Π_{p|n} (1 − 1/p) où le produit est sur des facteurs premiers distincts de n
---

## Théorèmes clés
### Le petit théorème de Fermat
Si p est premier et pgcd(a, p) = 1, alors :
uneᵖ⁻¹ ≡ 1 (mod p)
**Corollaire (pour tout a) :** aᵖ ≡ a (mod p)
**Utiliser :** Inverse modulaire rapide lorsque le module est premier : a⁻¹ ≡ aᵖ⁻² (mod p)
**Exemple concret :** Recherchez 3⁻¹ mod 7.
- Par Fermat : 3⁻¹ ≡ 3⁵ (mod 7)
- 3² = 9 ≡ 2 (mod 7)
- 3⁴ = 4 (mod 7)
- 3⁵ = 3⁴ × 3 = 4 × 3 = 12 ≡ 5 (mod 7)
- Vérifier : 3 × 5 = 15 ≡ 1 (mod 7).
### Théorème d'Euler (Généralisation de Fermat)
Si pgcd(a, n) = 1, alors :
une^φ(n) ≡ 1 (mod n)
Cela généralise le petit théorème de Fermat des nombres premiers à n'importe quel module.
### Théorème des restes chinois (CRT)
Si m₁, m₂, ..., mₖ sont premiers entre eux deux à deux, le système :
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
...
x ≡ aₖ (modmₖ)
a une solution unique modulo M = m₁ · m₂ · ... · mₖ.
**Exemple pratique :** Résolvez x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7).
- M = 3 × 5 × 7 = 105
- M₁ = 105/3 = 35 ; M₂ = 105/5 = 21 ; M₃ = 105/7 = 15
- Trouver les inverses : 35y₁ ≡ 1 (mod 3) → 2y₁ ≡ 1 → y₁ = 2
  21y₂ ≡ 1 (mod 5) → y₂ ≡ 1 (mod 5) → y₂ = 1
  15y₃ ≡ 1 (mod 7) → y₃ ≡ 1 (mod 7) → y₃ = 1
- x = 2·35·2 + 3·21·1 + 2·15·1 = 140 + 63 + 30 = 233
-x ≡ 233 mod 105 = 23
- Vérifier : 23 mod 3 = 2, 23 mod 5 = 3, 23 mod 7 = 2.
### Théorème de Wilson
(p-1)! ≡ −1 (mod p) si et seulement si p est premier.
Surtout d'intérêt théorique - pas pratique pour les tests de primalité car le calcul des factorielles est coûteux.
### Résidus quadratiques
Un entier a est un **résidu quadratique mod n** si x² ≡ a (mod n) a une solution.
**Critère d'Euler :** a est un résidu quadratique mod premier p ssi a^((p−1)/2) ≡ 1 (mod p).
**Symbole de légende :** (a/p) = a^((p−1)/2) mod p, donnant +1, −1 ou 0.
**Réciprocité quadratique** (Gauss) : pour des nombres premiers impairs distincts p, q :
(p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2)
Ce théorème profond relie les résidus quadratiques entre différents nombres premiers et comporte huit lois supplémentaires gérant les cas p = 2.
---

## Applications à la cryptographie
### Cryptosystème RSA
Le cryptosystème à clé publique le plus largement déployé, basé sur la difficulté de factoriser de grands entiers.
**Configuration :**
1. Choisissez deux grands nombres premiers p, q (généralement plus de 1024 bits chacun)
2. Calculez n = pq et φ(n) = (p−1)(q−1)
3. Choisissez e tel que 1 < e < φ(n) et pgcd(e, φ(n)) = 1 (commun : e = 65537)
4. Calculez d ≡ e⁻¹ (mod φ(n)) à l'aide de l'algorithme euclidien étendu
5. **Clé publique :** (n, e). **Clé privée :** (n, d)
**Cryptage :** c = mᵉ mod n (où m est le message en texte brut)
**Décryptage :** m = cᵈ mod n
**Pourquoi ça marche :** cᵈ = m^(ed) ≡ m (mod n) d'après le théorème d'Euler, puisque ed ≡ 1 (mod φ(n)).
**Sécurité :** La factorisation de n dans p et q est irréalisable sur le plan informatique pour un grand n (plus de 2 048 bits). Sans p et q, un attaquant ne peut pas calculer φ(n) et ne peut donc pas trouver d.
### Échange de clés Diffie-Hellman
Permet à deux parties d'établir un secret partagé sur un canal non sécurisé.
**Configuration :** Mettez-vous d'accord sur un grand p premier et un générateur g (mod p).
**Protocole :**
1. Alice chooses secret a, sends A = gᵃ mod p to Bob
2. Bob chooses secret b, sends B = gᵇ mod p to Alice
3. Alice calcule s = Bᵃ mod p = gᵃᵇ mod p
4. Bob calcule s = Aᵇ mod p = gᵃᵇ mod p
5. Tous deux partagent le secret s = gᵃᵇ mod p
**Sécurité :** Basé sur la difficulté du **problème du logarithme discret** — trouver un à partir du mod gᵃ p.
### Fonctions de hachage et théorie des nombres
Les bonnes fonctions de hachage utilisent l'arithmétique modulaire pour distribuer les clés uniformément :
- **Hachage multiplicatif :** h(k) = (k · A) mod m, où A ≈ m · (√5 − 1) / 2 (nombre d'or)
- **Hachage universel :** h(k) = ((ak + b) mod p) mod m, où p est premier, a, b sont aléatoires
---

## Pertinence pour l'apprentissage automatique et la science des données
| Concept de théorie des nombres | Demande |
|----------------------|-------------|
| Arithmétique modulaire | Hachage (tables de hachage, cartes de hachage), génération de nombres aléatoires |
| Nombres premiers | Dimensionnement des tables de hachage (utiliser des tailles de tables principales pour réduire les collisions) |
| GCD / Euclidean algorithm | Arithmétique rationnelle, simplification des fractions en probabilité |
| Exponentiation modulaire | Sécurité cryptographique pour le modèle ML servi sur HTTPS |
| Le totient d'Euler | Génération de clés RSA, compréhension des garanties cryptographiques |
| Théorème des restes chinois | Calcul distribué, arithmétique modulaire parallèle |
| Test de primalité | Generating primes for cryptographic operations |
| Résidus quadratiques | Problème de résiduosité quadratique en cryptographie avancée |
| Finite fields (GF(p), GF(2ᵏ)) | Codes correcteurs d'erreurs, codes Reed-Solomon, cryptage AES |
---

## Résumé
| Sujet | Idée de base | Résultat clé |
|-------|-----------|------------|
| Divisibilité | Division avec reste | Algorithme de division : a = bq + r |
| PGCD | Le plus grand facteur partagé | Algorithme euclidien : O(log n) |
| Primes | Atomes des entiers | Théorème fondamental de l'arithmétique (factorisation unique) |
| Arithmétique modulaire | Arithmétique enveloppante | Classes de congruence, exponentiation modulaire |
| Le Totient d'Euler | Compter les entiers premiers entre eux | φ(n) = n · Π(1 − 1/p) |
| Le petit théorème de Fermat | Raccourci du module premier | uneᵖ⁻¹ ≡ 1 (mod p) |
| Théorème d'Euler | Fermat généralisé | une^φ(n) ≡ 1 (mod n) |
| Théorème des restes chinois | Combinaison de systèmes modulaires | Produit mod de solution unique de modules coprime |
| Cryptographie | Problèmes difficiles de théorie des nombres | RSA (affacturage), Diffie-Hellman (log discret) |
La théorie des nombres transforme des questions simples sur les nombres entiers en mathématiques approfondies avec de profondes applications pratiques. Chaque connexion Web sécurisée, message chiffré et signature numérique repose sur des résultats de la théorie des nombres découverts des siècles avant l'existence des ordinateurs. Pour les data scientists et les ingénieurs ML, comprendre la théorie des nombres donne un aperçu du hachage, de la génération de nombres aléatoires et de l'infrastructure cryptographique qui protège les données en transit et au repos.