---
# Metadata
title: "Signal Processing"
description: "Fourier transforms, FFT, Laplace transforms, Z-transforms, filtering, sampling theorem, windowing, spectral analysis, and wavelets"
category: "Data Science and Analytics"
subcategory: "Mathematics"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "AI Model Training Team"
    changes: "Initial deep-dive into signal processing"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [signal-processing, fourier-transform, fft, laplace-transform, z-transform, filtering, sampling-theorem, wavelets]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "optics_and_waves.md"
  - "numerical_methods.md"
estimated_reading_time: "25 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Signalverarbeitung
Signalverarbeitung ist die Wissenschaft der Analyse, Modifizierung und Synthese von Signalen – Darstellungen physikalischer Größen, die sich über Zeit, Raum oder Frequenz ändern. Audio, Bilder, Video, Sensordaten, Gehirnwellen, Aktienkurse – alles sind Signale. Die mathematischen Werkzeuge der Signalverarbeitung (Fourier-Transformationen, Filter, Abtasttheorie) sind grundlegend für maschinelles Lernen, Kommunikation, medizinische Bildgebung und praktisch jeden Bereich, der mit Daten arbeitet.
---

## Signale und Systeme
### Signalklassifizierung
| Geben Sie | ein Beschreibung | Beispiel |
|------|-------------|---------|
| **Kontinuierliche Zeit** | Definiert für alle t ∈ ℝ | Audiospannung, Temperatur |
| **Zeitdiskrete** | Definiert durch ganzzahlige Indizes n | Gesampeltes Audio, Pixelwerte |
| **Analog** | Kontinuierlich in Zeit und Amplitude | Schallplattenrille |
| **Digital** | Zeitdiskret und quantisierte Amplitude | MP3-Datei, JPEG-Bild |
| **Periodisch** | x(t + T) = x(t) für alle t | Sinuswelle, Rechteckwelle |
| **Aperiodisch** | Kein sich wiederholendes Muster | Sprache, Musik |
| **Deterministisch** | Völlig vorhersehbar | Sinuswelle |
| **Stochastisch** | Enthält Zufälligkeit | Lärm, Aktienkurse |
### Systemeigenschaften
| Eigentum | Definition | Beispiel |
|----------|-----------|---------|
| **Linear** | T[ax₁ + bx₂] = aT[x₁] + bT[x₂] | Tiefpassfilter |
| **Zeitinvariant** | Verschiebung der Eingabe → gleiche Verschiebung der Ausgabe | Beliebiger fester Filter |
| **Kausal** | Der Output hängt nur von aktuellen und vergangenen Inputs ab | Echtzeitsystem |
| **Stabil (BIBO)** | Begrenzte Eingabe → begrenzte Ausgabe | Gut gestalteter Filter |
| **Gedächtnislos** | Die Ausgabe hängt nur von der aktuellen Eingabe | ab Verstärker |
---

## Fourier-Transformation
Die **Fourier-Transformation** zerlegt ein Signal in seine einzelnen Frequenzen.
### Kontinuierliche Fourier-Transformation
X(f) = ∫_{−∞}^{∞} x(t) e^{−j2πft} dt
Umkehrung: x(t) = ∫_{−∞}^{∞} X(f) e^{j2πft} df
### Fourier-Transformationspaare
| Zeitbereich x(t) | Frequenzbereich X(f) |
|-----|--------|
| Rechteckimpuls | sinc-Funktion |
| sinc-Funktion | Rechteckimpuls |
| Gaußsches e^{−at²} | Gaußsche (√(π/a))e^{−π²f²/a} |
| Dirac-Delta δ(t) | 1 (alle Frequenzen) |
| Komplexe Exponentialfunktion e^{j2πf₀t} | δ(f − f₀) |
| Kosinus cos(2πf₀t) | ½[δ(f−f₀) + δ(f+f₀)] |
### Schlüsseleigenschaften
| Eigentum | Zeitbereich | Frequenzbereich |
|----------|-------------|-----------------|
| Linearität | ax₁(t) + bx₂(t) | aX₁(f) + bX₂(f) |
| Zeitverschiebung | x(t − t₀) | X(f)e^{−j2πft₀} |
| Frequenzverschiebung | x(t)e^{j2πf₀t} | X(f − f₀) |
| Faltung | x₁(t) ∗ x₂(t) | X₁(f) · X₂(f) |
| Multiplikation | x₁(t) · x₂(t) | X₁(f) ∗ X₂(f) |
| Differenzierung | dx/dt | j2πf X(f) |
| Satz von Parseval | ∫\|x(t)\|² dt | ∫\|X(f)\|² df |
**Faltungssatz:** Faltung in der Zeit = Multiplikation in der Frequenz. Dies ist die wichtigste Eigenschaft – sie verwandelt teure Faltungsoperationen in kostengünstige Multiplikationen.
### Diskrete Fourier-Transformation (DFT)
Für eine Folge x[0], x[1], ..., x[N−1]:
X[k] = Σ_{n=0}^{N−1} x[n] e^{−j2πkn/N}, k = 0, 1, ..., N−1
| Eigentum | Wert |
|----------|-------|
| Eingabe | N reale oder komplexe Stichproben |
| Ausgabe | N komplexe Frequenz-Bins |
| Frequenzauflösung | f_s/N (wobei f_s die Abtastrate ist) |
| Nyquist-Frequenz | f_s/2 (maximal darstellbare Frequenz) |
| Komplexität | O(N²) direkte Berechnung |
### Schnelle Fourier-Transformation (FFT)
Die **FFT** berechnet die DFT in O(N log N) anstelle von O(N²).
| N | O(N²)-Operationen | O(N log N) Operationen | Beschleunigung |
|---|------------------|-------|---------|
| 1.024 | 1.048.576 | 10.240 | 102× |
| 1.048.576 | 1,1 × 10¹² | 20.971.520 | 52.428× |
Die FFT ist einer der wichtigsten Algorithmen, die jemals erfunden wurden. Es ermöglicht Echtzeit-Audioverarbeitung, Bildkomprimierung (JPEG), drahtlose Kommunikation (OFDM) und Spektralanalyse.
---

