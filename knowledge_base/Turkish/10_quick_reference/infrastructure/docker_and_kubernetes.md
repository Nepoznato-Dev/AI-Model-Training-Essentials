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
# Docker ve Kubernetes Hile Sayfası
Uygulamaları Docker ile kapsayıcı hale getirmek ve bunları Kubernetes ile düzenlemek için pratik bir referans. Komut satırına temel aşinalığı varsayar.
---

## Docker'ın Temelleri
| Konsept | Açıklama |
|-----------|------------|
| **Resim** | Uygulama kodu + bağımlılıklar + işletim sistemi kitaplıkları içeren salt okunur şablon |
| **Konteyner** | Bir görüntünün örneğinin çalıştırılması; izole süreç |
| **Docker dosyası** | Görüntü oluşturmak için tarif |
| **Kayıt** | Görüntüler için depolama (Docker Hub, ECR, GCR, GHCR) |
| **Cilt** | Konteyner yeniden başlatıldığında hayatta kalan kalıcı depolama |
| **Ağ** | Sanal ağ bağlantı kapları |
---

## Temel Docker Komutları
### Görseller
| Komut | Açıklama |
|-----------|------------|
| `docker build -t myapp:1.0 .`| Dockerfile'dan görüntü oluşturma |
| `docker images`| Yerel görselleri listele |
| `docker pull nginx:latest`| Kayıt defterinden bir resim çekin |
| `docker push myrepo/myapp:1.0`| Bir resmi kayıt defterine aktarma |
| `docker rmi myapp:1.0`| Yerel bir resmi kaldırın |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| Bir görüntüyü kayıt defteri için etiketleme |
| `docker image prune -a`| Kullanılmayan tüm görselleri kaldırın |
### Konteynerler
| Komut | Açıklama |
|-----------|------------|
| `docker run -d -p 8080:80 nginx`| Arka planda bir kapsayıcı çalıştırın, bağlantı noktası 8080→80'i eşleyin |
| `docker run -it ubuntu bash`| Bir kabukla etkileşimli olarak çalıştırın |
| `docker run --name web -e DB_HOST=db nginx`| Kapsayıcı adını ve ortam değişkenini ayarlayın |
| `docker ps`| Çalışan kapsayıcıları listele |
| `docker ps -a`| Tüm kapsayıcıları listele (durdurulanlar dahil) |
| `docker stop web`| Çalışan bir kapsayıcıyı durdurma |
| `docker start web`| Durdurulmuş bir kapsayıcıyı başlatın |
| `docker rm web`| Durdurulmuş bir kapsayıcıyı kaldırma |
| `docker exec -it web bash`| Çalışan bir kapsayıcının içindeki kabuğu açın |
| `docker logs -f web`| Konteyner günlüklerini takip edin |
| `docker inspect web`| Ayrıntılı kapsayıcı meta verileri (JSON) |
| `docker stats`| Tüm kapsayıcılar için canlı kaynak kullanımı |
### Temizlemek
| Komut | Açıklama |
|-----------|------------|
| `docker system prune -a`| Kullanılmayan tüm kapsayıcıları, görüntüleri, ağları kaldırın ve önbellek oluşturun |
| `docker volume prune`| Kullanılmayan tüm birimleri kaldırın |
| `docker container prune`| Durdurulan tüm kapsayıcıları kaldırın |
---

