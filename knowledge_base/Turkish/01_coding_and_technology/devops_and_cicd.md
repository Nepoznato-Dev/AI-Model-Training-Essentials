---
# Metadata
title: "DevOps and CI/CD"
description: "CI/CD pipelines, Docker, Kubernetes, Terraform, GitOps"
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
tags: [devops, cicd, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "11 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---
# DevOps ve CI/CD
DevOps, ekiplerin yazılımı daha hızlı ve daha güvenilir bir şekilde sunmasını sağlayan kültürel felsefe, uygulamalar ve araçların birleşimidir. Geliştiriciler (değişiklikleri göndermek isteyen) ve operasyonlar (istikrar isteyen) arasındaki duvarı yıkar. CI/CD — Sürekli Entegrasyon ve Sürekli Teslimat — bunu mümkün kılan otomasyon omurgasıdır.
---

## CI/CD İşlem Hatları
### CI/CD Aslında Ne Anlama Geliyor
| Dönem | Ne İşe Yarar |
|------|-----------------|
| **Sürekli Entegrasyon (CI)** | Geliştiriciler kodları sıklıkla birleştirir; her birleşme otomatik derlemeleri ve testleri tetikler |
| **Sürekli Teslimat (CD)** | Kod her zaman konuşlandırılabilir durumdadır; üretime sunmak manuel bir karardır |
| **Sürekli Dağıtım** | Testleri geçen her değişiklik otomatik olarak üretime geçer; manuel geçişe gerek yoktur |
### Tipik Boru Hattı Aşamaları
| Sahne | Ne Olur | Araçlar |
|----------|----------------|-------|
| **Kaynak** | Geliştirici kodu Git'e aktarıyor | GitHub, GitLab, Bitbucket |
| **İnşa** | Kodu derleyin, bağımlılıkları yükleyin | Maven, Gradle, npm, pip |
| **Test** | Çalıştırma ünitesi, entegrasyon, tüy kontrolleri | Şaka, pytest, JUnit |
| **Paket** | Docker görüntüsü veya yapıtı oluşturun | Docker, Yapı Paketleri |
| **Dağıtım (hazırlama)** | Hazırlama ortamına dağıtma | Kubernetes, ECS, VM |
| **Test (aşamalama)** | Entegrasyon testleri, duman testleri | Selenyum, Postacı |
| **Dağıtım (üretim)** | Üretime sürüm | Mavi-yeşil, kanarya, inişli çıkışlı |
| **Monitör** | Sağlığı, hataları ve performansı gözlemleyin | Prometheus, Grafana, Datadog |
### CI/CD Araçları Karşılaştırıldı
| Araç | Tür | Güç |
|------|----------|----------|
| **GitHub Eylemleri** | Bulut CI/CD | GitHub ile derinlemesine entegre; YAML iş akışları |
| **GitLab CI** | Dahili CI/CD | Repo + boru hattı için tek platform |
| **Jenkins** | Kendi kendine barındırılan CI/CD | Son derece yapılandırılabilir; devasa eklenti ekosistemi |
| **ÇemberCI** | Bulut CI/CD | Hızlı; kapsayıcılı iş akışları için iyi |
| **ArgoCD** | Kubernetes için GitOps | Bildirime dayalı, Git odaklı dağıtımlar |
---

## Docker ve Konteynerler
### Neden Konteynerler?
Konteynerlerden önce klasik sorun "makinemde çalışıyor" idi. Konteynerler bu sorunu, bir uygulamayı tüm bağımlılıklarıyla (kitaplıklar, çalışma zamanı, yapılandırma) her yerde aynı şekilde çalışan tek, taşınabilir bir birimde paketleyerek çözer.
### Docker'ın Temelleri
| Konsept | Açıklama |
|-----------|------------|
| **Resim** | Uygulama + bağımlılıkları içeren salt okunur şablon |
| **Konteyner** | Bir görüntünün örneğini çalıştırma |
| **Docker dosyası** | Görüntü oluşturmak için tarif |
| **Kayıt** | Görüntüler için depolama (Docker Hub, ECR, GCR) |
| **Cilt** | Konteyner yeniden başlatmalarına dayanabilen kalıcı depolama |
| **Ağ** | Kapsayıcılar için yalıtılmış ağ katmanı |
### Dockerfile En İyi Uygulamaları
```dockerfile
# Use specific base image tags, not 'latest'
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency file first (leverage Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Run as non-root user
USER appuser

# Expose port and define entrypoint
EXPOSE 8000
CMD ["python", "main.py"]
```

Temel uygulamalar: ince/alpine temel görüntüleri kullanın, kök olmayan olarak çalıştırın, katman önbelleğe alma özelliğini kullanın,`.dockerignore`kullanın, görüntüleri güvenlik açıklarına karşı tarayın (`trivy`, `docker scan`) ve kaynak sınırlarını ayarlayın.
### Docker Oluşturma
Birden fazla kapsayıcıyı birlikte çalıştırmak için (uygulama + veritabanı + önbellek):
```yaml
services:
  app:
    build: .
    ports: ["8000:8000"]
    depends_on: [db, redis]
    environment:
      DATABASE_URL: postgresql://user:pass@db:5432/mydb
  db:
    image: postgres:16
    volumes: [pgdata:/var/lib/postgresql/data]
  redis:
    image: redis:7-alpine
volumes:
  pgdata:
```

---

## Kubernet'ler (K8'ler)
Kubernetes, endüstri standardı konteyner orkestratörüdür. Konteynerli uygulamaların dağıtımını, ölçeklendirilmesini ve çalışmasını yönetir.
### Çekirdek Mimari
| Bileşen | Rol |
|-----------|------|
| **Kontrol Düzlemi** | Kümeyi yönetir (API sunucusu, zamanlayıcı, vb., denetleyici yöneticisi) |
| **Düğüm** | Konteynerleri çalıştıran çalışan makine (VM veya fiziksel) |
| **Bölme** | En küçük konuşlandırılabilir birim; ağı paylaşan bir veya daha fazla kapsayıcı |
| **Hizmet** | Trafiği bölmelere yönlendiren kararlı ağ uç noktası |
| **Dağıtım** | İstenilen bölme durumunun bildirimsel tanımı (kopyalar, görüntü vb.) |
| **Giriş** | Harici trafik için HTTP yönlendirme kuralları |
| **ConfigMap / Gizli** | Bölmelere eklenen yapılandırma ve hassas veriler |
### Temel kubectl Komutları
```bash
kubectl get pods                    # List pods
kubectl get services                # List services
kubectl describe pod <name>         # Detailed pod info
kubectl logs <pod-name>             # View pod logs
kubectl exec -it <pod> -- /bin/sh   # Shell into a pod
kubectl apply -f deployment.yaml    # Apply a manifest
kubectl rollout status deploy/myapp # Check rollout progress
kubectl scale deploy/myapp --replicas=5  # Scale to 5 replicas
```

### Dümen
Helm, Kubernetes'in paket yöneticisidir. **grafik** önceden yapılandırılmış Kubernetes kaynaklarının bir paketidir. Bunu K8'ler için`apt`veya`brew`olarak düşünün.
```bash
helm install my-release bitnami/postgresql   # Install a chart
helm upgrade my-release bitnami/postgresql   # Upgrade
helm rollback my-release 1                   # Rollback to revision 1
helm list                                    # List releases
```

---

## Kod Olarak Altyapı (IaC)
IaC, altyapı yapılandırmasını uygulama koduyla aynı şekilde ele alır: sürüm kontrollü, test edilmiş ve işlem hatları aracılığıyla dağıtılmış.
### Terraform ve Ansible
| Araç | Tür | Yaklaşım | En İyisi |
|------|------|----------|----------|
| **Terraform** | Tedarik | Bildirimsel (HCL); devlet bazlı | Bulut kaynakları oluşturma (VPC'ler, VM'ler, veritabanları) |
| **Ansible** | Yapılandırma | Bildirimsel (YAML); acentesiz | Sunucuları yapılandırma, yazılımı yükleme |
| **Pulumi** | Tedarik | Zorunluluk (Python, Go, TS) | Gerçek programlama dillerini tercih eden ekipler |
| **Bulut Oluşumu** | Tedarik | Bildirime dayalı (YAML/JSON); AWS'de yerel | Yalnızca AWS altyapısı |
### Terraform Örneği
```hcl
provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

En iyi uygulamalar: Yeniden kullanılabilirlik için modülleri kullanın, durumu uzaktan saklayın (kilitleme için S3 + DynamoDB), gizli kodları hiçbir zaman sabit kodlamayın ve her şeyi sürüm kontrolüyle kontrol edin.
---

## İzleme ve Gözlemlenebilirlik
### Üç Sütun
| Sütun | Size Ne Anlatıyor | Araçlar |
|----------|-----------|-------|
| **Metrikler** | Zaman içindeki sayısal ölçümler (CPU, istek oranı, hata oranı) | Prometheus, CloudWatch, Datadog |
| **Günlükler** | Bağlamlı ayrı olaylar (hatalar, istekler, durum değişiklikleri) | ELK Yığını, Loki, CloudWatch Günlükleri |
| **İzler** | Hizmetler arasında uçtan uca istek yolculuğu | Jaeger, Röntgen, Zipkin |
### Prometheus + Grafana Yığını
Standart açık kaynak izleme yığını:
| Bileşen | Rol |
|-----------|------|
| **Prometheus** | Zaman serisi veritabanı; hizmetlerden ölçümleri alır |
| **Grafana** | Görselleştirme ve kontrol panelleri |
| **Uyarı yöneticisi** | Uyarıları Slack, PagerDuty, e-postaya yönlendirir |
| **Düğüm Aktarıcı** | Sistem düzeyindeki ölçümleri ortaya çıkarır (CPU, RAM, disk) |
| **Kara Kutu İhracatçısı** | Uç noktaları araştırır (HTTP, TCP, ICMP) |
### İzlenecek Temel Metrikler
| Kategori | Metrikler |
|----------|-----------|
| **Altyapı** | CPU, RAM, disk kullanımı, ağ G/Ç |
| **Uygulama** | İstek oranı, gecikme (p50, p95, p99), hata oranı |
| **Veritabanı** | Sorgu sayısı, yavaş sorgular, bağlantı havuzu kullanımı |
| **İş** | Kayıtlar, dönüşümler, gelir |
---

## Dağıtım Stratejileri
| Strateji | Nasıl Çalışır | Risk | Geri Alma |
|----------|----------------|------|----------|
| **Devamlı Güncelleme** | Eski örnekleri yavaş yavaş yenileriyle değiştirin | Bazı kullanıcılar eski sürümde, bazıları yeni sürümde | Önceki resme dön |
| **Mavi-Yeşil** | İki özdeş ortamı çalıştırın; trafiği değiştir | Geçiş sırasında iki kat altyapı maliyeti | Anında geri dönüş |
| **Kanarya** | Trafiğin küçük bir yüzdesini yeni sürüme yönlendirin; kademeli olarak artırın | Karmaşık trafik yönetimi | Trafiği tekrar stabile yönlendir |
| **Özellik Bayrakları** | Kodu dağıtın ancak özellikleri geçişlerin arkasına gizleyin | Koşullu mantıktan kod karmaşıklığı | Kapat |
---

## GitOps
GitOps, IaC'yi mantıksal sonucuna götürür: Git deposu, altyapınızın ve uygulamalarınızın istenen durumu için tek gerçek kaynaktır.
| Prensip | Açıklama |
|-----------|----------------|
| **Bildirim niteliğinde** | Kod olarak tanımlanan her şey (YAML, HCL) |
| **Sürümlendi** | Git gerçeğin kaynağıdır |
| **Otomatik** | Araçlar sürekli olarak istenen durumu gerçek durumla uzlaştırır |
| **Denetlenebilir** | Her değişiklik bir Git taahhüdüdür |
**ArgoCD** ve **Flux** Kubernetes için önde gelen GitOps araçlarıdır. Git deponuza bir değişiklik gönderirsiniz ve araç bunu otomatik olarak kümeye dağıtır.
---

## Olay Müdahalesi
Gece 3'te bir şey bozulduğunda:
1. Uyarıyı **onaylayın**.
2. **Kapsamın değerlendirilmesi**: Hangi hizmetler, kullanıcılar ve veriler etkileniyor?
3. Temel nedeni **belirleyin** — günlükleri, ölçümleri ve son dağıtımları kontrol edin.
4. **Mümkünse devre kesicileri, özellik işaretlerini, trafik geçişini engelleyin**.
5. **Düzeltme** — geri alma veya ileri yama.
6. **İletişim kurun** — Paydaşları ve kullanıcıları güncelleyin (durum sayfası).
7. **Opsi sonrası** — 24-48 saat içinde temel nedeni ve eylem öğelerini belgeleyin.
Amaç sadece olayı düzeltmek değil, aynı olayın tekrar yaşanmayacağından emin olmaktır.