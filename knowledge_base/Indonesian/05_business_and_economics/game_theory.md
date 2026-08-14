---
# Metadata
title: "Game Theory and Strategic Thinking"
description: "Nash equilibrium, prisoner's dilemma, mechanism design, auctions"
category: "Business and Economics"
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
reviewed_by: "Business & Economics Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [game, theory, business-and-economics]
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
# Teori Permainan dan Pemikiran Strategis
Teori permainan adalah studi matematis tentang interaksi strategis — situasi di mana hasil Anda tidak hanya bergantung pada apa yang Anda lakukan, namun juga pada apa yang dilakukan orang lain. Hal ini berlaku di mana saja: persaingan bisnis, hubungan internasional, lelang, negosiasi, biologi evolusi, dan keputusan sehari-hari seperti memilih rute melalui lalu lintas. Pemahaman intinya adalah bahwa para pelaku rasional dalam situasi strategis tidak hanya mengoptimalkan strategi mereka sendiri — mereka juga mengantisipasi apa yang akan dilakukan pihak lain, dan pihak lain juga melakukan hal yang sama.
---

## Konsep Dasar
### Terminologi Utama
| Istilah | Definisi |
|------|-----------|
| **Permainan** | Setiap situasi dengan dua atau lebih pengambil keputusan (pemain) yang pilihannya mempengaruhi hasil masing-masing |
| **Pemain** | Pengambil keputusan dalam permainan |
| **Strategi** | Rencana tindakan lengkap untuk setiap situasi yang mungkin timbul |
| **Hasilnya** | Hasil yang diterima pemain dari kombinasi strategi tertentu |
| **Ekuilibrium Nash** | Seperangkat strategi di mana tidak ada pemain yang dapat meningkatkan keuntungannya dengan mengubah strateginya secara sepihak |
| **Strategi dominan** | Strategi yang terbaik terlepas dari apa yang dilakukan pemain lain |
| **Permainan zero-sum** | Keuntungan satu pemain sama dengan kerugian pemain lainnya |
| **Permainan bukan jumlah nol** | Pemain berpotensi untung semua atau kalah semua |
| **Permainan kooperatif** | Pemain dapat membentuk perjanjian yang mengikat |
| **Permainan non-kooperatif** | Tidak ada perjanjian yang mengikat; setiap pemain bertindak demi kepentingan pribadi |
---

## Game Klasik
### Dilema Tahanan
Dua tersangka ditangkap. Masing-masing bisa bekerja sama (diam) atau membelot (mengaku).
| | B Bekerjasama | B Cacat |
|---|-------------|-----------|
| **A Bekerja Sama** | A : 1 tahun, B : 1 tahun | A : 10 tahun, B : gratis |
| **A Cacat** | A : gratis, B : 10 tahun | A : 5 tahun, B : 5 tahun |
| Wawasan | Deskripsi |
|---------|-------------|
| **Strategi dominan** | Cacat dominan bagi kedua pemain |
| **Ekuilibrium Nash** | Keduanya cacat (masing-masing 5 tahun) |
| **Pareto optimal** | Keduanya bekerja sama (masing-masing 1 tahun) |
| **Pelajaran** | Keputusan individu yang rasional dapat menyebabkan hasil yang lebih buruk secara kolektif |
### Game Klasik Lainnya
| Permainan | Deskripsi | Ekuilibrium Nash | Pelajaran |
|------|-------------|-----------------|--------|
| **Ayam (Elang-Merpati)** | Dua pengemudi saling berhadapan; berbelok atau lurus | Yang satu berbelok, yang satu lurus | Nyerempet bahaya; kredibilitas komitmen |
| **Perburuan Rusa** | Berburu rusa jantan bersama-sama (hasilnya tinggi) atau berburu kelinci sendirian (hasilnya rendah) | Baik rusa jantan atau keduanya kelinci | Koordinasi; kepercayaan |
| **Pertempuran Jenis Kelamin** | Dua pemain lebih memilih hasil yang berbeda tetapi ingin berkoordinasi | Keduanya pergi ke acara yang sama | Keseimbangan ganda; siapa yang bergerak lebih dulu mempunyai keuntungan |
| **Permainan terakhir** | Pengusul membagi uang; responden menerima atau menolak (keduanya tidak mendapat apa-apa) | Pengusul menawarkan minimum; responden menerima | Orang menolak tawaran yang tidak adil (tidak rasional tapi umum) |
| **Permainan barang umum** | Berkontribusi pada kolam bersama atau tumpangan gratis | Semua orang menumpang gratis | Tragedi milik bersama; perlunya penegakan |
---

