<!--
---
# Metadata
title: "Local AI Architecture"
description: "Local AI deployment architectures"
category: "AI and Machine Learning"
subcategory: "ML Engineering"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.1"
    date: "2026-08-09"
    author: "Nepoznato-Dev"
    changes: "Moved to engineering/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "AI & Machine Learning Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [local, ai, architecture, ai-and-machine-learning]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "10 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
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
| FP32 | 4 | ~15 GB | ~28GB | ~52GB | ~280 GB |
| FP16 | 2 | ~7,6GB | ~14 GB | ~26 GB | ~140GB |
| INT8 (8-bit) | 1 | ~3,8GB | ~7 GB | ~13GB | ~70GB |
| INT4 (4-bit) | 0,5 | ~1,9GB | ~3,5GB | ~6,5GB | ~35 GB |
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
**Contoh perintah:**```bash
./llama-cli -m model.Q4_K_M.gguf -p "Tell me a joke" -n 100 -ngl 32
# -ngl 32 offloads 32 layers to GPU
```

### Ollama
- Membungkus llama.cpp dengan CLI dan REST API sederhana.
- Model unduh otomatis, kelola.
- Bagus untuk pembuatan prototipe dan aplikasi desktop.
- Mendukung File Model khusus untuk perintah sistem.
```bash
ollama run phi3:3.8b
ollama run llama3:8b
```

### LM Studio
- Aplikasi desktop grafis untuk Windows, macOS, Linux.
- Unduhan sekali klik dan antarmuka obrolan.
- Server lokal bawaan dengan API yang kompatibel dengan OpenAI.
- Baik untuk pengguna non-teknis dan pengujian cepat.
### Memeluk Wajah Transformers + bitsandbytes
- Pustaka Python standar untuk model HF.
- Gunakan`bitsandbytes`untuk kuantisasi 4-bit (`load_in_4bit=True`).
- Lebih fleksibel untuk penyesuaian tetapi lebih lambat dari llama.cpp untuk inferensi.
### MantanLlamaV2
- Inferensi GPU yang sangat cepat untuk GPTQ dan AWQ.
- Performa terbaik pada GPU NVIDIA.
- Mendukung generasi batch.
### mlx (Apple)
- Kerangka kerja Apple untuk chip seri M.
- Sangat dioptimalkan untuk Apple Silicon.
- API Python.
---

## Manajemen Memori
### Jendela Konteks dan KV Cache
Cache KV menyimpan pasangan nilai kunci untuk setiap lapisan dan setiap token dalam konteksnya. Itu tumbuh secara linear dengan panjang konteks.
Biaya memori ≈ 2 × lapisan × (kepala KV × kepala redup) × token × byte per nilai
Untuk model 32 lapisan dengan 8 head KV dan 128 head redup, setiap token berharga ~32 × 8 × 128 × 2 byte = 65 KB per token. Untuk 128 ribu token, itu ~8 GB hanya untuk cache.
### Strategi Pembongkaran
- **Pembongkaran lapisan**: Letakkan beberapa lapisan di GPU, yang lainnya di CPU. Lebih cepat dari CPU murni, kebutuhan VRAM lebih rendah.
- **Streaming token**: Memproses token secara bertahap, bukan sekaligus.
### Penyimpanan Cepat
Gunakan kembali cache KV di seluruh perintah serupa untuk menghindari penghitungan ulang fase pra-pengisian. Beberapa kerangka kerja mendukung hal ini (misalnya vLLM, llama.cpp dengan`--prompt-cache`).
### File yang Dipetakan Memori
Memuat bobot model langsung dari disk tanpa memuat seluruhnya ke dalam RAM (berguna untuk model besar pada sistem dengan memori terbatas). llama.cpp menggunakan pemetaan memori secara default.
---

