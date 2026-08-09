---
# Metadata
title: "Materials Science"
description: "Crystal structures, polymers, alloys, semiconductors, nanomaterials"
category: "Natural Sciences"
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
reviewed_by: "Natural Sciences Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [materials, science, natural-sciences]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
#Ilmu Material
Ilmu material adalah studi tentang bagaimana struktur suatu material (pada skala atom, mikroskopis, dan makroskopis) menentukan sifat-sifatnya, dan bagaimana metode pemrosesan dapat digunakan untuk mengontrol struktur tersebut guna mencapai kinerja yang diinginkan. Bidang inilah yang menjawab pertanyaan seperti: mengapa baja kuat namun berat? Mengapa kaca transparan tetapi rapuh? Bagaimana kita bisa membuat baterai terisi lebih cepat? Bahan apa yang bisa bertahan dalam kondisi di Mars? Setiap teknologi yang pernah Anda gunakan terbuat dari material, dan kemajuan teknologi hampir selalu membutuhkan kemajuan material.
---

## Tetrahedron Ilmu Material
Empat elemen yang saling berhubungan yang menentukan bidang:
| Elemen | Deskripsi |
|---------|-------------|
| **Struktur** | Bagaimana atom dan molekul tersusun (struktur kristal; batas butir; cacat) |
| **Properti** | Bagaimana material berperilaku (mekanik; listrik; termal; optik; magnet) |
| **Pemrosesan** | Bagaimana bahan dibuat dan dibentuk (casting; sintering; doping; annealing) |
| **Kinerja** | Bagaimana fungsi material dalam aplikasi nyata |
Wawasan utamanya: mengubah pemrosesan akan mengubah struktur, mengubah properti, dan mengubah kinerja.
---

## Kelas Materi
### Ringkasan
| Kelas | Ikatan | Properti Utama | Contoh |
|-------|---------|---------------|---------|
| **Logam** | Logam (elektron terdelokalisasi) | Kuat; elastis; konduktif; buram | Baja; aluminium; tembaga; titanium |
| **Keramik** | Ionik / kovalen | Keras; rapuh; tahan panas; isolasi | alumina; silikon karbida; kaca; porselen |
| **Polimer** | Kovalen (rantai) + van der Waals | Ringan; fleksibel; isolasi; titik leleh rendah | Polietilen; nilon; karet; epoksi |
| **Komposit** | Kombinasi dua kelas atau lebih | Properti yang disesuaikan; kekuatan-terhadap-berat yang tinggi | serat karbon; fiberglass; beton |
| **Semikonduktor** | Kovalen (dengan pengotor terkontrol) | Konduktivitas merdu; dasar elektronik | silikon; jerman; galium arsenida |
| **Biomaterial** | Bermacam-macam; diperlukan biokompatibel | Berinteraksi dengan sistem biologis | Implan titanium; kolagen; hidroksiapatit |
---

## Struktur Kristal
### Struktur Kristal Logam Umum
| Struktur | Atom per Satuan Sel | Fraksi Pengepakan | Contoh |
|-----------|-------------------|-----------------|---------|
| **FCC** (Kubik Berpusat pada Wajah) | 4 | 0,74 (kemasan terdekat) | Aluminium; tembaga; emas; nikel; austenit (γ-besi) |
| **BCC** (Kubik Berpusat pada Tubuh) | 2 | 0,68 | Besi (besi α); kromium; tungsten; molibdenum |
| **HCP** (Kemasan Dekat Heksagonal) | 6 | 0,74 (kemasan terdekat) | titanium; seng; magnesium; kobalt |
### Mengapa Struktur Kristal Penting
| Properti | Pengaruh Struktur Kristal |
|----------|----------------|
| **Kekuatan** | Sistem slip (bidang tempat atom meluncur) berbeda berdasarkan strukturnya; Logam FCC lebih ulet dibandingkan HCP |
| **Kepadatan** | Fraksi pengepakan menentukan seberapa rapat atom dikemas |
| **Transformasi fase** | Besi berubah dari BCC menjadi FCC pada 912°C — ini adalah dasar perlakuan panas baja |
| **Anisotropi** | Sifat dapat bervariasi menurut arah pada kristal non-kubik |
---