## Jenis Permainan
### Berdasarkan Waktu
| Ketik | Deskripsi | Contoh |
|------|-------------|---------|
| **Serentak** | Pemain bergerak secara bersamaan (atau tanpa mengetahui gerakan orang lain) | Gunting batu-kertas; lelang penawaran tertutup |
| **Berurutan** | Pemain bergerak satu demi satu; pemain kemudian mengamati gerakan sebelumnya | Catur; keputusan masuk pasar |
| **Berulang** | Permainan yang sama dimainkan beberapa kali | Dilema tahanan yang berulang; persaingan bisnis yang sedang berlangsung |
### Berdasarkan Informasi
| Ketik | Deskripsi | Contoh |
|------|-------------|---------|
| **Informasi sempurna** | Semua pemain mengetahui semua gerakan sebelumnya | Catur; catur |
| **Informasi tidak sempurna** | Beberapa gerakan disembunyikan | Poker; persaingan bisnis |
| **Informasi lengkap** | Semua pemain mengetahui semua hasil dan strategi | Kebanyakan permainan buku teks |
| **Informasi tidak lengkap** | Beberapa imbalan atau jenis tidak diketahui | Lelang; negosiasi |
---

## Konsep Solusi
### Ekuilibrium Nash
| Aspek | Deskripsi |
|--------|-------------|
| **Definisi** | Tidak ada pemain yang dapat meningkatkan hasil mereka hanya dengan mengubah strategi |
| **Cara menemukan** | Untuk setiap pemain, temukan respons terbaik terhadap strategi pemain lain; dimana semuanya berpotongan adalah keseimbangan Nash |
| **Keberadaan** | Setiap permainan terbatas memiliki setidaknya satu ekuilibrium Nash (mungkin dalam strategi campuran) |
| **Keunikan** | Permainan dapat memiliki banyak keseimbangan Nash; timbul masalah koordinasi |
| **Batasan** | Ekuilibrium Nash tidak memberi tahu Anda ekuilibrium mana yang akan dipilih; tidak memperhitungkan keadilan |
### Ekuilibrium Strategi Dominan
| Langkah | Deskripsi |
|------|-------------|
| **1. Identifikasi strategi** | Daftar semua strategi yang tersedia untuk setiap pemain |
| **2. Temukan strategi dominan** | Sebuah strategi yang terbaik terlepas dari apa yang dilakukan orang lain |
| **3. Jika semua pemain memiliki satu** | Kombinasi tersebut merupakan keseimbangan strategi yang dominan |
| **4. Jika tidak** | Gunakan eliminasi berulang dari strategi yang didominasi atau keseimbangan Nash |
### Induksi Mundur (Permainan Berurutan)
| Langkah | Deskripsi |
|------|-------------|
| **1. Gambar pohon permainan** | Node = poin keputusan; cabang = tindakan |
| **2. Mulai dari akhir** | Identifikasi pilihan optimal pemain terakhir di setiap node terminal |
| **3. Bekerja mundur** | Pada setiap node sebelumnya, pilih tindakan yang memberikan hasil terbaik |
| **4. Hasil** | Keseimbangan sempurna subgame — strategi optimal di setiap titik keputusan |
---

