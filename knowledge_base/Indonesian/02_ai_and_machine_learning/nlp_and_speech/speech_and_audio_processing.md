<!--
---
# Metadata
title: "Speech and Audio Processing"
description: "ASR, TTS, audio features, Whisper, speech pipelines"
category: "AI and Machine Learning"
subcategory: "NLP and Speech"
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
    changes: "Moved to nlp_and_speech/ subfolder; added subcategory field"
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
tags: [speech, audio, processing, ai-and-machine-learning]
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

-->
# Pemrosesan Pidato dan Audio
Pemrosesan ucapan dan audio mencakup teknologi yang memungkinkan mesin mendengar, memahami, menghasilkan, dan memanipulasi suara. Hal ini mencakup pengenalan ucapan (mengubah kata-kata yang diucapkan menjadi teks), sintesis ucapan (mengubah teks menjadi kata-kata yang diucapkan), identifikasi pembicara, pembuatan musik, dan pemahaman suara lingkungan. Bidang ini telah diubah melalui pembelajaran mendalam — sistem modern mendekati akurasi tingkat manusia untuk pengenalan ucapan dan menghasilkan suara sintetis yang sangat alami.
---

## Dasar-Dasar Audio Digital
Suara adalah gelombang tekanan. Untuk memprosesnya secara digital, kami mengambil sampel gelombang secara berkala.
| Konsep | Deskripsi | Nilai Khas |
|---------|-------------|---------------|
| **Tingkat sampel** | Berapa kali per detik bunyi diukur | 8 kHz (telepon), 16 kHz (ucapan), 44,1 kHz (CD), 48 kHz (profesional) |
| **Kedalaman sedikit** | Presisi setiap sampel | 16-bit (CD), 24-bit (profesional), 32-bit float (pemrosesan) |
| **Saluran** | Mono (1), stereo (2), surround (5.1, 7.1) | Stereo untuk musik; mono untuk pidato |
| **Durasi** | Panjang audio | Bervariasi |
Rekaman mono 1 menit pada 16 kHz, 16-bit = 1,92 MB. Lagu stereo 3 menit pada 44,1 kHz, 16-bit = 30,3 MB.
---

## Ekstraksi Fitur Audio
Bentuk gelombang audio mentah sulit digunakan secara langsung oleh model. Kami mengekstrak fitur yang menangkap karakteristik penting suara.
| Fitur | Apa yang Ditangkapnya | Kasus Penggunaan |
|---------|-----------------|----------|
| **Spektogram mel** | Konten frekuensi dari waktu ke waktu, dipetakan ke persepsi pendengaran manusia | Pengenalan ucapan, klasifikasi musik |
| **MFCC** (Koefisien Cepstral Frekuensi Mel) | Representasi ringkas dari selubung spektral | Pengenalan ucapan tradisional |
| **Kromagram** | Distribusi kelas nada (not mana yang dimainkan) | Analisis musik, deteksi akord |
| **Tingkat zero-crossing** | Seberapa sering sinyal melewati nol | Deteksi bersuara vs tidak bersuara |
| **Energi RMS** | Kerasnya sinyal seiring waktu | Deteksi aktivitas suara |
| **Pitch (F0)** | Frekuensi dasar | Identifikasi pembicara, transkripsi musik |
### Spektogram Mel
Representasi audio paling umum untuk pembelajaran mendalam. Ini mengubah audio menjadi format seperti gambar 2D:
| Sumbu | Mewakili |
|------|-----------|
| **Sumbu X** | Waktu |
| **Sumbu Y** | Frekuensi (pada skala Mel — jarak persepsi) |
| **Warna/intensitas** | Energi pada frekuensi dan waktu tersebut |
Skala Mel mendekati pendengaran manusia: kita lebih baik dalam membedakan frekuensi rendah dibandingkan frekuensi tinggi.
---

