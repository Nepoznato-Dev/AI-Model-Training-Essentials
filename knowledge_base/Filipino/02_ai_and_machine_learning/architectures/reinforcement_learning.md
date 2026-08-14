---
# Metadata
title: "Reinforcement Learning"
description: "MDPs, Q-learning, policy gradients, RLHF, multi-agent systems"
category: "AI and Machine Learning"
subcategory: "Model Architectures"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to architectures/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [reinforcement, learning, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "9 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

# Reinforcement Learning
Ang reinforcement learning (RL) ay kung paano natututo ang mga machine na gumawa ng mga pagkakasunud-sunod ng mga desisyon sa pamamagitan ng trial at error. Hindi tulad ng pinangangasiwaang pag-aaral, kung saan ang tamang sagot ay ibinibigay para sa bawat halimbawa, ang RL ay nagbibigay lamang sa isang ahente ng signal ng reward — at dapat malaman ng ahente kung aling mga aksyon ang humahantong sa pinakamahusay na mga resulta sa paglipas ng panahon. Ito ang diskarte sa likod ng AlphaGo, robotic control, laro-playing AI, at — critically — RLHF, ang diskarteng ginamit upang ihanay ang modernong malalaking modelo ng wika sa mga kagustuhan ng tao.
---

## Mga Pangunahing Konsepto
Binabalangkas ng RL ang paggawa ng desisyon bilang isang loop sa pagitan ng isang **agent** at isang **environment**.
| Bahagi | Tungkulin | Halimbawa |
|-----------|------|---------|
| **Agent** | Ang gumagawa ng desisyon | Isang programa ng chess, isang robot, isang modelo ng wika |
| **Kapaligiran** | Ang mundo na nakikipag-ugnayan ang ahente sa | Ang chessboard, isang bodega, isang pag-uusap |
| **Estado** | Ang kasalukuyang sitwasyon | Posisyon ng board, pagbabasa ng sensor ng robot, history ng chat |
| **Pagkilos** | Ano ang magagawa ng ahente | Ilipat ang isang piraso, lumiko pakaliwa, bumuo ng isang token |
| **Reward** | Signal ng feedback (scalar number) | +1 para sa panalo, -1 para sa pag-crash, marka ng kagustuhan ng tao |
| **Patakaran** | Strategy mapping states to actions | "Kung ang hari ay pinagbantaan, ilipat ito" |
| **Value function** | Inaasahang pinagsama-samang gantimpala mula sa isang estado | "Ang posisyon ng board na ito ay nagkakahalaga ng humigit-kumulang +3 puntos" |
### Ang RL Loop
```
Agent observes State → chooses Action → Environment returns new State + Reward
        ↑                                                                         |
        └─────────────────────────────────────────────────────────────────────────┘
```

Ang layunin ng ahente ay i-maximize ang **cumulative reward** sa paglipas ng panahon, hindi lang ang agarang reward. Ito ang dahilan kung bakit naiiba ang RL sa pinangangasiwaang pag-aaral.
---

## Mga Pangunahing Pagkakaiba mula sa Iba pang Paradigma sa Pag-aaral
| Aspeto | Pinangangasiwaang Pag-aaral | Unsupervised Learning | Reinforcement Learning |
|----------------------|--------------------|---------------------|----------------------|
| **Signal** | Mga tamang label para sa bawat halimbawa | Walang mga label; hanapin ang istraktura | Scalar reward, madalas na naantala |
| **Feedback** | Kaagad | Wala | Naantala at kalat-kalat |
| **Sequence** | Ang bawat halimbawa ay independyente | Ang bawat halimbawa ay independyente | Nakakaapekto ang mga pagkilos sa mga estado sa hinaharap |
| **Layunin** | I-minimize ang error sa hula | Tuklasin ang mga pattern | I-maximize ang pinagsama-samang reward |
---

## Markov Decision Processes (MDPs)
Ang mga MDP ay ang mathematical framework para sa RL. Ipinapalagay nila na ang hinaharap ay nakasalalay lamang sa kasalukuyang estado, hindi ang kasaysayan kung paano ka nakarating doon (ang **Markov property**).
| Bahagi | Notasyon | Ibig sabihin |
|-----------|----------|---------|
| **Mga Estado** | S | Lahat ng posibleng sitwasyon na maaaring nasa |
| **Mga Pagkilos** | Isang | Lahat ng bagay na kayang gawin ng ahente |
| **Transition function** | P(s' \| s, a) | Probabilidad na maabot ang state s' pagkatapos gumawa ng aksyon a sa state s |
| **Pag-andar ng reward** | R(s, a, s') | Natanggap na gantimpala para sa paglipat |
| **Discount factor** | γ (gamma) | Magkano ang pahalagahan ang mga reward sa hinaharap kumpara sa mga agarang (0 hanggang 1) |
Ang **return** (kabuuang may diskwentong reward) ay:
```
G = R₁ + γR₂ + γ²R₃ + ...
```

Ang isang mataas na kadahilanan ng diskwento (γ malapit sa 1) ay nangangahulugan na ang ahente ay malayo ang paningin. Ang isang mababa ay nangangahulugan na ito ay maikli ang paningin.
---

## Classical RL Algorithms
### Mga Paraang Nakabatay sa Halaga
Natututo ang mga ito kung gaano kahusay ang bawat estado (o pares ng pagkilos ng estado).
| Algorithm | Pangunahing Ideya | Limitasyon |
|-----------|----------|------------|
| **Q-Learning** | Matuto ng talahanayan ng mga Q-values: Q(state, action) = inaasahang reward | Hindi sumusukat sa malalaking puwang ng estado |
| **Deep Q-Network (DQN)** | Gumamit ng neural network para tantiyahin ang mga Q-value | Tanging humahawak ng mga hiwalay na aksyon; maaaring hindi matatag |
| **Dobleng DQN** | Ayusin ang sobrang pagpapahalaga ng Q-learning na bias | Limitado pa rin sa mga hiwalay na pagkilos |
Panuntunan sa pag-update ng Q-learning:
```
Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]
```

### Mga Paraang Batay sa Patakaran
Direktang natututunan ng mga ito ang patakaran (diskarte) nang hindi tinatantya ang mga halaga.
| Algorithm | Pangunahing Ideya | Pakinabang |
|-----------|----------|-----------|
| **REINFORCE** | gradient ng patakaran ng Monte Carlo; i-update ang patakaran sa direksyon ng magagandang resulta | Simple; gumagana sa tuluy-tuloy na pagkilos |
| **PPO** (Proximal Policy Optimization) | I-clip ang mga update sa patakaran upang maiwasan ang malaki, nakakapagpapahinang pagbabago | Matatag; malawakang ginagamit; magandang default |
| **TRPO** | Trust region method para sa mga update sa patakaran | Mas may prinsipyo kaysa PPO; mas mahirap ipatupad |
### Paraan ng Actor-Critic
Pagsamahin ang pinakamahusay sa pareho: isang **aktor** (patakaran) at isang **kritiko** (value function).
| Algorithm | Pangunahing Ideya |
|-----------|----------|
| **A2C / A3C** | Advantage Actor-Critic; gumagamit ng pagtatantya ng kalamangan upang mabawasan ang pagkakaiba |
| **SAC** (Soft Actor-Critic) | I-maximize ang reward habang pinapanatili ang paggalugad (entropy regularization) |
| **TD3** (Twin Delayed DDPG) | Tugunan ang labis na pagpapahalaga sa tuluy-tuloy na mga puwang ng pagkilos |
---

## RLHF: Reinforcement Learning mula sa Human Feedback
Ang RLHF ay ang pamamaraan na ginawang posible ang ChatGPT. Tinutulay nito ang agwat sa pagitan ng isang modelo na maaaring mahulaan ang teksto at isa na gumagawa ng mga output na talagang nakakatulong sa mga tao.
### Ang Tatlong Hakbang
| Hakbang | Ano ang Mangyayari | Output |
|------|-------------|--------|
| **1. Pinangangasiwaang Fine-Tuning (SFT)** | I-fine-tune ang isang pre-trained na modelo sa mataas na kalidad na mga halimbawang isinulat ng tao | Isang modelo na sumusunod sa mga tagubilin nang makatwirang mahusay |
| **2. Pagsasanay sa Modelong Gantimpala** | Ang mga tao ay naghahambing ng mga pares ng mga output ng modelo; sanayin ang isang modelo upang mahulaan ang mga kagustuhan ng tao | Isang modelo ng gantimpala na nagbibigay ng marka ng kalidad ng output |
| **3. RL Optimization** | Gamitin ang PPO para i-fine-tune ang SFT model para ma-maximize ang mga score ng reward model | Isang modelong nakahanay sa mga kagustuhan ng tao |
### Bakit Mahalaga ang RLHF
Kung walang RLHF, ang modelo ng wika ay parang isang mag-aaral na nagbasa ng bawat libro ngunit hindi alam kung paano kumilos sa isang usapan. Maaari itong makabuo ng teksto, ngunit ang teksto ay maaaring hindi nakakatulong, nakakalason, o ganap na nakaligtaan ang punto. Itinuturo ng RLHF ang modelo *kung ano ang gusto ng mga tao* — hindi lang kung ano ang hitsura ng text.
### Mga Variant at Alternatibo
| Paraan | Paglalarawan | Pakinabang |
|--------|-------------|-----------|
| **DPO** (Direct Preference Optimation) | Laktawan ang modelo ng gantimpala; direktang i-optimize ang patakaran mula sa mga kagustuhan ng tao | Mas simple; walang hiwalay na reward model para sanayin |
| **RLAIF** | Gumamit ng AI (sa halip na mga tao) upang bumuo ng mga label ng kagustuhan | Mas mura kaysa sa pag-label ng tao |
| **Constitutional AI** | Gumamit ng isang hanay ng mga prinsipyo upang gabayan ang pag-uugali ng modelo nang walang mga label ng tao | Mas nasusukat; Ang diskarte ni Anthropic |
| **GRPO** (Group Relative Policy Optimisation) | Ihambing ang mga output sa loob ng isang pangkat sa halip na laban sa isang hiwalay na modelo | Ginamit sa DeepSeek-R1; binabawasan ang pangangailangan para sa halaga ng network |
---

## Exploration vs Exploitation
Ito ang gitnang tensyon sa RL. Ang ibig sabihin ng **Pagsasamantala** ay pagpili ng mga aksyon na alam mong gumagana nang maayos. Ang ibig sabihin ng **Exploration** ay sumubok ng mga bagong bagay upang tumuklas ng mga potensyal na mas mahusay na diskarte.
| Diskarte | Paano Ito Gumagana | Trade-off |
|----------|-------------|-----------|
| **ε-matakaw** | Piliin ang pinakamahusay na aksyon sa halos lahat ng oras; random na pagkilos na may posibilidad na ε | Simple ngunit hindi epektibo |
| **Boltzmann exploration** | Pumili ng mga pagkilos na malamang batay sa kanilang mga tinantyang halaga | Mas makinis kaysa sa ε-matakaw |
| **UCB** (Upper Confidence Bound) | Mas gusto ang mga pagkilos na may mataas na kawalan ng katiyakan (optimismo sa harap ng kawalan ng katiyakan) | Magandang teoretikal na mga garantiya |
| **Entropy regularization** | Magdagdag ng bonus para sa pagbisita sa magkakaibang estado (ginamit sa SAC, PPO) | Hinihikayat ang natural na pagsaliksik |
---

## Multi-Agent Reinforcement Learning
Kapag ang maraming ahente ay natututo nang sabay-sabay, ang dynamics ay nagiging mas kumplikado.
| Sitwasyon | Hamon | Halimbawa |
|----------|-----------|---------|
| **Kooperatiba** | Dapat mag-coordinate ang mga ahente; mahirap ang pagtatalaga ng kredito | Mga robot na koponan ng football; distributed sensor network |
| **Mapagkumpitensya** | Ang mga kalaban ay umaangkop; ang kapaligiran ay hindi nakatigil | Game AI (poker, StarCraft); cybersecurity |
| **Halong-halong** | Ang ilang mga ahente ay nakikipagtulungan, ang iba ay nakikipagkumpitensya | Mga merkado ng auction; mga sistema ng trapiko |
| Algorithm | Paglalarawan |
|-----------|-------------|
| **MADDPG** | Multi-agent na bersyon ng DDPG; sentralisadong kritiko, desentralisadong aktor |
| **MAPPO** | Multi-agent PPO; malawakang ginagamit sa pagsasanay |
| **Self-Play** | Nagsasanay ang mga ahente laban sa mga kopya ng kanilang sarili (AlphaGo, AlphaStar) |
---

## Sim-to-Real Transfer
Ang pagsasanay sa mga robot sa totoong mundo ay mabagal at mapanganib. Sa halip, ang mga ahente ay nagsasanay sa simulation at lumipat sa katotohanan.
| Hamon | Solusyon |
|-----------|----------|
| **Reality gap** (simulation ≠ totoong mundo) | Pag-randomization ng domain: iba-iba ang mga parameter ng physics sa panahon ng pagsasanay |
| **Sample inefficiency** | Gumamit ng RL na nakabatay sa modelo o magsanay sa malalaking parallel simulation |
| **Kaligtasan** | Constrained RL: parusahan ang mga hindi ligtas na aksyon sa panahon ng pagsasanay |
| **Bahagyang pagmamasid** | Magsanay gamit ang mga maingay na sensor at naantala na mga obserbasyon |
Ang mga kumpanya tulad ng Boston Dynamics at Tesla ay gumagamit ng simulation nang husto, ngunit ang agwat sa pagitan ng simulate at pisikal na pagganap ay nananatiling isa sa mga pinakamalaking hamon sa larangan.
---

## Mga Tool at Framework
| Tool | Layunin | Pinakamahusay Para sa |
|------|---------|----------|
| **Stable-Baselines3** | Malinis na pagpapatupad ng Python ng PPO, SAC, TD3, DQN | Pag-aaral at prototyping |
| **RLlib** | Scalable RL library na binuo sa Ray | Malaking-scale na ipinamahagi na pagsasanay |
| **CleanRL** | Mga pagpapatupad ng solong file para sa pananaliksik | Malalim na pag-unawa sa mga algorithm |
| **Gymnasium (OpenAI)** | Standardized environment interface | Pagtukoy sa mga problema sa RL |
| **Isaac Gym / Isaac Lab** | GPU-accelerated physics simulation | Robotics, sim-to-real |
| **TRL** (Transformer RL Library) | RLHF, DPO, PPO para sa mga modelo ng wika | Pag-align ng mga LLM |
| **OpenRLHF** | Ibinahagi na balangkas ng RLHF | Pagsasanay ng malalaking modelo gamit ang RLHF |
---

## Mga Praktikal na Tip
- **Magsimula sa PPO.** Ito ang pinaka maaasahang pangkalahatang layunin na algorithm. Kung hindi ka sigurado kung ano ang gagamitin, PPO ang default.
- **I-normalize ang iyong mga reward.** Ang pag-scale ng reward ay lubhang nakakaapekto sa katatagan ng pagsasanay.
- **Gumamit ng mga naka-vector na kapaligiran.** Ang pagpapatakbo ng maraming kapaligiran nang magkatulad (hal., 8–64) ay nagpapatatag ng mga pagtatantya ng gradient at napakabilis ng pagsasanay.
- **Subaybayan ang parehong reward at entropy.** Kung ang entropy ay bumaba sa zero, ang iyong ahente ay tumigil sa paggalugad at maaaring ma-stuck sa isang lokal na pinakamainam.
- **Ang paghubog ng reward ay isang sining.** Ang pagdidisenyo ng tamang function ng reward ay kadalasang pinakamahirap na bahagi. Ang mga kalat-kalat na reward (sa dulo lang) ay nagpapabagal sa pag-aaral. Ang siksik at mahusay na hugis na mga reward ay gumagabay sa ahente ngunit maaaring magpakilala ng hindi sinasadyang pag-uugali.
- **Ang RLHF ay marupok.** Ang maliliit na pagbabago sa reward model o PPO hyperparameter ay maaaring magdulot ng malalaking pagbaba ng kalidad. Ang DPO ay isang mas matatag na alternatibo kung hindi mo kailangan ang buong pipeline ng RLHF.
---

## Buod
Ang reinforcement learning ay ang pag-aaral kung paano natututo ang mga ahente na gumawa ng mga desisyon sa pamamagitan ng pakikipag-ugnayan. Ito ay mula sa mga klasikal na algorithm tulad ng Q-learning hanggang sa mga modernong deep RL na pamamaraan tulad ng PPO at SAC, at pinapatibay nito ang ilan sa pinakamahalagang kamakailang pagsulong sa AI — mula sa paglalaro hanggang sa pagkakahanay ng modelo ng wika. Ang pangunahing hamon ay nananatiling pareho: paano mo matututo ang pinakamainam na gawi kapag ang feedback ay naantala, kalat-kalat, at maingay? Ang sagot — trial and error, na ginagabayan ng matalinong matematika — ay lumalabas na isa sa pinakamakapangyarihang ideya sa lahat ng artificial intelligence.