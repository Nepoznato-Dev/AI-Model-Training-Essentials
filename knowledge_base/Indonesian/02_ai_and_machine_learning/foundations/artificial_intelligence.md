---
# Metadata
title: "Artificial Intelligence"
description: "AI overview, ML, deep learning, LLMs, ethics"
category: "AI and Machine Learning"
subcategory: "Foundations"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "AI Model Training Team"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "AI Model Training Team"
    changes: "Moved to foundations/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "AI Model Training Team"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [artificial, intelligence, ai-and-machine-learning]
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

# Kecerdasan Buatan
Kecerdasan buatan adalah upaya untuk membuat mesin yang dapat melakukan hal-hal yang memerlukan kecerdasan jika manusia melakukannya: mengenali wajah, memahami ucapan, membuat keputusan, menulis teks, bermain game, mengendarai mobil, mendiagnosis penyakit. Bidang ini sama tuanya dengan komputasi itu sendiri — Alan Turing bertanya, "Dapatkah mesin berpikir?" pada tahun 1950 — namun ledakan kemampuan yang terjadi baru-baru ini (tahun 2020-an) telah menjadikan AI sebagai salah satu teknologi yang paling penting dan diperebutkan dalam sejarah manusia.
---

## Sejarah Singkat
AI telah melalui siklus hype dan kekecewaan selama beberapa dekade. Memahami sejarah ini membantu Anda memahami mengapa orang-orang bersemangat dan skeptis.
| Zaman | Apa yang Terjadi | Hasil |
|-----|---------------|---------|
| **1950an-1960an** | Optimisme awal. Tes Turing diusulkan (1950). Koin Konferensi Dartmouth "Kecerdasan Buatan" (1956). Program awal seperti ELIZA (chatbot) dan SHRDLU (pemahaman bahasa). | Kegembiraan: "Kita akan memiliki AGI dalam satu generasi!" |
| **1970-an** | Musim dingin AI pertama. Keterbatasan pendekatan awal menjadi jelas. Pendanaan mengering. | Kekecewaan: janji tidak terpenuhi |
| **1980-an** | Booming sistem pakar — program berbasis aturan yang mengkodekan pengetahuan spesialis manusia. Proyek Generasi Kelima Jepang. | Kegembiraan lagi: investasi AI perusahaan |
| **1987-1993** | Musim dingin AI kedua. Sistem pakar terbukti rapuh dan mahal pemeliharaannya. | Kekecewaan lagi |
| **2000an** | Pembelajaran mesin mendapatkan daya tarik. Lebih banyak data tersedia (internet). Metode statistik menggantikan aturan kode tangan. | Kemajuan yang stabil |
| **2012+** | Revolusi pembelajaran mendalam. AlexNet memenangkan kompetisi ImageNet menggunakan GPU. Jaringan saraf mulai mengungguli metode tradisional dalam hal penglihatan, ucapan, dan bahasa. | Transformasi cepat |
| **2017** | Makalah "Attention Is All You Need" memperkenalkan arsitektur Transformer. | Landasan untuk segala sesuatu yang mengikuti |
| **2020-2026** | Model bahasa besar (GPT-3, GPT-4, Claude, Gemini, LLaMA). AI menghasilkan teks, kode, gambar, video. Adopsi perusahaan semakin cepat. | AI menjadi bagian dari kehidupan sehari-hari |
---