## Pengenalan Ucapan Otomatis (ASR)
ASR mengubah bahasa lisan menjadi teks. Ini adalah salah satu aplikasi audio AI yang paling penting secara komersial.
### Evolusi ASR
| Zaman | Pendekatan | Batasan |
|-----|----------|------------|
| **Pra-2010** | Model Markov Tersembunyi + Model Campuran Gaussian | Diperlukan rekayasa tangan yang ekstensif; miskin dalam kondisi bising |
| **2010-2015** | Hibrida DNN-HMM | Jaringan saraf menggantikan GMM; peningkatan yang signifikan |
| **2015-2020** | Model ujung ke ujung (Deep Speech, LAS) | Jaringan saraf tunggal dari audio ke teks |
| **2020+** | Berbasis Transformer (Whisper, Conformer) | Akurasi tercanggih; multibahasa; kuat |
### Model ASR Utama
| Model | Arsitektur | Data Pelatihan | Fitur Penting |
|-------|-------------|---------------|-----------------|
| **Bisikan** (OpenAI) | Transformator encoder-decoder | 680.000 jam, 99 bahasa | Multibahasa; kuat terhadap aksen dan kebisingan; sumber terbuka |
| **Konformer** | Konvolusi + perhatian diri | Berbagai | Menggabungkan fitur lokal (konv) dan global (perhatian) |
| **wav2vec 2.0** | Transformator yang diawasi sendiri | Pidato tanpa label | Belajar dari audio mentah tanpa transkripsi |
| **USM** (Google) | Model pidato universal | 2 juta jam, 300+ bahasa | Sebagian besar bahasa tercakup |
| **MMS** (Meta) | Pidato Multibahasa Secara Besar-besaran | 1.400+ bahasa | Memperluas cakupan ke bahasa dengan sumber daya rendah |
### Metrik ASR
| Metrik | Deskripsi |
|--------|-------------|
| **WER** (Tingkat Kesalahan Kata) | Persentase kata yang salah ditranskripsi. Lebih rendah lebih baik. Performa manusia ~4-5% untuk bahasa Inggris yang bersih. |
| **CER** (Tingkat Kesalahan Karakter) | Sama seperti WER tetapi pada level karakter. Digunakan untuk bahasa tanpa batas kata (Cina, Jepang). |
### Tantangan Umum ASR
| Tantangan | Deskripsi |
|-----------|-------------|
| **Aksen dan dialek** | Performa turun secara signifikan untuk aksen non-standar |
| **Kebisingan latar belakang** | Musik, lalu lintas, speaker lain menurunkan akurasi |
| **Peralihan kode** | Penutur beralih antar bahasa di tengah kalimat |
| **Homofon** | "Di sana" vs "mereka" vs "mereka" — memerlukan konteks |
| **Tanda baca dan pemformatan** | Keluaran ASR biasanya tidak diberi tanda baca; membutuhkan pasca-pemrosesan |
| **Bahasa dengan sumber daya rendah** | Sebagian besar model berperforma buruk untuk bahasa dengan sedikit data pelatihan |
---

## Teks-ke-Ucapan (TTS)
TTS mengubah teks tertulis menjadi audio lisan. Sistem modern menghasilkan ucapan yang seringkali tidak dapat dibedakan dari rekaman manusia.
### Evolusi TTS
| Zaman | Pendekatan | Kualitas |
|-----|----------|---------|
| **Pra-2010** | Concatenative (menjahit fragmen rekaman) | Robot; ekspresi terbatas |
| **2010-2017** | Parametrik statistik (HMM, saraf awal) | Lebih baik tetapi masih dapat dikenali sebagai sintetis |
| **2017-2020** | Saraf (Tacotron, WaveNet) | Kualitas mendekati manusia; ekspresif |
| **2020+** | Codec saraf (VALL-E, Bark) | Kloning suara; beberapa tembakan; sangat alami |
### Model TTS Utama
| Model | Arsitektur | Fitur Penting |
|-------|-------------|-----------------|
| **WaveNet** (DeepMind) | Model generatif autoregresif | TTS pertama yang benar-benar terdengar natural |
| **Tacotron 2** (Google) | Seq2seq + vocoder | ujung ke ujung; kualitas tinggi |
| **VIT** | Inferensi variasional + pelatihan permusuhan | Cepat; kualitas bagus; banyak digunakan |
| **VALL-E** (Microsoft) | Model bahasa codec saraf | Kloning suara dari sampel 3 detik |
| **Kulit** (Suno) | Berbasis transformator | Multibahasa; suara non-ucapan (tawa, musik) |
| **SebelasLabs** | Komersial | Kloning suara terdepan di industri |
| **ObrolanTTS** | Sumber terbuka | Dioptimalkan untuk pidato percakapan |
| **Pidato Ikan** | Sumber terbuka | Cepat; multibahasa |
### Kloning Suara
Kloning suara menghasilkan suara sintetis yang terdengar seperti orang tertentu dari sampel audio pendek.
| Metode | Data yang Dibutuhkan | Kualitas |
|--------|------------|---------|
| **Penyempurnaan** | Pidato 10-60 menit | Kualitas tinggi; khusus pembicara |
| **Beberapa tembakan** | Pidato 3-30 detik | Kualitas bagus; pengaturan cepat |
| **Tembakan nol** | Tidak ada data pembicara target | Menggunakan audio referensi pada waktu inferensi |
**Kekhawatiran etis**: kloning suara dapat digunakan untuk peniruan identitas, penipuan, dan deepfake. Sebagian besar penyedia komersial memerlukan persetujuan suara.
---

## Pengenalan Pembicara
| Tugas | Deskripsi | Aplikasi |
|------|-------------|-------------|
| **Verifikasi pembicara** | “Apakah orang ini seperti yang mereka klaim?” | Perbankan telepon, buka kunci perangkat |
| **Identifikasi pembicara** | “Siapa yang berbicara?” | Transkripsi pertemuan, forensik |
| **Diarisasi pembicara** | "Siapa yang bicara kapan?" (dalam audio multi-speaker) | Ringkasan rapat, pembuatan subtitle |
| Model | Pendekatan |
|-------|----------|
| **ECAPA-TDNN** | Berbasis penyematan; canggih untuk verifikasi |
| **d-vektor** | Penyematan speaker sederhana dari DNN |
| **x-vektor** | Penyematan speaker yang ditingkatkan; banyak digunakan |
---

