#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
نقطة الدخول الرئيسية للتطبيق
Entry point for the application
"""

import sys
import os

# إضافة مجلد src للمسار
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    """تشغيل التطبيق"""
    try:
        from main import TajAlItqanApp
        app = TajAlItqanApp()
        app.run()
    except ImportError as e:
        print(f"❌ خطأ في استيراد التطبيق: {e}")
        print("تأكد من تثبيت المكتبات:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ خطأ أثناء تشغيل التطبيق: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == '__main__':
    main()
