---
# Metadata
title: "Logic and Critical Thinking"
description: "Formal logic, logical fallacies, argument analysis, and critical thinking frameworks"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [logic, critical-thinking, fallacies, arguments, reasoning, boolean-algebra]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Lohika at Kritikal na Pag-iisip
Ang lohika ay ang pag-aaral ng wastong pangangatwiran — kung paano bumuo ng mga tamang argumento at tukuyin ang mga may depekto. Ang kritikal na pag-iisip ay ang disiplinadong ugali ng pagtatanong ng mga pagpapalagay, pagsusuri ng ebidensya, at pangangatuwirang mabuti. Ang mga kasanayang ito ay mahalaga hindi lamang sa matematika at computer science, ngunit sa araw-araw na paggawa ng desisyon, siyentipikong pananaliksik, at pag-navigate sa isang mundong mayaman sa impormasyon.
---

## Ano ang isang Argumento?
Sa lohika, ang **argument** ay isang set ng mga pahayag (premise) na nilalayon upang suportahan ang isang konklusyon.
| Bahagi | Tungkulin | Halimbawa |
|-----------|------|---------|
| **Premis** | Isang pahayag na inaalok bilang ebidensya | "Lahat ng tao ay mortal" |
| **Konklusyon** | Ang pag-angkin ng suporta sa lugar | "Si Socrates ay mortal" |
| **Paghinuha** | Ang lohikal na hakbang mula sa lugar hanggang sa konklusyon | "Si Socrates ay tao, samakatuwid..." |
### Wasto kumpara sa Tunog
| Termino | Ibig sabihin | Halimbawa |
|------|---------|---------|
| **May bisa** | Kung totoo ang premises, dapat totoo ang konklusyon | Tama ang istraktura, kahit na mali ang mga lugar |
| **Di-wasto** | Ang konklusyon ay hindi sumusunod mula sa mga lugar | Nasira ang lohikal na istraktura |
| **Tunog** | Wasto AT lahat ng lugar ay talagang totoo | Ang gintong pamantayan ng argumento |
| **Hindi maayos** | Alinman sa di-wasto o may maling lugar | Karamihan sa mga maling argumento |
---

## Mga Uri ng Pangangatwiran
| Uri | Direksyon | Lakas | Halimbawa |
|------|-----------|----------|---------|
| **Deductive** | Pangkalahatan → tiyak | Ilang (kung wasto) | "Lahat ng mammal ay may baga. Ang balyena ay mammal. Samakatuwid, ang balyena ay may baga." |
| **Inductive** | Tukoy → pangkalahatan | Malamang | "Lahat ng swan na nakita ko ay puti. Samakatuwid, lahat ng swan ay malamang na puti." |
| **Abductive** | Pagmamasid → pinakamahusay na paliwanag | Posible | "Basa ang damo. Ang pinakamagandang paliwanag ay umulan." |
---

## Lohika ng Proposisyon
Ang lohika ng proposisyon ay tumatalakay sa mga simpleng proposisyon at kung paano pinagsama ang mga ito:
### Mga Lohikal na Connective
| Nag-uugnay | Simbolo | Ibig sabihin | Kondisyon ng Katotohanan |
|-----------|--------|---------|----------------|
| **AT** | ∧ (p ∧ q) | Pang-ugnay | Tama lamang kapag pareho ang totoo |
| **O** | ∨ (p ∨ q) | Disjunction | Tama kapag kahit isa ay totoo |
| **HINDI** | ¬ (¬p) | Negasyon | Kabaligtaran na halaga ng katotohanan |
| **KUNG...TAON** | → (p → q) | Implikasyon | Mali lamang kapag p ay tama at q ay mali |
| **IFF** | ↔ (p ↔ q) | Biconditional | Tama kapag pareho ang halaga ng katotohanan ng dalawa |
### Talahanayan ng Katotohanan para sa Implikasyon (p → q)
| p | q | p → q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |
Tandaan: Ang maling premise ay ginagawang vacuously true ang implikasyon. "Kung ang buwan ay keso, kung gayon ako ang Papa" ay lohikal na totoo.
---

## Boolean Algebra
Ang Boolean algebra ay ang matematika ng true/false value at ang pundasyon ng digital circuit design at programming:
| Batas | Pagpapahayag | Ibig sabihin |
|-----|-----------|---------|
| **Commutative** | A ∧ B = B ∧ A | Hindi mahalaga ang order |
| **Associative** | (A ∧ B) ∧ C = A ∧ (B ∧ C) | Hindi mahalaga ang pagpapangkat |
| **Pamamahagi** | A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C) | AT namamahagi sa OR |
| **De Morgan's** | ¬(A ∧ B) = ¬A ∨ ¬B | Ang negation flips AT sa O |
| **De Morgan's** | ¬(A ∨ B) = ¬A ∧ ¬B | Ang negation flips O sa AT |
| **Dobleng Negasyon** | ¬(¬A) = A | Dalawang negasyon ang kinansela |
| **Pagkakakilanlan** | A ∧ T = A; A ∨ F = A | Mga elemento ng pagkakakilanlan |
| **Complement** | A ∧ ¬A = F; A ∨ ¬A = T | Kontradiksyon at tautolohiya |
---

