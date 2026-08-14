<!--
---
# Metadata
title: "Prompt Engineering"
description: "Prompt techniques and strategies"
category: "AI and Machine Learning"
subcategory: "Foundations"
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
    changes: "Moved to foundations/ subfolder; added subcategory field"
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
tags: [prompt, engineering, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Maagap na Engineering
Ang mabilis na engineering ay ang pagsasanay ng pagdidisenyo, pagpino, at pag-optimize ng mga input prompt upang makuha ang pinakamahusay na posibleng output mula sa isang modelo ng wika. Ito ay parehong sining at agham, at ito ang pangunahing interface para sa pagkontrol sa gawi ng LLM nang walang fine-tuning.
---

## Mga Pangunahing Prinsipyo
### Kalinawan at Pagtitiyak
Ang isang malinaw na prompt ay hindi nag-iiwan ng puwang para sa kalabuan. Tukuyin kung ano mismo ang gusto mo, kabilang ang format, haba, at pananaw.
**Malabo:**
> "Sabihin mo sa akin ang tungkol sa Python."
**Tukoy:**
> "Ipaliwanag ang Global Interpreter Lock (GIL) ng Python. Ilarawan ang epekto nito sa multithreading, magbigay ng isang solusyon, at panatilihin ang iyong sagot sa ilalim ng 200 salita."
### Magbigay ng Konteksto
Mas mahusay na gumaganap ang mga modelo kapag alam nila ang tungkulin, madla, at layunin.
**Walang konteksto:**
> "Magsulat ng isang function upang pagbukud-bukurin ang isang listahan."
**Na may konteksto:**
> "Ikaw ay isang senior na developer ng Python. Sumulat ng isang function upang pagbukud-bukurin ang isang listahan ng mga diksyunaryo sa pamamagitan ng isang ibinigay na key. Gumamit ng mga pahiwatig ng uri at pangasiwaan ang mga edge case. Ang madla ay mga junior developer."
### Gumamit ng Mga Positibong Tagubilin
Sabihin sa modelo kung ano ang dapat gawin, hindi kung ano ang dapat iwasan. Ang "Huwag magsama ng jargon" ay mas mahina kaysa sa "Gumamit ng simpleng wika na naa-access ng isang 10 taong gulang."
---

## Mga Prompt Structure
### Mga Tungkulin ng System / User / Assistant
Karamihan sa mga LLM API ay sumusuporta sa isang multi-turn na istraktura:
- **System message**: Itinatakda ang gawi, persona, at mga hadlang ng modelo (nagpapatuloy sa buong session).
- **Mensahe ng user**: Ang kasalukuyang query o pagtuturo.
- **Mensahe ng Assistant**: Ang mga nakaraang tugon ng modelo (ginamit para sa pagpapatuloy).
**Halimbawa (Estilo ng OpenAI API):**
System: Isa kang matulunging coding assistant. Tumugon ka nang may maigsi na mga halimbawa ng code at maikling paliwanag. Huwag kailanman magbigay ng hindi ligtas na code.
User: Sumulat ng Python function para mag-download ng file mula sa isang URL.
### Few-Shot Prompting
Magbigay ng 2–3 halimbawa ng gustong format ng input-output bago hilingin sa modelo na gawin ang gawain. Itinuturo nito ang pattern.
**Halimbawa:**
User: I-convert ang mga pangungusap na ito sa passive voice:
Input: Hinabol ng pusa ang daga.
Output: Ang daga ay hinabol ng pusa.
Input: Nagluto ang chef ng pagkain.
Output: Ang pagkain ay niluto ng chef.
Input: Sinira ng bagyo ang bahay.
Output: (nakumpleto ang modelo)
### Chain-of-Thought (CoT)
Hikayatin ang modelo na ipakita ang pangangatuwiran nito nang sunud-sunod. Pinapabuti nito ang katumpakan sa mga gawain sa aritmetika, lohika, at maraming hakbang.
**Walang CoT:**
> "Ano ang 24 × 37?"
**May CoT:**
> "Kalkulahin ang 24 × 37. Ipakita ang iyong pangangatuwiran nang sunud-sunod."
Ang modelo ay gagawa ng mga intermediate na hakbang, na binabawasan ang mga error sa aritmetika.
### Mga Structured Output
Humiling ng partikular na format tulad ng JSON, YAML, o mga markdown na talahanayan upang gawing maaasahan ang pag-parse.
User: Maglista ng tatlong kalamangan at tatlong kahinaan ng mga microservice. Ibalik lamang ang isang wastong JSON object na may mga key na "pros" at "cons", bawat isa ay isang array ng mga string.
---

## Mga Advanced na Teknik
### Self-Consistency
Bumuo ng maraming tugon para sa parehong prompt (na may temperatura > 0) at kumuha ng mayoryang boto sa huling sagot. Ito ay lalong epektibo para sa mga gawain sa pangangatwiran.
### Tree-of-Thoughts
Galugarin ang maraming mga landas sa pangangatwiran nang magkatulad, suriin ang bawat isa, at piliin ang pinakamahusay. Isa itong diskarte sa antas ng pananaliksik ngunit maaaring tantiyahin sa pamamagitan ng pagtatanong sa modelo na "tuklasin ang mga alternatibong solusyon."
### ReAct (Reasoning + Acting)
Hayaang isama ng modelo ang pangangatwiran sa mga tawag sa tool. Maaari itong mag-isip, pagkatapos ay kumilos (hal., maghanap sa web, magpatakbo ng code), pagkatapos ay mag-isip muli batay sa resulta.
**Maagap na istraktura:**
Mayroon kang access sa isang calculator at isang search engine. Para sa bawat hakbang, output:
Pag-iisip: (ang iyong pangangatwiran)
Pagkilos: (pangalan ng tool, input)
Pagmamasid: (output ng tool)
... magpatuloy hanggang sa makuha mo ang huling sagot.
### Persona Assignment
Magtalaga ng isang partikular na persona upang i-frame ang tugon.
**Mga Halimbawa:**
- "Ikaw ay isang Linux kernel developer na nagpapaliwanag ng memory management sa isang bagong graduate."
- "Ikaw ay isang palakaibigang nutrisyunista na nagbibigay ng pangkalahatang payo sa isang kliyente."
- "Ikaw ay isang mapang-uyam na kritiko ng tech na nagsusuri ng bagong gadget."
---

## Pag-tune ng Parameter
- **Temperatura** (0.0 – 1.0+): Kinokontrol ang randomness. Mas mababa = mas deterministiko, mas mataas = mas malikhain. Gumamit ng 0.0–0.3 para sa mga makatotohanang sagot; 0.7–1.0 para sa malikhaing pagsulat.
- **Top-p** (nucleus sampling): Pinutol ang probability mass sa isang partikular na pinagsama-samang threshold. 0.9 ay nangangahulugang ang mga sample ng modelo mula sa nangungunang 90% ng malamang na mga token. Karaniwang ayusin ang alinman sa temperatura o top-p, hindi pareho.
- **Max token**: Itinatakda ang maximum na haba ng output. Tandaan na magreserba ng espasyo para sa tugon sa loob ng window ng konteksto.
- **Frequency penalty**: Binabawasan ang pag-uulit ng parehong mga token.
- **Presence penalty**: Hinihikayat ang modelo na magpakilala ng mga bagong paksa.
---

## Mga Karaniwang Pitfalls at Pag-aayos
| Problema | Malamang na sanhi | Ayusin |
|---------|--------------|-----|
| Binabalewala ng modelo ang mga bahagi ng prompt | Masyadong mahaba o overloaded | Paikliin; ilagay ang pinakamahalagang pagtuturo sa dulo |
| Masyadong verbose ang output | Walang limitasyon sa haba | Magdagdag ng "Limit sa 3 pangungusap" o magtakda ng max_tokens |
| Masyadong maikli ang output | Masyadong mahigpit | Magdagdag ng "Ipaliwanag nang detalyado" o babaan ang temperatura |
| Makatotohanang mga guni-guni | Hindi sapat na konteksto o hindi maliwanag na tanong | Idagdag ang "Kung hindi ka sigurado, sabihin ang 'Hindi ko alam'" at magbigay ng kontekstong RAG |
| Hindi pare-pareho ang pag-format | Walang tahasang pagtuturo ng format | Humingi ng JSON, markdown table, o bullet list |
| Mga sagot sa modelo sa maling wika | Walang pagtuturo ng wika | Tahasang sabihin ang "Tumugon sa Ingles" (o ang iyong target na wika) |
---

## Mga Prompt na Template para sa Mga Karaniwang Gawain
### Pagbubuod
Ibuod ang sumusunod na teksto sa 3 bullet point. Tumutok sa mga pangunahing argumento at iwasan ang mga detalye.
Teksto: [insert text]

### Pagbuo ng Code
Sumulat ng function na [wika] na [ginagawa ang X].
Mga kinakailangan:
Gumamit ng mga pahiwatig ng uri.
Magsama ng docstring.
Pangasiwaan ang mga case sa gilid: [listahan].
Huwag gumamit ng mga panlabas na aklatan maliban kung tinukoy.

### Paliwanag
Ipaliwanag ang [konsepto] sa isang [hindi eksperto / estudyante sa unibersidad / bata]. Gumamit ng pagkakatulad kung naaangkop.
### Brainstorming
Bumuo ng 10 ideya para sa [paksa]. Para sa bawat ideya, magbigay ng isang paglalarawan ng isang pangungusap at isang potensyal na hamon.
text
### Pag-uuri
Uriin ang sumusunod na feedback ng customer bilang [positibo, neutral, negatibo].
Magbigay ng marka ng kumpiyansa (0-100) at maikling dahilan.
Feedback: [insert text]
### Pagsasalin na may Estilo
Isalin ang sumusunod na tekstong Ingles sa Espanyol. Gumamit ng impormal na tono na angkop para sa isang post sa social media.
Teksto: [insert text]
---

## Pagsusuri ng mga Prompt
Tratuhin ang mga prompt bilang code: i-version ang mga ito, subukan ang mga ito, at ulitin.
- **A/B test** iba't ibang prompt na variant sa isang hold-out na hanay ng mga query.
- **Sukatin ang tagumpay** sa pamamagitan ng pagsusuri ng tao o mga automated na sukatan (hal., eksaktong tugma, BLEU, custom na pagmamarka).
- **Panatilihin ang isang prompt registry** (isang simpleng text file o spreadsheet) na may prompt, bersyon, at naobserbahang pagganap.
---