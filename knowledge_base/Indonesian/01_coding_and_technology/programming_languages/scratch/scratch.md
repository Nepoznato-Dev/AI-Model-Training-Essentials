---
# Metadata
title: "Scratch"
description: "Comprehensive reference for the Scratch programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
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
tags: [scratch, programming-language, syntax, ecosystem, coding-and-technology]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "29 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# Menggores
Scratch adalah bahasa pemrograman visual berbasis blok yang dikembangkan oleh MIT Media Lab dan pertama kali dirilis pada tahun 2007. Alih-alih menulis kode berbasis teks, pengguna menyatukan blok berwarna untuk membuat program. Scratch dirancang khusus untuk anak-anak usia 8-16 tahun (meskipun pelajar dari segala usia menggunakannya) untuk mengajarkan konsep dasar pemrograman — loop, kondisional, variabel, peristiwa, dan fungsi — tanpa hambatan kesalahan sintaksis.
Scratch adalah bahasa pemrograman pengantar yang paling banyak digunakan di dunia, dengan lebih dari 100 juta pengguna terdaftar dan tersedia dalam 70+ bahasa. Ini berjalan di browser web dan gratis.
---

## Mengapa Goresan Penting
- **Pengantar pemrograman terbaik**: Menghilangkan hambatan sintaksis sepenuhnya. Konsep diajarkan melalui manipulasi visual.
- **Pemikiran komputasional**: Mengajarkan dekomposisi, pengenalan pola, abstraksi, dan desain algoritma.
- **Didorong oleh kreativitas**: Anak-anak membuat game, animasi, cerita, dan musik — mempelajari pemrograman sebagai produk sampingan dari membuat hal-hal yang mereka minati.
- **Jangkauan global**: Digunakan di sekolah-sekolah di seluruh dunia. Tersedia dalam 70+ bahasa. Gratis dan berbasis browser.
- **Komunitas**: Komunitas online Scratch mengajarkan berbagi, remix, dan pembelajaran kolaboratif.
## Pengorbanan
| Batasan | Detail | Solusi Khas |
|-----------|---------|-------------------|
| **Bukan bahasa pemrograman "nyata"** | Tidak dapat membuat perangkat lunak produksi, API, atau sistem | Transisi ke Python, JavaScript, atau bahasa berbasis teks |
| **Kemampuan terbatas** | Tidak ada file I/O, jaringan, atau struktur data lanjutan | Gunakan untuk belajar; pindah ke bahasa teks untuk proyek nyata |
| **Kinerja** | Ditafsirkan, lambat untuk proyek yang kompleks | Tidak dirancang untuk pekerjaan yang kinerjanya kritis |
| **Persepsi usia** | Sering dianggap "hanya untuk anak-anak" | Scratch adalah alat pembelajaran, bukan bahasa profesional |
---

## Cara Kerja Goresan
Program awal (disebut "proyek") terdiri dari **sprite** (karakter/objek) yang merespons **blok** yang disatukan dalam skrip.
### Konsep Inti (Diajarkan Melalui Blok)
| Konsep | Kategori Blok Gores | Contoh |
|---------|----------------------|---------|
| **Urutan** | Gerak, Tampak | "Bergerak 10 langkah" lalu "Say Hello" |
| **Loop** | Kontrol (kuning) | "Ulangi 10", "Selamanya", "Ulangi sampai" |
| **Kondisi** | Kontrol (kuning) | "Jika... maka", "Jika... maka... lain" |
| **Variabel** | Variabel (oranye) | "Tetapkan skor menjadi 0", "Ubah skor menjadi 1" |
| **Acara** | Acara (kuning) | "Saat bendera hijau diklik", "Saat tombol ditekan" |
| **Fungsi** | Blok Saya (khusus) | Tentukan urutan blok yang dapat digunakan kembali |
| **Daftar (array)** | Variabel (oranye) | "Tambahkan ke daftar", "Item daftar" |
| **Penyiaran** | Acara | Kirim pesan antar sprite |
### Contoh: Logika Permainan Sederhana
```
When green flag clicked:
  Set [score] to 0
  Forever:
    If <touching [enemy]?> then:
      Change [score] by -1
      Play sound [ouch]
    If <touching [coin]?> then:
      Change [score] by 1
      Go to random position
```

