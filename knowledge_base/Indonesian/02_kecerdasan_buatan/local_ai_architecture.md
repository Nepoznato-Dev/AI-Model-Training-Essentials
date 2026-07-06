# Arsitektur AI Lokal

Panduan praktis untuk menjalankan model bahasa besar sepenuhnya pada perangkat — pertimbangan perangkat keras, mesin inferensi, optimalisasi memori, dan desain sistem untuk penerapan edge.

---

## Mengapa Menjalankan AI Secara Lokal?

- **Privasi**: Tidak ada data yang keluar dari perangkat.
- **Biaya**: Tidak ada biaya API per token.
- **Latensi**: Inferensi bebas jaringan yang dapat diprediksi.
- **Ketersediaan offline**: Bekerja tanpa internet.
- **Kontrol**: Kontrol penuh atas versi model, penyesuaian, dan penyesuaian.

---

## Persyaratan Perangkat Keras

### Memori GPU (VRAM)
Sumber daya yang paling penting. Ukuran model dalam memori ≈ **parameter × byte per parameter**.

| Presisi | Byte per parameter | model 3,8B | model 7B | model 13B | Model 70B |
|-----------|---------------------|------------|----------|-----------|-----------|
| FP32 | 4 | ~15 GB | ~28 GB | ~52GB | ~280 GB |
| FP16 | 2 | ~7,6GB | ~14 GB | ~26 GB | ~140GB |
| INT8 (8-bit) | 1 | ~3,8 GB | ~7 GB | ~13GB | ~70GB |
| INT4 (4-bit) | 0,5 | ~1,9GB | ~3,5 GB | ~6,5 GB | ~35 GB |

**Pedoman praktis:**
- VRAM 8GB → hingga model 7B pada 4-bit.
- VRAM 12GB → hingga model 13B pada 4-bit.
- VRAM 24GB → hingga model 70B pada 4-bit (atau 13B pada 8-bit).
- Apple Silicon (memori terpadu) dapat menjalankan model 70B pada sistem 64GB+.

### RAM (Memori Sistem)
- Untuk inferensi CPU, Anda memerlukan RAM sistem yang cukup untuk memuat model (mirip dengan nomor VRAM).
- Untuk inferensi GPU, RAM sistem penting untuk memuat model ke dalam memori sebelum memindahkannya ke VRAM.

### Penyimpanan
- Bobot model terkuantifikasi memerlukan beberapa GB (misalnya, 4-bit 7B ≈ 4 GB pada disk). Pastikan setidaknya 20–50 GB gratis untuk beberapa model.

### CPU
- Untuk pemrosesan cepat (pengisian awal) dan pembongkaran CPU, CPU multi-core modern membantu.
- Chip Apple seri M memiliki kinerja luar biasa untuk LLM karena memori terpadu dan Mesin Neural.

---

## Kuantisasi

Kuantisasi mengurangi presisi numerik bobot, mengurangi memori secara drastis, dan meningkatkan kecepatan dengan biaya akurasi yang kecil.

### Format Populer

| Format | Bit | Deskripsi | Penggunaan khas |
|--------|------|-------------|-------------|
| **GGUF** | 4–8 | Format llama.cpp, dioptimalkan untuk CPU/GPU hybrid | Terbaik untuk inferensi lokal |
| **GPTQ** | 4–8 | Khusus GPU, efisien di CUDA | Terbaik untuk GPU NVIDIA |
| **AWQ** | 4 | Sadar aktivasi, khusus GPU | Bagus untuk inferensi batch pada GPU |
| **ONNX** | variabel | Terstandarisasi, lintas platform | Penyajian produksi |

### Memilih Tingkat Kuantisasi
- **Q8_0** (8-bit): kehilangan kualitas minimal, ukuran terbesar.
- **Q6_K** (6-bit): kualitas bagus, kompresi lumayan.
- **Q5_K_M** (5-bit): titik manis yang umum.
- **Q4_K_M** (4-bit): kualitas terkecil dan dapat diterima untuk sebagian besar tugas.
- **IQ4_XS** / **IQ3_XS**: Peningkatan kuantisasi dengan kebingungan yang lebih baik pada 4/3 bit.

**Aturan praktis:** Gunakan Q4_K_M untuk keseimbangan kualitas dan ukuran yang baik. Jika Anda memiliki VRAM tambahan, gunakan Q5 atau Q6.