## Pengambilan Informasi Musik
| Tugas | Deskripsi | Alat/Model |
|------|-------------|-------------|
| **Transkripsi musik** | Konversi audio ke lembaran musik / MIDI | Nada Dasar Spotify, Spleeter |
| **Pemisahan sumber** | Isolasikan instrumen atau vokal individu | Demucs, Spleeter, Pemisahan Sumber Musik |
| **Klasifikasi genre** | Kategorikan musik berdasarkan genre | CNN pada spektogram |
| **Pelacakan ketukan** | Mendeteksi tempo dan mengalahkan posisi | Librosa, Ibu |
| **Pengenalan akord** | Identifikasi akord dalam musik | Chord-CNN, model CRF |
| **Generasi musik** | Buat musik baru | MusicGen, MuseNet, AIVA |
---

## Deteksi Suara Lingkungan
| Tugas | Deskripsi | Aplikasi |
|------|-------------|-------------|
| **Deteksi peristiwa suara** | Identifikasi suara di suatu lingkungan | Rumah pintar (kaca pecah, bayi menangis) |
| **Klasifikasi pemandangan akustik** | Klasifikasi lingkungan (kantor, taman, lalu lintas) | Perangkat sadar konteks |
| **Deteksi anomali** | Deteksi suara yang tidak biasa | Pemantauan industri (mesinæ•…éšœ) |
| Kumpulan data | Kedengarannya | Ukuran |
|---------|--------|------|
| **Set Audio** | 632 kelas suara | 2 juta+ klip YouTube |
| **ESC-50** | 50 kelas suara lingkungan | 2.000 klip |
| **UrbanSound8K** | Suara perkotaan | 8.732 klip |
---

## Alat dan Kerangka
| Alat | Tujuan |
|------|---------|
| **Librosa** | Pustaka Python untuk analisis audio (fitur, efek, visualisasi) |
| **Pydub** | Manipulasi audio sederhana (memotong, menggabungkan, mengekspor) |
| **FFmpeg** | Pemrosesan audio/video baris perintah (pisau Swiss Army) |
| **Torchaudio** | Pemrosesan audio PyTorch (transformasi, kumpulan data, model) |
| **Memeluk Wajah (transformator)** | Model ASR dan TTS terlatih |
| **Bisikan (OpenAI)** | Pengenalan ucapan (sumber terbuka) |
| **Coqui TTS** | Toolkit TTS sumber terbuka |
| **Demuc** | Pemisahan sumber musik |
| **Otak Pidato** | Perangkat ucapan lengkap (ASR, TTS, pengenalan speaker) |
---

## Tips Praktis
- **Selalu dengarkan data Anda.** Sebelum melatih apa pun, dengarkan sampel audio. Perhatikan laju sampel, tingkat kebisingan, dan karakteristik speaker.
- **Cocokkan kecepatan sampel.** Whisper mengharapkan 16 kHz. Jika audio Anda 44,1 kHz, lakukan sampel ulang — namun perlu diingat bahwa downsampling akan menghilangkan informasi.
- **Tambahkan data audio.** Tambahkan kebisingan latar belakang, variasikan kecepatan dan nada, simulasikan mikrofon yang berbeda. Hal ini secara signifikan meningkatkan ketahanan.
- **Gunakan model terlatih.** Whisper untuk ASR dan VITS/Bark untuk TTS adalah titik awal yang sangat baik. Menyempurnakan hampir selalu lebih baik daripada berlatih dari awal.
- **Menangani keheningan.** Deteksi Aktivitas Suara (VAD) menghilangkan keheningan sebelum pemrosesan, menghemat komputasi, dan meningkatkan akurasi. Silero VAD dan WebRTC VAD adalah pilihan populer.
- **Menormalkan volume.** Rekaman yang berbeda memiliki tingkat kenyaringan yang sangat berbeda. Normalisasikan ke tingkat yang konsisten sebelum diproses.
---

## Ringkasan
Pemrosesan ucapan dan audio telah direvolusi dengan pembelajaran mendalam. Sistem ASR modern seperti Whisper mendekati akurasi tingkat manusia dalam berbagai bahasa. Sistem TTS menghasilkan ucapan yang semakin sulit dibedakan dari rekaman suara manusia. Kloning suara berfungsi dari beberapa detik audio. Pembuatan musik, pemisahan sumber, dan deteksi suara lingkungan semuanya berkembang pesat. Bidang ini masih menghadapi tantangan – bahasa yang sumber dayanya terbatas, lingkungan yang bising, masalah etika seputar kloning suara – namun perkembangannya jelas: mesin menjadi sama baiknya dengan manusia dalam hal pendengaran, pemahaman, dan produksi suara.