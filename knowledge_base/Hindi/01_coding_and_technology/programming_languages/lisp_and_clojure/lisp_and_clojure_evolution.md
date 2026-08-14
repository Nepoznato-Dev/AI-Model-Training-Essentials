<!--
---
# Metadata
title: "Lisp & Clojure — Version History & Evolution"
description: "Comprehensive version history and evolution of Lisp from 1958 to modern Clojure."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial version history"
tags: [lisp, clojure, version-history, evolution, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "10 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# लिस्प और क्लोजर - संस्करण इतिहास और विकास
## लिस्प टाइमलाइन
| संस्करण | वर्ष | मुख्य विषय |
|------|------|-------|
| लिस्प 1.5 | 1962 | **पहली बार लिस्प लागू किया गया** (जॉन मैक्कार्थी, एमआईटी) |
| मैकलिस्प | 1960 का दशक | एमआईटी मेनफ्रेम लिस्प |
| इंटरलिस्प | 1967 | ज़ेरॉक्स PARC — संरचित संपादन |
| योजना | 1975 | **मिनिमलिस्ट लिस्प** (ससमैन एंड स्टील, एमआईटी) |
| सामान्य लिस्प | 1984 | **मानकीकृत लिस्प** (गाइ स्टील, एएनएसआई 1994) |
| इमाक्स लिस्प | 1985 | Emacs संपादक के लिए लिस्प |
| योजना R5RS | 1998 | संशोधित⁵ रिपोर्ट - व्यापक रूप से अपनाई गई योजना मानक |
| योजना R6RS | 2007 | मॉड्यूल प्रणाली, यूनिकोड |
| योजना R7RS | 2013 | छोटी भाषा (R7RS-छोटी) |
| क्लोजर | 2007 | **जेवीएम पर आधुनिक लिस्प** (रिच हिक्की) |
| क्लोजर 1.0 | 2009 | पहली स्थिर रिलीज़ |
| क्लोजर 1.3 | 2011 | प्रोटोकॉल,`defrecord`|
| क्लोजर 1.4 | 2012 | पाठक सशर्त |
| क्लोजर 1.5 | 2013 | ट्रांसड्यूसर (बाद में) |
| क्लोजर 1.7 | 2015 | **ट्रांसड्यूसर**, रीडर कंडीशनल |
| क्लोजर 1.8 | 2016 | `spec`(डेटा सत्यापन),`clojure.spec`|
| क्लोजर 1.9 | 2017 | **`spec`स्थिर**, त्रुटि संदेशों में सुधार |
| क्लोजर 1.10 | 2018 | बेहतर त्रुटि संदेश,`clj`CLI |
| क्लोजर 1.11 | 2022 | `update-keys`,`update-vals`,`abs`|
| क्लोजर 1.12 | 2024 | **जावा इंटरऑप सुधार**,`definterface`|
## प्रमुख मील के पत्थर
### अर्ली लिस्प (1958-1970)
- **1958**: जॉन मैक्कार्थी ने एमआईटी में लिस्प बनाया - "सूची प्रसंस्करण"
- **1962**: लिस्प 1.5 — पहला कार्यान्वित संस्करण
- प्रमुख नवाचार: **कचरा संग्रहण**, **पुनरावर्तन**, **समरूपता** (कोड = डेटा)
-`eval`- सार्वभौमिक कार्य
-`cond`,`car`/`cdr`,`cons`, लैम्ब्डा
### योजना (1975-वर्तमान)
- **1975**: गाइ स्टील और गेराल्ड सुसमैन ने एमआईटी में योजना बनाई
- **दर्शन**: न्यूनतमवादी - छोटा कोर, शक्तिशाली अमूर्तता
- लेक्सिकल स्कोपिंग (अधिकांश भाषाओं से पहले)
- प्रथम श्रेणी की निरंतरता
- स्वच्छ मैक्रोज़
- टेल-कॉल अनुकूलन (अनिवार्य)
### कॉमन लिस्प (1984-वर्तमान)
- **1984**: गाइ स्टील ने "कॉमन लिस्प द लैंग्वेज" प्रकाशित किया
- **1994**: एएनएसआई कॉमन लिस्प मानक (एएनएसआई एक्स3.226)
- ** "किचन सिंक" लिस्प** - विशाल मानक पुस्तकालय
- सीएलओएस (कॉमन लिस्प ऑब्जेक्ट सिस्टम) - सबसे शक्तिशाली ओओपी
- स्थिति प्रणाली - पुनः आरंभ करने योग्य त्रुटियाँ
- लूप मैक्रो - शक्तिशाली पुनरावृत्ति डीएसएल
### क्लोजर (2007-वर्तमान)
- **2007**: रिच हिक्की ने जेवीएम के लिए क्लोजर-लिस्प बनाया
- **दर्शन**: व्यावहारिक, समवर्ती, अपरिवर्तनीय
- लगातार अपरिवर्तनीय डेटा संरचनाएँ
- एसटीएम (सॉफ्टवेयर ट्रांजेक्शनल मेमोरी)
-`core.async`(सीएसपी-शैली संगामिति)
- निर्बाध जावा इंटरऑप
- आरईपीएल-संचालित विकास
## सिंटेक्स इवोल्यूशन
```lisp
;; Lisp 1.5 (1962): The essentials
(defun factorial (n)
  (cond ((= n 0) 1)
        (t (* n (factorial (- n 1))))))

;; Scheme (1975): Minimalist, lexical scoping
(define (factorial n)
  (if (<= n 1)
      1
      (* n (factorial (- n 1)))))

;; Common Lisp (1984): CLOS, condition system
(defclass shape ()
  ((x :initarg :x :accessor shape-x)
   (y :initarg :y :accessor shape-y)))

(defclass circle (shape)
  ((radius :initarg :radius :accessor circle-radius)))

(defgeneric area (shape))

(defmethod area ((c circle))
  (* pi (expt (circle-radius c) 2)))

;; Clojure (2007): Modern, immutable, JVM
(defn factorial [n]
  (reduce * (range 1 (inc n))))

;; Clojure: Persistent data structures
(def m {:name "Alice" :age 30})
(def m2 (assoc m :email "alice@example.com"))  ; original unchanged

;; Clojure: Transducers (1.7)
(def xf (comp (filter even?) (map #(* % %))))
(transduce xf + 0 (range 10))

;; Clojure: spec (1.8+)
(require '[clojure.spec.alpha :as s])
(s/def ::name string?)
(s/def ::age (s/and int? #(<= 0 % 150)))
(s/def ::person (s/keys :req [::name ::age]))

;; Clojure: core.async (channels)
(require '[clojure.core.async :refer [go chan >! <!]])
(go (let [c (chan)]
      (>! c "hello")
      (println (<! c))))
```

## फ़ीचर इवोल्यूशन
```
Lisp 1.5 (1962):  car/cdr/cons, eval, cond, lambda
Scheme (1975):    Lexical scoping, continuations, hygienic macros, TCO
Common Lisp (1984): CLOS, conditions, loop, defstruct, defmacro
Clojure (2007):   Persistent data structures, STM, Java interop
Clojure 1.7 (2015): Transducers, reader conditionals
Clojure 1.8 (2016): spec (data validation)
Clojure 1.9 (2017): spec stable, improved errors
Clojure 1.11 (2022): update-keys, update-vals
Clojure 1.12 (2024): Java interop improvements
```

## मुख्य डिज़ाइन सिद्धांत
```
Lisp (general):
1. "Code is data" — homoiconicity (programs are lists)
2. "Macros" — extend the language itself
3. "REPL-driven" — interactive development
4. "Functional" — functions are first-class

Clojure-specific:
5. "Immutable by default" — persistent data structures
6. "Concurrency" — STM, atoms, agents, core.async
7. "Practical" — Java interop, real-world libraries
8. "Simple" — few concepts, compose freely
```

## पारिस्थितिकी तंत्र का विकास
```
1958: Lisp created by John McCarthy at MIT
1962: Lisp 1.5 — first implementation
1975: Scheme — minimalist Lisp
1984: Common Lisp — standardized, comprehensive
1994: ANSI Common Lisp standard
2007: Clojure — Lisp on the JVM
2009: Clojure 1.0 — stable release
2015: Clojure 1.7 — transducers
2016: Clojure 1.8 — spec
2024: Clojure 1.12 — Java interop
2025: Lisp family powers:
       - Emacs (Emacs Lisp)
       - Racket (modern Scheme)
       - Clojure (web, data, concurrent systems)
       - Arc, Hy, Janet (Lisp dialects)
       Used by: NASA (JPL), Amazon, Apple, Nubank, CircleCI
```
