---
# Metadata
title: "Technology Glossary"
description: "Technical terminology (AI models, hardware, benchmarks)"
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
tags: [technology, glossary, coding-and-technology]
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
# Glosarium Teknologi
Glosarium referensi yang mencakup model AI, perangkat keras, tolok ukur, dan konsep inti
dalam lanskap AI dan komputasi modern.
---

## Model dan Asisten Bahasa AI
### ObrolanGPT
ChatGPT adalah chatbot AI yang dikembangkan oleh OpenAI, pertama kali dirilis pada November 2022.
Ini didukung oleh seri model bahasa besar (LLM) GPT. ChatGPT adalah salah satunya
salah satu produk AI konsumen dengan pertumbuhan tercepat dalam sejarah, mencapai 100 juta
pengguna dalam waktu dua bulan setelah peluncuran. Ini mendukung percakapan berbasis teks, kode
pembuatan, ringkasan, dan penulisan kreatif. Tingkatan berbayar menyediakan akses ke
model yang lebih kuat seperti GPT-4 dan GPT-4o.
### GPT (Transformator Terlatih Generatif)
GPT adalah rangkaian model bahasa besar yang dibuat oleh OpenAI. Arsitektur
menggunakan Transformer khusus decoder yang dilatih dengan tujuan prediksi token berikutnya
korpora teks besar. Versi utama mencakup GPT-2 (2019, parameter 1,5B, penting
untuk publisitas "terlalu berbahaya untuk dirilis"), GPT-3 (2020, parameter 175B, secara luas
digunakan melalui API), GPT-3.5 (tulang punggung ChatGPT asli), dan GPT-4
(2023, multimodal, kinerja mendekati tingkat keahlian manusia pada banyak tolok ukur).
### Claude
Claude adalah asisten AI yang dikembangkan oleh Anthropic. Namanya diambil dari nama Claude
Shannon, pendiri teori informasi. Anthropic didirikan oleh mantan
Peneliti OpenAI dan berfokus pada "AI konstitusional" — sebuah teknik yang harus dibuat
model lebih aman dengan melatih mereka untuk mengikuti serangkaian prinsip. Model Claude
(Claude 1, 2, 3 Haiku / Sonnet / Opus) dikenal dengan jendela konteks yang panjang (up
hingga 200.000 token), penalaran yang berbeda, dan mengurangi keluaran berbahaya dibandingkan dengan
LLM dasar.
### Gemini
Gemini adalah rangkaian model AI multimodal Google DeepMind, yang diumumkan pada
Desember 2023. Gemini pada dasarnya adalah multimodal — dilatih dari awal
teks, gambar, audio, dan video secara bersamaan, tidak seperti model sebelumnya
modalitas ditambahkan melalui fine-tuning. Versi termasuk Gemini Nano (di perangkat),
Gemini Flash (cepat, hemat biaya), dan Gemini Ultra (kemampuan tertinggi).
Gemini mendukung chatbot AI Google Bard (berganti nama menjadi Gemini) dan AI Google Penelusuran
Ikhtisar.
### Phi-3-mini
Phi-3-mini adalah model bahasa kecil (SLM) yang dikembangkan oleh Microsoft dengan 3.8B
parameter. Dirilis pada April 2026. Tidak seperti kebanyakan model besar, Phi-3-mini
dilatih pada kumpulan data "kualitas buku teks" yang dikuratori dengan cermat — sebuah teknik
dipelopori oleh Microsoft Research — yang memprioritaskan kualitas data dibandingkan volume mentah.
Meskipun jauh lebih kecil dari GPT-4 atau Claude 3 Opus, Phi-3-mini cocok atau
mengungguli model beberapa kali lebih besar pada tolok ukur penalaran seperti MMLU dan
Evaluasi Manusia. Ini mendukung jendela konteks token 4k dalam varian dasarnya dan 128k
jendela dalam varian konteks panjang. Phi-3-mini dapat berjalan pada satu GPU konsumen
atau bahkan di perangkat pada smartphone modern dengan RAM yang memadai.
### Lama (Meta AI)
Llama (Large Language Model Meta AI) adalah rangkaian model bobot terbuka
dirilis oleh Meta. Llama 2 (2023) dirilis untuk penelitian dan penggunaan komersial
dengan ukuran mulai dari parameter 7B hingga 70B. Llama 3 (2026) ditingkatkan
kinerja secara signifikan, dengan model mulai dari 8B hingga 70B (dan lebih baru 400B+).
Karena bobotnya dapat diunduh secara publik, model Llama adalah fondasinya
untuk ekosistem besar dengan varian yang disesuaikan (Mistral, Alpaca, Vicuna, dll.)
dan banyak digunakan untuk penerapan AI lokal/pribadi.
### Mistral
Mistral AI adalah perusahaan AI Perancis yang mengembangkan LLM terbuka dan berpemilik.
Mistral 7B (2023) menunjukkan bahwa model parameter 7B dapat menandingi
kinerja model yang jauh lebih besar menggunakan teknik efisien seperti geser
perhatian jendela dan perhatian kueri yang dikelompokkan. Mixtral 8x7B (2026) adalah campuran-
model pakar — merutekan setiap token ke subset dari 8 jaringan pakar,
mencapai performa tingkat GPT-3,5 sekaligus lebih murah secara komputasi.
Model Mistral sepenuhnya terbuka dan dapat dijalankan secara lokal.
---

