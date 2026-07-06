# Glossario tecnologico

Un glossario di riferimento che copre modelli di intelligenza artificiale, hardware, benchmark e concetti fondamentali
nel moderno panorama dell’intelligenza artificiale e dell’informatica.

---

## Modelli linguistici e assistenti AI

###ChatGPT
ChatGPT è un chatbot AI sviluppato da OpenAI, rilasciato per la prima volta nel novembre 2022.
È alimentato dalla serie GPT di modelli linguistici di grandi dimensioni (LLM). ChatGPT è uno
dei prodotti AI di consumo in più rapida crescita nella storia, raggiungendo i 100 milioni
utenti entro due mesi dal lancio. Supporta conversazioni basate su testo, code
generazione, sintesi e scrittura creativa. I livelli a pagamento forniscono l'accesso a
modelli più potenti come GPT-4 e GPT-4o.

### GPT (trasformatore generativo pre-addestrato)
GPT è una famiglia di modelli linguistici di grandi dimensioni creata da OpenAI. L'architettura
utilizza un trasformatore solo decoder addestrato con un obiettivo di previsione del token successivo attivato
corpora testuali massicci. Le versioni chiave includono GPT-2 (2019, parametri 1.5B, notevoli
per pubblicità "troppo pericoloso per essere rilasciata"), GPT-3 (2020, parametri 175B, ampiamente
utilizzato tramite API), GPT-3.5 (la spina dorsale dell'originale ChatGPT) e GPT-4
(2023, multimodale, prestazioni vicine al livello di un esperto umano su molti parametri di riferimento).

### Claudio
Claude è un assistente AI sviluppato da Anthropic. Prende il nome da Claude
Shannon, il fondatore della teoria dell'informazione. Anthropic è stata fondata da ex
I ricercatori di OpenAI si concentrano sull'"intelligenza artificiale costituzionale": una tecnica da realizzare
modelli più sicuri addestrandoli a seguire una serie di principi. I modelli di Claudio
(Claude 1, 2, 3 Haiku / Sonetto / Opus) sono noti per finestre contestuali lunghe (su
a 200.000 token), ragionamento sfumato e output dannoso ridotto rispetto a
LLM di base.

### Gemelli
Gemini è la famiglia di modelli IA multimodali di Google DeepMind, annunciata nel
Dicembre 2023. Gemini è nativamente multimodale: addestrato da zero
testo, immagini, audio e video contemporaneamente, a differenza dei modelli precedenti che avevano
modalità aggiunte tramite la messa a punto. Le versioni includono Gemini Nano (sul dispositivo),
Gemini Flash (veloce, conveniente) e Gemini Ultra (massima capacità).
Gemini alimenta il chatbot AI di Google Bard (rinominato Gemini) e l'intelligenza artificiale di Ricerca Google
Panoramica.

### Phi-3-mini
Phi-3-mini è un Small Language Model (SLM) sviluppato da Microsoft con 3.8B
parametri. È stato rilasciato nell'aprile 2024. A differenza della maggior parte dei modelli di grandi dimensioni, Phi-3-mini
è stato addestrato su un set di dati di "qualità da libro di testo" attentamente curato: una tecnica
introdotto da Microsoft Research, che dà priorità alla qualità dei dati rispetto al volume grezzo.
Nonostante sia molto più piccolo di GPT-4 o Claude 3 Opus, Phi-3-mini corrisponde o
supera i modelli molte volte più grandi su benchmark di ragionamento come MMLU e
Valutazione umana. Supporta una finestra di contesto token da 4k nella sua variante base e una da 128k
finestra nella variante a contesto lungo. Phi-3-mini può essere eseguito su una singola GPU consumer
o anche sul dispositivo su uno smartphone moderno con RAM sufficiente.

### Lama (Meta AI)
Llama (Large Language Model Meta AI) è una famiglia di modelli a peso aperto
rilasciato da Meta. Llama 2 (2023) è stato rilasciato per ricerca e uso commerciale
con dimensioni che vanno dai parametri 7B a 70B. Lama 3 (2024) migliorato
prestazioni in modo significativo, con modelli che vanno da 8B a 70B (e successivamente 400B+).
Poiché i pesi sono scaricabili pubblicamente, i modelli Llama costituiscono la base
per un ampio ecosistema di varianti calibrate (Mistral, Alpaca, Vicuna, ecc.)
e sono ampiamente utilizzati per distribuzioni di IA locali/private.

### Maestrale
Mistral AI è una società francese di intelligenza artificiale che sviluppa LLM aperti e proprietari.
Mistral 7B (2023) ha dimostrato che un modello con parametri 7B può corrispondere al
prestazioni di modelli molto più grandi utilizzando tecniche efficienti come lo scorrimento
attenzione alla finestra e attenzione alle query raggruppate. Mixtral 8x7B (2024) è una miscela-
modello di esperti: instrada ciascun token a un sottoinsieme di 8 reti di esperti,
raggiungere prestazioni di livello GPT-3.5 pur essendo computazionalmente più economico.
I modelli Mistral sono completamente a peso aperto e possono essere utilizzati localmente.

---

## Hardware GPU e schede grafiche

### GPU (unità di elaborazione grafica)
Una GPU è un processore progettato per calcoli massivamente paralleli. Originariamente
costruite per il rendering della grafica 3D, le GPU sono diventate essenziali per la formazione AI/ML
e inferenza perché possono eseguire migliaia di operazioni in virgola mobile
utilizzando contemporaneamente migliaia di piccoli core. I due principali produttori di GPU
per l'intelligenza artificiale sono NVIDIA e AMD.

### Serie NVIDIA GeForce RTX
La serie RTX (Ray Tracing Texel eXtreme) è la linea di GPU consumer di NVIDIA. RTX
Le generazioni 30xx (Ampere, 2020) e RTX 40xx (Ada Lovelace, 2022) includono
Tensor Core dedicati per accelerare le operazioni di intelligenza artificiale. VRAM (RAM video) lo è
fondamentale per l'esecuzione locale di modelli IA: una GPU da 8 GB può gestire parametri 7B
modelli in quantizzazione a 4 bit; una GPU da 24 GB può gestire modelli da 70 B a 4 bit.### NVIDIA Serie A e Serie H (data center)
A100 (Ampere, 2020) e H100 (Hopper, 2022) sono l'intelligenza artificiale professionale di NVIDIA
acceleratori. Un H100 ha fino a 80 GB di memoria HBM3 ed è lo standard
hardware dietro la maggior parte della formazione LLM su larga scala oggi. Queste GPU costano $ 25.000–
$ 40.000 ciascuna ma offrono 10-30 volte il throughput AI delle schede RTX consumer.

### Serie AMD Radeon RX
La linea di GPU consumer di AMD. La RX 7900 XTX (2022) ha 24 GB di VRAM e può funzionare
LLM locali tramite ROCm (stack di calcolo GPU di AMD). Le GPU AMD sono generalmente inferiori
ben supportato rispetto a NVIDIA per i framework AI, sebbene il supporto stia migliorando.

### Arco Intel
Intel Arc è la linea di prodotti GPU discreti di Intel, rilasciata a partire dal 2022. Arc
Le GPU supportano XeSS (il super-sampling di Intel) e hanno un supporto limitato ma in crescita
per attività di inferenza AI tramite framework OpenVINO e IPEX-LLM.

### ARK Intel (ark.intel.com)
ARK è il database ufficiale delle specifiche dei prodotti Intel su ark.intel.com. Esso
fornisce specifiche tecniche dettagliate per ogni CPU, GPU, FPGA e
Prodotto NUC, inclusi numero di core, velocità di clock, TDP, tipi di memoria supportati,
e funzionalità del set di istruzioni. Quando senti "controlla le specifiche di ARK", significa
visitando quel database per informazioni hardware autorevoli.

---

## Benchmark delle prestazioni dell'IA

### MMLU (Comprensione linguistica multitasking di massa)
MMLU è un punto di riferimento che testa la conoscenza LLM in 57 materie accademiche incluse
matematica, storia, diritto, medicina e informatica. È composto da
domande a scelta multipla tratte da veri esami di livello universitario. Un punteggio di
Il 70% è più o meno di livello universitario umano; GPT-4 e Claude 3 ottengono un punteggio superiore all'86%.
Phi-3-mini ottiene un punteggio di circa il 70% nonostante le sue piccole dimensioni.

###Valutazioneumana
HumanEval è il punto di riferimento di OpenAI per la generazione di codice. Si compone di 164 Python
problemi di programmazione con casi di test automatizzati. I modelli vengono misurati
pass@k — la probabilità che almeno una delle k soluzioni generate superi tutte
test. GPT-4 ottiene un punteggio di ~87% (pass@1); un modello 7B ben calibrato può raggiungere circa il 50–60%.

### Hella Swag
HellaSwag è un punto di riferimento del ragionamento basato sul buon senso. Ai modelli viene data una frase
descrivere un'attività banale e deve scegliere la continuazione più probabile da cui
quattro opzioni. Le opzioni errate sono appositamente progettate per essere plausibili ma
sottilmente sbagliato. Verifica se un modello ha una conoscenza fondata della fisica
e situazioni sociali.

### ARC (Sfida di ragionamento AI2)
ARC è un punto di riferimento dell'Allen Institute for AI. Si compone di scuola elementare
domande di scienze, suddivise in set "Facile" e "Sfida". Il set della sfida
contiene domande che utilizzano metodi basati sul recupero e semplici modelli statistici
lottare, richiedendo un ragionamento in più fasi.

---

## Concetti fondamentali di IA/ML

### RAG (generazione aumentata di recupero)
RAG è una tecnica che combina un sistema di recupero (tipicamente un file vector
database) con un modello linguistico. Invece di fare affidamento esclusivamente sul modello
conoscenza parametrica, RAG recupera prima i documenti rilevanti da un esterno
base di conoscenza e quindi includerli nel contesto del modello. Ciò consente il
modello per rispondere a domande su informazioni aggiornate o specifiche del dominio
senza riqualificazione. Potato.ai utilizza una forma di RAG: recupera dalla sua KB
e include i risultati nel contesto prima di generare una risposta.

### Perfezionamento
L'ottimizzazione è il processo attraverso il quale si continua ad addestrare un modello preaddestrato su a
set di dati più piccoli e specifici del dominio. Questo adatta i pesi del modello per a
particolare compito o dominio. Ad esempio, un LLM di base potrebbe essere messo a punto
cartelle cliniche per creare un assistente di domande e risposte mediche. La messa a punto è
computazionalmente costoso ma molto più economico della formazione da zero.

### Quantizzazione
La quantizzazione riduce la precisione numerica dei pesi del modello (ad esempio da 32 bit
float in intero a 4 bit). Ciò riduce drasticamente l'ingombro della memoria: un modello 7B
con precisione a 16 bit richiede ~14 GB VRAM; lo stesso modello a 4 bit (formato GGUF)
richiede ~4GB. La quantizzazione in genere provoca una precisione piccola ma accettabile
degrado ed è la tecnica principale che consente ai modelli di grandi dimensioni di funzionare sul consumatore
hardware o anche dispositivi mobili.

### Finestra contestuale
La finestra di contesto è il numero massimo di token che un modello può elaborare contemporaneamente,
includendo sia il prompt che la risposta generata. GPT-3.5 aveva un token 4.096
finestra; GPT-4 Turbo e Claude 3 supportano 128.000 token; Gemelli 1.5 Pro
supporta 1.000.000 di token. Una finestra di contesto più ampia consente al modello di "vedere"
più conversazioni o documenti contemporaneamente, migliorando la coerenza nel lungo periodo
scambi.### RLHF (Apprendimento per rinforzo dal feedback umano)
RLHF è la tecnica formativa che trasforma un modello linguistico di base (che
prevede semplicemente il token successivo) in un assistente che segue le istruzioni e
si comporta in modo utile. I valutatori umani valutano i risultati del modello, viene addestrato un modello di ricompensa
sulle loro preferenze, e il modello linguistico viene quindi ottimizzato rispetto a questo
modello di ricompensa che utilizza l’apprendimento per rinforzo. ChatGPT, Claude e Gemini utilizzano tutti
varianti di RLHF o tecniche di allineamento simili (ad esempio AI costituzionale,
Ottimizzazione delle preferenze dirette).

### Architettura del trasformatore
Il Transformer è l'architettura di rete neurale alla base di tutti i moderni LLM.
Introdotto nel documento del 2017 "L'attenzione è tutto ciò di cui hai bisogno" di Vaswani et al.,
utilizza meccanismi di auto-attenzione per elaborare tutti i token in parallelo anziché
in sequenza. I trasformatori solo encoder (BERT) vengono utilizzati per comprendere le attività;
Per i compiti di generazione vengono utilizzati trasformatori solo decoder (GPT, Llama, Mistral);
I trasformatori encoder-decoder (T5, BART) vengono utilizzati per la traduzione e il riepilogo.

### Incorporamenti e database vettoriali
Gli incorporamenti sono rappresentazioni numeriche dense di testo (o immagini) prodotte da
una rete neurale. Testi semanticamente simili hanno incorporamenti ravvicinati
spazio vettoriale. Archivio di database vettoriali (ChromaDB, Pinecone, Weaviate, Qdrant).
questi incorporamenti e supportano la ricerca rapida e approssimativa del vicino più vicino. Lo sono
la spina dorsale di archiviazione dei sistemi RAG, incluso lo strato di memoria fredda di Potato.ai.