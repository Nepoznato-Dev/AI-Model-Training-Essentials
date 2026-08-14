<!--
---
# Metadata
title: "Lisp & Clojure — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Lisp and Clojure ecosystem including tools, frameworks, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [lisp, clojure, ecosystem, tooling, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "15 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# Lisp & Clojure — Hướng dẫn về hệ sinh thái và công cụ
Hướng dẫn này bao gồm các công cụ, khung và cơ sở hạ tầng thiết yếu trong hệ sinh thái Lisp và Clojure.
---

## Triển khai Lisp & Clojure
| Thực hiện | Ngôn ngữ | Ghi chú |
|--------------|----------|-------|
| **Clojure** | JVM | Lisp hiện đại trên JVM |
| **ClojureScript** | JS | Clojure được biên dịch sang JavaScript |
| **SBCL** | Lisp thông thường | CL hiệu suất cao |
| **CCL** | Lisp thông thường | OpenMCL, biên dịch nhanh |
| **ECL** | Lisp thông thường | Có thể nhúng, tương tác C |
| **Emacs Lisp** | Emac | Ngôn ngữ mở rộng |
| **Vợt** | Đề án | Lập trình hướng ngôn ngữ |
| **Lỗi** | Đề án | Ngôn ngữ mở rộng GNU |
```bash
clojure --version           # Clojure version
clj -M:run                  # run project
bb                          # Babashka (fast Clojure)
sbcl --version              # SBCL version
racket --version            # Racket version
```

---

## Công cụ Clojure
| Công cụ | Mục đích |
|------|----------|
| **Clojure CLI (clj)** | Công cụ CLI chính thức |
| **Leiningen** | Công cụ dự án cổ điển |
| **deps.edn** | Quản lý phụ thuộc |
| **Babashka** | Kịch bản Clojure nhanh |
| **tools.build** | Xây dựng tự động hóa |
| **bóng-cljs** | Bản dựng ClojureScript |
| **Bánh xe sung** | Tải lại ClojureScript trực tiếp |
```clojure
;; deps.edn
{:paths ["src" "resources"]
 :deps {org.clojure/clojure {:mvn/version "1.11.1"}
        ring/ring-core {:mvn/version "1.11.0"}
        ring/ring-jetty-adapter {:mvn/version "1.11.0"}
        com.github.seancorfield/next.jdbc {:mvn/version "1.3.909"}}
 
 :aliases
 {:run {:main-opts ["-m" "myapp.core"]}
  :test {:extra-paths ["test"]
         :extra-deps {io.github.cognitect-labs/test-runner {:git/tag "v0.5.1"}}
         :main-opts ["-m" "cognitect.test-runner"]}
  :build {:deps {io.github.clojure/tools.build {:mvn/version "0.9.6"}}
          :ns-default build}}}
```

```bash
clj -M:run                # run with alias
clj -M:test               # run tests
clj -T:build jar          # build JAR
clj -M:nrepl              # start REPL
bb -e '(+ 1 2 3)'        # Babashka inline
```

---

## Công cụ Lisp thông dụng
| Công cụ | Mục đích |
|------|----------|
| **Quicklisp** | Quản lý gói |
| **ASDF** | Xây dựng hệ thống |
| **Roswell** | Quản lý môi trường Lisp |
| **QLô** | Quản lý phụ thuộc cục bộ |
| **NHỎNG** | Emacs Lisp IDE |
| **Rác rưởi** | Emacs Lisp IDE (ngã ba SLIME) |
```lisp
;; Quicklisp
(ql:quickload "hunchentoot")  ; install/load library
(ql:quickload "cl-json")
(ql:update-all-dists)          ; update all

;; ASDF system definition
(asdf:defsystem myapp
  :description "My application"
  :depends-on ("hunchentoot" "cl-json")
  :components ((:file "package")
               (:file "main" :depends-on ("package"))))
```

---

## Khung web
| Khung | Ngôn ngữ | Loại |
|----------|----------|------|
| **Nhẫn + Compojure** | Clojure | Trình xử lý HTTP + định tuyến |
| **Bệ** | Clojure | Web đầy đủ |
| **Luminus** | Clojure | Ngăn xếp khung web |
| ** Nhắc lại** | Clojure | Thư viện định tuyến |
| **Thở khò khè** | CL | Máy chủ HTTP |
| **Người thượng cổ** | CL | Khung web |
| **Nghỉ ngơi** | CL | Khung REST |
```clojure
;; Ring + Compojure example
(ns myapp.handler
  (:require [compojure.core :refer [defroutes GET POST]]
            [compojure.route :as route]
            [ring.middleware.json :refer [wrap-json-body wrap-json-response]]
            [ring.adapter.jetty :refer [run-jetty]]))

(defroutes app-routes
  (GET "/" [] "Hello, World!")
  (GET "/users/:id" [id] {:status 200 :body {:id id :name "User"}})
  (route/not-found "Not Found"))

(def app (-> app-routes wrap-json-response (wrap-json-body {:keywords? true})))

(defn -main [] (run-jetty app {:port 8080}))
```

---

## Cơ sở dữ liệu
| Công nghệ | Ngôn ngữ | Loại |
|----------||----------|------|
| **tiếp theo.jdbc** | Clojure | Trình bao bọc JDBC |
| **HugSQL** | Clojure | SQL đầu tiên |
| ** mật ong ** | Clojure | DSL SQL |
| **clojure.jdbc** | Clojure | Giao diện JDBC |
| **Hậu hiện đại** | CL | PostgreSQL |
| **CLSQL** | CL | Giao diện SQL |
| **SxQL** | CL | DSL SQL |
```clojure
;; next.jdbc example
(require '[next.jdbc :as jdbc]
         '[next.jdbc.result-set :as rs])

(def db {:dbtype "postgresql" :dbname "mydb" :user "admin" :password "secret"})

(defn find-users [min-age]
  (jdbc/execute! db
    ["SELECT id, name, email FROM users WHERE age > ?" min-age]
    {:builder-fn rs/as-unqualified-lower-maps}))
```

