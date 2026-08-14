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
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-10"
    author: "Nepoznato-Dev"
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
# Usindikaji wa Mawimbi
Uchakataji wa mawimbi ni sayansi ya kuchanganua, kurekebisha, na kuunganisha mawimbi - uwakilishi wa kiasi halisi kinachotofautiana kulingana na wakati, nafasi au marudio. Sauti, picha, video, data ya vitambuzi, mawimbi ya ubongo, bei za hisa - zote ni mawimbi. Zana za hisabati za usindikaji wa mawimbi (Nne za kubadilisha, vichungi, nadharia ya sampuli) ni za msingi katika kujifunza kwa mashine, mawasiliano, picha za kimatibabu, na karibu kila nyanja inayofanya kazi na data.
---

## Ishara na Mifumo
### Uainishaji wa Mawimbi
| Aina | Maelezo | Mfano |
|------|-------------|----------|
| **Muda unaoendelea** | Inafafanuliwa kwa zote t ∈ ℝ | Voltage ya sauti, halijoto |
| **Wakati wa kipekee** | Inafafanuliwa kwa fahirisi kamili n | Sampuli za sauti, thamani za pikseli |
| **Analogi** | Kuendelea kwa wakati na amplitude | Sehemu ya rekodi ya vinyl |
| **Dijitali** | Tofauti kwa wakati na amplitude quantised | faili ya MP3, picha ya JPEG |
| **Kipindi** | x(t + T) = x(t) kwa t zote | Sine wimbi, mraba wimbi |
| **Kipindi** | Hakuna muundo unaorudiwa | Hotuba, muziki |
| **Kuamua** | Inatabirika kabisa | Sine wimbi |
| **Stochastic** | Ina nasibu | Kelele, bei za hisa |
### Sifa za Mfumo
| Mali | Ufafanuzi | Mfano |
|----------|-----------|----------|
| **Mstari** | T[ax₁ + bx₂] = aT[x₁] + bT[x₂] | Kichujio cha pasi ya chini |
| **Sifa-tofauti** | Shift katika ingizo → mabadiliko sawa katika pato | Kichujio chochote kisichobadilika |
| **Sababu** | Pato hutegemea tu ingizo za sasa na zilizopita | Mfumo wa wakati halisi |
| **Imara (BIBO)** | Ingizo lenye mipaka → pato lenye mipaka | Kichujio kilichoundwa vizuri |
| **Sina kumbukumbu** | Pato hutegemea tu ingizo la sasa | Kikuza |
---

