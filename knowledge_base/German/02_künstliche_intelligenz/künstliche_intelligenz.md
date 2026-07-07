<!-- 
This file was automatically translated from English to German.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Künstliche Intelligenz

## Was ist Künstliche Intelligenz?

Künstliche Intelligenz (KI) bezeichnet die Simulation menschlicher Intelligenz in Maschinen, die programmiert sind zu denken, zu lernen und Probleme zu lösen. KI-Systeme können Aufgaben ausführen, die typischerweise menschliche Intelligenz erfordern, wie Spracherkennung, Entscheidungsfindung, Übersetzung von Sprachen und Identifizierung von Objekten in Bildern. Der Begriff wurde 1956 von John McCarthy auf der Dartmouth-Konferenz geprägt, die weithin als das Gründungsereignis der KI als wissenschaftliches Feld gilt.

Moderne KI wird grob in Narrow AI (auch Weak AI genannt) unterteilt, die für spezifische Aufgaben entwickelt wurde, und die theoretische Artificial General Intelligence (AGI), die menschliche kognitive Fähigkeiten in allen Bereichen erreichen oder übertreffen würde. Alle aktuellen KI-Systeme sind Narrow AI.

## Geschichte der KI

Die Geschichte der KI umfasst fast acht Jahrzehnte. Frühe theoretische Grundlagen wurden von Alan Turing gelegt, dessen 1950 erschienenes Papier "Computing Machinery and Intelligence" den Turing-Test einführte – ein Maß für die Fähigkeit einer Maschine, intelligentes Verhalten zu zeigen, das von einem Menschen nicht zu unterscheiden ist. Die Dartmouth-Konferenz von 1956 etablierte die KI formell als akademische Disziplin.

Die 1950er bis 1970er Jahre sahen optimistische frühe Programme wie ELIZA (einen einfachen Chatbot) und LISP (eine Programmiersprache, die für KI entwickelt wurde). Die "KI-Winter" der 1970er und 1980er Jahre waren Perioden reduzierter Finanzierung und des Interesses nach unerfüllten Erwartungen. Eine Wiederbelebung in den 1980er Jahren kam mit Expertensystemen – regelbasierten Programmen, die menschliches Fachwissen kodierten. Die 2000er Jahre brachten Durchbrüche im Maschinellen Lernen, angetrieben durch das Internet und wachsende Datensätze. Die 2010er Jahre sahen den Aufstieg des Deep Learning, der Computer Vision, Natural Language Processing (NLP) und Reinforcement Learning transformierte.

## Maschinelles Lernen

Maschinelles Lernen (ML) ist ein Teilbereich der KI, der es Systemen ermöglicht, aus Daten zu lernen, ohne explizit programmiert zu werden. Wichtige ML-Kategorien umfassen:

**Überwachtes Lernen**: Das Modell wird auf beschrifteten Eingabe-Ausgabe-Paaren trainiert. Beispiele umfassen Spam-Erkennung und Bildklassifizierung. Algorithmen umfassen lineare Regression, Entscheidungsbäume, Support Vector Machines und Neuronale Netze.

**Unüberwachtes Lernen**: Das Modell findet Muster in unbeschrifteten Daten. Beispiele umfassen Kundensegmentierung und Anomalieerkennung. Algorithmen umfassen k-Means-Clustering und Hauptkomponentenanalyse (PCA).

**Bestärkendes Lernen**: Ein Agent lernt durch Interaktion mit einer Umgebung und erhält Belohnungen oder Strafen. Wird in spielenden KIs (AlphaGo, AlphaZero), Robotik und Empfehlungssystemen verwendet.

**Semi-überwachtes und selbstüberwachtes Lernen**: Kombinieren kleine Mengen beschrifteter Daten mit großen unbeschrifteten Datensätzen. GPT-Modelle verwenden einen selbstüberwachten Ansatz während des Pre-Trainings.

## Deep Learning

Deep Learning ist ein Teilbereich des Maschinellen Lernens, der künstliche Neuronale Netze mit vielen Schichten (tiefe Netzwerke) verwendet. Lose inspiriert von der neuronalen Struktur des Gehirns, lernen diese Netzwerke hierarchische Darstellungen von Daten. Deep Learning treibt an:

- **Computer Vision**: Bilderkennung, Objekterkennung, medizinische Bildgebung
- **Natural Language Processing**: Maschinelle Übersetzung, Sentiment-Analyse, Fragebeantwortung
- **Spracherkennung**: Sprachassistenten wie Siri, Alexa, Google Assistant
- **Generative KI**: Bilderstellung (DALL-E, Stable Diffusion), Textgenerierung (GPT)

Wichtige Deep-Learning-Architekturen umfassen Convolutional Neural Networks (CNNs) für Bilder, Recurrent Neural Networks (RNNs) und LSTMs für Sequenzen, Transformer für Sprache und Generative Adversarial Networks (GANs) für Synthese.

## Large Language Models (LLMs)

Large Language Models (LLMs) sind KI-Systeme, die auf riesigen Mengen von Textdaten trainiert werden, um menschliche Sprache zu verstehen und zu generieren. Sie basieren auf der Transformer-Architektur, eingeführt im 2017er Papier "Attention Is All You Need" von Vaswani et al. LLMs sagen das nächste Token (Wortteil) in einer Sequenz vorher, was es ihnen ermöglicht, kohärenten Text zu generieren, Fragen zu beantworten, Code zu schreiben und Schlussfolgerungsaufgaben durchzuführen.

