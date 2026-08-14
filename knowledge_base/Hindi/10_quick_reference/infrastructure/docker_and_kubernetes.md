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
# डॉकर और कुबेरनेट्स चीट शीट
डॉकर के साथ अनुप्रयोगों को कंटेनरीकृत करने और कुबेरनेट्स के साथ उन्हें व्यवस्थित करने के लिए एक व्यावहारिक संदर्भ। कमांड लाइन के साथ बुनियादी परिचितता मानता है।
---

## डॉकर बुनियादी बातें
| संकल्पना | विवरण |
|---------|-----------------|
| **छवि** | ऐप कोड + निर्भरता + ओएस लाइब्रेरीज़ के साथ केवल पढ़ने योग्य टेम्पलेट |
| **कंटेनर** | किसी छवि का चालू उदाहरण; पृथक प्रक्रिया |
| **डॉकरफ़ाइल** | छवि निर्माण की विधि |
| **रजिस्ट्री** | छवियों के लिए भंडारण (डॉकर हब, ईसीआर, जीसीआर, जीएचसीआर) |
| **वॉल्यूम** | लगातार भंडारण जो कंटेनर के पुनरारंभ होने से बचा रहता है |
| **नेटवर्क** | कंटेनरों को जोड़ने वाला वर्चुअल नेटवर्क |
---

## आवश्यक डॉकर कमांड
### इमेजिस
| आदेश | विवरण |
|---------|-----------------|
| `docker build -t myapp:1.0 .`| Dockerfile से एक छवि बनाएं |
| `docker images`| स्थानीय छवियों की सूची बनाएं |
| `docker pull nginx:latest`| रजिस्ट्री से एक छवि खींचें |
| `docker push myrepo/myapp:1.0`| किसी छवि को रजिस्ट्री में पुश करें |
| `docker rmi myapp:1.0`| स्थानीय छवि हटाएँ |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| रजिस्ट्री के लिए एक छवि टैग करें |
| `docker image prune -a`| सभी अप्रयुक्त छवियों को हटा दें |
### कंटेनर
| आदेश | विवरण |
|---------|-----------------|
| `docker run -d -p 8080:80 nginx`| पृष्ठभूमि में एक कंटेनर चलाएँ, मैप पोर्ट 8080→80 |
| `docker run -it ubuntu bash`| एक शेल के साथ अंतःक्रियात्मक रूप से चलाएँ |
| `docker run --name web -e DB_HOST=db nginx`| कंटेनर नाम और पर्यावरण चर सेट करें |
| `docker ps`| चल रहे कंटेनरों की सूची बनाएं |
| `docker ps -a`| सभी कंटेनरों की सूची बनाएं (रोके गए सहित) |
| `docker stop web`| चल रहे कंटेनर को रोकें |
| `docker start web`| रुके हुए कंटेनर को चालू करें |
| `docker rm web`| रुके हुए कंटेनर को हटा दें |
| `docker exec -it web bash`| एक चालू कंटेनर के अंदर एक शेल खोलें |
| `docker logs -f web`| कंटेनर लॉग का पालन करें |
| `docker inspect web`| विस्तृत कंटेनर मेटाडेटा (JSON) |
| `docker stats`| सभी कंटेनरों के लिए लाइव संसाधन उपयोग |
### साफ - सफाई
| आदेश | विवरण |
|---------|-----------------|
| `docker system prune -a`| सभी अप्रयुक्त कंटेनर, चित्र, नेटवर्क हटाएं और कैश बनाएं |
| `docker volume prune`| सभी अप्रयुक्त वॉल्यूम हटाएं |
| `docker container prune`| सभी रुके हुए कंटेनरों को हटा दें |
---

