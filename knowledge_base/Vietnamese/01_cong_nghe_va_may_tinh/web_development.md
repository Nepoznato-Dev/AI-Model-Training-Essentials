#Phát triển trang web

## Phát triển giao diện người dùng

### Công nghệ cốt lõi

#### HTML (Ngôn ngữ đánh dấu siêu văn bản)
- **HTML ngữ nghĩa**: Sử dụng các thẻ có ý nghĩa (`<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`)
- **Biểu mẫu**: Loại đầu vào, nhãn xác thực, khả năng truy cập
- **Phương tiện**: Nhúng hình ảnh, video, âm thanh
- **Thẻ Meta**: SEO, khung nhìn, mã hóa ký tự
- **Tính năng HTML5**: Canvas, SVG, bộ nhớ cục bộ, vị trí địa lý, ổ cắm web

#### CSS (Bảng định kiểu xếp tầng)
- **Mẫu hộp**: Nội dung, phần đệm, đường viền, lề
- **Hệ thống bố trí**:
  - **Flexbox**: Bố cục một chiều, căn chỉnh nội dung, căn chỉnh các mục
  - **Lưới**: Bố cục hai chiều, mẫu lưới, vùng lưới
  - **Định vị**: Tĩnh, tương đối, tuyệt đối, cố định, cố định
- **Thiết kế đáp ứng**: Truy vấn phương tiện, cách tiếp cận ưu tiên thiết bị di động
- **Biến CSS**: Thuộc tính tùy chỉnh cho chủ đề
- **Hoạt ảnh**: Chuyển tiếp, khung hình chính, biến đổi
- **Bộ tiền xử lý**: Sass, Less (biến, mixins, lồng nhau)

####Javascript
- **Thao tác DOM**: Chọn, tạo, sửa đổi các phần tử
- **Sự kiện**: Nhấp chuột, gửi, bàn phím, sự kiện tùy chỉnh, ủy quyền sự kiện
- **Tính năng ES6+**: Chức năng mũi tên, phá hủy, trải rộng/nghỉ ngơi, mô-đun, không đồng bộ/chờ đợi
- **API**: Tìm nạp, XMLHttpRequest, localStorage, sessionStorage
- **TypeScript**: Gõ tĩnh, giao diện, khái quát, trang trí

### Khung giao diện người dùng hiện đại

#### Phản ứng
- **Thành phần**: Thành phần chức năng, thành phần lớp
- **Hooks**: useState, useEffect, useContext, useReducer, hook tùy chỉnh
- **Quản lý trạng thái**: API ngữ cảnh, Redux, Zustand, Recoil
- **Định tuyến**: Bộ định tuyến React (Trình duyệtRouter, Tuyến đường, Tuyến đường, Liên kết)
- **Hệ sinh thái**: Next.js (SSR, SSG), Remix, Gatsby
- **Virtual DOM**: Hiển thị hiệu quả thông qua thuật toán khác biệt

#### Vue.js
- **API tùy chọn**: dữ liệu, phương thức, tính toán, xem
- **Composition API**: setup(), ref, phản ứng, được tính toán
- **Chỉ thị**: v-if, v-for, v-bind, v-on, v-model
- **Vuex/Pinia**: Quản lý nhà nước
- **Vue Router**: Định tuyến phía máy khách
- **Nuxt.js**: Khung kết xuất phía máy chủ

#### Góc cạnh
- **Thành phần**: Trang trí, mẫu, móc vòng đời
- **Dịch vụ**: Chèn phần phụ thuộc, mẫu đơn
- **RxJS**: Lập trình phản ứng, quan sát được
- **Định tuyến**: RouterModule, bộ bảo vệ, bộ phân giải
- **Biểu mẫu**: Biểu mẫu phản hồi, dựa trên mẫu
- **NgRx**: Quản lý trạng thái theo phong cách Redux

