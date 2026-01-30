# تاج الإتقان — بناء APK

## الملخص السريع

هذا المشروع يحتوي على:
- ✅ تطبيق Kivy/KivyMD للإدارة الإسلامية (حفظ القرآن، إدارة الطلاب)
- ✅ Workflow GitHub Actions لبناء APK تلقائياً
- ✅ إعدادات Buildozer محسّنة للأندرويد
- ✅ دعم كامل للعربية ورموز QR

## خطوات البناء والتوزيع

### Option 1: البناء عبر GitHub Actions (موصى به — سهل وسريع)

1. **رفع المشروع إلى GitHub:**
   - إن لم تكن قد فعلت بعد:
     ```bash
     git remote add origin https://github.com/mohamedahmedshzero-sketch/Taj-Al-Itqan.git
     git add .
     git commit -m "initial commit: app setup and CI workflow"
     git push -u origin main
     ```

2. **تفعيل الـ Workflow:**
   - اذهب إلى **GitHub** → **Actions**
   - اختر **Build APK (Buildozer)**
   - اضغط **Run workflow** (أو سيعمل تلقائياً على أي push)

3. **انتظر الانتهاء** (يستغرق 30-60 دقيقة)

4. **حمّل APK:**
   - اذهب إلى **workflow run** → **Artifacts** → **taj-al-itqan-apk**
   - حمّل `bin/tajalitqan-1.0.0-debug.apk`

5. **(اختياري) توقيع الـ APK:**
   - لبناء **release APK موقّع**، أضف هذه الأسرار:
     - **Settings** → **Secrets and variables** → **Actions**
     - `ANDROID_KEYSTORE` (base64 من JKS file)
     - `ANDROID_KEY_ALIAS`
     - `ANDROID_KEY_PASSWORD`

### Option 2: البناء محلياً (WSL/Linux)

#### على Windows — استخدام WSL (Windows Subsystem for Linux)

1. **ثبت WSL وUbuntu:**
   ```powershell
   # من PowerShell مع صلاحيات Admin
   wsl --install Ubuntu
   ```

2. **من داخل WSL (Ubuntu):**
   ```bash
   # تحديث النظام
   sudo apt update && sudo apt upgrade -y
   
   # تثبيت الاعتمادات
   sudo apt install -y python3-pip python3-venv openjdk-17-jdk zip unzip \
     build-essential zlib1g-dev libssl-dev libffi-dev liblzma-dev \
     libjpeg-dev libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
   
   # إعداد البيئة
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip setuptools wheel cython buildozer
   
   # البناء
   buildozer -v android debug
   ```

3. **البحث عن APK:**
   - سيكون في `bin/tajalitqan-1.0.0-debug.apk`

#### على Linux/macOS:

```bash
# نفس الخطوات أعلاه بدون WSL
pip3 install buildozer cython
buildozer -v android debug
```

## المشاكل الشائعة والحلول

| المشكلة | الحل |
|--------|------|
| `ERROR: Could not find a version...` | الـ NDK/SDK غير متاح — اترك buildozer يحملها تلقائياً |
| `ImportError: FancyURLopener` | استخدم Python 3.10 أو 3.11 (Python 3.14 قديم) |
| خطوط عربية لا تظهر | الخطوط الموجودة في `assets/` تُحمل تلقائياً |
| ذاكرة قليلة | تأكد من 10+ GB مساحة حرة؛ WSL قد يحتاج 20 GB |
| Java غير موجود | تثبيت OpenJDK: `sudo apt install openjdk-17-jdk` |

## الملفات المهمة

- **`buildozer.spec`** — إعدادات البناء الأساسية
- **`.github/workflows/build_apk.yml`** — CI/CD workflow
- **`src/main.py`** — الشاشة الرئيسية
- **`src/database.py`** — إدارة البيانات والطلاب
- **`src/qr_handler.py`** — توليد رموز QR والمشاركة
- **`requirements.txt`** — المكتبات المطلوبة
- **`icon.png` و `splash.png`** — أيقونة وشاشة التحميل

## الأذونات المطلوبة

في `buildozer.spec`:
```
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
```

على Android 11+:
- التطبيق يحفظ البيانات في `app.user_data_dir` (آمن تلقائياً)
- لا يحتاج أذونات ذاكرة خارجية واسعة

## نصائح الأداء والنشر

1. **بناء Debug:** سريع، يصلح للتطوير
   ```bash
   buildozer android debug
   ```

2. **بناء Release (موقّع):**
   ```bash
   buildozer android release
   ```

3. **تثبيت على الجهاز:**
   ```bash
   adb install -r bin/tajalitqan-1.0.0-debug.apk
   ```

4. **نشر على Google Play:**
   - وقّع APK
   - أرفعه إلى [Google Play Console](https://play.google.com/console)

## الدعم والمساعدة

- **Buildozer Docs:** https://buildozer.readthedocs.io
- **Kivy Docs:** https://kivy.org/doc
- **KivyMD Docs:** https://kivymd.readthedocs.io
- **python-for-android:** https://python-for-android.readthedocs.io

---

**حالة المشروع:** ✅ جاهز للبناء  
**آخر تحديث:** 30 يناير 2026
