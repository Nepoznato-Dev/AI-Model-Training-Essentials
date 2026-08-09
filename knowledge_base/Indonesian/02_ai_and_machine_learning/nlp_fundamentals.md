---
# Metadata
title: "NLP Fundamentals"
description: "Text processing, embeddings, Transformers, BERT, GPT"
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
tags: [nlp, ai-and-machine-learning]
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
# Dasar-Dasar NLP
Natural Language Processing (NLP) adalah bidang mesin pengajaran untuk memahami, menghasilkan, dan bekerja dengan bahasa manusia. Ini mendukung mesin pencari, chatbot, sistem terjemahan, analisis sentimen, dan model bahasa besar (LLM) yang telah mengubah AI sejak tahun 2020. File ini mencakup evolusi dari teknik klasik ke arsitektur modern berbasis Transformer.
---

## Pemrosesan Awal Teks
Teks mentah berantakan. Sebelum model dapat menggunakannya, model tersebut perlu dibersihkan dan disusun.
| Langkah | Apa Fungsinya | Contoh |
|------|-------------|---------|
| **Tokenisasi** | Pisahkan teks menjadi token (kata, subkata, atau karakter) | "Saya suka NLP" →`["I", "love", "NLP"]`|
| **Menurunkan huruf** | Ubah menjadi huruf kecil | "Halo" → "halo" |
| **Hentikan penghapusan kata** | Hapus kata-kata umum (the, is, at) | "kucing duduk" → "kucing duduk" |
| **Membendung** | Potong akhiran kata (kasar) | "berlari" → "berlari" |
| **Lematisasi** | Dikurangi ke bentuk kamus (sadar konteks) | "lebih baik" → "baik" |
| **Normalisasi** | Perbaiki pengkodean, hapus karakter khusus, perluas kontraksi | "jangan" → "jangan" |
Model Transformer modern sering kali melewatkan penghapusan dan stemming stop word — model ini mempelajari pola ini dari data.
---

## Representasi Teks
Mesin membutuhkan angka, bukan kata-kata. Cara kami merepresentasikan teks sebagai vektor adalah hal mendasar.
### Pendekatan Klasik
| Metode | Deskripsi | Batasan |
|--------|-------------|-----------|
| **Pengkodean Satu-Panas** | Setiap kata adalah posisi unik dalam vektor besar | Jarang; tidak ada makna semantik |
| **Kantong Kata (BoW)** | Hitung frekuensi kata; abaikan pesanan | Kehilangan urutan kata seluruhnya |
| **TF-IDF** | Bobot kata berdasarkan frekuensi dalam dokumen × kelangkaan di seluruh korpus | Masih mengabaikan ketertiban dan konteks |
### Penyematan Kata
Penyematan memetakan kata-kata ke vektor padat di mana kata-kata serupa berdekatan.
| Model | Ide Kunci |
|-------|----------|
| **Word2Vec** (2013) | Memprediksi kata dari konteks (CBOW) atau konteks dari kata (Lewati-gram) |
| **Sarung Tangan** (2014) | Statistik kejadian bersama global → vektor padat |
| **Teks ​​Cepat** (2016) | Word2Vec + informasi subkata (menangani kata-kata langka dengan lebih baik) |
Contoh terkenal:`king - man + woman ≈ queen`. Penyematan menangkap hubungan semantik.
**Batasan**: penyematan klasik menetapkan satu vektor per kata, sehingga tidak dapat menangani polisemi (kata-kata dengan banyak makna). "Bank" di "tepi sungai" dan "rekening bank" mendapatkan vektor yang sama.
---