---

## Mesin Inferensi (Lokal)

### llama.cpp
- Ditulis dalam C++.
- Mendukung format GGUF.
- Dioptimalkan untuk CPU dan GPU (melalui CUDA, Metal, OpenCL).
- Sangat cepat, terutama pada CPU.
- Baris perintah, mode server, dan pengikatan Python.

**Contoh perintah:**
```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
(-ngl 32 offloads 32 layers to GPU)

Ollama
Wraps llama.cpp with a simple CLI and REST API.

Auto-downloads models, manages them.

Great for prototyping and desktop apps.

Supports custom Modelfiles for system prompts.

Usage:

bash
ollama run phi3:3.8b
ollama run llama3:8b
LM Studio
Graphical desktop app for Windows, macOS, Linux.

One-click download and chat interface.

Built-in local server with OpenAI-compatible API.

Good for non-technical users and quick testing.

Hugging Face Transformers + bitsandbytes
The standard Python library for HF models.

Use bitsandbytes for 4-bit quantisation (load_in_4bit=True).

More flexible for fine-tuning but slower than llama.cpp for inference.

ExLlamaV2
Very fast GPU inference for GPTQ and AWQ.

Best performance on NVIDIA GPUs.

Supports batched generation.

mlx (Apple)
Apple's framework for M-series chips.

Highly optimised for Apple Silicon.

Python API.

Memory Management
Context Window and KV Cache
The KV cache stores key-value pairs for every layer and every token in the context. It grows linearly with context length.

Memory cost ≈ 2 × layers × (KV heads × head dim) × tokens × bytes per value

For a 32-layer model with 8 KV heads and 128 head dim, each token costs ~32 × 8 × 128 × 2 bytes = 65 KB per token. For 128k tokens, that's ~8 GB just for the cache.

Offloading Strategies
Layer offloading: Put some layers on GPU, others on CPU. Faster than pure CPU, lower VRAM requirement.

Token streaming: Process tokens incrementally rather than all at once.

Prompt Caching
Reuse KV caches across similar prompts to avoid recomputing the prefill phase. Some frameworks support this (e.g., vLLM, llama.cpp with --prompt-cache).

Memory-Mapped Files
Load model weights directly from disk without loading them entirely into RAM (useful for huge models on memory-limited systems). llama.cpp uses memory-mapping by default.

Deployment Architectures
Single-Device Mode
One model runs on one machine (laptop, smartphone, edge device). Used for personal assistants, note-taking apps, code completion.

Hybrid Edge-Cloud
Local model handles common queries; fallback to a cloud model for complex questions. This gives the best of both worlds — speed/private for most, capability for edge cases.

Distributed Inference (Multi-GPU)
For larger models, split layers across multiple GPUs (tensor parallelism) or split context across devices (pipeline parallelism). Use llama.cpp with -ngl or ExLlamaV2 with --num-gpu-layers.

Mobile Deployment
Android: Use llama.cpp via JNI bindings or ML Kit.

iOS: Use llama.cpp via Swift bindings or mlx.

Web: Use WebLLM (runs on WebGPU via ONNX runtime) or transformers.js.

Performance Optimisation
Flash Attention
Speeds up attention computation and reduces memory usage. Available in llama.cpp, ExLlamaV2, and modern transformers libraries.

Batch Inference
Process multiple prompts in a single forward pass. Increases throughput dramatically. Use llama-batch or vLLM.

Early Stopping / Token Budgeting
Set a maximum token budget to prevent unbounded generation.

Speculative Decoding
Use a small fast model (draft) to predict tokens, then verify with the large model in parallel. Can yield 2–3× speedup.

Practical Setup Guide
1. Install Ollama
bash
curl -fsSL https://ollama.com/install.sh | sh
2. Pull a Model
bash
ollama pull phi3:3.8b-q4_K_M
3. Run with API
bash
ollama serve
Then send requests to http://localhost:11434/api/generate.

4. Python Integration
python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
5. (Alternative) Use llama.cpp directly
bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
Monitoring and Observability
Track GPU utilisation (nvidia-smi on Linux, Activity Monitor on macOS).

Track memory usage (RAM and VRAM).

Track tokens per second (throughput).

Track time to first token (latency).

Use built-in logging from llama.cpp or Ollama.

Limitations and Tradeoffs
Quality gap: Small local models (3.8B–7B) generally underperform large cloud models (GPT-4, Claude 3.5) on complex reasoning.

Knowledge cutoff: Model knowledge is frozen at training time; use RAG to inject current information.

Multilingual: Smaller models may have less multilingual capability.

Tool use: Agentic workflows (function calling) may be less reliable on small models.

For many everyday tasks (summarisation, Q&A, code completion, classification), local models are already sufficient and improving rapidly.

text

---

## File 4: `security_best_practices.md`

```penurunan harga
# Praktik Terbaik Keamanan