## Laplace-Transformation
Die **Laplace-Transformation** erweitert die Fourier-Transformation, um instabile Systeme und transiente Analysen zu verarbeiten.
F(s) = ∫₀^∞ f(t) e^{−st} dt, wobei s = σ + jω
### Gemeinsame Laplace-Transformationen
| f(t) | F(s) | Konvergenzregion |
|------|------|-------|
| δ(t) (Impuls) | 1 | Alle s |
| u(t) (Schritt) | 1/s | Re(s) > 0 |
| e^{−at}u(t) | 1/(s+a) | Re(s) > −a |
| tⁿu(t) | n!/s^{n+1} | Re(s) > 0 |
| sin(ωt)u(t) | ω/(s²+ω²) | Re(s) > 0 |
| cos(ωt)u(t) | s/(s²+ω²) | Re(s) > 0 |
### Verbindung zur Fourier-Transformation
Wenn σ = 0 (s = jω), reduziert sich die Laplace-Transformation auf die Fourier-Transformation. Die Laplace-Transformation liefert ein vollständigeres Bild, indem sie Informationen über Wachstum/Verfall (σ) einbezieht.
---

## Z-Transformation
Die **Z-Transformation** ist das zeitdiskrete Äquivalent der Laplace-Transformation.
X(z) = Σ_{n=−∞}^{∞} x[n] z^{−n}
### Gemeinsame Z-Transformationen
| x[n] | X(z) | ROC |
|------|------|-----|
| δ[n] | 1 | Alle z |
| u[n] (Schritt) | z/(z−1) | \|z\| > 1 |
| aⁿu[n] | z/(z−a) | \|z\| > \|a\| |
| naⁿu[n] | az/(z−a)² | \|z\| > \|a\| |
| sin(ω₀n)u[n] | z sin(ω₀)/(z²−2z cos(ω₀)+1) | \|z\| > 1 |
### Beziehung zu anderen Transformationen
| Transformieren | Domäne | Variable |
|-----------|--------|----------|
| Fourier | Kontinuierliche Frequenz | f oder ω |
| Laplace | Komplexe Frequenz | s = σ + jω |
| Z-Transformation | Komplexe Frequenz (diskret) | z = e^{sT} |
Der Einheitskreis in der z-Ebene (|z| = 1) entspricht der Fourier-Transformation.
---