## Model Urutan
Sebelum Transformers, pendekatan standar NLP adalah memproses teks secara berurutan.
| Arsitektur | Cara Kerja | Kekuatan | Kelemahan |
|-------------|-------------|----------|----------|
| **RNN** | Memproses token satu per satu; pertahankan status tersembunyi | Menangani input dengan panjang variabel | Hilangnya gradien; tidak dapat menangkap ketergantungan yang panjang |
| **LSTM** | RNN dengan gerbang (lupa, masukan, keluaran) untuk mengontrol aliran informasi | Lebih baik dalam ketergantungan jangka panjang | Masih berurutan; lambat untuk berlatih |
| **GRU** | LSTM Sederhana (gerbang lebih sedikit) | Lebih cepat dari LSTM; kinerja serupa | Keterbatasan mendasar yang sama |
Model ini memproses teks dari kiri ke kanan, yang berarti model tersebut lambat untuk dilatih (tidak dapat diparalelkan) dan kesulitan dengan ketergantungan jangka panjang.
---

## Mekanisme Perhatian
Perhatian memungkinkan model melihat semua posisi secara berurutan dan memutuskan mana yang paling relevan untuk prediksi saat ini.
### Wawasan Utama
Alih-alih mengompresi seluruh kalimat menjadi satu keadaan tersembunyi (seperti yang dilakukan RNN), perhatian menghitung jumlah tertimbang dari semua keadaan tersembunyi, tempat bobotnya dipelajari.
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

| Komponen | Peran |
|-----------|------|
| **Permintaan (Q)** | Apa yang saya cari? |
| **Kunci (K)** | Apa yang saya isi? |
| **Nilai (V)** | Informasi apa yang saya berikan? |
| **√d_k** | Faktor penskalaan untuk mencegah produk titik besar |
---

## Arsitektur Transformator
The Transformer (Vaswani et al., 2017 — "Attention Is All You Need") menggantikan pengulangan sepenuhnya dengan perhatian. Ini adalah dasar dari hampir semua NLP modern.
### Arsitektur
| Komponen | Deskripsi |
|-----------|-------------|
| **Pembuat enkode** | Membaca teks masukan; menghasilkan representasi kontekstual |
| **Dekoder** | Menghasilkan teks keluaran; memperhatikan keluaran encoder |
| **Perhatian Diri** | Setiap token melayani semua token lainnya dalam urutan yang sama |
| **Perhatian Multi-Kepala** | Jalankan beberapa kepala perhatian secara paralel; menangkap hubungan yang berbeda |
| **Pengkodean Posisi** | Suntikkan informasi posisi (karena tidak ada pengulangan) |
| **Jaringan Pengumpanan** | Melamar ke setiap posisi secara mandiri |
| **Normalisasi Lapisan** | Stabilkan pelatihan |
| **Koneksi Sisa** | Lewati koneksi untuk aliran gradien |
### Khusus Encoder, Khusus Decoder, Encoder-Decoder
| Varian | Arsitektur | Terbaik Untuk | Contoh |
|---------|-------------|----------|---------|
| **Khusus encoder** | Memahami teks | Klasifikasi, NER, analisis sentimen | BERT, RoBERTa, DeBERTa |
| **Khusus dekoder** | Menghasilkan teks | Model bahasa, chatbots, pembuatan kode | GPT-3/4, LLaMA, Claude |
| **Encoder-Decoder** | Mengubah teks | Terjemahan, ringkasan | T5, BART, mBART |
---

## Keluarga Model Utama
### Keluarga BERT (Khusus Encoder)
| Model | Fitur Utama |
|-------|-------------|
| **BERT** (2018) | Model Bahasa Bertopeng + Prediksi Kalimat Berikutnya |
| **RoBERTa** | Menghapus NSP; dilatih lebih lama dengan lebih banyak data |
| **ALBERT** | Berbagi parameter; tapak lebih kecil |
| **DeBERTa** | Perhatian yang terurai; peningkatan NLU |
| **DistilBERT** | 40% lebih kecil, 60% lebih cepat, mempertahankan 97% kinerja BERT |
### Rangkaian GPT (Khusus Dekoder)
| Model | Parameter | Catatan |
|-------|-----------|-------|
| **GPT-2** | 1,5B | Model khusus dekoder yang ditampilkan dapat menghasilkan teks yang koheren |
| **GPT-3** | 175B | Pembelajaran singkat; diminta daripada disempurnakan |
| **GPT-3.5 / GPT-4** | Tidak diungkapkan | Disetel dengan instruksi + RLHF; percakapan |
| **LLaMA** (Meta) | 7B–70B | Berat terbuka; melahirkan ekosistem LLM sumber terbuka |
| **Mistral / Campuran** | 7B / 8×7B (MoE) | Model terbuka yang efisien dengan kinerja kuat |
---

