<!--
---
# Metadata
title: "Docker and Kubernetes Cheat Sheet"
description: "Docker, Docker Compose, Kubernetes, Helm cheat sheet"
category: "Quick Reference"
subcategory: "Infrastructure"
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
    changes: "Moved to infrastructure/ subfolder; added subcategory field"
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-09"
review_date: "2027-02-05"
reviewed_by: "Quick Reference Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [docker, kubernetes, quick-reference]
difficulty_level: "beginner"
prerequisites: []
estimated_reading_time: "15 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# Lembar Cheat Docker dan Kubernetes
Referensi praktis untuk memasukkan aplikasi ke dalam container dengan Docker dan mengaturnya dengan Kubernetes. Mengasumsikan keakraban dasar dengan baris perintah.
---

## Dasar-Dasar Docker
| Konsep | Deskripsi |
|---------|-------------|
| **Gambar** | Templat hanya-baca dengan kode aplikasi + dependensi + pustaka OS |
| **Wadah** | Menjalankan contoh gambar; proses terisolasi |
| **File Docker** | Resep untuk membangun sebuah gambar |
| **Registrasi** | Penyimpanan gambar (Docker Hub, ECR, GCR, GHCR) |
| **Volume** | Penyimpanan persisten yang bertahan saat kontainer dimulai ulang |
| **Jaringan** | Kontainer penghubung jaringan virtual |
---

## Perintah Docker Penting
### Gambar
| Perintah | Deskripsi |
|---------|-------------|
| `docker build -t myapp:1.0 .`| Bangun gambar dari Dockerfile |
| `docker images`| Daftar gambar lokal |
| `docker pull nginx:latest`| Tarik gambar dari registri |
| `docker push myrepo/myapp:1.0`| Dorong gambar ke registri |
| `docker rmi myapp:1.0`| Hapus gambar lokal |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| Tandai gambar untuk registri |
| `docker image prune -a`| Hapus semua gambar yang tidak digunakan |
### Kontainer
| Perintah | Deskripsi |
|---------|-------------|
| `docker run -d -p 8080:80 nginx`| Jalankan container di latar belakang, petakan port 8080→80 |
| `docker run -it ubuntu bash`| Jalankan secara interaktif dengan shell |
| `docker run --name web -e DB_HOST=db nginx`| Tetapkan nama kontainer dan variabel lingkungan |
| `docker ps`| Daftar kontainer yang sedang berjalan |
| `docker ps -a`| Daftar semua kontainer (termasuk yang dihentikan) |
| `docker stop web`| Hentikan container yang sedang berjalan |
| `docker start web`| Mulai wadah yang dihentikan |
| `docker rm web`| Hapus wadah yang terhenti |
| `docker exec -it web bash`| Buka shell di dalam container yang sedang berjalan |
| `docker logs -f web`| Ikuti log kontainer |
| `docker inspect web`| Metadata kontainer terperinci (JSON) |
| `docker stats`| Penggunaan sumber daya langsung untuk semua kontainer |
### Pembersihan
| Perintah | Deskripsi |
|---------|-------------|
| `docker system prune -a`| Hapus semua container, image, jaringan, dan build cache yang tidak terpakai |
| `docker volume prune`| Hapus semua volume yang tidak digunakan |
| `docker container prune`| Hapus semua kontainer yang dihentikan |
---

