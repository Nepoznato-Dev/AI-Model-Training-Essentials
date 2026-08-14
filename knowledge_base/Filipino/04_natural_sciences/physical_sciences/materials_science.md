<!--
---
# Metadata
title: "Materials Science"
description: "Crystal structures, polymers, alloys, semiconductors, nanomaterials"
category: "Natural Sciences"
subcategory: "Physical Sciences"
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
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to physical_sciences/ subfolder; added subcategory field"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [materials, science, natural-sciences]
difficulty_level: "beginner"
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
# Materials Science
Ang agham ng mga materyales ay ang pag-aaral kung paano tinutukoy ng istruktura ng isang materyal (sa atomic, microscopic, at macroscopic scale) ang mga katangian nito, at kung paano magagamit ang mga pamamaraan sa pagpoproseso upang kontrolin ang istrukturang iyon upang makamit ang ninanais na pagganap. Ito ang larangan na sumasagot sa mga tanong tulad ng: bakit malakas ngunit mabigat ang bakal? Bakit ang salamin ay transparent ngunit malutong? Paano tayo makakagawa ng mga baterya na mas mabilis mag-charge? Anong mga materyales ang makakaligtas sa mga kondisyon sa Mars? Ang bawat piraso ng teknolohiya na iyong ginamit ay gawa sa mga materyales, at ang mga pag-unlad sa teknolohiya ay halos palaging nangangailangan ng mga pag-unlad sa mga materyales.
---

## Ang Materials Science Tetrahedron
Ang apat na magkakaugnay na elemento na tumutukoy sa field:
| Elemento | Paglalarawan |
|---------|-------------|
| **Istruktura** | Paano nakaayos ang mga atomo at molekula (kristal na istraktura; mga hangganan ng butil; mga depekto) |
| **Property** | Paano kumikilos ang materyal (mekanikal; elektrikal; thermal; optical; magnetic) |
| **Pinoproseso** | Paano ginawa at hinuhubog ang materyal (paghahagis; sintering; doping; annealing) |
| **Pagganap** | Paano gumagana ang materyal sa isang tunay na aplikasyon |
Ang pangunahing insight: ang pagbabago sa pagproseso ay nagbabago sa istraktura, na nagbabago sa mga katangian, na nagbabago sa pagganap.
---

## Mga Klase ng Materyales
### Pangkalahatang-ideya
| Klase | Pagbubuklod | Mga Pangunahing Katangian | Mga halimbawa |
|-------|---------|----------------|---------|
| **Mga Metal** | Metallic (delokalisado na mga electron) | Malakas; malagkit; conductive; malabo | Bakal; aluminyo; tanso; titan |
| **Mga Keramik** | Ionic / covalent | mahirap; malutong; lumalaban sa init; insulating | alumina; silikon karbid; salamin; porselana |
| **Polymer** | Covalent (chain) + van der Waals | Magaan; nababaluktot; insulating; mababang punto ng pagkatunaw | Polyethylene; naylon; goma; epoxy |
| **Mga Komposit** | Kumbinasyon ng dalawa o higit pang mga klase | Pinasadyang mga ari-arian; mataas na lakas-sa-timbang | Carbon fiber; fiberglass; kongkreto |
| **Mga Semiconductor** | Covalent (na may kontroladong impurities) | Mahimig na kondaktibiti; batayan ng electronics | Silicon; germanyum; gallium arsenide |
| **Mga Biomaterial** | iba't-ibang; kinakailangan ang biocompatible | Makipag-ugnayan sa mga biological system | Titanium implants; collagen; hydroxyapatite |
---

## Mga Istraktura ng Kristal
### Mga Karaniwang Metallic Crystal na Structure
| Istraktura | Mga Atom bawat Unit Cell | Fraction ng Packing | Mga halimbawa |
|------------------------|--------------------|----------------|---------|
| **FCC** (Face-Centred Cubic) | 4 | 0.74 (pinakamalapit na nakaimpake) | aluminyo; tanso; ginto; nikel; austenite (γ-bakal) |
| **BCC** (Body-Centred Cubic) | 2 | 0.68 | Bakal (α-iron); kromo; tungsten; molibdenum |
| **HCP** (Hexagonal Close-Packed) | 6 | 0.74 (pinakamalapit na nakaimpake) | titan; sink; magnesiyo; kobalt |
### Bakit Mahalaga ang Crystal Structure
| Ari-arian | Impluwensya ng Crystal Structure |
|-----------|--------------------------------|
| **Lakas** | Ang mga sistema ng slip (mga eroplano kung saan dumudulas ang mga atom) ay naiiba sa istraktura; Ang mga metal ng FCC ay mas ductile kaysa sa HCP |
| **Density** | Tinutukoy ng fraction ng pag-iimpake kung gaano kahigpit ang pagkaka-pack ng mga atom |
| **Mga pagbabago sa yugto** | Nagbabago ang bakal mula sa BCC patungong FCC sa 912°C — ito ang batayan ng steel heat treatment |
| **Anisotropy** | Maaaring mag-iba ang mga katangian sa direksyon sa mga non-cubic na kristal |
---

