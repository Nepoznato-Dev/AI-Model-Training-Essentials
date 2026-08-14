<!--
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
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "Nepoznato-Dev"
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

-->
# Teoria dei numeri
La teoria dei numeri è lo studio degli interi: i numeri interi e le loro proprietà. Gauss la definì "la regina della matematica". Nonostante studi gli oggetti più semplici (1, 2, 3, ...), la teoria dei numeri produce alcuni dei problemi più profondi e difficili di tutta la matematica. Oggi è alla base della crittografia moderna, degli algoritmi di hashing, dei codici di correzione degli errori e della generazione di numeri casuali.
---

## Divisibilità e algoritmo di divisione
### Definizioni fondamentali
| Termine | Definizione | Esempio |
|------|------------|---------|
| **Divide** | un \| b significa ∃k ∈ ℤ: b = ak | 3\| 12 (poiché 12 = 3 × 4) |
| **Divisore** | Un numero che ne divide un altro | Divisori di 12: 1, 2, 3, 4, 6, 12 |
| **Multipli** | b è un multiplo di a se a \| b | 15 è un multiplo di 5 |
| **Quoziente** | Il risultato della divisione | 17 ÷ 5 = quoziente 3 |
| **Resto** | Cosa resta dopo la divisione | 17 ÷ 5 = resto 2 |
### L'algoritmo della divisione
Per ogni numero intero a e b con b > 0, esistono numeri interi unici q (quoziente) e r (resto) tali che:
a = bq + r, dove 0 ≤ r < b
**Esempio:** 23 = 5 × 4 + 3. Quoziente q = 4, resto r = 3.
### Proprietà di divisibilità
| Immobile | Dichiarazione |
|----------|-----------|
| Transitività | Se un \| b e b \| c, quindi a \| c |
| Linearità | Se un \| b e a \| c, quindi a \| (bx + cy) per tutti gli interi x, y |
| Confronto | Se un \| b e b > 0, allora a ≤ b |
| Banale | un \| 0 per tutti a; 1\| a per tutti a; un \| a per ogni a ≠ 0 |
---

## Massimo Comun Divisore (MCD)
Il **massimo comun divisore** di a e b, indicato con mcd(a, b), è il più grande intero positivo che divide sia a che b.
### L'algoritmo euclideo
L'algoritmo classico più efficiente per il calcolo del GCD.
**Approfondimento chiave:** mcd(a, b) = mcd(b, a mod b)
**Algoritmo:**```
function gcd(a, b):
    while b ≠ 0:
        t = b
        b = a mod b
        a = t
    return a
```

**Esempio elaborato:** mcd(252, 105)
- 252 = 105 × 2 + 42 → mcd(105, 42)
- 105 = 42 × 2 + 21 → mcd(42, 21)
- 42 = 21 × 2 + 0 → mcd(21, 0)
- Risultato: mcd(252, 105) = 21
| Immobile | Valore |
|----------|-------|
| Complessità temporale | O(log(min(a, b))) |
| Complessità spaziale | O(1) iterativo |
### L'identità di Bézout
Per ogni numero intero a, b, esistono numeri interi x, y tali che:
ax + by = mcd(a, b)
**Algoritmo euclideo esteso** calcola mcd(a, b) e i coefficienti x, y simultaneamente.
**Esempio svolto:** Trova x, y tale che 252x + 105y = 21.
- Sostituzione all'indietro dall'algoritmo euclideo:
  - 21 = 105 − 42 × 2
  - 42 = 252 − 105 × 2
  - 21 = 105 − (252 − 105 × 2) × 2 = 105 × 5 − 252 × 2
- Quindi x = −2, y = 5. Verifica: 252(−2) + 105(5) = −504 + 525 = 21.
### Proprietà chiave del GCD
| Immobile | Dichiarazione |
|----------|-----------|
| mcd(a, 0) | = un |
| mcd(a, 1) | = 1 (a e 1 sono sempre coprimi) |
| mcd(a, b) = mcd(b, a) | Commutativo |
| mcd(a, b) = mcd(a, b + ka) | L'aggiunta di multipli non modifica il GCD |
| mcd(ca, cb) | = c · mcd(a, b) |
| Coprime | mcd(a, b) = 1 significa che a e b non condividono fattori comuni |
---