## Filter
Filter lassen bestimmte Frequenzkomponenten selektiv durch oder blockieren sie.
### Filtertypen
| Geben Sie | ein Pässe | Blöcke | Bewerbung |
|------|--------|--------|-------------|
| **Tiefpass** | Niedrige Frequenzen | Hohe Frequenzen | Glättung, Anti-Aliasing |
| **Hochpass** | Hohe Frequenzen | Niedrige Frequenzen | Kantenerkennung, Rauschentfernung |
| **Bandpass** | Eine Reihe von Frequenzen | Außerhalb des Bereichs | Kanalauswahl (Radio) |
| **Bandanschlag (Kerbe)** | Alles außer einem Bereich | Ein bestimmter Bereich | Entfernung von Netzbrummen |
### FIR vs. IIR-Filter
| Eigentum | FIR (Finite Impulse Response) | IIR (Unendliche Impulsantwort) |
|----------|----------------|--------------------------------|
| Impulsantwort | Endliche Dauer | Unendliche Dauer |
| Stabilität | Immer stabil | Kann instabil sein |
| Phase | Kann exakt linear sein | Im Allgemeinen nichtlineare Phase |
| Feedback | Nein | Ja |
| Berechnung | Weitere Koeffizienten erforderlich | Weniger Koeffizienten bei gleichem Roll-off |
| Design | Windowing, Parks-McClellan | Butterworth, Chebyshev, elliptisch |
| Übertragungsfunktion | H(z) = Σ bₖz⁻ᵏ | H(z) = Σ bₖz⁻ᵏ / (1 + Σ aₖz⁻ᵏ) |
### Filterdesign-Spezifikationen
| Parameter | Beschreibung |
|-----------|-------------|
| **Passband** | Frequenzbereich, der mit minimalem Verlust passieren soll |
| **Stoppband** | Frequenzbereich, der gedämpft werden soll |
| **Grenzfrequenz** | Grenze zwischen Durchlassband und Sperrband |
| **Welligkeit** | Variation der Durchlassband- (oder Sperrband-)Verstärkung |
| **Abrollen** | Dämpfungsrate (dB pro Oktave oder Dekade) |
| **Übergangsband** | Bereich zwischen Durchlassband und Sperrband |
### Gängige Filterdesigns
| Design | Eigenschaften | Anwendungsfall |
|--------|----------------|----------|
| **Butterworth** | Maximal flacher Durchlassbereich, moderater Roll-Off | Allzweck |
| **Tschebyschew Typ I** | Welligkeit im Durchlassbereich, steilerer Abfall | Wenn es auf Roll-off ankommt |
| **Tschebyschew Typ II** | Welligkeit im Sperrband, flaches Durchlassband | Wenn es auf die Ebenheit des Durchlassbandes ankommt |
| **Elliptisch (Cauer)** | Welligkeit in beiden, steilster Abfall | Mindestbestellmenge erforderlich |
| **Bessel** | Lineare Phase (maximal flache Gruppenverzögerung) | Wellenform beibehalten |
---

## Stichprobentheorie
### Nyquist-Shannon-Abtasttheorem
Ein kontinuierliches Signal lässt sich aus seinen Abtastwerten perfekt rekonstruieren, wenn die Abtastrate das Doppelte der Maximalfrequenz überschreitet:
f_s > 2f_max
| Begriff | Definition |
|------|------------|
| **Abtastrate** (f_s) | Anzahl der Samples pro Sekunde |
| **Nyquist-Kurs** | 2f_max (minimale Abtastrate) |
| **Nyquist-Frequenz** | f_s/2 (maximal darstellbare Frequenz) |
| **Aliasing** | Hohe Frequenzen werden als niedrige Frequenzen getarnt, wenn f_s < 2f_max |
### Gängige Abtastraten
| Bewerbung | Bewerten | Nyquist-Frequenz |
|-------------|------|-----|
| Telefonansprache | 8 kHz | 4 kHz |
| Audio-CD | 44,1 kHz | 22,05 kHz |
| Professionelles Audio | 48 kHz | 24 kHz |
| Hochauflösendes Audio | 96 kHz | 48 kHz |
| Video (30 fps) | 30 Hz (zeitlich) | 15 Hz |
### Anti-Aliasing
Vor der Abtastung entfernt ein **Anti-Aliasing-Filter** (Tiefpass) Frequenzen über f_s/2, um Aliasing zu verhindern.
---

## Fensterung
Bei der Analyse eines endlichen Segments eines Signals multiplizieren wir implizit mit einem rechteckigen Fenster, was zu spektralen Verlusten führt. **Fensterfunktionen** reduzieren diese Leckage.
### Allgemeine Windows
| Fenster | Hauptkeulenbreite | Seitenkeulenpegel | Anwendungsfall |
|--------|----------------|-----------------|----------|
| Rechteckig | Am schmalsten | −13 dB | Wenn die Auflösung am wichtigsten ist |
| Hann | 2× rechteckig | −31 dB | Allzweck |
| Hamming | 2× rechteckig | −41 dB | Reduzierte nächste Nebenkeule |
| Blackman | 3× rechteckig | −58 dB | Hoher Dynamikbereich |
| Kaiser | Einstellbar | Einstellbar (über β) | Wenn der Kompromiss einstellbar ist |
### Spektrale Leckage
Durch Multiplizieren eines Signals mit einem Fenster wird dessen Spektrum mit dem Spektrum des Fensters gefaltet. Breitere Hauptkeulen reduzieren die Frequenzauflösung; Untere Seitenkeulen verringern die Leckage.
---