## Mga Katangiang Mekanikal
### Mga Pangunahing Sukatan
| Ari-arian | Kahulugan | Mga Yunit | Mga Karaniwang Halaga |
|----------|-----------|-------|----------------|
| **Young's modulus (E)** | paninigas; stress / strain sa nababanat na rehiyon | GPa | Bakal: 200; Aluminyo: 70; Goma: 0.01–0.1 |
| **Lakas ng ani** | Stress kung saan nagsisimula ang permanenteng (plastic) deformation | MPa | Bakal: 250–1000; Aluminyo: 40–500 |
| **Tensile strength (UTS)** | Pinakamataas na diin bago mabigo | MPa | Bakal: 400–2000; Aluminyo: 90–600 |
| **Ductility (% elongation)** | Magkano ang isang materyal na umaabot bago masira | % | Bakal: 10–50; Salamin: <1 |
| **Katigasan** | Ang enerhiya ay hinihigop bago ang bali (lugar sa ilalim ng stress-strain curve) | MJ/m³ | Bakal: mataas; keramika: mababa |
| **Katigasan** | Paglaban sa surface indentation | Iba't ibang kaliskis | Diamond: pinakamahirap; talc: pinakamalambot |
### Mga Mekanismo ng Pagpapalakas
| Mekanismo | Paano Ito Gumagana | Halimbawa |
|-----------|-------------|---------|
| **Pagpino ng butil** | Mas maliliit na butil = mas maraming hangganan ng butil = mas mahirap para sa mga dislokasyon na ilipat | relasyong Hall-Petch |
| **Pagpapalakas ng solidong solusyon** | Binabaluktot ng mga dayuhang atomo ang sala-sala; hadlangan ang paggalaw ng dislokasyon | Pagdaragdag ng zinc sa tanso → tanso |
| **Pagpapatigas ng ulan** | Hinaharang ng maliliit na particle ang paggalaw ng dislokasyon | Pinatigas ng edad na mga aluminyo na haluang metal |
| **Pagpapatigas ng trabaho (pagpapatigas ng strain)** | Ang pagpapapangit ng plastik ay nagpapataas ng density ng dislokasyon; sila ay nagkakagulo at humahadlang sa isa't isa | Cold-rolling steel |
| **Composite strengthening** | Ang malalakas na hibla sa mas malambot na matrix ay nagdadala ng karga | Carbon fiber reinforced polimer |
---

## Mga Electrical at Thermal Property
### Electrical Conductivity
| Uri ng Materyal | Conductivity (S/m) | Mekanismo |
|--------------|--------------------|-----------|
| **Mga Konduktor** (tanso, pilak) | 10^7 – 10^8 | Libreng mga electron sa mga metal na bono |
| **Mga Semiconductor** (silicon, GaAs) | 10^-6 – 10^4 | Tunable sa pamamagitan ng doping; band gap engineering |
| **Mga Insulator** (salamin, goma) | 10^-12 – 10^-20 | Malaking banda gap; mga electron na nakatali |
| **Mga Superconductor** | Infinite (mababa sa kritikal na temperatura) | Zero electrical resistance; Meissner effect |
### Mga Thermal Property
| Ari-arian | Paglalarawan | Mahalaga Para sa |
|----------|-------------|--------------|
| **Thermal conductivity** | Gaano kahusay ang daloy ng init sa materyal | Mga paglubog ng init; pagkakabukod |
| **Thermal expansion** | Kung gaano lumalawak ang isang materyal kapag pinainit | Pagtutugma ng mga materyales sa mga composite; tulay; riles |
| **Tiyak na kapasidad ng init** | Kailangan ng enerhiya upang mapataas ang temperatura ng 1°C | Imbakan ng thermal energy |
| **Puntos ng pagkatunaw** | Temperatura kung saan ang solid ay nagiging likido | Mga application na may mataas na temperatura |
---