Panduan praktis untuk mengamankan aplikasi, infrastruktur, dan data — mulai dari pengembangan hingga produksi.

---

## OWASP 10 Teratas (2021) — Ikhtisar

1. **Kontrol Akses Rusak**: Pengguna dapat mengakses sumber daya yang tidak seharusnya.
2. **Kegagalan Kriptografi**: Enkripsi lemah atau hilang.
3. **Injeksi**: SQL, NoSQL, perintah OS, atau injeksi LDAP.
4. **Desain Tidak Aman**: Cacat arsitektur.
5. **Kesalahan Konfigurasi Keamanan**: Kata sandi default, port terbuka, kesalahan verbose.
6. **Komponen Rentan dan Kedaluwarsa**: CVE yang diketahui berada dalam ketergantungan.
7. **Kegagalan Identifikasi dan Otentikasi**: Kata sandi lemah, salah urus sesi.
8. **Kegagalan Integritas Perangkat Lunak dan Data**: Serangan rantai pasokan, pembaruan yang tidak ditandatangani.
9. **Kegagalan Pencatatan dan Pemantauan Keamanan**: Tidak ada deteksi pelanggaran.
10. **Pemalsuan Permintaan Sisi Server (SSRF)**: Penyalahgunaan server untuk membuat permintaan ke sistem internal.

---

## Validasi Masukan dan Pengkodean Keluaran

### Aturan Validasi
- **Daftar Putih > Daftar Hitam**: Menentukan pola yang diizinkan (misalnya, regex untuk email) daripada memblokir pola buruk yang diketahui.
- **Batas panjang**: Menerapkan panjang maksimum untuk mencegah buffer overflow dan DoS.
- **Pemeriksaan jenis**: Pastikan bilangan bulat adalah bilangan bulat, boolean adalah boolean.
- **Gunakan pustaka yang telah teruji**: Untuk validasi email, URL, dan tanggal, gunakan pustaka standar (misalnya, `email-validator` dengan Python, `validator.js` di Node).### Pengkodean Keluaran
- **Pengkodean HTML**: Enkode `<`, `>`, `&`, `"`, `'` untuk mencegah XSS.
- **Parameterisasi SQL**: Jangan pernah menggabungkan input pengguna ke dalam kueri SQL. Gunakan kueri berparameter (pernyataan yang disiapkan) atau ORM.
- **Shell escape**: Hindari membuat perintah shell dari input pengguna; jika tidak dapat dihindari, gunakan `shlex.quote()` atau serupa.

---

## Otentikasi dan Otorisasi

### Manajemen Kata Sandi
- **Hashing**: Menyimpan kata sandi dengan algoritma hashing yang kuat dan lambat: **Argon2id** (lebih disukai), **bcrypt**, **scrypt**, atau **PBKDF2**.
- **Salting**: Tambahkan garam unik per pengguna.
- **Panjang minimum**: Terapkan setidaknya 12–16 karakter.
- **MFA (Otentikasi Multi-Faktor)**: Memerlukan faktor kedua (TOTP, SMS, kunci perangkat keras) untuk operasi sensitif.
- **Pembatasan kecepatan**: Mencegah upaya brute force pada titik akhir login (misalnya, 5 upaya per 5 menit per IP/pengguna).

### Manajemen Sesi
- Gunakan cookie SameSite yang aman, khusus HTTP, untuk token sesi.
- Tetapkan waktu kedaluwarsa yang sesuai.
- Membatalkan sesi saat logout dan perubahan kata sandi.
- Hindari mengekspos ID sesi di URL.