### Công cụ xây dựng và gói
- **Webpack**: Đóng gói mô-đun, tách mã, trình tải, plugin
- **Vite**: Công cụ xây dựng nhanh bằng mô-đun ES gốc
- **Bưu kiện**: Bộ đóng gói không có cấu hình
- **Rollup**: Tối ưu hóa cho thư viện
- **esbuild**: Trình đóng gói JavaScript cực nhanh
- **Babel**: Trình biên dịch JavaScript để tương thích ngược
- **PostCSS**: Xử lý CSS bằng plugin

### Thư viện và khung CSS
- **Bootstrap**: Thư viện thành phần, hệ thống lưới, tiện ích
- **Tailwind CSS**: Khung CSS tiện ích đầu tiên
- **Giao diện người dùng Material**: Triển khai Material Design của Google
- **Chakra UI**: Thư viện thành phần có thể truy cập
- **Ant Design**: Các thành phần giao diện người dùng cấp doanh nghiệp
- **Thành phần được tạo kiểu**: Thư viện CSS-in-JS
- **Cảm xúc**: CSS-in-JS với bản đồ nguồn

## Phát triển phụ trợ

### Ngôn ngữ phía máy chủ

#### Node.js
- **Thời gian chạy**: JavaScript trên máy chủ (động cơ V8)
- **Express.js**: Khung web tối thiểu, kiến trúc phần mềm trung gian
- **NestJS**: Kiến trúc lấy cảm hứng từ góc cạnh, TypeScript
- **Fastify**: Khung hiệu suất cao
- **Koa**: Modern Express của cùng những người sáng tạo
- **Quản lý gói**: npm, sợi, pnpm

#### Python
- **Django**: Khung đầy đủ tính năng, ORM, bảng quản trị, bao gồm pin
- **Bình**: Microframework, hệ sinh thái mở rộng
- **FastAPI**: Tài liệu API hiện đại, không đồng bộ, tự động
- **Kim tự tháp**: Khung linh hoạt, có thể mở rộng

#### Ngôn ngữ phụ trợ khác
- **Ruby on Rails**: Quy ước về cấu hình, ActiveRecord ORM
- **Java Spring**: Khung doanh nghiệp, nội dung phụ thuộc
- **PHP Laravel**: Cú pháp tinh tế, ORM Eloquent, tạo khuôn mẫu Blade
- **Go Gin**: Hiệu suất cao, khung tối thiểu
- **Rust Actix**: An toàn bộ nhớ, hiệu suất
- **C# ASP.NET Core**: Tính năng đa nền tảng, dành cho doanh nghiệp

### Tích hợp cơ sở dữ liệu

#### ORM (Ánh xạ quan hệ đối tượng)
- **Phần tiếp theo**: Node.js ORM cho cơ sở dữ liệu SQL
- **Prisma**: Truy cập cơ sở dữ liệu an toàn theo kiểu, ứng dụng khách được tạo tự động
- **SQLAlchemy**: Bộ công cụ Python SQL và ORM
- **ActiveRecord**: Ruby on Rails ORM
- **Ngủ đông**: Java ORM
- **Khung thực thể**: .NET ORM

#### Trình điều khiển cơ sở dữ liệu
- **pg**: Máy khách PostgreSQL cho Node.js
- **mysql2**: Máy khách MySQL với những lời hứa
- **pymongo**: Trình điều khiển MongoDB cho Python
- **redis**: Ứng dụng khách Redis cho nhiều ngôn ngữ

### Phát triển API#### API REST
- **Phương thức HTTP**: GET, POST, PUT, PATCH, DELETE
- **Mã trạng thái**: 200, 201, 400, 401, 403, 404, 500
- **Đặt tên tài nguyên**: Danh từ, số nhiều, phân cấp
- **Phiên bản**: đường dẫn URL, tiêu đề, tham số truy vấn
- **Xác thực**: JWT, OAuth, khóa API
- **Tài liệu**: OpenAPI/Swagger, Postman

####GraphQL
- **Định nghĩa lược đồ**: Loại, truy vấn, đột biến, đăng ký
- **Trình giải quyết**: Tìm nạp dữ liệu cấp trường
- **Máy chủ Apollo**: Triển khai máy chủ GraphQL
- **Chuyển tiếp**: Ứng dụng khách GraphQL của Facebook
- **Ưu điểm**: Không tìm nạp quá mức, điểm cuối duy nhất, gõ mạnh

