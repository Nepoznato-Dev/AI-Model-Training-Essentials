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
# Generative AI Deep Dive
Tumutukoy ang Generative AI sa mga modelong gumagawa ng bagong content — mga larawan, text, audio, video, code — sa halip na pag-uuri o hulaan lang ang umiiral na data. Habang ang malalaking modelo ng wika ay nakakakuha ng karamihan ng atensyon, ang generative AI landscape ay mas malawak. Sinasaklaw ng file na ito ang mga arkitektura, diskarte, at trade-off sa likod ng mga modernong generative system, mula sa mga modelo ng pagsasabog hanggang sa variational na autoencoders hanggang sa mga flow model.
---

## Ano ang Ginagawang "Generative" ng Modelo?
| Uri | Ano ang Ginagawa Nito | Halimbawa |
|------|-------------|---------|
| **Diskriminatibo** | Alamin ang hangganan sa pagitan ng mga klase | "Ang imahe ba ay isang pusa o isang aso?" |
| **Generative** | Alamin ang pamamahagi ng data mismo | "Bumuo ng bagong larawan ng isang pusa" |
Kinukuha ng mga generative model ang *kung paano ginawa ang data*, hindi lang kung paano ito ikategorya. Dahil dito, mas malakas sila — at mas mahirap sanayin.
---