## Numeri primi
Un **primo** è un numero intero maggiore di 1 i cui unici divisori positivi sono 1 e se stesso.
### Proprietà fondamentali
| Immobile | Dichiarazione |
|----------|-----------|
| **Teorema Fondamentale dell'Aritmetica** | Ogni intero n > 1 ha un'unica scomposizione in fattori primi |
| **Infinità di numeri primi** | Esistono infiniti numeri primi (Euclide, ~300 aC) |
| **Teorema dei numeri primi** | Il numero di numeri primi ≤ n è approssimativamente n / ln(n) |
| **Postulato di Bertrand** | Per ogni n > 1 esiste un primo p con n < p < 2n |
### I primi numeri primi
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97...

### Fattorizzazione dei primi
Ogni intero n > 1 può essere scritto univocamente come:
n = p₁^a₁ · p₂^a₂ · ... · pₖ^aₖ
dove p₁ < p₂ < ... < pₖ sono primi e aᵢ ≥ 1.
**Esempi:**
- 60 = 2² × 3 × 5
- 360 = 2³ × 3² × 5
- 1001 = 7 × 11 × 13
**Utilizzo della fattorizzazione per calcolare MCD e LCM:**
- mcd(a, b) = prodotto delle potenze minime di numeri primi condivisi
- lcm(a, b) = prodotto delle potenze massime di tutti i numeri primi
**Esempio:** a = 12 = 2² × 3, b = 18 = 2 × 3²
- mcd(12, 18) = 2¹ × 3¹ = 6
- lcm(12, 18) = 2² × 3² = 36
### Setaccio di Eratostene
L'algoritmo classico per trovare tutti i primi fino al limite N.
| Immobile | Valore |
|----------|-------|
| Complessità temporale | O(N log log N) |
| Complessità spaziale | O(N) |
**Algoritmo:**
1. Elenca tutti i numeri interi da 2 a N.
2. Inizia con p = 2. Cancella tutti i multipli di p (a partire da p²).
3. Trova il successivo numero non barrato > p. Imposta p su quel numero.
4. Ripeti finché p² > N. Tutti i numeri non incrociati sono primi.
### Test di primalità
| Metodo | Digitare | Tempo | Caso d'uso |
|--------|------|------|----------|
| Divisione di prova | deterministico | O(√n) | Piccoli numeri |
| Test di Fermat | Probabilistico | O(k log² n) | Proiezione rapida |
| Miller-Rabin | Probabilistico | O(k log² n) | Scopo generale |
| AKS | deterministico | O(log⁶ n) | Importanza teorica |
**Test di primalità di Fermat:** Se p è primo e mcd(a, p) = 1, allora aᵖ⁻¹ ≡ 1 (mod p). Se questo fallisce per qualche a, allora p è sicuramente composto. Se passa per molti valori a casuali, p è probabilmente primo.
**Avvertenza:** i numeri di Carmichael (ad esempio, 561) superano il test di Fermat per tutte le basi coprime ma sono compositi. Miller-Rabin evita questo problema.
---

## Aritmetica modulare
L'aritmetica modulare studia gli interi sotto "wraparound" - aritmetica sul quadrante di un orologio.
### Relazioni di congruenza
a ≡ b (mod n) significa n | (a − b), cioè a e b lasciano lo stesso resto se divisi per n.
### Proprietà aritmetiche
| Operazione | Regola |
|-----------|------|
| Aggiunta | (a + b) mod n = ((a mod n) + (b mod n)) mod n |
| Moltiplicazione | (a × b) mod n = ((a mod n) × (b mod n)) mod n |
| Esponenziazione | aᵇ mod n può essere calcolato in modo efficiente eseguendo quadrati ripetuti |
| Negazione | (−a) mod n = n − (a mod n) |
### Esponenziazione modulare
Calcolare aᵇ mod n in modo efficiente utilizzando la **quadratura ripetuta**:
**Esempio lavorato:** 3¹³ mod 7
- 13 in binario: 1101
- 3¹ = 3 mod 7 = 3
- 3² = 9 mod 7 = 2
- 3⁴ = 4 mod 7 = 4
- 3⁸ = 16 mod 7 = 2
- 3¹³ = 3⁸ × 3⁴ × 3¹ = 2 × 4 × 3 = 24 mod 7 = 3
| Immobile | Valore |
|----------|-------|
| Complessità temporale | O(log b · log² n) |
| Complessità spaziale | O(1) |
### Funzione Toziente di Eulero
φ(n) conta gli interi da 1 a n che sono coprimi con n.
| n | φ(n) | Interi coprimi |
|---|------|-----|
| 1| 1| {1} |
| 2| 1| {1} |
| 6| 2| {1, 5} |
| 7| 6| {1, 2, 3, 4, 5, 6} (7 è primo) |
| 10| 4| {1, 3, 7, 9} |
| 12| 4| {1, 5, 7, 11} |
**Formule:**
- Se p è primo: φ(p) = p − 1
- Se p è primo: φ(pᵏ) = pᵏ − pᵏ⁻¹ = pᵏ⁻¹(p − 1)
- Se mcd(m, n) = 1: φ(mn) = φ(m) · φ(n) (moltiplicatività)
- Generale: φ(n) = n · Π_{p|n} (1 − 1/p) dove il prodotto è su fattori primi distinti di n
---

