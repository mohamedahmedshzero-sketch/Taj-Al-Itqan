# main.py
# الواجهة الرئيسية للتطبيق
# -*- coding: utf-8 -*-

import sys
import os
from pathlib import Path

# إضافة المسار الحالي للاستيراد
sys.path.insert(0, str(Path(__file__).parent))

try:
    from kivymd.app import MDApp
    from kivy.lang import Builder
    from kivy.core.text import LabelBase
    from kivy.core.window import Window
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.label import Label
    from kivy.uix.button import Button
    from kivy.uix.popup import Popup
    from kivy.uix.scrollview import ScrollView
    from kivymd.uix.button import MDRaisedButton, MDFlatButton
    from kivymd.uix.textfield import MDTextField
    from kivymd.uix.label import MDLabel
    from kivymd.uix.boxlayout import MDBoxLayout
    # Use MDToolbar (older KivyMD versions) and fallback to ScrollView from kivy
    from kivymd.uix.toolbar import MDToolbar
    from kivy.uix.screenmanager import Screen, ScreenManager
    from kivymd.toast import toast
except ImportError as e:
    print(f"❌ خطأ في استيراد مكتبة Kivy: {e}")
    print("تأكد من تثبيت المكتبات: pip install -r requirements.txt")
    sys.exit(1)

from database import DBManager
from qr_handler import make_student_card, share_qr_whatsapp

# تحميل KV string
KV = '''
#:kivy 2.0

<StudentScreen>:
    FloatLayout:
        MDToolbar:
            title: "تاج الإتقان - إدارة الحلقات"
            pos_hint: {'top': 1}
            md_bg_color: app.theme_cls.primary_color
            font_name: 'ArabicFont'

        ScrollView:
            pos_hint: {'top': 0.95, 'x': 0, 'right': 1}
            size_hint_y: 0.95
            
            MDBoxLayout:
                orientation: 'vertical'
                padding: "20dp"
                spacing: "15dp"
                adaptive_height: True
                size_hint_y: None

                MDLabel:
                    text: "إضافة طالب جديد"
                    theme_text_color: "Primary"
                    font_style: "H6"
                    font_name: 'ArabicFont'
                    size_hint_y: None
                    height: "40dp"

                MDTextField:
                    id: s_name
                    hint_text: "اسم الطالب"
                    icon_right: "account"
                    size_hint_x: 1
                    mode: "rectangle"
                    font_name: 'ArabicFont'
                    
                MDTextField:
                    id: s_phone
                    hint_text: "رقم ولي الأمر (مع رمز الدولة)"
                    icon_right: "phone"
                    size_hint_x: 1
                    mode: "rectangle"
                    font_name: 'ArabicFont'

                MDTextField:
                    id: s_days
                    hint_text: "أيام الحضور (مثلاً: الأحد، الخميس)"
                    icon_right: "calendar-clock"
                    size_hint_x: 1
                    mode: "rectangle"
                    font_name: 'ArabicFont'

                MDRaisedButton:
                    text: "حفظ الطالب ومشاركة الكود"
                    size_hint_x: 1
                    size_hint_y: None
                    height: "50dp"
                    font_name: 'ArabicFont'
                    on_release: root.save_and_share()

                MDLabel:
                    text: "الطلاب المسجلون"
                    theme_text_color: "Primary"
                    font_style: "H6"
                    font_name: 'ArabicFont'
                    size_hint_y: None
                    height: "40dp"
                    padding_top: "20dp"

                MDLabel:
                    id: students_list_label
                    text: "لا توجد طلاب مسجلون حتى الآن"
                    font_name: 'ArabicFont'
                    size_hint_y: None
                    height: "50dp"
'''