## Dockerfile Referansı
### Ortak Talimatlar
| Talimat | Amaç | Örnek |
|-------------|-----------|---------|
| `FROM`| Temel resim | `FROM python:3.12-slim`|
| `WORKDIR`| Resmin içindeki çalışma dizinini ayarlayın | `WORKDIR /app`|
| `COPY`| Dosyaları ana bilgisayardan görüntüye kopyalayın | `COPY requirements.txt .`|
| `ADD`| COPY'ye benzer, ancak aynı zamanda katranları çıkarır ve URL'leri destekler | `ADD app.tar.gz /app/`|
| `RUN`| Derleme sırasında bir komut yürütün | `RUN pip install -r requirements.txt`|
| `CMD`| Kapsayıcı başlatıldığında varsayılan komut | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| Sabit komut; CMD argümanlara dönüşür | `ENTRYPOINT ["python"]`|
| `ENV`| Ortam değişkenini ayarla | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| Uygulamanın hangi bağlantı noktasını dinlediğini belgeleyin | `EXPOSE 8000`|
| `ARG`| Oluşturma zamanı değişkeni | `ARG VERSION=1.0`|
| `USER`| Root dışı kullanıcıya geç | `USER appuser`|
| `HEALTHCHECK`| Durum denetimi komutunu tanımlayın | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| Bağlama noktası oluşturun | `VOLUME /data`|
### En İyi Uygulamalar
| Alıştırma | Neden |
|----------|-----|
| İnce/temel görselleri kullanın | Daha küçük resimler = daha hızlı çekme, daha küçük saldırı yüzeyi |
| RUN komutlarını`&&`ile birleştirin | Görüntü katmanlarını azaltır |
| Önce bağımlılık dosyalarını kopyalayın, ardından kodu | Docker'ın derleme önbelleğinden yararlanır |
|`.dockerignore`kullanın |`node_modules`,`.git`, `__pycache__`'yi hariç tutun |
| Root dışı kullanıcı olarak çalıştır | Güvenlikte en iyi uygulama |
| Çok aşamalı yapıları kullanın | Ayrı derleme ve çalışma zamanı; daha küçük son görüntü |
| Pin tabanı görsel versiyonları | Tekrarlanabilir yapılar (`python:3.12.1-slim`,`python:latest`değil) |
### Çok Aşamalı Yapı Örneği
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

## Docker Oluşturma
Docker Compose, tek bir YAML dosyasında çok kapsayıcılı uygulamaları tanımlar.
### Tuş Komutları
| Komut | Açıklama |
|-----------|------------|
| `docker compose up -d`| Tüm hizmetleri arka planda başlat |
| `docker compose down`| Kapları ve ağları durdurun ve kaldırın |
| `docker compose down -v`| Ayrıca birimleri de kaldırın |
| `docker compose logs -f`| Tüm hizmetlerin günlüklerini takip edin |
| `docker compose ps`| Çalışan hizmetleri listele |
| `docker compose build`| Görüntüleri yeniden oluştur |
| `docker compose exec web bash`| Çalışan bir hizmette komutu çalıştırın |
| `docker compose pull`| En son görüntüleri çekin |
### Örnek Dosya Oluşturma
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

## Kubernetes Mimarisi
| Bileşen | Rol |
|-----------|------|
| **Küme** | Konteynerli uygulamaları çalıştıran bir dizi düğüm (makine) |
| **Kontrol Düzlemi** | API sunucusu, zamanlayıcı, denetleyici yöneticisi, vb. (küme durumu) |
| **Düğüm** | Podları çalıştıran bir çalışan makine (VM veya fiziksel) |
| **Bölme** | En küçük birim; bir veya daha fazla sıkı bir şekilde bağlanmış kaplar |
| **Dağıtım** | Bir bölmenin kopyalarını yönetir; sürekli güncellemeleri yönetir |
| **Hizmet** | Bir dizi bölme için kararlı ağ uç noktası |
| **Giriş** | Kümenin dışından hizmetlere HTTP yönlendirmesi |
| **Yapılandırma Haritası** | Gizli olmayan yapılandırma verileri |
| **Gizli** | Hassas veriler (base64 kodlu) |
| **Ad alanı** | Küme içinde mantıksal izolasyon |
| **Kalıcı Hacim (PV)** | Küme düzeyinde depolama kaynağı |
| **Kalıcı Hacim Talebi (PVC)** | Kapsülle depolama talebi |
---

