---
# Metadata
title: "Reinforcement Learning"
description: "MDPs, Q-learning, policy gradients, RLHF, multi-agent systems"
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
# Pembelajaran Penguatan
Pembelajaran penguatan (RL) adalah cara mesin belajar membuat serangkaian keputusan melalui coba-coba. Tidak seperti pembelajaran yang diawasi, di mana jawaban yang benar diberikan untuk setiap contoh, RL hanya memberikan sinyal hadiah kepada agen — dan agen harus mencari tahu tindakan mana yang memberikan hasil terbaik dari waktu ke waktu. Ini adalah pendekatan di balik AlphaGo, kontrol robot, AI permainan, dan — yang terpenting — RLHF, teknik yang digunakan untuk menyelaraskan model bahasa besar modern dengan preferensi manusia.
---

## Konsep Inti
RL membingkai pengambilan keputusan sebagai perulangan antara **agen** dan **lingkungan**.
| Komponen | Peran | Contoh |
|-----------|------|---------|
| **Agen** | Pengambil keputusan | Program catur, robot, model bahasa |
| **Lingkungan** | Dunia tempat agen berinteraksi | Papan catur, gudang, percakapan |
| **Negara** | Situasi saat ini | Posisi papan, pembacaan sensor robot, riwayat obrolan |
| **Aksi** | Apa yang bisa dilakukan agen | Pindahkan sepotong, belok kiri, buat token |
| **Hadiah** | Sinyal umpan balik (bilangan skalar) | +1 untuk menang, -1 untuk crash, skor preferensi manusia |
| **Kebijakan** | Pemetaan strategi menyatakan tindakan | "Jika raja diancam, pindahkan" |
| **Fungsi nilai** | Imbalan kumulatif yang diharapkan dari suatu negara bagian | "Posisi dewan ini bernilai sekitar +3 poin" |
### Lingkaran RL
```
Agent observes State → chooses Action → Environment returns new State + Reward
        ↑                                                                         |
        └─────────────────────────────────────────────────────────────────────────┘
```

Sasaran agen adalah memaksimalkan **hadiah kumulatif** dari waktu ke waktu, bukan hanya hadiah langsung. Inilah yang membuat RL secara fundamental berbeda dari pembelajaran yang diawasi.
---

## Perbedaan Utama dengan Paradigma Pembelajaran Lainnya
| Aspek | Pembelajaran yang Diawasi | Pembelajaran Tanpa Pengawasan | Pembelajaran Penguatan |
|--------|-------------------|---------------------|----------------------|
| **Sinyal** | Label yang benar untuk setiap contoh | Tidak ada label; temukan struktur | Imbalan skalar, sering tertunda |
| **Umpan Balik** | Segera | Tidak ada | Tertunda dan jarang |
| **Urutan** | Setiap contoh bersifat independen | Setiap contoh bersifat independen | Tindakan mempengaruhi keadaan di masa depan |
| **Tujuan** | Minimalkan kesalahan prediksi | Temukan pola | Maksimalkan imbalan kumulatif |
---

