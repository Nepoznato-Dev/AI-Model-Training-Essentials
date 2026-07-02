# Künstliche Intelligenz

## Was ist Künstliche Intelligenz?

Künstliche Intelligenz (AI) bezeichnet die Simulation menschlicher Intelligenz in Maschinen, die darauf programmiert sind, zu denken, zu lernen und Probleme zu lösen. AI-Systeme können Aufgaben ausführen, die typischerweise menschliche Intelligenz erfordern, etwa Sprache erkennen, Entscheidungen treffen, Sprachen übersetzen und Objekte in Bildern identifizieren. Der Begriff wurde 1956 von John McCarthy auf der Dartmouth Conference geprägt, die weithin als Gründungsereignis von AI als Fachgebiet gilt.

Moderne AI wird grob in Narrow AI (auch Weak AI genannt), die für bestimmte Aufgaben entwickelt wurde, und die theoretische Artificial General Intelligence (AGI), die die menschliche kognitive Fähigkeit in allen Bereichen erreichen oder übertreffen würde, unterteilt. Alle heutigen AI-Systeme sind Narrow AI.

## Geschichte der AI

Die Geschichte der AI umfasst fast acht Jahrzehnte. Frühe theoretische Grundlagen wurden von Alan Turing gelegt, dessen Aufsatz von 1950 „Computing Machinery and Intelligence“ den Turing-Test einführte — ein Maß für die Fähigkeit einer Maschine, intelligentes Verhalten zu zeigen, das von dem eines Menschen nicht zu unterscheiden ist. Die Dartmouth Conference von 1956 etablierte AI formell als akademische Disziplin.

In den 1950er- bis 1970er-Jahren gab es optimistische frühe Programme wie ELIZA (ein einfacher Chatbot) und LISP (eine für AI entwickelte Programmiersprache). Die „AI winters“ der 1970er- und 1980er-Jahre waren Phasen reduzierter Finanzierung und geringeren Interesses nach unerfüllten Erwartungen. Ein Wiederaufschwung in den 1980er-Jahren kam mit Expertensystemen — regelbasierten Programmen, die menschliches Fachwissen kodierten. Die 2000er brachten Durchbrüche im Machine Learning, angetrieben durch das Internet und wachsende Datensätze. Die 2010er sahen den Aufstieg des Deep Learning, das Computer Vision, Natural Language Processing (NLP) und Reinforcement Learning veränderte.

## Machine Learning

Machine Learning (ML) ist ein Teilgebiet der AI, das Systemen ermöglicht, aus Daten zu lernen, ohne explizit programmiert zu werden. Wichtige ML-Kategorien sind:

**Supervised Learning**: Das Modell wird auf gelabelten Eingabe-Ausgabe-Paaren trainiert. Beispiele sind Spam-Erkennung und Bildklassifikation. Zu den Algorithmen gehören lineare Regression, Entscheidungsbäume, Support Vector Machines und neuronale Netze.

**Unsupervised Learning**: Das Modell findet Muster in ungelabelten Daten. Beispiele sind Kundensegmentierung und Anomalieerkennung. Zu den Algorithmen gehören k-means clustering und principal component analysis (PCA).

**Reinforcement Learning**: Ein Agent lernt durch Interaktion mit einer Umgebung und erhält Belohnungen oder Strafen. Wird in spielenden AI-Systemen (AlphaGo, AlphaZero), Robotik und Empfehlungssystemen eingesetzt.

**Semi-Supervised and Self-Supervised Learning**: Kombiniert kleine Mengen gelabelter Daten mit großen ungelabelten Datensätzen. GPT-Modelle verwenden während des Pre-Trainings einen selbstüberwachten Ansatz.

## Deep Learning

Deep Learning ist ein Teilgebiet des Machine Learning, das künstliche neuronale Netze mit vielen Schichten (tiefe Netze) verwendet. Diese Netze sind lose von der neuronalen Struktur des Gehirns inspiriert und lernen hierarchische Repräsentationen von Daten. Deep Learning treibt an:

- **Computer Vision**: Bilderkennung, Objekterkennung, medizinische Bildgebung
- **Natural Language Processing**: Maschinelle Übersetzung, Sentiment-Analyse, Fragebeantwortung
- **Speech Recognition**: Sprachassistenten wie Siri, Alexa, Google Assistant
- **Generative AI**: Bildgenerierung (DALL-E, Stable Diffusion), Textgenerierung (GPT)

Wichtige Deep-Learning-Architekturen sind convolutional neural networks (CNNs) für Bilder, recurrent neural networks (RNNs) und LSTMs für Sequenzen, Transformer für Sprache und generative adversarial networks (GANs) für Synthese.

## Large Language Models (LLMs)

Large Language Models (LLMs) sind AI-Systeme, die auf riesigen Mengen von Textdaten trainiert werden, um menschliche Sprache zu verstehen und zu erzeugen. Sie basieren auf der Transformer-Architektur, die im Paper von 2017 „Attention is All You Need“ von Vaswani et al. eingeführt wurde. LLMs sagen das nächste Token (Wortteil) in einer Sequenz vorher, wodurch sie zusammenhängenden Text generieren, Fragen beantworten, Code schreiben und Reasoning-Aufgaben ausführen können.