#### gRPC
- **Bộ đệm giao thức**: Ngôn ngữ định nghĩa giao diện
- **HTTP/2**: Truyền phát hai chiều
- **Trường hợp sử dụng**: Giao tiếp vi dịch vụ, ứng dụng thời gian thực

### Xác thực và ủy quyền
- **Dựa trên phiên**: Cookie, phiên phía máy chủ
- **Dựa trên mã thông báo**: JWT (Mã thông báo web JSON), không trạng thái
- **OAuth 2.0**: Khung ủy quyền, đăng nhập bên thứ ba
- **OpenID Connect**: Lớp nhận dạng trên OAuth 2.0
- **SAML**: Đăng nhập một lần dành cho doanh nghiệp
- **Băm mật khẩu**: bcrypt, argon2, scrypt
- **Xác thực đa yếu tố**: TOTP, SMS, mã email

## DevOps và triển khai

### Kiểm soát phiên bản
- **Git**: Kiểm soát phiên bản phân tán
- **GitHub/GitLab/Bitbucket**: Lưu trữ kho lưu trữ
- **Chiến lược phân nhánh**: Git Flow, GitHub Flow, phát triển dựa trên thân cây
- **CI/CD**: Quy trình triển khai và thử nghiệm tự động

### Container hóa
- **Docker**: Thời gian chạy vùng chứa, Dockerfile, hình ảnh
- **Docker Compose**: Phối hợp nhiều vùng chứa
- **Đăng ký vùng chứa**: Docker Hub, AWS ECR, Google GCR
- **Các phương pháp hay nhất**: Bản dựng nhiều giai đoạn, hình ảnh cơ sở tối thiểu

### Hòa âm
- **Kubernetes**: Điều phối vùng chứa, nhóm, dịch vụ, triển khai
- **Helm**: Trình quản lý gói Kubernetes
- **Lưới dịch vụ**: Istio, Linkerd cho mạng vi dịch vụ

### Nền tảng đám mây
- **AWS**: EC2, S3, Lambda, RDS, CloudFront, ECS/EKS
- **Google Cloud**: Công cụ điện toán, Lưu trữ đám mây, Chức năng đám mây, GKE
- **Azure**: Máy ảo, Bộ lưu trữ Blob, Chức năng, AKS
- **Vercel**: Triển khai giao diện người dùng, các chức năng serverless
- **Netlify**: Lưu trữ trang web tĩnh, chức năng serverless
- **Heroku**: Nền tảng dưới dạng dịch vụ (PaaS)
- **DigitalOcean**: Cơ sở hạ tầng đám mây được đơn giản hóa

### Đường ống CI/CD
- **Hành động GitHub**: Tự động hóa quy trình làm việc
- **GitLab CI**: Tích hợp liên tục
- **Jenkins**: Máy chủ tự động hóa mở rộng
- **CircleCI**: CI/CD dựa trên đám mây
- **Travis CI**: Dịch vụ tích hợp liên tục
- **ArgoCD**: Phân phối liên tục GitOps cho Kubernetes

### Giám sát và ghi nhật ký
- **Hiệu suất ứng dụng**: Relic mới, Datadog, AppDynamics
- **Theo dõi lỗi**: Sentry, Rollbar, Bugsnag
- **Ghi nhật ký**: ELK Stack (Elasticsearch, Logstash, Kibana), Splunk
- **Giám sát thời gian hoạt động**: Pingdom, UptimeRobot
- **Analytics**: Google Analytics, Mixpanel, Amplitude

## Hiệu suất Web

### Kỹ thuật tối ưu hóa
- **Tách mã**: Tải chậm, nhập động
- **Rung cây**: Xóa mã không sử dụng
- **Giảm thiểu**: Giảm kích thước tệp
- **Nén**: Gzip, Brotli
- **Bộ nhớ đệm**: Bộ nhớ đệm của trình duyệt, CDN, nhân viên dịch vụ
- **Tối ưu hóa hình ảnh**: WebP, AVIF, tải chậm, hình ảnh phản hồi
- **CSS quan trọng**: Nội tuyến các kiểu trong màn hình đầu tiên
- **Tối ưu hóa cơ sở dữ liệu**: Lập chỉ mục, tối ưu hóa truy vấn, tổng hợp kết nối