class StudentScreen(Screen):
    """شاشة إدارة الطلاب الرئيسية"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = None
    
    def save_and_share(self):
        """حفظ الطالب ومشاركة الكود"""
        name_field = self.ids.s_name
        phone_field = self.ids.s_phone
        days_field = self.ids.s_days
        
        name = name_field.text.strip()
        phone = phone_field.text.strip()
        days = days_field.text.strip()
        
        # التحقق من الحقول المطلوبة
        if not name:
            toast("الرجاء إدخال اسم الطالب")
            return
        
        if not phone:
            toast("الرجاء إدخال رقم الهاتف")
            return
        
        try:
            # 1. حفظ الطالب في قاعدة البيانات
            student_id = self.app.db.add_student(name, phone, days)
            
            # 2. إنشاء صورة الكود
            card_path = make_student_card(student_id, name)
            
            # 3. مشاركة عبر الواتساب
            success = share_qr_whatsapp(phone, name, card_path)
            
            if success:
                toast(f"✓ تم حفظ الطالب ومشاركة الكود بنجاح!")
                # مسح الحقول
                name_field.text = ""
                phone_field.text = ""
                days_field.text = ""
                # تحديث القائمة
                self.refresh_students_list()
            else:
                toast("✓ تم حفظ البيانات (قد تحتاج لفتح الواتساب يدويا)")
                
        except Exception as e:
            toast(f"✗ حدث خطأ: {str(e)}")

    def refresh_students_list(self):
        """تحديث قائمة الطلاب"""
        try:
            students = self.app.db.get_all_students()
            students_data = [
                {
                    'id': s['id'],
                    'name': s['name'],
                    'phone': s['phone'] or 'غير متوفر',
                    'days': s['days'] or 'لم تحدد'
                }
                for s in students
            ]
            # يمكن تحديث RecycleView هنا
        except Exception as e:
            print(f"خطأ في تحديث القائمة: {e}")


class TajAlItqanApp(MDApp):
    """تطبيق تاج الإتقان الرئيسي"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = None
        # تسجيل الخطوط العربية وضبط RTL
        self._register_arabic_fonts()
    
    def _register_arabic_fonts(self):
        """تسجيل خطوط عربية وضبط دعم RTL"""
        try:
            # محاولة تحميل خط مضمّن ضمن المشروع أولاً
            possible_fonts = [
                os.path.join(os.path.dirname(__file__), '..', 'arial.ttf.ttf'),
                os.path.join(os.path.dirname(__file__), '..', 'assets', 'arial.ttf'),
                'arial.ttf',
            ]
            registered = False
            for pf in possible_fonts:
                try:
                    if os.path.exists(pf):
                        LabelBase.register(name='ArabicFont', fn_regular=pf)
                        print(f"✓ تم تسجيل الخط العربي من: {pf}")
                        registered = True
                        break
                except Exception:
                    continue

            if not registered:
                # محاولة تسجيل خط نظامي كنسخة احتياطية
                default_font = 'C:\\Windows\\Fonts\\arial.ttf' if sys.platform == 'win32' else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
                LabelBase.register(name='ArabicFont', fn_regular=default_font)
                print("✓ تم تسجيل الخط العربي من المسار الافتراضي")
        except Exception as e:
            print(f"⚠️ تنبيه: لم يتمكن من تسجيل خط عربي: {e}")
            print("   سيتم استخدام الخط الافتراضي")
        
        # ضبط Window للدعم الكامل
        Window.softinput_mode = "below_target"
    
    def build(self):
        """بناء واجهة التطبيق"""
        try:
            # تحميل KV string أولاً
            Builder.load_string(KV)
            
            self.theme_cls.primary_palette = "Green"
            self.theme_cls.theme_style = "Light"
            
            # تهيئة قاعدة البيانات
            self.db = DBManager()
            
            # إنشاء Screen Manager
            screen_manager = ScreenManager()
            
            # إنشاء شاشة الطلاب
            student_screen = StudentScreen(name='students')
            student_screen.app = self
            screen_manager.add_widget(student_screen)
            
            return screen_manager
        except Exception as e:
            print(f"❌ خطأ في بناء التطبيق: {e}")
            import traceback
            traceback.print_exc()
            raise
    
    def on_stop(self):
        """إغلاق قاعدة البيانات عند إيقاف التطبيق"""
        if self.db:
            try:
                self.db.close()
                print("✓ تم إغلاق قاعدة البيانات")
            except Exception as e:
                print(f"⚠️ تحذير أثناء إغلاق قاعدة البيانات: {e}")
        return True


def main():
    """نقطة الدخول الرئيسية"""
    try:
        app = TajAlItqanApp()
        app.run()
    except Exception as e:
        print(f"❌ فشل تشغيل التطبيق: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
