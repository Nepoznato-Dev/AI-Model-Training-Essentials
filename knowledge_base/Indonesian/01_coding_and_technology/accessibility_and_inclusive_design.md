---
# Metadata
title: "Accessibility and Inclusive Design"
description: "WCAG, inclusive UX, assistive technology, accessible coding"
category: "Coding and Technology"
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
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [accessibility, inclusive, design, coding-and-technology]
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
# Aksesibilitas dan Desain Inklusif
Aksesibilitas (sering disingkat a11y) adalah praktik membuat perangkat lunak dapat digunakan oleh semua orang — termasuk penyandang disabilitas penglihatan, pendengaran, motorik, kognitif, dan neurologis. Ini adalah persyaratan hukum di banyak yurisdiksi dan merupakan praktik teknik standar. Perangkat lunak yang dapat diakses adalah perangkat lunak yang lebih baik untuk semua orang, karena keputusan desain yang mendukung pengguna penyandang disabilitas — struktur yang jelas, navigasi keyboard, kontras yang memadai, teks yang dapat dibaca — meningkatkan pengalaman bagi semua pengguna.
---

## Siapa yang Diuntungkan dari Aksesibilitas?
| Tipe Disabilitas | Contoh | Teknologi Bantu |
|----------------|---------|---------------------|
| **Visual** | Kebutaan, low vision, buta warna | Pembaca layar (JAWS, NVDA, VoiceOver); kaca pembesar; mode kontras tinggi |
| **Pendengaran** | Tuli, gangguan pendengaran | Keterangan; transkrip; peringatan visual |
| **Motor** | Keterbatasan ketangkasan, kelumpuhan, tremor | Navigasi hanya keyboard; kontrol suara; berpindah perangkat; pelacakan mata |
| **Kognitif** | Disleksia, ADHD, autisme, gangguan memori | Bahasa yang jelas; navigasi yang konsisten; mengurangi gangguan |
| **Sementara** | Lengan patah, sinar matahari cerah, lingkungan bising | Akomodasi yang sama dengan cacat tetap |
| **Situasi** | Menggendong bayi, mengemudi, satu tangan ditempati | Antarmuka suara; target sentuh besar |
**Wawasan utama**: fitur aksesibilitas yang dirancang untuk pengguna penyandang disabilitas membantu semua orang. Pemotongan tepi jalan (jalan landai di trotoar) dirancang untuk pengguna kursi roda namun digunakan oleh orang tua yang membawa kereta bayi, pekerja pengiriman dengan kereta, dan wisatawan yang membawa barang bawaan.
---

## Aksesibilitas Web (WCAG)
Pedoman Aksesibilitas Konten Web (WCAG) adalah standar internasional untuk aksesibilitas web.
### Prinsip WCAG (POUR)
| Prinsip | Persyaratan |
|-----------|-------------|
| **Dapat Dipahami** | Informasi harus dapat disajikan dengan cara yang dapat dipahami oleh pengguna (alternatif teks, keterangan, tata letak yang dapat disesuaikan) |
| **Dapat dioperasikan** | Antarmuka harus dapat dinavigasi dan digunakan (keyboard dapat diakses, waktu yang cukup, tidak ada konten yang menyebabkan kejang) |
| **Dapat dimengerti** | Informasi dan pengoperasian harus dapat dipahami (dapat dibaca, diprediksi, bantuan masukan) |
| **Kuat** | Konten harus sesuai dengan teknologi bantu saat ini dan masa depan |
### Tingkat Kesesuaian WCAG
| Tingkat | Persyaratan | Sasaran Khas |
|-------|-------------|---------------|
| **SEBUAH** | tingkat minimal; 30 kriteria keberhasilan | Hukum minimum di beberapa yurisdiksi |
| **AA** | Mengatasi hambatan paling umum | Target standar untuk sebagian besar organisasi |
| **AAA** | tingkat tertinggi; tidak semua konten bisa mencapainya | Konten khusus; situs pendidikan |
### Kriteria Kunci Keberhasilan (Tingkat AA)
| Kriteria | Persyaratan | Cara Mencapai |
|-----------|-------------|---------------|
| **1.1.1 Konten non-teks** | Semua gambar memiliki alternatif teks |  Atribut `alt`; `aria-label`untuk ikon |
| **1.3.1 Info dan hubungan** | Struktur disampaikan secara terprogram | HTML semantik; judul; daftar; landmark |
| **1.4.3 Kontras (minimum)** | Teks memiliki rasio kontras minimal 4,5:1 | Uji dengan pemeriksa kontras; pilih palet warna yang dapat diakses |
| **1.4.4 Mengubah ukuran teks** | Teks dapat diubah ukurannya hingga 200% tanpa kehilangan | Gunakan satuan relatif (rem, em); desain responsif |
| **2.1.1 Papan Ketik** | Semua fungsi tersedia melalui keyboard | Tidak ada jebakan keyboard; indikator fokus terlihat |
| **2.4.3 Urutan fokus** | Urutan fokus menjaga makna dan pengoperasian | Urutan tab logis; Urutan DOM cocok dengan urutan visual |
| **2.4.7 Fokus terlihat** | Fokus keyboard ditunjukkan secara visual | gaya CSS `:focus-visible`; tidak pernah`outline: none`tanpa penggantian |
| **3.3.2 Label atau instruksi** | Masukan memiliki label |  elemen `<label>`; `aria-label`|
| **4.1.2 Nama, peran, nilai** | Komponen UI memiliki nama dan peran yang dapat diakses | atribut ARIA; HTML semantik |
---

