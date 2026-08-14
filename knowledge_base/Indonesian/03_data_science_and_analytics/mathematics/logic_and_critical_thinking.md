<!--
---
# Metadata
title: "Logic and Critical Thinking"
description: "Formal logic, logical fallacies, argument analysis, and critical thinking frameworks"
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
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Split from mathematics_and_logic.md; expanded into standalone file"

# Review
created: "2026-08-09"
last_modified: "2026-08-09"
review_date: "2027-02-09"
reviewed_by: "Data Science Knowledge Base Team"
next_review: "2027-08-09"

# Classification
tags: [logic, critical-thinking, fallacies, arguments, reasoning, boolean-algebra]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Logika dan Berpikir Kritis
Logika adalah studi tentang penalaran yang valid — bagaimana membangun argumen yang masuk akal dan mengidentifikasi argumen yang cacat. Berpikir kritis adalah kebiasaan disiplin mempertanyakan asumsi, mengevaluasi bukti, dan berpikir secara hati-hati. Keterampilan ini penting tidak hanya dalam matematika dan ilmu komputer, tetapi juga dalam pengambilan keputusan sehari-hari, penelitian ilmiah, dan menavigasi dunia yang kaya informasi.
---

## Apa Itu Argumen?
Dalam logika, **argumen** adalah serangkaian pernyataan (premis) yang dimaksudkan untuk mendukung suatu kesimpulan.
| Komponen | Peran | Contoh |
|-----------|------|---------|
| **Premis** | Pernyataan yang ditawarkan sebagai bukti | "Semua manusia fana" |
| **Kesimpulan** | Klaim tempat dukungan | "Socrates itu fana" |
| **Inferensi** | Langkah logis dari premis ke kesimpulan | "Oleh karena itu, Socrates adalah manusia..." |
### Valid vs. Suara
| Istilah | Arti | Contoh |
|------|---------|---------|
| **Sah** | Jika premis benar, kesimpulan harus benar | Struktur benar, meskipun premisnya salah |
| **Tidak valid** | Kesimpulan tidak mengikuti premis | Struktur logis rusak |
| **Suara** | Valid DAN semua premis benar | Argumen standar emas |
| **Tidak sehat** | Entah tidak valid atau memiliki premis yang salah | Argumen paling cacat |
---

## Jenis Penalaran
| Ketik | Arah | Kekuatan | Contoh |
|------|-----------|----------|---------|
| **Deduktif** | Umum → spesifik | Tertentu (jika valid) | "Semua mamalia punya paru-paru. Paus tetap mamalia. Oleh karena itu, paus punya paru-paru." |
| **Induktif** | Spesifik → umum | Kemungkinan | "Setiap angsa yang saya lihat berwarna putih. Oleh karena itu, semua angsa mungkin berwarna putih." |
| **Menculik** | Observasi → penjelasan terbaik | Masuk akal | "Rumputnya basah. Penjelasan terbaiknya adalah hujan." |
---

## Logika Proposisional
Logika proposisional berkaitan dengan proposisi sederhana dan cara menggabungkannya:
### Konektivitas Logis
| Ikat | Simbol | Arti | Kondisi Kebenaran |
|-----------|--------|---------|----------------|
| **DAN** | ∧ (p ∧ q) | Konjungsi | Benar hanya jika keduanya benar |
| **ATAU** | ∨ (p ∨ q) | Disjungsi | Benar jika setidaknya satu benar |
| **TIDAK** | ¬ (¬p) | Negasi | Nilai kebenaran yang berlawanan |
| **JIKA...MAKA** | → (p → q) | Implikasi | Salah hanya jika p benar dan q salah |
| **JIKA** | ↔ (p ↔ q) | Bikondisional | Benar bila keduanya mempunyai nilai kebenaran yang sama |
### Tabel Kebenaran Implikasi (p → q)
| hal | q | hal → q |
|---|---|-------|
| T | T | T |
| T | F | F |
| F | T | T |
| F | F | T |
Catatan: Premis yang salah membuat implikasinya menjadi benar-benar hampa. “Jika bulan adalah keju, maka sayalah Pausnya” secara logika benar adanya.
---

## Aljabar Boolean
Aljabar Boolean adalah matematika nilai benar/salah dan merupakan dasar desain dan pemrograman sirkuit digital:
| Hukum | Ekspresi | Arti |
|-----|-----------|---------|
| **Komutatif** | A ∧ B = B ∧ A | Urutan tidak masalah |
| **Asosiatif** | (A ∧ B) ∧ C = A ∧ (B ∧ C) | Pengelompokan tidak masalah |
| **Distributif** | A ∧ (B ∨ C) = (A ∧ B) ∨ (A ∧ C) | DAN mendistribusikan ke OR |
| **De Morgan** | ¬(A ∧ B) = ¬A ∨ ¬B | Negasi membalik AND menjadi OR |
| **De Morgan** | ¬(A ∨ B) = ¬A ∧ ¬B | Negasi membalik OR menjadi AND |
| **Negasi Ganda** | ¬(¬A) = SEBUAH | Dua negasi batal |
| **Identitas** | SEBUAH ∧ T = SEBUAH; SEBUAH ∨ F = SEBUAH | Elemen identitas |
| **Pelengkap** | A ∧ ¬A = F; A ∨ ¬A = T | Kontradiksi dan tautologi |
---

