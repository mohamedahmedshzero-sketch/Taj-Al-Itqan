# تاج الإتقان

تطبيق إدارة حلقات تعليمية مبني بـ Kivy/KivyMD. هذا المستودع يحوي واجهة عربية، قاعدة SQLite محلية، وتوليد/مشاركة رموز QR للطلاب.

## إعداد وبناء (ملخص)

التعليمات التالية تبين طريقتين لبناء التطبيق على أندرويد:

1) الطريقة الموصى بها (Docker / CI)
- هذا المشروع يتضمن إعداد GitHub Actions لبناء APK باستخدام صورة `kivy/buildozer` (موجودة على Docker Hub).
- لهذه الطريقة لا تحتاج تثبيت Android SDK محليًا.

2) محلي على نظام لينكس / WSL2
- نزّل Python 3.11
- أنشئ بيئة افتراضية:

```powershell
cd "d:\Taj Al-Itqan"
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```

- لتشغيل التطبيق محليًا (سطح المكتب):

```powershell
cd "d:\Taj Al-Itqan"
.\.venv\Scripts\Activate.ps1
python __main__.py
```

- لبناء APK محليًا يفضل استخدام WSL2 أو صورة Docker الرسمية لـ `kivy/buildozer`.

## بناء APK باستخدام Docker (محلي)

استخدم السكربت `scripts/build_apk_docker.sh` (Linux / WSL) أو شغله يدوياً:

```bash
# مثال تشغيل محلي عبر Docker
./scripts/build_apk_docker.sh
```

المخرجات ستُوضع في `bin/` داخل المستودع.

## CI: GitHub Actions

المستودع يحتوي ملف `.github/workflows/build-apk.yml` الذي يبني APK باستخدام حاوية Docker `kivy/buildozer` عند تشغيل Workflow.

## ملاحظات مهمة
- بناء APK يتطلب مساحة ووقت (قد يتجاوز 20-40 دقيقة في CI).
- راجع `buildozer.spec` للأذونات وإصدارات `android.api`/`android.minapi` قبل رفع التطبيق إلى المتجر.
- أفصِح عن أي بيانات حساسة ولا تضعها صراحة في روابط مشاركة.

---

إذا تريد، أستطيع الآن:
- تشغيل عملية البناء على CI (أعدّ الملف فقط) أو
- تشغيل Docker محليًا لبناء APK هنا (إذا سمحت لي باستخدام Docker على جهازك) أو
- تعديل `buildozer.spec` لخيارات الـ release وkeystore وsignature.