## Cara Kerja AI Modern
### Pembelajaran Mesin — Belajar dari Data
Alih-alih memprogram aturan eksplisit, pembelajaran mesin memasukkan data ke algoritme yang menemukan polanya sendiri.
| Ketik | Cara Kerja | Contoh |
|------|-------------|---------|
| **Pembelajaran yang diawasi** | Latih contoh yang diberi label (input → output yang benar) | Deteksi spam: berikan ribuan email berlabel "spam" atau "bukan spam" |
| **Pembelajaran tanpa pengawasan** | Temukan pola pada data yang tidak berlabel | Segmentasi pelanggan: mengelompokkan pelanggan serupa tanpa menentukan terlebih dahulu grupnya |
| **Pembelajaran penguatan** | Agen belajar dengan coba-coba, menerima hadiah atau penalti | AI bermain game: coba gerakan, dapatkan poin untuk menang, pelajari strategi mana yang berhasil |
### Pembelajaran Mendalam — Jaringan Syaraf Tiruan
Pembelajaran mendalam menggunakan jaringan saraf tiruan — lapisan operasi matematika sederhana yang, jika digabungkan, dapat mempelajari pola yang sangat kompleks. Yang "dalam" mengacu pada jumlah lapisan.
Arsitektur utama:
| Arsitektur | Terbaik Di | Penggunaan di Dunia Nyata |
|-------------|---------|----------------|
| **CNN** (Jaringan Syaraf Konvolusional) | Gambar dan data spasial | Pengenalan wajah, pencitraan medis, mobil self-driving |
| **RNN/LSTM** | Data sekuensial (deret waktu) | Pengenalan ucapan, generasi musik (sebagian besar digantikan oleh Transformers) |
| **Transformator** | Semuanya — teks, gambar, audio, kode | GPT, Claude, Gemini, BERT, DALL-E — arsitektur dominan |
| **GAN** (Jaringan Adversarial Generatif) | Menghasilkan data yang realistis | Sintesis gambar, transfer gaya (sebagian digantikan oleh model difusi) |
| **Model difusi** | Pembuatan gambar/video berkualitas tinggi | Difusi Stabil, DALL-E 3, Tengah Perjalanan, Sora |
### Model Bahasa Besar (LLM)
LLM adalah model berbasis Transformer yang dilatih pada teks dalam jumlah besar. Mereka belajar memprediksi token (potongan kata) berikutnya secara berurutan, yang ternyata membutuhkan pemahaman tata bahasa, fakta, penalaran, dan bahkan sesuatu yang menyerupai “pengetahuan”.
| Model | Pengembang | Fitur Penting |
|-------|-----------|-----------------|
| **GPT-4 / GPT-4o** | OpenAI | Multimodal (teks + gambar); penalaran yang kuat |
| **Claude** | Antropik | Fokus pada keamanan dan kemanfaatan; jendela konteks panjang |
| **Gemini** | Google DeepMind | Multimoda asli; terintegrasi dengan layanan Google |
| **LLaMA / Llama 3** | Meta | Berat terbuka; dapat dijalankan secara lokal; komunitas besar |
| **mistral** | AI Mistral | Model terbuka yang efisien bersaing dengan model yang jauh lebih besar |
**Proses pelatihan**:
1. **Pra-pelatihan**: Belajar dari data teks yang sangat besar (memprediksi token berikutnya). Di sinilah model memperoleh “pengetahuan”.
2. **Penyempurnaan**: Melatih tugas tertentu atau dengan preferensi manusia.
3. **RLHF** (Pembelajaran Penguatan dari Umpan Balik Manusia): Manusia menilai keluaran model; model belajar untuk menghasilkan keluaran yang disukai manusia.
**Jendela konteks** (berapa banyak teks yang dapat diproses model sekaligus) telah berkembang dari token 4K (GPT-3 awal) menjadi lebih dari 1 juta token pada model tahun 2026.
---

