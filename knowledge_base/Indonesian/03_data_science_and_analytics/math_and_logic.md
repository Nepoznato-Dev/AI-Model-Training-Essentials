---
# Metadata
title: "Mathematics and Logic"
description: "Mathematics, logic, proofs"
category: "Data Science and Analytics"
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
reviewed_by: "Data Science & Analytics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [math, logic, data-science-and-analytics]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Matematika dan Logika
Matematika bukan hanya mata pelajaran yang Anda pelajari di sekolah — matematika adalah sistem operasi yang mendasari hampir semua bidang teknis. Fisika menggunakannya untuk menggambarkan alam semesta. Ilmu komputer menggunakannya untuk merancang algoritma. Pembelajaran mesin menggunakannya untuk mengoptimalkan bobot. Keuangan menggunakannya untuk menilai risiko. Anda tidak perlu menguasai setiap cabang, tetapi memahami lanskap — dan mengetahui di mana setiap cabang muncul — membuat segala sesuatunya berjalan lebih cepat.
---

## Sistem Angka
Sebelum hal lain, ada baiknya untuk memahami jenis angka yang Anda gunakan. Setiap lapisan memperluas lapisan sebelumnya untuk memecahkan masalah yang tidak dapat dipecahkan oleh lapisan lama.
| Jenis Nomor | Apa yang Termasuk | Mengapa Diciptakan | Contoh |
|---|---|---|---|
| Bilangan asli | 1, 2, 3, 4, ... | Menghitung sesuatu | 5 apel |
| Bilangan bulat | 0, 1, 2, 3, ... | Mewakili "tidak ada" | 0 derajat |
| Bilangan bulat | ..., −2, −1, 0, 1, 2, ... | Hutang, suhu di bawah nol | −15°C |
| Bilangan rasional | p/q dimana q ≠ 0 | Membagi sesuatu secara tidak merata | 1/3, 0,75 |
| Bilangan irasional | Tidak dapat dinyatakan sebagai pecahan | Diagonal, lingkaran, pertumbuhan | √2, π, e |
| Bilangan nyata | Semua rasional + irasional | Garis bilangan lengkap | 3.14159... |
| Bilangan imajiner | Kelipatan i = √(−1) | Menyelesaikan x² + 1 = 0 | 3i |
| Bilangan kompleks | a + bi (nyata + imajiner) | Teknik elektro, mekanika kuantum | 2 + 3i |
---

## Aritmatika dan Teori Bilangan
Dasar-dasarnya: penjumlahan, pengurangan, perkalian, pembagian, dan aturan-aturan yang mengatur urutannya.
**Urutan operasi** (PEMDAS/BODMAS): Tanda kurung → Eksponen → Perkalian/Pembagian (kiri ke kanan) → Penjumlahan/Pengurangan (kiri ke kanan).
**Bilangan prima** — bilangan bulat yang lebih besar dari 1 tanpa pembagi selain 1 dan bilangan itu sendiri — adalah atom dalam teori bilangan. Beberapa yang pertama: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29.
Mengapa bilangan prima penting di luar kelas matematika: enkripsi modern (RSA) bergantung pada fakta bahwa mengalikan dua bilangan prima besar itu mudah, tetapi memfaktorkan kembali hasilnya merupakan proses yang brutal secara komputasi.
**Operasi yang berguna:**
- Faktorisasi prima: 84 = 2² × 3 × 7
- Pembagi Persekutuan Terbesar (PBT) dari 24 dan 36: 12
- Kelipatan Persekutuan Terkecil (KPK) dari 4 dan 6:12
---

