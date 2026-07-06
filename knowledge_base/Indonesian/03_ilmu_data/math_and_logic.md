# Matematika dan Logika

## Apa itu Matematika?

Matematika adalah studi tentang angka, bentuk, pola, dan hubungan logis. Matematika adalah ilmu sekaligus bahasa yang digunakan untuk menggambarkan alam semesta. Matematika dibagi menjadi cabang-cabang termasuk aritmatika, aljabar, geometri, kalkulus, statistika, dan logika. Matematika adalah fondasi fisika, teknik, ilmu komputer, ekonomi, dan banyak bidang lainnya.

## Aritmatika

Aritmatika adalah cabang matematika yang berurusan dengan operasi dasar pada angka. Empat operasi fundamental adalah penjumlahan (+), pengurangan (−), perkalian (×), dan pembagian (÷). Urutan operasi menentukan urutan perhitungan yang harus dilakukan: Tanda Kurung, Eksponen, Perkalian dan Pembagian (kiri ke kanan), Penjumlahan dan Pengurangan (kiri ke kanan). Ini sering diingat sebagai **PEMDAS** atau **BODMAS**. Bilangan prima adalah bilangan bulat lebih besar dari 1 yang tidak memiliki pembagi selain 1 dan dirinya sendiri. Bilangan prima pertama adalah 2, 3, 5, 7, 11, 13, 17, 19, 23, dan 29.

**Contoh:**
- Faktorisasi prima: 84 = 2² × 3 × 7
- Pembagi Persekutuan Terbesar (FPB) dari 24 dan 36: 12
- Kelipatan Persekutuan Terkecil (KPK) dari 4 dan 6: 12

## Aljabar

Aljabar menggunakan huruf dan simbol untuk merepresentasikan angka dan kuantitas dalam persamaan dan rumus. **Variabel** adalah simbol (biasanya huruf) yang mewakili kuantitas yang tidak diketahui atau berubah. **Persamaan** menyatakan bahwa dua ekspresi sama. Menyelesaikan persamaan berarti menemukan nilai variabel yang membuat persamaan benar.

**Rumus kuadrat** menyelesaikan persamaan berbentuk ax² + bx + c = 0: x = (−b ± √(b²−4ac)) / (2a)

**Fungsi** memetakan setiap input ke tepat satu output. Fungsi umum meliputi:
- Linear: y = mx + b (garis lurus, laju perubahan konstan)
- Kuadratik: y = ax² + bx + c (parabola, melengkung)
- Eksponensial: y = a × bˣ (pertumbuhan atau peluruhan, perubahan cepat)
- Logaritmik: y = log_b(x) (invers dari eksponensial)

**Konsep kunci:**
- Domain: himpunan semua nilai input yang mungkin
- Range: himpunan semua nilai output yang mungkin
- Slope: laju perubahan (m dalam y = mx + b)
- Intercept: tempat fungsi memotong sumbu y (b dalam y = mx + b)

## Geometri

Geometri adalah cabang matematika yang mempelajari bentuk, ukuran, posisi, dan sifat figur. Titik tidak memiliki ukuran; titik mewakili lokasi. Garis memanjang tak terbatas di kedua arah. Ruas garis memiliki dua titik ujung. Sudut dibentuk oleh dua sinar yang berbagi titik ujung.

**Aturan kunci:**
- Jumlah sudut dalam segitiga selalu 180 derajat.
- Jumlah sudut dalam segiempat selalu 360 derajat.
- Teorema Pythagoras: dalam segitiga siku-siku, a² + b² = c² (di mana c adalah hipotenusa).
- Keliling lingkaran: 2πr
- Luas lingkaran: πr²
- Volume bola: (4/3)πr³

**π (pi)** kira-kira 3.14159 dan merupakan rasio keliling lingkaran terhadap diameternya.

**Bentuk geometris umum:**
- Segitiga: 3 sisi, jumlah sudut 180°
- Persegi: 4 sisi sama, 4 sudut siku-siku
- Persegi panjang: 4 sisi, sisi berlawanan sama, 4 sudut siku-siku
- Lingkaran: tidak ada sisi, batas melengkung kontinu
- Pentagon: 5 sisi, jumlah sudut 540°
- Heksagon: 6 sisi, jumlah sudut 720°