## Sifat Mekanik
### Metrik Utama
| Properti | Definisi | Satuan | Nilai Khas |
|----------|-----------|-------|----------------|
| **Modulus Young (E)** | Kekakuan; tegangan/regangan pada daerah elastis | IPK | Baja: 200; Aluminium: 70; Karet: 0,01–0,1 |
| **Kekuatan hasil** | Tegangan di mana deformasi permanen (plastis) dimulai | MPa | Baja: 250–1000; Aluminium: 40–500 |
| **Kekuatan tarik (UTS)** | Stres maksimal sebelum kegagalan | MPa | Baja: 400–2000; Aluminium: 90–600 |
| **Daktilitas (% perpanjangan)** | Berapa regangan suatu bahan sebelum putus | % | Baja: 10–50; Kaca: <1 |
| **Ketangguhan** | Energi yang diserap sebelum patah (luas di bawah kurva tegangan-regangan) | MJ/m³ | Baja: tinggi; keramik: rendah |
| **Kekerasan** | Ketahanan terhadap lekukan permukaan | Berbagai skala | Berlian: paling sulit; bedak: paling lembut |
### Penguatan Mekanisme
| Mekanisme | Cara Kerja | Contoh |
|-----------|-------------|---------|
| **Penghalusan biji-bijian** | Butir lebih kecil = batas butir lebih banyak = dislokasi lebih sulit bergerak | Hubungan Hall-Petch |
| **Penguatan solusi yang solid** | Atom asing mendistorsi kisi; menghambat gerak dislokasi | Menambahkan seng ke tembaga → kuningan |
| **Pengerasan presipitasi** | Partikel kecil menghalangi gerakan dislokasi | Paduan aluminium yang diperkeras usia |
| **Pengerasan kerja (strain hardening)** | Deformasi plastis meningkatkan kepadatan dislokasi; mereka kusut dan saling menghalangi | Baja canai dingin |
| **Penguatan komposit** | Serat kuat dalam matriks yang lebih lembut memikul beban | Polimer yang diperkuat serat karbon |
---

## Sifat Listrik dan Termal
### Konduktivitas Listrik
| Jenis Bahan | Konduktivitas (S/m) | Mekanisme |
|--------------|--------------------|-----------|
| **Konduktor** (tembaga, perak) | 10^7 – 10^8 | Elektron bebas dalam ikatan logam |
| **Semikonduktor** (silikon, GaAs) | 10^-6 – 10^4 | Merdu dengan doping; rekayasa celah pita |
| **Isolator** (kaca, karet) | 10^-12 – 10^-20 | Celah pita yang besar; elektron terikat |
| **Superkonduktor** | Tak terbatas (di bawah suhu kritis) | Nol hambatan listrik; Efek Meissner |
### Properti Termal
| Properti | Deskripsi | Penting Untuk |
|----------|-------------|---------------|
| **Konduktivitas termal** | Seberapa baik panas mengalir melalui material | Penyerap panas; isolasi |
| **Ekspansi termal** | Berapa besar pemuaian suatu bahan jika dipanaskan | Pencocokan material dalam komposit; jembatan; rel |
| **Kapasitas panas spesifik** | Energi yang dibutuhkan untuk menaikkan suhu sebesar 1°C | Penyimpanan energi panas |
| **Titik lebur** | Suhu di mana padat menjadi cair | Aplikasi suhu tinggi |
---

