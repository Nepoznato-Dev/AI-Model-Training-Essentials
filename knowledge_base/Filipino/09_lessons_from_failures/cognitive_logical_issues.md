<!--
---
# Metadata
title: "Cognitive Biases and Logical Fallacies"
description: "Reasoning errors and cognitive biases"
category: "Lessons from Failures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cognitive, logical, issues, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "27 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Mga Cognitive Biases at Logical Fallacies
Pinagsasama-sama ng dokumentong ito ang mga cognitive bias, lohikal na kamalian, at mga error sa pangangatwiran na nakakaapekto sa paggawa ng desisyon ng tao at mga output ng AI system.
---

## Mga Cognitive Bias
Ang mga cognitive bias ay mga sistematikong pattern ng paglihis mula sa rasyonalidad sa paghatol at paggawa ng desisyon. Sa software development at AI system, ang mga ito ay maaaring humantong sa mga mahihirap na desisyon sa disenyo, mga may depektong kinakailangan, at bias na pag-uugali ng modelo.
### Pagkiling sa Pagkumpirma
**Ano Ito:** Ang hilig na maghanap, magbigay-kahulugan, at mag-alaala ng impormasyon sa paraang nagpapatunay sa mga dati nang paniniwala.
**Masamang Halimbawa sa Pag-unlad:**```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    return "O(n log n)"  # Wrong conclusion
```

**Sa Mga Pagsusuri sa Code:**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**Pagbabawas:**
- Aktibong humanap ng nagpapatunay na ebidensya
- Gumamit ng blind code review
- Hikayatin ang mga hindi sumasang-ayon na opinyon
- Idokumento ang mga pagpapalagay nang tahasan
### Naka-angkla na Bias
**Ano Ito:** Masyadong umaasa sa unang piraso ng impormasyong nakatagpo.
**Masama Halimbawa:**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**Pagbabawas:**
- Kumuha ng maramihang mga independiyenteng pagtatantya
- Gumamit ng planning poker para sa pagtatantya
- Isaalang-alang ang mga saklaw sa halip na mga pagtatantya ng punto
- Reference historical data
### Pagkakamali sa Gastos ng Lubog
**Ano Ito:** Pagpapatuloy ng isang pagsisikap dahil sa dating namuhunan na mga mapagkukunan (oras, pera, pagsisikap), kahit na ang pag-abandona ay mas mabuti.
**Masama Halimbawa:**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**Pagbabawas:**
- Suriin ang mga desisyon batay sa halaga sa hinaharap, hindi nakaraang pamumuhunan
- Regular na muling suriin ang posibilidad ng proyekto
- Lumikha ng sikolohikal na kaligtasan para sa pag-pivot
- Gumamit ng layunin na pamantayan para sa magpatuloy/itigil na mga desisyon
### Availability Heuristic
**Ano Ito:** Pag-overestimate sa kahalagahan ng impormasyon na madaling makuha o kamakailan.
**Masama Halimbawa:**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**Pagbabawas:**
- Gumamit ng data-driven na paggawa ng desisyon
- Kumonsulta sa mga komprehensibong modelo ng pagbabanta
- Tingnan ang mga base rate at istatistika
- Iwasan ang reency bias sa prioritization
### Dunning-Kruger Effect
**Ano Ito:** Ang mga taong may mababang kakayahan sa isang gawain ay nagpapalaki sa kanilang kakayahan; maaaring maliitin ng mga eksperto ang kanila.
**Masama Halimbawa:**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**Pagbabawas:**
- Hikayatin ang patuloy na pag-aaral
- Ipatupad ang mga proseso ng peer review
- Lumikha ng mga programa sa pagtuturo
- Pagyamanin ang pagpapakumbaba at pagkamausisa
---

