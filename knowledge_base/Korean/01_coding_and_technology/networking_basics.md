<!--
---
# Metadata
title: "Networking Basics"
description: "OSI model, TCP/IP, protocols, security"
category: "Coding and Technology"
version: "1.0.0"
status: "active"

# Contribution
authors:
  - name: "Nepoznato-Dev"
    email: ""
    role: "original_author"
contributors: []
changelog:
  - version: "1.0.0"
    date: "2026-08-05"
    author: "Nepoznato-Dev"
    changes: "Added YAML frontmatter metadata for contributor tracking"

# Review
created: "2026-08-05"
last_modified: "2026-08-05"
review_date: "2027-02-05"
reviewed_by: "Coding & Technology Knowledge Base Team"
next_review: "2027-08-05"

# Classification
tags: [networking, coding-and-technology]
difficulty_level: "intermediate"
prerequisites: []
estimated_reading_time: "12 min"

# Contribution Guide
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
  how_to_contribute: "Submit a PR with changes and update the changelog"
  review_process: "Changes are reviewed by category maintainers before merge"
---

-->
# 네트워킹 기초
개발자와 시스템 관리자를 위한 실용적인 참고 자료 - 핵심 개념, 프로토콜, 명령 및 문제 해결.
---

## OSI 모델(7개 계층)
네트워크 통신을 이해하기 위한 개념적 프레임워크입니다.
| 레이어 | 이름 | 기능 | 예제 프로토콜 |
|-------|------|----------|------|
| 7 | 신청 | 최종 사용자 서비스 | HTTP, HTTPS, FTP, SMTP, DNS, SSH |
| 6 | 프리젠테이션 | 데이터 형식화, 암호화, 압축 | TLS, JPEG, ASCII |
| 5 | 세션 | 연결 관리 | NetBIOS, RPC |
| 4 | 교통 | End-to-End 전달, 오류수정, 흐름제어 | TCP, UDP |
| 3 | 네트워크 | 라우팅, 주소 지정 | IP, ICMP, OSPF, BGP |
| 2 | 데이터링크 | 프레이밍, 오류 감지, MAC 주소 | 이더넷, Wi-Fi, PPP |
| 1 | 물리적 | 원시 비트 전송 | 이더넷 케이블, 광섬유, 전파 |
실제로 인터넷에서는 **TCP/IP 모델**(4개 계층: 링크, 인터넷, 전송, 애플리케이션)이 더 일반적으로 사용됩니다.
---

## IP 주소 지정
### IPv4
- 4개의 옥텟으로 작성된 32비트 주소:`192.168.1.1`
- 전체: ~43억 개의 주소(그러나 실제로는 소진됨)
### IPv6
- 16진수로 작성된 128비트 주소:`2001:0db8:85a3:0000:0000:8a2e:0370:7334`
- 총계: 21²⁸ 주소(거의 무한).
### 개인 IP 범위(RFC 1918)
인터넷에서는 라우팅할 수 없습니다. 로컬 네트워크 내부에서 사용:
- `10.0.0.0/8`(10.0.0.0 – 10.255.255.255)
-`172.16.0.0/12`(172.16.0.0 – 172.31.255.255)
-`192.168.0.0/16`(192.168.0.0 – 192.168.255.255)
### CIDR 표기법
 `192.168.1.0/24`은 처음 24비트가 네트워크 접두사임을 의미합니다. 마지막 8비트는 호스트입니다. 여기에는`192.168.1.0`~`192.168.1.255`주소가 포함됩니다.
---