## Aljabar
Aljabar adalah tempat Anda berhenti bekerja dengan angka tertentu dan mulai bekerja dengan *hubungan*. Variabel seperti`x`tidak memiliki nilai tetap — variabel mewakili apa pun yang membuat persamaan tersebut benar.
**Rumus kuadrat** menyelesaikan ax² + bx + c = 0:
x = (−b ± √(b² − 4ac)) / 2a
**Jenis fungsi umum dan lokasi kemunculannya:**
| Fungsi | Rumus | Bentuk | Contoh Dunia Nyata |
|---|---|---|---|
| Linier | kamu = mx + b | Garis lurus | Biaya per unit dengan tarif tetap |
| Kuadrat | y = kapak² + bx + c | Parabola | Gerak proyektil, jarak pengereman |
| Eksponensial | kamu = a × b² | Pertumbuhan / pembusukan yang cepat | Bunga majemuk, pertumbuhan populasi, penyebaran virus |
| Logaritma | y = log_b(x) | Pertumbuhan lambat, kebalikan dari eksponensial | Skala desibel, skala pH, kompleksitas algoritma |
**Kosakata kunci:**
- **Domain**: semua input valid (misalnya, tidak dapat dibagi dengan nol, tidak dapat mengambil √ dari bilangan real negatif)
- **Rentang**: semua kemungkinan keluaran
- **Kemiringan** (m): laju perubahan — "untuk setiap 1 unit x, y berubah sebesar m"
- **Intercept**: ketika fungsi melintasi suatu sumbu
---

## Geometri
Geometri mempelajari bentuk, ukuran, dan hubungan spasial. Itu muncul di mana-mana: mesin game menggunakannya untuk rendering, robotika menggunakannya untuk perencanaan jalur, arsitektur menggunakannya untuk desain struktural.
**Rumus penting:**
| Bentuk | Properti | Rumus |
|---|---|---|
| Segitiga | Jumlah sudut | 180° |
| Segi Empat | Jumlah sudut | 360° |
| Lingkaran | Keliling | 2πr |
| Lingkaran | Daerah | πr² |
| Bola | Jilid | (4/3)πr³ |
| Segitiga siku-siku | Teorema Pythagoras | a² + b² = c² |
**π (pi)** ≈ 3,14159 — rasio keliling lingkaran terhadap diameternya. Ini muncul di tempat yang tidak Anda duga: probabilitas (distribusi normal), rekayasa (pemrosesan sinyal), bahkan persamaan prinsip ketidakpastian Heisenberg.
---

## Statistik dan Probabilitas
Statistik adalah cara Anda memahami data. Inilah perbedaan antara "Saya pikir ini berhasil" dan "Saya punya bukti bahwa ini berhasil."
**Ukuran tendensi sentral — apa yang "khas":**
| Ukur | Cara Menghitungnya | Kapan Menggunakannya |
|---|---|---|
| Berarti (rata-rata) | Jumlah ÷ hitung | Pilihan bawaan; sensitif terhadap outlier |
| median | Nilai tengah bila diurutkan | Data yang tidak tepat (misalnya, harga rumah, gaji) |
| Modus | Nilai paling sering | Data kategorikal (misalnya, warna terpopuler) |
**Ukuran penyebaran — seberapa "bervariasi" datanya:**
| Ukur | Ide Rumus | Apa yang Dikatakannya kepada Anda |
|---|---|---|
| Rentang | maks− menit | Penyebaran total, namun sensitif terhadap outlier |
| Varians | Deviasi kuadrat rata-rata dari mean | Dalam satuan kuadrat (sulit ditafsirkan secara langsung) |
| Deviasi standar | √varians | Unit yang sama dengan data — ukuran penyebaran |
**Dasar-dasar probabilitas:**
- Berkisar dari 0 (tidak mungkin) hingga 1 (pasti)
- Kejadian bebas: P(A dan B) = P(A) × P(B)
- Contoh: menggulirkan dua angka 6 berturut-turut = (1/6) × (1/6) = 1/36
**Distribusi probabilitas yang akan Anda temui di ML:**
| Distribusi | Apa yang Dimodelkan | Contoh |
|---|---|---|
| Bernoulli | Uji coba tunggal, dua hasil | Pelemparan satu koin |
| Binomial | Keberhasilan dalam n percobaan | Jawaban yang benar pada 10 soal MCQ |
| Normal (Gaussian) | Kurva lonceng, fenomena alam | Ketinggian, nilai ujian, kebisingan pengukuran |
| racun | Peristiwa dalam interval tetap | Email per jam, cacat per batch |
**Teorema Bayes** — memperbarui keyakinan dengan bukti:
P(A|B) = P(B|A) × P(A) / P(B)
Ini adalah tulang punggung filter spam, diagnostik medis, dan model ML Bayesian. Dikatakan: keyakinan Anda yang diperbarui = (seberapa cocok bukti tersebut dengan hipotesis Anda × keyakinan Anda sebelumnya) / seberapa besar kemungkinan bukti tersebut secara keseluruhan.
---

