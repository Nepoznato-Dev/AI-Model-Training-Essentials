# प्रौद्योगिकी और कंप्यूटिंग

## कंप्यूटर क्या है?

कंप्यूटर एक electronic device है जो program कहलाने वाले instructions के एक set के अनुसार data को process करता है। आधुनिक computers von Neumann architecture पर आधारित हैं, जिसमें central processing unit (CPU), memory, storage, और input/output devices शामिल होते हैं। CPU instructions को execute करता है। RAM (random access memory), computer के चलने के दौरान data को अस्थायी रूप से store करती है। SSDs और hard drives जैसे storage devices data को स्थायी रूप से store करते हैं।

## प्रोग्रामिंग भाषाएँ

Programming language एक formal language है जिसका उपयोग computers के लिए instructions लिखने में किया जाता है। Python एक high-level, interpreted, general-purpose programming language है जो अपने simple syntax और readability के लिए जानी जाती है। इसका व्यापक उपयोग data science, machine learning, web development और automation में होता है। JavaScript web development की प्रमुख भाषा है और browsers में चलती है। Java एक compiled, object-oriented language है जिसका enterprise software और Android development में व्यापक उपयोग होता है। C और C++ lower-level languages हैं जो hardware पर fine-grained control देती हैं और system programming, game development तथा performance-critical applications में उपयोग की जाती हैं। Rust एक आधुनिक systems programming language है जो safety और performance पर केंद्रित है।

## इंटरनेट कैसे काम करता है

Internet परस्पर जुड़े computers का एक वैश्विक network है जो standardized protocols का उपयोग करके संचार करता है। World Wide Web, websites और web pages की एक प्रणाली है जिसे browsers के माध्यम से internet पर access किया जाता है। HTTP (HyperText Transfer Protocol) और HTTPS (secure HTTP), web pages transfer करने के लिए उपयोग किए जाने वाले protocols हैं। IP address किसी network पर प्रत्येक device को दिया गया एक विशिष्ट numerical address है। DNS (Domain Name System) human-readable domain names (जैसे google.com) को IP addresses में translate करता है। Router devices और networks के बीच network traffic को निर्देशित करता है।

## नेटवर्किंग और protocols

