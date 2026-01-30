# examples/basic_usage.py
# أمثلة استخدام أساسية

from pathlib import Path
import sys

# إضافة المسار الأب
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.database import DBManager
from src.qr_handler import make_student_card, share_qr_whatsapp
from src.quran_data import get_surah_by_number, get_surah_by_name
from utils.validators import validate_phone_number, validate_student_name


def example_1_basic_operations():
    """مثال 1: العمليات الأساسية"""
    print("=" * 50)
    print("مثال 1: العمليات الأساسية")
    print("=" * 50)
    
    # إنشاء مدير قاعدة البيانات
    db = DBManager()
    
    # إضافة طلاب
    student1_id = db.add_student(
        name="محمد علي",
        phone="966501234567",
        days="الأحد، الخميس"
    )
    print(f"✓ تم إضافة الطالب برقم: {student1_id}")
    
    # الحصول على معلومات الطالب
    student = db.get_student(student1_id)
    print(f"✓ بيانات الطالب: {dict(student)}")
    
    # عرض جميع الطلاب
    all_students = db.get_all_students()
    print(f"✓ عدد الطلاب: {len(all_students)}")
    for s in all_students:
        print(f"  - {s['name']} ({s['id']})")


def example_2_surah_operations():
    """مثال 2: عمليات السور"""
    print("\n" + "=" * 50)
    print("مثال 2: عمليات السور")
    print("=" * 50)
    
    db = DBManager()
    
    # الحصول على معلومات السورة
    surah = get_surah_by_number(1)
    print(f"✓ السورة الأولى: {surah[1]} - {surah[2]} آية")
    
    surah_by_name = get_surah_by_name("البقرة")
    print(f"✓ سورة البقرة: {surah_by_name[2]} آية")
    
    # تسجيل إكمال سورة
    student_id = 1
    db.record_surah_completion(student_id, surah_id=1)
    print(f"✓ تم تسجيل إكمال السورة الأولى للطالب {student_id}")
    
    # الحصول على السور المحفوظة
    student_surahs = db.get_student_surahs(student_id)
    print(f"✓ السور المحفوظة:")
    for s in student_surahs:
        print(f"  - {s['name']} ({s['verses']} آية)")
    
    # الحصول على نسبة الإكمال
    completed, total, percentage = db.get_completion_progress(student_id)
    print(f"✓ نسبة الإكمال: {completed}/{total} ({percentage})")


def example_3_attendance():
    """مثال 3: تسجيل الحضور"""
    print("\n" + "=" * 50)
    print("مثال 3: تسجيل الحضور")
    print("=" * 50)
    
    db = DBManager()
    
    # تسجيل الحضور
    db.record_attendance(
        student_id=1,
        date="2026-01-28",
        present=True,
        notes="طالب متفاني"
    )
    print(f"✓ تم تسجيل حضور الطالب")
    
    # الحصول على سجل الحضور
    attendance = db.get_student_attendance(1)
    print(f"✓ سجل الحضور:")
    for a in attendance:
        status = "حاضر" if a['present'] else "غائب"
        print(f"  - {a['attendance_date']}: {status}")


def example_4_validation():
    """مثال 4: التحقق من البيانات"""
    print("\n" + "=" * 50)
    print("مثال 4: التحقق من البيانات")
    print("=" * 50)
    
    # التحقق من رقم الهاتف
    valid, msg = validate_phone_number("966501234567")
    print(f"✓ التحقق من الهاتف: {valid}")
    
    valid, msg = validate_phone_number("123")
    print(f"✓ التحقق من هاتف قصير: {valid} - {msg}")
    
    # التحقق من الاسم
    valid, msg = validate_student_name("محمد علي")
    print(f"✓ التحقق من الاسم: {valid}")
    
    valid, msg = validate_student_name("م")
    print(f"✓ التحقق من اسم قصير: {valid} - {msg}")


if __name__ == "__main__":
    print("🎓 أمثلة استخدام تاج الإتقان\n")
    
    try:
        example_1_basic_operations()
        example_2_surah_operations()
        example_3_attendance()
        example_4_validation()
        
        print("\n" + "=" * 50)
        print("✓ تم تنفيذ جميع الأمثلة بنجاح!")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n✗ حدث خطأ: {e}")
        import traceback
        traceback.print_exc()
