# Intelligenza artificiale

## Cos'è l'intelligenza artificiale?

L’Intelligenza Artificiale (AI) indica l’insieme di tecniche che permettono alle macchine di svolgere compiti normalmente associati all’intelligenza umana, come ragionare, apprendere, prendere decisioni, comprendere il linguaggio e riconoscere schemi. I sistemi di AI possono, per esempio, riconoscere il parlato, tradurre testi, classificare immagini e supportare processi decisionali complessi. Il termine fu coniato da John McCarthy nel 1956 durante la Conferenza di Dartmouth, considerata l’atto di nascita dell’AI come disciplina.

L’AI moderna viene comunemente distinta in intelligenza artificiale ristretta (o debole), progettata per compiti specifici, e intelligenza artificiale generale teorica (AGI), che eguaglierebbe o supererebbe le capacità cognitive umane in ogni ambito. Tutti i sistemi oggi realmente impiegati appartengono alla prima categoria.

## Storia dell'intelligenza artificiale

La storia dell’intelligenza artificiale copre quasi otto decenni. Le sue basi teoriche furono poste da Alan Turing, il cui articolo del 1950 "Computing Machinery and Intelligence" introdusse il test di Turing, un criterio per valutare se una macchina mostri un comportamento intelligente indistinguibile da quello umano. La Conferenza di Dartmouth del 1956 sancì formalmente la nascita del settore.

Tra gli anni ’50 e ’70 emersero i primi programmi pionieristici, come ELIZA, uno dei primi chatbot, e LISP, un linguaggio creato appositamente per la ricerca sull’AI. Gli “inverni dell’intelligenza artificiale” degli anni ’70 e ’80 furono periodi di calo di investimenti e interesse, causati da aspettative troppo ambiziose rispetto ai risultati raggiunti. Negli anni ’80 arrivarono i sistemi esperti, basati su regole. Dagli anni 2000 il machine learning ha accelerato grazie a Internet e alla crescita dei dati disponibili, mentre gli anni 2010 hanno segnato l’esplosione del deep learning in ambiti come visione artificiale, elaborazione del linguaggio naturale e apprendimento per rinforzo.

## Apprendimento automatico

Il Machine Learning (ML) è un sottoinsieme dell’intelligenza artificiale che consente ai sistemi di apprendere dai dati senza essere programmati in modo esplicito. Le principali categorie di ML includono:

**Apprendimento supervisionato**: il modello viene addestrato su coppie input-output etichettate. Tra gli esempi rientrano il filtro antispam e la classificazione di immagini. Gli algoritmi più comuni includono regressione lineare, alberi decisionali, macchine a vettori di supporto e reti neurali.

**Apprendimento non supervisionato**: il modello individua strutture o pattern in dati privi di etichette. Esempi tipici sono la segmentazione dei clienti e il rilevamento delle anomalie. Gli algoritmi comprendono k-means e analisi delle componenti principali (PCA).

**Apprendimento per rinforzo**: un agente impara interagendo con un ambiente e ricevendo ricompense o penalità. È usato nell’AI per i giochi (AlphaGo, AlphaZero), nella robotica e nei sistemi di raccomandazione.

**Apprendimento semi-supervisionato e auto-supervisionato**: combinano piccole quantità di dati etichettati con grandi moli di dati non etichettati. I modelli GPT, per esempio, sfruttano l’auto-supervisione nella fase di pre-addestramento.

## Apprendimento profondo

Il Deep Learning è un ramo del machine learning che utilizza reti neurali artificiali con molti livelli, dette reti profonde. Ispirate in modo molto libero al cervello umano, queste reti apprendono rappresentazioni gerarchiche dei dati. Il deep learning alimenta:

- **Visione artificiale**: riconoscimento di immagini, rilevamento di oggetti, imaging medico
- **Elaborazione del linguaggio naturale**: traduzione automatica, analisi del sentiment, risposta alle domande
- **Riconoscimento vocale**: assistenti vocali come Siri, Alexa e Google Assistant
- **AI generativa**: generazione di immagini (DALL-E, Stable Diffusion) e di testo (GPT)

Tra le principali architetture di deep learning ci sono le reti neurali convoluzionali (CNN) per le immagini, le reti neurali ricorrenti (RNN) e le LSTM per le sequenze, i Transformer per il linguaggio e le GAN per la generazione sintetica di contenuti.

## Modelli linguistici di grandi dimensioni (LLM)