## Logical Fallacies
Ang mga lohikal na kamalian ay mga pagkakamali sa pangangatwiran na sumisira sa bisa ng argumento. Ang mga modelo ng AI ay maaaring gumawa ng mga output na naglalaman ng mga kamalian na ito.
### Ad Hominem (Atake Laban sa Tao)
**Ano Ito:** Pag-atake sa taong gumagawa ng argumento kaysa sa argumento mismo.
**Masama Halimbawa:**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**Why It's Bad:** Ang validity ng feedback ay nakadepende sa content nito, hindi sa seniority ng reviewer.
### Apela sa Awtoridad
**Ano Ito:** Ang pag-claim ng isang bagay ay totoo dahil sinasabi ito ng isang awtoridad, nang walang ebidensya.
**Masama Halimbawa:**```markdown
"This architecture must be correct because Google uses it."
```

**Bakit Masama:** Ang gumagana para sa Google sa kanilang sukat ay maaaring hindi gumana para sa iyong kaso ng paggamit.
### Maling Dichotomy (Black-and-White Thinking)
**Ano Ito:** Nagpapakita lamang ng dalawang opsyon kapag mayroon pa.
**Masama Halimbawa:**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**Reality:** Maraming opsyon ang umiiral sa pagitan ng mga sukdulang ito (i-optimize ang maiinit na landas, gamitin ang Rust para sa mga partikular na bahagi, pagbutihin ang Python code, atbp.)
### Madulas na Slope
**Ano Ito:** Ang pagtatalo na ang isang kaganapan ay tiyak na hahantong sa isang hanay ng mga negatibong kahihinatnan.
**Masama Halimbawa:**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**Bakit Masama:** Ipinapalagay ang hindi maiiwasang pag-unlad nang walang ebidensya; binabalewala ang mga nagpapagaan na kadahilanan.
### Circular Reasoning
**Ano Ito:** Gamit ang konklusyon bilang premise.
**Masama Halimbawa:**```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc (Maling Dahilan)
**Ano Ito:** Ipagpalagay na dahil sinundan ni B ang A, naging sanhi si A ng B.
**Masama Halimbawa:**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**Reality:** Ang ugnayan ay hindi nagpapahiwatig ng sanhi. Ang iba pang mga kadahilanan ay maaaring maging responsable.
### Straw Man
**Ano Ito:** Maling pagkatawan sa argumento ng isang tao upang gawing mas madali ang pag-atake.
**Masama Halimbawa:**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### Bandwagon Fallacy
**Ano Ito:** Ang pagtatalo ng isang bagay ay tama dahil maraming tao ang naniniwala dito.
**Masama Halimbawa:**```markdown
"Everyone is using Kubernetes, so we should too."
```

**Bakit Masama:** Hindi ginagarantiyahan ng kasikatan ang pagiging angkop para sa iyong mga partikular na pangangailangan.
---

## Mga Pagkabigo sa Pangangatwiran sa AI
### Mga Multi-Step Logic Error
**Masama Halimbawa:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**Bakit Masama:**
- Nagsasagawa ng kamalian ng pagpapatibay sa kahihinatnan
- Si Alice ay maaaring magsulat ng code nang hindi isang programmer
- Lohikal na istraktura: (P→Q, Q) ⊬ P
**Tamang Pangangatwiran:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### Mga Pagkabigo sa Mathematical Reasoning
**Masama Halimbawa:**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**Reality:** Kung ang bola ay nagkakahalaga ng $0.10 at ang paniki ay nagkakahalaga ng $1 pa ($1.10), ang kabuuan ay magiging $1.20. Ang tamang sagot ay $0.05 para sa bola at $1.05 para sa paniki.
### Mga Dahilan na Error sa Pangangatwiran
**Masama Halimbawa:**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**Reality:** Parehong sanhi ng ikatlong salik (mainit na panahon), hindi ng isa't isa.
---

## Mga Istratehiya para sa Pagpapabuti
### Para sa Paggawa ng Desisyon ng Tao
1. **Pagsasanay sa Kamalayan**: Matutong kilalanin ang mga karaniwang bias
2. **Paggamit ng Checklist**: Gumamit ng mga checklist ng desisyon upang malabanan ang mga bias
3. **Diverse Team**: Isama ang mga taong may iba't ibang pananaw
4. **Pre-mortems**: Isipin ang pagkabigo at magtrabaho pabalik upang matukoy ang mga sanhi
5. **Dokumentasyon**: Magtala ng pangangatwiran para sa pagsusuri sa ibang pagkakataon
### Para sa AI Systems
1. **Chain-of-Thought Prompting**: Hilingin sa modelo na magpakita ng mga hakbang sa pangangatwiran
2. **Pagwawasto sa Sarili**: Ipasuri ang modelo at punahin ang mga sagot nito
3. **Pormal na Pag-verify**: Gumamit ng mga tool sa simbolikong pangangatwiran para sa kritikal na lohika
4. **Decomposition**: Hatiin ang mga kumplikadong problema sa mas maliliit na hakbang
5. **Mga Panlabas na Tool**: Gumamit ng mga calculator at solver para sa mga mathematical na gawain
6. **Maramihang Sample**: Bumuo ng maraming tugon at ihambing
---

## Mga Kaugnay na Paksa
- **AI/LLM Failures**: Tingnan ang`ai_llm_failures.md`para sa mga guni-guni at mga isyu sa pangangatwiran
- **Mga Salungat na Pinagmumulan**: Tingnan ang dokumentasyon sa pagsusuri ng magkasalungat na impormasyon
- **Kritikal na Pag-iisip**: Ilapat ang mga konseptong ito upang suriin ang mga argumento at ebidensya
- **Prompt Engineering**: Tingnan ang`../02_artificial_intelligence/prompt_engineering.md`para sa mga diskarte upang mabawasan ang mga error sa pangangatwiran
---

## Karagdagang Mga Cognitive Biase sa Software Development
### Status Quo Bias
**Ano Ito:** Kagustuhan para sa pagpapanatili ng kasalukuyang estado; anumang pagbabago ay itinuturing na isang pagkawala.
**Masama Halimbawa:**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**Pagbabawas:**
- Tukuyin ang halaga ng hindi pagbabago
- Magtakda ng mga regular na iskedyul ng pag-upgrade
- Lumikha ng mga ligtas na kapaligiran sa pag-eksperimento
- Nagbabago ang frame bilang mga pagkakataon, hindi mga pagbabanta
### Optimismo Bias
**Ano Ito:** Minamaliit ang oras, gastos, at mga panganib habang labis na tinatantya ang mga benepisyo.
**Masama Halimbawa:**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**Pagbabawas:**
- Gumamit ng reference class forecasting (ihambing sa mga katulad na nakaraang proyekto)
- Magdagdag ng mga contingency buffer (20-50%)
- Magsagawa ng pre-mortems
- Subaybayan ang katumpakan ng pagtatantya sa paglipas ng panahon
### Pagkiling sa Survivorship
**Ano Ito:** Nakatuon sa matagumpay na mga halimbawa habang binabalewala ang mga pagkabigo.
**Masama Halimbawa:**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**Pagbabawas:**
- Pag-aralan ang parehong mga tagumpay AT kabiguan
- Maghanap ng mga batayang rate at istatistika
- Isaalang-alang ang invisible data
- Iwasan ang mga halimbawa ng pagpili ng cherry
### Pangunahing Error sa Pagpapatungkol
**Ano Ito:** Pag-uugnay sa pag-uugali ng iba sa karakter kaysa sa mga pangyayari.
**Masama Halimbawa:**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**Pagbabawas:**
- Isaalang-alang ang mga salik sa sitwasyon
- Magsanay ng empatiya
- Tumutok sa mga sistema, hindi sa mga indibidwal
- Gumamit ng walang kapintasang post-mortem
### Hindsight Bias
**Ano Ito:** Pagkatapos maganap ang isang kaganapan, sa paniniwalang ito ay mahuhulaan sa lahat ng panahon.
**Masama Halimbawa:**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**Pagbabawas:**
- Idokumento ang mga hula bago ang mga kinalabasan
- Suriin ang konteksto ng desisyon, hindi lamang ang mga resulta
- Iwasan ang "Sabi ko sa iyo" kultura
- Tumutok sa pagpapabuti ng mga proseso, hindi pagtatalaga ng sisihin
---

## Higit pang Logical Fallacies
### Apela sa Novelty
**Ano Ito:** Ipagpalagay na mas maganda ang isang bagay dahil mas bago ito.
**Masama Halimbawa:**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### Apela sa Tradisyon
**Ano Ito:** Ang pagtatalo ng isang bagay ay tama dahil palagi itong ginagawa sa ganoong paraan.
**Masama Halimbawa:**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (Apela sa Pagkukunwari)
**Ano Ito:** Tinatanggihan ang pagpuna sa pamamagitan ng pagturo sa hindi pagkakapare-pareho ng kritiko.
**Masama Halimbawa:**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### Na-load na Tanong
**Ano Ito:** Pagtatanong ng isang tanong na naglalaman ng isang palagay.
**Masama Halimbawa:**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### Walang Tunay na Scotsman
**Ano Ito:** Paggawa ng pagbubukod sa isang pangkalahatang paghahabol kapag hinamon.
**Masama Halimbawa:**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### Genetic Fallacy
**Ano Ito:** Paghuhusga sa isang bagay batay sa pinagmulan nito sa halip na kasalukuyang merito.
**Masama Halimbawa:**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### Middle Ground Fallacy
**Ano Ito:** Ipagpalagay na ang katotohanan ay palaging nasa gitna ng dalawang sukdulan.
**Masama Halimbawa:**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## Mga Cognitive Biases sa AI Systems
### Pagkiling ng Data ng Pagsasanay
Ang mga modelo ng AI ay nagmamana ng mga bias na naroroon sa kanilang data ng pagsasanay.
**Halimbawa:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**Pagbabawas:**
- Data ng pagsasanay sa pag-audit para sa mga bias
- Gumamit ng mga diskarte sa debiasing
- Pagsubok para sa mga bias na output
- Iba't ibang pangongolekta ng data
### Automation Bias
**Ano Ito:** Masyadong umaasa sa mga automated na system, kahit na mali ang mga ito.
**Halimbawa:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**Pagbabawas:**
- Panatilihin ang pangangasiwa ng tao
- Hikayatin ang kritikal na pagsusuri ng mga output ng AI
- Huwag ituring ang AI bilang hindi nagkakamali
- Ipatupad ang mga proseso ng pagsusuri
### Ilusyon ng Pag-unawa
**Ano Ito:** Naniniwalang naiintindihan mo kung paano gumagana ang AI kapag hindi mo naiintindihan.
**Halimbawa:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**Pagbabawas:**
- Turuan ang mga user tungkol sa mga limitasyon ng AI
- Maging transparent tungkol sa kung paano gumagana ang mga system
- Iwasan ang anthropomorphizing AI
- Magtakda ng naaangkop na mga inaasahan
---

## Pag-aaral ng Kaso
### Pag-aaral ng Kaso 1: Pagkiling sa Kumpirmasyon sa Pagpili ng Arkitektura
**Insidente:** Ang isang team ay pumili ng isang microservices architecture para sa isang maliit na application.
**Root Cause:** Nabasa ng lead team ang ilang artikulo na pumupuri sa mga microservice at 
humingi lamang ng impormasyong nagpapatunay sa pagpiling ito, hindi pinapansin ang mga babala tungkol sa pagiging kumplikado.
**Epekto:**
- Napakalaking overhead para sa isang pangkat ng 3 developer
- Ang pagiging kumplikado ng deployment ay tumaas ng 10x
- Bumaba ang performance dahil sa mga tawag sa network
- Naantala ang proyekto ng 6 na buwan
**Aralin:** Suriin ang mga arkitektura batay sa iyong partikular na konteksto, hindi lamang 
positibong mga testimonial. Isaalang-alang ang mga trade-off nang tahasan.
### Pag-aaral ng Kaso 2: Lumubog na Gastos sa Legacy System
**Insidente:** Nagpatuloy ang kumpanya sa pagpapanatili ng custom-built CRM sa loob ng 5 taon 
sa kabila ng mas mahusay na mga alternatibo.
**Root Cause:** "Namuhunan na kami ng $2M, hindi namin ito maaaring iwanan ngayon."
**Epekto:**
- Taunang gastos sa pagpapanatili: $500K
- Gastos ng pagkakataon: Hindi makagamit ng mga modernong feature
- Mga isyu sa pagpapanatili ng talento (nais na magtrabaho ang mga developer sa modernong teknolohiya)
- Kabuuang 5-taong gastos: $4.5M kumpara sa $1.5M para sa alternatibong SaaS
**Aralin:** Ang nakaraang pamumuhunan ay lumubog. Gumawa ng mga desisyon batay sa halaga sa hinaharap.
### Pag-aaral ng Kaso 3: Availability Heuristic sa Seguridad
**Insidente:** Inuna ng koponan ang pagtatanggol laban sa isang kamakailang naisapublikong pag-atake 
vector habang binabalewala ang mas malamang na mga banta.
**Root Cause:** Ang kamakailang saklaw ng balita ay gumawa ng isang uri ng pagbabanta na lubos na magagamit 
sa memorya, skewing risk assessment.
**Epekto:**
- Gumastos ng $100K sa pagbabawas ng mababang posibilidad na pagbabanta
- Naganap ang aktwal na paglabag sa pamamagitan ng napabayaang vector
- Gastos sa pagbawi: $500K+
**Aralin:** Gumamit ng pagmomodelo ng pagbabanta na hinihimok ng data, hindi ang reency-based na priyoridad.
---

## Mga Praktikal na Pagsasanay
### Pagsasanay sa Pagtukoy ng Bias
Suriin ang mga kamakailang desisyon at itanong:
1. Anong mga pagpapalagay ang ginawa natin?
2. Anong ebidensiya ang sasalungat sa ating konklusyon?
3. Isinaalang-alang ba natin ang maraming mga opsyon o anchor sa unang ideya?
4. Nagpapatuloy ba tayo dahil sa future value o past investment?
5. Ano ang aming irerekomenda kung may magtanong sa amin?
### Logical Fallacy Spotting
Magsanay sa pagtukoy ng mga kamalian sa pang-araw-araw na talakayan:
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### Pre-Mortem Technique
Bago simulan ang isang proyekto:
1. Isipin na ito ay 6 na buwan sa hinaharap
2. Ang proyekto ay nabigo nang husto
3. Isulat ang kuwento kung bakit ito nabigo
4. Trabaho pabalik upang maiwasan ang mga mode ng pagkabigo
Sinasalungat nito ang optimism bias at availability heuristic.
---

## Mga Tool at Framework
### Template ng Decision Journal
```markdown
Date: [When]
Decision: [What we decided]
Context: [Situation and constraints]
Options Considered: [Alternatives evaluated]
Expected Outcome: [What we think will happen]
Confidence Level: [How sure we are]
Review Date: [When to revisit]

[Later] Actual Outcome: [What actually happened]
Lessons Learned: [What we'd do differently]
```

### Checklist ng Bias
Bago gumawa ng mahahalagang desisyon:
- [ ] Naghanap ba tayo ng hindi nagpapatunay na ebidensya?
- [ ] Naka-angkla ba tayo sa paunang impormasyon?
- [ ] Naiimpluwensyahan ba tayo ng sunk cost?
- [ ] Masyado ba tayong kumpiyansa sa ating mga pagtatantya?
- [ ] Isinaalang-alang ba natin ang mga batayang rate?
- [ ] Nahuhulog ba tayo sa pagiging available/recency bias?
- [ ] Gagawin ba natin ang parehong pagpipilian kung magsisimula ng bago?
### Red Team Exercise
Magtalaga ng isang tao na makipagtalo laban sa iminungkahing desisyon:
- Ang kanilang tungkulin ay maghanap ng mga bahid
- Dapat silang magpakita ng mga alternatibong pananaw
- Nakabubuo ang mga kasanayan ng pangkat na tumugon sa mga kritisismo
- Idokumento ang mga alalahanin na iniharap at natugunan
Sinasalungat nito ang bias sa pagkumpirma at groupthink.