## Mabadiliko ya Fourier
**Mabadiliko ya Nne** hutenganisha mawimbi katika masafa yake ya msingi.
### Mabadiliko ya Fourier Endelevu
X(f) = ∫_{−∞}^{∞} x(t) e^{−j2πft} dt
Kinyume: x(t) = ∫_{−∞}^{∞} X(f) e^{j2πft} df
### Fourier Transform Jozi
| Kikoa cha Wakati x(t) | Frequency Domain X(f) |
|-----------------------------------------|
| mapigo ya mstatili | kazi ya sinc |
| kazi ya sinc | mapigo ya mstatili |
| Gaussian e^{−at²} | Kigaussia (√(π/a))e^{−π²f²/a} |
| Delta ya Dirac δ(t) | 1 (masafa yote) |
| Kielelezo changamano e^{j2πf₀t} | δ(f − f₀) |
| Cosine cos(2πf₀t) | ½[δ(f−f₀) + δ(f+f₀)] |
### Sifa Muhimu
| Mali | Kikoa cha Wakati | Kikoa cha Marudio |
|----------|-------------------------------|
| Linearity | shoka₁(t) + bx₂(t) | aX₁(f) + bX₂(f) |
| Mabadiliko ya wakati | x(t − t₀) | X(f)e^{−j2πft₀} |
| Kuhama kwa masafa | x(t)e^{j2πf₀t} | X(f − f₀) |
| Mapinduzi | x₁(t) ∗ x₂(t) | X₁(f) · X₂(f) |
| Kuzidisha | x₁(t) · x₂(t) | X₁(f) ∗ X₂(f) |
| Tofauti | dx/dt | j2πf X(f) |
| Nadharia ya Parseval | ∫\|x(t)\|² dt | ∫\|X(f)\|² df |
**Nadharia ya ubadilishaji:** Mbadiliko katika wakati = kuzidisha kwa mzunguko. Hii ndiyo sifa muhimu zaidi - inabadilisha shughuli za ubadilishanaji ghali kuwa kuzidisha kwa bei nafuu.
### Mageuzi ya Tofauti ya Fourier (DFT)
Kwa mfuatano x[0], x[1], ..., x[N-1]:
X[k] = Σ_{n=0}^{N−1} x[n] e^{−j2πkn/N}, k = 0, 1, ..., N−1
| Mali | Thamani |
|----------|-------|
| Ingizo | N sampuli halisi au changamano |
| Pato | N changamano mapipa ya masafa |
| Ubora wa masafa | f_s/N (ambapo f_s ni kiwango cha sampuli) |
| Masafa ya Nyquist | f_s/2 (masafa ya juu zaidi yanayoweza kuwakilishwa) |
| Utata | O(N²) hesabu ya moja kwa moja |
### Mabadiliko ya Haraka ya Fourier (FFT)
**FFT** hukusanya DFT katika O(N logi N) badala ya O(N²).
| N | O(N²) Operesheni | O(N logi N) Operesheni | Kuongeza kasi |
|---|-----------------|-------------------------------|
| 1,024 | 1,048,576 | 10,240 | 102× |
| 1,048,576 | 1.1 × 10¹² | 20,971,520 | 52,428× |
FFT ni mojawapo ya kanuni muhimu zaidi kuwahi kuvumbuliwa. Huwezesha uchakataji wa sauti katika wakati halisi, mbano wa picha (JPEG), mawasiliano ya pasiwaya (OFDM), na uchanganuzi wa taswira.
---

## Mabadiliko ya Laplace
**Mabadiliko ya Laplace** yanapanua mabadiliko ya Fourier ili kushughulikia mifumo isiyo imara na uchanganuzi wa muda mfupi.
F(s) = ∫₀^∞ f(t) e^{−st} dt, ambapo s = σ + jω
### Mabadiliko ya Kawaida ya Laplace
| f(t) | F(vi) | Eneo la Muunganiko |
|------|------|----------------------|
| δ(t) (msukumo) | 1 | Yote |
| u(t) (hatua) | 1/s | Re(vi) > 0 |
| e^{−at}u(t) | 1/(s+a) | Re(vi) > −a |
| tⁿu(t) | n!/s^{n+1} | Re(vi) > 0 |
| dhambi(ωt)u(t) | ω/(s²+ω²) | Re(vi) > 0 |
| cos(ωt)u(t) | s/(s²+ω²) | Re(vi) > 0 |
### Muunganisho kwa Fourier Transform
Wakati σ = 0 (s = jω), kigeuzi cha Laplace kinapungua hadi kigeuzi cha Fourier. Badiliko la Laplace hutoa picha kamili zaidi kwa kujumuisha taarifa kuhusu ukuaji/kuoza (σ).
---

## Z-Mabadiliko
**Z-transform** ni sawa na wakati tofauti na ubadilishaji wa Laplace.
X(z) = Σ_{n=−∞}^{∞} x[n] z^{−n}
### Mabadiliko ya Kawaida ya Z
| x[n] | X(z) | ROC |
|------|------|-----|
| δ[n] | 1 | Zote |
| u[n] (hatua) | z/(z-1) | \|z\| > 1 |
| aⁿu[n] | z/(z-a) | \|z\| > \|a\| |
| naⁿu[n] | az/(z−a)² | \|z\| > \|a\| |
| dhambi(ω₀n)u[n] | z sin(ω₀)/(z²−2z cos(ω₀)+1) | \|z\| > 1 |
### Uhusiano na Mabadiliko Mengine
| Badilisha | Kikoa | Tofauti |
|-----------|--------------------|
| Fourier | Mzunguko unaoendelea | f au ω |
| Mahali | Mzunguko tata | s = σ + jω |
| Z-badilisha | Masafa tata (ya kipekee) | z = e^{sT} |
Mduara wa kitengo katika z-ndege (|z| = 1) inalingana na kigeuzi cha Fourier.
---

