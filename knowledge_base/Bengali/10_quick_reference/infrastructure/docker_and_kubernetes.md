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
# ডকার এবং কুবারনেটস চিট শীট
ডকারের সাথে অ্যাপ্লিকেশানগুলিকে ধারণ করার জন্য একটি ব্যবহারিক রেফারেন্স এবং কুবারনেটসের সাথে সেগুলিকে সাজানোর জন্য। কমান্ড লাইনের সাথে প্রাথমিক পরিচিতি অনুমান করে।
---

## ডকার ফান্ডামেন্টাল
| ধারণা | বর্ণনা |
|---------|---------------|
| **ছবি** | অ্যাপ কোড + নির্ভরতা + OS লাইব্রেরি সহ শুধুমাত্র পঠনযোগ্য টেমপ্লেট
| **ধারক** | একটি চিত্রের চলমান উদাহরণ; বিচ্ছিন্ন প্রক্রিয়া |
| **ডকারফাইল** | একটি ছবি নির্মাণের রেসিপি |
| **রেজিস্ট্রি** | ছবির জন্য স্টোরেজ (ডকার হাব, ইসিআর, জিসিআর, জিএইচসিআর) |
| **ভলিউম** | স্থায়ী সঞ্চয়স্থান যা কন্টেইনার পুনঃসূচনা থেকে বেঁচে থাকে |
| **নেটওয়ার্ক** | ভার্চুয়াল নেটওয়ার্ক সংযোগ পাত্রে |
---

## প্রয়োজনীয় ডকার কমান্ড
### ছবি
| আদেশ | বর্ণনা |
|---------|---------------|
| `docker build -t myapp:1.0 .`| একটি ডকারফাইল থেকে একটি ছবি তৈরি করুন |
| `docker images`| স্থানীয় ছবি তালিকাভুক্ত করুন |
| `docker pull nginx:latest`| একটি রেজিস্ট্রি থেকে একটি ছবি টানুন |
| `docker push myrepo/myapp:1.0`| একটি রেজিস্ট্রিতে একটি ছবি পুশ করুন |
| `docker rmi myapp:1.0`| একটি স্থানীয় ছবি সরান |
| `docker tag myapp:1.0 myrepo/myapp:1.0`| একটি রেজিস্ট্রির জন্য একটি ছবি ট্যাগ করুন |
| `docker image prune -a`| সমস্ত অব্যবহৃত ছবি সরান |
### ধারক
| আদেশ | বর্ণনা |
|---------|---------------|
| `docker run -d -p 8080:80 nginx`| পটভূমিতে একটি ধারক চালান, মানচিত্র পোর্ট 8080→80 |
| `docker run -it ubuntu bash`| একটি শেল দিয়ে ইন্টারেক্টিভভাবে চালান |
| `docker run --name web -e DB_HOST=db nginx`| ধারক নাম এবং পরিবেশ পরিবর্তনশীল সেট করুন |
| `docker ps`| চলমান পাত্রের তালিকা |
| `docker ps -a`| সমস্ত পাত্রের তালিকা করুন (বন্ধ করা সহ) |
| `docker stop web`| একটি চলমান ধারক বন্ধ করুন |
| `docker start web`| একটি বন্ধ পাত্রে শুরু করুন |
| `docker rm web`| একটি বন্ধ ধারক সরান |
| `docker exec -it web bash`| চলমান পাত্রের ভিতরে একটি শেল খুলুন |
| `docker logs -f web`| ধারক লগ অনুসরণ করুন |
| `docker inspect web`| বিস্তারিত কন্টেইনার মেটাডেটা (JSON) |
| `docker stats`| সমস্ত পাত্রের জন্য লাইভ সম্পদ ব্যবহার |
### পরিচ্ছন্নতা
| আদেশ | বর্ণনা |
|---------|---------------|
| `docker system prune -a`| সমস্ত অব্যবহৃত পাত্র, ছবি, নেটওয়ার্ক সরান এবং ক্যাশে তৈরি করুন |
| `docker volume prune`| সমস্ত অব্যবহৃত ভলিউম সরান |
| `docker container prune`| সব বন্ধ পাত্রে সরান |
---

