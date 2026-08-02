# Glossario tecnologico

Un glossario di riferimento che copre modelli di intelligenza artificiale, hardware, benchmark e concetti fondamentali del moderno panorama AI e informatico.

---

## Modelli linguistici e assistenti AI

### ChatGPT
ChatGPT è un assistente AI sviluppato da OpenAI e rilasciato per la prima volta nel novembre 2022. Si basa sulla famiglia GPT di Large Language Models (LLM). È stato uno dei prodotti AI consumer con la crescita più rapida di sempre, raggiungendo 100 milioni di utenti in pochi mesi. Supporta conversazioni testuali, scrittura, riepilogo e generazione di codice. I piani a pagamento danno accesso a modelli più potenti come GPT-4 e GPT-4o.

### GPT (Generative Pre-trained Transformer)
GPT è una famiglia di modelli linguistici creata da OpenAI. L’architettura utilizza Transformer decoder-only addestrati con l’obiettivo di prevedere il token successivo su enormi corpora di testo. Tra le versioni principali figurano GPT-2 (2019, 1,5 miliardi di parametri), GPT-3 (2020, 175 miliardi di parametri), GPT-3.5 e GPT-4 (2023, multimodale e con prestazioni di alto livello su molti benchmark).

### Claude
Claude è un assistente AI sviluppato da Anthropic. Il nome richiama Claude Shannon, pioniere della teoria dell’informazione. Anthropic è stata fondata da ex ricercatori di OpenAI con un forte focus sulla sicurezza e sull’"AI costituzionale", un approccio che mira a rendere i modelli più affidabili facendoli aderire a un insieme di principi. Le famiglie Claude 1, 2 e 3 (Haiku, Sonnet, Opus) sono note per la qualità del ragionamento e per le finestre di contesto molto ampie.

### Gemini
Gemini è la famiglia di modelli multimodali di Google DeepMind, annunciata nel dicembre 2023. È stata progettata per trattare insieme testo, immagini, audio e video. Le versioni comprendono Gemini Nano, pensato per l’esecuzione on-device, Gemini Flash, ottimizzato per velocità e costo, e Gemini Ultra, focalizzato sulla massima capacità. Gemini alimenta anche varie funzioni AI dell’ecosistema Google.

### Phi-3-mini
Phi-3-mini è uno Small Language Model (SLM) sviluppato da Microsoft con 3,8 miliardi di parametri. È stato rilasciato nell’aprile 2026. Invece di puntare solo alla quantità di dati, è stato addestrato su un dataset accuratamente curato, spesso descritto come di qualità "textbook". Nonostante le dimensioni contenute, ottiene risultati competitivi su benchmark di ragionamento e può essere eseguito anche su hardware consumer o dispositivi mobili sufficientemente potenti.

### Llama (Meta AI)
Llama (Large Language Model Meta AI) è una famiglia di modelli open-weight rilasciata da Meta. Llama 2, pubblicato nel 2023, è stato distribuito per ricerca e uso commerciale in varie dimensioni. Llama 3 ha ulteriormente migliorato le prestazioni e ha consolidato l’ecosistema di modelli eseguibili in locale. Grazie alla disponibilità pubblica dei pesi, Llama ha favorito un vasto panorama di varianti e adattamenti.

### Mistral
Mistral AI è un’azienda francese che sviluppa LLM aperti e proprietari. Mistral 7B ha mostrato come modelli relativamente piccoli possano ottenere risultati molto forti grazie a tecniche architetturali efficienti. Mixtral 8x7B, per esempio, utilizza un’architettura mixture-of-experts, attivando solo parte della rete per ciascun token. I modelli Mistral sono molto usati in scenari self-hosted e open.

---

## Hardware GPU e schede grafiche

### GPU (Graphics Processing Unit)
Una GPU è un processore progettato per eseguire calcoli altamente paralleli. Nata per il rendering grafico 3D, oggi è fondamentale per training e inferenza AI perché può svolgere moltissime operazioni in parallelo. I principali produttori di GPU rilevanti per l’AI sono NVIDIA e AMD.

### Serie NVIDIA GeForce RTX
La serie RTX è la linea consumer di NVIDIA. Le generazioni RTX 30xx (Ampere) e RTX 40xx (Ada Lovelace) includono Tensor Core dedicati che accelerano carichi AI. La quantità di VRAM è determinante per l’esecuzione locale dei modelli: una GPU da 8 GB può gestire modelli da circa 7B quantizzati a 4 bit, mentre 24 GB permettono di spingersi molto più in alto.

### NVIDIA Serie A e Serie H (data center)
A100 e H100 sono acceleratori professionali di NVIDIA per data center. La H100, basata su Hopper, può avere fino a 80 GB di memoria HBM3 ed è uno degli standard di riferimento per l’addestramento di grandi modelli. Queste GPU costano molto più delle schede consumer, ma offrono throughput AI enormemente superiore.

