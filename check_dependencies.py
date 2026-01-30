#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
التحقق من المكتبات والتبعيات
Dependency checker script
"""

import sys
import subprocess
from importlib import import_module

# قائمة المكتبات المطلوبة
REQUIRED_PACKAGES = {
    'kivy': 'kivy',
    'kivymd': 'kivymd',
    'qrcode': 'qrcode',
    'PIL': 'Pillow',
    'arabic_reshaper': 'arabic-reshaper',
    'bidi': 'python-bidi',
    'dotenv': 'python-dotenv',
    'requests': 'requests',
}

def check_package(import_name, package_name):
    """التحقق من تثبيت المكتبة"""
    try:
        import_module(import_name)
        return True, None
    except ImportError as e:
        return False, package_name

def main():
    """تشغيل فحص المكتبات"""
    print("=" * 60)
    print("🔍 فحص المكتبات المطلوبة")
    print("=" * 60)
    
    missing_packages = []
    installed_packages = []
    
    for import_name, package_name in REQUIRED_PACKAGES.items():
        is_installed, package = check_package(import_name, package_name)
        
        if is_installed:
            status = "✅"
            installed_packages.append(import_name)
            print(f"{status} {import_name:20} مثبت")
        else:
            status = "❌"
            missing_packages.append(package)
            print(f"{status} {import_name:20} غير مثبت - يحتاج: {package}")
    
    print("=" * 60)
    
    if missing_packages:
        print(f"\n⚠️ عدد المكتبات غير المثبتة: {len(missing_packages)}")
        print("\nلتثبيتها، استخدم:")
        print(f"pip install {' '.join(missing_packages)}")
        print("\nأو:")
        print("pip install -r requirements.txt")
        return 1
    else:
        print("\n✅ جميع المكتبات مثبتة بنجاح!")
        print(f"✓ عدد المكتبات المثبتة: {len(installed_packages)}")
        return 0

if __name__ == "__main__":
    sys.exit(main())