## Polimer
### Jenis Polimer
| Ketik | Struktur | Properti | Contoh |
|------|-----------|-----------|---------|
| **Termoplastik** | Rantai linier atau bercabang; gaya antarmolekul lemah | Meleleh saat dipanaskan; dapat didaur ulang | Polietilen; polistiren; nilon |
| **Termoset** | Jaringan yang saling terkait; ikatan kovalen antar rantai | Jangan meleleh; terurai pada suhu tinggi | Epoksi; karet vulkanisasi; Bakelit |
| **Elastomer** | Ikatan silang ringan; rantai melingkar | Regangkan dan kembalikan ke bentuk | karet alam; silikon; neoprena |
### Properti Polimer
| Properti | Deskripsi |
|----------|-------------|
| **Suhu transisi kaca (Tg)** | Di bawah Tg: keras dan rapuh. Di atas Tg : lembut dan lentur |
| **Kristalinitas** | Polimer semi-kristalin lebih kuat dan lebih buram; amorf transparan |
| **Berat molekul** | UM yang lebih tinggi = lebih kuat; lebih sulit untuk diproses |
| **Tingkat polimerisasi** | Jumlah unit monomer; mempengaruhi properti |
---

## Diagram Fase
### Diagram Fase Besi-Karbon (Sederhana)
| Fase | Kandungan Karbon | Struktur | Properti |
|-------|---------------|-----------|-----------|
| **Ferit (α)** | Hingga 0,022% | besi BCC | Lembut; elastis; magnetis |
| **Austenit (γ)** | Hingga 2,14% | besi FCC | Non-magnetik; dapat dibentuk |
| **Semenit (Fe₃C)** | 6,67% | Ortorombik | Keras; rapuh |
| **Pearlit** | 0,76% (eutektoid) | Lapisan ferit dan sementit bergantian | Kuat; tangguh |
| **Martensit** | Apa saja (dibentuk dengan pendinginan cepat) | BCT (tetragonal berpusat pada tubuh) | Sangat keras; rapuh |
---

## Bahan Modern dan Berkembang
| Bahan | Deskripsi | Aplikasi |
|----------|-------------|-------------|
| **Grafena** | Lapisan tunggal atom karbon; bahan terkuat yang diketahui; konduktor yang sangat baik | Elektronik; komposit; sensor |
| **Tabung nano karbon** | Silinder graphene yang digulung; rasio kekuatan-terhadap-berat yang ekstrim | Komposit; elektronik; penyimpanan energi |
| **Perovskit** | Struktur kristal ABX₃; celah pita merdu | sel surya; LED; detektor |
| **Kerangka logam-organik (MOF)** | Bahan kristal berpori; luas permukaan yang sangat besar | Penyimpanan gas; katalisis; pemberian obat |
| **Paduan memori bentuk** | Kembali ke bentuk semula bila dipanaskan | Stent; aktuator; struktur perbaikan diri |
| **Metamaterial** | Struktur mikro yang direkayasa memberikan sifat yang tidak ditemukan di alam | Indeks bias negatif; penyelubungan |
| **Paduan entropi tinggi** | Beberapa elemen utama; kombinasi properti yang tidak biasa | Lingkungan ekstrim; luar angkasa |
---

## Ringkasan
Ilmu material menghubungkan struktur atom suatu material dengan sifat makroskopisnya dan kinerjanya di dunia nyata. Logam kuat dan konduktif tetapi berat. Keramik keras dan tahan panas tetapi rapuh. Polimer ringan dan fleksibel tetapi dibatasi oleh suhu. Komposit menggabungkan yang terbaik dari kelas yang berbeda. Struktur kristal menentukan perilaku mekanik. Pemrosesan - perlakuan panas, paduan, pengerasan kerja - mengontrol struktur mikro dan juga sifat-sifatnya. Material modern seperti graphene, perovskit, dan MOF mendorong batasan dari apa yang mungkin terjadi. Bidang ini pada dasarnya bersifat interdisipliner: fisika menjelaskan ikatan, kimia menjelaskan reaksi, teknik menjelaskan kinerja, dan semuanya penting untuk setiap teknologi mulai dari ponsel pintar hingga pesawat ruang angkasa.