<!--
---
# Metadata
title: "Embedded Systems and IoT"
description: "Microcontrollers, sensors, RTOS, IoT protocols, edge computing"
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
tags: [embedded, systems, iot, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "8 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Gömülü Sistemler ve IoT
Gömülü sistemler, arabanızın motor kontrol ünitesi, çamaşır makinenizin kontrolörü, akıllı termostattaki mikrokontrolör gibi diğer cihazların içine gizlenmiş bilgisayarlardır. Genel amaçlı bilgisayarların aksine, genellikle güç, bellek ve işlem hızı konusunda sıkı kısıtlamalarla belirli görevler için tasarlanmıştır. Nesnelerin İnterneti (IoT), gömülü sistemleri ağlara bağlayarak, uzaktan izleme, kontrol ve veri toplama olanağı sağlayarak genişletir. Birlikte, fiziksel dünyayla etkileşime giren milyarlarca bilgi işlem cihazını temsil ediyorlar.
---

## Gömülü Sistemlerin Temelleri
### Gömülü'yü Farklı Kılan Nedir?
| Görünüş | Genel Amaçlı Bilgisayar | Gömülü Sistem |
|----------|---------------------------|------|
| **Amaç** | Herhangi bir yazılımı çalıştırın | Belirli görevleri gerçekleştirin |
| **Kaynaklar** | Bol CPU, RAM, depolama | Sınırlı (KB - MB RAM; MHz - düşük GHz) |
| **Güç** | Takılı veya büyük pil | Çoğunlukla pille çalışan veya enerji toplayan |
| **İşletim Sistemi** | Tam İşletim Sistemi (Windows, Linux, macOS) | RTOS, çıplak metal veya gömülü Linux |
| **Kullanıcı arayüzü** | Zengin (ekran, klavye, fare) | Minimal (LED'ler, düğmeler, sensörler) veya hiçbiri |
| **Gerçek zamanlı** | En iyi çaba | Çoğu zaman zor, gerçek zamanlı teslim tarihleri ​​|
| **ömür boyu** | 3-7 yaş | 10-25+ yıl |
### Mikrodenetleyiciler ve Mikroişlemciler
| Özellik | Mikrodenetleyici (MCU) | Mikroişlemci (MPU) |
|-----------|--------------------------|----------|
| **Entegrasyon** | CPU + RAM + Flash + çevre birimleri tek çipte | Yalnızca CPU; harici RAM ve depolama |
| **Performans** | Düşük ila orta (MHz aralığı) | Yüksek (GHz aralığı) |
| **Güç** | Çok düşük (μA ila mA) | Daha yüksek (yüzlerce mA'dan ampere) |
| **Maliyet** | 0,10$ - 10$ | 5$ - 100$+ |
| **Örnekler** | STM32, ESP32, Arduino (ATmega), nRF52 | Raspberry Pi (BCM2835), i.MX, Allwinner |
| **Kullanım örneği** | Sensörler, aktüatörler, basit kontrol | Gösterimler, karmaşık işleme, Linux |
---

## Ortak Gömülü Platformlar
| Platformu | MCU/MPU | Temel Özellik | En İyisi |
|----------|---------|-------------|----------|
| **Arduino** | ATmega328P (and others) | Basit; büyük topluluk | Öğrenme; prototip oluşturma |
| **ESP32** | Espressif çift çekirdekli | Wi-Fi + Bluetooth; düşük maliyetli | Nesnelerin İnterneti projeleri; bağlı cihazlar |
| **Ahududu Pi Pico** | RP2040 (çift çekirdekli ARM) | Ekonomik; MicroPython desteği | Eğitim; hobi projeleri |
| **STM32** | ARM Cortex-M serisi | Endüstriyel sınıf; geniş ürün yelpazesi | Profesyonel gömülü; endüstriyel |
| **nRF52/nRF53** | İskandinav Yarı İletken | Bluetooth Low Energy specialist | Giyilebilir ürünler; fenerler |
| **Ahududu Pi** | Broadcom BCM (ARM) | Tam Linux; GPIO pinleri | Prototipleme; medya merkezleri; hafif uç bilişim |
| **BeagleBone** | TI Sitara (ARM) | Gerçek zamanlı PRU çekirdekleri | Endüstriyel; gerçek zamanlı uygulamalar |
| **ESP32-S3** | Espressif | AI hızlandırma; USB | Kenar Yapay Zekası; görme uygulamaları |
---

## Gerçek Zamanlı İşletim Sistemleri (RTOS)
RTOS, kritik görevlerin tanımlanmış bir zaman aralığında tamamlanmasını garanti eder.
| RTOS | Lisans | En İyisi |
|------|------------|----------|
| **ÜcretsizRTOS** | MİT | En yaygın olanı; geniş MCU desteği |
| **Zefir** | Apache 2.0 | Modern; Linux Vakfı; büyüyen ekosistem |
| **ThreadX (Azure RTOS)** | MİT | Güvenlik sertifikalı; Nesnelerin İnterneti |
| **embOS** | Ticari | Endüstriyel; sertifikalı |
| **RT-Konu** | Apache 2.0 | Çin ekosistemi; küresel olarak büyüyor |
### RTOS ve Çıplak Metal Karşılaştırması
| Görünüş | Çıplak Metal | RTOS |
|----------|---------------|------|
| **Karmaşıklık** | Basit görevler için basit | Karmaşık, eşzamanlı görevler için gereklidir |
| **Zamanlama** | Manuel (ana döngü + kesintiler) | Önceliklere göre önleyici planlama |
| **Ölçeklenebilirlik** | Özellik eklemek zor | Görev eklemek kolay |
| **Bellek** | Minimum genel gider | Küçük yük (birkaç KB) |
---

## İletişim Protokolleri
### Kablolu Protokoller
| Protokol | Hız | Mesafe | Kullanım Örneği |
|----------|----------|----------|----------|
| **UART** | 1 Mbps'ye kadar | Kısa (yerleşik) | Hata ayıklama konsolu; GPS modülleri |
| **SPI** | 100 MHz'e kadar | Kısa (yerleşik) | Yüksek hızlı çevre birimleri (ekranlar, flaş) |
| **I²C** | 3,4 MHz'e kadar | Kısa (yerleşik) | Sensörler; düşük pin sayımlı iletişim |
| **CAN** | 1 Mbps'ye kadar | 1 km'ye kadar | Otomotiv; endüstriyel |
| **Ethernet** | 10 Mb/sn - 100 Gb/sn | 100 m'ye kadar | Ağ oluşturma; endüstriyel (uzantılarla birlikte) |
| **USB** | 40 Gbps'ye kadar (USB4) | 5 m'ye kadar | Çevre birimleri; şarj |
### Kablosuz Protokoller
| Protokol | Menzil | Güç | Hız | Kullanım Örneği |
|----------|----------|----------|----------|----------|
| **Wi-Fi** | ~100m | Yüksek | Wi-Fi 7'ye kadar (46 Gbps teorik) | Yüksek bant genişliğine sahip IoT; akış |
| **Bluetooth Klasik** | ~100 m | Orta | 1-3 Mb/sn | Ses; dosya aktarımı |
| **BLE** (Bluetooth Düşük Enerji) | ~100 m | Çok düşük | 1-2 Mb/sn | Giyilebilir ürünler; işaretler; sensörler |
| **Zigbee** | ~100 m (gözenek) | Düşük | 250kbps | Ev otomasyonu; endüstriyel sensörler |
| **Z-Dalgası** | ~100 m (gözenek) | Düşük | 100 kbps | Ev otomasyonu |
| **LoRa / LoRaWAN** | 15 km'ye kadar | Çok düşük | 0,3-50 kbps | Tarım; yardımcı programlar; şehir çapında sensörler |
| **NB-IoT** | Hücresel kapsama alanı | Düşük | 250kbps | Ölçüm; varlık takibi |
| **Konu / Konu** | ~100 m (gözenek) | Düşük | Orta | Akıllı ev (Apple, Google, Amazon) |
| **Hücresel (4G/5G)** | Küresel | Yüksek | Yüksek | Bağlantılı araçlar; uzaktan izleme |
---

## IoT Mimarisi
### IoT Yığını
| Katman | İşlev | Örnekler |
|----------|----------|-----------|
| **Cihazlar** | Sensörler, aktüatörler, mikrokontrolörler | ESP32, STM32, Ahududu Pi |
| **Bağlantı** | Ağ protokolleri | MQTT, HTTP, CoAP, LoRaWAN |
| **Edge bilişim** | Cihazın yakınında işleniyor | AWS Greengrass, Azure IoT Edge |
| **Bulut platformu** | Veri alımı, depolanması, işlenmesi | AWS IoT, Azure IoT Hub, Google Cloud IoT |
| **Uygulama** | Gösterge tabloları, analizler, uyarılar | Grafana, özel web uygulamaları |
### IoT İletişim Protokolleri
| Protokol | Desen | En İyisi |
|----------|------------|----------|
| **MQTT** | Yayınla/abone ol; hafif | Çoğu IoT uygulaması; düşük bant genişliği |
| **HTTP/REST** | Talep/cevap | Sadelik önemli olduğunda; web entegrasyonu |
| **CoAP** | Talep/cevap; UDP tabanlı | Kısıtlı cihazlar; düşük güç |
| **AMQP** | Mesaj kuyruğuna alma | Kurumsal IoT; güvenilir teslimat |
| **WebSocket** | Çift yönlü; kalıcı bağlantı | Gerçek zamanlı gösterge tabloları; canlı veriler |
### Ayrıntılı Olarak MQTT
| Konsept | Açıklama |
|-----------|------------|
| **Komisyoncu** | Mesajları yönlendiren merkezi sunucu (Mosquitto, EMQX, HiveMQ) |
| **Konu** | Hiyerarşik adres (ör.`home/living-room/temperature`) |
| **QoS** | 0 (en fazla bir kez), 1 (en az bir kez), 2 (tam olarak bir kez) |
| **Saklanan ileti** | Bir konuyla ilgili son mesaj; yeni abonelere teslim edildi |
| **Son Vasiyet** | Bir istemcinin bağlantısı beklenmedik bir şekilde kesildiğinde yayınlanan mesaj |
---

## Uç Bilgi İşlem
Her şeyi buluta göndermek yerine, verileri kaynağın yakınında işlemek.
| Fayda | Açıklama |
|-----------|------------|
| **Daha az gecikme** | Buluta gidiş-dönüş yok; acil kararlar |
| **Bant genişliğinden tasarruf** | Yalnızca özetleri veya anormallikleri gönderin |
| **Gizlilik** | Hassas veriler şirket içinde kalır |
| **Güvenilirlik** | İnternet kapalıyken çalışır |
| Platformu | Açıklama |
|----------|----------------|
| **AWS Greengrass** | Lambda işlevlerini uç cihazlarda çalıştırın |
| **Azure IoT Edge** | Container'ları uç cihazlarda çalıştırın |
| **NVIDIA Jetson** | GPU ile hızlandırılmış uç yapay zeka (Orin, Nano) |
| **Ahududu Pi** | Hafif uç bilişim |
---

## Firmware Güncellemesi (OTA)
Kablosuz güncellemeler, hataları düzeltmenize ve dağıtılan cihazlara özellikler eklemenize olanak tanır.
| endişe | Çözüm |
|-----------|----------|
| **Güvenilirlik** | Çift bankalı flaş; başarısızlık durumunda geri alma |
| **Güvenlik** | İmzalı görseller; şifreli aktarımlar |
| **Boyut** | Delta güncellemeleri (yalnızca değiştirilen kısımlar) |
| **Bağlantı** | Cihaz çevrimiçi olduğunda kuyruk güncellemeleri |
---

## Güvenlik Açısından Kritik Gömülü Sistemler
| Etki Alanı | Standartlar | Örnekler |
|----------|---------------|-----------|
| **Otomotiv** | ISO 26262 (ASIL A-D) | Motor kontrolü, frenleme, hava yastıkları |
| **Tıp** | IEC 62304 | Kalp pilleri, infüzyon pompaları |
| **Havacılık** | DO-178C (DAL A-E) | Uçuş kontrolü, navigasyon |
| **Endüstriyel** | IEC 61508 (SIL 1-4) | PLC'ler, güvenlik kontrolörleri |
| **Demiryolu** | EN 50128 (SIL 1-4) | Sinyalizasyon, tren kontrolü |
---

## Araçlar ve Geliştirme
| Araç | Amaç |
|------|------------|
| **PlatformIO** | Çapraz platformlu gömülü geliştirme (Arduino, ESP32, STM32) |
| **STM32CubeIDE** | ST'nin STM32 için resmi IDE'si |
| **Arduino IDE'si** | Arduino ve uyumlu kartlar için basit geliştirme |
| **ESP-IDF** | Espressif'in ESP32 için resmi SDK'sı |
| **Zephyr SDK'sı** | Zephyr RTOS için Batı sistemi inşa edildi |
| **OCD'yi açın** | Çip üzerinde hata ayıklama |
| **Mantık analizörü** | SPI, I²C, UART protokollerinde hata ayıklama |
| **Wireshark** | Ağ protokolü analizi |
---

## Özet
Gömülü sistemler ve IoT, yazılım ile fiziksel dünyanın kesişimini temsil eder. Motorları kontrol eden mikrodenetleyicilerden buluta bağlı sensör ağlarına kadar, web veya uygulama geliştirmeden farklı bir zihniyet gerektirirler: kısıtlı kaynaklar, gerçek zamanlı gereksinimler, uzun ömürler ve hataların fiziksel dünyadaki sonuçları. Ekosistem son derece olgunlaştı; ESP-IDF ve Zephyr gibi çerçeveler profesyonel gelişimi erişilebilir hale getirirken, AWS IoT ve Azure IoT Hub gibi platformlar bulut tarafını yönetiyor. Temel beceriler, donanım arayüzlerini, iletişim protokollerini, güç yönetimini ve yıllarca müdahale edilmeden güvenilir bir şekilde çalışması gereken yazılım yazma disiplinini anlamaktır.