---

##Thử nghiệm
| Khung | Ngôn ngữ | Mục đích |
|----------|----------|----------|
| **clojure.test** | Clojure | Thử nghiệm tích hợp |
| **midje** | Clojure | Thử nghiệm kiểu BDD |
| **kỳ vọng** | Clojure | Dựa trên kỳ vọng |
| **kiểm tra.kiểm tra** | Clojure | Dựa trên thuộc tính (QuickCheck) |
| **Năm giờ sáng** | CL | Kiểm tra đơn vị |
| **chứng minh** | CL | Khung kiểm tra |
| **đơn vị lisp** | CL | Kiểm tra đơn vị |
```clojure
;; clojure.test
(ns myapp.user-service-test
  (:require [clojure.test :refer [deftest testing is are]]
            [myapp.user-service :as sut]))

(deftest find-user-test
  (testing "returns user when found"
    (let [repo (atom {1 {:id 1 :name "Alice"}})
          user (sut/find-user repo 1)]
      (is (= "Alice" (:name user)))))
  
  (testing "returns nil when not found"
    (let [repo (atom {})
          user (sut/find-user repo 999)]
      (is (nil? user)))))

;; test.check (property-based)
(require '[clojure.test.check :as tc]
         '[clojure.test.check.generators :as gen]
         '[clojure.test.check.properties :as prop])

(tc/quick-check 100
  (prop/for-all [v (gen/vector gen/int)]
    (= (sort v) (sort (sort v)))))
```

---

## Chất lượng mã
| Công cụ | Ngôn ngữ | Mục đích |
|------|----------|----------|
| **clj-kondo** | Clojure | Kẻ nói dối |
| **cljfmt** | Clojure | Trình định dạng |
| **eastwood** | Clojure | Lining |
| **kibit** | Clojure | Gợi ý mã |
| **alex-và-terrys** | Clojure | Hướng dẫn phong cách |
| **alex-cộng** | CL | Phân tích mã |
```bash
clj-kondo --lint src/     # lint
cljfmt check src/         # check formatting
cljfmt fix src/           # fix formatting
```

---

## Thư viện chính
| Thư viện | Ngôn ngữ | Mục đích |
|----------|----------|---------|
| **core.async** | Clojure | Đồng thời CSP |
| **đầu dò** | Clojure | Thuật toán tổng hợp |
| **bóng ma** | Clojure | Điều hướng dữ liệu |
| **lược đồ** | Clojure | Xác thực dữ liệu |
| **mali** | Clojure | Xác thực dữ liệu |
| **data.json** | Clojure | JSON |
| **cheshire** | Clojure | JSON (nhanh hơn) |
| **nấc** | Clojure | Tạo HTML |
| **đóng khung lại** | ClojureScript | Khung SPA |
| **thuốc thử** | ClojureScript | Trình bao bọc phản ứng |
| **Ôi** | ClojureScript | Giao diện phản ứng |
| **core.match** | Clojure | Khớp mẫu |
| **tools.logging** | Clojure | Ghi nhật ký |
| **gắn kết** | Clojure | Quản lý nhà nước |
| **tích phân** | Clojure | Hệ thống thành phần |
| **usocket** | CL | Thư viện ổ cắm |
| **chủ đề bordeaux** | CL | Luồng |
| **Alexandria** | CL | Thư viện tiện ích |
---

## IDE & Trình chỉnh sửa
| IDE | Điểm mạnh |
|------|-------------|
| **Mã VS + Calva** | IDE Clojure tốt nhất |
| **CIDER (Emacs)** | IDE Clojure cổ điển |
| **IntelliJ + Chữ thảo** | JetBrains Clojure |
| **SLIME / ranh mãnh** | Lisp thông thường (Emacs) |
| **Lêm** | IDE Lisp thông thường |
| **Vim + Lò sưởi** | Vim Clojure |
---

## Triển khai
| Phương pháp | Ghi chú |
|--------|-------|
| **Uberjar** | `clj -T:build jar`(Clojure) |
| **Bản địa GraalVM** | Hình ảnh gốc (có giới hạn) |
| **Docker** | Được đóng gói |
| **Babashka** | Viết kịch bản nhanh |
| **Nhị phân Lisp** | Biên dịch nhị phân (SBCL) |
| **Kubernetes** | Dàn nhạc |
---

## Bản tóm tắt
Hệ sinh thái Lisp trải rộng trên nhiều phương ngữ: **Clojure** (JVM, hiện đại), **Common Lisp** (cổ điển, ANSI), **Racket** (hướng ngôn ngữ) và **Emacs Lisp** (kịch bản soạn thảo). Ngăn xếp tiêu chuẩn của Clojure là: **Clojure CLI** với **deps.edn** cho bản dựng, **Ring + Compojure** hoặc **Pedestal** cho web, **next.jdbc** cho cơ sở dữ liệu, **clojure.test** cho thử nghiệm, **clj-kondo** cho linting và **VS Code + Calva** hoặc **CIDER** làm IDE. Lisp thông thường sử dụng **Quicklisp** cho các gói, **SBCL** để biên dịch và **SLIME** để phát triển. Điểm mạnh của Lisp là macro, tính đồng âm, phát triển dựa trên REPL và lập trình tương tác. Hệ sinh thái vượt trội ở khả năng tạo mẫu nhanh, ngôn ngữ dành riêng cho miền và xử lý dữ liệu.