## Pangunahing Generative Architecture
### Variational Autoencoders (VAEs)
Natututo ang mga VAE ng naka-compress at structured na representasyon (latent space) ng data, pagkatapos ay bumuo ng mga bagong sample sa pamamagitan ng sampling mula sa space na iyon.
| Bahagi | Tungkulin |
|-----------|------|
| **Encoder** | Data input ng Maps sa isang distribution sa latent space (mean at variance) |
| **Latent space** | Isang tuluy-tuloy, mababang-dimensional na espasyo kung saan magkakalapit ang magkatulad na mga punto ng data |
| **Decoder** | Ang mga mapa ay tumuturo sa latent space pabalik sa data space |
| **KL divergence** | Regularization term na nagpapanatili sa latent distribution na malapit sa isang karaniwang normal |
**Paano gumagana ang pagbuo**: sample ng random vector mula sa latent space → ipasa ito sa decoder → kumuha ng bagong data point.
| Lakas | Kahinaan |
|----------|----------|
| Makinis, tuluy-tuloy na nakatagong espasyo | Ang mga output ay malamang na malabo |
| Principled mathematical framework | Limitado ng kapasidad ng arkitektura |
| Maaaring mag-interpolate sa pagitan ng mga halimbawa | Hindi gaanong matalas kaysa sa diffusion o GAN na mga output |
Ang mga VAE ay kadalasang ginagamit bilang mga bahagi sa ibang mga modelo (hal., Ang Stable Diffusion ay gumagamit ng VAE bilang bahagi ng pipeline nito).
### Mga Generative Adversarial Network (GAN)
Pinagsasama ng mga GAN ang dalawang network laban sa isa't isa: isang **generator** na gumagawa ng pekeng data, at isang **diskriminator** na sumusubok na sabihin ang totoo mula sa peke.
| Bahagi | Layunin |
|-----------|------|
| **Generator** | Gumawa ng data na niloloko ang discriminator |
| **Diskriminator** | Tamang uriin ang tunay kumpara sa nabuong data |
Sabay-sabay silang nagsasanay, ang bawat isa ay nagtutulak sa isa't isa upang mapabuti. Sa teorya, ang generator sa kalaunan ay gumagawa ng data na hindi makilala sa totoong data.
| Variant ng GAN | Pangunahing Pagbabago |
|-------------|----------------|
| **DCGAN** | Convolutional architecture; matatag na pagsasanay |
| **StyleGAN / StyleGAN2 / StyleGAN3** | Estilo-based na henerasyon; photorealistic na mga mukha; nakokontrol na mga katangian |
| **CycleGAN** | Hindi ipinares na pagsasalin ng larawan-sa-larawan (kabayo → zebra) |
| **Pix2Pix** | Ipinares na pagsasalin ng larawan-sa-larawan (sketch → larawan) |
| **ProGAN** | Progresibong paglaki para sa mga larawang may mataas na resolution |
| **BigGAN** | Class-conditional na henerasyon sa sukat |
**Bakit tinanggihan ang mga GAN**: Ang pagsasanay ay kilalang hindi matatag (mode collapse, nawawalang mga gradient). Gumagawa na ngayon ang mga diffusion model ng mas mahusay na kalidad para sa karamihan ng mga gawain sa pagbuo ng imahe. Ginagamit pa rin ang mga GAN para sa mga real-time na application (mabilis ang mga ito sa hinuha) at mga partikular na gawain tulad ng super-resolution.
### Mga Modelo ng Diffusion
Ang mga modelo ng pagsasabog ay ang kasalukuyang estado ng sining para sa pagbuo ng larawan at video. Gumagana ang mga ito sa pamamagitan ng unti-unting pagdaragdag ng ingay sa data hanggang sa ito ay purong random na ingay, pagkatapos ay natutong i-reverse ang proseso.
| Yugto | Ano ang Mangyayari |
|-------|-------------|
| **Proseso ng pagpasa (pagsasanay)** | Dahan-dahang magdagdag ng Gaussian noise sa daan-daang/libong hakbang hanggang sa masira ang data |
| **Baliktad na proseso (generation)** | Matutong mag-denoise nang hakbang-hakbang, simula sa purong ingay, hanggang sa lumabas ang isang malinis na imahe |
| Modelo | Developer | Kapansin-pansing Tampok |
|-------|-----------|----------------|
| **DDPM** (Denoising Diffusion Probabilistic Model) | Ho et al., 2020 | Ang mga ipinakitang modelo ng pagsasabog ay maaaring makagawa ng mga de-kalidad na larawan |
| **Stable Diffusion** | Katatagan AI | Latent diffusion (tumatakbo sa compressed space); open-source |
| **DALL-E 3** | OpenAI | Pinagsama sa ChatGPT para sa pag-unawa sa teksto |
| **Midjourney** | Midjourney | Artistic na kalidad; closed-source |
| **Larawan** | Google DeepMind | High-fidelity text-to-image |
| **Sora** | OpenAI | Pagbuo ng video sa pamamagitan ng mga diffusion transformer |
| **FLUX** | Black Forest Labs | Open-weight na kahalili sa Stable Diffusion |
### Bakit Nanalo ang Diffusion Models
| Pakinabang | Paliwanag |
|-----------|-------------|
| **Katatagan ng pagsasanay** | Higit na mas matatag kaysa sa mga GAN; walang adversarial na pagsasanay |
| **Kalidad ng output** | Makabagong kalidad at pagkakaiba-iba ng larawan |
| **Kakayahang kontrolin** | Maaaring gabayan ng text (sa pamamagitan ng CLIP), pagpinta ng mga maskara, o iba pang kundisyon |
| **Pagkakaiba** | Mas kaunting mode collapse kaysa sa mga GAN; bumubuo ng magkakaibang mga output |
| Disadvantage | Paliwanag |
|-------------|-------------|
| **Mabagal na hinuha** | Nangangailangan ng maraming denoising na hakbang (20–50 karaniwang) |
| **Compute-intensive** | Ang bawat hakbang ay isang full forward pass sa isang malaking modelo |
### Latent Diffusion
Ang pagpapatakbo ng diffusion sa pixel space ay mahal. **Latent diffusion** (ginamit ng Stable Diffusion) sa halip ay nagpapatakbo ng proseso ng diffusion sa isang naka-compress na latent space.
| Hakbang | Ano ang Mangyayari |
|------|-------------|
| 1. I-compress | Ang isang pre-trained na VAE ay nag-encode ng imahe sa isang mas maliit na latent na representasyon |
| 2. Diffuse | Ang diffusion model ay nagdaragdag/nag-aalis ng ingay sa latent space |
| 3. I-decode | Kino-convert ng VAE decoder ang latent pabalik sa isang buong imahe |
Ginagawa nitong mas mabilis at mas mura ang henerasyon habang pinapanatili ang kalidad.
---

