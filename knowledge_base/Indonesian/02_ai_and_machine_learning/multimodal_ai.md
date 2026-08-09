---
# Metadata
title: "Multimodal AI"
description: "Vision-language models, CLIP, DALL-E, cross-modal learning"
category: "AI and Machine Learning"
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
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [multimodal, ai, ai-and-machine-learning]
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
# AI multimoda
Sistem AI multimodal memproses dan menggabungkan informasi dari berbagai jenis data — teks, gambar, audio, video, dan lainnya — secara bersamaan. Meskipun sistem AI sebelumnya biasanya menggunakan modalitas tunggal (hanya teks, hanya gambar), sistem modern yang paling mampu adalah multimodal. GPT-4V membaca gambar dan teks secara bersamaan; Gemini memproses teks, gambar, audio, dan video secara asli; dan sistem seperti Sora menghasilkan video dari deskripsi teks. File ini membahas cara kerja AI multimodal, arsitektur di baliknya, dan mengapa menggabungkan modalitas sangat bermanfaat.
---

## Mengapa Multimoda?
| Manfaat | Deskripsi | Contoh |
|---------|-------------|---------|
| **Pemahaman yang lebih kaya** | Modalitas yang berbeda memberikan informasi yang saling melengkapi | Video menyampaikan gerakan, suara, dan konteks yang tidak dapat dilakukan oleh teks saja |
| **Generalisasi yang lebih baik** | Pembelajaran lintas modalitas menciptakan representasi yang lebih kuat | Model yang telah melihat gambar dan deskripsi teks "kucing" memahami konsep dengan lebih baik |
| **Interaksi yang lebih alami** | Manusia berkomunikasi melalui berbagai saluran | Asisten suara yang melihat apa yang Anda tunjuk |
| **Transfer lintas moda** | Pengetahuan dari satu modalitas membantu modalitas lainnya | Pemahaman gambar meningkatkan pembuatan teks, dan sebaliknya |
---

## Arsitektur Inti
### Model Bahasa Visi (VLM)
Model yang memproses gambar dan teks secara bersamaan.
| Arsitektur | Cara Kerja | Contoh |
|-------------|-------------|---------|
| **Encoder ganda** | Pisahkan encoder untuk gambar dan teks; gabungkan di tahap selanjutnya | KLIP, SEJARAH |
| **Encoder fusi** | Token gambar dan teks disisipkan dan diproses bersama | Flamingo, Gemini |
| **Perhatian silang** | Token teks memperhatikan fitur gambar (atau sebaliknya) | Flamingo, CoCa |
| **Tokeniser terpadu** | Gambar dikonversi menjadi token dan diproses bersama token teks | Gemini, Bunglon |
### Cara Kerja Model Bahasa Visi
| Langkah | Deskripsi |
|------|-------------|
| **1. Enkode gambar** | Encoder visi (ViT, SigLIP) mengubah gambar menjadi sekumpulan vektor fitur |
| **2. Menyandikan teks** | Encoder bahasa memproses token teks |
| **3. Modalitas sekering** | Fitur gambar diproyeksikan ke dalam ruang penyematan model bahasa |
| **4. Hasilkan** | Model bahasa menghasilkan teks yang dikondisikan pada input gambar dan teks |
### Model Bahasa Visi Utama
| Model | Pengembang | Arsitektur | Fitur Penting |
|-------|-----------|-------------|-----------------|
| **KLIP** | OpenAI | Encoder ganda (ViT + encoder teks) | Klasifikasi gambar zero-shot melalui teks |
| **LLaVA** | Sumber terbuka | Encoder visual LLaMA + CLIP | VLM sumber terbuka; komunitas yang kuat |
| **GPT-4V / 4o** | OpenAI | Multimoda terpadu | Memproses teks, gambar, audio bersama-sama |
| **Gemini** | Google DeepMind | Multimodal asli dari pelatihan | Dibangun untuk multimoda dari awal |
| **Claude** | Antropik | Visi + teks | Kuat dalam pemahaman dokumen dan bagan |
| **Qwen-VL** | Alibaba | VLM berbobot terbuka | Kompetitif dengan model tertutup |
| **MagangVL** | Sumber terbuka | Encoder visi multi-skala | Opsi sumber terbuka yang kuat |
---

