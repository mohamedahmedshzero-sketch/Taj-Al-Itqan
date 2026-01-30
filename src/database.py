# database.py
# إدارة قاعدة البيانات والبيانات الدائمة
# -*- coding: utf-8 -*-

import sqlite3
import os
from pathlib import Path
try:
    from quran_data import get_full_quran_data
except ImportError as e:
    print(f"❌ خطأ في استيراد البيانات: {e}")
    raise
try:
    from kivy.app import App
except Exception:
    App = None


class DBManager:
    """مدير قاعدة البيانات الرئيسي"""
    
    def __init__(self, db_path=None):
        """
        تهيئة مدير قاعدة البيانات
        
        Args:
            db_path: مسار ملف قاعدة البيانات (اختياري)
        """
        # استخدام المسار الافتراضي إذا لم يتم تحديده
        if db_path is None:
            # على أندرويد/كحالة كايفي حاول استخدام مجلد بيانات التطبيق القابل للكتابة
            try:
                if App:
                    running_app = App.get_running_app()
                    if running_app:
                        db_path = os.path.join(running_app.user_data_dir, "taj_al_itqan.db")
                    else:
                        db_path = os.path.join(os.path.dirname(__file__), "..", "data", "taj_al_itqan.db")
                else:
                    db_path = os.path.join(os.path.dirname(__file__), "..", "data", "taj_al_itqan.db")
            except Exception:
                db_path = os.path.join(os.path.dirname(__file__), "..", "data", "taj_al_itqan.db")
        
        # التأكد من وجود مجلد البيانات
        Path(db_path).parent.mkdir(parents=True, exist_ok=True)
        
        self.db_path = db_path
        try:
            self.conn = sqlite3.connect(db_path, check_same_thread=False)
            self.conn.row_factory = sqlite3.Row  # للحصول على الصفوف كقواميس
            self.create_tables()
            self.initialize_quran()
        except sqlite3.Error as e:
            print(f"❌ خطأ في قاعدة البيانات: {e}")
            raise

    def create_tables(self):
        """إنشاء جداول قاعدة البيانات"""
        cursor = self.conn.cursor()
        
        # جدول السور
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS surahs (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL UNIQUE,
                verses INTEGER NOT NULL,
                juz INTEGER NOT NULL
            )
        ''')
        
        # جدول الطلاب
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                days TEXT,
                points INTEGER DEFAULT 100,
                registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status TEXT DEFAULT 'active'
            )
        ''')
        
        # جدول تسجيل السور (ما حفظه كل طالب)
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS student_surahs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                surah_id INTEGER NOT NULL,
                completion_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (surah_id) REFERENCES surahs(id),
                UNIQUE(student_id, surah_id)
            )
        ''')
        
        # جدول تقييم الطالب يومياً
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                attendance_date DATE NOT NULL,
                present BOOLEAN DEFAULT 1,
                notes TEXT,
                FOREIGN KEY (student_id) REFERENCES students(id),
                UNIQUE(student_id, attendance_date)
            )
        ''')
        
        self.conn.commit()

    def initialize_quran(self):
        """تهيئة بيانات القرآن في قاعدة البيانات"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM surahs")
        
        if cursor.fetchone()[0] == 0:
            quran_data = get_full_quran_data()
            cursor.executemany(
                "INSERT INTO surahs (id, name, verses, juz) VALUES (?, ?, ?, ?)",
                quran_data
            )
            self.conn.commit()
            print(f"✓ تم تحميل {len(quran_data)} سورة في قاعدة البيانات")

    # ========== عمليات الطلاب ==========
    
    def add_student(self, name, phone=None, days=None):
        """
        إضافة طالب جديد
        
        Args:
            name: اسم الطالب
            phone: رقم الهاتف (اختياري)
            days: أيام الحضور (اختياري)
        
        Returns:
            رقم الطالب الجديد
        """
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO students (name, phone, days) VALUES (?, ?, ?)",
            (name, phone, days)
        )
        self.conn.commit()
        return cursor.lastrowid

    def get_student(self, student_id):
        """الحصول على معلومات طالب"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        return cursor.fetchone()

    def get_all_students(self):
        """الحصول على قائمة جميع الطلاب"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM students WHERE status = 'active'")
        return cursor.fetchall()

    def update_student(self, student_id, **kwargs):
        """تحديث بيانات الطالب"""
        allowed_fields = ['name', 'phone', 'days', 'points', 'status']
        fields = {k: v for k, v in kwargs.items() if k in allowed_fields}
        
        if not fields:
            return False
        
        cursor = self.conn.cursor()
        set_clause = ", ".join([f"{k} = ?" for k in fields.keys()])
        values = list(fields.values()) + [student_id]
        
        cursor.execute(f"UPDATE students SET {set_clause} WHERE id = ?", values)
        self.conn.commit()
        return cursor.rowcount > 0

    def delete_student(self, student_id):
        """حذف (عدم تنشيط) طالب"""
        return self.update_student(student_id, status='inactive')

    # ========== عمليات السور المحفوظة ==========
    
    def record_surah_completion(self, student_id, surah_id):
        """تسجيل إكمال الطالب لسورة"""
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                "INSERT INTO student_surahs (student_id, surah_id) VALUES (?, ?)",
                (student_id, surah_id)
            )
            self.conn.commit()
            # إضافة نقاط
            self.update_student(student_id, points=self.get_student(student_id)['points'] + 10)
            return True
        except sqlite3.IntegrityError:
            return False  # السورة مسجلة بالفعل

    def get_student_surahs(self, student_id):
        """الحصول على السور المحفوظة لطالب"""
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT s.id, s.name, s.verses, s.juz, ss.completion_date
            FROM student_surahs ss
            JOIN surahs s ON ss.surah_id = s.id
            WHERE ss.student_id = ?
            ORDER BY ss.completion_date DESC
        ''', (student_id,))
        return cursor.fetchall()

    def get_completion_progress(self, student_id):
        """الحصول على نسبة الإكمال"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM student_surahs WHERE student_id = ?", (student_id,))
        completed = cursor.fetchone()[0]
        total = 114  # عدد السور
        return (completed, total, f"{(completed/total)*100:.1f}%")

    # ========== عمليات الحضور ==========
    
    def record_attendance(self, student_id, date, present=True, notes=None):
        """تسجيل حضور الطالب"""
        cursor = self.conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO attendance (student_id, attendance_date, present, notes)
                VALUES (?, ?, ?, ?)
            ''', (student_id, date, present, notes))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            # تحديث السجل الموجود
            cursor.execute('''
                UPDATE attendance SET present = ?, notes = ?
                WHERE student_id = ? AND attendance_date = ?
            ''', (present, notes, student_id, date))
            self.conn.commit()
            return True

    def get_student_attendance(self, student_id):
        """الحصول على سجل حضور الطالب"""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM attendance WHERE student_id = ? ORDER BY attendance_date DESC",
            (student_id,)
        )
        return cursor.fetchall()

    # ========== إغلاق قاعدة البيانات ==========
    
    def close(self):
        """إغلاق اتصال قاعدة البيانات"""
        self.conn.close()

    def __del__(self):
        """التنظيف عند حذف الكائن"""
        try:
            self.close()
        except:
            pass