## Pagbuo ng Text-Conditioned
Karamihan sa mga modernong generative system ay nakakondisyon sa mga text prompt — inilalarawan mo kung ano ang gusto mo, at binubuo ito ng modelo.
### CLIP (Contrastive Language-Image Pre-training)
Natututo ang CLIP ng nakabahaging espasyo sa pag-embed para sa teksto at mga larawan. Ito ay sinanay sa bilyun-bilyong pares ng imahe-text mula sa internet.
| Kakayahan | Paglalarawan |
|------------|-------------|
| **Pag-uuri ng zero-shot** | Pag-uri-uriin ang mga larawan gamit ang mga paglalarawan ng teksto nang walang anumang pagsasanay |
| **Pagkuha ng imahe-text** | Hanapin ang pinakanauugnay na larawan para sa isang text query |
| **Guiding diffusion** | Patnubayan ang pagbuo ng larawan patungo sa text prompt |
### Classifier-Free Guidance (CFG)
Kinokontrol ng CFG kung gaano kalapit ang nabuong larawan na sumusunod sa text prompt.
| Scale ng CFG | Epekto |
|-----------|--------|
| **1.0** | Walang patnubay; magkakaiba ngunit maaaring hindi tumugma sa prompt |
| **5.0–7.5** | Balanseng; magandang kalidad at maagap na pagsunod |
| **10.0+** | Malakas na pagsunod; maaaring gumawa ng mga oversaturated o artefact-heavy na mga larawan |
---

## Iba Pang Generative Approach
### Pag-normalize ng Daloy
| Tampok | Paglalarawan |
|---------|-------------|
| **Paano ito gumagana** | Alamin ang isang invertible na pagmamapa sa pagitan ng data at isang simpleng pamamahagi |
| **Lakas** | Eksaktong pagkalkula ng posibilidad; mabilis na sampling |
| **Kahinaan** | Nangangailangan ng maingat na idinisenyong mga arkitektura; hindi gaanong nababaluktot |
| **Mga kaso ng paggamit** | Pagtuklas ng anomalya, pagtatantya ng density |
### Mga Autoregressive na Modelo
| Tampok | Paglalarawan |
|---------|-------------|
| **Paano ito gumagana** | Bumuo ng data ng isang elemento sa isang pagkakataon, pagkondisyon sa lahat ng nakaraang elemento |
| **Lakas** | Natural para sa sequential data (text, code, musika) |
| **Kahinaan** | Mabagal na henerasyon (dapat sunud-sunod); nililimitahan ng pamamahagi ng data ng pagsasanay |
| **Mga Halimbawa** | GPT (teksto), WaveNet (audio), ImageGPT (mga larawan) |
### Mga Modelong Batay sa Enerhiya
| Tampok | Paglalarawan |
|---------|-------------|
| **Paano ito gumagana** | Alamin ang isang function ng enerhiya; mababang enerhiya = makatotohanang data |
| **Lakas** | Flexible; walang kinakailangang normalisasyon |
| **Kahinaan** | Mahirap ang pagsasanay; nangangailangan ng MCMC |
| **Mga kaso ng paggamit** | Teoretikal na pananaliksik; ilang mga robotics application |
---

## Mga Sukatan ng Pagsusuri
Paano mo sinusukat ang kalidad ng nabuong data? Ito ay mas mahirap kaysa sa maaari mong isipin.
| Sukatan | Para sa | Ang Sinusukat Nito | Limitasyon |
|--------|-----|----------------|------------|
| **FID** (Fréchet Inception Distansya) | Mga Larawan | Distansya sa pagitan ng tunay at nabuong mga pamamahagi ng imahe | Ang mas mababa ay mas mabuti; hindi nakakakuha ng pagkakaiba-iba nang maayos |
| **IS** (Inception Score) | Mga Larawan | Kalidad at pagkakaiba-iba ng mga nabuong larawan | Kontrobersyal; maaaring i-game |
| **CLIP Score** | Text-to-image | Gaano kahusay tumugma ang larawan sa text prompt | Depende sa mga bias ng CLIP |
| **Kagulo** | Text | Gaano kahusay hinulaan ng modelo ang susunod na token | Ang mas mababa ay mas mabuti; hindi sinusukat ang pagkakaugnay |
| **BLEU / ROUGE** | Pagbuo ng teksto | Nag-overlap sa reference na text | Mahina proxy para sa paghatol ng tao |
| **FAD** (Fréchet Audio Distansya) | Audio | Distansya sa pagitan ng tunay at nabuong mga pamamahagi ng audio | Katulad sa FID para sa audio |
---