## Apa yang Bisa dan Tidak Bisa Dilakukan AI
### Kemampuan Saat Ini
| Tugas | Kinerja | Keterbatasan |
|------|-------------|-------------|
| **Pembuatan teks** | Luar biasa — koheren, kontekstual, bervariasi secara gaya | Dapat berhalusinasi (menghasilkan informasi palsu dengan percaya diri) |
| **Pembuatan kode** | Sangat bagus untuk pola umum; dapat menulis seluruh program | Berjuang dengan arsitektur baru; dapat menimbulkan bug halus |
| **Pembuatan gambar** | Fotorealistik; gaya artistik; pengeditan | Tangan dan teks masih belum sempurna; berjuang dengan penalaran spasial yang tepat |
| **Terjemahan** | Hampir mirip manusia untuk pasangan bahasa utama | Bahasa dengan sumber daya rendah kurang akurat; nuansa budaya bisa hilang |
| **Pengenalan ucapan** | Hampir seperti manusia dalam audio yang jernih | Berjuang dengan aksen yang berat, kebisingan latar belakang |
| **Penalaran** | Meningkat dengan cepat; dapat memecahkan banyak masalah logika | Gagal dalam permasalahan baru yang memerlukan pemahaman tulus |
| **Matematika** | Pandai dalam soal standar | Membuat kesalahan pada bukti baru; bukan pengganti verifikasi formal |
| **Perencanaan dan penggunaan alat** | Muncul (agen) | Masih tidak dapat diandalkan untuk tugas-tugas multi-langkah yang kompleks tanpa pengawasan manusia |
### Apa yang Tidak Dapat Dilakukan AI (mulai 2026)
- **Benar-benar memahami** apa pun yang dilakukan manusia — ia memproses pola, bukan makna
- **Menjamin keakuratan faktual** — halusinasi masih menjadi masalah yang belum terpecahkan
- **Ganti penilaian manusia** dalam keputusan berisiko tinggi tanpa pengawasan
- **Gneralisasikan dengan sempurna** ke domain yang sangat berbeda dengan data pelatihan
- **Beroperasi secara mandiri** di lingkungan fisik yang tidak dapat diprediksi (robotika masih sulit)
---

## Etika dan Keamanan AI
AI tidak netral. Hal ini mencerminkan data yang dilatih, pilihan pengembangnya, dan insentif dari organisasi yang menerapkannya.
### Masalah Utama
| Edisi | Apa yang Terjadi | Contoh |
|-------|-------------|---------|
| **Bias** | Sistem AI mereproduksi dan memperkuat bias dalam data pelatihan | Mempekerjakan algoritma yang memihak kandidat laki-laki; pengenalan wajah dengan tingkat kesalahan lebih tinggi untuk kulit lebih gelap |
| **Privasi** | AI dilatih tentang data pribadi; kemampuan pengawasan | Pelatihan tentang karya berhak cipta; pengenalan wajah di ruang publik |
| **Penyalahgunaan** | Deepfakes, disinformasi, phishing otomatis | Video palsu politisi yang dibuat oleh AI; panggilan penipuan otomatis |
| **Perpindahan pekerjaan** | Otomatisasi tugas yang sebelumnya dilakukan oleh manusia | Pembuatan konten, layanan pelanggan, entri data, beberapa pemrograman |
| **Penyelarasan** | Memastikan tujuan AI sesuai dengan nilai-nilai kemanusiaan | AI yang diperintahkan untuk "memaksimalkan produksi penjepit kertas" mungkin mengubah semua materi menjadi penjepit kertas |
| **Risiko eksistensial** | Kekhawatiran teoritis tentang AGI masa depan | Perdebatan di kalangan peneliti — beberapa menganggapnya mendesak, yang lain terlalu dini |
### Siapa yang Mengerjakan Keselamatan
- **Anthropic** — didirikan oleh mantan peneliti OpenAI yang secara khusus berfokus pada keamanan AI
- **Keamanan DeepMind** — tim peneliti dalam Google DeepMind
- **MIRI** (Machine Intelligence Research Institute) — penelitian keselamatan teoritis
- **ARC** (AI Research Center) — penelitian keamanan empiris
- **Badan pemerintah** — EU AI Act (2026), perintah eksekutif AS, kerangka kerja internasional
---