## Perangkat Keras GPU dan Kartu Grafis
### GPU (Unit Pemrosesan Grafis)
GPU adalah prosesor yang dirancang untuk komputasi paralel besar-besaran. Awalnya
dibuat untuk merender grafik 3D, GPU menjadi penting untuk pelatihan AI/ML
dan inferensi karena mereka dapat melakukan ribuan operasi floating-point
secara bersamaan menggunakan ribuan inti kecil. Dua produsen GPU utama
untuk AI adalah NVIDIA dan AMD.
### Seri NVIDIA GeForce RTX
Seri RTX (Ray Tracing Texel eXtreme) adalah lini GPU konsumen NVIDIA. RTX
Generasi 30xx (Ampere, 2020) dan RTX 40xx (Ada Lovelace, 2022) meliputi
Tensor Cores khusus untuk mempercepat operasi AI. VRAM (RAM video) adalah
penting untuk menjalankan model AI secara lokal — GPU 8GB dapat menangani parameter 7B
model dalam kuantisasi 4-bit; GPU 24GB dapat menangani model 70B dalam 4-bit.
### NVIDIA Seri A dan Seri H (Pusat Data)
A100 (Ampere, 2020) dan H100 (Hopper, 2022) adalah AI profesional NVIDIA
akselerator. H100 memiliki memori HBM3 hingga 80GB dan merupakan standarnya
perangkat keras di balik sebagian besar pelatihan LLM skala besar saat ini. GPU ini berharga $25.000–
Masing-masing $40.000 tetapi menawarkan 10–30× throughput AI pada kartu RTX konsumen.
### Seri AMD Radeon RX
Jajaran GPU konsumen AMD. RX 7900 XTX (2022) memiliki VRAM 24GB dan dapat dijalankan
LLM lokal melalui ROCm (tumpukan komputasi GPU AMD). GPU AMD umumnya lebih sedikit
didukung lebih baik dibandingkan NVIDIA untuk kerangka kerja AI, meskipun dukungannya semakin meningkat.
### Intel Busur
Intel Arc merupakan lini produk GPU diskrit Intel yang dirilis mulai tahun 2022. Arc
GPU mendukung XeSS (super-sampling Intel) dan memiliki dukungan terbatas namun terus berkembang
untuk tugas inferensi AI melalui kerangka OpenVINO dan IPEX-LLM.
### BAHTERA Intel (ark.intel.com)
ARK adalah database spesifikasi produk resmi Intel di ark.intel.com. Itu
memberikan spesifikasi teknis terperinci untuk setiap CPU Intel, GPU, FPGA, dan
Produk NUC, termasuk jumlah inti, kecepatan clock, TDP, jenis memori yang didukung,
dan fitur set instruksi. Saat Anda mendengar "periksa spesifikasi ARK", itu artinya
mengunjungi database itu untuk informasi perangkat keras resmi.
---

## Tolok Ukur Kinerja AI
### MMLU (Pemahaman Bahasa Multitask Besar-besaran)
MMLU adalah tolok ukur yang menguji pengetahuan LLM di 57 mata pelajaran akademik termasuk
matematika, sejarah, hukum, kedokteran, dan ilmu komputer. Terdiri dari
pertanyaan pilihan ganda yang diambil dari ujian tingkat universitas yang sebenarnya. Skor
70% kira-kira adalah tingkat sarjana manusia; Skor GPT-4 dan Claude 3 di atas 86%.
Phi-3-mini mendapat skor sekitar 70% meskipun ukurannya kecil.
### ManusiaEval
HumanEval adalah tolok ukur OpenAI untuk pembuatan kode. Ini terdiri dari 164 Python
masalah pemrograman dengan kasus uji otomatis. Model diukur
pass@k — probabilitas bahwa setidaknya satu dari k solusi yang dihasilkan lolos semuanya
tes. Skor GPT-4 ~87% (lulus@1); model 7B yang disesuaikan dengan baik dapat mencapai ~50–60%.
### HellaSwag
HellaSwag adalah tolok ukur penalaran yang masuk akal. Model diberi kalimat
menggambarkan aktivitas duniawi dan harus memilih kelanjutan yang paling mungkin
empat pilihan. Opsi yang salah dirancang khusus agar masuk akal namun
agak salah. Ini menguji apakah suatu model memiliki pemahaman fisik yang mendasar
dan situasi sosial.
### ARC (Tantangan Penalaran AI2)
ARC adalah tolok ukur dari Allen Institute for AI. Terdiri dari sekolah dasar
pertanyaan sains, dibagi menjadi set "Mudah" dan "Tantangan". Tantangan ditetapkan
berisi soal-soal yang pengambilannya berbasis metode dan model statistik sederhana
berjuang dengan, membutuhkan penalaran multi-langkah.
---

