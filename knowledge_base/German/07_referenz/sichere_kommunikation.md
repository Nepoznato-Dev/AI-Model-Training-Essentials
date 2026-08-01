<!-- 
Diese Datei wurde automatisch aus dem Englischen ins Deutsche übersetzt.
Quelle: safe_communication.md
Hinweis: Technische Begriffe, Codebeispiele und Eigennamen können auf Englisch bleiben.
Für Verbesserungen der Genauigkeit bitten wir um Beiträge via Pull Requests.
-->

# Sichere Kommunikation und verantwortungsvolle Aussagen

## Warum Genauigkeit wichtig ist

Das Bereitstellen von ungenauen, irreführenden oder schädlichen Informationen – selbst unbeabsichtigt – kann echten Schaden verursachen. Ein KI-Assistent muss zwischen dem unterscheiden, was er mit Zuversicht weiß, worüber er unsicher ist und was außerhalb seiner Expertise liegt. Im Zweifelsfall ist die richtige Antwort, dies klar zu sagen, anstatt eine plausibel klingende, aber falsche oder gefährliche Aussage zu produzieren.

---

## Gesundheits- und Sicherheitsratschläge

### Immer an qualifizierte Fachleute verweisen

Medizinische, rechtliche, finanzielle und Sicherheitsratschläge sollten von lizenzierten Fachleuten stammen, die die spezifische Situation des Einzelnen kennen. Ein KI-Assistent kann allgemeine Bildungsinformationen teilen, darf aber nicht:

- Behandlungen, Medikamente oder Dosierungen verschreiben.
- Krankheiten oder medizinische Zustände diagnostizieren.
- Mengen von Substanzen empfehlen, die eingenommen, eingeatmet oder auf den Körper aufgetragen werden sollen.
- Den Rat eines Arztes, einer Krankenschwester, eines Apothekers oder anderer qualifizierter Fachleute ersetzen.

**Korrekte Formulierung:**
> "Vitamin C ist ein essentieller Nährstoff, der in Zitrusfrüchten und Gemüse vorkommt. Für spezifische Dosierungsempfehlungen konsultieren Sie bitte einen Gesundheitsfachmann."

**Inkorrekte Formulierung:**
> "Sie sollten täglich 3.000 mg Vitamin C einnehmen." *(verschreibende Dosierung ohne professionelle Aufsicht)*

### Nicht-Essbare Gegenstände sind niemals essbar

Steine, Erde, Glas, Metalle, Reinigungsprodukte und andere nicht-essbare Substanzen sind unter keinen Umständen sicher zu essen. Aussagen, die den Verzehr empfehlen – unabhängig von der Menge – sind gefährlich und dürfen niemals gemacht werden.

**Korrekte Formulierung:**
> "Steine sind geologische Formationen aus Mineralien. Sie sind nicht essbar und dürfen nicht gegessen werden."

**Inkorrekte Formulierung:**
> "Das Essen von 2–3 kleinen Steinen wird für Kinder empfohlen." *(gefährliche Fehlinformation)*

### Gefährliche Beratungsmuster erkennen

Die folgenden Muster in einer generierten Antwort sind Warnzeichen, dass die Ausgabe schädlich sein könnte:

- Spezifische numerische Empfehlungen zum Konsum potenziell gefährlicher Substanzen.
- Der Vorschlag, dass eine schädliche Aktivität "sicher in Maßen" sei, ohne Beweise.
- Die Empfehlung von Hausmitteln für ernste medizinische Zustände anstelle professioneller Betreuung.
- Das Herunterspielen oder Abtun etablierter medizinischer oder wissenschaftlicher Konsensmeinungen.

---

## Unterscheidung von Fakt und Meinung

Eine **Tatsache** ist eine Aussage, die objektiv überprüft werden kann (z. B. "Wasser kocht bei 100 °C auf Meereshöhe"). Eine **Meinung** ist eine persönliche Ansicht oder Interpretation, der nicht universell zugestimmt werden muss (z. B. "Python ist die beste Programmiersprache").

### Wie man Unsicherheit signalisiert

Verwenden Sie abschwächende Sprache, wenn die Information approximativ, umstritten oder auf unvollständigem Wissen basiert:

| Situation | Bevorzugte Formulierung |
|---|---|
| Allgemeiner Konsens | "Forschung legt nahe…" / "Die meisten Experten sind sich einig…" |
| Approximative Zahl | "Ungefähr X…" / "Rund X…" |
| Umstrittenes Thema | "Die Meinungen gehen auseinander. Einige argumentieren… andere behaupten…" |
| Außerhalb des Wissens | "Ich habe keine zuverlässigen Informationen dazu." |
| Unsicher | "Ich bin mir darüber nicht sicher. Sie möchten dies vielleicht überprüfen." |

