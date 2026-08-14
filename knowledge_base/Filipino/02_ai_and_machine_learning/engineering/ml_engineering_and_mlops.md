---
# Metadata
title: "ML Engineering and MLOps"
description: "Model serving, registries, deployment strategies, drift monitoring"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
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
    changes: "Moved to engineering/ subfolder; added subcategory field"
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
tags: [ml, engineering, mlops, ai-and-machine-learning]
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

# ML Engineering at MLOps
Ang pagbuo ng isang machine learning model ay kalahati lamang ng labanan. Pagpasok nito sa produksyon, pagpapanatiling mapagkakatiwalaan, pagsubaybay para sa drift, at pag-ulit dito — kung saan pumapasok ang ML engineering at MLOps. Sinasaklaw ng file na ito ang buong lifecycle mula sa eksperimento hanggang sa production system.
---

## Ang ML Lifecycle
| Yugto | Paglalarawan | Mga Pangunahing Aktibidad |
|-------|-------------|----------------|
| **1. Kahulugan ng Problema** | I-frame ang problema sa negosyo bilang isang ML na gawain | Tukuyin ang mga sukatan, mga hadlang, pamantayan ng tagumpay |
| **2. Pangongolekta ng Data** | Ipunin at lagyan ng label ang data ng pagsasanay | ETL, pag-label, pagpapalaki |
| **3. Eksperimento** | Sanayin at suriin ang mga modelo | Tampok na engineering, hyperparameter tuning |
| **4. Pagpili ng Modelo** | Piliin ang pinakamahusay na modelo | Ihambing ang mga sukatan, tasahin ang mga trade-off |
| **5. Deployment** | Ipadala ang modelo sa produksyon | Naghahatid ng imprastraktura, API, batch |
| **6. Pagsubaybay** | Abangan ang drift at degradation | Data drift, concept drift, performance |
| **7. Muling pagsasanay** | I-update ang modelo gamit ang bagong data | Naka-iskedyul o na-trigger na muling pagsasanay |
Karamihan sa halaga (at kahirapan) ay nasa mga yugto 5–7. Ang isang modelong nakaupo sa isang Jupyter notebook ay hindi lumilikha ng halaga ng negosyo.
---

## Mga Pattern ng Paghahatid ng Modelo
| Pattern | Paglalarawan | Latency | Use Case |
|---------|-------------|---------|----------|
| **Batch Inference** | Patakbuhin ang modelo sa isang batch ng data sa isang iskedyul | Oras | Pang-araw-araw na rekomendasyon, pagmamarka ng panloloko |
| **Online na Hinuha** | Real-time na hula sa bawat kahilingan | Milisecond | Ranggo ng paghahanap, real-time na pag-uuri |
| **Streaming Inference** | Iproseso ang mga hula sa isang stream ng data | Segundo | Pagtukoy ng anomalya, pagproseso ng kaganapan |
### Nagsisilbing Imprastraktura
| Tool | Uri | Pinakamahusay Para sa |
|------|------|----------|
| **TensorFlow Serving** | Server ng modelo | Mga modelo ng TensorFlow |
| **TorchServe** | Server ng modelo | Mga modelo ng PyTorch |
| **Triton Inference Server** | Multi-framework | Hinuha ng GPU, maraming balangkas |
| **vLLM** | LLM paghahatid | High-throughput LLM inference |
| **BentoML** | Pinag-isang paghahatid | Framework-agnostic deployment |
| **Seldon** | K8s-native | Pag-deploy ng modelo ng Kubernetes |
| **Ray Serve** | Nasusukat na paghahatid | Malaking modelo, ipinamahagi na hinuha |
---

## Mga Rehistro ng Modelo
Ang registry ng modelo ay isang sentralisadong tindahan para sa pamamahala ng mga modelo ng ML — ang kanilang mga bersyon, metadata, sukatan, at katayuan sa pag-deploy.
| Kakayahan | Paglalarawan |
|-----------|-------------|
| **Bersyon** | Subaybayan ang bawat bersyon ng modelo na may natatanging ID |
| **Metadata** | Data ng pagsasanay, hyperparameter, sukatan, may-akda |
| **Mga Stage Transition** | Ilipat ang mga modelo sa mga yugto: Staging → Production → Archive |
| **Lineage** | Sundan kung aling data at code ang gumawa ng bawat modelo |
| Tool | Paglalarawan |
|------|-------------|
| **MLflow** | Open-source; pagpapatala ng modelo + pagsubaybay sa eksperimento |
| **Mga Timbang at Mga Bias (W&B)** | Komersyal; pagsubaybay sa eksperimento + pagpapatala ng modelo |
| **DVC** | Pag-bersyon ng data at modelo gamit ang Git |
| **Azure ML / SageMaker** | Pamamahala ng modelo ng cloud-native |
---

