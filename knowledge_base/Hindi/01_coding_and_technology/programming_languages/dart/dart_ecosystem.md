<!--
---
# Metadata
title: "Dart — Ecosystem & Tooling Guide"
description: "Comprehensive guide to the Dart ecosystem including tools, frameworks, testing, and deployment."
category: "Coding and Technology"
version: "1.0.0"
status: "active"
authors:
  - name: "Nepoznato-Dev"
changelog:
  - version: "1.0.0"
    date: "2026-08-09"
    changes: "Initial ecosystem guide"
tags: [dart, ecosystem, tooling, flutter, testing, coding-and-technology]
difficulty_level: "beginner"
estimated_reading_time: "14 min"
contribution:
  license: "MIT"
  feedback_channel: "GitHub Issues"
---

-->
# डार्ट - पारिस्थितिकी तंत्र और टूलींग गाइड
यह मार्गदर्शिका डार्ट पारिस्थितिकी तंत्र में आवश्यक उपकरण, ढांचे और बुनियादी ढांचे को शामिल करती है।
---

## टूलचेन
| उपकरण | उद्देश्य |
|------|---------|
| **डार्ट** | डार्ट एसडीके (संकलक, फ़ॉर्मेटर, विश्लेषक) |
| **फड़फड़ाहट** | स्पंदन एसडीके (डार्ट शामिल) |
| **पब** | पैकेज मैनेजर (डार्ट में निर्मित) |
| **डार्ट विश्लेषण** | स्थैतिक विश्लेषण |
| **डार्ट प्रारूप** | कोड फ़ॉर्मेटिंग |
| **डार्ट संकलन** | मूल/JS/WASM में संकलित करें |
| **डार्ट रन** | डार्ट स्क्रिप्ट चलाएँ |
```bash
dart --version              # check version
dart create myapp           # create project
dart run                    # run project
dart pub get                # install dependencies
dart analyze                # static analysis
dart format .               # format code
dart compile exe bin/app.dart -o app  # compile to native
```

---

## पैकेज प्रबंधन
| उपकरण | उद्देश्य |
|------|---------|
| **पब.देव** | आधिकारिक पैकेज भंडार |
| **डार्ट पब** | पैकेज मैनेजर सीएलआई |
| **pubspec.yaml** | पैकेज मेनिफेस्ट |
```yaml
# pubspec.yaml
name: myapp
description: A sample Dart application
version: 0.1.0
environment:
  sdk: ^3.4.0

dependencies:
  http: ^1.2.0
  json_annotation: ^4.9.0
  riverpod: ^2.5.0

dev_dependencies:
  test: ^1.25.0
  build_runner: ^2.4.0
  json_serializable: ^6.7.0
  lints: ^4.0.0
```

```bash
dart pub get                # install dependencies
dart pub upgrade            # upgrade packages
dart pub add http           # add dependency
dart pub outdated           # check outdated packages
```

---

## स्पंदन (डार्ट यूआई फ्रेमवर्क)
| प्रौद्योगिकी | उद्देश्य |
|---|---|
| **फड़फड़ाना** | क्रॉस-प्लेटफॉर्म यूआई फ्रेमवर्क |
| **स्पंदन वेब** | फ़्लटर के साथ वेब ऐप्स |
| **फ़्लटर डेस्कटॉप** | विंडोज़, मैकओएस, लिनक्स |
| **फ़्लटर मोबाइल** | आईओएस और एंड्रॉइड |
| **स्पंदन एंबेडेड** | एंबेडेड डिवाइस |
```dart
// Flutter widget example
class UserCard extends StatelessWidget {
  final User user;
  const UserCard({super.key, required this.user});

  @override
  Widget build(BuildContext context) {
    return Card(
      child: ListTile(
        title: Text(user.name),
        subtitle: Text(user.email),
        trailing: Icon(Icons.arrow_forward),
        onTap: () => Navigator.push(
          context,
          MaterialPageRoute(builder: (_) => UserDetail(user: user)),
        ),
      ),
    );
  }
}
```

---