## ডকারফাইল রেফারেন্স
### সাধারণ নির্দেশনা
| নির্দেশ | উদ্দেশ্য | উদাহরণ |
|---------------|---------|---------|
| `FROM`| বেস ইমেজ | `FROM python:3.12-slim`|
| `WORKDIR`| ছবির ভিতরে কাজের ডিরেক্টরি সেট করুন | `WORKDIR /app`|
| `COPY`| হোস্ট থেকে ইমেজে ফাইল কপি করুন | `COPY requirements.txt .`|
| `ADD`| কপির মত, কিন্তু tars বের করে এবং URL সমর্থন করে | `ADD app.tar.gz /app/`|
| `RUN`| বিল্ড করার সময় একটি কমান্ড চালান | `RUN pip install -r requirements.txt`|
| `CMD`| কন্টেইনার শুরু হলে ডিফল্ট কমান্ড | `CMD ["python", "app.py"]`|
| `ENTRYPOINT`| স্থির আদেশ; সিএমডি হয়ে গেলেন তর্ক | `ENTRYPOINT ["python"]`|
| `ENV`| পরিবেশ পরিবর্তনশীল সেট করুন | `ENV DATABASE_URL=postgres://...`|
| `EXPOSE`| ডকুমেন্ট কোন পোর্টে অ্যাপটি শোনে | `EXPOSE 8000`|
| `ARG`| বিল্ড-টাইম পরিবর্তনশীল | `ARG VERSION=1.0`|
| `USER`| নন-রুট ব্যবহারকারীতে স্যুইচ করুন | `USER appuser`|
| `HEALTHCHECK`| একটি স্বাস্থ্য পরীক্ষা কমান্ড সংজ্ঞায়িত করুন | `HEALTHCHECK CMD curl -f http://localhost:8000/health`|
| `VOLUME`| একটি মাউন্ট পয়েন্ট তৈরি করুন | `VOLUME /data`|
### সর্বোত্তম অভ্যাস
| অনুশীলন | কেন |
|------------|------|
| পাতলা/বেস ছবি ব্যবহার করুন | ছোট ছবি = দ্রুত টানা, ছোট আক্রমণ পৃষ্ঠ |
|`&&`এর সাথে RUN কমান্ড একত্রিত করুন | ইমেজ স্তর হ্রাস |
| প্রথমে নির্ভরতা ফাইলগুলি অনুলিপি করুন, তারপর কোড | ডকারের বিল্ড ক্যাশে ব্যবহার করে |
|`.dockerignore`ব্যবহার করুন |`node_modules`,`.git`,`__pycache__`বাদ দিন |
| অ-রুট ব্যবহারকারী হিসাবে চালান | নিরাপত্তা সর্বোত্তম অনুশীলন |
| মাল্টি-স্টেজ বিল্ড ব্যবহার করুন | পৃথক বিল্ড এবং রানটাইম; ছোট চূড়ান্ত চিত্র |
| পিন বেস ইমেজ সংস্করণ | প্রজননযোগ্য বিল্ড ( `python:3.12.1-slim`,`python:latest`নয়) |
### মাল্টি-স্টেজ বিল্ড উদাহরণ
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

## ডকার কম্পোজ
ডকার কম্পোজ একটি একক YAML ফাইলে মাল্টি-কন্টেইনার অ্যাপ্লিকেশন সংজ্ঞায়িত করে।
### কী কমান্ড
| আদেশ | বর্ণনা |
|---------|---------------|
| `docker compose up -d`| পটভূমিতে সমস্ত পরিষেবা শুরু করুন |
| `docker compose down`| বন্ধ করুন এবং পাত্রে অপসারণ করুন, নেটওয়ার্ক |
| `docker compose down -v`| এছাড়াও ভলিউম সরান |
| `docker compose logs -f`| সমস্ত পরিষেবা থেকে লগ অনুসরণ করুন |
| `docker compose ps`| চলমান পরিষেবার তালিকা করুন |
| `docker compose build`| ছবি পুনর্নির্মাণ |
| `docker compose exec web bash`| একটি চলমান পরিষেবাতে কমান্ড চালান |
| `docker compose pull`| সর্বশেষ ছবি টানুন |
### উদাহরণ কম্পোজ ফাইল
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

