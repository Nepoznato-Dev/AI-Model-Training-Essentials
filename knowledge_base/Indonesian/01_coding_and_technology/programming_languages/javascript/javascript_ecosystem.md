<!--
---
# Metadata
title: "JavaScript — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the JavaScript ecosystem including package managers, build tools, testing frameworks, linters, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [javascript, ecosystem, tooling, npm, node, testing, ide, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "20 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# JavaScript — Panduan Ekosistem & Peralatan
Panduan ini mencakup alat, kerangka kerja, dan infrastruktur penting dalam ekosistem JavaScript.
---

## Waktu proses
| Waktu proses | Lingkungan | Terbaik Untuk |
|---------|-------------|----------|
| **Node.js** | Server/CLI | Backend, API, perkakas |
| **Deno** | Server/CLI | Aman secara default, TypeScript asli |
| **Roti** | Server/CLI | Bundler/test runner bawaan yang cepat |
| **Peramban** | Sisi klien | Aplikasi web |
---

## Manajemen Paket
| Alat | Registri | Fitur |
|------|----------|----------|
| **npm** | npmjs.com | Default dengan Node.js |
| **benang** | npmjs.com | Ruang kerja, mode PnP |
| **pnpm** | npmjs.com | Cepat, hemat disk, ketat |
| **sanggul** | npmjs.com | Sangat cepat, bawaan |
```bash
npm init -y                   # initialize project
npm install express           # add dependency
npm install -D typescript     # add dev dependency
npm run build                 # run script from package.json
```

---

## Bangun Alat & Bundel
| Alat | Ketik | Terbaik Untuk |
|------|------|----------|
| **Sangat** | Bundel | Server pengembang cepat, modern |
| **membangun** | Bundel | Sangat cepat, berbasis Go |
| **paket web** | Bundel | Dewasa, sangat dapat dikonfigurasi |
| **Gabungan** | Bundel | Perpustakaan, pengguncangan pohon |
| **Paket** | Bundel | Konfigurasi nol |
| **Turbopack** | Bundel | Next.js, berbasis Rust |
| **SWC** | Kompiler | TypeScript/JSX Cepat |
| **Babel** | Kompiler | Transpilasi, plugin |
---

## Kerangka kerja
### Bagian depan
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **Bereaksi** | Perpustakaan UI | UI berbasis komponen, ekosistem |
| **Vue** | Progresif | Mudah didekati, DX hebat |
| **Ringan** | Kompiler | Waktu proses minimal, cepat |
| **Sudut** | Kerangka penuh | Perusahaan, TypeScript-pertama |
| **Padat** | Reaktif | Reaktivitas berbutir halus |
| **Astro** | Statis/SSR | Situs konten, pulau |
### Bagian belakang
| Kerangka | Ketik | Terbaik Untuk |
|-----------|------|----------|
| **Ekspres** | Mikro | API sederhana, middleware |
| **Percepat** | Kinerja | API throughput tinggi |
| **NestJS** | Perusahaan | Terstruktur, DI, TypeScript |
| **Hono** | Tepi | Ringan, multi-waktu proses |
| **Koa** | Modern | Penerus ekspres |
---

## Pengujian
| Kerangka | Ketik |
|-----------|------|
| **Kunjungan** | Cepat, Vite-asli |
| **Lelucon** | Dewasa, pengujian snapshot |
| **Penulis drama** | E2E, multi-peramban |
| **cemara** | E2E, pengalaman pengembang |
| **Perpustakaan Pengujian** | Pengujian komponen |
| **Moka** | Fleksibel, berbasis plugin |
```bash
vitest                        # run tests
vitest --coverage             # with coverage
playwright test               # E2E tests
```

---

## Kualitas Kode
| Alat | Tujuan |
|------|---------|
| **ESLint** | Linter (aturan yang dapat dikonfigurasi) |
| **Lebih cantik** | Pemformat kode |
| **Bioma** | Linter + formatter cepat (Karat) |
| **Skrip Ketik** | Pemeriksaan tipe statis |
| **pola-ts** | Pencocokan pola untuk TS |
```json
// eslint.config.js (flat config)
export default [
  { rules: { "no-unused-vars": "warn" } }
];
```

---

## IDE & Editor
| IDE | Kekuatan |
|-----|-----------|
| **Kode VS** | Dukungan JS/TS yang dominan dan luar biasa |
| **WebStorm** | IDE JetBrains berfitur lengkap |
| **Kursor** | Garpu VS Code bertenaga AI |
| **Neovim** | Berbasis terminal dengan LSP |
---

## Penerapan
| Peron | Ketik |
|----------|------|
| **Vercel** | Frontend/Tanpa Server (Next.js) |
| **Netlifikasi** | Bagian Depan/Jamstack |
| **Pekerja Cloudflare** | Komputasi tepi |
| **Kereta Api** | PaaS tumpukan penuh |
| **Terbang.io** | Hosting aplikasi, global |
| **AWS Lambda** | Tanpa server |
| **Buruh pelabuhan** | dalam kontainer |
---

## Ringkasan
Ekosistem JavaScript adalah yang terbesar dalam pemrograman. Tumpukan modernnya adalah: **Vite** untuk pembuatan, **pnpm** untuk paket, **Vitest** untuk pengujian, **ESLint + Prettier** untuk kualitas kode, **React/Next.js** atau **Vue/Nuxt** untuk frontend, dan **Vercel** atau **Cloudflare** untuk penerapan. TypeScript sekarang penting untuk proyek serius apa pun. Ekosistem bergerak cepat — tetap mengikuti perkembangan namun menghindari pergantian kerangka kerja.