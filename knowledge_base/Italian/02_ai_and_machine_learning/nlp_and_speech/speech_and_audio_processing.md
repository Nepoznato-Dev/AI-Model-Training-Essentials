---
# Metadata
title: "Speech and Audio Processing"
description: "ASR, TTS, audio features, Whisper, speech pipelines"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [speech, audio, processing, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Elaborazione vocale e audio
L'elaborazione vocale e audio copre le tecnologie che consentono alle macchine di ascoltare, comprendere, generare e manipolare il suono. Ciò include il riconoscimento vocale (trasformare le parole pronunciate in testo), la sintesi vocale (trasformare il testo in parole pronunciate), l'identificazione del parlante, la generazione di musica e la comprensione del suono ambientale. Il campo è stato trasformato dal deep learning: i sistemi moderni si avvicinano alla precisione del livello umano per il riconoscimento vocale e producono voci sintetiche stranamente naturali.
---

## Fondamenti di audio digitale
Il suono è un'onda di pressione. Per elaborarlo digitalmente, campioniamo l'onda a intervalli regolari.
| Concetto | Descrizione | Valore tipico |
|---------|-----|------|
| **Tasso di campionamento** | Quante volte al secondo viene misurato il suono | 8 kHz (telefono), 16 kHz (parlato), 44,1 kHz (CD), 48 kHz (professionale) |
| **Profondità di bit** | Precisione di ciascun campione | 16 bit (CD), 24 bit (professionale), 32 bit float (elaborazione) |
| **Canali** | Mono (1), stereo (2), surround (5.1, 7.1) | Stereo per la musica; mono per parlato |
| **Durata** | Durata dell'audio | Varia |
Una registrazione mono di 1 minuto a 16 kHz, 16 bit = 1,92 MB. Un brano stereo di 3 minuti a 44,1 kHz, 16 bit = 30,3 MB.
---

## Estrazione di funzionalità audio
È difficile per i modelli lavorare direttamente con le forme d'onda audio grezze. Estraiamo caratteristiche che catturano le caratteristiche importanti del suono.
| Caratteristica | Cosa cattura | Caso d'uso |
|---------|-----------|----------|
| **Spettrogramma di Mel** | Contenuto della frequenza nel tempo, mappato sulla percezione dell'udito umano | Riconoscimento vocale, classificazione musicale |
| **MFCC** (coefficienti cepstral della frequenza Mel) | Rappresentazione compatta dell'inviluppo spettrale | Riconoscimento vocale tradizionale |
| **Cromagramma** | Distribuzione delle classi di altezza (quali note vengono suonate) | Analisi musicale, rilevamento accordi |
| **Tasso di passaggio allo zero** | La frequenza con cui il segnale attraversa lo zero | Rilevamento sonoro e non sonoro |
| **Energia RMS** | Intensità del segnale nel tempo | Rilevamento dell'attività vocale |
| **Intonazione (F0)** | Frequenza fondamentale | Identificazione del relatore, trascrizione musicale |
### Spettrogramma di Mel
La rappresentazione audio più comune per il deep learning. Converte l'audio in un formato simile a un'immagine 2D:
| Asse | Rappresenta |
|------|-----------|
| **Asse X** | Tempo |
| **Asse Y** | Frequenza (sulla scala Mel — percettivamente spaziata) |
| **Colore/intensità** | Energia a quella frequenza e a quel tempo |
La scala Mel si avvicina all'udito umano: siamo più bravi a distinguere le frequenze basse da quelle alte.
---

## Riconoscimento vocale automatico (ASR)
ASR converte la lingua parlata in testo. È una delle applicazioni commercialmente più importanti dell'intelligenza artificiale audio.
### Evoluzione dell'ASR
| Epoca | Avvicinamento | Limitazione |
|-----|----------|------------|
| **Pre-2010** | Modelli Markov nascosti + modelli di miscela gaussiana | Richiesta un'ampia attività di ingegneria manuale; povero in condizioni rumorose |
| **2010-2015** | Ibrido DNN-HMM | Le reti neurali hanno sostituito i MGM; miglioramento significativo |
| **2015-2020** | Modelli end-to-end (Deep Speech, LAS) | Rete neurale singola dall'audio al testo |
| **2020+** | Basato su trasformatore (Whisper, Conformer) | Precisione all'avanguardia; multilingue; robusto |
### Principali modelli ASR
| Modello | Architettura | Dati di allenamento | Caratteristica notevole |
|-------|-------------|--------------|-----------------|
| **Sussurro** (OpenAI) | Trasformatore encoder-decodificatore | 680.000 ore, 99 lingue | Multilingue; robusto agli accenti e al rumore; open source |
| **Conforme** | Convoluzione + autoattenzione | Vari | Combina funzionalità locali (conv) e globali (attenzione) |
| **wav2vec 2.0** | Trasformatore autocontrollato | Discorso senza etichetta | Impara dall'audio grezzo senza trascrizioni |
| **USM** (Google) | Modello vocale universale | 2 milioni di ore, oltre 300 lingue | La maggior parte delle lingue coperte |
| **MMS** (Meta) | Discorso massivamente multilingue | Oltre 1.400 lingue | Estende la copertura alle lingue con risorse limitate |
### Metriche ASR
| Metrico | Descrizione |
|--------|-------------|
| **WER** (Tasso di errore delle parole) | Percentuale di parole trascritte in modo errato. Più basso è meglio. La prestazione umana è del 4-5% circa per l’inglese pulito. |
| **CER** (tasso di errore dei caratteri) | Come il WER ma a livello di personaggio. Utilizzato per le lingue senza confini di parole (cinese, giapponese). |
### Sfide ASR comuni
| Sfida | Descrizione |
|-----------|-------------|
| **Accenti e dialetti** | Le prestazioni diminuiscono significativamente per gli accenti non standard |
| **Rumore di fondo** | Musica, traffico e altri altoparlanti riducono la precisione |
| **Commutazione di codice** | I relatori passano da una lingua all'altra a metà frase |
| **Omofoni** | "Lì" vs "loro" vs "loro sono" - richiede contesto |
| **Punteggiatura e formattazione** | L'output ASR è generalmente senza punteggiatura; necessita di post-elaborazione |
| **Lingue con poche risorse** | La maggior parte dei modelli ha prestazioni scarse per le lingue con pochi dati di addestramento |
---

## Sintesi vocale (TTS)
TTS converte il testo scritto in audio parlato. I sistemi moderni producono un parlato che spesso è indistinguibile dalle registrazioni umane.
### Evoluzione del TTS
| Epoca | Avvicinamento | Qualità |
|-----|----------|---------|
| **Pre-2010** | Concatenativo (cucitura di frammenti registrati) | robotica; espressività limitata |
| **2010-2017** | Parametrico statistico (HMM, neurale precoce) | Migliore ma comunque riconoscibile come sintetico |
| **2017-2020** | Neurale (Tacotron, WaveNet) | Qualità quasi umana; espressivo |
| **2020+** | Codec neurale (VALL-E, Bark) | Clonazione vocale; pochi colpi; altamente naturale |
### Modelli TTS chiave
| Modello | Architettura | Caratteristica notevole |
|-------|-------------|-----------------|
| **WaveNet** (DeepMind) | Modello generativo autoregressivo | Il primo TTS dal suono veramente naturale |
| **Tacotron 2** (Google) | Seq2seq + vocoder | Dall'inizio alla fine; alta qualità |
| **VITS** | Inferenza variazionale + addestramento contraddittorio | Veloce; buona qualità; ampiamente usato |
| **VALL-E** (Microsoft) | Modello linguistico codec neurale | Clonazione vocale da un campione di 3 secondi |
| **Corteccia** (Suno) | Basato su trasformatore | Multilingue; suoni non vocali (risate, musica) |
| **UndiciLabs** | Commerciale | Clonazione vocale leader del settore |
| **ChatTTS** | Open source | Ottimizzato per il parlato |
| **Discorso dei pesci** | Open source | Veloce; multilingue |
### Clonazione vocale
La clonazione della voce crea una voce sintetica che suona come una persona specifica da un breve campione audio.
| Metodo | Dati necessari | Qualità |
|--------|------------|---------|
| **Regolazione** | 10-60 minuti di discorso | Alta qualità; specifico dell'oratore |
| **Pochi colpi** | 3-30 secondi di discorso | Buona qualità; configurazione rapida |
| **Scatto zero** | Nessun dato sul relatore di destinazione | Utilizza l'audio di riferimento al momento dell'inferenza |
**Preoccupazione etica**: la clonazione vocale può essere utilizzata per furto d'identità, frode e deepfake. La maggior parte dei fornitori commerciali richiede il consenso vocale.
---

## Riconoscimento del relatore
| Compito | Descrizione | Applicazione |
|------|-------------|-----|
| **Verifica del relatore** | "Questa persona è chi dicono di essere?" | Banking telefonico, sblocco del dispositivo |
| **Identificazione del parlante** | "Chi sta parlando?" | Trascrizione della riunione, medicina legale |
| **Diarizzazione dell'oratore** | "Chi ha parlato quando?" (in audio con più altoparlanti) | Riepiloghi delle riunioni, generazione dei sottotitoli |
| Modello | Avvicinamento |
|-------|----------|
| **ECAPA-TDNN** | Basato sull'incorporamento; stato dell'arte per la verifica |
| **d-vettore** | Semplici incorporamenti di altoparlanti da DNN |
| **x-vettore** | Incorporamenti degli altoparlanti migliorati; ampiamente usato |
---

## Recupero di informazioni musicali
| Compito | Descrizione | Strumenti/Modelli |
|------|-------------|-----|
| **Trascrizione musicale** | Converti audio in spartiti / MIDI | Spotify Base Pitch, Spleeter |
| **Separazione della fonte** | Isolare singoli strumenti o voci | Demucs, Spleeter, Separazione delle fonti musicali |
| **Classificazione del genere** | Classificare la musica per genere | CNN sugli spettrogrammi |
| **Tracciamento del battito** | Rileva il tempo e le posizioni delle battute | Librosa, Madmom |
| **Riconoscimento accordi** | Identificare gli accordi nella musica | Accordi-CNN, modelli CRF |
| **Generazione musicale** | Crea nuova musica | MusicGen, MuseNet, AIVA |
---

## Rilevamento del suono ambientale
| Compito | Descrizione | Applicazione |
|------|-------------|-----|
| **Rilevamento eventi sonori** | Identificare i suoni in un ambiente | Casa intelligente (rottura di vetri, pianto del bambino) |
| **Classificazione della scena acustica** | Classificare l'ambiente (ufficio, parco, traffico) | Dispositivi sensibili al contesto |
| **Rilevamento anomalie** | Rileva suoni insoliti | Monitoraggio industriale (macchinaæ•…éšœ) |
| Insieme di dati | Suoni | Taglia |
|---------|--------|------|
| **Set audio** | 632 classi sonore | Oltre 2 milioni di clip YouTube |
| **ESC-50** | 50 classi di suono ambientale | 2.000 clip |
| **UrbanSound8K** | Suoni urbani | 8.732 clip |
---

## Strumenti e framework
| Strumento | Scopo |
|------|---------|
| **Librosa** | Libreria Python per l'analisi audio (funzionalità, effetti, visualizzazione) |
| **Pydub** | Manipolazione audio semplice (taglia, concatena, esporta) |
| **FFmpeg** | Elaborazione audio/video da riga di comando (il coltellino svizzero) |
| **Audio della torcia** | Elaborazione audio PyTorch (trasformazioni, set di dati, modelli) |
| **Faccia che abbraccia (trasformatori)** | Modelli ASR e TTS pre-addestrati |
| **Sussurro (OpenAI)** | Riconoscimento vocale (open source) |
| **Coqui TTS** | Kit di strumenti TTS open source |
| **Demuc** | Separazione della sorgente musicale |
| **SpeechBrain** | Kit di strumenti vocali tutto in uno (ASR, TTS, riconoscimento dell'oratore) |
---

## Consigli pratici
- **Ascolta sempre i tuoi dati.** Prima di addestrare qualsiasi cosa, ascolta l'audio di esempio. Prendere nota della frequenza di campionamento, del livello di rumore e delle caratteristiche degli altoparlanti.
- **Frequenze di campionamento corrispondenti.** Whisper prevede 16 kHz. Se l'audio è a 44,1 kHz, ricampionalo, ma tieni presente che il downsampling perde informazioni.
- **Aumenta i dati audio.** Aggiungi rumore di fondo, varia velocità e tono, simula diversi microfoni. Ciò migliora notevolmente la robustezza.
- **Utilizzare modelli pre-addestrati.** Whisper per ASR e VITS/Bark per TTS sono ottimi punti di partenza. La messa a punto è quasi sempre migliore che allenarsi da zero.
- **Gestisci il silenzio.** Il rilevamento dell'attività vocale (VAD) rimuove il silenzio prima dell'elaborazione, risparmiando calcoli e migliorando la precisione. Silero VAD e WebRTC VAD sono scelte popolari.
- **Normalizza il volume.** Registrazioni diverse hanno livelli di volume molto diversi. Normalizzare a un livello coerente prima dell'elaborazione.
---

## Riepilogo
L’elaborazione vocale e audio è stata rivoluzionata dal deep learning. I moderni sistemi ASR come Whisper si avvicinano alla precisione a livello umano in dozzine di lingue. I sistemi TTS producono un parlato sempre più indistinguibile dalle registrazioni umane. La clonazione vocale funziona da pochi secondi di audio. La generazione di musica, la separazione delle sorgenti e il rilevamento dei suoni ambientali stanno tutti avanzando rapidamente. Il campo deve affrontare sfide continue – lingue con scarse risorse, ambienti rumorosi, preoccupazioni etiche sulla clonazione della voce – ma la traiettoria è chiara: le macchine stanno diventando brave quanto gli esseri umani nell’udire, comprendere e produrre suoni.