## Wavelets
**Wavelets** sind kleine, lokalisierte wellenartige Funktionen, die für die Signalanalyse mit mehreren Auflösungen verwendet werden.
### Wavelet-Transformation
Im Gegensatz zur Fourier-Transformation (die globale Frequenzinformationen liefert) liefert die Wavelet-Transformation eine **Zeit-Frequenz-Lokalisierung**.
| Transformieren | Zeitauflösung | Frequenzauflösung |
|-----------|----------------|---------------------|
| Fourier | Keine (global) | Ausgezeichnet |
| Kurzzeit-FT | Fest (Fenstergröße) | Behoben |
| Wavelet | Variabel (gut bei hohen Frequenzen) | Variabel (gut bei niedriger Frequenz) |
### Gemeinsame Wavelet-Familien
| Familie | Eigenschaften | Bewerbung |
|--------|-----------|-------------|
| **Haar** | Einfachste, diskontinuierliche | Kantenerkennung, schnelle Analyse |
| **Daubechies** (dbN) | Kompakte Unterstützung, N verschwindende Momente | Komprimierung, Rauschunterdrückung |
| **Symlets** | Nahezu symmetrische Daubechies | Reduzierte Phasenverzerrung |
| **Coiflets** | Entwickelt für momentane Bedingungen | Signalverarbeitung |
| **Morlet** | Gaußsche Sinuskurve | Zeit-Frequenz-Analyse |
| **Mexikanischer Hut** | Zweite Ableitung von Gauß | Merkmalserkennung |
### Anwendungen von Wavelets
| Bewerbung | Wie Wavelets helfen |
|-------------|-------------------|
| Bildkomprimierung (JPEG 2000) | Darstellung mit mehreren Auflösungen, besser als DCT für Kanten |
| Rauschunterdrückung | Schwellenwert für kleine Wavelet-Koeffizienten (Signal liegt in großen Koeffizienten vor) |
| Merkmalserkennung | Kantenerkennung, Transientenerkennung in Zeitreihen |
| EKG-Analyse | Erkennung von QRS-Komplexen, Klassifizierung von Arrhythmien |
| Seismische Analyse | Identifizierung geologischer Schichten, Verarbeitung von Erdbebensignalen |
---

## Relevanz für maschinelles Lernen und Datenwissenschaft
| Signalverarbeitungskonzept | Bewerbung |
|-----------|-------------|
| Fourier-Transformation | Spektrale Merkmale für Audio-ML, Frequenzbereichsanalyse von Zeitreihen |
| FFT | Schnelle Faltung in CNNs (Spektralfaltung), effiziente Korrelation |
| Faltungssatz | Verstehen, wie CNNs funktionieren (es sind erlernte Filter) |
| Filter | Vorverarbeitung (Glättung, Rauschunterdrückung), Merkmalsextraktion |
| Abtasttheorem | Diskretisierung verstehen, Sensorraten auswählen, Aliasing vermeiden |
| Fenster | STFT für Audio-ML (Spektrogramme), Zeit-Frequenz-Analyse |
| Wavelets | Merkmalsextraktion für Zeitreihen, Komprimierung, Rauschunterdrückung |
| Laplace/Z-Transformation | Kontrolltheorie für die Robotik, Systemstabilität verstehen |
| Spektralanalyse | EEG/fMRT-Analyse, Vibrationsüberwachung, vorausschauende Wartung |
| Nyquist-Rate | Auswahl geeigneter Datenerfassungsraten für ML-Pipelines |
---

## Zusammenfassung
| Werkzeug | Domäne | Wichtige Erkenntnisse |
|------|--------|-------------|
| Fourier-Transformation | Zeit → Frequenz | Signale sind Summen von Sinuskurven |
| Laplace-Transformation | Zeit → Komplexe Frequenz | Behandelt Transienten und Stabilität |
| Z-Transformation | Diskrete Zeit → Komplex | Analyse und Design digitaler Filter |
| FFT | Effiziente DFT-Berechnung | O(N log N) statt O(N²) |
| Filter | Frequenzauswahl | Geben Sie weiter, was Sie benötigen, und blockieren Sie, was Sie nicht benötigen |
| Abtasttheorem | Kontinuierlich ↔ diskret | Schnell genug probieren, nichts verlieren |
| Fenster | Zeit-Frequenz-Kompromiss | Bilanzauflösung und Leckage |
| Wavelets | Analyse mit mehreren Auflösungen | Lokal in Zeit und Frequenz |
Die Signalverarbeitung liefert die mathematische Grundlage für das Verstehen, Analysieren und Bearbeiten von Daten. Jede Machine-Learning-Pipeline, die mit Zeitreihen, Audio, Bildern oder Sensordaten arbeitet, nutzt implizit Signalverarbeitungskonzepte. Insbesondere die Fourier-Transformation ist nach der Analysis wohl das wichtigste mathematische Werkzeug für jeden Datenwissenschaftler.