## কুবারনেটস আর্কিটেকচার
| উপাদান | ভূমিকা |
|------------|------|
| **গুচ্ছ** | নোডের একটি সেট (মেশিন) চলমান কন্টেইনারাইজড অ্যাপ্লিকেশন |
| **কন্ট্রোল প্লেন** | API সার্ভার, শিডিউলার, কন্ট্রোলার ম্যানেজার, etcd (ক্লাস্টার স্টেট) |
| **নোড** | একটি কর্মী মেশিন (ভিএম বা শারীরিক) যা পড চালায় |
| **পড** | ক্ষুদ্রতম একক; এক বা একাধিক শক্তভাবে সংযুক্ত পাত্রে |
| **নিয়োগ** | একটি পডের প্রতিলিপি পরিচালনা করে; রোলিং আপডেট পরিচালনা করে |
| **পরিষেবা** | পডের একটি সেটের জন্য স্থিতিশীল নেটওয়ার্ক এন্ডপয়েন্ট |
| **অনুপ্রবেশ** | ক্লাস্টারের বাইরে থেকে পরিষেবাগুলিতে HTTP রাউটিং |
| **কনফিগম্যাপ** | অ-গোপন কনফিগারেশন ডেটা |
| **গোপন** | সংবেদনশীল তথ্য (বেস64-এনকোডেড) |
| **নেমস্পেস** | একটি ক্লাস্টারের মধ্যে যৌক্তিক বিচ্ছিন্নতা |
| **পারসিস্টেন্ট ভলিউম (PV)** | ক্লাস্টার-স্তরের স্টোরেজ রিসোর্স |
| **পারসিস্টেন্ট ভলিউম ক্লেইম (পিভিসি)** | একটি পড দ্বারা সঞ্চয়ের জন্য অনুরোধ |
---

## kubectl কমান্ড
### ক্লাস্টার তথ্য
| আদেশ | বর্ণনা |
|---------|---------------|
| `kubectl cluster-info`| ক্লাস্টার এন্ডপয়েন্ট বিশদ |
| `kubectl get nodes`| সমস্ত নোড তালিকাভুক্ত করুন |
| `kubectl get namespaces`| নামস্থান তালিকা |
| `kubectl config current-context`| বর্তমান ক্লাস্টার প্রসঙ্গ দেখান |
| `kubectl config use-context prod`| প্রসঙ্গ পরিবর্তন করুন |
### কাজের চাপ
| আদেশ | বর্ণনা |
|---------|---------------|
| `kubectl get pods`| বর্তমান নামস্থানে পড তালিকাভুক্ত করুন |
| `kubectl get pods -A`| সমস্ত নামস্থান জুড়ে পড তালিকাভুক্ত করুন |
| `kubectl get deployments`| তালিকা স্থাপন |
| `kubectl get services`| তালিকা পরিষেবা |
| `kubectl get ingress`| প্রবেশ সম্পদ তালিকা |
| `kubectl describe pod <name>`| বিস্তারিত পড তথ্য (ইভেন্ট, অবস্থা, চশমা) |
| `kubectl logs <pod>`| পড লগ দেখুন |
| `kubectl logs -f <pod>`| পড লগ অনুসরণ করুন |
| `kubectl logs <pod> -c <container>`| একটি মাল্টি-কন্টেইনার পডে একটি নির্দিষ্ট ধারক থেকে লগ |
| `kubectl exec -it <pod> -- bash`| একটি শুঁটি মধ্যে শেল |
| `kubectl delete pod <name>`| একটি পড মুছুন (এটি এর নিয়ামক দ্বারা পুনরায় তৈরি করা হবে) |
| `kubectl rollout status deployment/<name>`| রোলআউট অগ্রগতি চেক করুন |
| `kubectl rollout undo deployment/<name>`| আগের সংস্করণে ফিরে যান |
### কনফিগারেশন প্রয়োগ করা হচ্ছে
| আদেশ | বর্ণনা |
|---------|---------------|
| `kubectl apply -f deployment.yaml`| একটি YAML ম্যানিফেস্ট প্রয়োগ করুন |
| `kubectl apply -f ./dir/`| একটি ডিরেক্টরিতে সমস্ত YAML ফাইল প্রয়োগ করুন |
| `kubectl delete -f deployment.yaml`| একটি YAML ফাইলে সংজ্ঞায়িত সংস্থান মুছুন |
| `kubectl scale deployment/web --replicas=5`| একটি স্থাপনার স্কেল করুন |
| `kubectl set image deployment/web web=myapp:2.0`| কন্টেইনার ইমেজ আপডেট করুন |
---