## Statistika dan Probabilitas

Statistika adalah ilmu mengumpulkan, menganalisis, menafsirkan, dan menyajikan data.

**Ukuran tendensi sentral:**
- **Mean** (rata-rata): jumlah semua nilai dibagi jumlah nilai
- **Median**: nilai tengah saat data diurutkan (kurang sensitif terhadap outlier)
- **Modus**: nilai yang paling sering muncul (dapat memiliki beberapa modus)

**Ukuran sebaran:**
- **Rentang**: maksimum - minimum
- **Varians**: rata-rata kuadrat deviasi dari mean
- **Deviasi standar**: akar kuadrat dari varians (dalam satuan yang sama dengan data)

Probabilitas mengukur kemungkinan suatu kejadian terjadi, berkisar dari 0 (mustahil) hingga 1 (pasti). Probabilitas dua kejadian independen keduanya terjadi adalah produk dari probabilitas masing-masing.

**Contoh:** Probabilitas mendapatkan angka 6 pada dadu adil: 1/6. Probabilitas mendapatkan dua angka 6 berturut-turut: (1/6) × (1/6) = 1/36.

## Probabilitas untuk Komputing dan ML

**Variabel acak** adalah variabel yang nilainya tergantung pada hasil proses acak. **Distribusi probabilitas** menjelaskan seberapa mungkin setiap hasil.

**Distribusi umum:**
- **Bernoulli**: satu percobaan dengan dua hasil (misalnya lemparan koin)
- **Binomial**: jumlah keberhasilan dalam n percobaan Bernoulli independen
- **Normal (Gaussian)**: kurva lonceng, simetris di sekitar mean (umum dalam fenomena alami)
- **Poisson**: jumlah kejadian dalam interval tetap (misalnya email per jam)

**Nilai harapan** adalah hasil rata-rata jangka panjang dari variabel acak. **Varians** mengukur sebaran di sekitar harapan tersebut.

**Probabilitas bersyarat** menjelaskan probabilitas suatu kejadian mengingat kejadian lain telah terjadi: P(A|B) = P(A ∩ B) / P(B) [jika P(B) > 0].

**Teorema Bayes** memperbarui keyakinan menggunakan bukti: P(A|B) = P(B|A) × P(A) / P(B).

Dalam machine learning, probabilitas mendasari kepercayaan klasifikasi, estimasi ketidakpastian, metode Bayesian, dan banyak fungsi loss (seperti cross-entropy).

## Kalkulus

Kalkulus adalah cabang matematika yang mempelajari perubahan kontinu.

**Kalkulus diferensial** berurusan dengan laju perubahan dan kemiringan kurva, menggunakan **turunan**. Turunan fungsi f(x) mewakili laju perubahan f terhadap x pada suatu titik. Notasi: f'(x) atau df/dx.

**Turunan umum:**
- d/dx [x^n] = n·x^(n−1)
- d/dx [e^x] = e^x
- d/dx [ln(x)] = 1/x
- d/dx [sin(x)] = cos(x)

**Kalkulus integral** berurusan dengan akumulasi kuantitas dan luas di bawah kurva, menggunakan **integral**. Integral mewakili luas di bawah kurva antara dua titik.

**Teorema fundamental kalkulus** menghubungkan diferensiasi dan integrasi: diferensiasi dan integrasi adalah operasi invers.

Kalkulus dikembangkan secara independen oleh Isaac Newton dan Gottfried Wilhelm Leibniz pada abad ke-17.

## Sistem Bilangan

- **Bilangan asli**: 1, 2, 3, 4, ... (bilangan hitung)
- **Bilangan cacah**: 0, 1, 2, 3, ... (bilangan asli ditambah nol)
- **Bilangan bulat**: ..., −2, −1, 0, 1, 2, ... (semua bilangan cacah dan negatifnya)
- **Bilangan rasional**: bilangan yang dapat dinyatakan sebagai p/q di mana p dan q adalah bilangan bulat dan q ≠ 0 (misalnya 1/2, 3/4, −5/3)
- **Bilangan irasional**: tidak dapat dinyatakan sebagai pecahan (misalnya √2, π, e)
- **Bilangan real**: semua bilangan rasional dan irasional (garis bilangan)
- **Bilangan imajiner**: melibatkan akar kuadrat dari bilangan negatif; i = √(−1)
- **Bilangan kompleks**: menggabungkan bagian real dan imajiner (a + bi)