## Tugas Inti NLP
| Tugas | Deskripsi | Model Khas |
|------|-------------|--------------|
| **Klasifikasi Teks** | Tetapkan label pada teks (spam/bukan spam, positif/negatif) | BERT, pengklasifikasi yang disempurnakan |
| **Pengenalan Entitas Bernama (NER)** | Identifikasi orang, organisasi, lokasi dalam teks | Lapisan BERT + CRF |
| **Analisis Sentimen** | Tentukan nada emosional | BERT yang disempurnakan atau LLM zero-shot |
| **Terjemahan Mesin** | Terjemahkan antar bahasa | T5, mBART, MarianMT |
| **Menjawab Pertanyaan** | Jawab pertanyaan sesuai konteks | BERT (ekstraktif), GPT (generatif) |
| **Ringkasan** | Padatkan teks panjang | T5, BART, GPT |
| **Pembuatan Teks** | Menghasilkan teks yang koheren | GPT-4, LLaMA, Claude |
---

## Penyempurnaan vs Anjuran
| Pendekatan | Cara Kerja | Kapan Menggunakan |
|----------|-------------|-------------|
| **Penyempurnaan** | Perbarui bobot model pada data khusus tugas Anda | Anda telah memberi label pada data; butuh performa maksimal |
| **Mendorong** | Berikan instruksi model dalam bahasa alami | Pembuatan prototipe cepat; data yang terbatas; menggunakan LLM |
| **Beberapa tembakan** | Sertakan contoh di prompt | Ketika Anda memiliki beberapa contoh tetapi tidak cukup untuk menyempurnakan |
| **LoRA / QLoRA** | Penyempurnaan yang efisien; perbarui matriks kecil peringkat rendah | Sempurnakan model besar dengan memori GPU terbatas |
---

## Alat dan Kerangka
| Alat | Tujuan |
|------|---------|
| **Memeluk Wajah Transformers** | Model terlatih, tokeniser, saluran penyempurnaan |
| **spaCy** | Pipeline NLP tingkat produksi (tokenisasi, NER, POS, ketergantungan) |
| **NLTK** | Pendidikan; algoritma NLP klasik |
| **Gensim** | Pemodelan topik (LDA), penyematan kata (Word2Vec, Doc2Vec) |
| **LangChain / LlamaIndex** | Kerangka kerja untuk membangun aplikasi yang didukung LLM |
| **vLLM** | Pelayanan LLM throughput tinggi |
| **Tokenizer (HF)** | Tokenisasi cepat (BPE, WordPiece, SentencePiece) |
---

## Lanskap LLM
Lanskap NLP modern didominasi oleh Model Bahasa Besar:
| Kategori | Contoh | Catatan |
|----------|---------|-------|
| **Kepemilikan** | GPT-4, Claude, Gemini | Performa terbaik; Hanya akses API |
| **Berat terbuka** | LLaMA 3, Mistral, Qwen | Bobot tersedia; dijalankan secara lokal |
| **Sumber terbuka** | Pythia, MEMILIH | Terbuka penuh (data, bobot, kode) |
| **Multimoda** | GPT-4V, Gemini, LLaVA | Proses teks + gambar |
| **Khusus kode** | CodeLlama, StarCoder, DeepSeek Coder | Dilatih tentang kode |
| **Kecil / Efisien** | Phi-3, Gemma, TinyLlama | Kinerja yang kuat pada skala kecil |
Lapangan bergerak cepat. Apa yang mutakhir saat ini mungkin akan tergantikan dalam beberapa bulan. Dasar-dasarnya – perhatian, tokenisasi, penyesuaian, evaluasi – tetap stabil.