## সাধারণ কুবারনেটস ম্যানিফেস্ট
### স্থাপনা
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

### পরিষেবা
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

### প্রবেশ
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

## হেল্ম বেসিক
হেলম হলেন কুবারনেটসের প্যাকেজ ম্যানেজার। এটি কুবারনেটস সংস্থানগুলিকে পুনরায় ব্যবহারযোগ্য চার্টে প্যাকেজ করে।
| আদেশ | বর্ণনা |
|---------|---------------|
| `helm repo add bitnami https://charts.bitnami.com/bitnami`| একটি চার্ট সংগ্রহস্থল যোগ করুন |
| `helm repo update`| স্থানীয় চার্ট সূচক আপডেট করুন |
| `helm search repo nginx`| একটি চার্ট অনুসন্ধান করুন |
| `helm install my-release bitnami/nginx`| একটি চার্ট ইনস্টল করুন |
| `helm install my-release bitnami/nginx --set replicaCount=3`| কাস্টম মান দিয়ে ইনস্টল করুন |
| `helm install my-release bitnami/nginx -f values.yaml`| একটি মান ফাইলের সাথে ইনস্টল করুন |
| `helm list`| ইনস্টল করা রিলিজের তালিকা |
| `helm upgrade my-release bitnami/nginx --set image.tag=2.0`| একটি রিলিজ আপগ্রেড করুন |
| `helm rollback my-release 1`| আগের রিভিশনে ফিরে যান |
| `helm uninstall my-release`| একটি রিলিজ আনইনস্টল করুন |
| `helm status my-release`| প্রকাশের অবস্থা দেখান |
---

## দ্রুত রেফারেন্স সমস্যা সমাধান
| সমস্যা | চেষ্টা করার আদেশ |
|---------|----------------|
| পড শুরু হচ্ছে না | `kubectl describe pod <name>`→ ইভেন্ট পরীক্ষা করুন |
| CrashLoopBackOff | `kubectl logs <pod> --previous`→ দেখুন কেন এটি ক্র্যাশ হয়েছে |
| চিত্র টান ত্রুটি | ছবির নাম, ট্যাগ এবং রেজিস্ট্রি শংসাপত্র পরীক্ষা করুন |
| সেবা পৌঁছানো যাচ্ছে না | `kubectl get endpoints <service>`→ পড নির্বাচন করা হয়? |
| OOMKilled | মেমরি সীমা বাড়ান বা অ্যাপ মেমরি ব্যবহার অপ্টিমাইজ করুন |
| মুলতুবি পোড | `kubectl describe pod`→ চেক নোড রিসোর্স, টেন্টস, অ্যাফিনিটি |
| DNS সমস্যা | `kubectl exec <pod> -- nslookup kubernetes.default`|