## Kalkulus
Studi kalkulus *perubahan* dan *akumulasi*. Jika aljabar menangani snapshot, kalkulus menangani gambar bergerak.
**Kalkulus diferensial** — laju perubahan. Turunan f'(x) menunjukkan seberapa cepat f berubah pada suatu titik.
| Fungsi f(x) | Turunan f'(x) | Intuisi |
|---|---|---|
| xⁿ | n·xⁿâ»¹ | Aturan kekuasaan |
| e² | e² | Satu-satunya fungsi yang sama dengan turunannya sendiri |
| dalam(x) | 1/x | Laju pertumbuhan melambat seiring bertambahnya x |
| dosa(x) | karena(x) | Laju perubahan osilasi |
Mengapa turunan penting dalam ML: penurunan gradien — algoritme yang melatih sebagian besar jaringan saraf — bekerja dengan menghitung turunan dari fungsi kerugian dan melangkah ke arah yang mengurangi kesalahan.
**kalkulus integral** — akumulasi. Integral mewakili area di bawah kurva. Jika turunan menjawab “seberapa cepat perubahannya?”, integral menjawab “berapa akumulasinya?”
**Teorema dasar kalkulus** menghubungkan keduanya: diferensiasi dan integrasi adalah operasi invers.
---

## Logika dan Penalaran
Logika adalah ilmu yang mempelajari penalaran yang *valid* — bukan apakah suatu kesimpulan *terasa* benar, tetapi apakah kesimpulan tersebut *mengikuti* premis.
**Penalaran deduktif** (kesimpulan terjamin jika premisnya benar):
- Semua manusia fana. Socrates adalah manusia. → Socrates adalah makhluk fana.
**Penalaran induktif** (kemungkinan kesimpulan, tidak dijamin):
- Setiap angsa yang kulihat berwarna putih. → Semua angsa mungkin berwarna putih. (Tapi angsa hitam itu ada.)
**Kekeliruan logika yang umum — kesalahan yang terlihat masuk akal padahal sebenarnya tidak:**
| Kekeliruan | Apa Itu | Contoh |
|---|---|---|
| Iklan hominem | Menyerang orangnya, bukan adu argumennya | “Anda tidak bisa mempercayai ide kebijakannya – dia masih muda.” |
| Manusia Jerami | Salah mengartikan argumen untuk menjatuhkannya | “Dia ingin memotong pengeluaran militer? Dia ingin membuat kita tidak berdaya!” |
| Dikotomi yang salah | Menyajikan dua opsi ketika ada lebih banyak | "Anda bersama kami atau melawan kami." |
| Penalaran melingkar | Menggunakan kesimpulan sebagai premis tersendiri | “Hukum ini tidak adil karena tidak adil.” |
| Banding ke otoritas | "Memang benar karena ada ahli yang mengatakan demikian" | "Saham ini akan naik — kata seorang investor terkenal." |
| Post hoc | Misalkan A menyebabkan B karena A lebih dulu | "Saya meminum suplemen ini, lalu flu saya hilang. Suplemen tersebut menyembuhkan saya." |
---

## Set
**Set** adalah kumpulan objek berbeda — dasar matematika modern.
| Operasi | Simbol | Arti | Contoh (A={1,2,3}, B={2,4}) |
|---|---|---|---|
| Persatuan | A ∪ B | Elemen di salah satu set | {1, 2, 3, 4} |
| Persimpangan | A ∩ B | Elemen di kedua set | {2} |
| Perbedaan | A \ B | Elemen di A tetapi tidak di B | {1, 3} |
| Kumpulan kosong | ∅ | Tidak mengandung apa pun | {} |
| Bagian | A ⊂ B | Semua elemen A ada di B | {1,2} ⊂ {1,2,3} |
Teori himpunan muncul dalam database (SQL JOIN pada dasarnya adalah operasi himpunan), probabilitas (peristiwa adalah himpunan hasil), dan pemrograman (himpunan, peta hash).
---