## AI dalam Praktek — Industri demi Industri
| Industri | Aplikasi | Kedewasaan |
|----------|-------------|----------|
| **Perawatan Kesehatan** | Mendiagnosis kanker dari gambar; penemuan obat (AlphaFold); memprediksi hasil pasien | Dikerahkan dan diperluas |
| **Keuangan** | Deteksi penipuan, perdagangan algoritmik, penilaian kredit, robo-advisors | Dikerahkan secara luas |
| **Transportasi** | Kendaraan tanpa pengemudi (Waymo, Tesla Autopilot); optimasi rute | Dikerahkan sebagian; otonomi penuh masih terbatas |
| **Pendidikan** | Pembelajaran yang dipersonalisasi; bimbingan AI; penilaian otomatis | Berkembang pesat |
| **Bidang kreatif** | Pembuatan gambar (Midjourney, DALL-E); musik; bantuan menulis; penyelesaian kode | Mengubah alur kerja sekarang |
| **Keamanan siber** | Deteksi ancaman; identifikasi anomali; baik serangan maupun pertahanan | Perlombaan senjata sedang berlangsung |
| **Hukum** | Analisis kontrak; peninjauan dokumen; penelitian hukum | Diadopsi; masalah akurasi |
| **Pertanian** | Pemantauan tanaman melalui satelit/drone; penyemprotan presisi; prediksi hasil | Tumbuh |
| **Manufaktur** | Inspeksi kualitas; pemeliharaan prediktif; optimalisasi rantai pasokan | Dikerahkan secara luas |
---

## Robotika dan AI yang Terwujud
Robotika menggabungkan AI dengan mesin fisik. Meskipun terdapat kemajuan selama beberapa dekade, interaksi fisik dengan dunia masih jauh lebih sulit dibandingkan dengan kecerdasan digital.
- **Boston Dynamics' Atlas** — gerakan bipedal tingkat lanjut; parkour; tugas gudang
- **Robot industri** (ABB, FANUC, KUKA) — mengotomatiskan manufaktur; pengelasan; perakitan
- **Robot bedah** (Sistem da Vinci) — operasi invasif minimal dengan presisi melebihi tangan manusia
- **Robot rumah tangga** (Roomba) — sederhana namun sukses secara komersial
- **Robot humanoid** (Tesla Optimus, Gambar AI) — muncul; tugas-tugas fisik untuk keperluan umum masih sangat sulit
Kesenjangan antara AI digital (yang telah mencapai kemajuan besar) dan AI fisik (yang berjuang dengan ketangkasan, keseimbangan, dan lingkungan yang tidak dapat diprediksi) adalah salah satu tantangan besar di bidang ini.
---

## Tren Saat Ini (2020-an)
| Tren | Apa yang Sedang Terjadi |
|-------|-------------------|
| **AI multimoda** | Sistem yang memproses teks, gambar, audio, dan video secara bersamaan (GPT-4V, Gemini) |
| **Agen** | LLM yang dapat menggunakan alat, menelusuri web, menulis kode, dan melakukan tindakan multi-langkah |
| **Model berbobot terbuka** | LLaMA Meta dan lainnya mendemokratisasi akses ke model besar |
| **AI pada perangkat** | Menjalankan model secara lokal di ponsel dan laptop (Apple Intelligence, Qualcomm NPUs) |
| **Peraturan AI** | EU AI Act (2026) — undang-undang AI komprehensif pertama; mengklasifikasikan sistem berdasarkan tingkat risiko |
| **AI dalam sains** | Pelipatan protein (AlphaFold), penemuan material, pemodelan iklim, bukti matematis |
| **Model bahasa kecil** | Model efisien yang dijalankan pada perangkat keras konsumen; kualitas mendekati model yang lebih besar |
---

## Ringkasan
AI merupakan perkembangan teknologi paling signifikan di abad ke-21 sejauh ini. Ini bukan keajaiban — ini adalah pencocokan pola dalam skala besar, yang dimungkinkan oleh data yang sangat besar, perangkat keras yang kuat, dan arsitektur yang cerdas. Yang menjadikannya transformatif adalah pencocokan pola, jika dilakukan dengan cukup baik, dapat mereplikasi banyak tugas yang sebelumnya memerlukan kecerdasan manusia. Tantangan yang dihadapi juga sama besarnya: halusinasi, bias, perpindahan pekerjaan, penyalahgunaan, dan pertanyaan terbuka apakah jalur dari AI yang sempit menuju kecerdasan umum itu pendek atau sangat panjang. Yang jelas AI akan mengubah setiap industri, setiap profesi, dan setiap aspek kehidupan sehari-hari. Memahami cara kerjanya – dan apa yang tidak bisa dilakukan – sangat penting untuk menavigasi dunia yang sedang kita bangun.