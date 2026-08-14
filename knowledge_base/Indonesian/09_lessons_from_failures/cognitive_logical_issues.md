<!--
---
# Metadata
title: "Cognitive Biases and Logical Fallacies"
description: "Reasoning errors and cognitive biases"
category: "Lessons from Failures"
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
reviewed_by: "Lessons from Failures Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [cognitive, logical, issues, lessons-from-failures]
difficulty_level: "advanced"
prerequisites: []
estimated_reading_time: "27 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Bias Kognitif dan Kekeliruan Logis
Dokumen ini menggabungkan bias kognitif, kesalahan logika, dan kesalahan penalaran yang memengaruhi pengambilan keputusan manusia dan keluaran sistem AI.
---

## Bias Kognitif
Bias kognitif adalah pola sistematis penyimpangan dari rasionalitas dalam penilaian dan pengambilan keputusan. Dalam pengembangan perangkat lunak dan sistem AI, hal ini dapat menyebabkan keputusan desain yang buruk, persyaratan yang cacat, dan perilaku model yang bias.
### Bias Konfirmasi
**Apa Artinya:** Kecenderungan untuk mencari, menafsirkan, dan mengingat informasi dengan cara yang menegaskan keyakinan yang sudah ada sebelumnya.
**Contoh Buruk dalam Pembangunan:**```python
# Developer believes their algorithm is O(n log n)
def analyze_complexity(code):
    # Only looks for evidence supporting O(n log n)
    sees_divide_and_conquer = True
    sees_recursion = True
    
    # Ignores contradictory evidence
    nested_loop_present = True  # Actually makes it O(n²)
    redundant_computation = True  # Adds extra factor
    
    return "O(n log n)"  # Wrong conclusion
```

**Dalam Tinjauan Kode:**```markdown
Developer A (senior): "This looks good, nice work!"
Developer B (junior): "This has several potential issues..."

Team accepts Developer A's review without scrutiny but questions Developer B's feedback excessively.
```

**Mitigasi:**
- Secara aktif mencari bukti yang tidak dapat dikonfirmasi
- Gunakan ulasan kode buta
- Mendorong perbedaan pendapat
- Dokumentasikan asumsi secara eksplisit
### Bias Penahan
**Apa Artinya:** Terlalu mengandalkan informasi pertama yang ditemui.
**Contoh Buruk:**```markdown
Project Manager: "This feature should take about 2 days."
Developer: (Anchored to 2 days, even though realistic estimate is 5 days)
"Okay, I'll try to finish in 2 days."

Result: Rushed work, technical debt, missed deadlines anyway.
```

**Mitigasi:**
- Dapatkan beberapa perkiraan independen
- Gunakan poker perencanaan untuk estimasi
- Pertimbangkan rentang, bukan perkiraan titik
- Referensi data historis
### Kekeliruan Biaya Tenggelam
**Apa Artinya:** Melanjutkan usaha karena sumber daya yang telah diinvestasikan sebelumnya (waktu, uang, tenaga), bahkan ketika ditinggalkan akan lebih baik.
**Contoh Buruk:**```markdown
"We've already spent 6 months building this custom framework. 
We can't switch to the industry standard now, even though 
it would save us time in the long run."
```

**Mitigasi:**
- Mengevaluasi keputusan berdasarkan nilai masa depan, bukan investasi masa lalu
- Secara teratur menilai kembali kelayakan proyek
- Ciptakan keamanan psikologis untuk berputar
- Gunakan kriteria objektif untuk melanjutkan/menghentikan keputusan
### Heuristik Ketersediaan
**Apa Artinya:** Melebih-lebihkan pentingnya informasi yang tersedia atau terkini.
**Contoh Buruk:**```markdown
"I just read about a SQL injection attack, so we should 
prioritize SQL injection prevention over XSS, even though 
our security audit shows XSS is our bigger risk."
```

