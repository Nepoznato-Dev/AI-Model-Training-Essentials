---
# Metadata
title: "Accessibility and Inclusive Design"
description: "WCAG, inclusive UX, assistive technology, accessible coding"
category: "Coding and Technology"
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
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [accessibility, inclusive, design, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Accessibility at Inclusive Design
Ang pagiging naa-access (kadalasang dinadaglat bilang a11y) ay ang kasanayan sa paggawa ng software na magagamit ng lahat — kabilang ang mga taong may kapansanan sa visual, auditory, motor, cognitive, at neurological. Ito ay isang legal na kinakailangan sa maraming hurisdiksyon at isang karaniwang kasanayan sa engineering. Ang naa-access na software ay mas mahusay na software para sa lahat, dahil ang mga desisyon sa disenyo na sumusuporta sa mga hindi pinaganang user — malinaw na istraktura, nabigasyon sa keyboard, sapat na kaibahan, nababasang teksto — ay nagpapahusay sa karanasan para sa lahat ng mga user.
---

## Sino ang Nakikinabang sa Accessibility?
| Uri ng Kapansanan | Mga halimbawa | Pantulong na Teknolohiya |
|----------------|----------------------|---------------------|
| **Visual** | Pagkabulag, mahinang paningin, pagkabulag ng kulay | Mga screen reader (JAWS, NVDA, VoiceOver); mga magnifier; high-contrast na mga mode |
| **Auditory** | Bingi, hirap sa pandinig | Mga caption; mga transcript; visual na alerto |
| **Motor** | Limitadong kagalingan ng kamay, paralisis, panginginig | Keyboard-only nabigasyon; kontrol ng boses; lumipat ng mga aparato; pagsubaybay sa mata |
| **Cognitive** | Dyslexia, ADHD, autism, mga kapansanan sa memorya | Malinaw na wika; pare-parehong nabigasyon; pinababang mga distractions |
| **Pansamantala** | Sirang braso, maliwanag na sikat ng araw, maingay na kapaligiran | Parehong mga kaluwagan sa mga permanenteng kapansanan |
| **Situasyonal** | Hawak ang isang sanggol, nagmamaneho, ang isang kamay ay okupado | Mga interface ng boses; malalaking touch target |
**Pangunahing insight**: ang mga feature ng pagiging naa-access na idinisenyo para sa mga user na may kapansanan ay nakakatulong sa lahat. Ang mga curb cut (rampa sa mga bangketa) ay idinisenyo para sa mga wheelchair ngunit ginagamit ng mga magulang na may mga stroller, mga delivery worker na may mga cart, at mga manlalakbay na may mga bagahe.
---

## Web Accessibility (WCAG)
Ang Web Content Accessibility Guidelines (WCAG) ay ang internasyonal na pamantayan para sa web accessibility.
### Mga Prinsipyo ng WCAG (POUR)
| Prinsipyo | Kinakailangan |
|-----------|-------------|
| **Makikita** | Dapat na presentable ang impormasyon sa mga paraan na makikita ng mga user (mga alternatibo sa text, mga caption, naaangkop na layout) |
| **Maaandar** | Ang interface ay dapat na navigable at magagamit (keyboard accessible, sapat na oras, walang seizure-inducing content) |
| **Maiintindihan** | Ang impormasyon at pagpapatakbo ay dapat na maunawaan (nababasa, nahuhulaan, tulong sa pag-input) |
| **Matatag** | Ang nilalaman ay dapat gumana sa kasalukuyan at hinaharap na mga teknolohiyang pantulong |
### Mga Antas ng Pagsunod ng WCAG
| Antas | Mga Kinakailangan | Karaniwang Target |
|-------|-------------|----------------|
| **A** | Pinakamababang antas; 30 pamantayan sa tagumpay | Legal na minimum sa ilang hurisdiksyon |
| **AA** | Tinutugunan ang mga pinakakaraniwang hadlang | Karaniwang target para sa karamihan ng mga organisasyon |
| **AAA** | Pinakamataas na antas; hindi lahat ng nilalaman ay makakamit ito | Espesyal na nilalaman; pang-edukasyon na mga site |
### Pangunahing Pamantayan sa Tagumpay (AA Level)
| Pamantayan | Kinakailangan | Paano Makamit |
|-----------|-------------|--------------|
| **1.1.1 Nilalaman na hindi teksto** | Ang lahat ng mga larawan ay may mga kahalili sa teksto |  Mga katangian ng `alt`; `aria-label`para sa mga icon |
| **1.3.1 Impormasyon at mga relasyon** | Structure conveyed programmatically | Semantic HTML; mga pamagat; mga listahan; mga palatandaan |
| **1.4.3 Contrast (minimum)** | Ang text ay may contrast ratio na hindi bababa sa 4.5:1 | Subukan gamit ang mga contrast checker; pumili ng mga naa-access na palette ng kulay |
| **1.4.4 Baguhin ang laki ng teksto** | Maaaring baguhin ang laki ng teksto sa 200% nang walang pagkawala | Gumamit ng mga kamag-anak na yunit (rem, em); tumutugon na disenyo |
| **2.1.1 Keyboard** | Available ang lahat ng functionality sa pamamagitan ng keyboard | Walang mga traps sa keyboard; nakikitang mga tagapagpahiwatig ng focus |
| **2.4.3 Pagkakasunod-sunod ng focus** | Ang pagkakasunud-sunod ng pokus ay nagpapanatili ng kahulugan at kakayahang magamit | Lohikal na pagkakasunud-sunod ng tab; Ang order ng DOM ay tumutugma sa visual na order |
| **2.4.7 Nakikita ang focus** | Ang focus sa keyboard ay biswal na ipinahiwatig | CSS`:focus-visible`estilo; hindi kailanman`outline: none`nang walang kapalit |
| **3.3.2 Mga label o tagubilin** | Ang mga input ay may mga label | `<label>`elemento; `aria-label`|
| **4.1.2 Pangalan, tungkulin, halaga** | Ang mga bahagi ng UI ay may naa-access na mga pangalan at tungkulin | Mga katangian ng ARIA; semantikong HTML |
---

## ARIA (Accessible Rich Internet Applications)
Nagdaragdag ang ARIA ng impormasyon sa pagiging naa-access sa mga elemento ng HTML na walang built-in na semantics.
### Mga Tungkulin ng ARIA
| Tungkulin | Layunin | Halimbawa |
|------|---------|---------|
| `button`| Kinikilala ang isang elemento bilang isang pindutan | Isang`<div>`na naka-istilo bilang isang button |
| `dialog`| Modal o di-modal na dialog | Mga custom na bahagi ng modal |
| `tablist`/`tab`/`tabpanel`| Interface ng tab | Mga bahagi ng custom na tab |
| `alert`| Mahalagang mensahe na dynamic na lumalabas | Mga abiso ng error |
| `progressbar`| Tagapagpahiwatig ng pag-unlad | Naglo-load ng mga estado |
| `menu`/`menuitem`| Pag-navigate sa menu | Mga dropdown na menu |
### Mga Katangian ng ARIA
| Katangian | Layunin | Halimbawa |
|-----------|---------|---------|
| `aria-label`| Naa-access na pangalan kapag walang nakikitang text | Icon-only na button:`aria-label="Search"`|
| `aria-describedby`| Iniuugnay ang elemento sa paglalarawan nito | Field ng form na may text ng tulong |
| `aria-expanded`| Isinasaad kung ang isang seksyon ay pinalawak | Akordyon; dropdown |
| `aria-hidden`| Itinatago ang elemento mula sa pantulong na teknolohiya | Mga icon na pampalamuti |
| `aria-live`| Nag-aanunsyo ng mga pagbabago sa dynamic na nilalaman | Mga live na update; mga abiso |
| `aria-disabled`| Isinasaad na hindi pinagana ang elemento | Mga naka-grey na button |
### Ang Unang Panuntunan ng ARIA
> **Huwag gumamit ng ARIA kung maaari mong gamitin sa halip ang katutubong HTML.** Ang isang`<button>`ay naa-access na. Hinihiling sa iyo ng`<div role="button">`na manu-manong magdagdag ng paghawak sa keyboard, pamamahala ng focus, at suporta sa screen reader. Gamitin muna ang semantic HTML; ARIA lang kapag hindi kayang gawin ng mga katutubong elemento ang trabaho.
---

## Keyboard Navigation
| Susi | Inaasahang Gawi |
|------|-------------------|
| **Tab** | Ilipat ang focus sa susunod na interactive na elemento |
| **Shift + Tab** | Ilipat ang focus sa nakaraang interactive na elemento |
| **Enter / Space** | I-activate ang nakatutok na elemento (button, link) |
| **Mga arrow key** | Mag-navigate sa loob ng mga bahagi (menu, tab, radio group) |
| **Takasan** | Isara ang isang dialog, menu, o popover |
| **Home / End** | Tumalon sa una / huling item sa isang listahan |
### Mga Karaniwang Traps sa Keyboard
| Problema | Ayusin |
|---------|-----|
| Ang focus ay pumapasok sa isang bahagi ngunit hindi makaalis | Tiyaking inilalabas ng Tab ang focus; hawakan ang Escape |
| Modal ay hindi bitag focus | Dapat umikot ang focus sa loob ng modal; bumalik sa trigger sa malapit |
| Ang mga custom na bahagi ay hindi tumutugon sa keyboard | Magdagdag ng mga tagapangasiwa ng keydown para sa Enter, Space, mga arrow |
---

## Kulay at Visual na Disenyo
| Patnubay | Kinakailangan |
|-----------|-------------|
| **Contrast ratio** | 4.5:1 para sa normal na teksto; 3:1 para sa malaking text (18pt+ o 14pt+ bold) |
| **Huwag umasa sa kulay lamang** | Gumamit ng mga icon, teksto, o mga pattern bilang karagdagan sa kulay |
| **Mga indicator ng focus** | Palaging nakikita; mataas na kaibahan; hindi kailanman tinanggal nang walang kapalit |
| **Pagbabago ng laki ng teksto** | Dapat gumana ang layout sa 200% zoom |
| **Tumugon** | Dapat mag-reflow ang content sa 320px na lapad (mobile) |
### Mga Pagsasaalang-alang sa Color Blindness
| Uri | Mga Apektadong Kulay | Tip sa Disenyo |
|------|-----------------|------------|
| **Deuteranopia** | Pula-berde (pinakakaraniwan) | Huwag gumamit ng pula/berde upang ihatid ang katayuan; gumamit ng mga icon + kulay |
| **Protanopia** | Pula-berde | Pareho sa itaas |
| **Tritanopia** | Asul-dilaw | Huwag gumamit ng asul/dilaw bilang nag-iisang pagkakaiba |
---

## Pagsubok sa Accessibility
| Paraan | Tool | Ano ang Nahuhuli Nito |
|--------|------|----------------|
| **Awtomatikong pag-scan** | palakol, Parola, AWAY | Nawawalang alt text; mga isyu sa kaibahan; Mga error sa ARIA |
| **Pagsusuri sa keyboard** | Manual: tanggalin sa saksakan ang mouse, gamitin lamang ang keyboard | Pagkakasunud-sunod ng pagtuon; mga bitag sa keyboard; nawawalang mga handler |
| **Pagsubok sa screen reader** | NVDA (libre), VoiceOver (macOS), JAWS | Nawawalang mga label; mahinang istraktura; hindi ipinaalam na mga pagbabago |
| **Pagsubok sa pag-zoom** | Browser zoom sa 200%, 400% | Pagkasira ng layout; pinutol na teksto; mga isyu sa overflow |
| **Contrast ng kulay** | WebAIM contrast checker, Stark plugin | Hindi sapat na contrast ratio |
| **Pagsubok ng user** | Subukan sa mga may kapansanan na user | Mga real-world na hadlang na nakakaligtaan ng mga awtomatikong tool |
---

## Mga Legal na Kinakailangan
| Batas | Rehiyon | Mga Kinakailangan |
|-----|--------|--------------|
| **ADA** (Americans with Disabilities Act) | USA | Ang mga website ng mga pampublikong akomodasyon ay dapat ma-access |
| **Seksyon 508** | USA (pederal) | Ang ICT ng mga pederal na ahensya ay dapat ma-access |
| **EAA** (European Accessibility Act) | EU (2025+) | Dapat matugunan ng mga produkto at serbisyo ang mga kinakailangan sa pagiging naa-access |
| **EN 301 549** | EU | Teknikal na pamantayan para sa ICT accessibility |
| **ACA** (Accessibility Canada Act) | Canada | Pamahalaan at kinokontrol na mga industriya |
| **Equality Act 2010** | UK | Ang mga service provider ay dapat gumawa ng mga makatwirang pagsasaayos |
---

## Mobile Accessibility
| Platform | Mga Alituntunin | Mga Pangunahing Kasangkapan |
|----------|-----------|-----------|
| **iOS** | Mga Alituntunin ng Apple Human Interface (Seksyon ng Accessibility) | VoiceOver; Dynamic na Uri; Switch Control |
| **Android** | Mga alituntunin sa Accessibility ng Android | TalkBack; Switch Access; Piliin upang Magsalita |
| Pag-aalala sa Mobile | Solusyon |
|--------------|----------|
| **Touch target** | Minimum na 44×44 puntos (iOS) / 48×48 dp (Android) |
| **Suporta sa screen reader** | Mga paglalarawan ng nilalaman; mga label ng pagiging naa-access |
| **Pagiging sensitibo sa paggalaw** | Igalang ang`prefers-reduced-motion`; iwasan ang awtomatikong paglalaro ng mga animation |
| **Dynamic na sukat ng text** | Mga laki ng font ng system ng suporta; gumamit ng mga nasusukat na unit ng teksto |
---

## Buod
Ang pagiging naa-access ay isang prinsipyo ng disenyo na dapat ipaalam sa bawat desisyon mula sa simula, hindi isang tampok na idinagdag sa dulo. Gumamit ng semantic HTML. Tiyaking gumagana ang keyboard navigation. Panatilihin ang sapat na contrast ng kulay. Magbigay ng mga alternatibong teksto para sa nilalamang hindi teksto. Subukan sa mga screen reader at may kapansanan na user. Ang resulta ay software na mas mahusay na gumagana para sa lahat — kabilang ang mga may pansamantalang kapansanan, mga limitasyon sa sitwasyon, mas lumang mga device, mabagal na koneksyon, at ang maraming paraan kung saan naiiba ang paggamit sa totoong mundo sa isang kontroladong development environment.