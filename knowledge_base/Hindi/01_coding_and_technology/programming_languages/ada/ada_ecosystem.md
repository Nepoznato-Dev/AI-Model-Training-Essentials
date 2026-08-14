---
# Metadata
title: "Ada — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Ada ecosystem including compilers, build systems, libraries, and tools."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "AI Model Training Team"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [ada, ecosystem, tooling, compilers, safety-critical, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "12 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

#एडीए - पारिस्थितिकी तंत्र और टूलींग गाइड
यह मार्गदर्शिका Ada पारिस्थितिकी तंत्र में आवश्यक उपकरण, पुस्तकालय और बुनियादी ढांचे को शामिल करती है।
---

## कंपाइलर और कार्यान्वयन
| संकलक | प्रकार | नोट्स |
|-------|------|-------|
| **जीएनएटी** | ओपन-सोर्स | जीसीसी-आधारित, सबसे व्यापक रूप से उपयोग किया जाने वाला |
| **GNAT समुदाय** | मुफ़्त | AdaCore का निःशुल्क संस्करण |
| **जीएनएटी प्रो** | वाणिज्यिक | सुरक्षा-प्रमाणित, AdaCore |
| **ऑब्जेक्टएडा** | वाणिज्यिक | विंडोज़, सुरक्षा-महत्वपूर्ण |
| **जानूस/अदा** | वाणिज्यिक | एंबेडेड सिस्टम |
```bash
gprbuild -P myproject     # build project
gprclean -P myproject     # clean
gnatmake main.adb         # compile single file
gnatcheck -P myproject    # code analysis
alr version               # Alire version
```

---

## बिल्ड सिस्टम और पैकेज प्रबंधन
| उपकरण | उद्देश्य |
|------|---------|
| **अलीरे** | आधुनिक पैकेज मैनेजर (अनुशंसित) |
| **जीपीआरबिल्ड** | प्रोजेक्ट निर्माण उपकरण |
| **जीपीआर (जीएनएटी प्रोजेक्ट)** | प्रोजेक्ट फ़ाइल स्वरूप |
| **बनाओ** | क्लासिक बिल्ड |
```toml
# alire.toml
name = "myapp"
description = "My Ada application"
version = "0.1.0"

[[depends-on]]
gnat = "^13"
gnatcoll = "^24"

[[pins]]
```

```bash
alr init --bin myapp      # create project
alr build                 # build
alr run                   # run
alr get --build gnatcoll  # get dependency
alr search                # search packages
alr index                 # update index
```

```gpr
-- myproject.gpr
project Myproject is
   for Source_Dirs use ("src/**");
   for Object_Dir use "obj";
   for Main use ("main.adb");
   
   package Compiler is
      for Default_Switches ("Ada") use ("-gnatwa", "-gnatVa", "-O2");
   end Compiler;
   
   package Binder is
      for Default_Switches ("Ada") use ("-E");  -- store exceptions
   end Binder;
end Myproject;
```

---

## सुरक्षा एवं सत्यापन
| उपकरण | उद्देश्य |
|------|---------|
| **जीएनएटीसाबित** | औपचारिक सत्यापन |
| **स्पार्क** | सुरक्षा-महत्वपूर्ण उपसमुच्चय |
| **कोडपीयर** | स्थैतिक विश्लेषण |
| **पॉलीस्पेस** | रनटाइम सत्यापन |
| **कवरिटी** | स्थैतिक विश्लेषण |
```ada
-- SPARK example
package Stack with
   SPARK_Mode
is
   type Bounded_Stack (Capacity : Positive) is tagged private;
   
   procedure Push (S : in out Bounded_Stack; Element : Integer)
      with Pre  => not S.Is_Full,
           Post => not S.Is_Empty and S.Top = Element;
   
   function Is_Full (S : Bounded_Stack) return Boolean;
   function Is_Empty (S : Bounded_Stack) return Boolean;
   
private
   type Bounded_Stack (Capacity : Positive) is tagged record
      Data : array (1 .. Capacity) of Integer;
      Top_Index : Natural := 0;
   end record;
end Stack;
```

---

## परीक्षण
| ढाँचा | उद्देश्य |
|----|----|
| **एयूनिट** | इकाई परीक्षण रूपरेखा |
| **अहवेन** | सरल परीक्षण |
| **GNATtest** | कोड आधारित परीक्षण |
| **जीपीआरबिल्ड** | निर्माण एवं परीक्षण |
```ada
with AUnit.Simple_Test_Cases;
with AUnit.Test_Suites;
with AUnit.Run;
with AUnit.Reporter.Text;

package Stack_Test is
   type Test_Case is new AUnit.Simple_Test_Cases.Test_Case with null record;
   
   function Name (T : Test_Case) return AUnit.Message_String;
   procedure Run_Test (T : in out Test_Case);
end Stack_Test;

package body Stack_Test is
   function Name (T : Test_Case) return AUnit.Message_String is
   begin
      return new String'("Stack Tests");
   end Name;
   
   procedure Run_Test (T : in out Test_Case) is
      S : Bounded_Stack (10);
   begin
      Push (S, 42);
      AUnit.Assertions.Assert (Top (S) = 42, "Top should be 42");
      AUnit.Assertions.Assert (not Is_Empty (S), "Should not be empty");
   end Run_Test;
end Stack_Test;
```

---

## प्रमुख पुस्तकालय
| पुस्तकालय | उद्देश्य |
|---------|---------|
| **एडीए.कंटेनर्स** | वेक्टर, मानचित्र, सेट |
| **एडीए.स्ट्रिंग्स** | स्ट्रिंग हैंडलिंग |
| **Ada.Text_IO** | कंसोल I/O |
| **Ada.कैलेंडर** | दिनांक/समय |
| **GNATcoll** | जीएनएटी उपयोगिताएँ |
| **एडब्ल्यूएस** | एडा वेब सर्वर |
| **एक्सएमएल/एडीए** | एक्सएमएल पार्सिंग |
| **जीआईडी** | छवि डिकोडिंग |
| **SDLAda** | SDL2 बाइंडिंग |
| **जीएलएफडब्ल्यू** | ओपनजीएल विंडोइंग |
| **कॉर्टेक्स जीएनएटी रनटाइम** | एंबेडेड (एआरएम) |
---

## समवर्ती
| फ़ीचर | उद्देश्य |
|---------|---------|
| **कार्य** | समवर्ती सूत्र |
| **संरक्षित वस्तुएँ** | सिंक्रोनाइज़्ड डेटा |
| **बयान चुनें** | मुलाकात |
| **प्रवेश कॉल** | तुल्यकालन |
```ada
task type Worker is
   entry Do_Work (Item : in Integer);
end Worker;

task body Worker is
   Value : Integer;
begin
   loop
      select
         accept Do_Work (Item : in Integer) do
            Value := Item;
         end Do_Work;
         Process (Value);
      or
         terminate;
      end select;
   end loop;
end Worker;
```

---

## आईडीई और संपादक
| आईडीई | ताकतें |
|----|-----|
| **जीपीएस (जीएनएटी प्रोग्रामिंग स्टूडियो)** | एडाकोर की आईडीई |
| **वीएस कोड + एडीए** | एडा भाषा समर्थन |
| **Emacs + ada-मोड** | क्लासिक एडा वातावरण |
---

## तैनाती
| विधि | नोट्स |
|-------|-------|
| **स्टेटिक बाइनरी** | GNAT स्थिर बायनेरिज़ उत्पन्न करता है |
| **क्रॉस-कंपाइल** | GNAT क्रॉस-संकलन |
| **एम्बेडेड** | बेयर-मेटल, आरटीओएस (रेवेन्सकर) |
| **डॉकर** | कंटेनरीकृत |
| **सुरक्षा प्रमाणीकरण** | डीओ-178सी, आईईसी 61508, सामान्य मानदंड |
---

## सारांश
Ada का पारिस्थितिकी तंत्र सुरक्षा-महत्वपूर्ण और उच्च-विश्वसनीयता प्रणालियों के उद्देश्य से बनाया गया है। मानक टूलचेन है: संकलन के लिए **GNAT** (GCC-आधारित), पैकेज प्रबंधन के लिए **Alire**, बिल्ड के लिए **GPRbuild**, औपचारिक सत्यापन के लिए **GNATprove** और **SPARK**, और परीक्षण के लिए **AUnit**। Ada एयरोस्पेस (DO-178C), रक्षा, रेलवे, चिकित्सा उपकरणों और किसी भी क्षेत्र में उत्कृष्टता प्राप्त करता है जहां शुद्धता सर्वोपरि है। एडा की ताकतें मजबूत टाइपिंग, समवर्ती (कार्य, संरक्षित वस्तुएं), औपचारिक सत्यापन (स्पार्क), और सुरक्षा प्रमाणन हैं। सुरक्षा-महत्वपूर्ण एम्बेडेड सिस्टम के लिए पारिस्थितिकी तंत्र आवश्यक है।