---

## Sintaks & Pola Tingkat Lanjut
### Blokir Kategori secara Detail
Scratch 3.0 mengatur blok ke dalam kategori kode warna:
| Kategori | Warna | Jenis Blok |
|----------|--------|-------------|
| **Gerakan** | Biru | bergerak, memutar, pergi, meluncur, mengarahkan, mengubah x/y |
| **Tampak** | Ungu | ucapkan, pikirkan, ganti kostum, ubah ukuran, tampilkan/sembunyikan |
| **Suara** | Merah Muda | memutar suara, menghentikan suara, mengubah volume, mengubah nada |
| **Acara** | Kuning | ketika bendera diklik, ketika tombol ditekan, ketika sprite diklik, siaran |
| **Kontrol** | Emas | tunggu, ulangi, selamanya, jika, jika-lain, ulangi sampai, berhenti |
| **Penginderaan** | Biru Muda | menyentuh, menekan tombol, mouse, jarak, bertanya/menjawab, pengatur waktu |
| **Operator** | Hijau | operasi matematika, operasi teks, perbandingan, dan/atau/tidak, acak |
| **Variabel** | Oranye | atur/ubah variabel, operasi daftar |
| **Blok Saya** | Merah Tua | definisi blok khusus (fungsi) |
### Pola Blok Tingkat Lanjut
```
// Pattern: Timer-based movement (smooth animation)
When green flag clicked:
  Set [speed] to 5
  Forever:
    Change x by (speed)
    If <(x position) > 200> then
      Set [speed] to ((speed) * -1)
    If <(x position) < -200> then
      Set [speed] to ((speed) * -1)

// Pattern: State machine using variables
When green flag clicked:
  Set [game_state] to [menu]
  Forever:
    If <(game_state) = [menu]> then
      Show
      Go to x: 0 y: 0
    If <(game_state) = [playing]> then
      Hide
    If <(game_state) = [game_over]> then
      Say [Game Over!] for 2 secs

// Pattern: Object-oriented sprite (each sprite manages its own state)
When green flag clicked:
  Set [hp] to 100
  Set [max_hp] to 100
  Set [is_alive] to true
  Forever:
    If <(is_alive) = true> then
      If <touching [enemy]?> then
        Change [hp] by -10
        If <(hp) < 1> then
          Set [is_alive] to false
          Broadcast [player_dead]
```

### Blok Khusus (Fungsi)
```
// Define a custom block with parameters
Define: Jump (height) times (count)
  Repeat (count):
    Change y by (height)
    Wait 0.2 seconds
    Change y by ((height) * -1)
    Wait 0.2 seconds

// Usage:
When space key pressed:
  Jump height: 50 times: 3

// Custom block with "run without screen refresh" (optimization)
Define: Draw fractal (depth) (size)
  Run without screen refresh: true
  If <(depth) = 0> then
    Move (size) steps
  Else:
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn right 60 degrees
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn left 120 degrees
    Draw fractal depth: ((depth) - 1) size: ((size) / 2)
    Turn right 60 degrees
```

### Daftar Operasi (Array)
```
// Creating and using lists
When green flag clicked:
  Delete all of [scores]
  Add [100] to [scores]
  Add [85] to [scores]
  Add [92] to [scores]
  Add [78] to [scores]
  
  // Access items (1-indexed)
  Set [total] to 0
  Set [i] to 1
  Repeat (length of [scores]):
    Change [total] by (item (i) of [scores])
    Change [i] by 1
  
  Set [average] to ((total) / (length of [scores]))
  Say (join [Average: ] (average)) for 2 secs

// Sorting a list (bubble sort)
Define: Sort List
  Set [n] to (length of [scores])
  Repeat (n)
    Set [i] to 1
    Repeat ((n) - 1)
      If <(item (i) of [scores]) > (item ((i) + 1) of [scores])> then
        // Swap
        Set [temp] to (item (i) of [scores])
        Replace item (i) of [scores] with (item ((i) + 1) of [scores])
        Replace item ((i) + 1) of [scores] with (temp)
      Change [i] by 1
```

