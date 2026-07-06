# Intelligenza artificiale

## Cos'è l'intelligenza artificiale?

L’Intelligenza Artificiale (AI) si riferisce alla simulazione dell’intelligenza umana in macchine programmate per pensare, apprendere e risolvere problemi. I sistemi di intelligenza artificiale possono eseguire compiti che tipicamente richiedono l’intelligenza umana, come riconoscere il parlato, prendere decisioni, tradurre le lingue e identificare oggetti nelle immagini. Il termine fu coniato da John McCarthy nel 1956 alla Conferenza di Dartmouth, ampiamente considerata come l'evento fondatore dell'intelligenza artificiale come campo.

L’intelligenza artificiale moderna è ampiamente divisa in intelligenza artificiale ristretta (chiamata anche intelligenza artificiale debole), progettata per compiti specifici, e intelligenza generale artificiale teorica (AGI), che eguaglierebbe o supererebbe le capacità cognitive umane in tutti i settori. Tutti gli attuali sistemi di IA sono IA ristretta.

## Storia dell'intelligenza artificiale

La storia dell’intelligenza artificiale abbraccia quasi otto decenni. Le prime basi teoriche furono gettate da Alan Turing, il cui articolo del 1950 "Computing Machinery and Intelligence" introdusse il test di Turing, una misura della capacità di una macchina di mostrare un comportamento intelligente indistinguibile da quello di un essere umano. La Conferenza di Dartmouth del 1956 stabilì formalmente l’intelligenza artificiale come disciplina accademica.