## डॉकरफ़ाइल संदर्भ
### सामान्य निर्देश
| निर्देश | उद्देश्य | उदाहरण |
|---|--|---|
| `FROM`| आधार छवि | `FROM python:3.12-slim`|
| `WORKDIR`| छवि के अंदर कार्यशील निर्देशिका सेट करें | `WORKDIR /app`|
| `COPY`| होस्ट से छवि में फ़ाइलें कॉपी करें | `COPY requirements.txt .`|
| `ADD`| COPY की तरह, लेकिन टार भी निकालता है और URL का समर्थन करता है | `ADD app.tar.gz /app/`|
| `RUN`| निर्माण के दौरान एक आदेश निष्पादित करें | `RUN pip install -r requirements.txt`|
| `CMD`| कंटेनर प्रारंभ होने पर डिफ़ॉल्ट कमांड | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| निश्चित आदेश; सीएमडी तर्क बन जाता है | `ENTRYPOINT ["python"]`|
| `ENV`| पर्यावरण चर सेट करें | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| दस्तावेज़ जिस पोर्ट पर ऐप सुनता है | `EXPOSE 8000`|
| `ARG`| बिल्ड-टाइम वैरिएबल | `ARG VERSION=1.0`|
| `USER`| गैर-रूट उपयोक्ता पर स्विच करें | `USER appuser`|
| `HEALTHCHECK`| स्वास्थ्य जांच आदेश को परिभाषित करें | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| एक माउंट पॉइंट बनाएं | `VOLUME /data`|
### सर्वोत्तम प्रथाएं
| अभ्यास करें | क्यों |
|---|-----|
| स्लिम/बेस छवियों का उपयोग करें | छोटी छवियाँ = तेज़ खींच, छोटी आक्रमण सतह |
| RUN कमांड को`&&`| के साथ संयोजित करें छवि परतों को कम करता है |
| पहले निर्भरता फ़ाइलें कॉपी करें, फिर कोड | डॉकर के बिल्ड कैश का लाभ उठाता है |
|`.dockerignore`| का उपयोग करें`node_modules`,`.git`,`__pycache__`को बाहर करें |
| गैर-रूट उपयोक्ता के रूप में चलाएँ | सुरक्षा सर्वोत्तम अभ्यास |
| मल्टी-स्टेज बिल्ड का उपयोग करें | अलग निर्माण और रनटाइम; छोटी अंतिम छवि |
| आधार छवि संस्करण पिन करें | प्रतिलिपि प्रस्तुत करने योग्य बिल्ड (`python:3.12.1-slim`,`python:latest`नहीं) |
### मल्टी-स्टेज बिल्ड उदाहरण
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

## डॉकर कंपोज़
डॉकर कंपोज़ एकल YAML फ़ाइल में मल्टी-कंटेनर अनुप्रयोगों को परिभाषित करता है।
### मुख्य आदेश
| आदेश | विवरण |
|---------|-----------------|
| `docker compose up -d`| पृष्ठभूमि में सभी सेवाएँ प्रारंभ करें |
| `docker compose down`| कंटेनर, नेटवर्क को रोकें और हटाएं |
| `docker compose down -v`| वॉल्यूम भी हटाएं |
| `docker compose logs -f`| सभी सेवाओं से लॉग का पालन करें |
| `docker compose ps`| चल रही सेवाओं की सूची |
| `docker compose build`| छवियों का पुनर्निर्माण करें |
| `docker compose exec web bash`| चालू सेवा में कमांड चलाएँ |
| `docker compose pull`| नवीनतम छवियाँ खींचें |
### उदाहरण फ़ाइल लिखें
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

## कुबेरनेट्स वास्तुकला
| घटक | भूमिका |
|--------|------|
| **क्लस्टर** | कंटेनरीकृत अनुप्रयोगों को चलाने वाले नोड्स (मशीनों) का एक सेट |
| **नियंत्रण विमान** | एपीआई सर्वर, शेड्यूलर, नियंत्रक प्रबंधक, आदि (क्लस्टर स्थिति) |
| **नोड** | एक वर्कर मशीन (वीएम या फिजिकल) जो पॉड्स चलाती है |
| **पॉड** | सबसे छोटी इकाई; एक या अधिक मजबूती से जुड़े कंटेनर |
| **तैनाती** | एक पॉड की प्रतिकृतियां प्रबंधित करता है; रोलिंग अपडेट को संभालता है |
| **सेवा** | पॉड्स के एक सेट के लिए स्थिर नेटवर्क एंडपॉइंट |
| **प्रवेश** | क्लस्टर के बाहर से सेवाओं तक HTTP रूटिंग |
| **कॉन्फिगमैप** | गैर-गुप्त कॉन्फ़िगरेशन डेटा |
| **गुप्त** | संवेदनशील डेटा (बेस64-एन्कोडेड) |
| **नेमस्पेस** | क्लस्टर के भीतर तार्किक अलगाव |
| **पर्सिस्टेंटवॉल्यूम (पीवी)** | क्लस्टर-स्तरीय भंडारण संसाधन |
| **पर्सिस्टेंटवॉल्यूमक्लेम (पीवीसी)** | पॉड द्वारा भंडारण के लिए अनुरोध |
---

