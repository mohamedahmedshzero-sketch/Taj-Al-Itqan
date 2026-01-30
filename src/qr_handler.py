# qr_handler.py
# إدارة إنشاء ومشاركة رموز QR للطلاب
# -*- coding: utf-8 -*-

import qrcode
from PIL import Image, ImageDraw, ImageFont
import webbrowser
import os
from pathlib import Path
try:
    from kivy.app import App
except Exception:
    App = None
import urllib.parse

# محاولة استيراد مكتبات الدعم العربي
try:
    from arabic_reshaper import reshape
    from bidi.algorithm import get_display
    ARABIC_SUPPORT = True
except ImportError:
    ARABIC_SUPPORT = False
    print("⚠️ تحذير: لم يتم العثور على مكتبات الدعم العربي (arabic-reshaper, python-bidi)")
    print("قد لا تظهر النصوص العربية بشكل صحيح في بطاقات QR")


def make_student_card(student_id, name, output_dir=None):
    """
    إنشاء بطاقة QR للطالب تحتوي على البيانات الأساسية
    
    Args:
        student_id: رقم الطالب الفريد
        name: اسم الطالب
        output_dir: مجلد حفظ البطاقات
    
    Returns:
        مسار الملف المحفوظ
    """
    # تحديد مجلد الحفظ: إذا لم يمرر أي مسار، استخدم مجلد بيانات التطبيق على أندرويد/كـيفي
    if output_dir is None:
        try:
            if App:
                running_app = App.get_running_app()
                if running_app:
                    output_dir = os.path.join(running_app.user_data_dir, "cards")
                else:
                    output_dir = "./assets"
            else:
                output_dir = "./assets"
        except Exception:
            output_dir = "./assets"

    # التأكد من وجود المجلد
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # إنشاء الـ QR Code
    qr_data = f"TAJ_STUDENT_{student_id}"
    qr = qrcode.make(qr_data)
    qr_img = qr.convert('RGB')
    
    # معالجة النص العربي
    if ARABIC_SUPPORT:
        try:
            reshaped_text = get_display(reshape(f"الطالب: {name}"))
        except Exception as e:
            print(f"خطأ في معالجة النص العربي: {e}")
            reshaped_text = f"الطالب: {name}"
    else:
        reshaped_text = f"الطالب: {name}"
    
    # إنشاء البطاقة
    w, h = qr_img.size
    card = Image.new('RGB', (w, h + 80), 'white')
    card.paste(qr_img, (0, 0))
    
    # رسم النصوص
    draw = ImageDraw.Draw(card)
    try:
        # محاولة تحميل خط مضمّن (موجود في المشروع) أولاً
        possible_fonts = [
            "arial.ttf.ttf",
            "arial.ttf",
            "fonts/arial.ttf",
        ]
        loaded = False
        for pf in possible_fonts:
            try:
                font = ImageFont.truetype(pf, 20)
                id_font = ImageFont.truetype(pf, 16)
                loaded = True
                break
            except Exception:
                continue
        if not loaded:
            font = ImageFont.load_default()
            id_font = ImageFont.load_default()
    except Exception:
        font = ImageFont.load_default()
        id_font = ImageFont.load_default()
    
    # رسم اسم الطالب
    draw.text((w / 2, h + 15), reshaped_text, fill="black", font=font, anchor="mm")
    # رسم رقم الطالب
    draw.text((w / 2, h + 50), f"الرقم: {student_id}", fill="gray", font=id_font, anchor="mm")
    
    # حفظ البطاقة
    file_name = f"card_{student_id}.png"
    file_path = os.path.join(output_dir, file_name)
    card.save(file_path)
    
    return file_path


def share_qr_whatsapp(phone, student_name, card_path):
    """
    فتح تطبيق الواتساب لمشاركة بطاقة الـ QR
    
    Args:
        phone: رقم الهاتف (مع رمز الدولة، مثل: 966501234567)
        student_name: اسم الطالب
        card_path: مسار صورة البطاقة
    """
    message = f"السلام عليكم، هذه بطاقة الكيو أر الخاصة بالطالب {student_name} في حلقة تاج الإتقان."
    
    # تنسيق الرقم للتأكد من عدم وجود رموز غير ضرورية
    phone = str(phone).replace("+", "").replace(" ", "").replace("-", "")
    
    # إنشاء رابط الواتساب
    # تأكد من ترميز الرسالة بشكل صحيح
    quoted = urllib.parse.quote_plus(message)
    url = f"https://wa.me/{phone}?text={quoted}"
    
    try:
        webbrowser.open(url)
        print(f"✓ تم فتح الواتساب لمشاركة البطاقة: {card_path}")
        return True
    except Exception as e:
        print(f"✗ حدث خطأ عند فتح الواتساب: {e}")
        return False


def share_qr_email(email, student_name, card_path):
    """
    فتح برنامج البريد الإلكتروني لمشاركة البطاقة
    
    Args:
        email: عنوان البريد الإلكتروني
        student_name: اسم الطالب
        card_path: مسار صورة البطاقة
    """
    subject = f"بطاقة الكيو أر للطالب {student_name}"
    body = f"السلام عليكم،\n\nهذه بطاقة الكيو أر الخاصة بالطالب {student_name} في حلقة تاج الإتقان."
    
    url = f"mailto:{email}?subject={subject}&body={body}"
    
    try:
        webbrowser.open(url)
        print(f"✓ تم فتح البريد الإلكتروني لمشاركة البطاقة")
        return True
    except Exception as e:
        print(f"✗ حدث خطأ عند فتح البريد: {e}")
        return False
