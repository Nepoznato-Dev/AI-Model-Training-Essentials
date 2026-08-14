<!--
---
# Metadata
title: "Relativity"
description: "Special relativity, Lorentz transformations, time dilation, length contraction, mass-energy equivalence, four-vectors, and introduction to general relativity"
category: "Data Science and Analytics"
subcategory: "Mathematics"
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
    date: "2026-08-10"
    author: "Nepoznato-Dev"
    changes: "Initial deep-dive into relativity"

# Review
created: "2026-08-10"
last_modified: "2026-08-10"
review_date: "2027-02-10"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-10"

# Classification
tags: [relativity, special-relativity, general-relativity, lorentz-transformations, time-dilation, length-contraction, mass-energy, spacetime]
difficulty_level: "advanced"
prerequisites:
  - "mathematics.md"
  - "abstract_algebra.md"
  - "classical_mechanics.md"
estimated_reading_time: "22 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Relativitas
Teori relativitas Einstein merevolusi pemahaman kita tentang ruang, waktu, dan gravitasi. **Relativitas khusus** (1905) menunjukkan bahwa ruang dan waktu tidak terpisah tetapi terjalin menjadi satu kesatuan yang disebut ruangwaktu, dan kecepatan cahaya adalah sama untuk semua pengamat. **Relativitas umum** (1915) menata ulang gravitasi bukan sebagai gaya, melainkan sebagai kelengkungan ruangwaktu yang disebabkan oleh massa dan energi. Teori-teori ini mendasari navigasi GPS, akselerator partikel, dan pemahaman kita tentang lubang hitam dan evolusi alam semesta.
---

## Postulat Relativitas Khusus
Einstein membangun relativitas khusus berdasarkan dua postulat yang tampak sederhana:
| Postulat | Pernyataan |
|-----------|-----------|
| **Prinsip Relativitas** | Hukum fisika adalah sama di semua kerangka acuan inersia (tidak dipercepat) |
| **Keteguhan c** | Kecepatan cahaya dalam ruang hampa (c ≈ 3 × 10⁸ m/s) adalah sama untuk semua pengamat, apapun geraknya atau gerak sumber |
Gabungan kedua postulat ini membalikkan intuisi Newton selama berabad-abad tentang ruang dan waktu absolut.
---

## Transformasi Lorentz
**Transformasi Lorentz** menghubungkan koordinat antara dua kerangka inersia yang bergerak dengan kecepatan relatif v.
### Persamaan Transformasi
Untuk kerangka S' yang bergerak dengan kecepatan v sepanjang sumbu x relatif terhadap kerangka S:
| Kuantitas | Transformasi |
|----------|---------------|
| x' | γ(x − vt) |
| t' | γ(t − vx/c²) |
| kamu' | kamu |
| z' | z |
dimana γ (Faktor Lorentz) = 1/√(1 − v²/c²)
### Faktor Lorentz γ
| v/c | | Efek |
|-----|---|--------|
| 0 | 1.0 | Tidak ada efek relativistik (batas Newton) |
| 0,1 | 1,005 | koreksi 0,5% |
| 0,5 | 1.155 | koreksi 15,5% |
| 0,9 | 2.294 | Pelebaran waktu yang signifikan |
| 0,99 | 7.089 | Efek ekstrim |
| 0,999 | 22.37 | Rezim akselerator partikel |
| → 1 | → ∞ | Tidak mungkin untuk benda berukuran besar |
### Transformasi Terbalik
Untuk berpindah dari S' kembali ke S: ganti v dengan −v.
---

## Pelebaran Waktu
Jam bergerak berjalan lambat.
Δt = γΔt₀
dengan Δt₀ adalah **waktu yang tepat** (waktu diukur dalam kerangka istirahat jam).
**Contoh Pekerjaan:** Muon yang tercipta pada ketinggian 10 km bergerak dengan kecepatan 0,998c. Masa pakai bingkai istirahatnya adalah 2,2 μs.
- γ = 1/√(1 − 0,998²) ≈ 15,8
- Masa pakai melebar: Δt = 15,8 × 2,2 μs = 34,8 μs
- Jarak tempuh: d = 0,998c × 34,8 μs ≈ 10,4 km
- Tanpa pelebaran waktu: d = 0,998c × 2,2 μs ≈ 0,66 km (tidak akan pernah mencapai tanah)
- **Kenyataan:** Muon mencapai permukaan bumi — mengonfirmasi pelebaran waktu secara eksperimental.
### Paradoks Kembar
Salah satu kembaran bergerak dengan kecepatan tinggi dan kembali. Mereka lebih muda dari saudara kembar yang tinggal di rumah. Bukan paradoks yang sebenarnya - kembaran yang bergerak itu berakselerasi (mengubah kerangka inersia), mematahkan simetrinya.
---