### OAuth2 / OIDC
- Gunakan perpustakaan yang sudah mapan (misalnya, Authlib, PyJWT, Passport.js, Spring Security).
- Validasi token ID secara menyeluruh (tanda tangan, penerbit, audiens, kedaluwarsa).
- Gunakan parameter status untuk mencegah CSRF.
- Jaga kerahasiaan rahasia klien.

### JWT (Token Web JSON)
- **Tanda**: Gunakan RS256 atau ES256 (asimetris) untuk keamanan yang lebih baik; HS256 (simetris) dapat diterima jika rahasia bersama dikelola dengan baik.
- **Validasi**: Selalu verifikasi tanda tangan, penerbit (`iss`), audiens (`aud`), dan kedaluwarsa (`exp`).
- **Jaga masa berlakunya tetap pendek**: 15–60 menit untuk token akses; gunakan token penyegaran untuk sesi yang lebih lama.
- **Simpan dengan aman**: Jangan pernah menyimpan JWT di Penyimpanan lokal (rentan terhadap XSS); gunakan cookie khusus HTTP saja.

---

## Keamanan API

### Otentikasi
- Selalu autentikasi panggilan API (kecuali titik akhir publik).
- Lebih memilih kunci API atau token OAuth2 daripada autentikasi dasar (yang mengirimkan kredensial pada setiap permintaan).

### Pembatasan dan Pembatasan Tarif
- Terapkan batas kecepatan per pengguna dan per IP untuk mencegah penyalahgunaan dan DoS.
- Kembalikan `429 Too Many Requests` dengan header `Retry-After`.

### CORS (Berbagi Sumber Daya Lintas Asal)
- Hanya mengizinkan asal tertentu (tidak pernah `*` dalam produksi).
- Validasi header `Origin` di sisi server.

### Validasi Masukan
- Validasi semua parameter permintaan, termasuk header dan isi.
- Tolak kolom yang tidak diharapkan (`"strict": true` atau `additionalProperties: false` dalam Skema JSON).

### HTTPS/TLS
- Terapkan HTTPS dalam produksi.
- Gunakan HSTS (HTTP Strict Transport Security) untuk memaksa browser menggunakan HTTPS.
- Gunakan TLS 1.2 atau 1.3 (nonaktifkan TLS 1.0/1.1).

---

## Manajemen Rahasia

### Jangan Pernah Rahasia Hardcode
- Jangan memasukkan rahasia (kunci API, kata sandi, URL basis data) ke kontrol sumber.
- Gunakan variabel lingkungan atau alat manajemen rahasia.

### Alat
- **HashiCorp Vault**: Rahasia dinamis tingkat perusahaan.
- **AWS Secrets Manager / Azure Key Vault / GCP Secret Manager**: Cloud-asli.
- **SOPS**: Enkripsi rahasia dalam file dan komit (dengan KMS atau GPG).
- **Rahasia Docker**: Untuk mode Swarm; Rahasia Kubernetes (dikodekan base64, tetapi gunakan dengan hati-hati; pertimbangkan driver CSI Secrets Store eksternal).

### Rotasi
- Rotasi rahasia dan akun layanan secara teratur.
- Otomatiskan rotasi jika memungkinkan.

---

## Manajemen Ketergantungan

### Pemindaian Kerentanan
- **Python**: `safety`, `pip-audit`, `bandit`.
- **Node**: `npm audit`, `yarn audit`, `snyk`.
- **Karat**: `cargo audit`.
- **Ayo**: `govulncheck`.
- **Umum**: `Dependabot` (GitHub), `Renovate`, `Trivy`.

### Menambal
- Terus perbarui dependensi ke versi yang ditambal.
- Mengatur permintaan penarikan otomatis untuk pembaruan kecil/tambalan.
- Tinjau log perubahan untuk mengetahui perubahan yang dapat terjadi.

### Integritas Rantai Pasokan
- Gunakan file kunci paket (`package-lock.json`, `Cargo.lock`, `go.sum`) untuk memastikan build yang dapat direproduksi.
- Verifikasi checksum dari dependensi yang diunduh.
- Lebih memilih pendaftar resmi dan hanya mempercayai penerbit terverifikasi.

---

## Keamanan Infrastruktur