## Referensi Dockerfile
### Petunjuk Umum
| Instruksi | Tujuan | Contoh |
|-------------|---------|---------|
| `FROM`| Gambar dasar | `FROM python:3.12-slim`|
| `WORKDIR`| Atur direktori kerja di dalam gambar | `WORKDIR /app`|
| `COPY`| Salin file dari host ke gambar | `COPY requirements.txt .`|
| `ADD`| Seperti COPY, tetapi juga mengekstrak tar dan mendukung URL | `ADD app.tar.gz /app/`|
| `RUN`| Jalankan perintah selama build | `RUN pip install -r requirements.txt`|
| `CMD`| Perintah default saat penampung dimulai | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| Perintah tetap; CMD menjadi argumen | `ENTRYPOINT ["python"]`|
| `ENV`| Tetapkan variabel lingkungan | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| Dokumentasikan port mana yang didengarkan aplikasi | `EXPOSE 8000`|
| `ARG`| Variabel waktu pembuatan | `ARG VERSION=1.0`|
| `USER`| Beralih ke pengguna non-root | `USER appuser`|
| `HEALTHCHECK`| Tentukan perintah pemeriksaan kesehatan | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| Buat titik pemasangan | `VOLUME /data`|
### Praktik Terbaik
| Latihan | Mengapa |
|----------|-----|
| Gunakan gambar ramping/dasar | Gambar lebih kecil = tarikan lebih cepat, permukaan serangan lebih kecil |
| Gabungkan perintah RUN dengan`&&`| Mengurangi lapisan gambar |
| Salin file ketergantungan terlebih dahulu, lalu kode | Memanfaatkan cache build Docker |
| Gunakan`.dockerignore`| Kecualikan`node_modules`,`.git`,`__pycache__`|
| Jalankan sebagai pengguna non-root | Praktik terbaik keamanan |
| Gunakan build multi-tahap | Pisahkan build dan runtime; gambar akhir yang lebih kecil |
| Sematkan versi gambar dasar | Build yang dapat direproduksi (`python:3.12.1-slim`, bukan`python:latest`) |
### Contoh Pembuatan Multi-Tahap
```dockerfile
# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/main.js"]
```

---

## Penulisan Docker
Docker Compose mendefinisikan aplikasi multi-kontainer dalam satu file YAML.
### Perintah Utama
| Perintah | Deskripsi |
|---------|-------------|
| `docker compose up -d`| Mulai semua layanan di latar belakang |
| `docker compose down`| Hentikan dan hapus kontainer, jaringan |
| `docker compose down -v`| Hapus juga volume |
| `docker compose logs -f`| Ikuti log dari semua layanan |
| `docker compose ps`| Daftar layanan yang berjalan |
| `docker compose build`| Bangun kembali gambar |
| `docker compose exec web bash`| Jalankan perintah di layanan yang sedang berjalan |
| `docker compose pull`| Tarik gambar terbaru |
### Contoh Penulisan File
```yaml
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - DATABASE_URL=postgres://user:pass@db:5432/mydb
      - REDIS_URL=redis://cache:6379
    depends_on:
      db:
        condition: service_healthy
      cache:
        condition: service_started
    restart: unless-stopped

  db:
    image: postgres:16-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: mydb
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 5s
      timeout: 5s
      retries: 5

  cache:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  pgdata:
```

---

## Arsitektur Kubernetes
| Komponen | Peran |
|-----------|------|
| **Kluster** | Sekumpulan node (mesin) yang menjalankan aplikasi dalam container |
| **Bidang Kendali** | Server API, penjadwal, manajer pengontrol, dll (status cluster) |
| **Simpul** | Mesin pekerja (VM atau fisik) yang menjalankan pod |
| **Pod** | Satuan terkecil; satu atau lebih wadah yang berpasangan rapat |
| **Penerapan** | Mengelola replika pod; menangani pembaruan berkelanjutan |
| **Layanan** | Titik akhir jaringan yang stabil untuk sekumpulan pod |
| **Masuk** | Perutean HTTP dari luar cluster ke layanan |
| **ConfigMap** | Data konfigurasi non-rahasia |
| **Rahasia** | Data sensitif (dikodekan base64) |
| **Ruang Nama** | Isolasi logis dalam sebuah cluster |
| **Volume Persisten (PV)** | Sumber daya penyimpanan tingkat cluster |
| **PersistentVolumeClaim (PVC)** | Permintaan penyimpanan berdasarkan pod |
---