## DNS(도메인 이름 시스템)
도메인 이름(예:`example.com`)을 IP 주소에 매핑합니다.
### 레코드 유형
| 유형 | 목적 |
|------|---------|
| **아** | 도메인을 IPv4 주소에 매핑 |
| **아아아아** | 도메인을 IPv6 주소에 매핑 |
| **CNAME** | 다른 도메인 이름에 대한 별칭 |
| **MX** | 메일 교환 서버 |
| **TXT** | 임의의 텍스트(SPF, DKIM, 검증) |
| **NS** | 도메인의 네임서버 |
| **SRV** | 서비스 기록(예: SIP) |
### 공통 도구```bash
dig example.com            # DNS lookup (detailed)
nslookup example.com       # DNS lookup (simpler)
host example.com           # Quick lookup
dig -x 8.8.8.8             # Reverse lookup (IP to name)
```

---

## 포트 및 프로토콜
### 잘 알려진 포트(0–1023)
| 포트 | 프로토콜 | 서비스 |
|------|----------|---------|
| 20, 21 | TCP | FTP |
| 22 | TCP | SSH |
| 23 | TCP | 텔넷 |
| 25 | TCP | SMTP |
| 53 | UDP/TCP | DNS |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 123 | UDP | NTP |
| 143 | TCP | IMAP |
| 443 | TCP | HTTPS |
| 465 | TCP | SMTPS |
| 587 | TCP | SMTP(제출) |
| 993 | TCP | IMAPS |
| 995 | TCP | POP3S |
| 3306 | TCP | MySQL |
| 5432 | TCP | 포스트그레SQL |
| 6379 | TCP | 레디스 |
| 27017 | TCP | 몽고DB |
### 열린 포트 확인
```bash
ss -tulpn                 # Linux: listen and established sockets
netstat -an               # Older tool
lsof -i :8080             # See process using port 8080
nmap localhost            # Scan local ports
```

---

## TCP 대 UDP
| 기능 | TCP | UDP |
|---------|-------|------|
| 연결 | 연결 지향(핸드셰이크) | 무접속 |
| 신뢰성 | 배달 보장, 재전송 | 최선의 노력(패킷이 삭제될 수 있음) |
| 주문 | 질서 유지 | 주문 보장 없음 |
| 흐름 제어 | 예(슬라이딩 윈도우) | 아니요 |
| 사용 사례 | 웹(HTTP), 이메일, SSH, 파일 전송 | DNS, 스트리밍, VoIP, 게임, SNMP |
| 헤더 크기 | 20~60바이트 | 8바이트 |
---

## HTTP 및 HTTPS
### HTTP 메소드
| 방법 | 설명 |
|---------|-------------|
| **받기** | 리소스 검색(멱등성, 안전) |
| **포스트** | 데이터 제출(멱등성이 아님) |
| **넣어** | 리소스 업데이트/교체(멱등성) |
| **패치** | 부분 업데이트 |
| **삭제** | 리소스 제거(멱등성) |
### 상태 코드
| 코드 | 의미 |
|------|---------|
| **1xx** | 정보 제공(100 계속) |
| **2xx** | 성공(200 확인, 201 생성, 204 콘텐츠 없음) |
| **3xx** | 리디렉션(301 영구 이동, 302 발견, 304 수정되지 않음) |
| **4xx** | 클라이언트 오류(400 잘못된 요청, 401 승인되지 않음, 403 금지됨, 404 찾을 수 없음, 429 요청이 너무 많음) |
| **5xx** | 서버 오류(500 내부 서버 오류, 502 잘못된 게이트웨이, 503 서비스를 사용할 수 없음) |
### 헤더
| 헤더 | 목적 |
|---------|---------|
|  __보호됨_0__ | 미디어 유형(`application/json`,`text/html`) |
|  __보호됨_3__ | 자격 증명(예:`Bearer <token>`) |
|  __보호됨_5__ | 캐싱 정책 |
| CORS 헤더 | `Access-Control-Allow-Origin`등 |
---

## TLS/SSL
HTTP 트래픽을 암호화합니다(HTTPS = TLS를 통한 HTTP).
- CA(인증 기관)의 인증서가 서버를 인증합니다.
- 클라이언트 측에서 인증서 체인과 호스트 이름을 확인합니다.
---

## 방화벽과 NAT
### 방화벽
- 규칙(소스 IP, 대상 IP, 포트, 프로토콜)을 기반으로 트래픽을 필터링합니다.
- 상태 저장 방화벽은 연결 상태를 추적합니다.
### NAT(네트워크 주소 변환)
- 인터넷 접속을 위해 개인 IP를 공용 IP로 변환합니다.
- 포트 전달: 공용 포트를 내부 호스트/포트에 매핑합니다.
---

## 일반적인 네트워킹 명령
### 연결 테스트
```bash
ping google.com            # ICMP echo request
ping -c 4 8.8.8.8          # ping 4 times
traceroute google.com      # Trace the route (Linux)
tracert google.com         # Windows version
```

### 라우팅
```bash
ip route show              # Linux: routing table
route -n                   # Older Linux
netstat -r                 # Windows/Mac
```

### 네트워크 인터페이스
```bash
ip addr show               # List interfaces and IPs
ifconfig                   # Older command
```

### DNS
```bash
dig example.com
nslookup example.com
host example.com
```

### 포트 연결
```bash
nc -zv google.com 443      # Netcat: check if port 443 is open
telnet google.com 443      # Telnet to port
curl -v https://google.com # Verbose output
```

### 방화벽(리눅스 iptables/nftables)
```bash
sudo ufw status            # Ubuntu: simple firewall
sudo iptables -L -n        # List rules
```

### 네트워크 통계
```bash
ss -tulpn                  # Show listening sockets (Linux)
netstat -an                # All sockets (all OS)
```

---

## 서브넷팅(빠른 참조)
| CIDR | 넷마스크 | 주소 수 | 사용 가능한 호스트 |
|------|---------|---------|-------------|
| /32 | 255.255.255.255 | 1 | 1 |
| /30 | 255.255.255.252 | 4 | 2 |
| /29 | 255.255.255.248 | 8 | 6 |
| /28 | 255.255.255.240 | 16 | 14 |
| /27 | 255.255.255.224 | 32 | 30 |
| /26 | 255.255.255.192 | 64 | 62 |
| /25 | 255.255.255.128 | 128 | 126 |
| /24 | 255.255.255.0 | 256 | 254 |
| /23 | 255.255.254.0 | 512 | 510 |
| /22 | 255.255.252.0 | 1,024 | 1,022 |
| /16 | 255.255.0.0 | 65,536 | 65,534 |
| /8 | 255.0.0.0 | 16,777,216 | 16,777,214 |
---

## 로드 밸런싱 및 역방향 프록시
### Nginx를 역방향 프록시로 사용
```nginx
server {
    listen 80;
    server_name example.com;
    location / {
        proxy_pass http://localhost:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 로드 밸런싱 알고리즘
- **라운드 로빈**
- **최소 연결**
- **IP 해시**(세션 고정성)
- **가중 라운드 로빈**
### 도구
- **Nginx, HAProxy**(소프트웨어)
- **AWS ELB, Azure 로드 밸런서, GCP 클라우드 로드 밸런싱**(클라우드)
---

## 문제 해결 체크리스트
1. 물리적 링크가 작동 중인가요? (케이블, Wi-Fi 연결을 확인하세요).
2. 게이트웨이에 ping을 보낼 수 있나요? (예:`ping 192.168.1.1`).
3. 외부 IP로 핑을 보낼 수 있나요? (예:`8.8.8.8`).
4. 도메인을 확인할 수 있나요? ( __보호됨_2__ ).
5. 애플리케이션이 예상 포트에서 수신 대기하고 있습니까? ( __보호됨_3__ ).
6. 방화벽이 포트를 차단하고 있나요? (`iptables` /`ufw`또는 클라우드 보안 그룹을 확인하세요).
7. 애플리케이션 로그에 오류가 있나요?
8. TLS 인증서가 유효하고 신뢰할 수 있나요? ( __보호됨_6__ ).