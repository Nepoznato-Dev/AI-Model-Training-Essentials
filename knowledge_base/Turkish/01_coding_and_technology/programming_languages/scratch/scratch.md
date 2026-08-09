---
# Metadata
title: "Scratch"
description: "Comprehensive reference for the Scratch programming language covering overview, trade-offs, syntax fundamentals, ecosystem, and when to use it."
category: "Coding and Technology"
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

# Çizik
Scratch, MIT Medya Laboratuvarı tarafından geliştirilen ve ilk olarak 2007'de piyasaya sürülen görsel, blok tabanlı bir programlama dilidir. Kullanıcılar, metin tabanlı kod yazmak yerine renkli blokları bir araya getirerek programlar oluşturur. Scratch, temel programlama kavramlarını (döngüler, koşullar, değişkenler, olaylar ve işlevler) sözdizimi hataları engeli olmadan öğretmek için özel olarak 8-16 yaş arası çocuklar için tasarlanmıştır (gerçi her yaştan öğrenci bunu kullanır).
Scratch, 100 milyondan fazla kayıtlı kullanıcısı ve 70'ten fazla dilde kullanılabilirliği ile dünyada en yaygın kullanılan başlangıç ​​programlama dilidir. Bir web tarayıcısında çalışır ve ücretsizdir.
---

## Scratch Neden Önemlidir?
- **Programlamaya en iyi giriş**: Sözdizimi engellerini tamamen kaldırır. Kavramlar görsel manipülasyon yoluyla öğretilir.
- **Bilgisayarlı düşünme**: Ayrıştırma, örüntü tanıma, soyutlama ve algoritma tasarımını öğretir.
- **Yaratıcılık odaklı**: Çocuklar oyunlar, animasyonlar, hikayeler ve müzik yaratır; programlamayı önemsedikleri şeyleri yapmanın bir yan ürünü olarak öğrenirler.
- **Küresel erişim**: Dünya çapındaki okullarda kullanılır. 70'den fazla dilde mevcuttur. Ücretsiz ve tarayıcı tabanlı.
- **Topluluk**: Scratch çevrimiçi topluluğu paylaşmayı, yeniden düzenlemeyi ve işbirliğine dayalı öğrenmeyi öğretir.
## Takaslar
| Sınırlama | Ayrıntılar | Tipik Geçici Çözüm |
|-----------|------------|-----------|
| **"Gerçek" bir programlama dili değildir** | Üretim yazılımı, API'ler veya sistemler oluşturulamıyor | Python, JavaScript veya metin tabanlı dillere geçiş |
| **Sınırlı yetenekler** | Dosya G/Ç'si, ağ iletişimi veya gelişmiş veri yapıları yok | Öğrenmek için kullanın; gerçek projeler için metin dillerine geçin |
| **Performans** | Yorumlanmış, karmaşık projeler için yavaş | Performans açısından kritik işler için tasarlanmamıştır |
| **Yaş algısı** | Genellikle "sadece çocuklar için" olarak görülüyor | Scratch bir öğrenme aracıdır, profesyonel bir dil değildir |
---

## Scratch Nasıl Çalışır?
Kazıma programları ("projeler" olarak adlandırılır), komut dosyalarında bir araya getirilen **bloklara** yanıt veren **hareketlilerden** (karakterler/nesneler) oluşur.
### Temel Kavramlar (Bloklar Aracılığıyla Öğretilir)
| Konsept | Çizilme Blok Kategorisi | Örnek |
|-----------|-----------|-----------|
| **Diziler** | Hareket, Görünüş | "10 adım ilerleyin" ve ardından "Merhaba Deyin" |
| **Döngüler** | Kontrol (sarı) | "10 Tekrarla", "Sonsuza Kadar Tekrarla", "Şuna Kadar Tekrarla" |
| **Koşullar** | Kontrol (sarı) | "Eğer... o zaman", "Eğer... o zaman... değilse" |
| **Değişkenler** | Değişkenler (turuncu) | "Puan 0 olarak ayarla", "Puan 1'e göre değiştir" |
| **Etkinlikler** | Etkinlikler (sarı) | "Yeşil bayrak tıklandığında", "Tuşa basıldığında" |
| **İşlevler** | Bloklarım (özel) | Yeniden kullanılabilir blok dizilerini tanımlayın |
| **Listeler (diziler)** | Değişkenler (turuncu) | "Listeye ekle", "Listenin öğesi" |
| **Yayınlanıyor** | Etkinlikler | Karakterler arasında mesaj gönderin |
### Örnek: Basit Oyun Mantığı
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

