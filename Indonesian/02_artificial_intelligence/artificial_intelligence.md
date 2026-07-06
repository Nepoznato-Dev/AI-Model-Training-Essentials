# Kecerdasan Buatan

## Apa itu Kecerdasan Buatan?

Kecerdasan Buatan (AI) mengacu pada simulasi kecerdasan manusia dalam mesin yang diprogram untuk berpikir, belajar, dan memecahkan masalah. Sistem AI dapat melakukan tugas-tugas yang biasanya memerlukan kecerdasan manusia, seperti mengenali ucapan, mengambil keputusan, menerjemahkan bahasa, dan mengidentifikasi objek dalam gambar. Istilah ini diciptakan oleh John McCarthy pada tahun 1956 di Konferensi Dartmouth, yang secara luas dianggap sebagai peristiwa pendiri AI sebagai sebuah bidang.

AI modern secara luas dibagi menjadi AI Sempit (juga disebut AI Lemah), yang dirancang untuk tugas-tugas tertentu, dan Kecerdasan Umum Buatan (AGI) teoretis, yang akan menyamai atau melampaui kemampuan kognitif manusia di semua domain. Semua sistem AI saat ini adalah AI Sempit.

## Sejarah AI

Sejarah AI mencakup hampir delapan dekade. Landasan teoretis awal diletakkan oleh Alan Turing, yang makalahnya pada tahun 1950, "Mesin Komputasi dan Kecerdasan", memperkenalkan Tes Turing - suatu ukuran kemampuan mesin untuk menunjukkan perilaku cerdas yang tidak dapat dibedakan dari manusia. Konferensi Dartmouth tahun 1956 secara resmi menetapkan AI sebagai disiplin akademis.

Tahun 1950-an–1970-an menyaksikan program-program awal yang optimis seperti ELIZA (chatbot sederhana) dan LISP (bahasa pemrograman yang dirancang untuk AI). “Musim dingin AI” pada tahun 1970an dan 1980an adalah periode berkurangnya pendanaan dan bunga karena ekspektasi yang tidak terpenuhi. Kebangkitan sistem pakar terjadi pada tahun 1980an – program berbasis aturan yang mengkodekan keahlian manusia. Tahun 2000-an membawa terobosan pembelajaran mesin yang didorong oleh internet dan kumpulan data yang terus berkembang. Pada tahun 2010-an terjadi kebangkitan pembelajaran mendalam, transformasi visi komputer, pemrosesan bahasa alami (NLP), dan pembelajaran penguatan.

## Pembelajaran Mesin

Machine Learning (ML) adalah bagian dari AI yang memungkinkan sistem belajar dari data tanpa diprogram secara eksplisit. Kategori utama ML meliputi:

**Pembelajaran yang Diawasi**: Model dilatih pada pasangan input-output yang diberi label. Contohnya termasuk deteksi spam dan klasifikasi gambar. Algoritma mencakup regresi linier, pohon keputusan, mesin vektor dukungan, dan jaringan saraf.

**Pembelajaran Tanpa Pengawasan**: Model menemukan pola dalam data yang tidak berlabel. Contohnya termasuk segmentasi pelanggan dan deteksi anomali. Algoritmanya mencakup pengelompokan k-means dan analisis komponen utama (PCA).

**Pembelajaran Penguatan**: Agen belajar dengan berinteraksi dengan lingkungan, menerima hadiah atau penalti. Digunakan dalam AI permainan (AlphaGo, AlphaZero), robotika, dan sistem rekomendasi.

**Pembelajaran Semi-Supervised dan Self-Supervised**: Menggabungkan sejumlah kecil data berlabel dengan kumpulan data besar yang tidak berlabel. Model GPT menggunakan pendekatan pengawasan mandiri selama pra-pelatihan.

## Pembelajaran Mendalam

Deep Learning merupakan bagian dari pembelajaran mesin yang menggunakan jaringan saraf tiruan dengan banyak lapisan (deep network). Terinspirasi secara longgar oleh struktur saraf otak, jaringan ini mempelajari representasi data secara hierarkis. Kekuatan pembelajaran mendalam:

- **Computer Vision**: Pengenalan gambar, deteksi objek, pencitraan medis
- **Pemrosesan Bahasa Alami**: Terjemahan mesin, analisis sentimen, menjawab pertanyaan
- **Pengenalan Ucapan**: Asisten suara seperti Siri, Alexa, Asisten Google
- **AI Generatif**: Pembuatan gambar (DALL-E, Difusi Stabil), pembuatan teks (GPT)

Arsitektur pembelajaran mendalam yang utama mencakup jaringan saraf konvolusional (CNN) untuk gambar, jaringan saraf berulang (RNN) dan LSTM untuk urutan, transformator untuk bahasa, dan jaringan permusuhan generatif (GAN) untuk sintesis.

## Model Bahasa Besar (LLM)

Model Bahasa Besar (LLM) adalah sistem AI yang dilatih pada data teks dalam jumlah besar untuk memahami dan menghasilkan bahasa manusia. Mereka didasarkan pada arsitektur Transformer, yang diperkenalkan dalam makalah tahun 2017 "Attention is All You Need" oleh Vaswani dkk. LLM memprediksi token berikutnya (potongan kata) secara berurutan, memungkinkan mereka menghasilkan teks yang koheren, menjawab pertanyaan, menulis kode, dan melakukan tugas penalaran.