##Vichujio
Vichujio hupitisha au kuzuia vijenzi fulani vya masafa kwa kuchagua.
### Aina za Vichujio
| Aina | Pasi | Vitalu | Maombi |
|------|--------|----------------------|
| **Pasi ya chini** | Masafa ya chini | masafa ya juu | Laini, kuzuia kutengwa |
| **High-pass** | masafa ya juu | Masafa ya chini | Kugundua makali, kuondolewa kwa kelele |
| **Band-pass** | Msururu wa masafa | Nje ya safu | Uchaguzi wa kituo (redio) |
| **Kikomesha bendi (nochi)** | Kila kitu isipokuwa safu | Safu maalum | Kuondoa hum ya laini ya umeme |
### Vichujio vya FIR dhidi ya IIR
| Mali | MOTO (Finite Impulse Response) | IIR (Majibu ya Msukumo usio na kikomo) |
|----------|-------------------------------------------------------------|
| Jibu la msukumo | Muda wa mwisho | Muda usio na kikomo |
| Utulivu | Daima thabiti | Inaweza kutokuwa thabiti |
| Awamu | Inaweza kuwa mstari haswa | Kwa ujumla awamu isiyo ya mstari |
| Maoni | Hapana | Ndiyo |
| Kuhesabu | Migawo zaidi inahitajika | Vigawo vichache vya uondoaji sawa |
| Ubunifu | Dirisha, Viwanja-McClellan | Butterworth, Chebyshev, mviringo |
| Chaguo za kuhamisha | H(z) = Σ bₖz⁻ᵏ | H(z) = Σ bₖz⁻ᵏ / (1 + Σ aₖz⁻ᵏ) |
### Viainisho vya Muundo wa Kichujio
| Kigezo | Maelezo |
|-----------|-------------|
| **Nenosiri** | Masafa ya masafa ambayo yanapaswa kupita kwa hasara ndogo |
| **Kikomesha** | Masafa ya masafa ambayo yanapaswa kupunguzwa |
| **Marudio ya kukatwa** | Mpaka kati ya passband na stopband |
| **Ripple** | Tofauti katika faida ya pasi (au stopband) |
| **Ondosha ** | Kiwango cha kupungua (dB kwa oktava au muongo) |
| **Bendi ya mpito** | Eneo kati ya pasi na stopband |
### Miundo ya Kichujio cha Kawaida
| Ubunifu | Sifa | Tumia Kesi |
|--------|---------------------------|
| **Butterworth** | Pasi tambarare ya juu zaidi, uondoaji wa wastani | Kusudi la jumla |
| **Chebyshev Aina ya I** | Ripple in passband, steeper roll-off | Wakati uondoaji ni muhimu |
| **Chebyshev Aina II** | Ripple katika stopband, bapa passband | Wakati ubapa wa pasi ni muhimu |
| **Mviringo (Cauer)** | Ripple katika zote mbili, roll-off mwinuko zaidi | Agizo la chini linalohitajika |
| **Bessel** | Awamu ya mstari (upeo ucheleweshaji wa kikundi tambarare) | Kuhifadhi umbo la wimbi |
---