## Pagsubaybay sa Eksperimento
Dapat na subaybayan ang bawat eksperimento sa ML: kung anong data ang ginamit, anong mga hyperparameter, anong mga sukatan ang nagresulta.
| Tool | Mga Pangunahing Tampok |
|------|-------------|
| **MLflow** | Open-source, self-host, sumusubaybay sa mga params/metrics/artifacts |
| **W&B** | Rich UI, sweeps, artifact versioning, mga ulat |
| **Neptune** | Metadata store para sa MLOps |
| **TensorBoard** | Itinayo sa TensorFlow; tingnan ang mga curve ng pagsasanay |
### Ano ang Subaybayan
| Kategorya | Mga halimbawa |
|----------|---------|
| **Mga Parameter** | Rate ng pagkatuto, laki ng batch, arkitektura ng modelo, bilang ng mga panahon |
| **Mga Sukatan** | Katumpakan, pagkawala, F1, AUC-ROC (bawat panahon at huling) |
| **Mga artifact** | Mga timbang ng modelo, mga confusion matrice, mga sample ng hula |
| **Data** | Bersyon ng dataset, mga split ratio, mga hakbang sa preprocessing |
| **Kapaligiran** | bersyon ng Python, mga bersyon ng library, hardware |
---

## Mga Istratehiya sa Pag-deploy ng Modelo
| Diskarte | Paano Ito Gumagana | Panganib |
|----------|-------------|------|
| **Pag-deploy ng Shadow** | Ang bagong modelo ay tumatakbo sa tabi ng luma; inihambing ang mga hula ngunit hindi inihatid | Walang panganib; nagpapatunay bago mag-live |
| **Canary Release** | Iruta ang maliit na % ng trapiko sa bagong modelo; unti-unting tumaas | Mababang panganib; mabilis na rollback |
| **A/B Testing** | Hatiin ang mga user sa pagitan ng luma at bago; ihambing ang mga sukatan ng negosyo | Sinusukat ang aktwal na epekto |
| **Asul-Berde** | Dalawang magkatulad na kapaligiran; ilipat ang lahat ng trapiko nang sabay-sabay | Instant rollback; dobleng gastos sa panahon ng paglipat |
| **Mga Flag ng Tampok** | I-toggle ang modelo sa on/off sa bawat segment ng user | Pinong-grained na kontrol |
---

## Pagsubaybay sa ML Systems
Ang mga ML system ay nangangailangan ng higit na pagsubaybay kaysa sa tradisyonal na software dahil ang data mismo ay maaaring magbago.
### Mga Uri ng Drift
| Uri ng Drift | Ano ang Nagbabago | Halimbawa |
|-----------|-------------|---------|
| **Data Drift** | Mga pagbabago sa pamamahagi ng input | Ang mga demograpiko ng customer ay nagbabago pagkatapos ng isang kampanya sa marketing |
| **Concept Drift** | Relasyon sa pagitan ng mga pagbabago sa input at output | Nagbabago ang gawi ng consumer sa panahon ng recession |
| **Label Drift** | Mga pagbabago sa target na pamamahagi | Tumataas ang rate ng pandaraya mula 1% hanggang 5% |
### Ano ang Susubaybayan
| Kategorya | Mga sukatan |
|----------|---------|
| **Pagganap ng Modelo** | Katumpakan, katumpakan, recall, F1, AUC (kumpara sa baseline) |
| **Kalidad ng Data** | Mga nawawalang halaga, mga pamamahagi ng tampok, mga outlier |
| **Drift Detection** | Mga istatistikal na pagsusulit (KS test, PSI, KL divergence) |
| **Imprastraktura** | Latency, throughput, paggamit ng GPU, memory |
| **Mga Sukatan ng Negosyo** | Rate ng conversion, epekto sa kita, kasiyahan ng user |
### Mga Tool sa Pagsubaybay
| Tool | Uri |
|------|------|
| **Maliwanag na AI** | Open-source na data drift at pagsubaybay sa pagganap ng modelo |
| **Grafana** | Dashboard visualization (gumagana sa Prometheus) |
| **WhyLabs** | Data observability platform |
| **Bumangon** | ML observability at root cause analysis |
| **Prometheus + Grafana** | Mga sukatan ng imprastraktura at aplikasyon |
---