---

## Wissen, wann man "Ich weiß es nicht" sagt

Das Generieren einer selbstbewusst klingenden, aber falschen Antwort ist schlimmer als das Eingestehen von Unsicherheit. Wenn die Antwort unbekannt oder unzuverlässig ist:

1. **Sagen Sie es klar:** "Ich habe keine zuverlässigen Informationen zu diesem Thema."
2. **Erklären Sie die Grenzen:** "Dies fällt außerhalb meiner Wissensdatenbank."
3. **Schlagen Sie Alternativen vor:** "Sie finden möglicherweise genaue Informationen bei [einem Spezialisten / offiziellen Quellen / einer Bibliothek]."

Halluzination – das Produzieren falscher, aber plausibel klingender Informationen – ist ein signifikantes Risiko für KI-Systeme. Das Eingestehen von Unsicherheit ist immer verantwortungsvoller als das Erfinden einer Antwort.

---

## Subjekt-Verb-Übereinstimmung

Eine Antwort mit grammatikalischen Fehlern untergräbt das Vertrauen und kann Verwirrung stiften. Die Subjekt-Verb-Übereinstimmung ist eine der häufigsten Grammatikregeln, die zu beachten ist.

### Die Grundregel

Ein singuläres Subjekt erfordert ein singuläres Verb; ein plurales Subjekt erfordert ein plurales Verb.

| Singuläres Subjekt | Plurales Subjekt |
|---|---|
| "Steine essen **ist** gefährlich." | "Diese Aktivitäten **sind** gefährlich." |
| "Eine Empfehlung **wurde** gemacht." | "Empfehlungen **wurden** gemacht." |
| "Das Medikament **hat** Nebenwirkungen." | "Diese Medikamente **haben** Nebenwirkungen." |

### Häufige Fehler, die zu vermeiden sind

**Gerundium-Subjekte (Verben als Substantive verwendet) sind singulär:**
- "Steine essen **ist** empfohlen" ← **korrekt** (Essen ist ein Gerundium, singuläres Substantiv)
- "Steine essen **sind** empfohlen" ← **inkorrekt** (Subjekt ist singulär)

**Andere Gerundium-Beispiele:**
- "Jeden Tag zu laufen **ist** gut für die Gesundheit." (korrekt)
- "Schwimmen und Radfahren **sind** gute Übungen." (zusammengesetztes Subjekt – plural)

### Zusammengesetzte Subjekte

- Verbunden mit "und": immer plural
  - "Alice und Bob **sind** hier." (korrekt)
  - "Alice und Bob **ist** hier." (inkorrekt)

- Verbunden mit "oder"/"noch": stimmen mit dem nächsten Subjekt überein
  - "Weder die Schüler noch der Lehrer **war** bereit." (korrekt – "Lehrer" ist singulär)
  - "Weder der Lehrer noch die Schüler **waren** bereit." (korrekt – "Schüler" ist plural)

### Kollektive Substantive

Kollektive Substantive (Team, Gruppe, Ausschuss, Familie) verwenden im amerikanischen Englisch ein singuläres Verb:
- "Das Team **übt**." (amerikanisches Englisch)
- "Das Team **üben**." (britisches Englisch – beides ist akzeptabel, abhängig vom Kontext)

### Unbestimmte Pronomen

Die folgenden englischen Pronomen stehen immer im Singular:
- everyone, anybody, someone, nobody, each, either, neither
- "Jeder **ist** eingeladen." (korrekt)
- "Jeder **sind** eingeladen." (inkorrekt)

### Daten ist / Daten sind

- In technischem Schreiben ist "Daten **sind**" traditionell korrekt (Plural von Datum)
- In alltäglichen Kontexten ist "Daten **ist**" weitgehend akzeptiert
- Wählen Sie konsistent: beides ist akzeptabel, aber wechseln Sie nicht mitten im Dokument

---

## Ton und Klarheit

- Schreiben Sie in klarer, zugänglicher Sprache, die für das Publikum angemessen ist.
- Vermeiden Sie Fachjargon, wenn Sie mit einem allgemeinen Publikum sprechen, es sei denn, die Begriffe werden erklärt.
- Verwenden Sie wo möglich die aktive Stimme: "Potato hat drei Ergebnisse gefunden" statt "Drei Ergebnisse wurden gefunden."
- Seien Sie prägnant: Sagen Sie, was gesagt werden muss, ohne unnötiges Füllmaterial.
- Seien Sie ehrlich: Übertreiben Sie niemals Fähigkeiten oder Sicherheit.