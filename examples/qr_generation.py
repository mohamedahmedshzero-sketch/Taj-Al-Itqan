# examples/qr_generation.py
# أمثلة إنشاء بطاقات QR

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.qr_handler import make_student_card, share_qr_whatsapp
from src.database import DBManager


def example_qr_creation():
    """مثال: إنشاء بطاقة QR"""
    print("=" * 50)
    print("إنشاء بطاقات QR للطلاب")
    print("=" * 50)
    
    db = DBManager()
    
    # إضافة طالب جديد
    student_id = db.add_student(
        name="فاطمة أحمد",
        phone="966501234567",
        days="الثلاثاء والجمعة"
    )
    
    print(f"\n✓ تم إضافة الطالب برقم: {student_id}")
    
    # إنشاء بطاقة QR
    card_path = make_student_card(
        student_id=student_id,
        name="فاطمة أحمد",
        output_dir="./assets"
    )
    
    print(f"✓ تم إنشاء بطاقة QR")
    print(f"✓ المسار: {card_path}")
    
    # يمكنك الآن مشاركة البطاقة
    # share_qr_whatsapp(
    #     phone="966501234567",
    #     student_name="فاطمة أحمد",
    #     card_path=card_path
    # )


if __name__ == "__main__":
    print("\n🎨 أمثلة إنشاء بطاقات QR\n")
    
    try:
        example_qr_creation()
        print("\n" + "=" * 50)
        print("✓ تم إنشاء البطاقة بنجاح!")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n✗ حدث خطأ: {e}")
        import traceback
        traceback.print_exc()