## Kontraksi Panjang
Benda yang bergerak diperpendek sepanjang arah geraknya.
L = L₀/γ
dengan L₀ adalah **panjang yang tepat** (panjang diukur dalam kerangka diam objek).
| v/c | | Faktor kontraksi L/L₀ |
|-----|---|------------------------|
| 0,5 | 1.15 | 87% |
| 0,9 | 2.29 | 44% |
| 0,99 | 7.09 | 14% |
| 0,999 | 22.4 | 4,5% |
**Poin penting:** Kontraksi panjang bukanlah ilusi optik — ini adalah efek fisik nyata yang diukur oleh pengamat dalam gerakan relatif.
---

## Relativitas Simultanitas
Peristiwa yang serentak dalam satu frame TIDAK serentak di frame lain yang bergerak relatif terhadap frame pertama.
**Eksperimen pemikiran kereta Einstein:** Petir menyambar kedua ujung kereta yang bergerak. Seorang pengamat di platform melihatnya secara bersamaan. Seorang pengamat di kereta (bergerak menuju satu serangan) melihat serangan depan terlebih dahulu.
**Kesimpulan:** "Serentak" tidak mutlak — hal ini bergantung pada kerangka acuan pengamat.
---

## Penambahan Kecepatan
Kecepatan tidak sekadar menambah relativitas khusus.
### Penambahan Kecepatan Relativistik
Jika sebuah benda bergerak dengan kecepatan u' dalam kerangka S', dan S' bergerak dengan kecepatan v relatif terhadap S:
u = (u' + v) / (1 + u'v/c²)
| Skenario | Hasil |
|----------|--------|
| u' = c (ringan) | u = c (kecepatan cahaya invarian) |
| kamu', v ≪ c | u ≈ u' + v (direduksi menjadi penjumlahan Galilea) |
| u' = 0,9c, v = 0,9c | u = 0,9945c (tidak pernah melebihi c) |
---

## Kesetaraan Massa-Energi
E = mc²
| Konsep | Rumus | Arti |
|---------|---------|---------|
| Energi istirahat | E₀ = mc² | Energi suatu massa diam |
| Jumlah energi | E = mc² | Termasuk energi kinetik |
| Energi kinetik | KE = (γ − 1)mc² | Dikurangi menjadi ½mv² untuk v ≪ c |
| Momentum-energi | E² = (pc)² + (mc²)² | Hubungan energi-momentum relativistik |
| Partikel tak bermassa | E = buah | Foton mempunyai energi dan momentum tetapi tidak memiliki massa diam |
### Contoh Energi Nuklir
| Reaksi | Cacat Massal | Energi Dirilis |
|----------|-------------|-----------------|
| Fisi U-235 | 0,1% massa | ~200 MeV per fisi |
| Fusi D-T | 0,7% massa | 17,6 MeV per reaksi |
| Materi-antimateri | 100% massa | 2mc² (konversi lengkap) |
---

## Empat-Vektor dan Ruangwaktu
### Ruangwaktu Minkowski
Relativitas khusus menyatukan ruang dan waktu menjadi 4D **Ruangwaktu Minkowski** dengan koordinat (ct, x, y, z).
### Interval Ruangwaktu
ds² = −c²dt² + dx² + dy² + dz²
| Tipe Interval | Kondisi | Arti |
|--------------|-----------|---------|
| **Seperti waktu** | ds²< 0 | Events can be causally connected |
| **Lightlike (null)** | ds² = 0 | Connected by a light signal |
| **Spacelike** | ds² >0 | Peristiwa tidak dapat saling mempengaruhi |
Interval ruangwaktu adalah **invarian** — semua pengamat sepakat mengenai nilainya.
### Empat-Vektor
| Empat-Vektor | Komponen | Kuantitas Invarian |
|-------------|-----------|-------------------|
| Posisi | (ct, x, y, z) | Interval ruangwaktu |
| Kecepatan | (c, vₓ, vᵧ, v_z) | Waktu yang tepat |
| Momentum | (E/c, pₓ, pᵧ, p_z) | Massa diam: m²c² = E²/c² − p² |
| Memaksa | dP/dτ | Akselerasi yang tepat |
---