## Mga Karaniwang Logical Fallacies
Ang pagkilala sa mga kamalian ay mahalaga para sa kritikal na pag-iisip:
### Mga Pormal na Pagkakamali (Mga Error sa Estruktura)
| Pagkakamali | Istraktura | Halimbawa |
|---------|-----------|---------|
| **Pagpapatibay sa Bunga** | Kung P ay Q. Q. Samakatuwid P. | "Kung umuulan, ang lupa ay basa. Ang lupa ay basa. Kaya't umulan." (Maaaring isang sprinkler.) |
| **Pagtanggi sa Nauna** | Kung P ay Q. Hindi P. Samakatuwid hindi Q. | "Kung umuulan, basa ang lupa. Hindi umulan. Kaya hindi basa ang lupa." |
### Mga Impormal na Pagkakamali (Mga Error sa Nilalaman)
| Pagkakamali | Paglalarawan | Halimbawa |
|---------|-------------|---------|
| **Ad Hominem** | Pag-atake sa tao, hindi ang argumento | "Hindi mo mapagkakatiwalaan ang kanyang plano sa ekonomiya - hindi siya isang ekonomista." |
| **Taong Dayami** | Maling pagkatawan ng argumento para mas madaling atakehin | "Gusto mong bawasan ang paggastos sa militar? Kaya gusto mong umalis ng bansa nang walang pagtatanggol!" |
| **Apela sa Awtoridad** | Pagbanggit sa isang awtoridad na hindi eksperto sa nauugnay na larangan | "Sinasabi ng celebrity na ito na gumagana ang diet na ito, kaya dapat itong maging epektibo." |
| **Maling Dilemma** | Nagtatanghal lamang ng dalawang pagpipilian kapag mas marami ang umiiral | "Kasama ka man o laban sa amin." |
| **Madulas na Slope** | Ang pangangatwiran na ang isang kaganapan ay tiyak na hahantong sa isang matinding kinalabasan | "If we allow this, next thing you know, total chaos." |
| **Paikot na Pangangatwiran** | Ang konklusyon ay ipinapalagay sa lugar | "Ang libro ay totoo dahil ito ay nagsasabi na ito ay totoo." |
| **Nagmamadaling Paglalahat** | Pagguhit ng malawak na konklusyon mula sa hindi sapat na ebidensya | "May nakilala akong dalawang bastos na tao mula sa lungsod na iyon. Lahat ng tao doon ay dapat bastos." |
| **Post Hoc Ergo Propter Hoc** | Ipagpalagay na sanhi mula sa temporal na pagkakasunud-sunod | "Ininom ko ang suplemento na ito at mas mabuti ang pakiramdam, kaya dapat itong gumana." |
| **Red Herring** | Ipinapakilala ang isang walang kaugnayang paksa upang makagambala | "Nagtatanong ka tungkol sa aking patakaran sa edukasyon, ngunit ang talagang mahalaga ay ang ekonomiya." |
| **Bandwagon** | May totoo dahil maraming tao ang naniniwala dito | "Lahat ay bumibili ng produktong ito, kaya dapat ito ang pinakamahusay." |
---

## Pagsusuri ng mga Argumento: Isang Checklist
| Hakbang | Tanong |
|------|----------|
| 1. **Kilalanin ang konklusyon** | Ano ang sinusubukang patunayan ng argumento? |
| 2. **Kilalanin ang lugar** | Anong ebidensya ang iniaalok? |
| 3. **Suriin ang bisa** | Ang konklusyon ba ay sumusunod mula sa lugar? |
| 4. **Suriin ang kagalingan** | Totoo ba talaga ang lugar? |
| 5. **Maghanap ng mga kamalian** | Mayroon bang mga error sa istruktura o nilalaman? |
| 6. **Isaalang-alang ang mga kontraargumento** | Anong mga pagtutol ang maaaring magkaroon? |
| 7. **Turiin ang kalidad ng ebidensya** | Ang ebidensya ba ay maaasahan, sapat, at may kaugnayan? |
---

## Bakit Ito Mahalaga
Ang lohika at kritikal na pag-iisip ay ang pundasyon ng matematika, computer science, batas, at siyentipikong pagtatanong. Sa isang mundong puno ng maling impormasyon, advertising, at mapanghikayat na retorika, ang kakayahang magsuri ng mga argumento nang mahigpit ay hindi lamang isang akademikong kasanayan — ito ay isang kasanayan sa kaligtasan. Nagde-debug ka man ng code, nagdidisenyo ng mga algorithm, o gumagawa ng mga desisyon sa buhay, ang malinaw na pangangatwiran ay naghihiwalay sa mabubuting paghuhusga mula sa masasama.