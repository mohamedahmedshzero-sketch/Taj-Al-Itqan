# utils/validators.py
# التحقق من صحة البيانات

import re
from typing import Tuple


def validate_phone_number(phone: str) -> Tuple[bool, str]:
    """
    التحقق من صيغة رقم الهاتف
    يجب أن يبدأ برمز الدولة (مثل: 966، 20، إلخ)
    
    Args:
        phone: رقم الهاتف
    
    Returns:
        (صحة الرقم، رسالة الخطأ)
    """
    phone = str(phone).strip()
    
    # التحقق من أنه يحتوي على أرقام فقط
    if not re.match(r'^\d+$', phone):
        return False, "رقم الهاتف يجب أن يحتوي على أرقام فقط"
    
    # التحقق من الطول (10-15 رقم عادةً)
    if len(phone) < 10 or len(phone) > 15:
        return False, "رقم الهاتف غير صحيح (يجب أن يكون 10-15 أرقام)"
    
    return True, ""


def validate_student_name(name: str) -> Tuple[bool, str]:
    """
    التحقق من اسم الطالب
    
    Args:
        name: اسم الطالب
    
    Returns:
        (صحة الاسم، رسالة الخطأ)
    """
    name = str(name).strip()
    
    if not name:
        return False, "اسم الطالب مطلوب"
    
    if len(name) < 3:
        return False, "اسم الطالب يجب أن يكون 3 أحرف على الأقل"
    
    if len(name) > 100:
        return False, "اسم الطالب طويل جداً"
    
    return True, ""


def validate_days(days: str) -> Tuple[bool, str]:
    """
    التحقق من أيام الحضور
    
    Args:
        days: أيام الحضور
    
    Returns:
        (صحة الأيام، رسالة الخطأ)
    """
    if not days or not str(days).strip():
        return True, ""  # اختياري
    
    valid_days = ["الأحد", "الاثنين", "الثلاثاء", "الأربعاء", "الخميس", "الجمعة", "السبت"]
    days_list = [d.strip() for d in str(days).split(",")]
    
    for day in days_list:
        if day not in valid_days:
            return False, f"يوم '{day}' غير صحيح"
    
    return True, ""


def validate_quran_surah_number(number: int) -> Tuple[bool, str]:
    """
    التحقق من رقم السورة
    
    Args:
        number: رقم السورة
    
    Returns:
        (صحة الرقم، رسالة الخطأ)
    """
    try:
        num = int(number)
    except (ValueError, TypeError):
        return False, "رقم السورة يجب أن يكون رقماً صحيحاً"
    
    if num < 1 or num > 114:
        return False, "رقم السورة يجب أن يكون بين 1 و 114"
    
    return True, ""
