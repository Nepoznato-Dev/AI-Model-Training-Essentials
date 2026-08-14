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
# Sistem Tertanam dan IoT
Sistem tertanam adalah komputer yang tersembunyi di dalam perangkat lain — unit kontrol mesin mobil Anda, pengontrol mesin cuci Anda, mikrokontroler dalam termostat cerdas. Tidak seperti komputer untuk tujuan umum, komputer ini dirancang untuk tugas-tugas tertentu, seringkali dengan batasan ketat pada daya, memori, dan kecepatan pemrosesan. Internet of Things (IoT) memperluas sistem tertanam dengan menghubungkannya ke jaringan, memungkinkan pemantauan, pengendalian, dan pengumpulan data jarak jauh. Bersama-sama, mereka mewakili miliaran perangkat komputasi yang berinteraksi dengan dunia fisik.
---

## Dasar-dasar Sistem Tertanam
### Apa yang Membuat Tertanam Berbeda
| Aspek | Komputer Serbaguna | Sistem Tertanam |
|--------|------------------------|-----------------|
| **Tujuan** | Jalankan perangkat lunak apa pun | Melakukan tugas tertentu |
| **Sumber Daya** | CPU, RAM, penyimpanan berlimpah | Terbatas (KB hingga MB RAM; MHz hingga GHz rendah) |
| **Kekuatan** | Dicolokkan atau baterai besar | Seringkali bertenaga baterai atau hemat energi |
| **OS** | OS Lengkap (Windows, Linux, macOS) | RTOS, bare-metal, atau Linux tertanam |
| **Antarmuka pengguna** | Kaya (layar, keyboard, mouse) | Minimal (LED, tombol, sensor) atau tidak sama sekali |
| **Waktu Nyata** | Upaya terbaik | Seringkali tenggat waktu real-time yang sulit |
| **Seumur Hidup** | 3-7 tahun | 10-25+ tahun |
### Mikrokontroler vs Mikroprosesor
| Fitur | Mikrokontroler (MCU) | Mikroprosesor (MPU) |
|---------|----------------------|---------------------|
| **Integrasi** | CPU + RAM + Flash + periferal dalam satu chip | Hanya CPU; RAM dan penyimpanan eksternal |
| **Kinerja** | Rendah hingga sedang (rentang MHz) | Tinggi (rentang GHz) |
| **Kekuatan** | Sangat rendah (µA ke mA) | Lebih tinggi (ratusan mA hingga amp) |
| **Biaya** | $0,10 - $10 | $5 - $100+ |
| **Contoh** | STM32, ESP32, Arduino (ATmega), nRF52 | Raspberry Pi (BCM2835), i.MX, Pemenang Semua |
| **Kasus penggunaan** | Sensor, aktuator, kontrol sederhana | Tampilan, pemrosesan kompleks, Linux |
---

## Platform Tersemat Umum
| Peron | MCU/MPU | Fitur Utama | Terbaik Untuk |
|----------|---------|-------------|----------|
| **Arduino** | ATmega328P (dan lainnya) | Sederhana; komunitas besar | Sedang belajar; pembuatan prototipe |
| **ESP32** | Espressif dual-core | Wi-Fi + Bluetooth; biaya rendah | proyek IoT; perangkat yang terhubung |
| **Raspberi Pi Pico** | RP2040 (lengan inti ganda) | Terjangkau; Dukungan MicroPython | Pendidikan; proyek hobi |
| **STM32** | Seri ARM Cortex-M | Kelas industri; jangkauan luas | Tertanam profesional; industri |
| **nRF52/nRF53** | Semikonduktor Nordik | Spesialis Bluetooth Hemat Energi | Perangkat yang dapat dikenakan; suar |
| **Raspberi Pi** | Broadcom BCM (LENGAN) | Linux Lengkap; Pin GPIO | pembuatan prototipe; pusat media; komputasi tepi ringan |
| **BeagleBone** | TI Sitara (LENGAN) | Inti PRU waktu nyata | Industri; aplikasi waktu nyata |
| **ESP32-S3** | Espresif | akselerasi AI; USB | Tepi AI; aplikasi visi |
---

