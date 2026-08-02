<!-- 
This file was automatically translated from English to German.
Source: artificial_intelligence.md
Note: Technical terms, code examples, and proper nouns may remain in English.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Künstliche Intelligenz

## Was ist Künstliche Intelligenz?

Künstliche Intelligenz (KI) bezeichnet die Nachbildung menschlicher Intelligenz in Maschinen, die darauf ausgelegt sind zu denken, zu lernen und Probleme zu lösen. KI-Systeme können Aufgaben ausführen, die normalerweise menschliche Intelligenz erfordern, etwa Spracherkennung, Entscheidungsfindung, Sprachübersetzung und die Identifikation von Objekten in Bildern. Der Begriff wurde 1956 von John McCarthy auf der Dartmouth-Konferenz geprägt, die weithin als Gründungsereignis der KI als wissenschaftliche Disziplin gilt.

Moderne KI wird grob in Narrow AI (auch Weak AI, also auf bestimmte Aufgaben spezialisierte KI) und die theoretische Artificial General Intelligence (AGI) unterteilt, die menschliche kognitive Fähigkeiten in allen Bereichen erreichen oder übertreffen würde. Alle heutigen KI-Systeme sind Formen von Narrow AI.

## Geschichte der KI

Die Geschichte der KI umfasst fast acht Jahrzehnte. Frühere theoretische Grundlagen wurden von Alan Turing gelegt, dessen 1950 erschienener Aufsatz "Computing Machinery and Intelligence" den Turing-Test einführte – ein Maß dafür, ob das Verhalten einer Maschine von dem eines Menschen nicht zu unterscheiden ist. Die Dartmouth-Konferenz von 1956 etablierte KI anschließend formell als akademische Disziplin.

Die 1950er- bis 1970er-Jahre brachten frühe, optimistisch betrachtete Programme wie ELIZA (einen einfachen Chatbot) und LISP (eine für KI entwickelte Programmiersprache) hervor. Die „KI-Winter" der 1970er- und 1980er-Jahre waren Phasen sinkender Finanzierung und nachlassenden Interesses infolge unerfüllter Erwartungen. In den 1980er-Jahren kam es durch Expertensysteme – regelbasierte Programme, die menschliches Fachwissen kodierten – zu einer Wiederbelebung. Die 2000er-Jahre brachten Durchbrüche im Maschinellen Lernen, angetrieben durch das Internet und wachsende Datensätze. In den 2010er-Jahren setzte sich Deep Learning durch und veränderte Computer Vision, Natural Language Processing (NLP) und Reinforcement Learning grundlegend.

## Maschinelles Lernen

Maschinelles Lernen (ML) ist ein Teilgebiet der KI, das Systemen ermöglicht, aus Daten zu lernen, ohne explizit programmiert zu werden. Wichtige ML-Kategorien sind:

**Überwachtes Lernen**: Das Modell wird auf beschrifteten Eingabe-Ausgabe-Paaren trainiert. Beispiele sind Spam-Erkennung und Bildklassifizierung. Typische Algorithmen sind lineare Regression, Entscheidungsbäume, Support Vector Machines und neuronale Netze.

**Unüberwachtes Lernen**: Das Modell erkennt Muster in unbeschrifteten Daten. Beispiele sind Kundensegmentierung und Anomalieerkennung. Häufig verwendete Verfahren sind k-Means-Clustering und Hauptkomponentenanalyse (PCA).

**Bestärkendes Lernen**: Ein Agent lernt durch die Interaktion mit einer Umgebung und erhält Belohnungen oder Strafen. Dieses Verfahren wird in spielenden KIs (AlphaGo, AlphaZero), in der Robotik und in Empfehlungssystemen eingesetzt.

**Semi-überwachtes und selbstüberwachtes Lernen**: Diese Ansätze kombinieren kleine Mengen beschrifteter Daten mit großen unbeschrifteten Datensätzen. GPT-Modelle verwenden während des Pre-Trainings einen selbstüberwachten Ansatz.

## Tiefes Lernen (Deep Learning)

Tiefes Lernen (Deep Learning) ist ein Teilbereich des Maschinellen Lernens, der künstliche neuronale Netze mit vielen Schichten verwendet. Lose von der Struktur des Gehirns inspiriert, lernen diese Netze hierarchische Darstellungen von Daten. Tiefes Lernen treibt unter anderem folgende Bereiche an:

- **Computer Vision**: Bilderkennung, Objekterkennung, medizinische Bildgebung
- **Natural Language Processing**: Maschinelle Übersetzung, Sentiment-Analyse, Fragebeantwortung
- **Spracherkennung**: Sprachassistenten wie Siri, Alexa und Google Assistant
- **Generative KI**: Bilderzeugung (DALL-E, Stable Diffusion), Textgenerierung (GPT)

Wichtige Deep-Learning-Architekturen sind Convolutional Neural Networks (CNNs) für Bilder, Recurrent Neural Networks (RNNs) und LSTMs für Sequenzen, Transformer für Sprache sowie Generative Adversarial Networks (GANs) für die Synthese.

## Große Sprachmodelle (LLMs)

Große Sprachmodelle (LLMs) sind KI-Systeme, die auf riesigen Textmengen trainiert werden, um menschliche Sprache zu verstehen und zu erzeugen. Sie basieren auf der Transformer-Architektur, die im 2017 erschienenen Paper "Attention Is All You Need" von Vaswani et al. vorgestellt wurde. LLMs sagen das nächste Token (Wortteil) in einer Sequenz vorher und können dadurch zusammenhängende Texte generieren, Fragen beantworten, Code schreiben und Aufgaben lösen, die Schlussfolgern erfordern.