Zu den bemerkenswerten LLMs gehören:
- **GPT series** (OpenAI): GPT-3, GPT-4 und Nachfolger — breit für Chat und Code genutzt
- **Claude** (Anthropic): Fokus auf Sicherheit und Hilfsbereitschaft
- **Gemini** (Google DeepMind): Multimodal, integriert Text, Bilder und Code
- **LLaMA / Llama 3** (Meta): Open-Weight-Modelle für Forschung und lokale Bereitstellung
- **Mistral** (Mistral AI): Effiziente offene Modelle, die mit deutlich größeren LLMs konkurrieren

LLMs werden in zwei Phasen trainiert: Pre-Training (unüberwacht auf großen Textkorpora) und Fine-Tuning (überwacht oder per reinforcement learning from human feedback, RLHF). Kontextfenster beschreiben, wie viel Text ein LLM auf einmal verarbeiten kann, von 4K Tokens (frühes GPT-3) bis zu über 1 Million Tokens in den fortschrittlichsten Modellen des Jahres 2024.

## Ethik und Sicherheit der AI

AI wirft wichtige ethische Fragen auf, darunter Bias, Privatsphäre, Arbeitsplatzverdrängung und das Risiko von Missbrauch. Algorithmischer Bias entsteht, wenn Trainingsdaten historische Ungleichheiten widerspiegeln und dadurch AI-Systeme diskriminierende Ausgaben erzeugen. Gesichtserkennungssysteme haben höhere Fehlerraten bei Personen mit dunklerer Haut gezeigt. Einstellungsalgorithmen wurden dabei beobachtet, männliche Kandidaten zu bevorzugen.

AI Safety ist das Fachgebiet, das sicherstellen soll, dass AI-Systeme sich wie beabsichtigt verhalten, ohne unbeabsichtigten Schaden zu verursachen. Wichtige Anliegen sind:
- **Alignment**: Sicherstellen, dass AI-Ziele mit menschlichen Werten übereinstimmen
- **Interpretability / Explainability**: Verstehen, warum eine AI eine Entscheidung getroffen hat (kritisch in Medizin, Recht, Finanzen)
- **Misuse**: AI-generierte Deepfakes, Desinformation, Cyberangriffe
- **Existential risk**: Theoretische Sorge, dass eine zukünftige AGI Ziele verfolgen könnte, die nicht mit dem Überleben der Menschheit vereinbar sind

Zu den Organisationen, die an AI Safety arbeiten, gehören das Safety-Team von OpenAI, Anthropic (von ehemaligen OpenAI-Safety-Forschern gegründet), das Safety-Team von DeepMind und unabhängige Institute wie MIRI und ARC.

## AI in der Gesellschaft

AI verändert nahezu jede Branche:

- **Healthcare**: AI unterstützt bei der Krebsdiagnose aus medizinischen Bildern, bei der Vorhersage von Patientenergebnissen, bei der Beschleunigung der Wirkstoffforschung (AlphaFold löste die Vorhersage der Proteinfaltungsstruktur) und bei der Personalisierung von Behandlungsplänen.
- **Finance**: Betrugserkennung, algorithmischer Handel, Kreditbewertung und Robo-Advisors nutzen ML-Modelle.
- **Transportation**: Selbstfahrende Fahrzeuge nutzen Computer Vision, lidar und Reinforcement Learning. Tesla Autopilot, Waymo und Cruise gehören zu den führenden Bemühungen.
- **Education**: Personalisierte Lernplattformen passen Inhalte an das individuelle Lerntempo und den Lernstil von Schülern an.
- **Creative fields**: AI erzeugt Musik, Kunst und Texte; Werkzeuge wie Midjourney, DALL-E und GitHub Copilot haben kreative Workflows verändert.
- **Cybersecurity**: AI erkennt Anomalien, identifiziert Bedrohungen und treibt sowohl Angriffe als auch Verteidigung an.

## Robotik und verkörperte AI

Robotik kombiniert AI mit physischen Maschinen. Moderne Roboter nutzen Wahrnehmung (Kameras, lidar), Planung und Steuerung, um sich in Umgebungen zu bewegen und diese zu manipulieren. Atlas von Boston Dynamics demonstriert fortgeschrittene zweibeinige Bewegung. Industrieroboter von Unternehmen wie ABB und FANUC automatisieren die Fertigung. Haushaltsroboter (Roomba) und Operationsroboter (da Vinci System) setzen AI im Alltag und in der Medizin ein. Die Forschung zu verkörperter AI konzentriert sich auf Agenten, die physische Fähigkeiten durch Interaktion mit der Welt erlernen, und überbrückt die Lücke zwischen simulierten und realen Umgebungen.

## Aktuelle AI-Trends (2020er)

- **Multimodale AI**: Systeme, die Text, Bilder, Audio und Video gemeinsam verarbeiten (GPT-4V, Gemini)
- **Agenten und agentische AI**: LLMs, die Werkzeuge nutzen, im Web browsen, Code schreiben und mehrstufige Aktionen ausführen können (OpenAIs Operator, Anthropic Computer Use)
- **Open-Weight-Modelle**: Metas LLaMA demokratisierte den Zugang zu großen Modellen für Forscher
- **On-Device-AI**: AI-Modelle lokal auf Smartphones und Laptops ohne Cloud-Konnektivität ausführen (Apple Intelligence, Qualcomm NPUs)
- **AI-Regulierung**: Der EU AI Act (2024) ist das erste umfassende AI-Gesetz der Welt und klassifiziert AI-Systeme nach Risikostufen