## ARIA (Aplikasi Internet Kaya yang Dapat Diakses)
ARIA menambahkan informasi aksesibilitas ke elemen HTML yang tidak memiliki semantik bawaan.
### Peran ARIA
| Peran | Tujuan | Contoh |
|------|---------|---------|
| `button`| Mengidentifikasi elemen sebagai tombol |`<div>`ditata sebagai tombol |
| `dialog`| Dialog modal atau non-modal | Komponen modal khusus |
| `tablist`/`tab`/`tabpanel`| Antarmuka tab | Komponen tab khusus |
| `alert`| Pesan penting yang muncul secara dinamis | Pemberitahuan kesalahan |
| `progressbar`| Indikator kemajuan | Memuat status |
| `menu`/`menuitem`| Navigasi menu | Menu tarik-turun |
### Atribut ARIA
| Atribut | Tujuan | Contoh |
|-----------|---------|---------|
| `aria-label`| Nama yang dapat diakses ketika tidak ada teks yang terlihat | Tombol hanya ikon:`aria-label="Search"`|
| `aria-describedby`| Tautan elemen ke deskripsinya | Bidang formulir dengan teks bantuan |
| `aria-expanded`| Menunjukkan jika suatu bagian diperluas | Akordeon; tarik-turun |
| `aria-hidden`| Menyembunyikan elemen dari teknologi bantu | Ikon dekoratif |
| `aria-live`| Mengumumkan perubahan konten dinamis | Pembaruan langsung; pemberitahuan |
| `aria-disabled`| Menunjukkan elemen dinonaktifkan | Tombol berwarna abu-abu |
### Aturan Pertama ARIA
> **Jangan gunakan ARIA jika Anda dapat menggunakan HTML asli.**`<button>`sudah dapat diakses.`<div role="button">`mengharuskan Anda menambahkan penanganan keyboard, manajemen fokus, dan dukungan pembaca layar secara manual. Gunakan HTML semantik terlebih dahulu; ARIA hanya jika elemen asli tidak dapat melakukan tugasnya.
---

## Navigasi Papan Ketik
| Kunci | Perilaku yang Diharapkan |
|-----|-------------------|
| **Tab** | Pindahkan fokus ke elemen interaktif berikutnya |
| **Shift + Tab** | Pindahkan fokus ke elemen interaktif sebelumnya |
| **Masuk / Spasi** | Aktifkan elemen fokus (tombol, tautan) |
| **Tombol panah** | Menavigasi di dalam komponen (menu, tab, grup radio) |
| **Melarikan diri** | Tutup dialog, menu, atau popover |
| **Beranda / Akhir** | Lompat ke item pertama/terakhir dalam daftar |
### Jebakan Keyboard Umum
| Masalah | Perbaiki |
|---------|-----|
| Fokus masuk ke komponen tapi tidak bisa keluar | Pastikan Tab memindahkan fokus keluar; menangani Escape |
| Modal tidak menjebak fokus | Fokus harus berputar dalam modal; kembali ke pemicu pada penutupan |
| Komponen khusus tidak merespons keyboard | Tambahkan pengendali keydown untuk Enter, Spasi, panah |
---