### Penyiaran (Komunikasi Antar Sprite)
```
// Sprite 1 (Player):
When space key pressed:
  Broadcast [fire_bullet]

// Sprite 2 (Bullet):
When I receive [fire_bullet]:
  Go to [Player]
  Show
  Repeat 50:
    Change y by 10
  Hide

// Sprite 3 (Enemy):
When I receive [fire_bullet]:
  If <touching [Bullet]?> then
    Change [hp] by -25
    If <(hp) < 1> then
      Broadcast [enemy_destroyed]
      Hide
```

---

## Arsitektur & Desain Sistem
### Desain Berbasis Peristiwa
Scratch menggunakan arsitektur berbasis peristiwa. Setiap skrip dimulai dengan blok peristiwa (blok topi) dan dijalankan sebagai respons terhadap peristiwa tersebut.
```
Event Types:
+-------------------------------------------+
| when [green flag] clicked    (startup)     |
| when [space] key pressed     (keyboard)    |
| when this sprite clicked     (mouse)       |
| when [backdrop] switches to  (stage event) |
| when [loudness] > [10]       (sound)       |
| when I receive [message]     (broadcast)   |
| when video motion > [10]     (camera)      |
+-------------------------------------------+
```

### Struktur Proyek
```
scratch-project/
├── project.sb3              * Saved project file (ZIP format)
├── sprites/
│   ├── Player/              * Player sprite
│   │   ├── costumes/        * Costume images
│   │   └── sounds/          * Sound files
│   ├── Enemy/
│   │   ├── costumes/
│   │   └── sounds/
│   └── Bullet/
├── stage/
│   ├── backdrops/           * Background images
│   └── sounds/              * Stage sounds
└── README.md
```

### Sistem Klon (Pembuatan Objek)
```
// Creating clones (like creating object instances)
When green flag clicked:
  Forever:
    Wait 1 seconds
    Create clone of [Enemy]

When I start as a clone:
  Go to random position
  Show
  Set [hp] to 3
  Forever:
    Change y by -3
    If <(y position) < -170> then
      Delete this clone
    If <touching [Bullet]?> then
      Change [hp] by -1
      If <(hp) < 1> then
        Change [score] by 10
        Delete this clone
```

---

## Konfigurasi Proyek & Sistem Pembangunan
### Ekstensi Goresan
Scratch mendukung ekstensi resmi dan komunitas yang menambah kemampuan:
| Ekstensi | Tujuan |
|-----------|---------|
| **Pena** | Menggambar garis dan bentuk di atas panggung |
| **Penginderaan Video** | Gunakan webcam untuk mendeteksi gerakan |
| **Teks ​​ke Ucapan** | Ubah teks menjadi audio lisan |
| **Terjemahkan** | Terjemahkan teks antar bahasa |
| **Makey Makey** | Hubungkan objek fisik sebagai masukan |
| **mikro:bit** | Hubungkan perangkat keras mikro:bit BBC |
| **Badai Pikiran LEGO** | Kontrol robot LEGO |
| **Musik** | Mainkan notasi dan instrumen musik |
### Format File Gores
```
Scratch 3.0 projects (.sb3) are ZIP archives containing:
├── project.json             * All scripts, sprites, and metadata
├── [md5hash].svg           * Costume images (SVG or PNG)
├── [md5hash].png           * Additional costumes
└── [md5hash].wav           * Sound files

The project.json contains:
{
  "targets": [
    {
      "isStage": true,
      "name": "Stage",
      "costumes": [...],
      "sounds": [...],
      "blocks": {...}
    },
    {
      "isStage": false,
      "name": "Sprite1",
      "position": {"x": 0, "y": 0},
      "blocks": {...}
    }
  ],
  "monitors": [...],
  "meta": {"semver": "3.0.0"}
}
```