## Model Audio dan Ucapan
### Pengenalan Ucapan (ASR)
| Model | Arsitektur | Fitur Penting |
|-------|-------------|-----------------|
| **Bisikan** (OpenAI) | Transformator encoder-decoder | Dilatih dengan audio multibahasa 680 ribu jam; kuat |
| **Konformer** | Konvolusi + perhatian diri | Menggabungkan fitur lokal dan global |
| **wav2vec 2.0** | Diawasi sendiri | Belajar dari ucapan yang tidak diberi label |
| **USM** (Google) | Model pidato universal | 2 juta jam data berlabel; 300+ bahasa |
### Teks-ke-Ucapan (TTS)
| Model | Pendekatan | Fitur Penting |
|-------|----------|-----------------|
| **VALL-E** (Microsoft) | Kodek saraf | Kloning suara dari sampel 3 detik |
| **Kulit** (Suno) | Berbasis transformator | Multibahasa; termasuk suara non-ucapan |
| **SebelasLabs** | Komersial | Kloning suara berkualitas tinggi |
| **ObrolanTTS** | Sumber terbuka | Pidato percakapan dengan prosodi natural |
| **Pidato Ikan** | Sumber terbuka | Multibahasa; inferensi cepat |
### Pemahaman Audio
| Model | Kemampuan |
|-------|-----------|
| **AudioLDM** | Pembuatan efek suara dari teks |
| **Gen Musik** (Meta) | Generasi teks-ke-musik |
| **Qwen-Audio** | Pemahaman audio (ucapan, musik, suara lingkungan) |
| **SALMON** | Pemahaman ucapan, audio, bahasa, musik, dan kebisingan |
---

## Model Video
Video menggabungkan gambar, audio, teks, dan waktu — menjadikannya modalitas yang paling kompleks.
| Model | Ketik | Kemampuan |
|-------|------|-------------|
| **Sora** (OpenAI) | Teks-ke-video | Hingga 1080p; memahami fisika |
| **Gemini** | Pemahaman video | Dapat menganalisis video panjang dengan audio |
| **Video-LLaVA** | Video + teks | Pemahaman video sumber terbuka |
| **Landasan Pacu Gen-3** | Teks/gambar-ke-video | Pembuatan video komersial |
| **Kling** | Teks-ke-video | Pembuatan video berdurasi panjang |
### Tantangan Pemahaman Video
| Tantangan | Deskripsi |
|-----------|-------------|
| **Penalaran sementara** | Memahami peristiwa yang terjadi seiring berjalannya waktu |
| **Konteks panjang** | Video bisa berdurasi berjam-jam; memproses semua frame itu mahal |
| **Sinkronisasi audio-visual** | Menghubungkan apa yang dikatakan dengan apa yang ditampilkan |
| **Kausalitas** | Memahami sebab akibat dalam rangkaian video |
---

## Pengambilan Lintas Modal
Menemukan konten yang relevan di berbagai modalitas.
| Tugas | Deskripsi | Contoh |
|------|-------------|---------|
| **Teks ​​→ Gambar** | Temukan gambar yang cocok dengan kueri teks | Cari "matahari terbenam di atas pegunungan" di perpustakaan foto |
| **Gambar → Teks** | Temukan teks yang relevan dengan gambar | Menghasilkan keterangan untuk gambar |
| **Teks ​​→ Audio** | Temukan suara yang cocok dengan deskripsi | Desain suara: "langkah kaki di atas kerikil" |
| **Gambar → Gambar** | Temukan gambar yang mirip secara visual | Pencarian produk berdasarkan gambar |
### CLIP untuk Pengambilan Lintas Modal
Ruang penyematan bersama CLIP memungkinkan pengambilan lintas modal zero-shot:
| Langkah | Deskripsi |
|------|-------------|
| 1 | Encode semua gambar dengan vision encoder |
| 2 | Enkode kueri teks dengan pembuat enkode teks |
| 3 | Hitung kesamaan kosinus antara penyematan teks dan semua penyematan gambar |
| 4 | Kembalikan gambar dengan kemiripan tertinggi |
Ini berfungsi tanpa pelatihan khusus tugas apa pun — properti yang disebut kemampuan **zero-shot**.
---