### Các chỉ số quan trọng về trang web cốt lõi
- **LCP (Sơn có nội dung lớn nhất)**: Hiệu suất tải (<2,5 giây)
- **FID (Độ trễ đầu vào đầu tiên)**: Tính tương tác (<100ms)
- **CLS (Thay đổi bố cục tích lũy)**: Độ ổn định hình ảnh (<0,1)
- **INP (Tương tác với lần sơn tiếp theo)**: Chỉ số về độ phản hồi

### Mạng phân phối nội dung (CDN)
- **Cloudflare**: Bảo mật, hiệu suất, DNS
- **Akamai**: CDN doanh nghiệp
- **Amazon CloudFront**: AWS CDN
- **Nhanh chóng**: Nền tảng đám mây biên
- **StackPath**: Dịch vụ biên

## Bảo mật web

### Các lỗ hổng phổ biến (Top 10 OWASP)
- **Tiêm**: Chèn SQL, chèn lệnh
- **Xác thực bị hỏng**: Chiếm quyền điều khiển phiên, nhồi thông tin xác thực
- **Lộ lộ dữ liệu nhạy cảm**: Dữ liệu không được mã hóa, mật mã yếu
- **Thực thể bên ngoài XML (XXE)**: Lỗ hổng của trình phân tích cú pháp XML
- **Kiểm soát truy cập bị hỏng**: Leo thang đặc quyền, truy cập trái phép
- **Cấu hình sai bảo mật**: Thông tin xác thực mặc định, lỗi dài dòng
- **Tập lệnh chéo trang (XSS)**: Được phản ánh, lưu trữ, dựa trên DOM
- **Khử lưu huỳnh không an toàn**: Tấn công chèn đối tượng
- **Sử dụng các thành phần có lỗ hổng đã biết**: Các phần phụ thuộc đã lỗi thời
- **Ghi nhật ký và giám sát không đầy đủ**: Không phát hiện được vi phạm

### Các phương pháp bảo mật tốt nhất
- **HTTPS**: Mã hóa TLS/SSL, HSTS
- **Chính sách bảo mật nội dung (CSP)**: Ngăn chặn các cuộc tấn công XSS
- **Xác thực đầu vào**: Vệ sinh đầu vào của người dùng
- **Mã hóa đầu ra**: Ngăn chặn các cuộc tấn công tiêm nhiễm
- **Bảo vệ CSRF**: Mã thông báo chống CSRF, cookie SameSite
- **Giới hạn tỷ lệ**: Ngăn chặn các cuộc tấn công vũ phu
- **Tiêu đề bảo mật**: X-Frame-Options, X-Content-Type-Options
- **Quét phụ thuộc**: kiểm toán npm, Snyk, Dependabot

##Thử nghiệm### Các loại thử nghiệm
- **Kiểm tra đơn vị**: Các thành phần/chức năng riêng lẻ
- **Thử nghiệm tích hợp**: Tương tác thành phần
- **End-to-End (E2E)**: Quy trình làm việc đầy đủ của người dùng
- **Hồi quy trực quan**: Phát hiện thay đổi giao diện người dùng
- **Kiểm tra hiệu suất**: Kiểm tra tải, ứng suất, tăng đột biến
- **Kiểm tra khả năng truy cập**: Tuân thủ WCAG

### Khung kiểm tra
- **Jest**: Khung kiểm tra JavaScript
- **Mocha**: Chạy thử linh hoạt
- **pytest**: Khung thử nghiệm Python
- **RSpec**: Khung thử nghiệm Ruby
- **JUnit**: Khung thử nghiệm Java

### Công cụ kiểm tra E2E
- **Selenium**: Tự động hóa trình duyệt
- **Cypress**: Thử nghiệm E2E hiện đại
- **Nhà viết kịch**: Tự động hóa trên nhiều trình duyệt
- **Người múa rối**: Điều khiển Chrome không đầu