### Penyunting Luring
```
Scratch Desktop (offline editor) available for:
- Windows 10+ (Microsoft Store or direct download)
- macOS 10.13+
- ChromeOS

Installation:
1. Download from https://scratch.mit.edu/download
2. Install and run — no internet required
3. Projects save as .sb3 files locally
```

---

## Pengujian & Debugging
### Alat Debugging Bawaan
Scratch menyediakan beberapa alat bawaan untuk men-debug proyek:
| Alat | Cara Menggunakan |
|------|-----------|
| **Mode penyu** | Klik kanan sprite dan pilih "show debug" untuk melihat koordinat |
| **Monitor variabel** | Klik kanan variabel dan pilih "tampilkan" untuk melihat nilainya secara real-time |
| **Daftar monitor** | Melihat isi daftar dalam tampilan normal, baris, atau kolom |
| **Mode Turbo** | Tahan Shift sambil klik bendera hijau untuk eksekusi lebih cepat |
| **Mode satu langkah** | Klik kanan bendera hijau untuk "satu langkah" (memperlambat eksekusi) |
### Pola Debugging
```
// Debug: Display variable values on sprite
When green flag clicked:
  Forever:
    Say (join [Score: ] (score))

// Debug: Visual boundary checking
When green flag clicked:
  Forever:
    If <(x position) > 240> then
      Say [TOO FAR RIGHT!] for 0.5 secs
      Set x to 240
    If <(x position) < -240> then
      Say [TOO FAR LEFT!] for 0.5 secs
      Set x to -240

// Debug: Frame counter
When green flag clicked:
  Set [frames] to 0
  Forever:
    Change [frames] by 1
    If <(frames) mod 30 = 0> then
      Say (join [FPS: ] ((frames) / (timer))) for 0.1 secs
```

### Masalah Umum
| Masalah | Penyebab | Solusi |
|---------|-------|----------|
| Sprite tidak merespons | Tidak ada blok topi acara | Tambahkan "Saat bendera hijau diklik" atau acara lainnya |
| Klon tidak berfungsi | Klon dibuat tetapi tidak ditampilkan | Tambahkan blok "Tampilkan" setelah "Ketika saya memulai sebagai klon" |
| Variabel dibagikan antar sprite | Kebingungan variabel global vs lokal | Gunakan opsi "Hanya untuk sprite ini" |
| Siaran tidak diterima | Nama pesan salah | Verifikasi siaran dan terima nama yang sama persis |
| Pembekuan loop tak terbatas | "Selamanya" tanpa menunggu | Tambahkan blok kecil "Tunggu" dalam loop ketat |
---

## Interoperabilitas
### Ekstensi Perangkat Keras
Scratch dapat terhubung ke perangkat keras fisik melalui ekstensi:
```
Supported Hardware:
├── micro:bit
│   ├── Accelerometer/gyroscope input
│   ├── LED matrix display output
│   ├── Button input
│   └── Radio communication
├── LEGO Education
│   ├── SPIKE Prime / Essential
│   ├── EV3 (older)
│   └── Motors and sensors
├── Makey Makey
│   ├── Capacitive touch input
│   ├── Any conductive object as button
│   └── USB connection (no drivers needed)
├── Arduino (via extensions)
│   ├── GPIO pin control
│   ├── Sensor readings
│   └── Motor control
└── Camera / Webcam
    ├── Video sensing (motion detection)
    └── Face detection (via extensions)
```

### Scratch Extensions API (Ekstensi Khusus)
```javascript
// Custom Scratch extension (JavaScript)
class MyExtension {
  getInfo() {
    return {
      id: 'myExtension',
      name: 'My Extension',
      blocks: [
        {
          opcode: 'greet',
          blockType: Scratch.BlockType.REPORTER,
          text: 'greet [NAME]',
          arguments: {
            NAME: { type: Scratch.ArgumentType.STRING, defaultValue: 'World' }
          }
        },
        {
          opcode: 'addNumbers',
          blockType: Scratch.BlockType.REPORTER,
          text: '[A] + [B]',
          arguments: {
            A: { type: Scratch.ArgumentType.NUMBER, defaultValue: 1 },
            B: { type: Scratch.ArgumentType.NUMBER, defaultValue: 2 }
          }
        }
      ]
    };
  }
  greet(args) { return 'Hello, ' + args.NAME + '!'; }
  addNumbers(args) { return Number(args.A) + Number(args.B); }
}
Scratch.extensions.register(new MyExtension());
```
---