## Polimer
### Mga Uri ng Polimer
| Uri | Istraktura | Mga Katangian | Mga halimbawa |
|------|-----------|-----------|---------|
| **Thermoplastics** | Linear o branched chain; mahinang intermolecular na pwersa | Matunaw kapag pinainit; nare-recycle | Polyethylene; polisterin; naylon |
| **Thermoset** | Cross-linked na network; covalent bond sa pagitan ng mga chain | Huwag matunaw; mabulok sa mataas na temperatura | Epoxy; bulkanisadong goma; Bakelite |
| **Elastomer** | Banayad na cross-linked; nakapulupot na mga kadena | Mag-stretch at bumalik sa hugis | Likas na goma; silicone; neoprene |
### Mga Katangian ng Polimer
| Ari-arian | Paglalarawan |
|----------|-------------|
| **Temperatura ng paglipat ng salamin (Tg)** | Sa ibaba ng Tg: matigas at malutong. Sa itaas ng Tg: malambot at nababaluktot |
| **Crystallinity** | Ang mga semi-crystalline polymers ay mas malakas at mas malabo; amorphous ay transparent |
| **Molekular na timbang** | Mas mataas na MW = mas malakas; mas mahirap iproseso |
| **Degree ng polymerization** | Bilang ng mga yunit ng monomer; nakakaapekto sa mga ari-arian |
---

## Mga Phase Diagram
### Iron-Carbon Phase Diagram (Pinasimple)
| Yugto | Nilalaman ng Carbon | Istraktura | Mga Katangian |
|-------|----------------|-----------|-----------|
| ** Ferrite (α)** | Hanggang 0.022% | BCC na bakal | Malambot; malagkit; magnetic |
| **Austenite (γ)** | Hanggang 2.14% | FCC na bakal | Non-magnetic; mabubuo |
| **Cementite (Fe₃C)** | 6.67% | Orthorhombic | mahirap; malutong |
| **Pearlite** | 0.76% (eutectoid) | Alternating layer ng ferrite at cementite | Malakas; matigas |
| **Martensite** | Anumang (nabuo sa pamamagitan ng mabilis na pagsusubo) | BCT (body-centred tetragonal) | Napakahirap; malutong |
---

## Modern at Umuusbong na Mga Materyal
| Materyal | Paglalarawan | Application |
|----------|-------------|-------------|
| **Grapene** | Isang layer ng carbon atoms; pinakamatibay na materyal na kilala; mahusay na konduktor | Electronics; mga composite; mga sensor |
| **Mga carbon nanotube** | Mga pinagsama-samang graphene cylinder; matinding ratio ng lakas-sa-timbang | Mga komposisyon; electronics; imbakan ng enerhiya |
| **Perovskite** | Istraktura ng kristal ABX₃; mahimig na banda gap | Mga solar cell; mga LED; mga detektor |
| **Metal-organic frameworks (MOFs)** | Mga buhaghag na mala-kristal na materyales; napakalaking lugar sa ibabaw | Imbakan ng gas; catalysis; paghahatid ng gamot |
| **Mga haluang metal ng hugis** | Bumalik sa orihinal na hugis kapag pinainit | Stent; mga actuator; self-repairing structures |
| **Mga Metamaterial** | Ang inhinyero na microstructure ay nagbibigay ng mga katangiang hindi matatagpuan sa kalikasan | Negatibong refractive index; pagbabalat |
| **Mga haluang metal na may mataas na entropy** | Maramihang mga pangunahing elemento; hindi pangkaraniwang kumbinasyon ng mga katangian | Matinding kapaligiran; aerospace |
---

## Buod
Iniuugnay ng agham ng mga materyales ang atomic na istraktura ng isang materyal sa mga macroscopic na katangian nito at pagganap sa totoong mundo. Ang mga metal ay malakas at conductive ngunit mabigat. Ang mga keramika ay matigas at lumalaban sa init ngunit malutong. Ang mga polimer ay magaan at nababaluktot ngunit limitado ng temperatura. Pinagsasama ng mga composite ang pinakamahusay sa iba't ibang klase. Tinutukoy ng istraktura ng kristal ang mekanikal na pag-uugali. Pagproseso — heat treatment, alloying, work hardening — kinokontrol ang microstructure at samakatuwid ang mga katangian. Ang mga modernong materyales tulad ng graphene, perovskite, at MOF ay nagtutulak sa mga hangganan ng kung ano ang posible. Ang larangan ay pangunahing interdisiplinary: ang pisika ay nagpapaliwanag ng pagbubuklod, ang chemistry ay nagpapaliwanag ng mga reaksyon, ang engineering ay nagpapaliwanag ng pagganap, at lahat ng ito ay mahalaga para sa bawat teknolohiya mula sa mga smartphone hanggang sa spacecraft.