## AI yang diwujudkan
AI yang diwujudkan menggabungkan persepsi multimodal dengan tindakan fisik.
| Sistem | Modalitas | Aplikasi |
|--------|----------|-------------|
| **RT-2** (Google) | Visi + bahasa → aksi robot | Kontrol robot serba guna dari instruksi teks |
| **Okto** | Kebijakan robot sumber terbuka | Dilatih pada beragam data robot |
| **Tesla Optimus** | Visi + bahasa → tugas fisik | Robot humanoid untuk tugas umum |
| **Gambar 01** | Penglihatan + bahasa + ucapan | Robot humanoid dengan kemampuan percakapan |
### Tantangan dalam AI yang Terwujud
| Tantangan | Mengapa Sulit |
|-----------|--------------|
| **Kesenjangan sim-ke-nyata** | Simulasi tidak secara sempurna menangkap fisika dunia nyata |
| **Ketangkasan** | Pengendalian motorik halus (tangan, jari) sangat sulit |
| **Keamanan** | Robot fisik dapat menyebabkan kerusakan nyata |
| **Pemrosesan waktu nyata** | Harus memahami, memutuskan, dan bertindak dalam milidetik |
| **Generalisasi** | Robot yang dilatih untuk mengambil cangkir merah mungkin gagal pada cangkir biru |
---

## Data dan Pelatihan
### Data Pelatihan Multimoda
| Kumpulan data | Modalitas | Ukuran |
|---------|-----------|------|
| **LAION-5B** | Pasangan gambar-teks | 5,85 miliar pasang |
| **Komputasi Data** | Teks gambar yang dikurasi | Tolok ukur untuk desain kumpulan data |
| **CERITA** (Wikipedia) | Gambar-teks dari Wikipedia | 11,5 juta pasang |
| **Cara100M** | Teks video (video petunjuk) | 100 juta klip |
| **LibriSpeech** | Teks pidato | 1.000 jam bahasa Inggris |
| **Suara Umum** | Teks pidato | Multibahasa; kontribusi komunitas |
### Strategi Pelatihan
| Strategi | Deskripsi | Kapan Menggunakan |
|----------|-------------|-------------|
| **Pelatihan bersama** | Latih semua modalitas secara bersamaan | Ketika Anda telah menyelaraskan data multimodal |
| **Pembelajaran Kurikulum** | Mulailah dengan contoh mudah; meningkatkan kesulitan | Meningkatkan konvergensi |
| **Pembelajaran kontrastif** | Belajar mencocokkan pasangan terkait di seluruh modalitas (gaya CLIP) | Membangun representasi bersama |
| **Penyetelan instruksi** | Melatih pasangan instruksi-respons multimodal | Pembuatan model mengikuti instruksi multimodal |
---

## Evaluasi
| Tolok Ukur | Modalitas | Apa yang Diuji |
|-----------|-----------|---------------|
| **MMLU** | Teks | Pengetahuan di 57 mata pelajaran |
| **MMMU** | Teks + gambar | Penalaran tingkat perguruan tinggi dengan diagram |
| **MathVista** | Teks + gambar | Penalaran matematis dengan data visual |
| **Video-MME** | Teks + video | Pemahaman video dan penalaran temporal |
| **HELM** | Teks + audio | Evaluasi multimodal konteks panjang |
| **bangku SWE** | Teks + kode | Tugas rekayasa perangkat lunak dunia nyata |
---

## Ringkasan
AI multimodal mewakili peralihan dari model tujuan tunggal ke sistem yang memahami dan menalar semua bentuk data. Model bahasa visi seperti GPT-4V dan Gemini dapat memahami gambar dan teks secara bersamaan; model ucapan seperti Whisper dan VALL-E menangani audio; model video mulai memproses kompleksitas penuh gambar bergerak dengan suara. Trennya jelas: sistem AI yang paling mumpuni di masa depan akan bersifat multimodal, yang memproses semua jenis informasi secara bersamaan. Tantangannya – penyelarasan data, biaya komputasi, evaluasi, dan penerapan yang diterapkan – sangatlah besar, namun kemajuan pada tahun 2024–2026 sangat pesat.