## Sistem Operasi Waktu Nyata (RTOS)
RTOS menjamin bahwa tugas-tugas penting diselesaikan dalam jangka waktu yang ditentukan.
| RTOS | Lisensi | Terbaik Untuk |
|------|---------|----------|
| **GratisRTOS** | MIT | Paling umum; dukungan MCU yang luas |
| **Zefhir** | Apache 2.0 | Modern; Yayasan Linux; ekosistem tumbuh |
| **ThreadX (Azure RTOS)** | MIT | Bersertifikat keselamatan; IoT |
| **emmbos** | Komersial | Industri; bersertifikat |
| **RT-Utas** | Apache 2.0 | ekosistem Tiongkok; tumbuh secara global |
### RTOS vs Bare Metal
| Aspek | Logam Telanjang | RTOS |
|--------|-----------|------|
| **Kompleksitas** | Sederhana untuk tugas sederhana | Dibutuhkan untuk tugas yang kompleks dan bersamaan |
| **Penjadwalan** | Manual (loop utama + interupsi) | Penjadwalan preemptive dengan prioritas |
| **Skalabilitas** | Sulit untuk menambahkan fitur | Mudah untuk menambahkan tugas |
| **Memori** | Biaya overhead minimal | Overhead kecil (beberapa KB) |
---

## Protokol Komunikasi
### Protokol Berkabel
| Protokol | Kecepatan | Jarak | Kasus Penggunaan |
|----------|-------|----------|----------|
| **UART** | Hingga 1 Mbps | Pendek (on-board) | Konsol debug; Modul GPS |
| **SPI** | Hingga 100MHz | Pendek (on-board) | Periferal berkecepatan tinggi (layar, flash) |
| **I²C** | Hingga 3,4 MHz | Pendek (on-board) | Sensor; komunikasi dengan jumlah pin rendah |
| **BISA** | Hingga 1 Mbps | Hingga 1 km | Otomotif; industri |
| **Ethernet** | 10 Mbps - 100 Gbps | Hingga 100 m | Jaringan; industri (dengan ekstensi) |
| **USB** | Hingga 40 Gbps (USB4) | Hingga 5 m | Periferal; pengisian |
### Protokol Nirkabel
| Protokol | Rentang | Kekuatan | Kecepatan | Kasus Penggunaan |
|----------|-------|-------|-------|----------|
| **Wi-Fi** | ~100 m | Tinggi | Hingga Wi-Fi 7 (teoritis 46 Gbps) | IoT bandwidth tinggi; streaming |
| **Bluetooth Klasik** | ~100 m | Sedang | 1-3Mbps | audio; transfer berkas |
| **BLE** (Bluetooth Hemat Energi) | ~100 m | Sangat rendah | 1-2Mbps | Perangkat yang dapat dikenakan; suar; sensor |
| **Zigbee** | ~100 m (jaring) | Rendah | 250 kbps | Otomatisasi rumah; sensor industri |
| **Z-Gelombang** | ~100 m (jaring) | Rendah | 100 kbps | Otomatisasi rumah |
| **LoRa / LoRaWAN** | Hingga 15 km | Sangat rendah | 0,3-50 kbps | Pertanian; utilitas; sensor seluruh kota |
| **NB-IoT** | Jangkauan seluler | Rendah | 250 kbps | Pengukuran; pelacakan aset |
| **Benang / Materi** | ~100 m (jaring) | Rendah | Sedang | Rumah pintar (Apple, Google, Amazon) |
| **Seluler (4G/5G)** | Global | Tinggi | Tinggi | Kendaraan yang terhubung; pemantauan jarak jauh |
---

## Arsitektur IoT
### Tumpukan IoT
| Lapisan | Fungsi | Contoh |
|-------|----------|---------|
| **Perangkat** | Sensor, aktuator, mikrokontroler | ESP32, STM32, Raspberry Pi |
| **Konektivitas** | Protokol jaringan | MQTT, HTTP, CoAP, LoRaWAN |
| **Komputasi tepi** | Memproses di dekat perangkat | AWS Greengrass, Azure IoT Edge |
| **Platform awan** | Penyerapan data, penyimpanan, pemrosesan | AWS IoT, Azure IoT Hub, Google Cloud IoT |
| **Aplikasi** | Dasbor, analitik, peringatan | Grafana, aplikasi web khusus |
### Protokol Komunikasi IoT
| Protokol | Pola | Terbaik Untuk |
|----------|---------|----------|
| **MQTT** | Publikasikan/berlangganan; ringan | Sebagian besar aplikasi IoT; bandwidth rendah |
| **HTTP/SISANYA** | Permintaan/tanggapan | Ketika kesederhanaan itu penting; integrasi web |
| **CoAP** | Permintaan/tanggapan; Berbasis UDP | Perangkat terbatas; daya rendah |
| **AMQP** | Antrian pesan | IoT Perusahaan; pengiriman yang dapat diandalkan |
| **Soket Web** | Dua arah; koneksi persisten | Dasbor waktu nyata; data langsung |
### MQTT secara Detail
| Konsep | Deskripsi |
|---------|-------------|
| **Broker** | Server pusat yang merutekan pesan (Mosquitto, EMQX, HiveMQ) |
| **Topik** | Alamat hierarki (misalnya,`home/living-room/temperature`) |
| **QoS** | 0 (paling banyak satu kali), 1 (minimal satu kali), 2 (tepat satu kali) |
| **Pesan yang disimpan** | Pesan terakhir tentang suatu topik; dikirimkan ke pelanggan baru |
| **Wasiat Terakhir** | Pesan diterbitkan ketika klien terputus secara tidak terduga |
---