## Kekeliruan Logika yang Umum
Mengenali kekeliruan sangat penting untuk berpikir kritis:
### Kekeliruan Formal (Kesalahan Struktural)
| Kekeliruan | Struktur | Contoh |
|---------|-----------|---------|
| **Menegaskan Konsekuensi** | Jika P maka Q.Q. Oleh karena itu P.| "Kalau hujan, tanahnya basah. Tanahnya basah. Makanya hujan." (Bisa jadi alat penyiram.) |
| **Menyangkal Anteseden** | Jika P maka Q. Bukan P. Oleh karena itu bukan Q. | "Kalau hujan, tanahnya basah. Tidak hujan. Jadi tanahnya tidak basah." |
### Kekeliruan Informal (Kesalahan Konten)
| Kekeliruan | Deskripsi | Contoh |
|---------|-------------|---------|
| **Ad Hominem** | Menyerang orangnya, bukan adu argumennya | “Anda tidak bisa mempercayai rencana ekonominya – dia bahkan bukan seorang ekonom.” |
| **Manusia Jerami** | Salah mengartikan argumen agar lebih mudah diserang | "Anda ingin mengurangi pengeluaran militer? Jadi Anda ingin meninggalkan negara ini tanpa pertahanan!" |
| **Banding ke Otoritas** | Mengutip otoritas yang bukan ahli di bidang terkait | "Selebriti ini bilang diet ini berhasil, jadi pasti efektif." |
| **Dilema Palsu** | Hanya menyajikan dua opsi ketika ada lebih banyak | "Anda bersama kami atau melawan kami." |
| **Lereng Licin** | Berpendapat bahwa satu peristiwa pasti akan membawa akibat yang ekstrim | "Jika kita membiarkan ini, hal berikutnya yang Anda tahu, akan terjadi kekacauan total." |
| **Penalaran Melingkar** | Kesimpulannya diasumsikan di premis | “Buku itu benar karena dikatakan benar.” |
| **Generalisasi Tergesa-gesa** | Menarik kesimpulan luas dari bukti yang tidak mencukupi | "Aku bertemu dengan dua orang kasar dari kota itu. Semua orang di sana pasti kasar." |
| **Post Hoc Ergo Propter Hoc** | Dengan asumsi sebab akibat dari urutan temporal | "Saya mengonsumsi suplemen ini dan merasa lebih baik, jadi pasti berhasil." |
| **Ikan Merah** | Memperkenalkan topik yang tidak relevan untuk mengalihkan perhatian | "Anda bertanya tentang kebijakan saya mengenai pendidikan, tapi yang paling penting adalah perekonomian." |
| **Ikut-ikutnya** | Sesuatu itu benar karena banyak orang mempercayainya | “Semua orang membeli produk ini, jadi ini pasti yang terbaik.” |
---

## Mengevaluasi Argumen: Daftar Periksa
| Langkah | Pertanyaan |
|------|----------|
| 1. **Identifikasi kesimpulannya** | Argumen apa yang ingin dibuktikan? |
| 2. **Identifikasi lokasinya** | Bukti apa yang ditawarkan? |
| 3. **Periksa validitas** | Apakah kesimpulannya mengikuti premis? |
| 4. **Periksa kesehatan** | Apakah premis tersebut benar adanya? |
| 5. **Cari kekeliruan** | Apakah ada kesalahan struktural atau konten? |
| 6. **Pertimbangkan argumen tandingan** | Keberatan apa yang mungkin timbul? |
| 7. **Menilai kualitas bukti** | Apakah buktinya dapat diandalkan, cukup, dan relevan? |
---

## Mengapa Ini Penting
Logika dan pemikiran kritis adalah dasar matematika, ilmu komputer, hukum, dan penyelidikan ilmiah. Di dunia yang penuh dengan misinformasi, periklanan, dan retorika persuasif, kemampuan mengevaluasi argumen dengan cermat bukan sekadar keterampilan akademis — melainkan keterampilan bertahan hidup. Baik Anda sedang men-debug kode, merancang algoritme, atau membuat keputusan hidup, penalaran yang jelas memisahkan penilaian yang baik dari penilaian yang buruk.