## Pola Desain
### Pola 1: Gerakan Platformer
```
When green flag clicked:
  Set [gravity] to -1
  Set [velocity_y] to 0
  Set [speed] to 5
  Set [is_jumping] to false
  Forever:
    // Horizontal movement
    If <key [right arrow] pressed?> then
      Change x by (speed)
    If <key [left arrow] pressed?> then
      Change x by ((speed) * -1)
    // Jumping
    If <key [space] pressed?> then
      If <(is_jumping) = false> then
        Set [velocity_y] to 12
        Set [is_jumping] to true
    // Gravity
    Change [velocity_y] by (gravity)
    Change y by (velocity_y)
    // Ground collision
    If <(y position) < -100> then
      Set y to -100
      Set [velocity_y] to 0
      Set [is_jumping] to false
```

### Pola 2: Latar Belakang Bergulir
```
// Background sprite scrolls left to create side-scrolling effect
When green flag clicked:
  Forever:
    Change x by -5
    If <(x position) < -240> then
      Set x to 240

// Or use two copies for seamless scrolling
When I start as a clone:
  Forever:
    Change x by -5
    If <(x position) < -480> then
      Change x by 960
```

### Pola 3: Mengikuti Sprite (Mengejar AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### Pola 4: Sistem Inventaris dengan Daftar
```
When green flag clicked:
  Delete all of [inventory]
  Add [Sword] to [inventory]
  Add [Shield] to [inventory]
  Add [Potion] to [inventory]

When key [i] pressed:
  // Display inventory
  Set [display] to []
  Set [idx] to 1
  Repeat (length of [inventory]):
    Set [display] to (join (display) (join (item (idx) of [inventory]) [
]))
    Change [idx] by 1
  Say (display) for 3 secs

When key [1] pressed:
  // Use first item
  If <(length of [inventory]) > 0> then
    Set [used_item] to (item 1 of [inventory])
    Delete 1 of [inventory]
    Say (join [Used: ] (used_item)) for 1 secs
```

### Pola 5: Sistem Partikel dengan Klon
```
// Create particles on click
When this sprite clicked:
  Repeat 10:
    Create clone of [Particle]

// Each particle moves randomly and fades
When I start as a clone:
  Go to [mouse-pointer]
  Point in direction (pick random 0 to 360)
  Set [size] to (pick random 20 to 50)
  Set [ghost] to 0
  Show
  Repeat 20:
    Move 5 steps
    Change [ghost] by 5
  Hide
  Delete this clone
```

---

## Kinerja & Optimasi
### Optimasi Sprite
| Teknik | Dampak | Deskripsi |
|-----------|--------|-------------|
| **Minimalkan klon** | Tinggi | Setiap klon menghabiskan memori; hapus setelah selesai |
| **Kurangi kostum** | Sedang | Lebih sedikit kostum switch berarti lebih sedikit rendering overhead |
| **Gunakan "jalankan tanpa penyegaran layar"** | Tinggi | Blok khusus tanpa penyegaran layar berjalan lebih cepat |
| **Batasi blok "ucapkan"** | Sedang | Gelembung ucapan menyebabkan overhead rendering |
| **Hindari "selamanya" di setiap sprite** | Sedang | Gunakan siaran dan acara alih-alih polling terus-menerus |
### Manajemen Klon
```
// BAD: Creating clones without cleanup
When green flag clicked:
  Forever:
    Create clone of [Enemy]
    Wait 0.1 secs
    // Clones pile up and slow everything down

// GOOD: Limit active clones
When green flag clicked:
  Set [max_enemies] to 10
  Forever:
    If <(enemy_count) < (max_enemies)> then
      Create clone of [Enemy]
      Change [enemy_count] by 1
    Wait 1 secs

When I start as a clone:
  // ... enemy behaviour ...
  // When done:
  Change [enemy_count] by -1
  Delete this clone
```