**Mitigasi:**
- Gunakan pengambilan keputusan berdasarkan data
- Konsultasikan model ancaman yang komprehensif
- Lihatlah tarif dasar dan statistik
- Hindari bias keterkinian dalam penentuan prioritas
### Efek Dunning-Kruger
**Apa Artinya:** Orang dengan kemampuan rendah dalam suatu tugas melebih-lebihkan kemampuan mereka; para ahli mungkin meremehkan pendapat mereka.
**Contoh Buruk:**```markdown
Junior Developer: "I've completed a Python tutorial. 
I'm ready to architect our entire microservices platform."

Senior Developer: "I've been building distributed systems for 10 years. 
I'm probably missing something important in this design."
```

**Mitigasi:**
- Mendorong pembelajaran berkelanjutan
- Menerapkan proses tinjauan sejawat
- Membuat program mentoring
- Menumbuhkan kerendahan hati dan rasa ingin tahu
---

## Kekeliruan Logis
Kekeliruan logika adalah kesalahan dalam penalaran yang melemahkan validitas argumen. Model AI dapat menghasilkan keluaran yang mengandung kesalahan-kesalahan ini.
### Ad Hominem (Serangan Terhadap Orangnya)
**Apa Artinya:** Menyerang orang yang membuat argumen, bukan argumen itu sendiri.
**Contoh Buruk:**```markdown
"This code review is wrong because the reviewer is a junior developer."
```

**Mengapa Buruk:** Validitas masukan bergantung pada kontennya, bukan senioritas pengulas.
### Banding ke Otoritas
**Apa Artinya:** Mengklaim sesuatu itu benar karena figur otoritas mengatakan demikian, tanpa bukti.
**Contoh Buruk:**```markdown
"This architecture must be correct because Google uses it."
```

**Mengapa Ini Buruk:** Apa yang berhasil untuk Google pada skalanya mungkin tidak berhasil untuk kasus penggunaan Anda.
### Dikotomi Salah (Pemikiran Hitam-Putih)
**Apa Artinya:** Hanya menyajikan dua opsi jika ada lebih banyak opsi.
**Contoh Buruk:**```markdown
"We either rewrite everything in Rust or accept that our 
codebase will always be slow and buggy."
```

**Kenyataan:** Ada banyak opsi di antara kedua ekstrem ini (mengoptimalkan jalur panas, menggunakan Rust untuk komponen tertentu, menyempurnakan kode Python, dll.)
### Lereng Licin
**Apa Artinya:** Berpendapat bahwa satu peristiwa pasti akan menimbulkan serangkaian konsekuensi negatif.
**Contoh Buruk:**```markdown
"If we allow this small technical debt, soon our entire 
codebase will be unmaintainable and the company will fail."
```

**Mengapa Buruk:** Mengasumsikan kemajuan yang tak terelakkan tanpa bukti; mengabaikan faktor-faktor yang meringankan.
### Penalaran Melingkar
**Apa Artinya:** Menggunakan kesimpulan sebagai premis.
**Contoh Buruk:**```markdown
"Our code is high quality because we write good code."
```

### Post Hoc Ergo Propter Hoc (Penyebab Salah)
**Apa Artinya:** Dengan asumsi bahwa karena B mengikuti A, A menyebabkan B.
**Contoh Buruk:**```markdown
"We deployed the new feature and then saw increased latency. 
The new feature must be causing the latency."
```

**Kenyataan:** Korelasi tidak berarti sebab-akibat. Faktor-faktor lain mungkin menjadi penyebabnya.
### Manusia Jerami
**Apa Artinya:** Menyalahartikan argumen seseorang agar lebih mudah diserang.
**Contoh Buruk:**```markdown
Developer A: "We should add more tests for edge cases."
Developer B: "So you want us to spend all our time writing tests 
and never ship features?"
```

### Kekeliruan ikut-ikutan
**Apa Artinya:** Berdebat tentang suatu hal itu benar karena banyak orang yang mempercayainya.
**Contoh Buruk:**```markdown
"Everyone is using Kubernetes, so we should too."
```

**Mengapa Buruk:** Popularitas tidak menjamin kesesuaian dengan kebutuhan spesifik Anda.
---