## Gelişmiş Sözdizimi ve Desenler
### Kategorileri Ayrıntılı Olarak Engelleyin
Scratch 3.0, blokları renk kodlu kategoriler halinde düzenler:
| Kategori | Renk | Blok Türleri |
|----------|-----------|------------|
| **Hareket** | Mavi | hareket et, dön, git, kay, noktala, değiştir x/y |
| **Görünüş** | Mor | söyle, düşün, kostümü değiştir, boyutunu değiştir, göster/gizle |
| **Ses** | Pembe | ses çal, sesleri durdur, ses seviyesini değiştir, perdeyi değiştir |
| **Etkinlikler** | Sarı | bayrak tıklandığında, tuşa basıldığında, sprite tıklandığında yayın |
| **Kontrol** | Altın | bekle, tekrarla, sonsuza kadar, if, if-else, tekrarla, dur |
| **Algılama** | Açık Mavi | dokunma, tuşa basma, fare, mesafe, sorma/cevaplama, zamanlayıcı |
| **Operatörler** | Yeşil | matematik işlemleri, metin işlemleri, karşılaştırma ve/veya/değil, rastgele |
| **Değişkenler** | Turuncu | değişkeni ayarlama/değiştirme, listeleme işlemleri |
| **Bloklarım** | Koyu Kırmızı | özel blok tanımları (işlevler) |
### Gelişmiş Blok Desenleri
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

### Özel Bloklar (İşlevler)
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

### Liste İşlemleri (Diziler)
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

### Yayın (Sprite Arası İletişim)
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

## Mimari ve Sistem Tasarımı
### Olay Odaklı Tasarım
Scratch olay odaklı bir mimari kullanır. Her komut dosyası bir olay bloğuyla (şapka bloğu) başlar ve bu olaya yanıt olarak çalışır.
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

### Proje Yapısı
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

### Klonlama Sistemi (Nesne Oluşturma)
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

## Proje Yapılandırması ve Oluşturma Sistemi
### Çizik Uzantıları
Scratch, yetenekler ekleyen resmi ve topluluk uzantılarını destekler:
| Uzantı | Amaç |
|-----------|------------|
| **Kalem** | Sahnede çizgiler ve şekiller çizin |
| **Video Algılama** | Hareket algılama için web kamerasını kullanın |
| **Metinden Konuşmaya** | Metni sözlü sese dönüştürün |
| **Çevir** | Diller arasında metin çevirme |
| **Makey Makey** | Fiziksel nesneleri giriş olarak bağlama |
| **mikro:bit** | BBC mikro:bit donanımını bağlayın |
| **LEGO Zihin Fırtınaları** | LEGO robotlarını kontrol edin |
| **Müzik** | Nota ve enstrüman çalma |
### Kazı Kazan Dosya Formatı
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

### Çevrimdışı Düzenleyici
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

## Test Etme ve Hata Ayıklama
### Yerleşik Hata Ayıklama Araçları
Scratch, projelerde hata ayıklamak için çeşitli yerleşik araçlar sağlar:
| Araç | Nasıl Kullanılır |
|------|---------------|
| **Kaplumbağa modu** | Bir karaktere sağ tıklayın ve koordinatları görmek için "hata ayıklamayı göster"i seçin |
| **Değişken monitörler** | Bir değişkene sağ tıklayın ve değerini gerçek zamanlı olarak görmek için "göster"i seçin |
| **Monitörleri listele** | Liste içeriğini normal, satır veya sütun görünümünde görüntüleyin |
| **Turbo modu** | Daha hızlı yürütme için yeşil bayrağa tıklarken Shift tuşunu basılı tutun |
| **Tek adımlı mod** | "Tek adım" için yeşil bayrağa sağ tıklayın (yürütmeyi yavaşlatır) |
### Hata Ayıklama Modelleri
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