## Teoremi chiave
### Il Piccolo Teorema di Fermat
Se p è primo e mcd(a, p) = 1, allora:
aᵖ⁻¹ ≡ 1 (mod p)
**Corollario (per ogni a):** aᵖ ≡ a (mod p)
**Utilizzo:** Inverso modulare veloce quando il modulo è primo: a⁻¹ ≡ aᵖ⁻² (mod p)
**Esempio realizzato:** Trova 3⁻¹ mod 7.
- Per Fermat: 3⁻¹ ≡ 3⁵ (mod 7)
- 3² = 9 ≡ 2 (mod 7)
- 3⁴ = 4 (mod 7)
- 3⁵ = 3⁴ × 3 = 4 × 3 = 12 ≡ 5 (mod 7)
- Verifica: 3 × 5 = 15 ≡ 1 (mod 7).
### Teorema di Eulero (Generalizzazione di Fermat)
Se mcd(a, n) = 1, allora:
a^φ(n) ≡ 1 (mod n)
Questo generalizza il Piccolo Teorema di Fermat dai numeri primi a qualsiasi modulo.
### Teorema cinese del resto (CRT)
Se m₁, m₂, ..., mₖ sono coprimi a due a due, il sistema:
x ≡ a₁ (mod m₁)
x ≡ a₂ (mod m₂)
...
x ≡ aₖ (mod mₖ)
ha un'unica soluzione modulo M = m₁ · m₂ · ... · mₖ.
**Esempio svolto:** Risolvi x ≡ 2 (mod 3), x ≡ 3 (mod 5), x ≡ 2 (mod 7).
- M = 3 × 5 × 7 = 105
- M₁ = 105/3 = 35; M₂ = 105/5 = 21; M₃ = 105/7 = 15
- Trova gli inversi: 35y₁ ≡ 1 (mod 3) → 2y₁ ≡ 1 → y₁ = 2
  21y₂ ≡ 1 (mod 5) → y₂ ≡ 1 (mod 5) → y₂ = 1
  15y₃ ≡ 1 (mod 7) → y₃ ≡ 1 (mod 7) → y₃ = 1
- x = 2·35·2 + 3·21·1 + 2·15·1 = 140 + 63 + 30 = 233
- x ≡ 233 mod 105 = 23
- Controlla: 23 mod 3 = 2, 23 mod 5 = 3, 23 mod 7 = 2.
### Teorema di Wilson
(p-1)! ≡ −1 (mod p) se e solo se p è primo.
Per lo più di interesse teorico, non pratico per i test di primalità poiché il calcolo dei fattoriali è costoso.
### Residui quadratici
Un intero a è un **residuo quadratico mod n** se x² ≡ a (mod n) ha soluzione.
**Criterio di Eulero:** a è un residuo quadratico mod primo p sse e se a^((p−1)/2) ≡ 1 (mod p).
**Simbolo della legenda:** (a/p) = a^((p−1)/2) mod p, che dà +1, −1 o 0.
**Reciprocità quadratica** (Gauss): Per numeri primi dispari distinti p, q:
(p/q)(q/p) = (−1)^((p−1)/2 · (q−1)/2)
Questo profondo teorema collega i residui quadratici tra diversi numeri primi e ha otto leggi supplementari che gestiscono i casi p = 2.
---