## Penalaran Kegagalan dalam AI
### Kesalahan Logika Multi-Langkah
**Contoh Buruk:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Yes, Alice must be a programmer.
```

**Mengapa Ini Buruk:**
- Melakukan kekeliruan dalam menegaskan konsekuensinya
- Alice bisa menulis kode tanpa menjadi seorang programmer
- Struktur logis: (P→Q, Q) ⊬ P
**Penalaran yang Benar:**```
User: If all programmers write code, and Alice writes code, is Alice a programmer?
Assistant: Not necessarily. While all programmers write code, not everyone
who writes code is a programmer. Alice could be a student, hobbyist, or
work in another field that involves coding.
```

### Kegagalan Penalaran Matematis
**Contoh Buruk:**```
User: A bat and ball cost $1.10 together. The bat costs $1 more than the ball.
How much does the ball cost?
Assistant: The ball costs $0.10.
```

**Kenyataan:** Jika harga bola $0,10 dan harga pemukulnya $1 lebih mahal ($1,10), totalnya akan menjadi $1,20. Jawaban yang benar adalah $0,05 untuk bola dan $1,05 untuk pemukul.
### Kesalahan Penalaran Kausal
**Contoh Buruk:**```
User: Ice cream sales and drowning rates both increase in summer. Does ice cream cause drowning?
Assistant: Yes, there appears to be a causal relationship.
```

**Kenyataan:** Keduanya disebabkan oleh faktor ketiga (cuaca panas), bukan satu sama lain.
---

## Strategi Peningkatan
### Untuk Pengambilan Keputusan Manusia
1. **Pelatihan Kesadaran**: Belajar mengenali bias umum
2. **Penggunaan Daftar Periksa**: Gunakan daftar periksa keputusan untuk mengatasi bias
3. **Tim yang Beragam**: Melibatkan orang-orang dengan perspektif berbeda
4. **Pra-mortem**: Bayangkan kegagalan dan bekerja mundur untuk mengidentifikasi penyebabnya
5. **Dokumentasi**: Catat alasannya untuk ditinjau nanti
### Untuk Sistem AI
1. **Anjuran Rantai Pemikiran**: Minta model untuk menunjukkan langkah-langkah penalaran
2. **Koreksi Mandiri**: Minta model meninjau dan mengkritik jawabannya
3. **Verifikasi Formal**: Gunakan alat penalaran simbolis untuk logika kritis
4. **Dekomposisi**: Pecah masalah kompleks menjadi langkah-langkah lebih kecil
5. **Alat Eksternal**: Gunakan kalkulator dan pemecah masalah matematika
6. **Beberapa Sampel**: Hasilkan banyak respons dan bandingkan
---

## Topik Terkait
- **Kegagalan AI/LLM**: Lihat`ai_llm_failures.md`untuk masalah halusinasi dan penalaran
- **Sumber yang Bertentangan**: Lihat dokumentasi tentang evaluasi informasi yang bertentangan
- **Berpikir Kritis**: Terapkan konsep ini untuk mengevaluasi argumen dan bukti
- **Rekayasa Cepat**: Lihat`../02_artificial_intelligence/prompt_engineering.md`untuk mengetahui teknik mengurangi kesalahan penalaran
---

## Bias Kognitif Tambahan dalam Pengembangan Perangkat Lunak
### Bias Status Quo
**Apa Artinya:** Preferensi untuk mempertahankan kondisi saat ini; setiap perubahan dianggap sebagai kerugian.
**Contoh Buruk:**```markdown
Team Lead: "Should we upgrade to Python 3.12? It has performance improvements 
and security fixes."

Developer: "Python 3.8 works fine. Why risk breaking things?"