## Pengantar Relativitas Umum
### Prinsip Kesetaraan
| Versi | Pernyataan |
|---------|-----------|
| **Lemah** | Massa gravitasi = massa inersia (semua benda jatuh dengan kecepatan yang sama) |
| **Einstein** | Kerangka yang mengalami percepatan seragam secara lokal tidak dapat dibedakan dari medan gravitasi |
| **Kuat** | Semua hukum fisika (bukan hanya mekanika) secara lokal sama dalam kerangka jatuh bebas |
### Gravitasi sebagai Ruangwaktu yang Melengkung
Ide utama relativitas umum: ruangwaktu kurva massa dan energi, dan objek mengikuti jalur yang paling lurus (geodesik) melalui ruangwaktu yang melengkung.
**Persamaan medan Einstein:**
G_μν + Λg_μν = (8πG/c⁴) T_μν
| Simbol | Arti |
|--------|---------|
| G_μν | Tensor Einstein (mengkodekan kelengkungan ruangwaktu) |
| | Konstanta kosmologis (energi gelap) |
| g_μν | Tensor metrik (menjelaskan geometri ruangwaktu) |
| G | Konstanta gravitasi Newton |
| T_μν | Tensor energi-tekanan (kandungan materi dan energi) |
**Ringkasan John Wheeler:** "Ruangwaktu memberi tahu materi cara bergerak; materi memberi tahu ruangwaktu cara melengkung."
### Prediksi Relativitas Umum
| Prediksi | Deskripsi | Dikonfirmasi? |
|-----------|-------------|------------|
| Pelebaran waktu gravitasi | Jam berjalan lebih lambat di medan gravitasi yang lebih kuat | Ya (GPS memerlukan koreksi) |
| Lensa gravitasi | Cahaya membelok di sekitar benda besar | Ya (Eddington 1919, gambar Hubble) |
| Pergeseran merah gravitasi | Cahaya kehilangan energi saat keluar dari sumur gravitasi | Ya (Pound-Rebka 1959) |
| Lubang hitam | Wilayah di mana kelengkungan ruangwaktu menghalangi cahaya keluar | Ya (LIGO, EHT 2019) |
| Gelombang gravitasi | Riak di ruangwaktu dari percepatan massa | Ya (LIGO 2015) |
| Presesi perihelion Merkurius | Ekstra 43 detik busur per abad | Ya (menjelaskan anomali sejak 1859) |
| Menyeret bingkai | Massa yang berputar menyeret ruangwaktu disekitarnya | Ya (Pemeriksaan Gravitasi B 2011) |
### Metrik Schwarzschild
Solusi lubang hitam paling sederhana (tidak berputar, tidak bermuatan):
ds² = −(1 − 2GM/rc²)c²dt² + (1 − 2GM/rc²)⁻¹dr² + r²dΩ²
**Radius Schwarzschild:** r_s = 2GM/c²
| Objek | Massa | r_s |
|--------|------|-----|
| Bumi | 6 × 10²⁴kg | 9mm |
| Matahari | 2×10³⁰kg | 3 km |
| Sgr A* (Pusat Bima Sakti) | 4 × 10⁶ M☉ | 12 juta km |
---

## Relevansi dengan Pembelajaran Mesin dan Ilmu Data
| Konsep Relativitas | Aplikasi |
|-------------------|-------------|
| Transformasi Lorentz | Jaringan saraf ekuivalen Lorentz, model sadar simetri |
| Geometri ruangwaktu | Pembelajaran mendalam geometris, pembelajaran berjenis |
| Empat vektor | Notasi tensor digunakan dalam simulasi fisika relativistik |
| Pelebaran waktu gravitasi | Koreksi GPS (layanan berbasis lokasi, ML geospasial) |
| Lensa gravitasi | Analisis data astronomi, pemetaan materi gelap |
| Relativitas umum | Jaringan saraf berbasis fisika untuk deteksi gelombang gravitasi |
| Geometri Riemann | Penurunan gradien alami (geometri informasi), optimasi berjenis |
| Tensor metrik | Mendefinisikan jarak dalam ruang melengkung — dasar pembelajaran berjenis |
| Geodesi | Jalur terpendek pada manifold — digunakan dalam robotika, penyematan grafik |
| Kalkulus tensor | Landasan untuk memahami manifold data berdimensi tinggi |
---

## Ringkasan
| Konsep | Ide Inti | Persamaan Kunci |
|---------|-----------|-------------|
| Relativitas khusus | Ruang dan waktu bersatu; c adalah mutlak | Transformasi Lorentz |
| Pelebaran waktu | Jam bergerak berjalan lambat | Δt = γΔt₀ |
| Kontraksi panjang | Benda bergerak dipersingkat | L = L₀/γ |
| Energi massa | Massa dan energi setara | E = mc² |
| Empat vektor | Deskripsi ruangwaktu terpadu | Interval invarian ds² |
| Prinsip kesetaraan | Gravitasi = percepatan lokal | Landasan GR |
| Relativitas umum | Gravitasi adalah ruangwaktu yang melengkung | G_μν = (8πG/c⁴)T_μν |
| Geodesi | Benda mengikuti jalur paling lurus dalam ruangwaktu melengkung | Jalur terpendek pada manifold |
Relativitas mengubah pemahaman kita tentang aspek paling mendasar dari realitas — ruang, waktu, massa, energi, dan gravitasi. Alat matematikanya — tensor, manifold, geodesik, ruang metrik — telah bermigrasi jauh melampaui fisika ke dalam pembelajaran mesin, yang mendukung pembelajaran mendalam geometris, metode gradien alami, dan algoritma pembelajaran berjenis.