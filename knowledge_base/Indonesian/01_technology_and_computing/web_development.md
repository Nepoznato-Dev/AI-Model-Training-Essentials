# Pengembangan Web

## Pengembangan Bagian Depan

### Teknologi Inti

#### HTML (Bahasa Markup HiperTeks)
- **HTML Semantik**: Menggunakan tag yang bermakna (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Formulir**: Jenis input, validasi, label aksesibilitas
- **Media**: Penyematan gambar, video, audio
- **Meta Tag**: SEO, area pandang, pengkodean karakter
- **Fitur HTML5**: Kanvas, SVG, penyimpanan lokal, geolokasi, soket web

#### CSS (Lembar Gaya Bertingkat)
- **Model Kotak**: Konten, padding, batas, margin
- **Sistem Tata Letak**:
  - **Flexbox**: Tata letak satu dimensi, konten justifikasi, item penyelarasan
  - **Kisi**: Tata letak dua dimensi, templat kisi, area kisi
  - **Pemosisian**: Statis, relatif, absolut, tetap, melekat
- **Desain Responsif**: Kueri media, pendekatan yang mengutamakan seluler
- **Variabel CSS**: Properti khusus untuk tema
- **Animasi**: Transisi, bingkai utama, transformasi
- **Praprosesor**: Sass, Less (variabel, mixin, nesting)

####JavaScript
- **Manipulasi DOM**: Memilih, membuat, memodifikasi elemen
- **Acara**: Klik, kirim, keyboard, acara khusus, delegasi acara
- **Fitur ES6+**: Fungsi panah, penghancuran, penyebaran/istirahat, modul, async/menunggu
- **API**: Ambil, XMLHttpRequest, Penyimpanan lokal, Penyimpanan sesi
- **TypeScript**: Pengetikan statis, antarmuka, generik, dekorator

### Kerangka Frontend Modern

#### Bereaksi
- **Komponen**: Komponen fungsional, komponen kelas
- **Kait**: useState, useEffect, useContext, useReducer, kait khusus
- **Manajemen Negara**: API Konteks, Redux, Zustand, Recoil
- **Perutean**: React Router (BrowserRouter, Rute, Rute, Tautan)
- **Ekosistem**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Render efisien melalui algoritma diffing

#### Vue.js
- **API Opsi**: data, metode, komputasi, jam tangan
- **API Komposisi**: setup(), ref, reaktif, dihitung
- **Petunjuk**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: Manajemen negara
- **Vue Router**: Perutean sisi klien
- **Nuxt.js**: Kerangka rendering sisi server

#### Sudut
- **Komponen**: Dekorator, templat, kait siklus hidup
- **Layanan**: Injeksi ketergantungan, pola tunggal
- **RxJS**: Pemrograman reaktif, dapat diamati
- **Perutean**: RouterModule, penjaga, penyelesai
- **Formulir**: Formulir reaktif berdasarkan templat
- **NgRx**: Manajemen status bergaya Redux

### Alat Pembuatan dan Bundel
- **Webpack**: Bundling modul, pemisahan kode, pemuat, plugin
- **Vite**: Alat pembuatan cepat menggunakan modul ES asli
- **Parcel**: Bundle dengan konfigurasi nol
- **Rollup**: Dioptimalkan untuk perpustakaan
- **esbuild**: Pemaket JavaScript yang sangat cepat
- **Babel**: transpiler JavaScript untuk kompatibilitas mundur
- **PostCSS**: Pemrosesan CSS dengan plugin

### Kerangka dan Perpustakaan CSS
- **Bootstrap**: Pustaka komponen, sistem grid, utilitas
- **Tailwind CSS**: Kerangka kerja CSS yang mengutamakan utilitas
- **Material UI**: implementasi Desain Material Google
- **Chakra UI**: Pustaka komponen yang dapat diakses
- **Desain Semut**: Komponen UI tingkat perusahaan
- **Komponen Bergaya**: pustaka CSS-in-JS
- **Emosi**: CSS-in-JS dengan peta sumber

## Pengembangan Backend

### Bahasa Sisi Server

#### Node.js
- **Runtime**: JavaScript di server (mesin V8)
- **Express.js**: Kerangka web minimal, arsitektur middleware
- **NestJS**: Arsitektur yang terinspirasi sudut, TypeScript
- **Fastify**: Kerangka kerja berkinerja tinggi
- **Koa**: Modern Express oleh pencipta yang sama
- **Manajemen Paket**: npm, benang, pnpm

#### Piton
- **Django**: Kerangka berfitur lengkap, ORM, panel admin, termasuk baterai
- **Flask**: Microframework, ekosistem ekstensi
- **FastAPI**: Dokumentasi API modern, asinkron, dan otomatis
- **Piramida**: Kerangka kerja yang fleksibel dan terukur

#### Bahasa Backend Lainnya
- **Ruby on Rails**: Konvensi mengenai konfigurasi, ActiveRecord ORM
- **Java Spring**: Kerangka kerja perusahaan, injeksi ketergantungan
- **PHP Laravel**: Sintaks yang elegan, ORM yang fasih, templating Blade
- **Go Gin**: Performa tinggi, kerangka minimal
- **Rust Actix**: Keamanan memori, kinerja
- **C# ASP.NET Core**: Fitur perusahaan lintas platform

### Integrasi Basis Data

#### ORM (Pemetaan Relasional Objek)
- **Sequelize**: Node.js ORM untuk database SQL
- **Prisma**: Akses database yang aman untuk tipe, klien yang dibuat secara otomatis
- **SQLAlchemy**: Perangkat Python SQL dan ORM
- **Catatan Aktif**: Ruby on Rails ORM
- **Hibernasi**: Java ORM
- **Kerangka Entitas**: .NET ORM

#### Driver Basis Data
- **hal**: Klien PostgreSQL untuk Node.js
- **mysql2**: Klien MySQL dengan janji
- **pymongo**: driver MongoDB untuk Python
- **redis**: Klien Redis untuk berbagai bahasa

### Pengembangan API#### REST API
- **Metode HTTP**: DAPATKAN, POST, PUT, PATCH, HAPUS
- **Kode Status**: 200, 201, 400, 401, 403, 404, 500
- **Penamaan Sumber Daya**: Kata benda, jamak, hierarkis
- **Pembuatan versi**: jalur URL, header, parameter kueri
- **Otentikasi**: JWT, OAuth, kunci API
- **Dokumentasi**: OpenAPI/Swagger, Tukang Pos

#### GrafikQL
- **Definisi Skema**: Jenis, kueri, mutasi, langganan
- **Resolver**: Pengambilan data tingkat lapangan
- **Server Apollo**: Implementasi server GraphQL
- **Relai**: klien GraphQL Facebook
- **Kelebihan**: Tidak ada pengambilan berlebihan, titik akhir tunggal, pengetikan kuat

#### gRPC
- **Buffer Protokol**: Bahasa definisi antarmuka
- **HTTP/2**: Streaming dua arah
- **Kasus Penggunaan**: Komunikasi layanan mikro, aplikasi waktu nyata

### Otentikasi dan Otorisasi
- **Berbasis sesi**: Cookie, sesi sisi server
- **Berbasis token**: JWT (JSON Web Tokens), tanpa kewarganegaraan
- **OAuth 2.0**: Kerangka otorisasi, login pihak ketiga
- **OpenID Connect**: Lapisan identitas di OAuth 2.0
- **SAML**: Sistem masuk tunggal perusahaan
- **Pencirian Kata Sandi**: bcrypt, argon2, scrypt
- **Otentikasi Multi-Faktor**: TOTP, SMS, kode email

## DevOps dan Penerapan

### Kontrol Versi
- **Git**: Kontrol versi terdistribusi
- **GitHub/GitLab/Bitbucket**: Hosting repositori
- **Strategi Percabangan**: Git Flow, GitHub Flow, pengembangan berbasis trunk
- **CI/CD**: Jalur pengujian dan penerapan otomatis

### Kontainerisasi
- **Docker**: Waktu proses container, Dockerfile, gambar
- **Docker Compose**: Orkestrasi multi-kontainer
- **Registrasi Kontainer**: Docker Hub, AWS ECR, Google GCR
- **Praktik Terbaik**: Pembuatan multi-tahap, gambar dasar minimal

### Orkestrasi
- **Kubernetes**: Orkestrasi container, pod, layanan, penerapan
- **Helm**: Manajer paket Kubernetes
- **Service Mesh**: Istio, Linkerd untuk jaringan layanan mikro

### Platform Awan
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Mesin Komputasi, Penyimpanan Cloud, Fungsi Cloud, GKE
- **Azure**: Mesin Virtual, Penyimpanan Blob, Fungsi, AKS
- **Vercel**: Penerapan frontend, fungsi tanpa server
- **Netlify**: Hosting situs statis, fungsi tanpa server
- **Heroku**: Platform sebagai Layanan (PaaS)
- **DigitalOcean**: Infrastruktur cloud yang disederhanakan

### Saluran Pipa CI/CD
- **Tindakan GitHub**: Otomatisasi alur kerja
- **GitLab CI**: Integrasi berkelanjutan bawaan
- **Jenkins**: Server otomatisasi yang dapat diperluas
- **CircleCI**: CI/CD berbasis cloud
- **Travis CI**: Layanan integrasi berkelanjutan
- **ArgoCD**: Pengiriman berkelanjutan GitOps untuk Kubernetes

### Pemantauan dan Pencatatan
- **Kinerja Aplikasi**: Relik Baru, Datadog, AppDynamics
- **Pelacakan Kesalahan**: Penjaga, Rollbar, Bugsnag
- **Logging**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Pemantauan Waktu Aktif**: Pingdom, UptimeRobot
- **Analitik**: Google Analytics, Mixpanel, Amplitudo

## Performa Web

### Teknik Optimasi
- **Pemisahan Kode**: Pemuatan lambat, impor dinamis
- **Pohon Gemetar**: Menghapus kode yang tidak digunakan
- **Minifikasi**: Mengurangi ukuran file
- **Kompresi**: Gzip, Brotli
- **Caching**: Cache browser, CDN, pekerja layanan
- **Optimasi Gambar**: WebP, AVIF, pemuatan lambat, gambar responsif
- **CSS Kritis**: Menyisipkan gaya paruh atas
- **Pengoptimalan Basis Data**: Pengindeksan, pengoptimalan kueri, pengumpulan koneksi

### Data Web Inti
- **LCP (Cat Berisi Terbesar)**: Performa pemuatan (<2,5 detik)
- **FID (Penundaan Input Pertama)**: Interaktivitas (<100 md)
- **CLS (Pergeseran Tata Letak Kumulatif)**: Stabilitas visual (<0,1)
- **INP (Interaksi ke Cat Berikutnya)**: Metrik Responsif

### Jaringan Pengiriman Konten (CDN)
- **Cloudflare**: Keamanan, kinerja, DNS
- **Akamai**: CDN Perusahaan
- **Amazon CloudFront**: AWS CDN
- **Dengan cepat**: Platform cloud tepi
- **StackPath**: Layanan tepi

## Keamanan Web

### Kerentanan Umum (10 Teratas OWASP)
- **Injeksi**: Injeksi SQL, injeksi perintah
- **Otentikasi Rusak**: Pembajakan sesi, penjejalan kredensial
- **Paparan Data Sensitif**: Data tidak terenkripsi, kriptografi lemah
- **Entitas Eksternal XML (XXE)**: Kerentanan parser XML
- **Kontrol Akses Rusak**: Peningkatan hak istimewa, akses tidak sah
- **Kesalahan Konfigurasi Keamanan**: Kredensial default, kesalahan verbose
- **Cross-Site Scripting (XSS)**: Tercermin, disimpan, berbasis DOM
- **Deserialisasi Tidak Aman**: Serangan injeksi objek
- **Menggunakan Komponen dengan Kerentanan yang Diketahui**: Dependensi yang sudah ketinggalan jaman
- **Pencatatan & Pemantauan Tidak Memadai**: Pelanggaran tidak terdeteksi

### Praktik Terbaik Keamanan
- **HTTPS**: Enkripsi TLS/SSL, HSTS
- **Kebijakan Keamanan Konten (CSP)**: Mencegah serangan XSS
- **Validasi Input**: Membersihkan input pengguna
- **Pengkodean Keluaran**: Mencegah serangan injeksi
- **Perlindungan CSRF**: Token anti-CSRF, cookie SameSite
- **Pembatasan Nilai**: Mencegah serangan brute force
- **Header Keamanan**: Opsi-Bingkai-X, Opsi-Jenis-Konten-X
- **Pemindaian Ketergantungan**: audit npm, Snyk, Dependabot

## Pengujian### Jenis Pengujian
- **Pengujian Unit**: Komponen/fungsi individual
- **Pengujian Integrasi**: Interaksi komponen
- **End-to-End (E2E)**: Alur kerja pengguna penuh
- **Regresi Visual**: Deteksi perubahan UI
- **Pengujian Kinerja**: Pengujian beban, tegangan, lonjakan
- **Pengujian Aksesibilitas**: Kepatuhan WCAG

### Kerangka Pengujian
- **Jest**: Kerangka pengujian JavaScript
- **Mocha**: Pelari tes yang fleksibel
- **pytest**: Kerangka pengujian Python
- **RSpec**: Kerangka pengujian Ruby
- **JUnit**: Kerangka pengujian Java

### Alat Pengujian E2E
- **Selenium**: Otomatisasi browser
- **Cypress**: Pengujian E2E modern
- **Penulis drama**: Otomatisasi lintas browser
- **Dalang**: Kontrol Chrome tanpa kepala

## Aksesibilitas (a11y)

### Pedoman WCAG
- **Dapat Dipahami**: Alternatif teks, keterangan, konten yang dapat disesuaikan
- **Dapat dioperasikan**: Navigasi keyboard, waktu cukup, tidak ada kejang
- **Dapat dimengerti**: Bantuan masukan yang dapat dibaca dan diprediksi
- **Kuat**: Kompatibel dengan teknologi bantu

### Implementasi
- **HTML Semantik**: Hierarki judul yang tepat, landmark
- **Atribut ARIA**: Peran, status, properti
- **Manajemen Fokus**: Indikator fokus terlihat, urutan tab logis
- **Kontras Warna**: Rasio minimum 4,5:1 untuk teks
- **Pengujian Pembaca Layar**: NVDA, JAWS, VoiceOver
- **Navigasi Keyboard**: Semua elemen interaktif dapat diakses

## Aplikasi Web Progresif (PWA)

### Fitur PWA
- **Pekerja Layanan**: Fungsi offline, sinkronisasi latar belakang
- **Manifes Aplikasi Web**: Perintah penginstalan, ikon, warna tema
- **App Shell**: Kerangka UI dalam cache
- **Pemberitahuan Push**: Keterlibatan pengguna
- **Desain Responsif**: Berfungsi di semua perangkat
- **HTTPS Diperlukan**: Konteks aman

### Alat
- **Kotak Kerja**: Pustaka pekerja layanan
- **Mercusuar**: Audit PWA
- **PWA Builder**: Menghasilkan manifes dan ikon

## Teknologi Baru

### WebAssembly (Wasm)
- **Tujuan**: Menjalankan kode yang dikompilasi di browser dengan kecepatan mendekati aslinya
- **Bahasa**: Target kompilasi C++, Rust, Go
- **Kasus Penggunaan**: Game, pengeditan video, kriptografi, inferensi ML

### Arsitektur Tanpa Server
- **Fungsi sebagai Layanan**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Manfaat**: Tidak ada manajemen server, penskalaan otomatis, bayar per penggunaan
- **Pertimbangan**: Cold start, vendor lock-in, kerumitan proses debug

### Arsitektur Jamstack
- **JavaScript**: Interaktivitas sisi klien
- **API**: Fungsi tanpa server, layanan pihak ketiga
- **Markup**: File statis bawaan
- **Alat**: Next.js, Gatsby, Hugo, Eleventy
- **Manfaat**: Kinerja, keamanan, skalabilitas, pengalaman pengembang

### Komunikasi Waktu Nyata
- **WebSockets**: Komunikasi dua arah
- **Acara Terkirim Server**: Streaming server-ke-klien
- **WebRTC**: Video, audio, data peer-to-peer
- **Kasus Penggunaan**: Obrolan, kolaborasi, streaming langsung, bermain game

### Frontend Mikro
- **Konsep**: Perluas layanan mikro ke frontend
- **Pendekatan**: Waktu pembuatan, waktu proses, integrasi sisi tepi
- **Manfaat**: Penerapan independen, otonomi tim
- **Tantangan**: Konsistensi, kinerja, kompleksitas