## Logika dan Penalaran

Logika adalah studi tentang penalaran yang valid.

**Penalaran deduktif** menarik kesimpulan khusus dari premis umum. Jika premis benar dan argumen valid, kesimpulan harus benar.
- **Contoh:** Semua manusia fana. Socrates adalah manusia. Karena itu, Socrates fana.

**Penalaran induktif** menarik kesimpulan umum dari observasi khusus. Ini tidak menjamin kesimpulan benar, tetapi membuatnya probable.
- **Contoh:** Setiap angsa yang pernah saya lihat berwarna putih. Karena itu, semua angsa berwarna putih. (Catatan: ini salah; angsa hitam ada!)

**Kesalahan logika umum (kesalahan dalam penalaran):**
- **Ad hominem**: menyerang orang daripada argumen
- **Straw man**: menyalahtampilkan argumen untuk membuatnya lebih mudah diserang
- **Dikotomi palsu**: menyajikan hanya dua opsi padahal ada lebih banyak
- **Penalaran sirkular**: menggunakan kesimpulan sebagai premis
- **Appeal to authority**: mengklaim sesuatu benar karena otoritas mengatakannya
- **Fallacy post hoc**: mengasumsikan bahwa karena A terjadi sebelum B, A menyebabkan B

## Himpunan

**Himpunan** adalah kumpulan objek yang berbeda.
- **Union** (A ∪ B): semua elemen dari kedua himpunan
- **Intersection** (A ∩ B): hanya elemen yang umum bagi keduanya
- **Himpunan kosong** (∅ atau {}): tidak mengandung elemen
- **Subset** (A ⊆ B): semua elemen A juga ada di B
- **Diagram Venn**: secara visual merepresentasikan hubungan antar himpunan

Teori himpunan adalah fondasi matematika dan logika modern.

## Biner dan Basis Bilangan

Komputer merepresentasikan data dalam **biner** (basis 2), hanya menggunakan digit 0 dan 1. Setiap digit biner disebut **bit**. Delapan bit membentuk satu **byte**.

**Desimal** adalah sistem bilangan basis-10 yang biasa digunakan manusia.

**Heksadesimal** adalah basis 16, menggunakan digit 0–9 dan huruf A–F, sering digunakan dalam komputasi untuk merepresentasikan data biner secara ringkas.

**Konversi:**
- Biner 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 8 + 0 + 2 + 1 = 11 (desimal)
- Heks A3 = 10×16¹ + 3×16⁰ = 160 + 3 = 163 (desimal)

Mengonversi antar basis bilangan adalah konsep fundamental dalam ilmu komputer.

## Aljabar Linear untuk Developer dan ML

Aljabar linear mempelajari vektor, matriks, dan transformasi linear.

**Vektor** adalah daftar angka yang terurut (misalnya fitur dalam sampel ML).
- Contoh: [23, 1.8, 175] mewakili usia, tinggi, dan berat seseorang

**Matriks** adalah array 2D angka (misalnya bobot model atau batch dataset).
- Contoh: [[1, 2], [3, 4]] adalah matriks 2×2

**Perkalian matriks** menggabungkan transformasi linear dan merupakan operasi inti dalam grafis, simulasi, dan jaringan saraf.

**Dot product** mengukur kesamaan dan proyeksi antar vektor:
- a·b = Σ(a_i × b_i)
- **Cosine similarity** = (a·b) / (||a|| × ||b||)
- Cosine similarity berkisar dari -1 (berlawanan) hingga 1 (arah sama)

**Eigenvalue dan eigenvector** menjelaskan arah yang diskalakan (tidak diputar) oleh matriks dan digunakan dalam metode seperti PCA (Principal Component Analysis).

**Rank** menunjukkan berapa banyak informasi independen yang dimiliki matriks. Aproksimasi low-rank berguna untuk kompresi dan reduksi dimensi.

Sebagian besar workload ML modern sangat bergantung pada pustaka aljabar linear yang dioptimalkan dan akselerasi perangkat keras.