## वेब फ्रेमवर्क (सर्वर-साइड डार्ट)
| ढाँचा | प्रकार | के लिए सर्वश्रेष्ठ |
|--------|------|-------|
| **शेल्फ** | मिडलवेयर-आधारित | HTTP सर्वर (सबसे लोकप्रिय) |
| **डार्ट मेंढक** | फुल-स्टैक | बैकएंड फ्रेमवर्क (लारवेल की तरह) |
| **देवदूत** | बाकी एपीआई | सरल एपीआई |
| **अल्फ्रेड** | एक्सप्रेस जैसा | Node.js-शैली सर्वर |
```dart
// Shelf example
import 'package:shelf/shelf.dart';
import 'package:shelf_router/shelf_router.dart';
import 'package:shelf/shelf_io.dart' as io;

void main() async {
  final router = Router();
  
  router.get('/hello', (Request req) => Response.ok('Hello, World!'));
  
  router.get('/users/<id>', (Request req) async {
    final id = req.params['id']!;
    final user = await UserService.findById(int.parse(id));
    return Response.ok(jsonEncode(user));
  });

  var server = await io.serve(router, 'localhost', 8080);
  print('Serving at http://${server.address.host}:${server.port}');
}
```

---

## डेटाबेस
| प्रौद्योगिकी | प्रकार |
|------|------|
| **बहाव** | टाइप-सुरक्षित एसक्यूएल (मूर की जगह) |
| **ऑब्जेक्टबॉक्स** | NoSQL मोबाइल डेटाबेस |
| **ईसर** | तेज़ मोबाइल डेटाबेस |
| **हाइव** | हल्के कुंजी-मूल्य |
| **पोस्टग्रेज** | PostgreSQL क्लाइंट |
| **mysql1** | MySQL क्लाइंट |
| **काउचबेस** | काउचबेस क्लाइंट |
| **सुपाबेस** | सेवा के रूप में बैकएंड |
| **फ़ायरबेस** | Google BaaS |
```dart
// Drift (type-safe SQL)
class UsersDao extends DatabaseAccessor<AppDatabase> with _$UsersDaoMixin {
  UsersDao(AppDatabase db) : super(db);

  Future<List<User>> findAll() => select(users).get();
  
  Future<User> findById(int id) =>
    (select(users)..where((t) => t.id.equals(id)))
      .getSingle();
  
  Stream<List<User>> watchAll() => select(users).watch();
}
```

---

## परीक्षण
| ढाँचा | उद्देश्य |
|----|----|
| **परीक्षण** | अंतर्निहित परीक्षण ढांचा |
| **मॉकिटो** | उपहास |
| **मॉकटेल** | अशक्त-सुरक्षित मॉकिंग |
| **स्पंदन_परीक्षण** | स्पंदन विजेट परीक्षण |
| **एकीकरण_परीक्षण** | एंड-टू-एंड परीक्षण |
| **गोल्डन_टूलकिट** | गोल्डन/स्नैपशॉट परीक्षण |
| **गश्त** | स्पंदन एकीकरण परीक्षण |
```dart
import 'package:test/test.dart';

void main() {
  group('UserService', () {
    late UserService service;
    late MockUserRepository mockRepo;

    setUp(() {
      mockRepo = MockUserRepository();
      service = UserService(mockRepo);
    });

    test('finds user by id', () async {
      when(mockRepo.findById(1)).thenAnswer((_) async => User(1, 'Alice'));

      final user = await service.findById(1);

      expect(user.name, equals('Alice'));
      verify(mockRepo.findById(1)).called(1);
    });

    test('throws when user not found', () async {
      when(mockRepo.findById(any)).thenThrow(NotFoundException());

      expect(() => service.findById(999), throwsA(isA<NotFoundException>()));
    });
  });
}
```

---

## कोड गुणवत्ता
| उपकरण | उद्देश्य |
|------|---------|
| **डार्ट विश्लेषण** | अंतर्निहित स्थैतिक विश्लेषण |
| **डार्ट प्रारूप** | बिल्ट-इन फ़ॉर्मेटर |
| **लिंट्स** | आधिकारिक लिंट नियम |
| **स्पंदन_लिंट्स** | स्पंदन-विशिष्ट लिंट |
| **बहुत_अच्छा_विश्लेषण** | सख्त लिंट नियम |
| **कवरेज** | कोड कवरेज |
```yaml
# analysis_options.yaml
include: package:lints/recommended.yaml

linter:
  rules:
    - prefer_final_locals
    - prefer_const_constructors
    - avoid_dynamic_calls
    - always_declare_return_types

analyzer:
  errors:
    missing_return: error
    dead_code: warning
```

---