### Yaygın Sorunlar
| Sorun | Sebep | Çözüm |
|-----------|----------|----------|
| Sprite yanıt vermiyor | Etkinlik yok şapka bloğu | "Yeşil bayrak tıklandığında" veya başka bir etkinlik ekleyin |
| Klon çalışmıyor | Klon oluşturuldu ancak gösterilmiyor | "Klon olarak başladığımda" ifadesinin sonuna "Göster" bloğunu ekle |
| Değişkenler arasında paylaşılan değişken | Küresel ve yerel değişken karışıklığı | "Yalnızca bu sprite için" seçeneğini kullanın |
| Yayın alınamadı | Yanlış mesaj adı | Yayın ve alma adlarının tam olarak eşleştiğini doğrulayın |
| Sonsuz döngü dondurma | "Sonsuza Kadar", beklemeden | Sıkı döngülere küçük "Bekle" blokları ekleyin |
---

## Birlikte Çalışabilirlik
### Donanım Uzantıları
Scratch, uzantılar aracılığıyla fiziksel donanıma bağlanabilir:
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

### Scratch Uzantıları API'si (Özel Uzantılar)
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

## Tasarım Desenleri
### Desen 1: Platform Hareketi
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

### Desen 2: Kaydırma Arka Planı
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

### Desen 3: Sprite Takip (Chase AI)
```
When green flag clicked:
  Forever:
    Point towards [Player]
    Move 3 steps
    If <touching [Player]?> then
      Broadcast [player_caught]
      Go to random position
```

### Model 4: Listeli Envanter Sistemi
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

### Desen 5: Klonlu Parçacık Sistemi
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

## Performans ve Optimizasyon
### Karakter Optimizasyonu
| Tekniği | Etki | Açıklama |
|-----------|-----------|------------|
| **Klonları en aza indirin** | Yüksek | Her klon hafızayı tüketir; bittiğinde sil |
| **Kostümleri azaltın** | Orta | Daha az kostüm değişikliği, daha az görüntü oluşturma yükü anlamına gelir |
| **"Ekran yenilemeden çalıştır" seçeneğini kullanın** | Yüksek | Ekran yenilemesi olmayan özel bloklar daha hızlı çalışır |
| **"say" bloklarını sınırlayın** | Orta | Konuşma balonları görüntü oluşturma yüküne neden oluyor |
| **Her karakterde "sonsuza kadar" ifadesinden kaçının** | Orta | Sürekli oylama yerine yayınları ve etkinlikleri kullanın |
### Klon Yönetimi
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

### Optimizasyon Kontrol Listesi
| Tekniği | Etki | Açıklama |
|-----------|-----------|------------|
| **Ekran yenilemeden çalıştır** | Çok Yüksek | Özel bloklar hız için görüntülemeyi atlıyor |
| **Etkin klonları en aza indirin** | Yüksek | Artık ihtiyaç duyulmadığı anda klonları silin |
| **Yayınları dikkatli kullanın** | Orta | Kare başına çok fazla yayın gecikmeye neden oluyor |
| **Kostümleri basitleştirin** | Orta | Daha küçük resimler daha hızlı işlenir |
| **Liste işlemlerini azaltın** | Orta | Her karede büyük listeleri taramaktan kaçının |
| **"bekleme" bloklarını kullanın** | Düşük | Sonsuz döngülerde CPU'nun aşırı yüklenmesini önleyin |
---

## Dağıtım ve Gerçek Dünya Kullanımı
### Projeleri Paylaşma
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