## Warna dan Desain Visual
| Pedoman | Persyaratan |
|-----------|-------------|
| **Rasio kontras** | 4.5:1 untuk teks normal; 3:1 untuk teks besar (18pt+ atau 14pt+ tebal) |
| **Jangan hanya mengandalkan warna** | Gunakan ikon, teks, atau pola selain warna |
| **Indikator fokus** | Selalu terlihat; kontras tinggi; tidak pernah dilepas tanpa penggantian |
| **Mengubah ukuran teks** | Tata letak harus berfungsi pada zoom 200% |
| **Responsif** | Konten harus dialirkan ulang pada lebar 320 piksel (seluler) |
### Pertimbangan Buta Warna
| Ketik | Warna yang Terkena Dampak | Tip Desain |
|------|-----------------|------------|
| **Deuteranopia** | Merah-hijau (paling umum) | Jangan gunakan warna merah/hijau untuk menyampaikan status; gunakan ikon + warna |
| **Protanopia** | Merah-hijau | Sama seperti di atas |
| **Tritanopia** | Biru-kuning | Jangan gunakan warna biru/kuning sebagai satu-satunya pembeda |
---

## Menguji Aksesibilitas
| Metode | Alat | Apa yang Ditangkapnya |
|--------|------|----------------|
| **Pemindaian otomatis** | kapak, Mercusuar, GELOMBANG | Teks alternatif tidak ada; masalah kontras; Kesalahan ARIA |
| **Pengujian papan ketik** | Panduan: cabut mouse, gunakan keyboard saja | Urutan fokus; jebakan keyboard; penangan yang hilang |
| **Pengujian pembaca layar** | NVDA (gratis), VoiceOver (macOS), JAWS | Label tidak ada; struktur yang buruk; perubahan mendadak |
| **Pengujian zoom** | Perbesar peramban hingga 200%, 400% | Kerusakan tata letak; teks terpotong; masalah meluap |
| **Kontras warna** | Pemeriksa kontras WebAIM, plugin Stark | Rasio kontras tidak mencukupi |
| **Pengujian pengguna** | Uji dengan pengguna yang dinonaktifkan | Hambatan dunia nyata yang terlewatkan oleh alat otomatis |
---

## Persyaratan Hukum
| Hukum | Wilayah | Persyaratan |
|-----|--------|-------------|
| **ADA** (Undang-Undang Penyandang Disabilitas Amerika) | Amerika Serikat | Website akomodasi publik harus dapat diakses |
| **Pasal 508** | AS (federal) | TIK lembaga federal harus dapat diakses |
| **EAA** (Undang-Undang Aksesibilitas Eropa) | UE (2025+) | Produk dan layanan harus memenuhi persyaratan aksesibilitas |
| **EN 301 549** | UE | Standar teknis aksesibilitas TIK |
| **ACA** (Undang-Undang Aksesibilitas Kanada) | Kanada | Industri yang diatur oleh pemerintah dan diatur |
| **UU Kesetaraan 2010** | Inggris | Penyedia layanan harus melakukan penyesuaian yang wajar |
---

## Aksesibilitas Seluler
| Peron | Pedoman | Alat Utama |
|----------|-----------|-----------|
| **iOS** | Pedoman Antarmuka Manusia Apple (bagian Aksesibilitas) | Pengisi suara; Tipe Dinamis; Kontrol Pengalihan |
| **Android** | Pedoman Aksesibilitas Android | Komentar Balik; Beralih Akses; Pilih untuk Berbicara |
| Kepedulian Seluler | Solusi |
|---------------|----------|
| **Sentuh target** | Minimal 44×44 poin (iOS) / 48×48 dp (Android) |
| **Dukungan pembaca layar** | Deskripsi konten; label aksesibilitas |
| **Sensitivitas gerakan** | Hormati`prefers-reduced-motion`; hindari animasi yang diputar otomatis |
| **Ukuran teks dinamis** | Ukuran font sistem pendukung; gunakan unit teks yang dapat diskalakan |
---

## Ringkasan
Aksesibilitas adalah prinsip desain yang harus menginformasikan setiap keputusan sejak awal, bukan fitur yang ditambahkan di akhir. Gunakan HTML semantik. Pastikan navigasi keyboard berfungsi. Pertahankan kontras warna yang cukup. Memberikan alternatif teks untuk konten non-teks. Uji dengan pembaca layar dan pengguna yang dinonaktifkan. Hasilnya adalah perangkat lunak yang berfungsi lebih baik untuk semua orang — termasuk mereka yang mengalami gangguan sementara, keterbatasan situasional, perangkat lama, koneksi lambat, dan banyak perbedaan penggunaan di dunia nyata dengan lingkungan pengembangan terkendali.