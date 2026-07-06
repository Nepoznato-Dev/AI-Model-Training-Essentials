# Matematica e Logica

## Cos'è la Matematica?

La matematica è lo studio di numeri, forme, modelli e relazioni logiche. È sia una scienza che un linguaggio usato per descrivere l'universo. La matematica è divisa in rami tra cui aritmetica, algebra, geometria, calcolo, statistica e logica. La matematica è il fondamento della fisica, dell'ingegneria, dell'informatica, dell'economia e di molti altri campi.

## Aritmetica

L'aritmetica è il ramo della matematica che si occupa delle operazioni di base sui numeri. Le quattro operazioni fondamentali sono addizione (+), sottrazione (−), moltiplicazione (×) e divisione (÷). L'ordine delle operazioni specifica la sequenza in cui i calcoli devono essere eseguiti: Parentesi, Esponenti, Moltiplicazione e Divisione (da sinistra a destra), Addizione e Sottrazione (da sinistra a destra). Questo è spesso ricordato come **PEMDAS** o **BODMAS**. Un numero primo è un numero intero maggiore di 1 che non ha divisori oltre 1 e se stesso. I primi numeri primi sono 2, 3, 5, 7, 11, 13, 17, 19, 23 e 29.

**Esempi:**
- Fattorizzazione prima: 84 = 2² × 3 × 7
- Massimo Comun Divisore (MCD) di 24 e 36: 12
- Minimo Comune Multiplo (mcm) di 4 e 6: 12

## Algebra

L'algebra usa lettere e simboli per rappresentare numeri e quantità in equazioni e formule. Una **variabile** è un simbolo (di solito una lettera) che rappresenta una quantità sconosciuta o variabile. Un'**equazione** afferma che due espressioni sono uguali. Risolvere un'equazione significa trovare il valore/i valori della/e variabile/i che rendono vera l'equazione.

La **formula quadratica** risolve equazioni della forma ax² + bx + c = 0: x = (−b ± √(b²−4ac)) / (2a)