### Firewall
- Blokir semua port masuk kecuali yang diperlukan secara eksplisit (mis., 80, 443).
- Batasi akses SSH pada rentang IP tertentu (atau gunakan VPN/bastion host).
- Gunakan grup keamanan (AWS) atau NSG (Azure) untuk kontrol yang lebih detail.

### Pengerasan OS
- Terapkan pembaruan keamanan secara berkala (`sudo apt upgrade`, `yum update`).
- Nonaktifkan layanan yang tidak perlu dan akun default.
- Gunakan fail2ban untuk memblokir upaya brute force pada SSH.
- Perkuat SSH: nonaktifkan login root, gunakan autentikasi berbasis kunci, ubah port default (opsional).### Segmentasi Jaringan
- Tempatkan database dan cache di subnet pribadi tanpa akses internet.
- Gunakan DMZ untuk layanan publik.
- Menerapkan prinsip hak istimewa paling rendah pada akses jaringan.

### Rahasia dalam Infrastruktur
- Jangan pernah menyimpan rahasia dalam variabel lingkungan CI/CD kecuali dienkripsi.
- Gunakan peran IAM penyedia cloud untuk instans EC2/VM, bukan kunci yang berumur panjang.

---

## Pencatatan dan Pemantauan

### Apa yang Harus Dicatat
- Peristiwa otentikasi (berhasil/gagal).
- Keputusan kontrol akses (kegagalan otorisasi).
- Tindakan Admin (pembuatan pengguna, penghapusan, perubahan izin).
- Perubahan skema database.
- Kesalahan dan pengecualian sistem.
- Permintaan dan tanggapan API (menyunting data sensitif).

### Yang Tidak Perlu Dicatat
- Kata sandi, rahasia, token, PII (Informasi Identifikasi Pribadi) kecuali di-hash/disunting.
- Nomor kartu kredit lengkap.

### Peringatan
- Atur peringatan untuk:
  - Beberapa login gagal (potensi kekerasan).
  - Pola akses yang tidak biasa (misalnya dari lokasi baru, pada jam-jam ganjil).
  - Akun admin baru dibuat.
  - Tingkat kesalahan tinggi atau lonjakan latensi.
- Gunakan SIEM (Informasi Keamanan dan Manajemen Acara) untuk korelasi tingkat lanjut.

### Retensi Log
- Simpan log setidaknya selama 30–90 hari tergantung pada persyaratan peraturan.
- Simpan log dalam sistem terpusat dan anti kerusakan (mis., ELK Stack, Splunk, Datadog).

---

## Siklus Hidup Pengembangan Aman (SDL)

1. **Pelatihan**: Pastikan pengembang memahami kerentanan umum.
2. **Pemodelan ancaman**: Identifikasi potensi ancaman di awal desain.
3. **Standar pengkodean yang aman**: Ditegakkan melalui linter dan daftar periksa peninjauan kode.
4. **SAST** (Pengujian Keamanan Aplikasi Statis): Pindai kode sumber untuk mencari kerentanan (SonarQube, CodeQL).
5. **DAST** (Pengujian Keamanan Aplikasi Dinamis): Memindai aplikasi yang sedang berjalan (OWASP ZAP, Burp Suite).
6. **SCA** (Analisis Komposisi Perangkat Lunak): Memindai dependensi.
7. **Pengujian penetrasi**: Latihan peretasan etis secara teratur.
8. **Bug bounty**: Mendorong peneliti eksternal untuk menemukan kerentanan secara bertanggung jawab.
9. **Rencana respons insiden**: Miliki rencana yang jelas ketika pelanggaran terdeteksi.

---

## Daftar Periksa Darurat (Bila Diduga Ada Pelanggaran)

1. **Jangan panik** — tetapi bertindak cepat.
2. **Isolasi** sistem yang terkena dampak (putuskan sambungan dari jaringan jika diperlukan).
3. **Simpan bukti**: Ambil log, dump memori, dan image disk.
4. **Identifikasi** cakupannya: sistem mana, data apa.
5. **Putar** semua kredensial dan rahasia yang disusupi.
6. **Menambal** kerentanan.
7. **Beri tahu** pengguna dan badan pengatur yang terkena dampak jika diperlukan (dalam jangka waktu yang sah).
8. **Lakukan pemeriksaan mayat** untuk memahami akar permasalahan dan meningkatkan proses.