### Serie AMD Radeon RX
La linea Radeon RX rappresenta l’offerta consumer di AMD. Modelli come la RX 7900 XTX, dotati di molta VRAM, possono eseguire LLM locali tramite ROCm, lo stack di calcolo GPU di AMD. In ambito AI il supporto software è in genere meno maturo rispetto a NVIDIA, ma sta migliorando progressivamente.

### Intel Arc
Intel Arc è la linea di GPU discrete di Intel, introdotta a partire dal 2022. Supporta tecnologie come XeSS e offre un supporto ancora limitato ma in crescita per l’inferenza AI tramite strumenti come OpenVINO e IPEX-LLM.

### Intel ARK (ark.intel.com)
Intel ARK è il database ufficiale delle specifiche hardware di Intel. Raccoglie dati tecnici dettagliati su CPU, GPU, FPGA e altri prodotti, come numero di core, frequenze, TDP, tipi di memoria supportati e set di istruzioni. Quando si parla di "controllare ARK", ci si riferisce a quella fonte autorevole.

---

## Benchmark delle prestazioni dell'AI

### MMLU (Massive Multitask Language Understanding)
MMLU è un benchmark che valuta la conoscenza degli LLM in 57 materie accademiche, tra cui matematica, storia, medicina, diritto e informatica. Le domande sono a scelta multipla e derivano da esami reali. Un punteggio intorno al 70% è spesso considerato vicino al livello umano universitario.

### HumanEval
HumanEval è il benchmark di OpenAI per la generazione di codice. Comprende 164 problemi di programmazione in Python con test automatici. Le prestazioni vengono spesso misurate con la metrica pass@k, cioè la probabilità che almeno una delle k soluzioni generate superi tutti i test.

### HellaSwag
HellaSwag è un benchmark di ragionamento basato sul buon senso. Il modello deve scegliere la continuazione più plausibile di una situazione quotidiana tra più opzioni progettate per sembrare credibili ma contenere errori sottili. Serve a misurare la capacità del modello di comprendere il mondo reale e il contesto implicito.

### ARC (AI2 Reasoning Challenge)
ARC è un benchmark dell’Allen Institute for AI basato su domande di scienze di livello scolastico. Comprende una sezione più semplice e una più impegnativa. La sezione più difficile richiede ragionamento in più passaggi e mette in crisi approcci semplici basati sul recupero di fatti.

---

## Concetti fondamentali di AI/ML

### RAG (Retrieval-Augmented Generation)
RAG è una tecnica che combina un sistema di recupero delle informazioni, spesso basato su un database vettoriale, con un modello linguistico. Invece di affidarsi solo alla conoscenza appresa nei pesi del modello, il sistema recupera documenti rilevanti da una base di conoscenza esterna e li inserisce nel contesto della risposta. Questo approccio è utile per gestire informazioni aggiornate o altamente specialistiche.

### Fine-tuning
Il fine-tuning è il processo con cui un modello pre-addestrato viene ulteriormente addestrato su un dataset più piccolo e specifico di un dominio o di un compito. In questo modo il modello adatta il proprio comportamento a casi d’uso particolari, come la medicina, il supporto clienti o il diritto. È molto meno costoso dell’addestramento da zero, ma richiede comunque risorse e dati di qualità.

### Quantizzazione
La quantizzazione riduce la precisione numerica dei pesi del modello, per esempio passando da float a 16 bit a rappresentazioni a 4 o 8 bit. Questo abbassa molto il consumo di memoria e rende possibile eseguire modelli grandi su GPU consumer o persino su dispositivi mobili. In genere comporta una perdita di precisione contenuta e spesso accettabile.

### Finestra di contesto
La finestra di contesto è il numero massimo di token che un modello può elaborare in una singola interazione, considerando sia il prompt sia l’output generato. Finestre più ampie permettono di gestire documenti lunghi, conversazioni estese e compiti che richiedono molta memoria locale di lavoro.

### RLHF (Reinforcement Learning from Human Feedback)
RLHF è una tecnica di addestramento che aiuta a trasformare un modello base in un assistente più utile e allineato alle aspettative umane. I valutatori confrontano risposte diverse, si addestra un modello di ricompensa sulle loro preferenze e poi il modello linguistico viene ottimizzato rispetto a quel segnale. ChatGPT, Claude e Gemini impiegano varianti di questo approccio o tecniche affini.

### Architettura Transformer
Il Transformer è l’architettura neurale alla base della maggior parte degli LLM moderni. Introdotto nel 2017, usa meccanismi di self-attention per elaborare i token in parallelo, invece che in sequenza. Esistono varianti encoder-only, decoder-only ed encoder-decoder, impiegate rispettivamente per comprensione, generazione o attività miste.

### Embedding e database vettoriali
Gli embedding sono rappresentazioni numeriche dense di testo, immagini o altri dati prodotte da una rete neurale. Elementi semanticamente simili tendono a essere vicini nello spazio vettoriale. I database vettoriali, come Pinecone, Weaviate, Qdrant o ChromaDB, archiviano questi vettori e permettono ricerche semantiche rapide, costituendo un componente chiave di molti sistemi RAG.