### Daftar Periksa Pengoptimalan
| Teknik | Dampak | Deskripsi |
|-----------|--------|-------------|
| **Jalankan tanpa penyegaran layar** | Sangat Tinggi | Blok khusus melewatkan rendering demi kecepatan |
| **Minimalkan klon aktif** | Tinggi | Hapus klon segera setelah tidak diperlukan lagi |
| **Gunakan siaran dengan hemat** | Sedang | Terlalu banyak siaran per frame menyebabkan lag |
| **Sederhanakan kostum** | Sedang | Gambar yang lebih kecil ditampilkan lebih cepat |
| **Kurangi operasi daftar** | Sedang | Hindari memindai daftar besar setiap frame |
| **Gunakan blok "tunggu"** | Rendah | Cegah CPU memonopoli loop selamanya |
---

## Penerapan & Penggunaan di Dunia Nyata
### Berbagi Proyek
```
Deployment Options:
├── Scratch Community (online)
│   ├── Upload to scratch.mit.edu
│   ├── Share with community
│   └── Allow remixing by others
├── Local sharing
│   ├── Save as .sb3 file
│   ├── Share via email/USB/cloud
│   └── Open in Scratch Desktop or web editor
├── Embedding
│   ├── Embed on websites via iframe
│   └── <iframe src="https://scratch.mit.edu/projects/embed/PROJECT_ID">
└── Standalone apps (via third-party tools)
    ├── TurboWarp (desktop packaging)
    ├── Electron-based wrappers
    └── HTML5 export tools
```

### Penggunaan Pendidikan di Dunia Nyata
| Konteks | Bagaimana Goresan Digunakan | Skala |
|---------|-------------------|-------|
| **Sekolah K-12** | Pengantar pemrograman di kelas CS | Digunakan di 190+ negara |
| **Klub coding** | Lokakarya Scratch Club / CoderDojo | 3000+ klub di seluruh dunia |
| **Perpustakaan** | Program pemrograman sepulang sekolah | Sistem perpustakaan umum |
| **Sekolah di Rumah** | Pendidikan pemrograman mandiri | Jutaan pembelajar ke rumah |
| **Universitas CS0** | Kursus pengantar CS non-utama | Program jembatan universitas |
| **Aksesibilitas** | Mengajar pemrograman untuk tunanetra | Dukungan pembaca layar |
| **Terapi** | Pengembangan keterampilan kognitif dan motorik | Terapi okupasi |
### Goresan dalam Penelitian Pendidikan
Penelitian telah menunjukkan bahwa Scratch secara efektif mengajarkan:
- **Pemikiran berurutan**: Memecah masalah menjadi langkah-langkah yang teratur
- **Keterampilan debugging**: Menemukan dan memperbaiki kesalahan dalam logika
- **Ekspresi kreatif**: Menggabungkan seni, musik, dan pemrograman
- **Kolaborasi**: Mencampur dan mengembangkan proyek orang lain
- **Persistence**: Mengulang proyek untuk memperbaikinya
---

## Transisi Dari Awal
Setelah mempelajari Scratch, langkah-langkah umum selanjutnya meliputi:
| Bahasa Berikutnya | Mengapa |
|--------------|-----|
| **Piton** | Transisi paling alami — sintaksis yang mudah dibaca, konsep logika serupa |
| **JavaScript** | Jika tertarik dengan web/game — umpan balik visual langsung |
| **Lua (melalui Roblox/Love2D)** | Jika tertarik dengan pengembangan game |
| **Penemu Aplikasi** | Blok visual untuk aplikasi Android (silsilah MIT yang sama) |
| **Terhambat** | Pustaka pemrograman visual Google (konsep serupa) |
### Pemetaan Konsep: Gores ke Python
| Konsep Awal | Setara dengan Python |
|----------------|-------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| Panggilan fungsi atau sistem acara |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(diindeks 0!) |
| `length of [list]`| `len(list)`|
---