LLM terkenal meliputi:
- **Seri GPT** (OpenAI): GPT-3, GPT-4, dan penerusnya — banyak digunakan untuk chat dan kode
- **Claude** (Antropis): Berfokus pada keselamatan dan kegunaan
- **Gemini** (Google DeepMind): Multimodal, mengintegrasikan teks, gambar, dan kode
- **LLaMA / Llama 3** (Meta): Model bobot terbuka untuk penelitian dan penerapan lokal
- **Mistral** (Mistral AI): Model terbuka yang efisien bersaing dengan LLM yang jauh lebih besar

LLM dilatih dalam dua tahap: pra-pelatihan (tanpa pengawasan pada korpora teks besar) dan penyesuaian (diawasi atau melalui pembelajaran penguatan dari umpan balik manusia, RLHF). Jendela konteks menjelaskan berapa banyak teks yang dapat diproses LLM sekaligus, mulai dari token 4K (GPT-3 awal) hingga lebih dari 1 juta token pada model paling canggih tahun 2024.

## Etika dan Keamanan AIAI menimbulkan pertanyaan etika yang penting termasuk bias, privasi, perpindahan pekerjaan, dan risiko penyalahgunaan. Bias algoritmik terjadi ketika data pelatihan mencerminkan ketidaksetaraan historis, sehingga menyebabkan sistem AI menghasilkan keluaran yang diskriminatif. Sistem pengenalan wajah menunjukkan tingkat kesalahan yang lebih tinggi pada individu berkulit gelap. Algoritme perekrutan terbukti lebih menguntungkan kandidat laki-laki.

Keamanan AI adalah bidang yang didedikasikan untuk memastikan sistem AI berfungsi sebagaimana mestinya tanpa menimbulkan bahaya yang tidak diinginkan. Kekhawatiran utama meliputi:
- **Penyelarasan**: Memastikan tujuan AI sesuai dengan nilai-nilai kemanusiaan
- **Interpretabilitas / Penjelasan**: Memahami alasan AI mengambil keputusan (penting dalam bidang kedokteran, hukum, keuangan)
- **Penyalahgunaan**: deepfake, disinformasi, dan serangan siber yang dihasilkan oleh AI
- **Risiko eksistensial**: Kekhawatiran teoretis bahwa AGI di masa depan dapat mengejar tujuan yang tidak sejalan dengan kelangsungan hidup manusia

Organisasi yang menangani keamanan AI termasuk tim Keamanan OpenAI, Anthropic (didirikan oleh mantan peneliti keamanan OpenAI), tim keamanan DeepMind, dan lembaga independen seperti MIRI dan ARC.

## AI di Masyarakat

AI mentransformasi hampir setiap industri:

- **Layanan Kesehatan**: AI membantu dalam mendiagnosis kanker dari gambar medis, memprediksi hasil akhir pasien, mempercepat penemuan obat (memecahkan prediksi struktur pelipatan protein AlphaFold), dan mempersonalisasi rencana perawatan.
- **Keuangan**: Deteksi penipuan, perdagangan algoritmik, penilaian kredit, dan robo-advisor menggunakan model ML.
- **Transportasi**: Kendaraan self-driving menggunakan computer vision, lidar, dan pembelajaran penguatan. Tesla Autopilot, Waymo, dan Cruise memimpin upaya ini.
- **Pendidikan**: Platform pembelajaran yang dipersonalisasi menyesuaikan konten dengan kecepatan dan gaya belajar masing-masing siswa.
- **Bidang kreatif**: AI menghasilkan musik, seni, dan tulisan; alat seperti Midjourney, DALL-E, dan GitHub Copilot telah mengubah alur kerja kreatif.
- **Keamanan siber**: AI mendeteksi anomali, mengidentifikasi ancaman, dan memperkuat serangan dan pertahanan.

## Robotika dan AI yang Terwujud

Robotika menggabungkan AI dengan mesin fisik. Robot modern menggunakan persepsi (kamera, lidar), perencanaan, dan kontrol untuk menavigasi dan memanipulasi lingkungan. Atlas Boston Dynamics mendemonstrasikan gerakan bipedal tingkat lanjut. Robot industri dari perusahaan seperti ABB dan FANUC mengotomatiskan manufaktur. Robot rumah tangga (Roomba) dan robot bedah (Sistem da Vinci) menerapkan AI dalam lingkungan sehari-hari dan medis. Penelitian AI yang diwujudkan berfokus pada agen yang mempelajari keterampilan fisik melalui interaksi dengan dunia, menjembatani kesenjangan antara lingkungan simulasi dan nyata.

## Tren AI Saat Ini (2020-an)

- **AI Multimodal**: Sistem yang memproses teks, gambar, audio, dan video secara bersamaan (GPT-4V, Gemini)
- **Agen dan AI agen**: LLM yang dapat menggunakan alat, menjelajahi web, menulis kode, dan melakukan tindakan multi-langkah (Operator OpenAI, Penggunaan Komputer Antropis)
- **Model bobot terbuka**: LLaMA Meta mendemokratisasikan akses ke model besar bagi para peneliti
- **AI pada perangkat**: Menjalankan model AI secara lokal di ponsel dan laptop tanpa konektivitas cloud (Apple Intelligence, Qualcomm NPU)
- **Regulasi AI**: EU AI Act (2024) adalah undang-undang AI komprehensif pertama di dunia, yang mengklasifikasikan sistem AI berdasarkan tingkat risiko