TCP/IP internet की बुनियादी protocol suite है। IP (Internet Protocol) networks के बीच packets की addressing और routing संभालता है, जबकि TCP (Transmission Control Protocol) retransmission और flow control के साथ reliable, ordered delivery प्रदान करता है। UDP एक connectionless alternative है, जिसका उपयोग तब किया जाता है जब guaranteed delivery की तुलना में low latency अधिक महत्वपूर्ण हो (उदाहरण के लिए streaming, gaming, या DNS queries में)। HTTP एक stateless application-layer protocol है जो clients और servers के बीच request/response communication के लिए उपयोग होता है। HTTPS, TLS के ऊपर चलने वाला HTTP है, जो encryption और integrity protection जोड़ता है। REST (Representational State Transfer) एक API architectural style है जो resources, standard HTTP verbs (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`), और stateless interactions का उपयोग करती है। WebSockets persistent, full-duplex connections प्रदान करते हैं ताकि client और server real time में messages push कर सकें; यह chat, live dashboards, और collaborative apps के लिए उपयोगी है।

## कृत्रिम बुद्धिमत्ता

Artificial intelligence (AI) मशीनों, विशेषकर computer systems, द्वारा मानव बुद्धिमत्ता का अनुकरण है। Machine learning, AI का एक subset है जिसमें systems data से सीखते हैं ताकि वे explicitly programmed किए बिना predictions या decisions ले सकें। Deep learning, machine learning का subset है जो अनेक layers वाले neural networks का उपयोग करता है। Neural networks computational models हैं जो loosely biological brains की संरचना से प्रेरित हैं। Large language models (LLMs) ऐसे AI models हैं जिन्हें प्राकृतिक भाषा को समझने और उत्पन्न करने के लिए विशाल मात्रा में text पर train किया जाता है।

## Algorithms और data structures

Algorithm किसी समस्या को हल करने की step-by-step procedure है। Data structures वे तरीके हैं जिनसे computer में data को इस प्रकार संगठित किया जाता है कि उसे कुशलतापूर्वक access और modify किया जा सके। Common data structures में arrays, linked lists, stacks, queues, trees, graphs, और hash tables शामिल हैं। Sorting algorithms items को किसी निर्धारित क्रम में व्यवस्थित करते हैं; common examples हैं bubble sort, merge sort, और quicksort। Binary search sorted list में किसी item को खोजने का एक कुशल algorithm है, जो search range को बार-बार आधा करता है।

## डेटाबेस

Database electronically stored structured data का एक संगठित संग्रह है। Relational database data को rows और columns वाली tables में store करता है। SQL (Structured Query Language) relational databases को manage और query करने की standard language है। NoSQL databases data को tabular relations के अलावा अन्य formats में store करते हैं, जैसे documents, key-value pairs, या graphs। Common database systems में PostgreSQL, MySQL, SQLite, MongoDB, और Redis शामिल हैं। Database में index extra storage की लागत पर data retrieval को तेज़ करता है।

## System design की मूल बातें

System design का केंद्र reliable, scalable, और maintainable software systems बनाना है। Load balancing traffic को अनेक servers में बाँटती है ताकि availability सुधरे और latency घटे। Horizontal scaling अधिक machines जोड़ती है; vertical scaling एक machine में अधिक resources जोड़ती है। Caching frequently accessed data को fast storage (उदाहरण के लिए Redis, Memcached, या CDN edge caches) में रखती है ताकि database load और response time कम हो। Scale पर databases के लिए replication, partitioning (sharding), backup strategies, और consistency tradeoffs का सावधानीपूर्वक प्रबंधन आवश्यक होता है। Microservices बड़े applications को छोटे independently deployable services में बाँटते हैं, जबकि monoliths अधिकांश logic को एक deployable unit में रखते हैं; दोनों approaches में complexity, deployment speed, debugging, और team autonomy के संबंध में tradeoffs होते हैं।

## Operating systems

Operating system (OS) वह software है जो computer hardware को manage करता है और programs को services प्रदान करता है। Common operating systems में Windows, macOS, और Linux शामिल हैं। Linux एक open-source OS kernel है जिसका उपयोग servers, embedded systems और Android में होता है। OS processes (running programs), memory, file systems, और input/output devices को manage करता है। Process किसी program का running instance है। Thread, process के भीतर execution की सबसे छोटी unit है।

## Version control

Version control systems समय के साथ code में हुए changes को track करते हैं, जिससे developers सहयोग कर सकते हैं और previous states पर लौट सकते हैं। Git सबसे व्यापक रूप से उपयोग किया जाने वाला version control system है। Repository (repo) files और उनके history का संग्रह है। Commit, changes का saved snapshot है। Branch, development की स्वतंत्र line है। Pull request एक branch से दूसरी branch में changes merge करने का प्रस्ताव है।

## Software development practices

Object-oriented programming (OOP) code को ऐसे objects में संगठित करती है जो data और behavior को जोड़ते हैं। OOP के प्रमुख सिद्धांतों में encapsulation, inheritance, polymorphism, और abstraction शामिल हैं। Test-driven development (TDD) वह practice है जिसमें code लिखने से पहले tests लिखे जाते हैं। Agile, software development methodologies का एक समूह है जो iterative development, collaboration, और adaptability पर ज़ोर देता है। DevOps, software development और IT operations को जोड़ता है ताकि development lifecycle छोटा हो। APIs (Application Programming Interfaces) अलग-अलग software systems को एक-दूसरे से संचार करने की अनुमति देती हैं।

## Cloud और DevOps की मूल बातें

Cloud computing internet के माध्यम से on-demand infrastructure और managed services प्रदान करती है। तीन प्रमुख public cloud providers हैं AWS (Amazon Web Services), Microsoft Azure, और Google Cloud Platform (GCP)। Common service models हैं IaaS (infrastructure), PaaS (platform), और SaaS (software)। Core cloud building blocks में compute instances/containers, object storage, managed databases, networking, और IAM (Identity and Access Management) शामिल हैं। CI/CD (Continuous Integration and Continuous Delivery/Deployment) build, test, और release pipelines को automate करता है ताकि code commit से production तक सुरक्षित रूप से पहुँच सके। Docker applications और dependencies को portable containers में package करता है; production में इन containers को आम तौर पर orchestrators (जैसे Kubernetes), serverless platforms, या managed container services के माध्यम से deploy किया जाता है।

## Data formats और tooling

JSON (JavaScript Object Notation) एक lightweight text format है जो objects (key/value pairs), arrays, strings, numbers, booleans, और null से बना होता है; इसका APIs में व्यापक उपयोग होता है। YAML एक human-friendly configuration format है जो nested structures और comments को support करता है, और CI/CD तथा infrastructure definitions में आम है। CSV (Comma-Separated Values) delimited text की rows के रूप में tabular data store करता है और data import/export pipelines में सामान्य है। XML (eXtensible Markup Language) एक tag-based structured format है जिसका उपयोग legacy systems, configuration, और document workflows में होता है। Developers आम तौर पर इन formats को linters, schema validators (जैसे JSON Schema), query tools (`jq`, XPath), और अपनी programming language की parsing libraries से validate और transform करते हैं।

## Regular expressions (Regex)

Regular expression एक pattern language है जिसका उपयोग text को search, match, extract, और transform करने में किया जाता है। Core regex concepts में literals (`cat`), character classes (`[a-z]`, `\d`), quantifiers (`*`, `+`, `?`, `{n,m}`), anchors (`^`, `$`), groups (`(...)`), alternation (`a|b`), और special characters को escape करना शामिल है। Regex का उपयोग input validation, log parsing, text extraction, और find/replace automation में बहुत होता है। अलग-अलग engines (PCRE, JavaScript, Python `re`, RE2) की features अलग होती हैं, इसलिए tools के बीच behavior भिन्न हो सकता है। Regex शक्तिशाली है, लेकिन पढ़ने में कठिन हो सकती है; bugs से बचने के लिए complex patterns का परीक्षण और documentation होना चाहिए।

## Cybersecurity

Cybersecurity computer systems, networks, और data को digital attacks से सुरक्षित रखने की practice है। Common threats में malware (malicious software), phishing (जानकारी चुराने के लिए बनाया गया fraudulent communication), ransomware (data को encrypt करके payment माँगने वाला malware), और denial-of-service attacks शामिल हैं। Encryption data को unreadable form में बदल देता है जिसे केवल key से decode किया जा सकता है। HTTPS, web traffic को encrypt करने के लिए TLS (Transport Layer Security) का उपयोग करता है। Strong, unique passwords और two-factor authentication बुनियादी security practices हैं।

## Developers के लिए security concepts

OAuth 2.0 एक authorization framework है जो users को credentials सीधे साझा किए बिना किसी application को limited access देने देता है। OpenID Connect (OIDC), authentication के लिए OAuth 2.0 पर बना एक identity layer है। JWT (JSON Web Token) claims वाला एक compact token format है, जिसका उपयोग अक्सर stateless auth के लिए होता है, लेकिन इसे सही तरह से sign और कड़ाई से validate करना आवश्यक है (signature, expiration, issuer, audience)। TLS certificates के माध्यम से encryption, integrity, और server authentication प्रदान करके data in transit को secure करता है। OWASP Top 10 common web application security risks की व्यापक रूप से उपयोग की जाने वाली सूची है, जिसमें broken access control, cryptographic failures, injection, insecure design, security misconfiguration, vulnerable components, और insufficient logging/monitoring शामिल हैं। Secure development के लिए defense-in-depth आवश्यक है: input validation, output encoding, least privilege, secret management, dependency patching, और regular security testing।