## Nakokontrol na Pagbuo
Hinahayaan ka ng mga modernong system na kontrolin kung ano ang nabubuo nang higit pa sa mga prompt ng text.
| Paraan | Uri ng Kontrol | Halimbawa |
|--------|-------------|---------|
| **Pagpinta** | Punan ang mga naka-mask na rehiyon | Alisin ang isang bagay mula sa isang larawan |
| **Outpainting** | Palawakin lampas sa mga hangganan ng larawan | Gawing mas malawak ang landscape |
| **ControlNet** | Patnubay sa istruktura (mga gilid, lalim, pose) | Bumuo ng larawang tumutugma sa isang partikular na pose |
| **IP-Adapter** | Estilo o nilalaman mula sa isang reference na larawan | "Gawin itong parang painting na ito" |
| **LoRA** | Pinong istilo o konsepto | Magdagdag ng partikular na karakter o istilo ng sining |
| **Img2Img** | Ibahin ang anyo ng isang umiiral na larawan | Gawing photorealistic na larawan ang isang sketch |
---

## Pagbuo ng Video
Ang pagbuo ng video ay ang susunod na hangganan pagkatapos ng mga larawan. Ito ay nagdaragdag ng sukat ng oras at paggalaw.
| Modelo | Diskarte | Kapansin-pansing Tampok |
|-------|----------|----------------|
| **Sora** (OpenAI) | Diffusion Transformer | Hanggang 1080p; naiintindihan ng mabuti ang pisika |
| **Runway Gen-3** | Nakabatay sa pagsasabog | Tool sa pagbuo ng komersyal na video |
| **Pika** | Nakabatay sa pagsasabog | Maikling video clip mula sa teksto |
| **Kling** | Autoregressive + diffusion | Long-form na pagbuo ng video |
| **Veo 2** (Google) | Diffusion Transformer | Mataas na kalidad, pisikal na pare-parehong video |
### Mga Hamon sa Pagbuo ng Video
| Hamon | Bakit Mahirap |
|-----------|--------------|
| **Temporal na pagkakapare-pareho** | Dapat magkapareho ang hitsura ng mga bagay sa mga frame |
| **Physics** | Ang gravity, banggaan, fluid dynamics ay dapat na tinatayang tama |
| **Haba** | Ang pagbuo ng mga minuto ng magkakaugnay na video ay mas mahirap kaysa sa isang larawan |
| **Compute** | Ang video ay mahalagang maraming larawan; sukat ng mga gastos na may bilang ng frame |
| **Pagsusuri** | Walang karaniwang sukatan ang nakakakuha ng kalidad ng video nang maayos |
---

## Pagbuo ng Audio
| Modelo | Uri | Application |
|-------|------|-------------|
| **WaveNet** (DeepMind) | Autoregressive | Mataas na kalidad na speech synthesis |
| **VALL-E** (Microsoft) | Neural codec | Text-to-speech mula sa isang 3 segundong sample ng boses |
| **MusicGen** (Meta) | Nakabatay sa transformer | Text-to-music generation |
| **AudioLDM** | Nakatagong pagsasabog | Pagbuo ng sound effect |
| **ElevenLabs** | Komersyal | Voice cloning at synthesis |
---

## Ang Ekonomiks ng Henerasyon
| Salik | Epekto |
|--------|--------|
| **Gastos sa pagsasanay** | Mga modelo ng pagsasabog: $100K–$10M+ depende sa sukat |
| **Halaga ng hinuha** | Pagbuo ng larawan: ~$0.01–0.05 bawat larawan sa sukat |
| **Hardware** | Pagsasanay: maramihang A100/H100 GPU; Hinuha: posible ang isang GPU |
| **Bukas vs sarado** | Ang mga bukas na modelo (Stable Diffusion, FLUX) ay maaaring tumakbo nang lokal; ang mga closed model (DALL-E, Midjourney) ay API-only |
---

## Buod
Ang Generative AI ay umunlad mula sa mga GAN hanggang sa mga VAE hanggang sa mga modelo ng pagsasabog at higit pa. Ang pangunahing insight sa lahat ng mga arkitektura na ito ay pareho: alamin ang pamamahagi ng data, pagkatapos ay mag-sample mula dito upang lumikha ng bagong nilalaman. Ang mga modelo ng pagsasabog ay kasalukuyang nangingibabaw sa pagbuo ng imahe at video dahil sa kanilang katatagan ng pagsasanay at kalidad ng output. Ang mga VAE ay nagsisilbing mahalagang mga bloke ng gusali. Ang mga autoregressive na modelo ay nangingibabaw sa text at code. Ang field ay lumilipat patungo sa multimodal generation — mga system na maaaring gumawa ng text, mga larawan, audio, at video mula sa anumang kumbinasyon ng mga input — at patungo sa paggawa ng henerasyon nang mas mabilis, mas mura, at mas nakokontrol.