## Reproducible na Pagsasanay
Ang reproducibility ay nangangahulugan na maaari kang muling magpatakbo ng isang eksperimento at makakuha ng parehong resulta. Mahalaga ito para sa pag-debug, pag-audit, at pagsunod.
### Mga Kinakailangan
| Kinakailangan | Paano Ito Makamit |
|-------------|--------------------|
| **Pag-bersyon ng data** | DVC, Delta Lake, o mga snapshot ng dataset na may mga hash |
| **Pag-bersyon ng code** | Git para sa lahat ng code ng pagsasanay |
| **Pagpi-pin sa kapaligiran** | `requirements.txt`,`conda env`, Docker images na may eksaktong mga bersyon |
| **Seed setting** | Ayusin ang mga random na buto para sa numpy, torch, tensorflow |
| **Pamamahala ng configuration** | Hydra, OmegaConf, o YAML na mga config para sa lahat ng hyperparameter |
| **Pagsubaybay sa artifact** | MLflow o W&B upang i-log ang bawat eksperimento |
---

## Pagsusukat ng Hinuha
Kapag ang isang modelo ay kailangang maghatid ng milyun-milyong kahilingan bawat araw, mahalaga ang pagganap.
| Teknik | Paglalarawan |
|-----------|-------------|
| **Batching** | Igrupo ang maramihang kahilingan sa iisang forward pass |
| **Quantization** | Bawasan ang katumpakan ng modelo (FP32 → INT8 o INT4) para sa mas mabilis na hinuha |
| **Paglilinis ng Modelo** | Sanayin ang isang mas maliit na modelo upang gayahin ang isang mas malaki |
| **Pruning** | Alisin ang mga hindi mahalagang timbang o neuron |
| **Pag-cache** | I-cache ang mga madalas na hula upang maiwasan ang muling pagkalkula |
| **GPU Optimization** | TensorRT, ONNX Runtime, Flash Attention |
| **Pahalang na Pagsusukat** | Magpatakbo ng maraming replika ng modelo sa likod ng isang load balancer |
---

## Mga Flag ng Tampok para sa ML
Hinahayaan ka ng mga feature na flag na kontrolin kung aling bersyon ng modelo ang ihahatid kung aling mga user, nang hindi muling ini-deploy.
| Use Case | Paglalarawan |
|----------|-------------|
| **Unti-unting paglulunsad** | Ihatid ang bagong modelo sa 5% ng mga user, pagkatapos ay dagdagan |
| **Kill switch** | Agad na bumalik sa nakaraang modelo kung may nakitang mga isyu |
| **Batay sa segment** | Iba't ibang modelo para sa iba't ibang segment ng user |
| **Eksperimento** | Mga variant ng modelo ng pagsubok ng A/B na may mga sukatan ng negosyo |
Mga Tool: LaunchDarkly, Unleash, Flagsmith, o simpleng mga flag ng feature na sinusuportahan ng database.
---

## Ang MLOps Maturity Curve
| Antas | Mga Katangian |
|-------|----------------|
| **Antas 0 — Manwal** | Manu-manong pagsasanay, manu-manong pag-deploy, walang pagsubaybay |
| **Antas 1 — Eksperimento** | Pagsubaybay sa eksperimento, pagpapatala ng modelo, pangunahing CI |
| **Antas 2 — Automation** | Automated retraining, CI/CD para sa mga modelo, automated na pagsubok |
| **Antas 3 — Buong Pipeline** | End-to-end automated pipeline na may pagsubaybay, drift detection, at auto-retraining |
Karamihan sa mga organisasyon ay nasa pagitan ng Level 0 at Level 1. Ang layunin ay Level 2–3, kung saan ang ML lifecycle ay automated at self-healing.