## Kapan Menggunakan Scratch
| Skenario | Mengapa Menggaruk | Alternatif Lebih Baik |
|----------|-----------|-------------------|
| Mengajari anak (8-16) coding | Dirancang khusus untuk ini | — |
| Memperkenalkan pemikiran komputasi | Visual, tidak ada kesalahan sintaksis | — |
| Lokakarya sekolah / klub coding | Gratis, berbasis browser, tanpa pengaturan | — |
| Membuat prototipe ide permainan secara visual | Iterasi cepat | — |
| Pengembangan profesional | Tidak dirancang untuk ini | Python, JavaScript, bahasa teks apa pun |
| Pendidikan ilmu komputer tingkat universitas | Terlalu sederhana | Python, Jawa, C |
---

## Tanya Jawab Sintetis
**Q1: Apakah Scratch benar-benar sebuah bahasa pemrograman?**
A1: Ya, Scratch adalah bahasa pemrograman sebenarnya, tetapi lebih bersifat visual dan bukan berbasis teks. Ini mendukung semua konsep dasar pemrograman: variabel, loop, kondisional, fungsi (blok khusus), daftar, dan pemrograman berbasis peristiwa. Perbedaannya adalah Anda menarik dan melepas blok alih-alih mengetikkan kode. Hal ini menghilangkan kesalahan sintaksis dan membuat pemrograman dapat diakses oleh pelajar muda.
**Q2: Bagaimana cara membuat fungsi khusus (blok khusus) di Scratch?**
A2: Buka kategori "Blok Saya" dan klik "Buat Blokir". Beri nama, tambahkan parameter jika diperlukan, lalu tentukan perilakunya dengan menambahkan blok di bawahnya. Blok khusus dapat menerima masukan (angka, string, boolean) dan dapat memanggil blok khusus lainnya. Hal ini memungkinkan pemrograman modular dan penggunaan kembali kode.
**Q3: Apa cara terbaik untuk menangani logika permainan yang kompleks di Scratch?**
A3: Gunakan blok khusus untuk mengatur logika, menyiarkan pesan untuk koordinasi acara antar sprite, dan menggunakan daftar untuk menyimpan status permainan (skor, level, inventaris). Untuk AI yang kompleks, gunakan mesin keadaan terbatas dengan variabel yang melacak keadaan saat ini. Kloning sprite untuk banyak musuh dan gunakan "saat saya mulai sebagai klon" untuk memberikan setiap perilaku independen.
**Q4: Bagaimana cara berbagi data antar sprite di Scratch?**
A4: Gunakan variabel global (dibuat tanpa "hanya untuk sprite ini") untuk data bersama seperti skor atau status permainan. Gunakan pesan siaran untuk memicu peristiwa di seluruh sprite. Untuk komunikasi yang lebih kompleks, gunakan daftar sebagai struktur data bersama. Setiap sprite dapat membaca dan memodifikasi variabel dan daftar global, sehingga memungkinkan koordinasi.
**Q5: Apa saja teknik lanjutan di Scratch?**
A5: Gunakan blok pena untuk menggambar dan membuat efek visual. Menerapkan raycasting untuk grafik seperti 3D. Gunakan variabel cloud untuk game multipemain (memerlukan status Scratcher). Buat pembuatan prosedural dengan nomor dan daftar acak. Gunakan blok khusus dengan parameter untuk algoritma yang dapat digunakan kembali. Bereksperimenlah dengan penginderaan video dan manipulasi suara untuk proyek interaktif.
---

## Rantai Pemikiran
### Masalah 1: Membuat Game Platformer
**Langkah 1: Pahami Masalahnya**
Kita perlu membuat platformer dimana karakter dapat bergerak ke kiri/kanan, melompat, menghindari rintangan, dan mengumpulkan item.
**Langkah 2: Identifikasi Pendekatannya**
- Gunakan simulasi gravitasi dengan variabel "jatuh".
- Mendeteksi tanah/tabrakan menggunakan sentuhan warna atau sprite
- Simpan data tingkat dalam daftar
- Gunakan blok khusus untuk logika lompatan dan gerakan
**Langkah 3: Terapkan Solusi**```scratch
// Gravity and movement
when green flag clicked
forever
  change y by (y velocity)
  if touching color [brown] then
    set [y velocity v] to [0]
    set [is jumping v] to [0]
  else
    change [y velocity v] by (-1)
  end
  
  if key [right arrow v] pressed then
    change x by (5)
  end
  if key [left arrow v] pressed then
    change x by (-5)
  end
  if key [space v] pressed and not <is jumping = [1]> then
    set [y velocity v] to [10]
    set [is jumping v] to [1]
  end
end
```