Bemerkenswerte LLMs umfassen:
- **GPT-Serie** (OpenAI): GPT-3, GPT-4 und Nachfolger – weit verbreitet für Chat und Code
- **Claude** (Anthropic): Fokussiert auf Sicherheit und Hilfsbereitschaft
- **Gemini** (Google DeepMind): Multimodal, integriert Text, Bilder und Code
- **LLaMA / Llama 3** (Meta): Open-Weight-Modelle für Forschung und lokale Bereitstellung
- **Mistral** (Mistral AI): Effiziente offene Modelle, die mit viel größeren LLMs konkurrieren

LLMs werden in zwei Phasen trainiert: Pre-Training (unüberwacht auf großen Textkorpora) und Fine-Tuning (überwacht oder via Reinforcement Learning from Human Feedback, RLHF). Kontextfenster beschreiben, wie viel Text ein LLM auf einmal verarbeiten kann, von 4K-Token (frühes GPT-3) bis über 1 Million Token in den fortschrittlichsten Modellen von 2024.

## KI-Ethik und Sicherheit

KI wirft wichtige ethische Fragen auf, einschließlich Bias, Privatsphäre, Arbeitsplatzverlagerung und das Risiko des Missbrauchs. Algorithmischer Bias tritt auf, wenn Trainingsdaten historische Ungleichheiten widerspiegeln, wodurch KI-Systeme diskriminierende Ausgaben produzieren. Gesichtserkennungssysteme haben höhere Fehlerraten bei dunkelhäutigen Personen gezeigt. Einstellungsalgorithmen bevorzugen nachweislich männliche Kandidaten.

KI-Sicherheit ist das Feld, das sich der Gewährleistung widmet, dass KI-Systeme wie beabsichtigt verhalten, ohne unbeabsichtigten Schaden zu verursachen. Wichtige Bedenken umfassen:
- **Alignment**: Sicherstellen, dass KI-Ziele mit menschlichen Werten übereinstimmen
- **Interpretierbarkeit / Erklärbarkeit**: Verstehen, warum eine KI eine Entscheidung getroffen hat (kritisch in Medizin, Recht, Finanzen)
- **Missbrauch**: KI-generierte Deepfakes, Desinformation, Cyberangriffe
- **Existenzielles Risiko**: Theoretische Sorge, dass eine zukünftige AGI Ziele verfolgen könnte, die mit dem menschlichen Überleben nicht vereinbar sind

Organisationen, die an KI-Sicherheit arbeiten, umfassen OpenAIs Safety-Team, Anthropic (gegründet von ehemaligen OpenAI-Sicherheitsforschern), DeepMinds Safety-Team und unabhängige Institute wie MIRI und ARC.

## KI in der Gesellschaft

KI transformiert nahezu jede Branche:

- **Gesundheitswesen**: KI unterstützt bei der Diagnose von Krebs aus medizinischen Bildern, der Vorhersage von Patientenergebnissen, der Beschleunigung der Arzneimittelentdeckung (AlphaFold löste die Vorhersage der Proteinfaltungsstruktur) und der Personalisierung von Behandlungsplänen.
- **Finanzen**: Betrugserkennung, algorithmischer Handel, Kredit-Scoring und Robo-Advisors verwenden ML-Modelle.
- **Transport**: Selbstfahrende Fahrzeuge verwenden Computer Vision, Lidar und bestärkendes Lernen. Tesla Autopilot, Waymo und Cruise sind führende Bemühungen.
- **Bildung**: Personalisierte Lernplattformen passen Inhalte an das individuelle Lerntempo und den Lernstil der Schüler an.
- **Kreative Bereiche**: KI generiert Musik, Kunst und Schreiben; Tools wie Midjourney, DALL-E und GitHub Copilot haben kreative Workflows verändert.
- **Cybersicherheit**: KI erkennt Anomalien, identifiziert Bedrohungen und treibt sowohl Angriffe als auch Verteidigungen an.

## Robotik und Embodied AI

Robotik kombiniert KI mit physischen Maschinen. Moderne Roboter verwenden Wahrnehmung (Kameras, Lidar), Planung und Steuerung, um sich in Umgebungen zu bewegen und diese zu manipulieren. Boston Dynamics' Atlas demonstriert fortgeschrittene zweibeinige Bewegung. Industrieroboter von Unternehmen wie ABB und FANUC automatisieren die Fertigung. Haushaltsroboter (Roomba) und chirurgische Roboter (da Vinci-System) wenden KI in alltäglichen und medizinischen settings an. Embodied-AI-Forschung konzentriert sich auf Agenten, die physische Fähigkeiten durch Interaktion mit der Welt lernen und überbrücken die Lücke zwischen simulierten und realen Umgebungen.

## Aktuelle KI-Trends (2020er)

- **Multimodale KI**: Systeme, die Text, Bilder, Audio und Video zusammen verarbeiten (GPT-4V, Gemini)
- **Agenten und agentische KI**: LLMs, die Tools verwenden, im Web surfen, Code schreiben und mehrstufige Aktionen ausführen können (OpenAIs Operator, Anthropic Computer Use)
- **Open-Weight-Modelle**: Metas LLaMA demokratisierte den Zugang zu großen Modellen für Forscher
- **On-Device-KI**: Ausführen von KI-Modellen lokal auf Telefonen und Laptops ohne Cloud-Konnektivität (Apple Intelligence, Qualcomm NPUs)
- **KI-Regulierung**: Der EU AI Act (2024) ist das weltweit erste umfassende KI-Gesetz, das KI-Systeme nach Risikostufen klassifiziert