## Konsep Inti AI/ML
### RAG (Generasi Pengambilan Augmented)
RAG adalah teknik yang menggabungkan sistem pengambilan (biasanya vektor
database) dengan model bahasa. Daripada hanya mengandalkan model saja
pengetahuan parametrik, RAG pertama-tama mengambil dokumen yang relevan dari eksternal
basis pengetahuan dan kemudian memasukkannya ke dalam konteks model. Hal ini memungkinkan
model untuk menjawab pertanyaan tentang informasi terkini atau spesifik domain
tanpa pelatihan ulang. Potato.ai menggunakan bentuk RAG — yang diambil dari KB-nya
dan memasukkan hasilnya ke dalam konteks sebelum menghasilkan respons.
### Penyempurnaan
Penyempurnaan adalah proses melanjutkan pelatihan model yang telah dilatih sebelumnya pada a
kumpulan data khusus domain yang lebih kecil. Ini menyesuaikan bobot model untuk a
tugas atau domain tertentu. Misalnya, LLM dasar mungkin dapat disesuaikan
rekam medis untuk membuat asisten tanya jawab medis. Penyempurnaan adalah
mahal secara komputasi tetapi jauh lebih murah daripada pelatihan dari awal.
### Kuantisasi
Kuantisasi mengurangi presisi numerik bobot model (misalnya dari 32-bit
float ke bilangan bulat 4-bit). Hal ini secara signifikan mengurangi jejak memori — model 7B
dalam presisi 16-bit membutuhkan ~14GB VRAM; model yang sama dalam 4-bit (format GGUF)
membutuhkan ~4GB. Kuantisasi biasanya menghasilkan akurasi yang kecil namun dapat diterima
degradasi dan merupakan teknik utama yang memungkinkan model besar dijalankan pada konsumen
perangkat keras atau bahkan perangkat seluler.
### Jendela Konteks
Jendela konteks adalah jumlah maksimum token yang dapat diproses oleh suatu model sekaligus,
termasuk prompt dan respons yang dihasilkan. GPT-3.5 memiliki 4.096 token
jendela; GPT-4 Turbo dan Claude 3 mendukung 128,000 token; Gemini 1.5 Pro
mendukung 1.000.000 token. Jendela konteks yang lebih besar memungkinkan model untuk "melihat"
lebih banyak percakapan atau dokumen sekaligus, sehingga meningkatkan koherensi dalam jangka panjang
pertukaran.
### RLHF (Pembelajaran Penguatan dari Umpan Balik Manusia)
RLHF adalah teknik pelatihan yang mengubah model bahasa dasar (yang
cukup memprediksi token berikutnya) menjadi asisten yang mengikuti instruksi dan
berperilaku membantu. Keluaran model penilai manusia dinilai, model penghargaan dilatih
berdasarkan preferensi mereka, dan model bahasa kemudian dioptimalkan untuk hal ini
model penghargaan menggunakan pembelajaran penguatan. ChatGPT, Claude, dan Gemini semuanya menggunakan
varian RLHF atau teknik penyelarasan serupa (misalnya AI Konstitusional,
Optimasi Preferensi Langsung).
### Arsitektur Transformator
Transformer adalah arsitektur jaringan saraf yang mendasari semua LLM modern.
Diperkenalkan dalam makalah tahun 2017 "Attention Is All You Need" oleh Vaswani dkk., itu
menggunakan mekanisme perhatian mandiri untuk memproses semua token secara paralel
secara berurutan. Transformer khusus encoder (BERT) digunakan untuk memahami tugas;
Transformer khusus dekoder (GPT, Llama, Mistral) digunakan untuk tugas pembangkitan;
encoder-decoder Transformers (T5, BART) digunakan untuk penerjemahan dan ringkasan.
### Penyematan dan Basis Data Vektor
Penyematan adalah representasi numerik padat dari teks (atau gambar) yang dihasilkan oleh
sebuah jaringan saraf. Teks yang mirip secara semantik memiliki sisipan yang berdekatan
ruang vektor. Penyimpanan database vektor (ChromaDB, Pinecone, Weaviate, Qdrant).
penyematan ini dan mendukung perkiraan pencarian tetangga terdekat dengan cepat. Benar
tulang punggung penyimpanan sistem RAG, termasuk lapisan memori dingin Potato.ai.