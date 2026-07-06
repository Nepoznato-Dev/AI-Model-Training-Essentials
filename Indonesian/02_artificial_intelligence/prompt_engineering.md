# Rekayasa Cepat

Rekayasa cepat adalah praktik merancang, menyempurnakan, dan mengoptimalkan perintah masukan untuk mendapatkan keluaran terbaik dari model bahasa. Ini adalah seni dan sains, dan merupakan antarmuka utama untuk mengendalikan perilaku LLM tanpa penyesuaian.

---

## Prinsip Inti

### Kejelasan dan Kekhususan
Perintah yang jelas tidak memberikan ruang bagi ambiguitas. Tentukan dengan tepat apa yang Anda inginkan, termasuk format, panjang, dan perspektif.

**Tidak jelas:**
> "Ceritakan tentang Python."

**Khusus:**
> "Jelaskan Global Interpreter Lock (GIL) Python. Jelaskan dampaknya terhadap multithreading, berikan satu solusi, dan simpan jawaban Anda kurang dari 200 kata."

### Memberikan Konteks
Model berkinerja lebih baik ketika mereka mengetahui peran, audiens, dan tujuannya.

**Tanpa konteks:**
> "Tulis fungsi untuk mengurutkan daftar."

**Dengan konteks:**
> "Anda adalah pengembang senior Python. Tulis fungsi untuk mengurutkan daftar kamus berdasarkan kunci tertentu. Gunakan petunjuk tipe dan tangani kasus tepi. Audiensnya adalah pengembang junior."

### Gunakan Petunjuk Positif
Beri tahu model apa yang harus dilakukan, bukan apa yang harus dihindari. "Jangan sertakan jargon" lebih lemah daripada "Gunakan bahasa sederhana yang dapat diakses oleh anak berusia 10 tahun."

---

## Struktur Prompt

### Peran Sistem / Pengguna / Asisten
Kebanyakan LLM API mendukung struktur multi-putaran:

- **Pesan sistem**: Menyetel perilaku, persona, dan batasan model (bertahan sepanjang sesi).
- **Pesan pengguna**: Kueri atau instruksi saat ini.
- **Pesan Asisten**: Respons model sebelumnya (digunakan untuk kontinuitas).

**Contoh (gaya OpenAI API):**
Sistem: Anda adalah asisten pengkodean yang membantu. Anda membalas dengan contoh kode ringkas dan penjelasan singkat. Jangan pernah memberikan kode yang tidak aman.
Pengguna: Tulis fungsi Python untuk mengunduh file dari URL.

### Anjuran Sedikit Tembakan
Berikan 2–3 contoh format input-output yang diinginkan sebelum meminta model melakukan tugas tersebut. Ini mengajarkan polanya.

**Contoh:**
Pengguna: Ubah kalimat berikut menjadi kalimat pasif:
Masukan : Kucing mengejar tikus.
Kesimpulan: Tikus dikejar kucing.
Masukan: Koki memasak makanannya.
Kesimpulan: Makanan dimasak oleh koki.
Masukan: Badai menghancurkan rumah.
Keluaran: (model selesai)

### Rantai Pemikiran (CoT)
Dorong model untuk menunjukkan alasannya langkah demi langkah. Hal ini meningkatkan akurasi pada tugas aritmatika, logika, dan multi-langkah.

**Tanpa CoT:**
> "Apa itu 24×37?"

**Dengan CoT:**
> "Hitung 24×37. Tunjukkan alasan Anda langkah demi langkah."

Model ini akan menghasilkan langkah-langkah perantara, mengurangi kesalahan aritmatika.

### Keluaran Terstruktur
Minta format tertentu seperti JSON, YAML, atau tabel penurunan harga agar penguraian dapat diandalkan.
Pengguna: Sebutkan tiga kelebihan dan tiga kekurangan layanan mikro. Kembalikan hanya objek JSON yang valid dengan kunci "pro" dan "kontra", masing-masing berupa array string.

---

## Teknik Tingkat Lanjut

### Konsistensi Diri
Hasilkan beberapa tanggapan untuk pertanyaan yang sama (dengan suhu > 0) dan ambil suara mayoritas pada jawaban akhir. Hal ini sangat efektif untuk tugas-tugas penalaran.

### Pohon Pikiran
Jelajahi berbagai jalur penalaran secara paralel, evaluasi masing-masing jalur, dan pilih yang terbaik. Ini adalah teknik tingkat penelitian tetapi dapat diperkirakan dengan meminta model untuk "mengeksplorasi solusi alternatif".