Reality: Staying on an older version increases technical debt, security risks,
and makes future upgrades harder.
```

**Mitigasi:**
- Hitung biaya jika tidak berubah
- Tetapkan jadwal peningkatan rutin
- Ciptakan lingkungan eksperimen yang aman
- Bingkai perubahan sebagai peluang, bukan ancaman
### Bias Optimisme
**Apa Artinya:** Meremehkan waktu, biaya, dan risiko namun melebih-lebihkan manfaat.
**Contoh Buruk:**```markdown
Project Plan:
- Development: 2 weeks (realistic: 4 weeks)
- Testing: 3 days (realistic: 1 week)
- Bug fixes: 2 days (realistic: 1-2 weeks)
- Contingency: None

Result: Project takes 3x longer than planned.
```

**Mitigasi:**
- Gunakan perkiraan kelas referensi (bandingkan dengan proyek serupa sebelumnya)
- Tambahkan buffer kontingensi (20-50%)
- Melakukan pemeriksaan mayat
- Lacak akurasi estimasi dari waktu ke waktu
### Bias Kelangsungan Hidup
**Apa Artinya:** Berfokus pada contoh sukses dan mengabaikan kegagalan.
**Contoh Buruk:**```markdown
"Look at all these successful startups that didn't do market research!
We don't need market research either."

Reality: Many more startups failed without market research, but they're 
not visible because they didn't survive.
```

**Mitigasi:**
- Pelajari keberhasilan DAN kegagalan
- Cari tarif dasar dan statistik
- Pertimbangkan data yang tidak terlihat
- Hindari contoh-contoh yang memetik ceri
### Kesalahan Atribusi Mendasar
**Apa Artinya:** Mengaitkan perilaku orang lain dengan karakter, bukan keadaan.
**Contoh Buruk:**```markdown
"That developer made a bug because they're careless."

Reality: The bug might be due to unclear requirements, time pressure,
lack of testing infrastructure, or fatigue.
```

**Mitigasi:**
- Pertimbangkan faktor situasional
- Latih empati
- Fokus pada sistem, bukan individu
- Gunakan pemeriksaan mayat yang tidak bersalah
### Bias Melihat ke Belakang
**Apa Artinya:** Setelah suatu peristiwa terjadi, percaya bahwa hal itu dapat diprediksi sejak awal.
**Contoh Buruk:**```markdown
After production outage:
"I knew that deployment was risky. This was totally predictable."

Reality: The outcome wasn't obvious beforehand; hindsight makes it seem clear.
```

**Mitigasi:**
- Dokumentasikan prediksi sebelum hasil
- Tinjau konteks keputusan, bukan hanya hasil
- Hindari budaya "Sudah kubilang".
- Fokus pada perbaikan proses, bukan menyalahkan
---

## Lebih Banyak Kekeliruan Logis
### Menarik Kebaruan
**Apa Artinya:** Dengan asumsi ada sesuatu yang lebih baik karena lebih baru.
**Contoh Buruk:**```markdown
"We should rewrite our entire backend in the latest framework. 
It's the newest, so it must be better."

Reality: Newer doesn't mean better for your specific use case.
Mature technologies often have better support and stability.
```

### Menarik Tradisi
**Apa Artinya:** Berdebat tentang sesuatu itu benar karena selalu dilakukan seperti itu.
**Contoh Buruk:**```markdown
"We've always deployed on Fridays at 5 PM. We shouldn't change that."

Reality: Just because something is traditional doesn't make it optimal.
(Actually, deploying on Friday at 5 PM is generally considered bad practice!)
```

### Tu Quoque (Menarik Kemunafikan)
**Apa Artinya:** Menolak kritik dengan menunjukkan ketidakkonsistenan sang kritikus.
**Contoh Buruk:**```markdown
Senior Dev: "You should write tests for this code."
Junior Dev: "But you don't write tests for your code either!"

Reality: The validity of the advice is independent of who gives it.
```

### Pertanyaan Termuat
**Apa Artinya:** Mengajukan pertanyaan yang mengandung asumsi.
**Contoh Buruk:**```markdown
"Why did you write such terrible code for this module?"

