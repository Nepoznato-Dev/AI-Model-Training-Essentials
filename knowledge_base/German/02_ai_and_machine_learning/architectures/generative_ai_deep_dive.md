<!--
---
# Metadata
title: "Generative AI Deep Dive"
description: "GANs, VAEs, diffusion models, LLMs, generative AI applications"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [generative, ai, deep, dive, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Generative KI Deep Dive
Generative KI bezieht sich auf Modelle, die neue Inhalte – Bilder, Text, Audio, Video, Code – erstellen, anstatt nur vorhandene Daten zu klassifizieren oder vorherzusagen. Während große Sprachmodelle die meiste Aufmerksamkeit erhalten, ist die generative KI-Landschaft weitaus umfassender. Diese Datei behandelt die Architekturen, Techniken und Kompromisse hinter modernen generativen Systemen, von Diffusionsmodellen über Variations-Autoencoder bis hin zu Flussmodellen.
---

## Was macht ein Modell „generativ“?
| Geben Sie | ein Was es tut | Beispiel |
|------|-------------|---------|
| **Diskriminierend** | Lernen Sie die Grenze zwischen Klassen | „Ist dieses Bild eine Katze oder ein Hund?“ |
| **Generativ** | Erfahren Sie die Verteilung der Daten selbst | „Erstellen Sie ein neues Bild einer Katze“ |
Generative Modelle erfassen, *wie die Daten erzeugt werden*, nicht nur, wie sie kategorisiert werden. Das macht sie wesentlich leistungsfähiger – und schwieriger zu trainieren.
---

## Wichtige generative Architekturen
### Variationale Autoencoder (VAEs)
VAEs lernen eine komprimierte, strukturierte Darstellung (latenter Raum) der Daten und generieren dann neue Stichproben durch Stichproben aus diesem Raum.
| Komponente | Rolle |
|-----------|------|
| **Encoder** | Ordnet Eingabedaten einer Verteilung im latenten Raum zu (Mittelwert und Varianz) |
| **Latenter Speicherplatz** | Ein kontinuierlicher, niedrigdimensionaler Raum, in dem ähnliche Datenpunkte nahe beieinander liegen |
| **Decoder** | Ordnet Punkte im latenten Raum wieder dem Datenraum zu |
| **KL-Divergenz** | Regularisierungsterm, der die latente Verteilung nahe an einer Standardnormalverteilung | hält
**So funktioniert die Generierung**: Abtasten Sie einen zufälligen Vektor aus dem latenten Raum → leiten Sie ihn durch den Decoder → erhalten Sie einen neuen Datenpunkt.
| Stärke | Schwäche |
|----------|----------|
| Glatter, kontinuierlicher latenter Raum | Ausgaben neigen dazu, verschwommen zu sein |
| Prinzipieller mathematischer Rahmen | Begrenzt durch die Kapazität der Architektur |
| Kann zwischen Beispielen interpolieren | Weniger scharf als Diffusions- oder GAN-Ausgaben |
VAEs werden häufig als Komponenten in anderen Modellen verwendet (z. B. Stable Diffusion verwendet ein VAE als Teil seiner Pipeline).
### Generative Adversarial Networks (GANs)
GANs lassen zwei Netzwerke gegeneinander antreten: einen **Generator**, der gefälschte Daten erzeugt, und einen **Diskriminator**, der versucht, echte von gefälschten zu unterscheiden.
| Komponente | Ziel |
|-----------|------|
| **Generator** | Produzieren Sie Daten, die den Diskriminator täuschen |
| **Diskriminator** | Echte und generierte Daten richtig klassifizieren |
Sie trainieren gleichzeitig und drängen sich gegenseitig, sich zu verbessern. Theoretisch erzeugt der Generator schließlich Daten, die nicht von echten Daten zu unterscheiden sind.
| GAN-Variante | Schlüsselinnovation |
|-------------|---------------|
| **DCGAN** | Faltungsarchitekturen; Stalltraining |
| **StyleGAN / StyleGAN2 / StyleGAN3** | Stilbasierte Generierung; fotorealistische Gesichter; steuerbare Attribute |
| **CycleGAN** | Ungepaarte Bild-zu-Bild-Übersetzung (Pferd → Zebra) |
| **Pix2Pix** | Paarweise Bild-zu-Bild-Übersetzung (Skizze → Foto) |
| **ProGAN** | Progressives Wachstum für hochauflösende Bilder |
| **BigGAN** | Klassenbedingte Generierung im Maßstab |
**Warum GANs zurückgegangen sind**: Das Training ist bekanntermaßen instabil (Moduskollaps, verschwindende Gradienten). Diffusionsmodelle liefern jetzt für die meisten Bilderzeugungsaufgaben eine bessere Qualität. GANs werden immer noch für Echtzeitanwendungen (sie können schnell schließen) und spezifische Aufgaben wie Superauflösung verwendet.
### Diffusionsmodelle
Diffusionsmodelle sind der aktuelle Stand der Technik zur Bild- und Videogenerierung. Sie funktionieren, indem sie den Daten nach und nach Rauschen hinzufügen, bis es reines Zufallsrauschen ist, und dann lernen, den Prozess umzukehren.
| Phase | Was passiert |
|-------|-------------|
| **Vorwärtsprozess (Training)** | Fügen Sie langsam Gaußsches Rauschen über Hunderte/Tausende von Schritten hinzu, bis die Daten zerstört sind |
| **Umgekehrter Prozess (Generierung)** | Lernen Sie, Schritt für Schritt zu entrauschen, beginnend mit dem reinen Rauschen, bis ein sauberes Bild entsteht |
| Modell | Entwickler | Bemerkenswerte Funktion |
|-------|-----------|-----------------|
| **DDPM** (Diffusions-Probabilistisches Modell zur Rauschunterdrückung) | Ho et al., 2020 | Dargestellte Diffusionsmodelle können qualitativ hochwertige Bilder erzeugen |
| **Stabile Diffusion** | Stabilitäts-KI | Latente Diffusion (läuft im komprimierten Raum); Open-Source |
| **DALL-E 3** | OpenAI | Integriert in ChatGPT zum Verstehen von Texten |
| **Mitten auf der Reise** | Mittlerweile | Künstlerische Qualität; Closed-Source |
| **Bild** | Google DeepMind | Text-zu-Bild mit hoher Wiedergabetreue |
| **Sora** | OpenAI | Videoerzeugung über Diffusionstransformatoren |
| **FLUSS** | Schwarzwaldlabore | Offener Nachfolger von Stable Diffusion |
### Warum Diffusionsmodelle gewonnen haben
| Vorteil | Erklärung |
|-----------|-------------|
| **Trainingsstabilität** | Viel stabiler als GANs; kein kontradiktorisches Training |
| **Ausgabequalität** | Modernste Bildqualität und Vielfalt |
| **Steuerbarkeit** | Kann mit Text (via CLIP), Inpainting-Masken oder anderen Bedingungen geführt werden |
| **Vielfalt** | Weniger Moduskollaps als bei GANs; erzeugt vielfältige Ergebnisse |
| Nachteil | Erklärung |
|-------------|-------------|
| **Langsame Schlussfolgerung** | Erfordert viele Entrauschungsschritte (typischerweise 20–50) |
| **Rechenintensiv** | Jeder Schritt ist ein vollständiger Vorwärtsdurchlauf durch ein großes Modell |
### Latente Verbreitung
Die Diffusion im Pixelraum durchzuführen ist teuer. **Latente Diffusion** (verwendet von Stable Diffusion) führt den Diffusionsprozess stattdessen in einem komprimierten latenten Raum aus.
| Schritt | Was passiert |
|------|-------------|
| 1. Komprimieren | Eine vorab trainierte VAE kodiert das Bild in eine kleinere latente Darstellung |
| 2. Diffuse | Das Diffusionsmodell fügt Rauschen im latenten Raum hinzu/entfernt |
| 3. Dekodieren | Der VAE-Decoder wandelt das latente Bild wieder in ein Vollbild um
Dadurch wird die Erzeugung erheblich schneller und kostengünstiger, während gleichzeitig die Qualität erhalten bleibt.
---

## Textbedingte Generierung
Die meisten modernen generativen Systeme basieren auf Texteingabeaufforderungen – Sie beschreiben, was Sie wollen, und das Modell generiert es.
### CLIP (Kontrastive Sprache-Bild-Vorschulung)
CLIP lernt einen gemeinsamen Einbettungsraum für Text und Bilder. Es wurde auf Milliarden von Bild-Text-Paaren aus dem Internet trainiert.
| Fähigkeit | Beschreibung |
|------------|-------------|
| **Zero-Shot-Klassifizierung** | Bilder mithilfe von Textbeschreibungen ohne Schulung klassifizieren |
| **Bild-Text-Abruf** | Finden Sie das relevanteste Bild für eine Textabfrage |
| **Diffusion leiten** | Lenken Sie die Bildgenerierung auf die Texteingabeaufforderung |
### Klassifikatorfreie Anleitung (CFG)
CFG steuert, wie genau das generierte Bild der Textaufforderung folgt.
| CFG-Skala | Wirkung |
|-----------|--------|
| **1,0** | Keine Anleitung; vielfältig, stimmt aber möglicherweise nicht mit der Eingabeaufforderung | überein
| **5,0–7,5** | Ausgewogen; gute Qualität und schnelle Einhaltung |
| **10.0+** | Starke Einhaltung; kann übersättigte oder artefaktreiche Bilder erzeugen |
---

## Andere generative Ansätze
### Normalisierung von Flüssen
| Funktion | Beschreibung |
|---------|-------------|
| **Wie es funktioniert** | Lernen Sie eine invertierbare Zuordnung zwischen Daten und einer einfachen Verteilung |
| **Stärke** | Exakte Wahrscheinlichkeitsberechnung; schnelle Probenahme |
| **Schwäche** | Erfordert sorgfältig entworfene Architekturen; weniger flexibel |
| **Anwendungsfälle** | Anomalieerkennung, Dichteschätzung |
### Autoregressive Modelle
| Funktion | Beschreibung |
|---------|-------------|
| **Wie es funktioniert** | Generieren Sie Daten Element für Element und konditionieren Sie dabei alle vorherigen Elemente |
| **Stärke** | Natürlich für sequentielle Daten (Text, Code, Musik) |
| **Schwäche** | Langsame Generierung (muss sequentiell erfolgen); begrenzt durch Trainingsdatenverteilung |
| **Beispiele** | GPT (Text), WaveNet (Audio), ImageGPT (Bilder) |
### Energiebasierte Modelle
| Funktion | Beschreibung |
|---------|-------------|
| **Wie es funktioniert** | Lernen Sie eine Energiefunktion; niedrige Energie = realistische Daten |
| **Stärke** | Flexibel; keine Normalisierung erforderlich |
| **Schwäche** | Das Training ist schwierig; Probenahme erfordert MCMC |
| **Anwendungsfälle** | Theoretische Forschung; einige Robotikanwendungen |
---

## Bewertungsmetriken
Wie messen Sie die Qualität der generierten Daten? Es ist schwieriger, als Sie vielleicht denken.
| Metrisch | Für | Was es misst | Einschränkung |
|--------|-----|-----------------|------------|
| **FID** (Fréchet Inception Distance) | Bilder | Abstand zwischen realer und generierter Bildverteilung | Niedriger ist besser; erfasst Vielfalt nicht gut |
| **IS** (Inception Score) | Bilder | Qualität und Vielfalt der generierten Bilder | Umstritten; kann gespielt werden |
| **CLIP-Score** | Text-zu-Bild | Wie gut das Bild mit der Textaufforderung übereinstimmt | Hängt von den Vorurteilen von CLIP ab |
| **Perplexität** | Text | Wie gut das Modell den nächsten Token vorhersagt | Niedriger ist besser; misst keine Kohärenz |
| **BLEU / ROUGE** | Textgenerierung | Überlappung mit Referenztext | Schlechter Stellvertreter für menschliches Urteilsvermögen |
| **FAD** (Fréchet Audio Distance) | Audio | Abstand zwischen realen und generierten Audioverteilungen | Analog zu FID für Audio |
---

## Kontrollierbare Erzeugung
Mit modernen Systemen können Sie über reine Textaufforderungen hinaus steuern, was generiert wird.
| Methode | Steuertyp | Beispiel |
|--------|-------------|---------|
| **Inpainting** | Maskierte Bereiche ausfüllen | Ein Objekt aus einem Foto entfernen |
| **Outpainting** | Über Bildgrenzen hinausgehen | Eine Landschaft breiter machen |
| **ControlNet** | Strukturelle Führung (Kanten, Tiefe, Pose) | Erzeugen Sie ein Bild, das einer bestimmten Pose entspricht |
| **IP-Adapter** | Stil oder Inhalt aus einem Referenzbild | „Lass es wie dieses Gemälde aussehen“ |
| **LoRA** | Fein abgestimmter Stil oder Konzept | Einen bestimmten Charakter oder Kunststil hinzufügen |
| **Img2Img** | Ein vorhandenes Bild transformieren | Verwandeln Sie eine Skizze in ein fotorealistisches Bild |
---

## Videogenerierung
Die Videogenerierung ist nach Bildern die nächste Grenze. Es fügt die Dimension von Zeit und Bewegung hinzu.
| Modell | Ansatz | Bemerkenswerte Funktion |
|-------|----------|-----------------|
| **Sora** (OpenAI) | Diffusionstransformator | Bis zu 1080p; versteht Physik einigermaßen gut |
| **Landebahn Gen-3** | Diffusionsbasiert | Kommerzielles Tool zur Videogenerierung |
| **Pika** | Diffusionsbasiert | Kurze Videoclips aus Text |
| **Kling** | Autoregressiv + Diffusion | Generierung von Langformatvideos |
| **Veo 2** (Google) | Diffusionstransformator | Hochwertiges, physikalisch konsistentes Video |
### Herausforderungen bei der Videogenerierung
| Herausforderung | Warum es schwer ist |
|-----------|--------------|
| **Zeitliche Konsistenz** | Objekte sollten in allen Frames gleich aussehen |
| **Physik** | Schwerkraft, Kollisionen, Strömungsdynamik müssen annähernd korrekt sein |
| **Länge** | Minutenlang zusammenhängendes Video zu generieren ist weitaus schwieriger als ein einzelnes Bild |
| **Berechnen** | Video besteht im Wesentlichen aus vielen Bildern; Kostenstaffel mit Frameanzahl |
| **Bewertung** | Keine Standardmetrik erfasst die Videoqualität gut |
---

## Audioerzeugung
| Modell | Geben Sie | ein Bewerbung |
|-------|------|-------------|
| **WaveNet** (DeepMind) | Autoregressiv | Hochwertige Sprachsynthese |
| **VALL-E** (Microsoft) | Neuronaler Codec | Text-to-Speech aus einer 3-Sekunden-Sprachprobe |
| **MusicGen** (Meta) | Transformatorbasiert | Text-zu-Musik-Generierung |
| **AudioLDM** | Latente Diffusion | Erzeugung von Soundeffekten |
| **ElevenLabs** | Kommerziell | Stimmklonen und -synthese |
---

## Die Ökonomie der Generation
| Faktor | Auswirkungen |
|--------|--------|
| **Schulungskosten** | Diffusionsmodelle: 100.000–10 Mio. USD+, je nach Umfang |
| **Inferenzkosten** | Bilderzeugung: ~ 0,01–0,05 $ pro Bild im Maßstab |
| **Hardware** | Schulung: mehrere A100/H100-GPUs; Schlussfolgerung: einzelne GPU möglich |
| **Offen vs. geschlossen** | Offene Modelle (Stabile Diffusion, FLUX) können lokal ausgeführt werden; geschlossene Modelle (DALL-E, Midjourney) sind nur API-fähig |
---

## Zusammenfassung
Generative KI hat sich von GANs über VAEs zu Diffusionsmodellen und darüber hinaus entwickelt. Die wichtigsten Erkenntnisse über alle diese Architekturen hinweg sind dieselben: Lernen Sie die Verteilung von Daten kennen und nutzen Sie diese dann, um neue Inhalte zu erstellen. Diffusionsmodelle dominieren derzeit aufgrund ihrer Trainingsstabilität und Ausgabequalität die Bild- und Videoerzeugung. VAEs dienen als entscheidende Bausteine. Autoregressive Modelle dominieren Text und Code. Der Bereich bewegt sich in Richtung multimodaler Generierung – Systeme, die aus jeder Kombination von Eingaben Text, Bilder, Audio und Video erzeugen können – und in Richtung einer schnelleren, kostengünstigeren und kontrollierbareren Generierung.