## Perintah kubectl
### Info Klaster
| Perintah | Deskripsi |
|---------|-------------|
| `kubectl cluster-info`| Detail titik akhir klaster |
| `kubectl get nodes`| Daftar semua node |
| `kubectl get namespaces`| Daftar namespace |
| `kubectl config current-context`| Tampilkan konteks cluster saat ini |
| `kubectl config use-context prod`| Ganti konteks |
### Beban kerja
| Perintah | Deskripsi |
|---------|-------------|
| `kubectl get pods`| Daftar pod di namespace saat ini |
| `kubectl get pods -A`| Daftarkan pod di seluruh namespace |
| `kubectl get deployments`| Daftar penerapan |
| `kubectl get services`| Daftar layanan |
| `kubectl get ingress`| Daftar sumber daya masuk |
| `kubectl describe pod <name>`| Info pod terperinci (acara, status, spesifikasi) |
| `kubectl logs <pod>`| Lihat log pod |
| `kubectl logs -f <pod>`| Ikuti log pod |
| `kubectl logs <pod> -c <container>`| Log dari container tertentu di pod multi-container |
| `kubectl exec -it <pod> -- bash`| Cangkang ke dalam pod |
| `kubectl delete pod <name>`| Menghapus sebuah pod (akan dibuat ulang oleh pengontrolnya) |
| `kubectl rollout status deployment/<name>`| Periksa kemajuan peluncuran |
| `kubectl rollout undo deployment/<name>`| Kembalikan ke versi sebelumnya |
### Menerapkan Konfigurasi
| Perintah | Deskripsi |
|---------|-------------|
| `kubectl apply -f deployment.yaml`| Terapkan manifes YAML |
| `kubectl apply -f ./dir/`| Terapkan semua file YAML dalam direktori |
| `kubectl delete -f deployment.yaml`| Hapus sumber daya yang ditentukan dalam file YAML |
| `kubectl scale deployment/web --replicas=5`| Skalakan penerapan |
| `kubectl set image deployment/web web=myapp:2.0`| Perbarui gambar kontainer |
---

## Manifes Kubernetes Umum
### Penerapan
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
  labels:
    app: web
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: myapp:1.0
        ports:
        - containerPort: 8080
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 15
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
```

### Melayani
```yaml
apiVersion: v1
kind: Service
metadata:
  name: web
spec:
  selector:
    app: web
  ports:
  - port: 80
    targetPort: 8080
  type: ClusterIP    # Internal only
  # type: LoadBalancer  # External (cloud provider)
  # type: NodePort      # External via node IP + port
```

### Masuk
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: web
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
spec:
  rules:
  - host: myapp.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: web
            port:
              number: 80
```

---

## Dasar-Dasar Helm
Helm adalah manajer paket untuk Kubernetes. Ini mengemas sumber daya Kubernetes ke dalam bagan yang dapat digunakan kembali.
| Perintah | Deskripsi |
|---------|-------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| Tambahkan repositori grafik |
| `helm repo update`| Perbarui indeks grafik lokal |
| `helm search repo nginx`| Cari grafik |
| `helm install my-release bitnami/nginx`| Pasang bagan |
| `helm install my-release bitnami/nginx --set replicaCount=3`| Instal dengan nilai khusus |
| `helm install my-release bitnami/nginx -f values.yaml`| Instal dengan file nilai |
| `helm list`| Daftar rilis yang diinstal |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| Tingkatkan rilis |
| `helm rollback my-release 1`| Kembalikan ke revisi sebelumnya |
| `helm uninstall my-release`| Copot pemasangan rilis |
| `helm status my-release`| Tampilkan status rilis |
---

## Pemecahan Masalah Referensi Cepat
| Masalah | Perintah untuk Dicoba |
|---------|----------------|
| Pod tidak dimulai | `kubectl describe pod <name>`→ periksa Acara |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ lihat mengapa crash |
| Kesalahan penarikan gambar | Periksa nama gambar, tag, dan kredensial registri |
| Layanan tidak dapat dijangkau | `kubectl get endpoints <service>`→ apakah pod dipilih? |
| OOMDibunuh | Tingkatkan batas memori atau optimalkan penggunaan memori aplikasi |
| Pod yang tertunda | `kubectl describe pod`→ periksa sumber daya node, noda, afinitas |
| Masalah DNS | `kubectl exec <pod> -- nslookup kubernetes.default`|