Bemerkenswerte LLMs sind:
- **GPT-Serie** (OpenAI): GPT-3, GPT-4 und Nachfolger – weit verbreitet für Chat und Code
- **Claude** (Anthropic): Fokussiert auf Sicherheit und Hilfsbereitschaft
- **Gemini** (Google DeepMind): Multimodal, integriert Text, Bilder und Code
- **LLaMA / Llama 3** (Meta): Open-Weight-Modelle für Forschung und lokale Bereitstellung
- **Mistral** (Mistral AI): Effiziente offene Modelle, die mit deutlich größeren LLMs konkurrieren

LLMs werden in zwei Phasen trainiert: Pre-Training (unüberwacht auf großen Textkorpora) und Fine-Tuning (überwacht oder mithilfe von Reinforcement Learning from Human Feedback, RLHF). Kontextfenster beschreiben, wie viel Text ein LLM auf einmal verarbeiten kann – von 4K-Token bei frühem GPT-3 bis zu mehr als 1 Million Token in den fortschrittlichsten Modellen des Jahres 2026.

## KI-Ethik und Sicherheit

KI wirft wichtige ethische Fragen auf, darunter Bias, Privatsphäre, Arbeitsplatzverlagerung und das Risiko des Missbrauchs. Algorithmischer Bias tritt auf, wenn Trainingsdaten historische Ungleichheiten widerspiegeln und KI-Systeme dadurch diskriminierende Ausgaben erzeugen. Gesichtserkennungssysteme zeigten beispielsweise höhere Fehlerraten bei dunkelhäutigen Personen. Einstellungsalgorithmen bevorzugten nachweislich männliche Kandidaten.

KI-Sicherheit befasst sich damit, sicherzustellen, dass KI-Systeme sich wie beabsichtigt verhalten, ohne unbeabsichtigten Schaden anzurichten. Wichtige Themen sind:
- **Ausrichtung (Alignment)**: Sicherstellen, dass KI-Ziele mit menschlichen Werten übereinstimmen
- **Interpretierbarkeit / Erklärbarkeit**: Verstehen, warum eine KI eine bestimmte Entscheidung getroffen hat (kritisch in Medizin, Recht und Finanzen)
- **Missbrauch**: KI-generierte Deepfakes, Desinformation, Cyberangriffe
- **Existenzielles Risiko**: Theoretische Sorge, dass eine zukünftige AGI Ziele verfolgen könnte, die mit dem menschlichen Überleben unvereinbar sind

Zu den Organisationen, die an KI-Sicherheit arbeiten, gehören OpenAIs Safety-Team, Anthropic (gegründet von ehemaligen OpenAI-Sicherheitsforschern), DeepMinds Safety-Team und unabhängige Institute wie MIRI und ARC.

## KI in der Gesellschaft

KI verändert nahezu jede Branche:

- **Gesundheitswesen**: KI unterstützt die Diagnose von Krebs anhand medizinischer Bilder, sagt Behandlungsergebnisse voraus, beschleunigt die Wirkstoffforschung (AlphaFold löste das Problem der Vorhersage von Proteinstrukturen) und personalisiert Behandlungspläne.
- **Finanzen**: Betrugserkennung, algorithmischer Handel, Kredit-Scoring und Robo-Advisors nutzen ML-Modelle.
- **Transport**: Selbstfahrende Fahrzeuge verwenden Computer Vision, Lidar und bestärkendes Lernen. Tesla Autopilot, Waymo und Cruise gehören zu den bekanntesten Projekten.
- **Bildung**: Personalisierte Lernplattformen passen Inhalte an das individuelle Lerntempo und den Lernstil von Schülerinnen und Schülern an.
- **Kreative Bereiche**: KI erzeugt Musik, Kunst und Texte; Werkzeuge wie Midjourney, DALL-E und GitHub Copilot haben kreative Arbeitsabläufe verändert.
- **Cybersicherheit**: KI erkennt Anomalien, identifiziert Bedrohungen und treibt sowohl Angriffe als auch Verteidigungsmaßnahmen an.

## Robotik und verkörperte KI (Embodied AI)

Robotik verbindet KI mit physischen Maschinen. Moderne Roboter nutzen Wahrnehmung (Kameras, Lidar), Planung und Steuerung, um sich in Umgebungen zu bewegen und Objekte zu manipulieren. Boston Dynamics' Atlas demonstriert fortgeschrittene zweibeinige Fortbewegung. Industrieroboter von Unternehmen wie ABB und FANUC automatisieren die Fertigung. Haushaltsroboter (Roomba) und chirurgische Roboter (da Vinci-System) setzen KI in alltäglichen und medizinischen Einsatzszenarien ein. Die Forschung zur verkörperten KI (Embodied AI) konzentriert sich auf Agenten, die physische Fähigkeiten durch die Interaktion mit der Welt erlernen und die Lücke zwischen simulierten und realen Umgebungen überbrücken.

## Aktuelle KI-Trends (2020er)

- **Multimodale KI**: Systeme, die Text, Bilder, Audio und Video gemeinsam verarbeiten (GPT-4V, Gemini)
- **Agenten und agentische KI**: LLMs, die Werkzeuge verwenden, im Web surfen, Code schreiben und mehrstufige Aktionen ausführen können (OpenAIs Operator, Anthropic Computer Use)
- **Open-Weight-Modelle**: Metas LLaMA hat den Zugang zu großen Modellen für Forschende demokratisiert
- **On-Device-KI**: Ausführung von KI-Modellen lokal auf Telefonen und Laptops ohne Cloud-Konnektivität (Apple Intelligence, Qualcomm NPUs)
- **KI-Regulierung**: Der EU AI Act (2026) ist das weltweit erste umfassende KI-Gesetz, das KI-Systeme nach Risikostufen klassifiziert
