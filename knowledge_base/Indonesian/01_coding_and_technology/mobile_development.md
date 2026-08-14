---
# Metadata
title: "Mobile Development"
description: "iOS, Android, React Native, Flutter, mobile architecture"
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
tags: [mobile, development, coding-and-technology]
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
# Pengembangan Seluler
Pengembangan seluler adalah praktik membangun aplikasi untuk ponsel cerdas dan tablet — terutama untuk iOS (Apple) dan Android (Google). Ini mencakup segalanya mulai dari desain UI untuk layar kecil hingga mengelola masa pakai baterai, menangani ketidakstabilan jaringan, dan mendistribusikan aplikasi melalui toko. Bidang ini telah berkembang secara signifikan, dengan kerangka kerja lintas platform kini bersaing dengan pengembangan asli untuk sebagian besar kasus penggunaan.
---

## Lanskap Seluler
| Peron | Pengembang | Bahasa | Toko | Pangsa Pasar (Global) |
|----------|-----------|-------------|-------|----------------------|
| **Android** | Google | Kotlin, Jawa | Google Bermain | ~72% |
| **iOS** | apel | Cepat, Objective-C | Toko Aplikasi | ~27% |
---

## Pengembangan Asli
### Android
| Aspek | Detail |
|--------|---------|
| **Bahasa** | Kotlin (utama), Java (lama) |
| **Kerangka UI** | Jetpack Compose (modern), tata letak XML (lama) |
| **Bangun sistem** | Gradasi |
| **IDE** | Android Studio |
| **Minimal SDK** | Pengembang memilih; API 24+ paling bertarget (Android 7.0, 2016) |
| **Distribusi** | Google Play Toko; toko alternatif di beberapa pasar |
### iOS
| Aspek | Detail |
|--------|---------|
| **Bahasa** | Swift (utama), Objective-C (warisan) |
| **Kerangka UI** | SwiftUI (modern), UIKit (dewasa) |
| **Bangun sistem** | Sistem pembangunan Xcode |
| **IDE** | Xcode (hanya macOS) |
| **Versi minimal** | Pengembang memilih; sebagian besar menargetkan iOS 16+ |
| **Distribusi** | Apple App Store (satu-satunya pilihan untuk sebagian besar aplikasi) |
---

## Kerangka Kerja Lintas Platform
Bangun sekali, terapkan ke iOS dan Android.
| Kerangka | Bahasa | Merender | Kinerja | Terbaik Untuk |
|-----------|----------|-----------|-------------|----------|
| **Berkibar** | Anak panah | Mesin khusus (Skia/Impeller) | Hampir asli | UI khusus yang kaya; tampilan yang konsisten di seluruh platform |
| **Reaksi Asli** | JavaScript/Skrip Ketik | Komponen asli melalui jembatan | Bagus (Arsitektur Baru meningkatkan ini) | Tim dengan pengalaman web/JS |
| **Multiplatform Kotlin** | Kotlin | UI asli per platform | Asli | Berbagi logika bisnis; UI asli |
| **MAUI** (.NET) | C#| Kontrol asli | Bagus | tim .NET; aplikasi perusahaan |
| **Ionik / Kapasitor** | HTML/CSS/JS | Tampilan Web | Lebih rendah | Aplikasi sederhana; tim web |
### Flutter vs Bereaksi Asli
| Aspek | Berkibar | Bereaksi Asli |
|--------|---------|-------------|
| **Bahasa** | Anak panah | JavaScript/Skrip Ketik |
| **Rendering UI** | Menggambar semuanya sendiri (konsisten di seluruh platform) | Menggunakan komponen asli (tampilan khusus platform) |
| **Muat ulang panas** | Luar biasa | Bagus |
| **Ekosistem** | Berkembang pesat; berbasis widget | Besar; ekosistem npm |
| **Kurva pembelajaran** | Perlu belajar Dart | Lebih mudah bagi pengembang web |
| **Integrasi platform** | Saluran platform untuk kode asli | Modul asli melalui jembatan |
| **Kinerja** | Bagus sekali; hampir asli | Bagus; jembatan di atas kepala (dikurangi dengan Arsitektur Baru) |
---

## Pola Arsitektur Seluler
| Pola | Deskripsi | Kapan Menggunakan |
|---------|-------------|-------------|
| **MVC** | Pengontrol Tampilan Model | Aplikasi sederhana; akrab bagi pengembang web |
| **MVVM** | Model-Tampilan-TampilanModel; pengikatan data | Aplikasi seluler paling modern |
| **MVI** | Model-View-Intent; aliran data searah | pengelolaan negara yang kompleks; Flutter (dengan BLoC/Riverpod) |
| **Arsitektur Bersih** | Lapisan dengan inversi ketergantungan | Tim besar; logika bisnis yang kompleks |
---