## प्रमुख पुस्तकालय
| पुस्तकालय | उद्देश्य |
|---------|---------|
| **डार्ट:कोर** | मानक पुस्तकालय |
| **डार्ट:एसिंक** | फ़्यूचर्स, स्ट्रीम्स, एसिंक्स |
| **डार्ट:आईओ** | फ़ाइल, HTTP, टीसीपी |
| **डार्ट:कन्वर्ट** | जेएसओएन, यूटीएफ-8 |
| **http** | HTTP क्लाइंट |
| **डियो** | HTTP क्लाइंट (स्पंदन) |
| **json_serializable** | JSON कोड जनरेशन |
| **जमा हुआ** | अपरिवर्तनीय डेटा वर्ग |
| **रिवरपोड** | राज्य प्रबंधन |
| **ब्लॉक / क्यूबिट** | राज्य प्रबंधन |
| **इसे_प्राप्त करें** | निर्भरता इंजेक्शन |
| **गो_राउटर** | घोषणात्मक रूटिंग |
| **समतामूलक** | मूल्य समानता |
| **उउइद** | यूयूआईडी पीढ़ी |
| **क्रिप्टो** | क्रिप्टोग्राफी |
| **पथ** | फ़ाइल पथ हेरफेर |
| **संग्रह** | अतिरिक्त संग्रह प्रकार |
| **अंतर्राष्ट्रीय** | अंतर्राष्ट्रीयकरण |
---

## राज्य प्रबंधन (स्पंदन)
| समाधान | प्रकार |
|-------|------|
| **रिवरपोड** | संकलन-सुरक्षित, परीक्षण योग्य |
| **ब्लॉक / क्यूबिट** | घटना-संचालित, पूर्वानुमेय |
| **प्रदाता** | अंतर्निर्मित, सरल |
| **गेटएक्स** | ऑल-इन-वन (विवादास्पद) |
| **सिग्नल** | प्रतिक्रियाशील आदिम |
---

## आईडीई और संपादक
| आईडीई | ताकतें |
|----|-----|
| **वीएस कोड + डार्ट** | सर्वोत्तम डार्ट/स्पंदन समर्थन |
| **एंड्रॉइड स्टूडियो + फ़्लटर** | पूर्ण स्पंदन आईडीई |
| **इंटेलिजे + डार्ट** | JetBrains समर्थन |
---

## तैनाती
| विधि | नोट्स |
|-------|-------|
| **डार्ट संकलन** | मूल निष्पादनयोग्य |
| **डार्ट कंपाइल जेएस** | जावास्क्रिप्ट में संकलित करें |
| **डार्ट संकलन था** | WebAssembly में संकलित करें |
| **स्पंदन निर्माण** | मोबाइल/डेस्कटॉप ऐप्स |
| **डॉकर** | कंटेनरीकृत सर्वर ऐप्स |
| **गूगल क्लाउड रन** | सर्वर रहित कंटेनर |
| **फ़ायरबेस होस्टिंग** | वेब ऐप होस्टिंग |
---

## सारांश
क्रॉस-प्लेटफ़ॉर्म यूआई विकास के लिए डार्ट के पारिस्थितिकी तंत्र में **फ़्लटर** का प्रभुत्व है। सर्वर-साइड डार्ट के लिए, **शेल्फ** मानक HTTP फ्रेमवर्क है, जिसमें **डार्ट फ्रॉग** एक पूर्ण-स्टैक विकल्प के रूप में है। मानक स्टैक है: रनटाइम के रूप में **डार्ट 3.4+**, पैकेज के लिए **pub.dev**, मोबाइल/वेब/डेस्कटॉप यूआई के लिए **फ़्लटर**, राज्य प्रबंधन के लिए **रिवरपॉड** या **ब्लॉक**, डेटाबेस के लिए **ड्रिफ्ट**, परीक्षण के लिए **टेस्ट** और लिंटिंग के लिए **डार्ट विश्लेषण**। डार्ट की ताकत ध्वनि शून्य सुरक्षा, तेज़ संकलन, हॉट रीलोड (फ़्लटर), और देशी, जावास्क्रिप्ट, या वेबअसेंबली में संकलित करने की क्षमता है। यह पारिस्थितिकी तंत्र क्रॉस-प्लेटफ़ॉर्म मोबाइल, वेब और डेस्कटॉप अनुप्रयोगों के लिए आदर्श है।