Reality: The question assumes the code is terrible, putting the respondent
on the defensive regardless of actual code quality.
```

### Bukan Orang Skotlandia Sejati
**Apa Artinya:** Membuat pengecualian terhadap klaim universal saat ditentang.
**Contoh Buruk:**```markdown
Person A: "No professional developer writes code without tests."
Person B: "But John is a professional developer and doesn't write tests."
Person A: "Well, no TRUE professional developer writes code without tests."

Reality: This redefines the category to exclude counterexamples rather 
than revising the claim.
```

### Kekeliruan Genetik
**Apa Artinya:** Menilai sesuatu berdasarkan asal usulnya, bukan berdasarkan manfaatnya saat ini.
**Contoh Buruk:**```markdown
"That library came from a small startup, so it can't be enterprise-grade."

Reality: The origin doesn't determine current quality. Evaluate based on
actual characteristics, not source.
```

### Kekeliruan Jalan Tengah
**Apa Artinya:** Dengan asumsi kebenaran selalu berada di tengah-tengah dua ekstrem.
**Contoh Buruk:**```markdown
Developer A: "We should add comprehensive error handling."
Developer B: "Error handling isn't important, skip it."
Compromise: "Let's add some error handling, but not too much."

Reality: One position might be clearly correct. Compromise isn't always wise.
```

---

## Bias Kognitif dalam Sistem AI
### Pelatihan Bias Data
Model AI mewarisi bias yang ada dalam data pelatihannya.
**Contoh:**```markdown
Training data contains: "The doctor said..." (mostly male pronouns)
                       "The nurse said..." (mostly female pronouns)

Model learns: Doctors are typically male, nurses are typically female.

Result: Model exhibits gender bias in profession associations.
```

**Mitigasi:**
- Audit data pelatihan untuk mengetahui adanya bias
- Gunakan teknik debiasing
- Uji keluaran yang bias
- Pengumpulan data yang beragam
### Bias Otomatisasi
**Apa Artinya:** Terlalu mengandalkan sistem otomatis, meskipun sistem tersebut salah.
**Contoh:**```markdown
AI suggests code with a subtle bug.
Developer accepts it without review because "the AI is usually right."

Result: Bug makes it to production.
```

**Mitigasi:**
- Pertahankan pengawasan manusia
- Mendorong evaluasi kritis terhadap keluaran AI
- Jangan perlakukan AI sebagai hal yang sempurna
- Menerapkan proses peninjauan
### Ilusi Pemahaman
**Apa Artinya:** Percaya bahwa Anda memahami cara kerja AI, padahal Anda tidak.
**Contoh:**```markdown
User: "The AI understands what I mean, it's like talking to a person."

