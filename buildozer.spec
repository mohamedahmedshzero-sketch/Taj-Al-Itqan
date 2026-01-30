[app]

# (str) Title of your application
title = تاج الإتقان

# (str) Package name
package.name = tajalitqan

# -----------------------------------------------------------------------------
# الإعدادات الحيوية للأيقونة وشاشة التحميل (تم تفعيلها وتعديل المسار)
# -----------------------------------------------------------------------------

# (string) Presplash of the application (شاشة التحميل)
presplash.filename = splash.png

# (string) Icon of the application (أيقونة التطبيق)
icon.filename = icon.png

# (str) Package domain (needed for android/ios packaging)
package.domain = org.tajalitqan

# (source.dir) Source directory where the main.py live
source.dir = src

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf,txt,md

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests, bin, venv

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.py

# (str) Application versioning (method 1)
version = 1.0.0

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# python3,kivy
requirements = python3,kivy==2.2.0,kivymd==0.104.2,qrcode,pillow,arabic-reshaper,python-bidi,requests

# (str) Supported orientation (landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (string) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
#android.ndk = 23b

# (bool) Use --private data storage (True) or --dir public storage (False)
#android.private_storage = True

# (str) Android app theme, default is ok for Kivy-based application
# android.theme = "@android:style/Theme.NoTitleBar"

# (bool) Copy library templates into the libs_dir/templates
# directory (used for build)
android.copy_libs = 1

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a

# (bool) enables Android auto backup & restore. Disable it with False
android.allow_backup = True

# (str) XML file for custom backup rules (see the documentation)
# android.backup_rules =

# (str) If you need to insert variables into your AndroidManifest.xml file,
# you can use the token {{variable}}. For example, if you want to enter text
# with a % sign, you can use %{{variable}}%.
#android.meta_data = <meta-data android:name="com.google.android.gms.version"
#    android:value="@integer/google_play_services_version" />

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
#android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
#android.activity_include = %(source.dir)s/activity.xml

# (str) launchMode to set for the main activity.  One of the values provided
# in the following link are supported (it is expected to be supported in 1.5.0)
# https://developer.android.com/guide/topics/manifest/activity-element
# android.launch_mode = singleTask

# (list) Pattern to whitelist for the whole project
#android.whitelist = lib-dynload/termios.so

# (str) Path to a custom whitelist file
#android.whitelist = ./whitelist.txt

# (bool) Disable fail on build tools errors.
#android.disable_buildozer_check = False

#
# Python for android (p4a) specific
#

# (str) python-for-android PEP 517 provider
p4a.provider = pip

# (str) python-for-android branch to use, defaults to master
p4a.branch = develop

# (str) python-for-android git repo to use, defaults to official
#p4a.url = https://github.com/kivy/python-for-android

# (str) python-for-android directory (if empty, it will be automatically cloned from github)
#p4a.dir = ../python-for-android/

# (list) python-for-android blacklist modules
#p4a.blacklist = tests,lib-dynload/unicodedata.so

# (str) python-for-android modules dir
#p4a.modules_dir = ./modules/

# (list) copy library instead of making a libpymodules.so
p4a.copy_libs = 1

# (str) The bootstrap to use. Leave empty to let python-for-android choose.
p4a.bootstrap = sdl2


#
# (int) port number to specify an explicit --port= p4a argument (eg for bootstrap flask)
# android.port = 8000

#
# [app] section
#

# (bool) Indicate if the application should use AndroidX support libraries
# android.enable_androidx = True

# (bool) Indicate if the application should use the new Kivy toolchain
# android.use_legacy_toolchain = False

# (str) The services to add to the app using the Service class
#android.services = MyService

# (str) Permissions
#android.permissions = INTERNET

# (str) android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library templates into the libs_dir/templates
# directory (used for build)
# android.copy_libs = 1

# (str) The presplash title as Java code lines. You can leave it empty if you don't need a title
# android.presplash_title = MyApplication

# (str) Filename of OUYA Console icon. It must be a 732x412 png image.
# android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png

# (str) XML file to include as an intent filters in <activity> tag
# android.activity_include = %(source.dir)s/activity.xml

# (list) Pattern to whitelist for the whole project
# android.whitelist = lib-dynload/termios.so

# (str) Path to a custom whitelist file
# android.whitelist = ./whitelist.txt

# (bool) Disable fail on build tools errors.
# android.disable_buildozer_check = False

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning + pause before building
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = .buildozer

# (str) Path to build output (i.e. where the built APK will be placed)
bin_dir = ./bin
