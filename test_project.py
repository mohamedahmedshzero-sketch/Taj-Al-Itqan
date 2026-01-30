#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# test_project.py
# اختبار شامل للمشروع للتحقق من أن كل شيء يعمل بشكل صحيح

import sys
import os
from pathlib import Path

# إضافة المسار الحالي
sys.path.insert(0, str(Path(__file__).parent / "src"))

def test_imports():
    """اختبار استيراد الوحدات"""
    print("🧪 اختبار الاستيراد...")
    try:
        from src.database import DBManager
        print("✓ DBManager تم استيراده بنجاح")
        
        from src.qr_handler import make_student_card
        print("✓ qr_handler تم استيراده بنجاح")
        
        from src.quran_data import get_full_quran_data
        print("✓ quran_data تم استيراده بنجاح")
        
        from utils.validators import validate_phone_number
        print("✓ validators تم استيراده بنجاح")
        
        from utils.logger import logger
        print("✓ logger تم استيراده بنجاح")
        
        return True
    except Exception as e:
        print(f"✗ خطأ في الاستيراد: {e}")
        return False


def test_database():
    """اختبار قاعدة البيانات"""
    print("\n🗄️  اختبار قاعدة البيانات...")
    try:
        from src.database import DBManager
        
        # إنشاء قاعدة بيانات اختبار
        db = DBManager(db_path="./test_db.db")
        print("✓ تم إنشاء قاعدة البيانات")
        
        # إضافة طالب
        student_id = db.add_student(
            name="محمد اختبار",
            phone="966501234567",
            days="الأحد"
        )
        print(f"✓ تم إضافة طالب برقم: {student_id}")
        
        # الحصول على الطالب
        student = db.get_student(student_id)
        assert student is not None
        print(f"✓ تم الحصول على بيانات الطالب: {student['name']}")
        
        # تسجيل سورة
        db.record_surah_completion(student_id, surah_id=1)
        print("✓ تم تسجيل سورة محفوظة")
        
        # الحصول على السور
        surahs = db.get_student_surahs(student_id)
        assert len(surahs) > 0
        print(f"✓ تم الحصول على {len(surahs)} سورة محفوظة")
        
        # التنظيف
        db.close()
        import os
        os.remove("./test_db.db")
        
        return True
    except Exception as e:
        print(f"✗ خطأ في اختبار قاعدة البيانات: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_quran_data():
    """اختبار بيانات القرآن"""
    print("\n📖 اختبار بيانات القرآن...")
    try:
        from src.quran_data import get_full_quran_data, get_surah_by_number, get_surah_by_name
        
        # الحصول على جميع السور
        quran = get_full_quran_data()
        assert len(quran) == 114
        print(f"✓ عدد السور: {len(quran)}")
        
        # البحث برقم
        surah = get_surah_by_number(1)
        assert surah[1] == "الفاتحة"
        print(f"✓ السورة الأولى: {surah[1]}")
        
        # البحث باسم
        surah_by_name = get_surah_by_name("البقرة")
        assert surah_by_name[0] == 2
        print(f"✓ سورة البقرة: رقم {surah_by_name[0]}")
        
        return True
    except Exception as e:
        print(f"✗ خطأ في اختبار بيانات القرآن: {e}")
        return False


def test_validators():
    """اختبار دوال التحقق"""
    print("\n✔️  اختبار دوال التحقق...")
    try:
        from utils.validators import (
            validate_phone_number,
            validate_student_name,
            validate_quran_surah_number
        )
        
        # اختبار رقم الهاتف
        valid, msg = validate_phone_number("966501234567")
        assert valid == True
        print("✓ رقم هاتف صحيح")
        
        # اختبار اسم الطالب
        valid, msg = validate_student_name("محمد علي")
        assert valid == True
        print("✓ اسم طالب صحيح")
        
        # اختبار رقم السورة
        valid, msg = validate_quran_surah_number(1)
        assert valid == True
        print("✓ رقم سورة صحيح")
        
        # اختبارات سلبية
        valid, msg = validate_phone_number("123")
        assert valid == False
        print("✓ كشف رقم هاتف خاطئ")
        
        return True
    except Exception as e:
        print(f"✗ خطأ في اختبار دوال التحقق: {e}")
        return False


def test_structure():
    """اختبار هيكل المشروع"""
    print("\n📁 اختبار هيكل المشروع...")
    try:
        required_dirs = [
            "src", "utils", "examples", "data", "assets", "logs"
        ]
        
        for dir_name in required_dirs:
            path = Path(dir_name)
            if path.exists() and path.is_dir():
                print(f"✓ مجلد {dir_name}/ موجود")
            else:
                print(f"✗ مجلد {dir_name}/ غير موجود")
                return False
        
        required_files = [
            "config.py", "requirements.txt", "setup.py"
        ]
        
        for file_name in required_files:
            path = Path(file_name)
            if path.exists() and path.is_file():
                print(f"✓ ملف {file_name} موجود")
            else:
                print(f"✗ ملف {file_name} غير موجود")
                return False
        
        return True
    except Exception as e:
        print(f"✗ خطأ في اختبار الهيكل: {e}")
        return False


def main():
    """تشغيل جميع الاختبارات"""
    print("=" * 50)
    print("🧪 اختبار مشروع تاج الإتقان")
    print("=" * 50)
    
    results = {
        "الاستيراد": test_imports(),
        "الهيكل": test_structure(),
        "بيانات القرآن": test_quran_data(),
        "التحقق": test_validators(),
        "قاعدة البيانات": test_database(),
    }
    
    print("\n" + "=" * 50)
    print("📊 النتائج:")
    print("=" * 50)
    
    for test_name, result in results.items():
        status = "✓ نجح" if result else "✗ فشل"
        print(f"{test_name:20} {status}")
    
    all_passed = all(results.values())
    
    print("\n" + "=" * 50)
    if all_passed:
        print("✓ جميع الاختبارات نجحت! المشروع جاهز للاستخدام.")
    else:
        print("✗ بعض الاختبارات فشلت. تحقق من الأخطاء أعلاه.")
    print("=" * 50)
    
    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
