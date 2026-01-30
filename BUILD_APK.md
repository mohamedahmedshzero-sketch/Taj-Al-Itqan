# 📱 دليل بناء APK
# Building APK Guide

## المتطلبات

### 1. Windows/Mac/Linux
- Python 3.8+
- Java JDK 11+
- Android SDK
- Buildozer

### 2. التثبيت على Windows

```bash
# 1. تثبيت Buildozer
pip install buildozer cython

# 2. تثبيت Java JDK 11
# اذهب إلى: https://adoptopenjdk.net/
# ثم اضبط JAVA_HOME في متغيرات البيئة

# 3. تثبيت Android SDK
# اذهب إلى: https://developer.android.com/studio
# ثم اضبط ANDROID_SDK_ROOT في متغيرات البيئة
```

### 3. على Linux/Mac

```bash
# تثبيت المتطلبات
sudo apt-get install openjdk-11-jdk-headless
pip install buildozer cython

# تحميل Android SDK
mkdir -p ~/android-sdk
cd ~/android-sdk
wget https://dl.google.com/android/repository/commandlinetools-linux-xxxxx_latest.zip
```

## البناء المحلي

### 1. تحضير المشروع

```bash
cd d:\Taj Al-Itqan

# تثبيت المكتبات
pip install -r requirements.txt

# اختبار التطبيق
python test_project.py

# تشغيل التطبيق
python -m main
```

### 2. بناء APK

```bash
# البناء الأول (قد يستغرق وقتاً)
buildozer android debug

# البناء السريع (بعد المرة الأولى)
buildozer android debug -- --skip-update

# البناء للإصدار (Release)
buildozer android release
```

### 3. النتيجة

سيتم إنشاء ملف APK في:
```
bin/tajalitqan-1.0.0-debug.apk
bin/tajalitqan-1.0.0-release.apk
```

## البناء على GitHub

### 1. دفع الكود إلى GitHub

```bash
git add .
git commit -m "تحديث: إضافة دعم APK والبناء التلقائي"
git push origin main
```

### 2. مراقبة البناء

- اذهب إلى: `https://github.com/yourusername/taj-al-itqan/actions`
- شاهد عملية البناء في الوقت الفعلي
- حمّل APK من `Artifacts`

## استكشاف الأخطاء

### ❌ خطأ: "Java not found"
```bash
# تحقق من JAVA_HOME
echo $JAVA_HOME  # Linux/Mac
echo %JAVA_HOME%  # Windows

# اضبطه إذا لم يكن موجود
export JAVA_HOME=/path/to/jdk  # Linux/Mac
set JAVA_HOME=C:\path\to\jdk  # Windows
```

### ❌ خطأ: "Android SDK not found"
```bash
# تحقق من ANDROID_SDK_ROOT
echo $ANDROID_SDK_ROOT  # Linux/Mac
echo %ANDROID_SDK_ROOT%  # Windows

# اضبطه
export ANDROID_SDK_ROOT=~/android-sdk  # Linux/Mac
set ANDROID_SDK_ROOT=C:\android-sdk  # Windows
```

### ❌ خطأ: "buildozer not found"
```bash
pip install buildozer --upgrade
```

### ❌ خطأ في الاستيراد
```bash
# تأكد من المكتبات
pip install -r requirements.txt --upgrade

# أعد المحاولة
buildozer android debug
```

## معلومات الإصدار

- **الإصدار:** 1.0.0
- **Python:** 3.8+
- **Kivy:** 2.2.0+
- **Android:** API 21+

## نصائح مهمة

✅ **استخدم Release build للتطبيق الفعلي**
```bash
buildozer android release
```

✅ **وقع الـ APK قبل النشر**
```bash
jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 \
  -keystore my-release-key.jks \
  bin/tajalitqan-1.0.0-release-unsigned.apk \
  alias_name
```

✅ **ضع buildozer.spec تحت التحكم بالإصدارات**
```bash
git add buildozer.spec
git commit -m "إضافة: إعدادات buildozer.spec"
```

## موارد إضافية

- 📖 [Buildozer Docs](https://buildozer.readthedocs.io/)
- 📖 [Kivy for Android](https://kivy.org/doc/stable/guide/android.html)
- 📖 [Python-for-Android](https://python-for-android.readthedocs.io/)

---

**تم إنشاؤه:** 28 يناير 2026  
**الحالة:** ✅ جاهز للبناء