## कुबेक्टल कमांड
### क्लस्टर जानकारी
| आदेश | विवरण |
|---------|-----------------|
| `kubectl cluster-info`| क्लस्टर समापन बिंदु विवरण |
| `kubectl get nodes`| सभी नोड्स की सूची बनाएं |
| `kubectl get namespaces`| सूची नामस्थान |
| `kubectl config current-context`| वर्तमान क्लस्टर संदर्भ दिखाएँ |
| `kubectl config use-context prod`| संदर्भ स्विच करें |
### कार्यभार
| आदेश | विवरण |
|---------|-----------------|
| `kubectl get pods`| वर्तमान नेमस्पेस में पॉड्स की सूची बनाएं |
| `kubectl get pods -A`| सभी नामस्थानों में पॉड्स की सूची बनाएं |
| `kubectl get deployments`| सूची तैनाती |
| `kubectl get services`| सूची सेवाएँ |
| `kubectl get ingress`| प्रवेश संसाधनों की सूची |
| `kubectl describe pod <name>`| विस्तृत पॉड जानकारी (घटनाएँ, स्थिति, विवरण) |
| `kubectl logs <pod>`| पॉड लॉग देखें |
| `kubectl logs -f <pod>`| पॉड लॉग का पालन करें |
| `kubectl logs <pod> -c <container>`| मल्टी-कंटेनर पॉड में एक विशिष्ट कंटेनर से लॉग |
| `kubectl exec -it <pod> -- bash`| एक फली में खोल |
| `kubectl delete pod <name>`| एक पॉड हटाएं (इसे इसके नियंत्रक द्वारा पुनः बनाया जाएगा) |
| `kubectl rollout status deployment/<name>`| रोलआउट प्रगति की जाँच करें |
| `kubectl rollout undo deployment/<name>`| पिछले संस्करण पर वापस जाएँ |
### कॉन्फ़िगरेशन लागू करना
| आदेश | विवरण |
|---------|-----------------|
| `kubectl apply -f deployment.yaml`| YAML मेनिफ़ेस्ट लागू करें |
| `kubectl apply -f ./dir/`| एक निर्देशिका में सभी YAML फ़ाइलें लागू करें |
| `kubectl delete -f deployment.yaml`| YAML फ़ाइल में परिभाषित संसाधनों को हटाएं |
| `kubectl scale deployment/web --replicas=5`| परिनियोजन स्केल करें |
| `kubectl set image deployment/web web=myapp:2.0`| कंटेनर छवि अपडेट करें |
---

## सामान्य कुबेरनेट्स प्रकट
### परिनियोजन
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

### सेवा
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

### प्रवेश
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

## हेल्म मूल बातें
हेल्म कुबेरनेट्स के लिए पैकेज मैनेजर है। यह कुबेरनेट्स संसाधनों को पुन: प्रयोज्य चार्ट में पैकेज करता है।
| आदेश | विवरण |
|---------|-----------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| एक चार्ट भंडार जोड़ें |
| `helm repo update`| स्थानीय चार्ट सूचकांक अद्यतन करें |
| `helm search repo nginx`| एक चार्ट खोजें |
| `helm install my-release bitnami/nginx`| एक चार्ट स्थापित करें |
| `helm install my-release bitnami/nginx --set replicaCount=3`| कस्टम मानों के साथ स्थापित करें |
| `helm install my-release bitnami/nginx -f values.yaml`| मान फ़ाइल के साथ स्थापित करें |
| `helm list`| स्थापित रिलीज़ों की सूची |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| किसी रिलीज़ को अपग्रेड करें |
| `helm rollback my-release 1`| पिछले पुनरीक्षण पर वापस जाएँ |
| `helm uninstall my-release`| किसी रिलीज़ को अनइंस्टॉल करें |
| `helm status my-release`| रिलीज़ स्थिति दिखाएँ |
---

## समस्या निवारण त्वरित संदर्भ
| समस्या | प्रयास करने का आदेश |
|------|----------------|
| पॉड प्रारंभ नहीं हो रहा है | `kubectl describe pod <name>`→ घटनाओं की जाँच करें |
| क्रैशलूपबैकऑफ़ | `kubectl logs <pod> --previous`→ देखें कि यह दुर्घटनाग्रस्त क्यों हुआ |
| छवि खींचने में त्रुटि | छवि का नाम, टैग और रजिस्ट्री क्रेडेंशियल जांचें |
| सेवा उपलब्ध नहीं है | `kubectl get endpoints <service>`→ क्या पॉड्स चयनित हैं? |
| OOMमार डाला | मेमोरी सीमा बढ़ाएँ या ऐप मेमोरी उपयोग को अनुकूलित करें |
| लंबित पॉड्स | `kubectl describe pod`→ नोड संसाधन, दोष, एफ़िनिटी की जाँच करें |
| डीएनएस मुद्दे | `kubectl exec <pod> -- nslookup kubernetes.default`|