### Gerçek Dünyada Eğitimsel Kullanım
| Bağlam | Scratch Nasıl Kullanılır | Ölçek |
|-----------|-----------|-------|
| **K-12 okulları** | Bilgisayar Bilimi sınıflarında programlamaya giriş | 190'dan fazla ülkede kullanılıyor |
| **Kodlama kulüpleri** | Scratch Club / CoderDojo atölyeleri | Dünya çapında 3000'den fazla kulüp |
| **Kütüphaneler** | Okul sonrası programlama programları | Halk kütüphanesi sistemleri |
| **Evde Eğitim** | Kendi hızınızda programlama eğitimi | Milyonlarca evde öğrenen |
| **Üniversite CS0** | Ana dal dışı bilgisayar bilimlerine giriş kursları | Üniversite köprü programları |
| **Erişilebilirlik** | Görme engellilere programlama öğretmek | Ekran okuyucu desteği |
| **Terapi** | Bilişsel ve motor beceri gelişimi | Mesleki terapi |
### Eğitim Araştırmalarında Çizik
Araştırmalar Scratch'in etkili bir şekilde şunları öğrettiğini göstermiştir:
- **Sıralı düşünme**: Sorunları sıralı adımlara ayırma
- **Hata ayıklama becerileri**: Mantıktaki hataları bulma ve düzeltme
- **Yaratıcı ifade**: Sanat, müzik ve programlamayı birleştirmek
- **İşbirliği**: Başkalarının projelerini yeniden düzenlemek ve geliştirmek
- **İstikrar**: Projeleri iyileştirmek için yinelemek
---

## Sıfırdan Geçiş
Scratch'i öğrendikten sonra tipik sonraki adımlar şunları içerir:
| Sonraki Dil | Neden |
|----------------|-----|
| **Python** | En doğal geçiş — okunabilir sözdizimi, benzer mantık kavramları |
| **JavaScript** | Web/oyunlarla ilgileniyorsanız anında görsel geri bildirim |
| **Lua (Roblox/Love2D aracılığıyla)** | Oyun geliştirmeyle ilgileniyorsanız |
| **Uygulama Mucidi** | Android uygulamaları için görsel bloklar (aynı MIT kökeni) |
| **Blok olarak** | Google'ın görsel programlama kitaplığı (benzer kavramlar) |
### Konsept Haritalama: Python'a Çiz
| Çizik Konsepti | Python Eşdeğeri |
|----------------|------------------|
| `set [x] to 0`| `x = 0`|
| `change [x] by 1`| `x += 1`|
| `repeat 10`| `for i in range(10):`|
| `forever`| `while True:`|
| `if ... then`| `if ...:`|
| `broadcast [msg]`| İşlev çağrısı veya olay sistemi |
| `My Blocks`| `def function():`|
| `list`| `list = []`|
| `item 1 of [list]`| `list[0]`(0-indeksli!) |
| `length of [list]`| `len(list)`|
---

## Scratch Ne Zaman Kullanılır?
| Senaryo | Neden Scratch | Daha İyi Alternatif |
|----------|-----------|-----------|
| Çocuklara (8-16) kodlamayı öğretmek | Bunun için özel olarak tasarlandı | — |
| Bilişimsel düşünmeye giriş | Görsel, söz dizimi hatası yok | — |
| Okul atölyeleri / kodlama kulüpleri | Ücretsiz, tarayıcı tabanlı, kurulum gerektirmez | — |
| Oyun fikirlerini görsel olarak prototipleme | Hızlı yineleme | — |
| Mesleki gelişim | Bunun için tasarlanmadı | Python, JavaScript, herhangi bir metin dili |
| Üniversite düzeyinde bilgisayar bilimleri eğitimi | Çok basit | Python, Java, C |
---

## Özet
Scratch geleneksel anlamda bir programlama dili değildir; bir öğrenme ortamıdır. Dehası, bir çocuk ile etkileşimli bir şey yaratmanın keyfi arasındaki tüm engelleri ortadan kaldırıyor. Scratch, söz dizimi yerine kavramlara odaklanarak, herhangi bir dile aktarılabilen programlamanın temellerini öğretir. Genç öğrencilere programlamayı tanıtmak için Scratch altın standarttır.