---
# Metadata
title: "Blockchain and Distributed Systems"
description: "Consensus, smart contracts, DeFi, Byzantine fault tolerance"
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
tags: [blockchain, distributed, systems, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "7 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Blockchain dan Sistem Terdistribusi
Blockchain adalah jenis sistem terdistribusi yang spesifik — buku besar yang terdesentralisasi dan hanya ditambahkan di mana catatan (blok) dihubungkan dengan hash kriptografi. Sistem terdistribusi adalah bidang yang lebih luas yang membuat banyak komputer bekerja sama menjadi satu. Kedua konsep tersebut penting untuk memahami infrastruktur modern, mulai dari mata uang kripto hingga database terdistribusi hingga algoritma konsensus yang mendukung layanan global.
---

## Dasar-Dasar Sistem Terdistribusi
### Mengapa Sistem Terdistribusi?
| Motivasi | Deskripsi |
|-----------|-------------|
| **Skalabilitas** | Tambahkan lebih banyak mesin untuk menangani lebih banyak beban |
| **Toleransi kesalahan** | Sistem terus bekerja meskipun beberapa mesin gagal |
| **Distribusi geografis** | Melayani pengguna dari pusat data terdekat |
| **Spesialisasi** | Mesin yang berbeda menangani tugas yang berbeda |
### Konsep Utama
| Konsep | Deskripsi | Tantangan |
|---------|-------------|-----------|
| **Konsensus** | Membuat semua node menyetujui nilai | Partisi jaringan; Kesalahan Bizantium |
| **Replikasi** | Menyalin data di beberapa node | Konsistensi vs ketersediaan |
| **Mempartisi (sharding)** | Memisahkan data antar node | Titik panas; kueri lintas pecahan |
| **Model konsistensi** | Jaminan tentang apa yang dilihat oleh pembaca berbeda | Konsistensi yang kuat itu lambat; konsistensi akhirnya dapat mengejutkan pengguna |
| **Teorema CAP** | Anda hanya dapat memiliki 2 dari: Konsistensi, Ketersediaan, Toleransi partisi | Dalam praktiknya, toleransi partisi diperlukan; pilih C atau A |
### Teorema CAP
| Pilihan | Apa yang Anda Dapatkan | Apa yang Anda Serahkan | Contoh |
|--------|-------------|-----------------|---------|
| **CP** | Konsisten + toleran terhadap partisi | Beberapa node mungkin tidak tersedia selama partisi | HBase, MongoDB, Redis |
| **AP** | Tersedia + toleran partisi | Pembacaan dapat mengembalikan data basi | Cassandra, DynamoDB, CouchDB |
| **CA** | Konsisten + tersedia | Tidak dapat mentolerir partisi jaringan | Database node tunggal (tidak benar-benar terdistribusi) |
---

## Algoritma Konsensus
Bagaimana node terdistribusi menyetujui keadaan sistem?
| Algoritma | Ketik | Toleransi Kesalahan | Digunakan Dalam |
|-----------|------|----------------|---------|
| **Paxos** | Toleransi kesalahan kerusakan | Kegagalan hingga f dengan 2f+1 node | Google Gemuk; teori dasar |
| **Rakit** | Toleransi kesalahan kerusakan | Kegagalan hingga f dengan 2f+1 node | dll, Konsul, TiKV |
| **PBFT** | Toleransi kesalahan Bizantium | Hingga f kegagalan dengan 3f+1 node | Kain Hyperledger |
| **Bukti Kerja** | Toleransi kesalahan Bizantium | Tergantung pada kekuatan hash | Bitcoin |
| **Bukti Taruhan** | Toleransi kesalahan Bizantium | Tergantung pada taruhan | Ethereum 2.0, Cardano |
### Rakit (Sederhana)
| Peran | Tanggung jawab |
|------|---------------|
| **Pemimpin** | Menangani semua permintaan klien; mengirimkan entri log ke pengikut |
| **Pengikut** | Menanggapi permintaan pemimpin; suara dalam pemilu |
| **Kandidat** | Meminta suara untuk menjadi pemimpin |
1. Semua node dimulai sebagai pengikut
2. Jika seorang pengikut tidak mendengar kabar dari pemimpinnya selama batas waktu pemilihan, ia menjadi kandidat
3. Kandidat meminta suara; yang mendapat suara terbanyak menjadi pemimpin
4. Pemimpin mereplikasi entri log ke pengikut
5. Ketika mayoritas menyetujui, entri tersebut dilakukan
---

## Blockchain
### Cara Kerja Blockchain
| Komponen | Deskripsi |
|-----------|-------------|
| **Blokir** | Kumpulan transaksi + metadata + hash dari blok sebelumnya |
| **hash** | Sidik jari kriptografi dari isi blok |
| **Rantai** | Setiap blok mereferensikan hash blok sebelumnya, menciptakan rantai | yang tidak dapat diubah
| **Konsensus** | Peserta jaringan menyetujui blok mana yang akan ditambahkan |
| **Pohon Merkle** | Pohon hash yang merangkum semua transaksi dalam satu blok |
### Mengapa Blockchain Sulit untuk Dirusak
1. Setiap blok berisi hash dari blok sebelumnya
2. Mengubah transaksi apa pun akan mengubah hash blok
3. Hash yang diubah memutus rantai — semua blok berikutnya menjadi tidak valid
4. Penyerang perlu menambang ulang semua blok berikutnya DAN mengontrol >50% jaringan
### Jenis Blockchain
| Ketik | Akses | Validator | Contoh |
|------|--------|-----------|---------|
| **Publik (tanpa izin)** | Siapapun dapat membaca dan menulis | Konsensus terbuka (PoW, PoS) | Bitcoin, Ethereum |
| **Pribadi (diizinkan)** | Akses terbatas | Validator yang dikenal | Hyperledger, Corda |
| **Konsorsium** | Diatur oleh sekelompok organisasi | Validator terpilih | R3 Corda untuk perbankan |
### Kontrak Cerdas
Kode yang dijalankan sendiri disimpan di blockchain yang berjalan ketika kondisi yang telah ditentukan terpenuhi.
| Peron | Bahasa | Fitur Penting |
|----------|----------|-----------------|
| **Ethereum** | Soliditas, Vyper | Ekosistem kontrak pintar terbesar |
| **Solana** | Karat, C | Throughput tinggi; biaya rendah |
| **Kardano** | Haskell (Plutus) | Ditinjau sejawat; verifikasi formal |
| **Hyperledger** | Buka, Java, JavaScript | Perusahaan; diizinkan |
---

## Mata Uang Kripto
| Mata uang | Konsensus | Pasokan | Penggunaan Utama |
|----------|-----------|--------|-------------|
| **Bitcoin** | Bukti Kerja | 21 juta (dibatasi) | Penyimpan nilai; emas digital |
| **Ethereum** | Bukti Taruhan | Tanpa batasan keras | Kontrak pintar; DeFi; NFT |
| **Solana** | Bukti Taruhan + Bukti Sejarah | Tanpa batasan keras | Transaksi berkecepatan tinggi |
| **Kardano** | Bukti Taruhan (Ouroboros) | 45 miliar (dibatasi) | Pendekatan akademis; keberlanjutan |
---

## Basis Data Terdistribusi
| Basis Data | Arsitektur | Konsistensi | Terbaik Untuk |
|----------|-------------|------------|----------|
| **Cassandra** | Kolom lebar; rekan-ke-rekan | Merdu (akhirnya mencapai kuorum) | Throughput penulisan yang tinggi; deret waktu |
| **MongoDB** | Dokumen; set replika | Akhirnya (dengan opsi konsistensi kausal) | Skema fleksibel; perkembangan pesat |
| **KecoaDB** | SQL terdistribusi; Konsensus rakit | Kuat | SQL terdistribusi; penyebaran global |
| **TiDB** | SQL terdistribusi; Rakit (melalui TiKV) | Kuat | Kompatibel dengan MySQL; penskalaan horizontal |
| **DynamoDB** | Nilai kunci; dikelola | Akhirnya (atau kuat dengan pembacaan yang konsisten) | Tanpa server; Terintegrasi AWS |
| **Kunci pas** | SQL terdistribusi; Paxos | Kuat | Google Awan; konsistensi global |
---

## Pola Sistem Terdistribusi
| Pola | Deskripsi | Kasus Penggunaan |
|---------|-------------|----------|
| **Pemilihan pemimpin** | Pilih satu node untuk dikoordinasikan | Pemimpin rakit; Penjaga Kebun Binatang |
| **Replikasi** | Salin data untuk redundansi dan baca penskalaan | Replika basis data; CDN |
| **Pecahan** | Partisi data berdasarkan rentang kunci atau hash | Database skala besar |
| **Pengurangan Peta** | Membagi komputasi antar node; hasil agregat | Pemrosesan data besar |
| **Protokol gosip** | Node secara berkala berbagi status dengan rekan acak | keanggotaan klaster; deteksi kegagalan |
| **Komitmen dua fase** | Koordinasikan transaksi di beberapa node | Basis data terdistribusi |
| **Pola saga** | Serangkaian transaksi lokal dengan tindakan kompensasi | Transaksi layanan mikro |
| **Pemutus arus** | Berhenti menelepon layanan yang gagal; gagal cepat | Ketangguhan; mencegah kegagalan berjenjang |
---

## Tantangan dalam Sistem Terdistribusi
| Tantangan | Deskripsi | Mitigasi |
|-----------|-------------|------------|
| **Partisi jaringan** | Node tidak dapat berkomunikasi | pertukaran CAP; coba lagi dengan backoff |
| **Jam miring** | Node yang berbeda memiliki jam yang berbeda | Gunakan jam logis; NTP; hindari mengandalkan waktu jam dinding |
| **Kesalahan Bizantium** | Node yang berbohong atau berperilaku sewenang-wenang | Konsensus BFT; blockchain |
| **Pisahkan otak** | Dua node sama-sama mengira mereka adalah pemimpin | Pagar; keputusan berbasis kuorum |
| **Kegagalan bertingkat** | Satu kegagalan memicu kegagalan lainnya | Pemutus arus; sekat; degradasi anggun |
| **Konsistensi data** | Menjaga replika tetap sinkron | Model konsistensi; resolusi konflik |
---

## Ringkasan
Sistem terdistribusi adalah cara perangkat lunak modern berkembang, bertahan dari kegagalan, dan melayani pengguna secara global. Algoritme konsensus (Raft, Paxos) memastikan node setuju. Blockchain menambahkan verifikasi kriptografi dan desentralisasi untuk menciptakan buku besar yang tidak dapat dipercaya. Basis data terdistribusi (Cassandra, CockroachDB, DynamoDB) menangani data dalam skala besar. Pertukaran mendasar – yang ditangkap oleh teorema CAP – adalah antara konsistensi dan ketersediaan ketika jaringan tidak dapat diandalkan. Memahami konsep-konsep ini penting untuk membangun sistem yang berfungsi pada skala internet.