## Masalah Utama Seluler
### Offline-Desain Pertama
Aplikasi seluler harus berfungsi tanpa internet yang andal.
| Strategi | Deskripsi |
|----------|-------------|
| **Basis data lokal** | Menyimpan data di perangkat (SQLite, Room, CoreData, Realm) |
| **Strategi sinkronisasi** | Sinkronisasi dengan server saat online; menyelesaikan konflik |
| **UI Optimis** | Perbarui UI segera; rekonsiliasi ketika server merespons |
| **Tembolok** | Respons API cache; melayani dari cache saat offline |
### Pertunjukan
| Kekhawatiran | Solusi |
|---------|----------|
| **Waktu memulai aplikasi** | Pemuatan lambat; meminimalkan pekerjaan inisialisasi |
| **Penggunaan memori** | Kompresi gambar; hindari kebocoran memori; gunakan alat pembuatan profil |
| **Pengurasan baterai** | Kurangi pekerjaan latar belakang; permintaan jaringan batch; gunakan layanan lokasi yang efisien |
| **Efisiensi jaringan** | Kompres muatan; gunakan penomoran halaman; cache secara agresif |
| **Pengguliran daftar** | Daur ulang tampilan; gunakan pemuatan lambat untuk gambar |
### Keamanan
| Kekhawatiran | Solusi |
|---------|----------|
| **Data tidak aktif** | Enkripsi data sensitif (Keychain di iOS, EncryptedSharedPreferences di Android) |
| **Jaringan** | Selalu HTTPS; penyematan sertifikat untuk aplikasi sensitif |
| **Otentikasi** | Biometrik (ID Wajah, sidik jari); OAuth; penyimpanan token |
| **Kebingungan kode** | ProGuard/R8 untuk Android; kode bit untuk iOS |
| **Jailbreak/deteksi root** | Deteksi perangkat yang disusupi; batasi fungsionalitas |
---

## Siklus Hidup Aplikasi
| Negara | Deskripsi | Apa yang Harus Dilakukan |
|-------|-------------|------------|
| **Latar depan (aktif)** | Pengguna sedang berinteraksi dengan aplikasi | Operasi normal |
| **Latar Belakang** | Aplikasi tidak terlihat tetapi masih ada di memori | Jeda animasi; simpan negara |
| **Ditangguhkan** | OS telah membekukan aplikasi untuk menghemat sumber daya | Tidak ada apa-apa; aplikasi dibekukan |
| **Dihentikan** | OS mematikan aplikasi untuk mengosongkan memori | Pulihkan status pada peluncuran berikutnya |
---

## Pemberitahuan Dorong
| Peron | Layanan | Protokol |
|----------|---------|----------|
| **iOS** | APN (layanan Pemberitahuan Push Apple) | HTTP/2 |
| **Android** | FCM (Firebase Cloud Messaging) | HTTP/v1 |
| Jenis Pemberitahuan | Deskripsi |
|-------------------|-------------|
| **Pemberitahuan data** | Diam; aplikasi memproses muatan | Pembaruan latar belakang |
| **Tampilkan notifikasi** | Ditampilkan di baki notifikasi | Peringatan pengguna |
| **Pemberitahuan kaya** | Menyertakan gambar, tindakan, atau UI khusus | Peningkatan keterlibatan pengguna |
---

## Distribusi Aplikasi
| Peron | Toko | Waktu Peninjauan | Pemotongan Pendapatan |
|----------|-------|-------------|-------------|
| **iOS** | Toko Aplikasi | 24-48 jam | 30% (15% untuk usaha kecil) |
| **Android** | Google Bermain | Jam ke hari | 30% (15% untuk $1 juta pertama) |
| **Android (alternatif)** | Toko Samsung Galaxy, Toko Aplikasi Amazon, F-Droid | Bervariasi | Bervariasi |
### CI/CD untuk Seluler
| Alat | Tujuan |
|------|---------|
| **Jalur Cepat** | Otomatiskan pembuatan, tangkapan layar, penandatanganan, dan penerapan |
| **Tindakan GitHub** | CI/CD dengan runner macOS untuk versi iOS |
| **Bitrise** | CI/CD yang berfokus pada seluler |
| **Pusat Aplikasi** (Microsoft) | Membangun, menguji, mendistribusikan (saat matahari terbenam; alternatif muncul) |
| **EAS** (Layanan Aplikasi Expo) | Cloud dibangun untuk React Native/Expo |
---

## Pengujian
| Ketik | Alat | Tujuan |
|------|-------|---------|
| **Uji unit** | JUnit, XCTest | Uji logika bisnis |
| **Tes widget** | Tes Widget Flutter, Roboelektrik | Uji komponen UI secara terpisah |
| **Tes integrasi** | Espresso (Android), XCUITest (iOS), Integrasi Flutter | Uji interaksi komponen |
| **Tes E2E** | Detoks, Appium, Maestro | Uji alur pengguna penuh pada perangkat nyata/simulasi |
| **Tes kinerja** | Profiler Android, Instrumen (iOS) | Ukur kecepatan bingkai, memori, CPU |
---

## Ringkasan
Pengembangan seluler menawarkan pilihan antara asli (kinerja terbaik, khusus platform) dan lintas platform (basis kode bersama, iterasi lebih cepat). Flutter dan React Native telah mencapai titik di mana lintas platform adalah pilihan yang tepat untuk sebagian besar aplikasi. Tantangan intinya tetap sama, apa pun kerangka kerjanya: desain yang mengutamakan offline, kinerja pada perangkat keras terbatas, efisiensi baterai, keamanan pada perangkat yang tidak tepercaya, dan menavigasi proses peninjauan toko aplikasi. Bidang ini memberikan penghargaan kepada pengembang yang memikirkan pengalaman pengguna terlebih dahulu — startup yang cepat, pengguliran yang lancar, dan penanganan konektivitas yang buruk dengan baik.