## Khả năng tiếp cận (a11y)

### Nguyên tắc WCAG
- **Có thể nhận biết**: Văn bản thay thế, chú thích, nội dung có thể điều chỉnh
- **Có thể hoạt động**: Điều hướng bằng bàn phím, đủ thời gian, không bị giật
- **Có thể hiểu được**: Có thể đọc được, có thể dự đoán được, hỗ trợ đầu vào
- **Mạnh mẽ**: Tương thích với các công nghệ hỗ trợ

### Triển khai
- **HTML ngữ nghĩa**: Phân cấp tiêu đề, mốc phù hợp
- **Thuộc tính ARIA**: Vai trò, trạng thái, thuộc tính
- **Quản lý tiêu điểm**: Chỉ báo tiêu điểm hiển thị, thứ tự tab hợp lý
- **Độ tương phản màu**: Tỷ lệ văn bản tối thiểu 4,5:1
- **Kiểm tra trình đọc màn hình**: NVDA, JAWS, VoiceOver
- **Điều hướng bàn phím**: Có thể truy cập tất cả các yếu tố tương tác

## Ứng dụng web lũy tiến (PWA)

### Tính năng PWA
- **Nhân viên dịch vụ**: Chức năng ngoại tuyến, đồng bộ hóa nền
- **Bản kê khai ứng dụng web**: Lời nhắc cài đặt, biểu tượng, màu chủ đề
- **App Shell**: Khung giao diện người dùng được lưu trong bộ nhớ đệm
- **Thông báo đẩy**: Sự tham gia của người dùng
- **Thiết kế đáp ứng**: Hoạt động trên tất cả các thiết bị
- **Yêu cầu HTTPS**: Bối cảnh an toàn

### Công cụ
- **Workbox**: Thư viện của nhân viên dịch vụ
- **Lighthouse**: Kiểm toán PWA
- **PWA Builder**: Tạo bảng kê khai và biểu tượng

## Công nghệ mới nổi

### WebAssugging (Wasm)
- **Mục đích**: Chạy mã đã biên dịch trong trình duyệt ở tốc độ gần như gốc
- **Ngôn ngữ**: Mục tiêu biên dịch C++, Rust, Go
- **Trường hợp sử dụng**: Trò chơi, chỉnh sửa video, mật mã, suy luận ML

### Kiến trúc không máy chủ
- **Chức năng như một dịch vụ**: AWS Lambda, Azure Functions, Google Cloud Functions
- **Lợi ích**: Không cần quản lý máy chủ, tự động mở rộng quy mô, trả tiền cho mỗi lần sử dụng
- **Cân nhắc**: Khởi động nguội, khóa nhà cung cấp, độ phức tạp của việc gỡ lỗi

### Kiến trúc Jamstack
- **JavaScript**: Tính tương tác phía máy khách
- **API**: Chức năng không có máy chủ, dịch vụ của bên thứ ba
- **Đánh dấu**: Tệp tĩnh dựng sẵn
- **Công cụ**: Next.js, Gatsby, Hugo, Eleventy
- **Lợi ích**: Hiệu suất, bảo mật, khả năng mở rộng, trải nghiệm của nhà phát triển

### Giao tiếp thời gian thực
- **WebSockets**: Giao tiếp hai chiều
- **Sự kiện do máy chủ gửi**: Truyền phát từ máy chủ đến máy khách
- **WebRTC**: Video, âm thanh, dữ liệu ngang hàng
- **Trường hợp sử dụng**: Trò chuyện, cộng tác, phát trực tiếp, chơi trò chơi

### Giao diện người dùng vi mô
- **Khái niệm**: Mở rộng vi dịch vụ sang giao diện người dùng
- **Phương pháp tiếp cận**: Tích hợp tại thời điểm xây dựng, thời gian chạy, biên
- **Lợi ích**: Triển khai độc lập, tự chủ nhóm
- **Thách thức**: Tính nhất quán, hiệu suất, độ phức tạp