## Applicazioni alla crittografia
### Sistema crittografico RSA
Il crittosistema a chiave pubblica più diffuso, basato sulla difficoltà di fattorizzare numeri interi di grandi dimensioni.
**Configurazione:**
1. Scegli due grandi numeri primi p, q (tipicamente 1024+ bit ciascuno)
2. Calcola n = pq e φ(n) = (p−1)(q−1)
3. Scegli e tale che 1 < e < φ(n) e mcd(e, φ(n)) = 1 (comune: e = 65537)
4. Calcola d ≡ e⁻¹ (mod φ(n)) utilizzando l'algoritmo euclideo esteso
5. **Chiave pubblica:** (n, e). **Chiave privata:** (n, d)
**Crittografia:** c = mᵉ mod n (dove m è il messaggio in chiaro)
**Decifratura:** m = cᵈ mod n
**Perché funziona:** cᵈ = m^(ed) ≡ m (mod n) per il teorema di Eulero, poiché ed ≡ 1 (mod φ(n)).
**Sicurezza:** Fattorizzare n in p e q è computazionalmente impossibile per n di grandi dimensioni (2048+ bit). Senza p e q, un utente malintenzionato non può calcolare φ(n) e quindi non può trovare d.
### Scambio di chiavi Diffie-Hellman
Consente a due parti di stabilire un segreto condiviso su un canale non sicuro.
**Configurazione:** Concordare un grande numero primo p e un generatore g (mod p).
**Protocollo:**
1. Alice sceglie il segreto a, invia A = gᵃ mod p a Bob
2. Bob sceglie il segreto b, invia B = gᵇ mod p ad Alice
3. Alice calcola s = Bᵃ mod p = gᵃᵇ mod p
4. Bob calcola s = Aᵇ mod p = gᵃᵇ mod p
5. Entrambi condividono il segreto s = gᵃᵇ mod p
**Sicurezza:** Basata sulla difficoltà del **problema del logaritmo discreto** — trovare un da gᵃ mod p.
### Funzioni hash e teoria dei numeri
Buone funzioni hash utilizzano l'aritmetica modulare per distribuire le chiavi in modo uniforme:
- **Hashing moltiplicativo:** h(k) = (k · A) mod m, dove A ≈ m · (√5 − 1) / 2 (sezione aurea)
- **Hashing universale:** h(k) = ((ak + b) mod p) mod m, dove p è primo, a, b sono casuali
---

## Rilevanza per l'apprendimento automatico e la scienza dei dati
| Concetto di teoria dei numeri | Applicazione |
|----------------------|-----|
| Aritmetica modulare | Hashing (tabelle hash, mappe hash), generazione di numeri casuali |
| Numeri primi | Dimensionamento della tabella hash (utilizzare le dimensioni della tabella principale per ridurre le collisioni) |
| MCD / Algoritmo euclideo | Aritmetica razionale, semplificazione delle frazioni in probabilità |
| Esponenziazione modulare | Sicurezza crittografica per il modello ML servito su HTTPS |
| Il totiente di Eulero | Generazione di chiavi RSA, comprensione delle garanzie crittografiche |
| Teorema cinese del resto | Calcolo distribuito, aritmetica modulare parallela |
| Test di primalità | Generazione di numeri primi per operazioni crittografiche |
| Residui quadratici | Problema della residuità quadratica nella crittografia avanzata |
| Campi finiti (GF(p), GF(2ᵏ)) | Codici di correzione errori, codici Reed-Solomon, crittografia AES |
---

## Riepilogo
| Argomento | Idea fondamentale | Risultato chiave |
|-------|-----------|------------|
| Divisibilità | Divisione con resto | Algoritmo di divisione: a = bq + r |
| GCD | Fattore condiviso più grande | Algoritmo euclideo: O(log n) |
| Primi | Atomi degli interi | Teorema Fondamentale dell'Aritmetica (fattorizzazione unica) |
| Aritmetica modulare | Aritmetica avvolgente | Classi di congruenza, esponenziazione modulare |
| Il Toziente di Eulero | Conteggio di interi coprimi | φ(n) = n · Π(1 − 1/p) |
| Il piccolo teorema di Fermat | Scorciatoia del modulo Prime | aᵖ⁻¹ ≡ 1 (mod p) |
| Teorema di Eulero | Fermat generalizzato | a^φ(n) ≡ 1 (mod n) |
| Teorema cinese del resto | Combinazione di sistemi modulari | Soluzione unica prodotto mod di moduli coprimi |
| Crittografia | Problemi difficili di teoria dei numeri | RSA (fattorizzazione), Diffie-Hellman (log discreto) |
La teoria dei numeri trasforma semplici domande sugli interi in matematica profonda con profonde applicazioni pratiche. Ogni connessione web sicura, messaggio crittografato e firma digitale si basa su risultati della teoria dei numeri scoperti secoli prima che esistessero i computer. Per i data scientist e gli ingegneri ML, la comprensione della teoria dei numeri fornisce informazioni sull'hashing, sulla generazione di numeri casuali e sull'infrastruttura crittografica che protegge i dati in transito e inattivi.