## kubectl Komutları
### Küme Bilgisi
| Komut | Açıklama |
|-----------|------------|
| `kubectl cluster-info`| Küme uç noktası ayrıntıları |
| `kubectl get nodes`| Tüm düğümleri listele |
| `kubectl get namespaces`| Ad alanlarını listeleyin |
| `kubectl config current-context`| Geçerli küme içeriğini göster |
| `kubectl config use-context prod`| Bağlamı değiştir |
### İş yükleri
| Komut | Açıklama |
|-----------|------------|
| `kubectl get pods`| Geçerli ad alanındaki bölmeleri listeleme |
| `kubectl get pods -A`| Tüm ad alanlarındaki bölmeleri listeleme |
| `kubectl get deployments`| Dağıtımları listeleyin |
| `kubectl get services`| Hizmetleri listele |
| `kubectl get ingress`| Giriş kaynaklarını listeleyin |
| `kubectl describe pod <name>`| Ayrıntılı kapsül bilgisi (olaylar, durum, özellikler) |
| `kubectl logs <pod>`| Pod günlüklerini görüntüle |
| `kubectl logs -f <pod>`| Pod günlüklerini takip edin |
| `kubectl logs <pod> -c <container>`| Çok kapsayıcılı bir bölmedeki belirli bir kapsayıcıdaki günlükler |
| `kubectl exec -it <pod> -- bash`| Kabuğu bir bölmeye dönüştürün |
| `kubectl delete pod <name>`| Bir bölmeyi silin (denetleyicisi tarafından yeniden oluşturulacaktır) |
| `kubectl rollout status deployment/<name>`| Kullanıma sunma ilerlemesini kontrol edin |
| `kubectl rollout undo deployment/<name>`| Önceki sürüme geri dönün |
### Yapılandırmanın Uygulanması
| Komut | Açıklama |
|-----------|------------|
| `kubectl apply -f deployment.yaml`| YAML bildirimi uygulama |
| `kubectl apply -f ./dir/`| Tüm YAML dosyalarını bir dizine uygulayın |
| `kubectl delete -f deployment.yaml`| YAML dosyasında tanımlanan kaynakları silin |
| `kubectl scale deployment/web --replicas=5`| Dağıtımı ölçeklendirme |
| `kubectl set image deployment/web web=myapp:2.0`| Kapsayıcı resmini güncelle |
---

## Ortak Kubernetes Bildirimleri
### Dağıtım
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

### Hizmet
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

### Giriş
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

## Dümen Temelleri
Helm, Kubernetes'in paket yöneticisidir. Kubernetes kaynaklarını yeniden kullanılabilir grafikler halinde paketler.
| Komut | Açıklama |
|-----------|------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| Grafik deposu ekleyin |
| `helm repo update`| Yerel grafik indeksini güncelleyin |
| `helm search repo nginx`| Grafik arayın |
| `helm install my-release bitnami/nginx`| Bir grafik yükleyin |
| `helm install my-release bitnami/nginx --set replicaCount=3`| Özel değerlerle yükleme |
| `helm install my-release bitnami/nginx -f values.yaml`| Değerler dosyasıyla kurulum |
| `helm list`| Kurulu sürümleri listele |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| Sürümü yükseltme |
| `helm rollback my-release 1`| Önceki revizyona geri dönme |
| `helm uninstall my-release`| Bir sürümü kaldırma |
| `helm status my-release`| Sürüm durumunu göster |
---

## Sorun Giderme Hızlı Başvurusu
| Sorun | Denenecek Komutlar |
|-----------|----------------|
| Kapsül başlamıyor | `kubectl describe pod <name>`→ Olayları kontrol edin |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ neden düştüğünü görün |
| Resim çekme hatası | Görüntü adını, etiketini ve kayıt defteri kimlik bilgilerini kontrol edin |
| Hizmete ulaşılamıyor | `kubectl get endpoints <service>`→ bölmeler seçili mi? |
| OOM Öldürüldü | Bellek sınırlarını artırın veya uygulama belleği kullanımını optimize edin |
| Bekleyen bölmeler | `kubectl describe pod`→ düğüm kaynaklarını, kusurları, yakınlığı kontrol edin |
| DNS sorunları | `kubectl exec <pod> -- nslookup kubernetes.default`|