## Arsitektur Penerapan
### Mode Satu Perangkat
Satu model berjalan pada satu mesin (laptop, smartphone, perangkat edge). Digunakan untuk asisten pribadi, aplikasi pencatatan, penyelesaian kode.
### Hibrida Edge-Cloud
Model lokal menangani pertanyaan umum; kembali ke model cloud untuk pertanyaan kompleks. Hal ini memberikan yang terbaik dari kedua hal tersebut — kecepatan/pribadi untuk sebagian besar, kemampuan untuk kasus edge.
### Inferensi Terdistribusi (Multi-GPU)
Untuk model yang lebih besar, pisahkan lapisan di beberapa GPU (paralelisme tensor) atau pisahkan konteks di seluruh perangkat (paralelisme pipeline). Gunakan llama.cpp dengan`-ngl`atau ExLlamaV2 dengan`--num-gpu-layers`.
### Penerapan Seluler
- **Android**: Gunakan llama.cpp melalui binding JNI atau ML Kit.
- **iOS**: Gunakan llama.cpp melalui Swift binding atau mlx.
- **Web**: Gunakan WebLLM (berjalan di WebGPU melalui runtime ONNX) atau transformers.js.
---

## Optimasi Kinerja
### Perhatian Kilat
Mempercepat komputasi perhatian dan mengurangi penggunaan memori. Tersedia di perpustakaan llama.cpp, ExLlamaV2, dan transformator modern.
### Inferensi Batch
Memproses beberapa perintah dalam satu gerakan maju. Meningkatkan throughput secara dramatis. Gunakan`llama-batch`atau vLLM.
### Penghentian Awal / Penganggaran Token
Tetapkan anggaran token maksimum untuk mencegah pembuatan tanpa batas.
### Penguraian Kode Spekulatif
Gunakan model cepat kecil (draf) untuk memprediksi token, lalu verifikasi dengan model besar secara paralel. Dapat menghasilkan percepatan 2–3×.
---

## Panduan Pengaturan Praktis
### 1. Instal Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Tarik Model
```bash
ollama pull phi3:3.8b-q4_K_M
```

### 3. Jalankan dengan API
```bash
ollama serve
```

Kemudian kirim permintaan ke`http://localhost:11434/api/generate`.
### 4. Integrasi Python
```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "phi3:3.8b", "prompt": "Hello", "stream": False}
)
print(response.json()["response"])
```

### 5. (Alternatif) Gunakan llama.cpp secara langsung
```bash
# Download GGUF from Hugging Face
wget https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf/resolve/main/Phi-3-mini-4k-instruct-q4_K_M.gguf

# Run server
./llama-server -m Phi-3-mini-4k-instruct-q4_K_M.gguf --host 0.0.0.0 --port 8080
```

---

## Pemantauan dan Observabilitas
- Lacak pemanfaatan GPU (`nvidia-smi` di Linux, Monitor Aktivitas di macOS).
- Melacak penggunaan memori (RAM dan VRAM).
- Lacak token per detik (throughput).
- Lacak waktu ke token pertama (latensi).
- Gunakan logging bawaan dari llama.cpp atau Ollama.
---

## Keterbatasan dan Pengorbanan
- **Kesenjangan kualitas**: Model lokal kecil (3,8B–7B) umumnya berperforma lebih rendah dari model cloud besar (GPT-4, Claude 3.5) karena alasan yang kompleks.
- **Pemutusan pengetahuan**: Pengetahuan model dibekukan pada waktu pelatihan; gunakan RAG untuk memasukkan informasi terkini.
- **Multibahasa**: Model yang lebih kecil mungkin memiliki kemampuan multibahasa yang lebih sedikit.
- **Penggunaan alat**: Alur kerja agen (pemanggilan fungsi) mungkin kurang dapat diandalkan pada model kecil.
Untuk banyak tugas sehari-hari (peringkasan, tanya jawab, penyelesaian kode, klasifikasi), model lokal sudah memadai dan berkembang pesat.