I Large Language Models (LLM) sono sistemi di AI addestrati su enormi quantità di testo per comprendere e generare linguaggio naturale. Si basano sull’architettura Transformer, introdotta nel celebre articolo del 2017 "Attention Is All You Need" di Vaswani e colleghi. Gli LLM prevedono il token successivo in una sequenza e, grazie a questo meccanismo, possono produrre testo coerente, rispondere a domande, scrivere codice e svolgere compiti di ragionamento.

Tra gli LLM più noti troviamo:
- **Serie GPT** (OpenAI): GPT-3, GPT-4 e successori, ampiamente usati per chat e codice
- **Claude** (Anthropic): orientato a sicurezza, affidabilità e lunghe finestre di contesto
- **Gemini** (Google DeepMind): multimodale, integra testo, immagini e codice
- **LLaMA / Llama 3** (Meta): modelli open-weight diffusi nella ricerca e nell’esecuzione locale
- **Mistral** (Mistral AI): modelli aperti molto efficienti rispetto alla loro dimensione

L’addestramento degli LLM avviene tipicamente in due fasi: pre-training su grandi corpora testuali e fine-tuning supervisionato o tramite apprendimento per rinforzo dal feedback umano (RLHF). La finestra di contesto indica quanta informazione il modello riesce a considerare contemporaneamente: si va da poche migliaia di token nei primi modelli fino a oltre un milione nei sistemi più avanzati.

## Etica e sicurezza dell'IA

L’intelligenza artificiale solleva questioni etiche importanti, tra cui bias, privacy, impatto sul lavoro e rischio di abuso. I bias algoritmici emergono quando i dati di addestramento riflettono squilibri o discriminazioni storiche, portando il sistema a produrre risultati ingiusti. Alcuni sistemi di riconoscimento facciale, per esempio, hanno mostrato tassi d’errore più elevati per persone con pelle più scura, mentre alcuni algoritmi di selezione del personale hanno favorito candidati maschili.

La sicurezza dell’AI studia come far sì che i sistemi si comportino come previsto senza causare danni indesiderati. Tra le principali preoccupazioni rientrano:
- **Allineamento**: far sì che gli obiettivi dell’AI siano coerenti con i valori umani
- **Interpretabilità/Spiegabilità**: comprendere perché un modello ha preso una certa decisione, soprattutto in medicina, diritto e finanza
- **Uso improprio**: deepfake, disinformazione, automazione di attacchi informatici
- **Rischio esistenziale**: timore teorico che una futura AGI persegua obiettivi incompatibili con la sopravvivenza umana

Tra le organizzazioni che lavorano sulla sicurezza dell’AI figurano OpenAI, Anthropic, DeepMind e istituti indipendenti come MIRI e ARC.

## L'intelligenza artificiale nella società

L’intelligenza artificiale sta trasformando quasi ogni settore:

- **Sanità**: supporta la diagnosi da immagini mediche, la previsione degli esiti clinici, la scoperta di farmaci e la personalizzazione delle cure
- **Finanza**: viene usata per rilevare frodi, fare trading algoritmico, valutare il credito e costruire robo-advisor
- **Trasporti**: i veicoli autonomi combinano visione artificiale, lidar e apprendimento per rinforzo
- **Istruzione**: le piattaforme adattive personalizzano contenuti e ritmo di apprendimento
- **Settori creativi**: strumenti come Midjourney, DALL-E e GitHub Copilot hanno cambiato musica, grafica e scrittura
- **Cybersecurity**: l’AI aiuta a rilevare anomalie e minacce, ma può anche rafforzare gli attacchi

## Robotica e intelligenza artificiale incarnata

La robotica unisce l’intelligenza artificiale alle macchine fisiche. I robot moderni sfruttano percezione, pianificazione e controllo per muoversi e manipolare l’ambiente circostante. Esempi noti includono Atlas di Boston Dynamics, i robot industriali di ABB e FANUC, i robot domestici come Roomba e i robot chirurgici come il sistema da Vinci. La ricerca sull’AI incarnata punta a creare agenti capaci di apprendere abilità fisiche interagendo direttamente con il mondo reale.

## Tendenze attuali dell'IA (anni 2020)

- **AI multimodale**: sistemi che elaborano insieme testo, immagini, audio e video
- **Agenti AI**: LLM capaci di usare strumenti, navigare sul web, scrivere codice e svolgere azioni in più fasi
- **Modelli open-weight**: famiglie come LLaMA hanno ampliato l’accesso a modelli avanzati per ricerca e uso locale
- **AI on-device**: esecuzione locale di modelli su telefoni e laptop senza dipendere sempre dal cloud
- **Regolamentazione dell’AI**: normative come l’AI Act dell’Unione Europea classificano i sistemi in base al rischio