## Nadharia ya Sampuli
### Nadharia ya Sampuli ya Nyquist-Shannon
Ishara inayoendelea inaweza kuundwa upya kikamilifu kutoka kwa sampuli zake ikiwa kiwango cha sampuli kinazidi mara mbili ya upeo wa juu:
f_s > 2f_max
| Muda | Ufafanuzi |
|------|-------------|
| **Kiwango cha sampuli** (f_s) | Idadi ya sampuli kwa sekunde |
| **Kiwango cha Nyquist** | 2f_max (kiwango cha chini cha sampuli) |
| **Marudio ya Nyquist** | f_s/2 (masafa ya juu zaidi yanayoweza kuwakilishwa) |
| **Kujitenga** | Masafa ya juu yanayojifanya kuwa masafa ya chini wakati f_s <2f_max |
### Viwango vya Kawaida vya Sampuli
| Maombi | Kiwango | Masafa ya Nyquist |
|--------------------|-------------------|
| Hotuba ya simu | 8 kHz | 4 kHz |
| CD ya sauti | 44.1 kHz | 22.05 kHz |
| Sauti ya kitaalamu | 48 kHz | 24 kHz |
| Sauti ya azimio la juu | 96 kHz | 48 kHz |
| Video (fps 30) | 30 Hz (ya muda) | 15 Hz |
### Anti-aliasing
Kabla ya kuchukua sampuli, ** kichujio cha kuzuia aliasing ** (chini ya kupita) huondoa masafa juu ya f_s/2 ili kuzuia kujulikana.
---

##Kufungua dirisha
Wakati wa kuchambua sehemu ya mwisho ya ishara, tunazidisha kwa uwazi kwa dirisha la mstatili, na kusababisha uvujaji wa spectral. **Vitendaji vya dirisha** hupunguza uvujaji huu.
### Windows ya kawaida
| Dirisha | Upana wa Lobe Kuu | Kiwango cha Lobe ya Upande | Tumia Kesi |
|--------|-------------------------------------------|
| Mstatili | Nyembamba | −13 dB | Wakati azimio ni muhimu zaidi |
| Hana | 2× mstatili | −31 dB | Kusudi la jumla |
| Kugonga | 2× mstatili | −41 dB | Imepunguza lobe iliyo karibu zaidi |
| Mtu mweusi | 3× mstatili | −58 dB | Masafa ya juu yanayobadilika |
| Kaisa | Inaweza Kurekebishwa | Inaweza kurekebishwa (kupitia β) | Wakati biashara inaweza kutumika |
### Uvujaji wa Spectral
Kuzidisha ishara kwa dirisha kunaunganisha wigo wake na wigo wa dirisha. Lobes kuu pana hupunguza azimio la mzunguko; lobes za chini hupunguza uvujaji.
---

## Mawimbi
**Mawimbi** ni vitendakazi vidogo, vilivyojanibishwa vinavyofanana na mawimbi vinavyotumika kwa uchanganuzi wa mawimbi yenye maazimio mengi.
### Mabadiliko ya Wavelet
Tofauti na mageuzi ya Fourier (ambayo hutoa taarifa ya masafa ya kimataifa), ubadilishaji wa wimbi hutoa **masafa ya saa** ujanibishaji.
| Badilisha | Azimio la Wakati | Azimio la Marudio |
|-----------|--------------------------------------|
| Fourier | Hakuna (ulimwenguni) | Bora |
| Muda Mfupi FT | Imewekwa (saizi ya dirisha) | Imewekwa |
| Wavelet | Inabadilika (nzuri kwa masafa ya juu) | Inabadilika (nzuri kwa masafa ya chini) |
### Familia za Kawaida za Wavelet
| Familia | Mali | Maombi |
|--------|-----------|-------------|
| **Haar** | Rahisi zaidi, isiyoendelea | Utambuzi wa makali, uchambuzi wa haraka |
| **Daubechies** (dbN) | Usaidizi thabiti, Nyakati za kutoweka | Mfinyazo, denoise |
| **Alama** | Daubechies karibu linganifu | Kupunguza upotoshaji wa awamu |
| **Coiflets** | Imeundwa kwa ajili ya hali ya sasa | Uchakataji wa mawimbi |
| **Moleti** | Sinusoid yenye madirisha ya Gaussian | Uchambuzi wa masafa ya wakati |
| **Kofia ya Mexico** | Toleo la pili la Gaussian | Utambuzi wa kipengele |
### Maombi ya Wavelets
| Maombi | Jinsi Mawimbi Yanavyosaidia |
|---------------------------------|
| Mfinyazo wa picha (JPEG 2000) | Uwakilishi wa maazimio mengi, bora kuliko DCT kwa kingo |
| Kutoa sauti | Kizingiti cha mgawo mdogo wa wimbi la wimbi (mawimbi iko katika coefficients kubwa) |
| Utambuzi wa kipengele | Utambuzi wa ukingo, utambuzi wa muda mfupi katika mfululizo wa saa |
| Uchambuzi wa ECG | Kugundua muundo wa QRS, uainishaji wa arrhythmia |
| Uchambuzi wa tetemeko | Kutambua tabaka za kijiolojia, usindikaji wa ishara ya tetemeko la ardhi |
---