## Basis Biner dan Angka
Komputer berpikir dalam biner (basis 2): hanya 0 dan 1. Manusia berpikir dalam desimal (basis 10). Pemrogram sering menggunakan heksadesimal (basis 16) sebagai cara ringkas untuk merepresentasikan biner.
| Basis | Digit yang Digunakan | Contoh | Setara Desimal |
|---|---|---|---|
| Biner (basis 2) | 0, 1 | 1011 | 8 + 0 + 2 + 1 = 11 |
| Desimal (basis 10) | 0–9 | 11 | 11 |
| Heksadesimal (basis 16) | 0–9, SEBUAH–F | B | 11 |
| Heksadesimal | 0–9, SEBUAH–F | A3 | 160 + 3 = 163 |
**Mengapa penting:** setiap bagian data di komputer — teks, gambar, audio, video — pada akhirnya hanyalah biner. Satu byte (8 bit) dapat mewakili 256 nilai berbeda. Warna dalam CSS (#FF5733), alamat memori (0x7FFF), dan alamat IP semuanya menggunakan hex karena memampatkan string biner yang panjang menjadi sesuatu yang dapat dibaca.
---

## Aljabar Linier untuk ML dan Grafik
Aljabar linier — vektor, matriks, dan transformasi — adalah mesin matematika di balik pembelajaran mesin, grafik komputer, simulasi fisika, dan mesin pencari.
**Vektor** adalah daftar angka yang diurutkan. Di ML, setiap titik data adalah vektor fitur:
- [23, 1.8, 75] dapat mewakili usia seseorang, tinggi badan dalam meter, dan berat badan dalam kg.
**Matriks** adalah susunan angka 2D. Bobot jaringan saraf disimpan sebagai matriks. Kumpulan 100 gambar mungkin berbentuk matriks (100, 784) — 100 baris, masing-masing dengan nilai 784 piksel.
**Operasi utama:**
| Operasi | Apa Fungsinya | Dimana Itu Muncul |
|---|---|---|
| Produk titik | Mengukur kesamaan antara dua vektor | Sistem rekomendasi, kesamaan kosinus |
| Perkalian matriks | Menggabungkan transformasi linier | Setiap lapisan jaringan saraf |
| Nilai eigen/vektor eigen | Arah suatu matriks berskala (tidak berputar) | Pengurangan dimensi PCA, PageRank |
| Peringkat matriks | Jumlah informasi independen | Kompresi, perkiraan peringkat rendah |
**Kesamaan kosinus** = (a·b) / (||a|| × ||b||) — berkisar dari −1 (berlawanan) hingga 1 (arah yang sama). Beginilah cara mesin pencari mengukur apakah dua dokumen "tentang hal yang sama" dan bagaimana model penyematan membandingkan kesamaan semantik.
---

## Ringkasan
| Cabang | Pertanyaan Inti | Aplikasi Kunci |
|---|---|---|
| Teori Aritmatika & Bilangan | Bagaimana perilaku angka? | Kriptografi, hashing |
| Aljabar | Bagaimana hubungan yang tidak diketahui? | Pemodelan, persamaan |
| Geometri | Bagaimana cara kerja bentuk dan ruang? | Grafik, robotika, arsitektur |
| Statistik & Probabilitas | Apa isi datanya? | ML, pengujian A/B, analisis risiko |
| Kalkulus | Bagaimana keadaannya berubah? | Pelatihan jaringan saraf, fisika |
| Logika | Apakah alasan ini valid? | Pemrograman, pembuktian, analisis argumen |
| Himpunan Teori | Bagaimana hubungan koleksi? | Basis data, probabilitas |
| Aljabar Linier | Bagaimana cara kerja transformasi? | ML, grafik, mesin pencari |
Anda tidak memerlukan semua ini pada hari pertama. Namun seiring Anda mendalami bidang teknis apa pun, Anda akan terus kembali ke dasar-dasar ini. Kabar baiknya: setiap cabang menjadi lebih masuk akal setelah Anda melihat *mengapa* cabang tersebut ditemukan — masalah apa yang ingin dipecahkannya.