Una **funzione** mappa ogni input a esattamente un output. Le funzioni comuni includono:
- Lineare: y = mx + b (retta, tasso di cambiamento costante)
- Quadratica: y = ax² + bx + c (parabola, curva)
- Esponenziale: y = a × bˣ (crescita o decadimento, cambiamento rapido)
- Logaritmica: y = log_b(x) (inverso dell'esponenziale)

**Concetti chiave:**
- Dominio: l'insieme di tutti i possibili valori di input
- Codominio: l'insieme di tutti i possibili valori di output
- Pendenza: tasso di cambiamento (m in y = mx + b)
- Intercetta: dove la funzione interseca l'asse y (b in y = mx + b)

## Geometria

La geometria è il ramo della matematica che studia forme, dimensioni, posizioni e proprietà delle figure. Un punto non ha dimensione; rappresenta una posizione. Una retta si estende all'infinito in entrambe le direzioni. Un segmento ha due estremi. Un angolo è formato da due semirette che condividono un estremo.

**Regole chiave:**
- La somma degli angoli in un triangolo è sempre 180 gradi.
- La somma degli angoli in un quadrilatero è sempre 360 gradi.
- Il teorema di Pitagora: in un triangolo rettangolo, a² + b² = c² (dove c è l'ipotenusa).
- Circonferenza del cerchio: 2πr
- Area del cerchio: πr²
- Volume della sfera: (4/3)πr³

**π (pi greco)** è circa 3.14159 ed è il rapporto tra la circonferenza di un cerchio e il suo diametro.

**Forme geometriche comuni:**
- Triangolo: 3 lati, somma angoli 180°
- Quadrato: 4 lati uguali, 4 angoli retti
- Rettangolo: 4 lati, lati opposti uguali, 4 angoli retti
- Cerchio: nessun lato, bordo curvo continuo
- Pentagono: 5 lati, somma angoli 540°
- Esagono: 6 lati, somma angoli 720°

## Statistica e Probabilità

La statistica è la scienza di raccogliere, analizzare, interpretare e presentare dati.

**Misure di tendenza centrale:**
- **Media** (media aritmetica): somma di tutti i valori divisa per il numero di valori
- **Mediana**: valore centrale quando i dati sono ordinati (meno sensibile agli outlier)
- **Moda**: valore che si verifica più frequentemente (può avere più mode)

**Misure di dispersione:**
- **Intervallo**: massimo - minimo
- **Varianza**: media dei quadrati degli scarti dalla media
- **Deviazione standard**: radice quadrata della varianza (nelle stesse unità dei dati)

La probabilità misura la verosimiglianza che un evento si verifichi, variando da 0 (impossibile) a 1 (certo). La probabilità che due eventi indipendenti si verifichino entrambi è il prodotto delle loro probabilità individuali.

**Esempio:** Probabilità di ottenere un 6 su un dado equilibrato: 1/6. Probabilità di ottenere due 6 consecutivi: (1/6) × (1/6) = 1/36.

## Probabilità per Informatica e ML

Una **variabile casuale** è una variabile il cui valore dipende dall'esito di un processo casuale. Una **distribuzione di probabilità** descrive quanto è probabile ogni esito.

**Distribuzioni comuni:**
- **Bernoulli**: singolo tentativo con due esiti (es. lancio di moneta)
- **Binomiale**: numero di successi in n tentativi Bernoulli indipendenti
- **Normale (Gaussiana)**: curva a campana, simmetrica attorno alla media (comune nei fenomeni naturali)
- **Poisson**: numero di eventi in un intervallo fisso (es. email per ora)

Il **valore atteso** è la media a lungo termine degli esiti di una variabile casuale. La **varianza** misura la dispersione attorno a quell'aspettativa.

La **probabilità condizionata** descrive la probabilità di un evento dato che un altro evento si è verificato: P(A|B) = P(A ∩ B) / P(B) [se P(B) > 0].

Il **teorema di Bayes** aggiorna le credenze usando le evidenze: P(A|B) = P(B|A) × P(A) / P(B).

Nel machine learning, la probabilità è alla base della fiducia nella classificazione, della stima dell'incertezza, dei metodi bayesiani e di molte funzioni di loss (come cross-entropy).

## Calcolo

Il calcolo è il ramo della matematica che studia il cambiamento continuo.

Il **calcolo differenziale** si occupa di tassi di cambiamento e pendenze di curve, usando le **derivate**. La derivata di una funzione f(x) rappresenta il tasso di cambiamento di f rispetto a x in un punto. Notazione: f'(x) o df/dx.

**Derivate comuni:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

Il **calcolo integrale** si occupa dell'accumulo di quantità e delle aree sotto le curve, usando gli **integrali**. L'integrale rappresenta l'area sotto la curva tra due punti.

Il **teorema fondamentale del calcolo** collega differenziazione e integrazione: differenziazione e integrazione sono operazioni inverse.

Il calcolo fu sviluppato indipendentemente da Isaac Newton e Gottfried Wilhelm Leibniz nel XVII secolo.

## Sistemi Numerici

- **Numeri naturali**: 1, 2, 3, 4, ... (numeri per contare)
- **Numeri interi non negativi**: 0, 1, 2, 3, ... (numeri naturali più lo zero)
- **Numeri interi**: ..., −2, −1, 0, 1, 2, ... (tutti i numeri interi non negativi e i loro negativi)
- **Numeri razionali**: numeri esprimibili come p/q dove p e q sono interi e q ≠ 0 (es. 1/2, 3/4, −5/3)
- **Numeri irrazionali**: non possono essere espressi come frazione (es. √2, π, e)
- **Numeri reali**: tutti i numeri razionali e irrazionali (la retta numerica)
- **Numeri immaginari**: coinvolgono la radice quadrata di numeri negativi; i = √(−1)
- **Numeri complessi**: combinano parti reali e immaginarie (a + bi)

## Logica e Ragionamento

La logica è lo studio del ragionamento valido.

Il **ragionamento deduttivo** trae conclusioni specifiche da premesse generali. Se le premesse sono vere e l'argomento è valido, la conclusione deve essere vera.
- **Esempio:** Tutti gli umani sono mortali. Socrate è umano. Quindi, Socrate è mortale.

Il **ragionamento induttivo** trae conclusioni generali da osservazioni specifiche. Non garantisce che la conclusione sia vera, ma la rende probabile.
- **Esempio:** Ogni cigno che ho visto è bianco. Quindi, tutti i cigni sono bianchi. (Nota: questo è falso; esistono cigni neri!)

**Fallacie logiche comuni (errori nel ragionamento):**
- **Ad hominem**: attaccare la persona piuttosto che l'argomento
- **Straw man**: travisare un argomento per renderlo più facile da attaccare
- **Falsa dicotomia**: presentare solo due opzioni quando ne esistono di più
- **Ragionamento circolare**: usare la conclusione come premessa
- **Appello all'autorità**: affermare che qualcosa è vero perché un'autorità lo dice
- **Fallacia post hoc**: assumere che perché A è accaduto prima di B, A ha causato B

## Insiemi

Un **insieme** è una collezione di oggetti distinti.
- **Unione** (A ∪ B): tutti gli elementi da entrambi gli insiemi
- **Intersezione** (A ∩ B): solo elementi comuni a entrambi
- **Insieme vuoto** (∅ o {}): non contiene elementi
- **Sottoinsieme** (A ⊆ B): tutti gli elementi di A sono anche in B
- **Diagrammi di Venn**: rappresentano visivamente le relazioni tra insiemi

La teoria degli insiemi è il fondamento della matematica e della logica moderna.

## Binario e Basi Numeriche

I computer rappresentano i dati in **binario** (base 2), usando solo le cifre 0 e 1. Ogni cifra binaria è chiamata **bit**. Otto bit formano un **byte**.

Il **decimale** è il sistema numerico in base 10 che gli umani usano tipicamente.

L'**esadecimale** è in base 16, usa le cifre 0–9 e le lettere A–F, spesso usato nell'informatica per rappresentare dati binari in modo compatto.

**Conversioni:**
- Binario 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (decimale)
- Esadecimale A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (decimale)

Convertire tra basi numeriche è un concetto fondamentale nell'informatica.

## Algebra Lineare per Sviluppatori e ML

L'algebra lineare studia vettori, matrici e trasformazioni lineari.

Un **vettore** è una lista ordinata di numeri (es. feature in un campione ML).
- Esempio: [23, 1.8, 175] rappresenta età, altezza e peso di una persona

Una **matrice** è un array 2D di numeri (es. pesi del modello o batch di dataset).
- Esempio: [[1, 2], [3, 4]] è una matrice 2×2

La **moltiplicazione di matrici** combina trasformazioni lineari ed è un'operazione fondamentale in grafica, simulazione e reti neurali.

Il **prodotto scalare** misura similarità e proiezione tra vettori:
- a·b = Σ(a_i × b_i)
- **Similarità del coseno** = (a·b) / (||a|| × ||b||)
- La similarità del coseno varia da -1 (opposto) a 1 (stessa direzione)

**Autovalori e autovettori** descrivono direzioni che vengono scalate (non ruotate) da una matrice e sono usati in metodi come PCA (Principal Component Analysis).

Il **rango** indica quante informazioni indipendenti contiene una matrice. Le approssimazioni a basso rango sono utili per compressione e riduzione della dimensionalità.

La maggior parte dei carichi di lavoro ML moderni si basa pesantemente su librerie di algebra lineare ottimizzate e accelerazione hardware.