Reality: LLMs predict tokens based on patterns, they don't truly 
"understand" in the human sense. This illusion leads to over-trust.
```

**Mitigasi:**
- Mendidik pengguna tentang batasan AI
- Bersikaplah transparan tentang cara kerja sistem
- Hindari antropomorfisasi AI
- Tetapkan ekspektasi yang sesuai
---

## Studi Kasus
### Studi Kasus 1: Bias Konfirmasi dalam Pemilihan Arsitektur
**Insiden:** Sebuah tim memilih arsitektur layanan mikro untuk aplikasi kecil.
**Akar Penyebab:** Pemimpin tim telah membaca beberapa artikel yang memuji layanan mikro dan 
hanya mencari informasi yang mengkonfirmasi pilihan ini, mengabaikan peringatan tentang kompleksitas.
**Dampak:**
- Overhead besar-besaran untuk tim yang terdiri dari 3 pengembang
- Kompleksitas penerapan meningkat 10x
- Kinerja menurun karena panggilan jaringan
- Proyek tertunda 6 bulan
**Pelajaran:** Evaluasi arsitektur berdasarkan konteks spesifik Anda, bukan sekadar 
testimoni positif. Pertimbangkan trade-off secara eksplisit.
### Studi Kasus 2: Sunk Cost dalam Sistem Lama
**Insiden:** Perusahaan terus mempertahankan CRM yang dibuat khusus selama 5 tahun 
meskipun ada alternatif yang lebih baik.
**Akar Penyebab:** "Kami telah menginvestasikan $2 juta, kami tidak dapat mengabaikannya sekarang."
**Dampak:**
- Biaya pemeliharaan tahunan: $500K
- Biaya peluang: Tidak dapat menggunakan fitur modern
- Masalah retensi talenta (pengembang ingin bekerja dengan teknologi modern)
- Total biaya 5 tahun: $4,5 juta vs. $1,5 juta untuk alternatif SaaS
**Pelajaran:** Investasi masa lalu tenggelam. Buat keputusan berdasarkan nilai masa depan.
### Studi Kasus 3: Heuristik Ketersediaan dalam Keamanan
**Insiden:** Tim memprioritaskan pertahanan dari serangan yang baru-baru ini dipublikasikan 
vektor sambil mengabaikan ancaman yang lebih mungkin terjadi.
**Akar Penyebab:** Liputan berita terkini membuat satu jenis ancaman menjadi sangat umum 
dalam memori, penilaian risiko yang menyimpang.
**Dampak:**
- Menghabiskan $100K untuk memitigasi ancaman dengan probabilitas rendah
- Pelanggaran aktual terjadi melalui vektor yang terabaikan
- Biaya pemulihan: $500K+
**Pelajaran:** Gunakan pemodelan ancaman berdasarkan data, bukan penentuan prioritas berdasarkan kekinian.
---

## Latihan Praktis
### Latihan Deteksi Bias
Tinjau keputusan terkini dan tanyakan:
1. Asumsi apa yang kita buat?
2. Bukti apa yang bertentangan dengan kesimpulan kita?
3. Apakah kita mempertimbangkan beberapa pilihan atau berpegang pada gagasan pertama?
4. Apakah kita meneruskannya karena nilai masa depan atau investasi masa lalu?
5. Apa yang akan kami rekomendasikan jika orang lain bertanya kepada kami?
### Menemukan Kekeliruan Logis
Berlatihlah mengidentifikasi kekeliruan dalam diskusi sehari-hari:
```markdown
Statement: "If we don't adopt AI now, we'll be left behind forever."

Analysis: This is a slippery slope fallacy. It assumes inevitable 
progression to being "left behind" without evidence. Also presents 
a false dichotomy (adopt AI or be left behind).
```

### Teknik Pra-Mortem
Sebelum memulai proyek:
1. Bayangkan 6 bulan ke depan
2. Proyek ini gagal total
3. Tuliskan cerita mengapa gagal
4. Bekerja mundur untuk mencegah mode kegagalan tersebut
Hal ini melawan bias optimisme dan heuristik ketersediaan.
---

## Alat dan Kerangka
### Templat Jurnal Keputusan
```markdown
Date: [When]
Decision: [What we decided]
Context: [Situation and constraints]
Options Considered: [Alternatives evaluated]
Expected Outcome: [What we think will happen]
Confidence Level: [How sure we are]
Review Date: [When to revisit]

[Later] Actual Outcome: [What actually happened]
Lessons Learned: [What we'd do differently]
```

### Daftar Periksa Bias
Sebelum mengambil keputusan penting:
- [ ] Sudahkah kita mencari bukti yang tidak dapat dikonfirmasi?
- [ ] Apakah kita berlabuh pada informasi awal?
- [ ] Apakah sunk cost mempengaruhi kita?
- [ ] Apakah kita terlalu percaya diri dengan perkiraan kita?
- [ ] Sudahkah kita mempertimbangkan tarif dasar?
- [ ] Apakah kita terjebak dalam bias ketersediaan/kekinian?
- [ ] Akankah kita membuat pilihan yang sama jika memulai dari awal?
### Latihan Tim Merah
Menugaskan seseorang untuk menentang keputusan yang diusulkan:
- Peran mereka adalah menemukan kekurangan
- Mereka harus menyajikan sudut pandang alternatif
- Latihan tim menanggapi kritik secara konstruktif
- Dokumentasikan kekhawatiran yang diangkat dan ditangani
Hal ini melawan bias konfirmasi dan pemikiran kelompok.