## Komputasi Tepi
Memproses data dekat sumbernya alih-alih mengirimkan semuanya ke cloud.
| Manfaat | Deskripsi |
|---------|-------------|
| **Mengurangi latensi** | Tidak perlu bolak-balik ke cloud; keputusan segera |
| **Penghematan bandwidth** | Hanya kirimkan ringkasan atau anomali |
| **Privasi** | Data sensitif tetap berada di lokasi |
| **Keandalan** | Berfungsi saat internet mati |
| Peron | Deskripsi |
|----------|-------------|
| **AWS Rumput Hijau** | Jalankan fungsi Lambda pada perangkat edge |
| **Azure IoT Edge** | Jalankan container di perangkat edge |
| **NVIDIA Jetson** | AI edge dengan akselerasi GPU (Orin, Nano) |
| **Raspberi Pi** | Komputasi tepi ringan |
---

## Pembaruan Firmware (OTA)
Pembaruan melalui udara memungkinkan Anda memperbaiki bug dan menambahkan fitur ke perangkat yang diterapkan.
| Kekhawatiran | Solusi |
|---------|----------|
| **Keandalan** | Flash bank ganda; kembalikan jika gagal |
| **Keamanan** | Gambar yang ditandatangani; transfer terenkripsi |
| **Ukuran** | Pembaruan Delta (hanya mengubah sebagian) |
| **Konektivitas** | Antrian pembaruan saat perangkat online |
---

## Sistem Tertanam yang Penting untuk Keselamatan
| Domain | Standar | Contoh |
|--------|-----------|---------|
| **Otomotif** | ISO 26262 (ASIL AD) | Kontrol mesin, pengereman, airbag |
| **Medis** | IEC 62304 | Alat pacu jantung, pompa infus |
| **Dirgantara** | DO-178C (DAL A-E) | Kontrol penerbangan, navigasi |
| **Industri** | IEC 61508 (SIL 1-4) | PLC, pengontrol keselamatan |
| **Kereta Api** | EN 50128 (SIL 1-4) | Persinyalan, kendali kereta api |
---

## Alat dan Pengembangan
| Alat | Tujuan |
|------|---------|
| **PlatformIO** | Pengembangan tertanam lintas platform (Arduino, ESP32, STM32) |
| **STM32CubeIDE** | IDE resmi ST untuk STM32 |
| **Arduino IDE** | Pengembangan sederhana untuk Arduino dan papan yang kompatibel |
| **ESP-IDF** | SDK resmi Espressif untuk ESP32 |
| **Zephyr SDK** | Sistem pembangunan barat untuk Zephyr RTOS |
| **BukaOCD** | Proses debug pada chip |
| **Penganalisis logika** | Debug protokol SPI, I²C, UART |
| **Wireshark** | Analisis protokol jaringan |
---

## Ringkasan
Sistem tertanam dan IoT mewakili titik temu antara perangkat lunak dan dunia fisik. Mulai dari mikrokontroler yang mengendalikan motor hingga jaringan sensor yang terhubung ke cloud, mereka memerlukan pola pikir yang berbeda dari pengembangan web atau aplikasi: sumber daya yang terbatas, persyaratan waktu nyata, masa pakai yang lama, dan konsekuensi bug di dunia fisik. Ekosistemnya telah sangat matang — kerangka kerja seperti ESP-IDF dan Zephyr membuat pengembangan profesional dapat diakses, sementara platform seperti AWS IoT dan Azure IoT Hub menangani sisi cloud. Keterampilan utamanya adalah memahami antarmuka perangkat keras, protokol komunikasi, manajemen daya, dan disiplin dalam menulis perangkat lunak yang harus berjalan dengan andal selama bertahun-tahun tanpa intervensi.