## Umuhimu kwa Kujifunza kwa Mashine na Sayansi ya Data
| Dhana ya Uchakataji wa Mawimbi | Maombi |
|---------------------------------------|
| Mabadiliko ya Fourier | Vipengele vya Spectral vya ML ya sauti, uchanganuzi wa kikoa cha mzunguko wa mfululizo wa saa |
| FFT | Ubadilishaji wa haraka katika CNNs (ubadilishaji wa spectral), uwiano unaofaa |
| Nadharia ya mapinduzi | Kuelewa jinsi CNNs hufanya kazi (ni vichungi vilivyojifunza) |
| Vichujio | Kuchakata mapema (kulainisha, kupunguza sauti), uchimbaji wa kipengele |
| Nadharia ya sampuli | Kuelewa hiari, kuchagua viwango vya sensorer, epuka kutamka |
| Dirisha | STFT ya sauti ML (spectrograms), uchanganuzi wa masafa ya wakati |
| Mawimbi | Uchimbaji wa kipengele kwa mfululizo wa saa, mbano, denoising |
| Laplace/Z-badilisha | Nadharia ya udhibiti wa robotiki, uthabiti wa mfumo wa kuelewa |
| Uchambuzi wa spectral | Uchunguzi wa EEG/fMRI, ufuatiliaji wa vibration, matengenezo ya utabiri |
| Kiwango cha Nyquist | Kuchagua viwango vinavyofaa vya ukusanyaji wa data kwa mabomba ya ML |
---

## Muhtasari
| Zana | Kikoa | Maarifa Muhimu |
|------|----------------------|
| Mabadiliko ya Fourier | Saa → Masafa | Ishara ni jumla ya sinusoids |
| Mabadiliko ya Laplace | Saa → Masafa tata | Hushughulikia muda mfupi na utulivu |
| Z-Kubadilisha | Wakati maalum → Tata | Uchambuzi na muundo wa kichujio cha dijiti |
| FFT | Uhesabuji bora wa DFT | O(N logi N) badala ya O(N²) |
| Vichujio | Uchaguzi wa mara kwa mara | Pitisha unachohitaji, zuia usichohitaji |
| Nadharia ya Sampuli | Inayoendelea ↔ ya kipekee | Sampuli haraka vya kutosha, usipoteze chochote |
| Dirisha | Biashara ya muda-frequency | Utatuzi wa usawa na uvujaji |
| Mawimbi | Uchambuzi wa maazimio mengi | Karibu katika saa na marudio |
Uchakataji wa mawimbi hutoa msingi wa hisabati wa kuelewa, kuchanganua na kudhibiti data. Kila bomba la kujifunza kwa mashine linalofanya kazi na mfululizo wa saa, sauti, picha au data ya vitambuzi kwa njia kamili hutumia dhana za usindikaji wa mawimbi. Ubadilishaji wa Fourier, haswa, ndio zana muhimu zaidi ya kihesabu baada ya calculus kwa mwanasayansi yeyote wa data.