## Konsep Lanjutan
### Strategi Campuran
| Konsep | Deskripsi | Contoh |
|---------|-------------|---------|
| **Strategi campuran** | Mengacak tindakan berdasarkan probabilitas | Gunting batu-kertas: mainkan masing-masing dengan probabilitas 1/3 |
| **Mengapa mengacak?** | Mencegah lawan memprediksi gerakan Anda | Tendangan penalti dalam sepak bola; pemeriksaan pajak |
| **Strategi campuran Ekuilibrium Nash** | Setiap pemain acuh tak acuh antara strategi murni mereka | Tidak ada pemain yang dapat mengeksploitasi yang lain |
### Permainan Berulang dan Teorema Rakyat
| Konsep | Deskripsi |
|---------|-------------|
| **Terakhir diulang** | Induksi ke belakang mengacaukan kerja sama; sama seperti permainan satu tembakan | Pembelotan putaran terakhir menyebar ke belakang |
| **Diulang tanpa batas** | Kerjasama dapat dipertahankan melalui ancaman hukuman di masa depan | Gayung bersambut; strategi pemicu suram |
| **Teorema Rakyat** | Setiap imbalan yang rasional secara individual dapat menjadi keseimbangan Nash dalam permainan yang berulang tanpa batas | Kerjasama dimungkinkan jika masa depan cukup penting |
| **Faktor diskon** | Seberapa besar pemain menghargai imbalan di masa depan; lebih tinggi = lebih banyak kerjasama | Pemain yang sabar lebih banyak bekerja sama |
### Desain Mekanisme (Teori Permainan Terbalik)
| Konsep | Deskripsi |
|---------|-------------|
| **Tujuan** | Merancang aturan permainan untuk mencapai hasil yang diinginkan |
| **Aplikasi** | Lelang; sistem pemungutan suara; desain kontrak; desain pasar |
| **Prinsip Wahyu** | Hasil apa pun yang dapat dicapai melalui mekanisme apa pun dapat dicapai melalui mekanisme langsung yang jujur ​​|
| **Contoh** | Lelang Vickrey (penawaran tertutup harga kedua) — menawar nilai sebenarnya adalah strategi dominan |
---

## Aplikasi
### Bisnis
| Aplikasi | Konsep Teori Permainan | Wawasan |
|-------------|-------------------|---------|
| **Persaingan harga** | Dilema Tahanan | Perang harga merugikan kedua perusahaan; kolusi diam-diam dalam permainan berulang |
| **Masuk pasar** | Permainan berurutan; komitmen | Ancaman petahana untuk melawan pendatang baru hanya dapat dipercaya jika mereka berinvestasi pada kapasitas |
| **Lelang** | Desain mekanisme | Lelang harga kedua menghasilkan nilai sebenarnya; lelang spektrum menghasilkan miliaran |
| **Negosiasi** | Permainan tawar-menawar; Kesetimbangan Nash | Bagi kelebihannya; keuntungan penggerak pertama dalam permainan ultimatum |
| **Sinyal** | Model pendidikan Spence | Sinyal mahal dapat dipercaya karena tipe berkualitas rendah tidak mampu membelinya |
### Hubungan Internasional
| Aplikasi | Konsep Teori Permainan | Wawasan |
|-------------|-------------------|---------|
| **Pacuan senjata** | Dilema Tahanan | Kedua belah pihak akan lebih baik melucuti senjatanya tetapi tidak bisa saling percaya |
| **Perang dagang** | Permainan berulang | Gayung-balas: bekerja sama sampai cacat lainnya, lalu membalas |
| **Perjanjian iklim** | Permainan barang publik | Menunggang bebas itu rasional; mekanisme penegakan hukum diperlukan |
| **Pencegahan** | Ayam; komitmen yang kredibel | Kehancuran yang dijamin bersama adalah keseimbangan Nash |
---

## Ringkasan
Teori permainan mempelajari interaksi strategis di mana hasil Anda bergantung pada tindakan orang lain. Ekuilibrium Nash – di mana tidak ada pemain yang mendapat manfaat dari perubahan strategi saja – adalah konsep solusi utama. Permainan klasik seperti dilema narapidana menunjukkan bahwa keputusan individu yang rasional dapat menghasilkan hasil yang buruk secara kolektif. Permainan berurutan diselesaikan dengan induksi mundur. Permainan yang berulang-ulang dapat mempertahankan kerja sama melalui ancaman hukuman di masa depan. Strategi campuran melibatkan pengacakan agar tetap tidak dapat diprediksi. Rancangan mekanisme membalikkan pertanyaan tersebut: alih-alih memprediksi hasil, mekanisme ini merancang aturan untuk mencapai hasil yang diinginkan (seperti dalam lelang). Penerapannya mencakup bisnis (penetapan harga, entri, lelang), politik (pemungutan suara, perjanjian), biologi (strategi stabil evolusioner), dan kehidupan sehari-hari. Pelajaran mendasarnya adalah bahwa strategi bukan hanya tentang apa yang Anda lakukan — ini tentang mengantisipasi apa yang akan dilakukan orang lain, mengetahui bahwa mereka juga melakukan hal yang sama.