# Taj Al-Itqan Package
# نظام إدارة حلقات تحفيظ القرآن الكريم
# -*- coding: utf-8 -*-

import sys
import os

__version__ = "1.0.0"
__author__ = "Taj Al-Itqan Team"
__description__ = "تطبيق تاج الإتقان لإدارة حلقات تحفيظ القرآن الكريم"

# التأكد من إمكانية الاستيراد من هذا المجلد
_current_dir = os.path.dirname(__file__)
if _current_dir not in sys.path:
    sys.path.insert(0, _current_dir)

try:
    from .database import DBManager
    from .qr_handler import make_student_card, share_qr_whatsapp
    from .quran_data import get_full_quran_data
except ImportError:
    # السماح بالاستيراد المطلق
    from database import DBManager
    from qr_handler import make_student_card, share_qr_whatsapp
    from quran_data import get_full_quran_data

__all__ = [
    'DBManager',
    'make_student_card',
    'share_qr_whatsapp',
    'get_full_quran_data'
]