## Proses Keputusan Markov (MDP)
MDP adalah kerangka matematika untuk RL. Mereka berasumsi masa depan hanya bergantung pada keadaan saat ini, bukan sejarah bagaimana Anda sampai di sana (**properti Markov**).
| Komponen | Notasi | Arti |
|-----------|----------|---------|
| **Negara Bagian** | S | Semua kemungkinan situasi yang mungkin dialami agen |
| **Tindakan** | SEBUAH | Semua hal yang bisa dilakukan agen |
| **Fungsi transisi** | P(s' \| s, a) | Peluang mencapai keadaan s' setelah melakukan tindakan a dalam keadaan s |
| **Fungsi hadiah** | R(s, a, s') | Hadiah diterima untuk transisi |
| **Faktor diskon** | γ (gamma) | Seberapa besar nilai imbalan di masa depan vs imbalan langsung (0 hingga 1) |
**pengembalian** (total hadiah diskon) adalah:
```
G = R₁ + γR₂ + γ²R₃ + ...
```

Faktor diskon yang tinggi (γ mendekati 1) berarti agen tersebut berpandangan jauh ke depan. Yang rendah berarti picik.
---

## Algoritma RL Klasik
### Metode Berbasis Nilai
Ini mempelajari seberapa bagus setiap negara bagian (atau pasangan tindakan negara bagian).
| Algoritma | Ide Kunci | Batasan |
|-----------|----------|------------|
| **Pembelajaran Q** | Pelajari tabel nilai-Q: Q(status, tindakan) = imbalan yang diharapkan | Tidak berskala pada ruang negara yang besar |
| **Jaringan Q Dalam (DQN)** | Gunakan jaringan saraf untuk memperkirakan nilai Q | Hanya menangani tindakan terpisah; bisa tidak stabil |
| **DQN Ganda** | Perbaiki bias perkiraan berlebihan Q-learning | Masih sebatas tindakan diskrit |
Aturan pembaruan Q-learning:
```
Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]
```

### Metode Berbasis Kebijakan
Mereka secara langsung mempelajari kebijakan (strategi) tanpa memperkirakan nilai.
| Algoritma | Ide Kunci | Keuntungan |
|-----------|----------|-----------|
| **PERKUAT** | Gradien kebijakan Monte Carlo; perbarui kebijakan ke arah hasil yang baik | Sederhana; bekerja dengan tindakan berkelanjutan |
| **PPO** (Optimasi Kebijakan Proksimal) | Klip pembaruan kebijakan untuk mencegah perubahan besar dan mengganggu stabilitas | Stabil; banyak digunakan; standar bagus |
| **TRPO** | Metode wilayah kepercayaan untuk pembaruan kebijakan | Lebih berprinsip dibandingkan PPO; lebih sulit untuk diterapkan |
### Metode Aktor-Kritikus
Gabungkan yang terbaik dari keduanya: **aktor** (kebijakan) dan **kritikus** (fungsi nilai).
| Algoritma | Ide Kunci |
|-----------|----------|
| **A2C / A3C** | Keuntungan Aktor-Kritikus; menggunakan estimasi keuntungan untuk mengurangi varians |
| **SAC** (Aktor-Kritikus Lembut) | Maksimalkan imbalan sambil mempertahankan eksplorasi (regularisasi entropi) |
| **TD3** (DDPG Kembar Tertunda) | Atasi perkiraan berlebihan dalam ruang tindakan berkelanjutan |
---

## RLHF: Pembelajaran Penguatan dari Masukan Manusia
RLHF adalah teknik yang memungkinkan ChatGPT. Ini menjembatani kesenjangan antara model yang dapat memprediksi teks dan model yang menghasilkan keluaran yang benar-benar berguna bagi manusia.
### Tiga Langkah
| Langkah | Apa yang Terjadi | Keluaran |
|------|-------------|--------|
| **1. Penyempurnaan yang Diawasi (SFT)** | Menyempurnakan model terlatih berdasarkan contoh tulisan manusia berkualitas tinggi | Sebuah model yang mengikuti instruksi dengan cukup baik |
| **2. Pelatihan Model Hadiah** | Manusia membandingkan pasangan keluaran model; melatih model untuk memprediksi preferensi manusia | Model penghargaan yang menilai kualitas keluaran |
| **3. Optimasi RL** | Gunakan PPO untuk menyempurnakan model SFT guna memaksimalkan skor model penghargaan | Sebuah model yang selaras dengan preferensi manusia |
### Mengapa RLHF Penting
Tanpa RLHF, model bahasa ibarat siswa yang telah membaca semua buku tetapi tidak tahu bagaimana harus bersikap dalam percakapan. Ini dapat menghasilkan teks, tetapi teks tersebut mungkin tidak membantu, beracun, atau tidak tepat sasaran. RLHF mengajarkan model *apa yang diinginkan manusia* — bukan hanya seperti apa teksnya.
### Varian dan Alternatif
| Metode | Deskripsi | Keuntungan |
|--------|-------------|-----------|
| **DPO** (Optimasi Preferensi Langsung) | Lewati model hadiah; langsung mengoptimalkan kebijakan dari preferensi manusia | Lebih sederhana; tidak ada model penghargaan terpisah untuk dilatih |
| **RLAIF** | Gunakan AI (bukan manusia) untuk menghasilkan label preferensi | Lebih murah dari pelabelan manusia |
| **AI Konstitusional** | Gunakan serangkaian prinsip untuk memandu perilaku model tanpa label manusia | Lebih terukur; Pendekatan Antropik |
| **GRPO** (Optimasi Kebijakan Relatif Kelompok) | Bandingkan keluaran dalam suatu kelompok dibandingkan dengan model terpisah | Digunakan di DeepSeek-R1; mengurangi kebutuhan akan jaringan nilai |
---

## Eksplorasi vs Eksploitasi
Inilah ketegangan utama di RL. **Eksploitasi** berarti memilih tindakan yang Anda tahu berhasil dengan baik. **Eksplorasi** berarti mencoba hal baru untuk menemukan strategi yang berpotensi lebih baik.
| Strategi | Cara Kerja | Pertukaran |
|----------|-------------|-----------|
| **ε-serakah** | Pilih tindakan terbaik sepanjang waktu; tindakan acak dengan probabilitas ε | Sederhana namun tidak efisien |
| **Eksplorasi Boltzmann** | Pilih tindakan secara probabilistik berdasarkan nilai perkiraannya | Lebih halus dari ε-serakah |
| **UCB** (Batas Keyakinan Atas) | Lebih menyukai tindakan dengan ketidakpastian yang tinggi (optimisme dalam menghadapi ketidakpastian) | Jaminan teoretis yang bagus |
| **Regulerisasi entropi** | Tambahkan bonus untuk mengunjungi berbagai negara bagian (digunakan di SAC, PPO) | Mendorong eksplorasi alam |
---

## Pembelajaran Penguatan Multi-Agen
Ketika banyak agen belajar secara bersamaan, dinamikanya menjadi jauh lebih kompleks.
| Skenario | Tantangan | Contoh |
|----------|-----------|---------|
| **Koperasi** | Agen harus berkoordinasi; penugasan kredit itu sulit | Tim sepak bola robot; jaringan sensor terdistribusi |
| **Kompetitif** | Lawan beradaptasi; lingkungan tidak stasioner | Permainan AI (poker, StarCraft); keamanan siber |
| **Campuran** | Beberapa agen bekerja sama, yang lain bersaing | Pasar lelang; sistem lalu lintas |
| Algoritma | Deskripsi |
|-----------|-------------|
| **MADDPG** | DDPG versi multi-agen; kritikus terpusat, aktor terdesentralisasi |
| **MAPPO** | PPO multi-agen; banyak digunakan dalam praktek |
| **Main Sendiri** | Agen berlatih melawan salinan dirinya sendiri (AlphaGo, AlphaStar) |
---

## Transfer Sim-ke-Nyata
Melatih robot di dunia nyata itu lambat dan berbahaya. Sebaliknya, agen berlatih dalam simulasi dan transfer ke dunia nyata.
| Tantangan | Solusi |
|-----------|----------|
| **Kesenjangan realitas** (simulasi ≠ dunia nyata) | Pengacakan domain: memvariasikan parameter fisika selama pelatihan |
| **Contoh inefisiensi** | Gunakan RL berbasis model atau latih simulasi paralel besar |
| **Keamanan** | RL yang Dibatasi: menghukum tindakan tidak aman selama pelatihan |
| **Kemampuan observasi parsial** | Berlatih dengan sensor berisik dan observasi tertunda |
Perusahaan seperti Boston Dynamics dan Tesla menggunakan simulasi secara ekstensif, namun kesenjangan antara simulasi dan kinerja fisik tetap menjadi salah satu tantangan terbesar di bidang ini.
---

## Alat dan Kerangka
| Alat | Tujuan | Terbaik Untuk |
|------|---------|----------|
| **Garis Dasar Stabil3** | Bersihkan implementasi Python dari PPO, SAC, TD3, DQN | Pembelajaran dan pembuatan prototipe |
| **RLlib** | Pustaka RL yang dapat diskalakan dibangun di atas Ray | Pelatihan terdistribusi skala besar |
| **BersihkanRL** | Implementasi file tunggal untuk penelitian | Memahami algoritma secara mendalam |
| **Gimnasium (OpenAI)** | Antarmuka lingkungan standar | Mendefinisikan masalah RL |
| **Isaac Gym/Lab Isaac** | Simulasi fisika yang dipercepat GPU | Robotika, sim-to-real |
| **TRL** (Perpustakaan RL Transformator) | RLHF, DPO, PPO untuk model bahasa | Menyelaraskan LLM |
| **BukaRLHF** | Kerangka kerja RLHF terdistribusi | Melatih model besar dengan RLHF |
---

## Tips Praktis
- **Mulai dengan PPO.** Ini adalah algoritme tujuan umum yang paling andal. Jika Anda tidak yakin apa yang harus digunakan, PPO adalah defaultnya.
- **Normalisasikan imbalan Anda.** Penskalaan imbalan sangat memengaruhi stabilitas pelatihan.
- **Gunakan lingkungan yang divektorkan.** Menjalankan banyak lingkungan secara paralel (misalnya, 8–64) akan menstabilkan estimasi gradien dan mempercepat pelatihan secara signifikan.
- **Pantau reward dan entropi.** Jika entropi turun ke nol, agen Anda telah berhenti menjelajah dan mungkin terjebak dalam optimal lokal.
- **Pembentukan hadiah adalah sebuah seni.** Merancang fungsi hadiah yang tepat sering kali merupakan bagian tersulit. Imbalan yang sedikit (hanya di akhir) membuat pembelajaran menjadi sangat lambat. Imbalan yang padat dan berbentuk baik memandu agen tetapi dapat menimbulkan perilaku yang tidak diinginkan.
- **RLHF bersifat rapuh.** Perubahan kecil pada model reward atau hyperparameter PPO dapat menyebabkan penurunan kualitas yang besar. DPO adalah alternatif yang lebih stabil jika Anda tidak memerlukan pipeline RLHF lengkap.
---

## Ringkasan
Pembelajaran penguatan adalah studi tentang bagaimana agen belajar membuat keputusan melalui interaksi. Mulai dari algoritma klasik seperti Q-learning hingga metode deep RL modern seperti PPO dan SAC, dan hal ini mendasari beberapa kemajuan terbaru yang paling penting dalam AI — mulai dari permainan hingga penyelarasan model bahasa. Tantangan intinya tetap sama: bagaimana Anda mempelajari perilaku optimal ketika umpan balik tertunda, jarang, dan berisik? Jawabannya – coba-coba, dipandu oleh matematika yang cerdas – ternyata menjadi salah satu ide paling kuat dalam semua kecerdasan buatan.