Gli anni '50 -'70 videro i primi programmi ottimistici come ELIZA (un semplice chatbot) e LISP (un linguaggio di programmazione progettato per l'intelligenza artificiale). Gli “inverni dell’intelligenza artificiale” degli anni ’70 e ’80 furono periodi di finanziamenti e interessi ridotti a seguito di aspettative non soddisfatte. Una rinascita negli anni ’80 arrivò con i sistemi esperti: programmi basati su regole che codificavano le competenze umane. Gli anni 2000 hanno portato innovazioni nel machine learning alimentate da Internet e da set di dati in crescita. Gli anni 2010 hanno visto l’ascesa del deep learning, trasformando la visione artificiale, l’elaborazione del linguaggio naturale (PNL) e l’apprendimento per rinforzo.

##Apprendimento automatico

Il Machine Learning (ML) è un sottoinsieme dell'intelligenza artificiale che consente ai sistemi di apprendere dai dati senza essere programmati esplicitamente. Le principali categorie di ML includono:

**Apprendimento supervisionato**: il modello viene addestrato su coppie input-output etichettate. Gli esempi includono il rilevamento dello spam e la classificazione delle immagini. Gli algoritmi includono regressione lineare, alberi decisionali, macchine a vettori di supporto e reti neurali.

**Apprendimento non supervisionato**: il modello trova modelli nei dati senza etichetta. Gli esempi includono la segmentazione della clientela e il rilevamento delle anomalie. Gli algoritmi includono il clustering k-means e l'analisi delle componenti principali (PCA).

**Apprendimento per rinforzo**: un agente impara interagendo con un ambiente, ricevendo premi o penalità. Utilizzato nell'intelligenza artificiale di gioco (AlphaGo, AlphaZero), nella robotica e nei sistemi di raccomandazione.

**Apprendimento semi-supervisionato e auto-supervisionato**: combina piccole quantità di dati etichettati con grandi set di dati non etichettati. I modelli GPT utilizzano un approccio auto-supervisionato durante la pre-formazione.

##Apprendimento profondo

Il Deep Learning è un sottoinsieme dell'apprendimento automatico che utilizza reti neurali artificiali con molti livelli (reti profonde). Ispirate vagamente alla struttura neurale del cervello, queste reti apprendono rappresentazioni gerarchiche dei dati. Poteri di apprendimento profondo:

- **Visione artificiale**: riconoscimento di immagini, rilevamento di oggetti, imaging medico
- **Elaborazione del linguaggio naturale**: traduzione automatica, analisi del sentiment, risposta alle domande
- **Riconoscimento vocale**: assistenti vocali come Siri, Alexa, Assistente Google
- **AI generativa**: generazione di immagini (DALL-E, diffusione stabile), generazione di testo (GPT)

Le principali architetture di deep learning includono reti neurali convoluzionali (CNN) per immagini, reti neurali ricorrenti (RNN) e LSTM per sequenze, trasformatori per il linguaggio e reti generative avversarie (GAN) per la sintesi.

## Modelli linguistici di grandi dimensioni (LLM)

I Large Language Models (LLM) sono sistemi di intelligenza artificiale addestrati su grandi quantità di dati di testo per comprendere e generare il linguaggio umano. Si basano sull'architettura Transformer, introdotta nel documento del 2017 "L'attenzione è tutto ciò di cui hai bisogno" di Vaswani et al. Gli LLM prevedono il token successivo (pezzo di parole) in una sequenza, consentendo loro di generare testo coerente, rispondere a domande, scrivere codice ed eseguire attività di ragionamento.

LLM degni di nota includono:
- **Serie GPT** (OpenAI): GPT-3, GPT-4 e successori: ampiamente utilizzati per chat e codice
- **Claude** (Antropico): focalizzato sulla sicurezza e sulla disponibilità
- **Gemini** (Google DeepMind): multimodale, che integra testo, immagini e codice
- **LLaMA / Llama 3** (Meta): modelli a peso aperto per la ricerca e la diffusione locale
- **Mistral** (Mistral AI): modelli aperti efficienti competitivi con LLM molto più grandi

I LLM vengono formati in due fasi: pre-formazione (senza supervisione su corpora di testo di grandi dimensioni) e messa a punto (supervisionata o tramite apprendimento per rinforzo dal feedback umano, RLHF). Le finestre di contesto descrivono la quantità di testo che un LLM può elaborare contemporaneamente, da token 4K (inizio GPT-3) a oltre 1 milione di token nei modelli 2024 più avanzati.

## Etica e sicurezza dell'IAL’intelligenza artificiale solleva importanti questioni etiche tra cui pregiudizi, privacy, spostamento del lavoro e rischio di uso improprio. La distorsione algoritmica si verifica quando i dati di addestramento riflettono disuguaglianze storiche, facendo sì che i sistemi di intelligenza artificiale producano risultati discriminatori. I sistemi di riconoscimento facciale hanno mostrato tassi di errore più elevati per gli individui dalla pelle più scura. È stato scoperto che gli algoritmi di assunzione favoriscono i candidati di sesso maschile.

La sicurezza dell’intelligenza artificiale è il campo dedicato a garantire che i sistemi di intelligenza artificiale si comportino come previsto senza causare danni involontari. Le preoccupazioni principali includono:
- **Allineamento**: garantire che gli obiettivi dell'IA corrispondano ai valori umani
- **Interpretabilità/Spiegabilità**: capire perché un'intelligenza artificiale ha preso una decisione (fondamentale in medicina, diritto, finanza)
- **Uso improprio**: deepfake generati dall'intelligenza artificiale, disinformazione, attacchi informatici
- **Rischio esistenziale**: preoccupazione teorica che una futura AGI possa perseguire obiettivi disallineati con la sopravvivenza umana

Le organizzazioni che lavorano sulla sicurezza dell'intelligenza artificiale includono il team di sicurezza di OpenAI, Anthropic (fondato da ex ricercatori sulla sicurezza di OpenAI), il team di sicurezza di DeepMind e istituti indipendenti come MIRI e ARC.

## L'intelligenza artificiale nella società

L’intelligenza artificiale sta trasformando quasi tutti i settori:

- **Assistenza sanitaria**: l'intelligenza artificiale aiuta nella diagnosi del cancro da immagini mediche, nella previsione degli esiti dei pazienti, nell'accelerazione della scoperta di farmaci (previsione della struttura di ripiegamento delle proteine risolte AlphaFold) e nella personalizzazione dei piani di trattamento.
- **Finanza**: il rilevamento delle frodi, il trading algoritmico, il credit scoring e i robo-advisor utilizzano modelli ML.
- **Trasporti**: i veicoli a guida autonoma utilizzano la visione artificiale, il lidar e l'apprendimento per rinforzo. Tesla Autopilot, Waymo e Cruise stanno guidando gli sforzi.
- **Istruzione**: piattaforme di apprendimento personalizzate adattano i contenuti al ritmo e allo stile di apprendimento dei singoli studenti.
- **Campi creativi**: l'intelligenza artificiale genera musica, arte e scrittura; strumenti come Midjourney, DALL-E e GitHub Copilot hanno cambiato i flussi di lavoro creativi.
- **Cybersecurity**: l'intelligenza artificiale rileva anomalie, identifica minacce e potenzia sia gli attacchi che le difese.

## Robotica e intelligenza artificiale incarnata

La robotica combina l’intelligenza artificiale con le macchine fisiche. I robot moderni utilizzano la percezione (telecamere, lidar), la pianificazione e il controllo per navigare e manipolare gli ambienti. L'Atlante di Boston Dynamics dimostra il movimento bipede avanzato. I robot industriali di aziende come ABB e FANUC automatizzano la produzione. I robot domestici (Roomba) e i robot chirurgici (sistema da Vinci) applicano l’intelligenza artificiale in contesti medici e quotidiani. La ricerca sull’intelligenza artificiale incorporata si concentra su agenti che apprendono abilità fisiche attraverso l’interazione con il mondo, colmando il divario tra ambienti simulati e reali.

## Tendenze attuali dell'IA (anni 2020)

- **AI multimodale**: sistemi che elaborano insieme testo, immagini, audio e video (GPT-4V, Gemini)
- **Agenti e AI agenti**: LLM che possono utilizzare strumenti, navigare sul Web, scrivere codice e intraprendere azioni in più fasi (operatore di OpenAI, utilizzo di computer antropici)
- **Modelli a peso aperto**: LLaMA di Meta ha democratizzato l'accesso a modelli di grandi dimensioni per i ricercatori
- **AI sul dispositivo**: esecuzione di modelli AI localmente su telefoni e laptop senza connettività cloud (Apple Intelligence, Qualcomm NPU)
- **Regolamento sull'IA**: la legge UE sull'IA (2024) è la prima legge completa al mondo sull'IA, che classifica i sistemi di IA in base al livello di rischio