**Langkah 4: Verifikasi dan Optimalkan**
Uji lompat pada platform berbeda. Sesuaikan gravitasi dan ketinggian lompatan untuk nuansa permainan yang bagus. Tambahkan animasi untuk berlari dan melompat. Menerapkan pos pemeriksaan menggunakan pesan siaran.
---

### Masalah 2: Membuat Game Kuis dengan Pelacakan Skor
**Langkah 1: Pahami Masalahnya**
Bangun permainan kuis yang mengajukan pertanyaan, memeriksa jawaban, dan melacak skor pemain.
**Langkah 2: Identifikasi Pendekatannya**
- Simpan pertanyaan dan jawaban dalam daftar paralel
- Gunakan penghitung pertanyaan untuk melacak kemajuan
- Gunakan blok "tanya dan tunggu" untuk input
- Bandingkan jawaban dan perbarui skor
**Langkah 3: Terapkan Solusi**```scratch
when green flag clicked
set [score v] to [0]
set [question number v] to [1]

repeat (length of [questions v])
  ask (item (question number) of [questions v]) and wait
  if <(answer) = (item (question number) of [answers v])> then
    change [score v] by (1)
    say [Correct!] for (2) secs
  else
    say [Wrong!] for (2) secs
  end
  change [question number v] by (1)
end

say (join [Final score: ] join (score) [/5]) for (4) secs
```

**Langkah 4: Verifikasi dan Optimalkan**
Uji dengan berbagai jawaban termasuk kasus tepi. Tambahkan umpan balik untuk jawaban yang salah. Terapkan opsi coba lagi. Tambahkan efek suara dan umpan balik visual untuk jawaban benar/salah.
---

### Soal 3: Menggambar Pohon Fraktal dengan Pena
**Langkah 1: Pahami Masalahnya**
Buat pohon fraktal rekursif menggunakan ekstensi pena.
**Langkah 2: Identifikasi Pendekatannya**
- Gunakan rekursi untuk menggambar cabang
- Setiap cabang terbagi menjadi dua cabang yang lebih kecil
- Gunakan sudut acak untuk variasi alami
- Lacak panjang cabang dan kurangi dengan setiap level rekursi
**Langkah 3: Terapkan Solusi**```scratch
define draw branch (length)
pen down
glide (1) secs to (x:(x position) + (length * cos of direction)) (y:(y position) + (length * sin of direction))
pen up

if <(length) > [5]> then
  turn right (pick random (10) to (45))
  draw branch (length * 0.7)
  turn left (pick random (20) to (90))
  draw branch (length * 0.7)
end

when green flag clicked
erase all
goto x:(0) y:(-150)
point in direction (90)
draw branch (100)
```

**Langkah 4: Verifikasi dan Optimalkan**
Sesuaikan ambang batas panjang cabang dan rentang sudut untuk pohon estetika. Tambahkan daun di ujung cabang menggunakan perubahan warna. Terapkan gaya pohon yang berbeda. Simpan gambar sebagai gambar.
---

## Ringkasan
Scratch bukanlah bahasa pemrograman dalam pengertian tradisional — ini adalah lingkungan belajar. Kejeniusannya adalah menghilangkan setiap penghalang antara seorang anak dan kegembiraan dalam menciptakan sesuatu yang interaktif. Dengan berfokus pada konsep daripada sintaksis, Scratch mengajarkan dasar-dasar pemrograman yang dapat ditransfer ke bahasa apa pun. Untuk memperkenalkan pemrograman kepada pelajar muda, Scratch adalah standar emasnya.