### ReAct (Penalaran + Akting)
Biarkan model menyisipkan penalaran dengan pemanggilan alat. Ia dapat berpikir, lalu bertindak (misalnya menelusuri web, menjalankan kode), lalu berpikir lagi berdasarkan hasilnya.

**Struktur cepat:**
Anda memiliki akses ke kalkulator dan mesin pencari. Untuk setiap langkah, keluaran:
Pikir: (alasan Anda)
Tindakan: (nama alat, masukan)
Pengamatan: (keluaran alat)
... lanjutkan sampai Anda mendapatkan jawaban akhir.

### Penugasan Persona
Tetapkan persona tertentu untuk membingkai respons.

**Contoh:**
- "Anda adalah pengembang kernel Linux yang menjelaskan manajemen memori kepada lulusan baru."
- "Anda adalah ahli gizi ramah yang memberikan nasihat umum kepada klien."
- "Anda adalah kritikus teknologi sinis yang mengulas gadget baru."

---

## Penyetelan Parameter

- **Suhu** (0,0 – 1,0+): Mengontrol keacakan. Lebih rendah = lebih deterministik, lebih tinggi = lebih kreatif. Gunakan 0,0–0,3 untuk jawaban faktual; 0,7–1,0 untuk penulisan kreatif.
- **Top-p** (pengambilan sampel inti): Memotong massa probabilitas pada ambang batas kumulatif tertentu. 0,9 berarti sampel model dari 90% token teratas yang mungkin ada. Biasanya menyesuaikan suhu atau top-p, tidak keduanya.
- **Token maks**: Menyetel panjang keluaran maksimum. Ingatlah untuk menyediakan ruang untuk respons dalam jendela konteks.
- **Penalti frekuensi**: Mengurangi pengulangan token yang sama.
- **Penalti kehadiran**: Mendorong model untuk memperkenalkan topik baru.

---

## Kesalahan dan Perbaikan Umum| Masalah | Kemungkinan penyebab | Perbaiki |
|---------|--------------|-----|
| Model mengabaikan bagian dari prompt | Prompt terlalu lama atau kelebihan beban | Mempersingkat; letakkan instruksi terpenting di akhir |
| Outputnya terlalu bertele-tele | Tidak ada batasan panjang | Tambahkan "Batasi hingga 3 kalimat" atau setel max_tokens |
| Output terlalu singkat | Terlalu membatasi | Tambahkan "Jelaskan secara detail" atau turunkan suhu |
| Halusinasi faktual | Konteks tidak memadai atau pertanyaan ambigu | Tambahkan "Jika Anda tidak yakin, katakan 'Saya tidak tahu'" dan berikan konteks RAG |
| Pemformatan tidak konsisten | Tidak ada instruksi format eksplisit | Minta JSON, tabel penurunan harga, atau daftar poin |
| Modelkan jawaban dalam bahasa yang salah | Tidak ada instruksi bahasa | Nyatakan secara eksplisit "Respon dalam bahasa Inggris" (atau bahasa target Anda) |

---

## Templat Prompt untuk Tugas Umum

### Ringkasan
Ringkaslah teks berikut dalam 3 poin-poin. Fokus pada argumen utama dan hindari detail.

Teks: [masukkan teks]


### Pembuatan Kode
Tulis fungsi [bahasa] yang [melakukan X].
Persyaratan:

Gunakan petunjuk tipe.

Sertakan dokumen.

Menangani kasus tepi: [daftar].

Jangan gunakan perpustakaan eksternal kecuali ditentukan.


### Penjelasan
Jelaskan [konsep] kepada [yang bukan ahli/mahasiswa/anak]. Gunakan analogi jika diperlukan.

### Bertukar pikiran
Hasilkan 10 ide untuk [topik]. Untuk setiap ide, berikan deskripsi satu kalimat dan satu tantangan potensial.

teks

### Klasifikasi
Klasifikasikan umpan balik pelanggan berikut sebagai [positif, netral, negatif].
Berikan skor keyakinan (0-100) dan alasan singkat.

Umpan Balik: [masukkan teks]

### Terjemahan dengan Gaya
Terjemahkan teks bahasa Inggris berikut ke bahasa Spanyol. Gunakan nada informal yang cocok untuk postingan media sosial.
Teks: [masukkan teks]

---

## Evaluasi Anjuran

Perlakukan perintah sebagai kode: buat versinya, uji, dan ulangi.

- **Pengujian A/B** varian perintah yang berbeda pada kumpulan kueri yang ditunda.
- **Ukur keberhasilan** melalui evaluasi manusia atau metrik otomatis (misalnya, pencocokan tepat, BLEU, penilaian khusus).
- **Simpan registri cepat** (file teks sederhana atau spreadsheet) dengan perintah, versi, dan kinerja yang diamati.

---