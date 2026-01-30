# config.py
# إعدادات التطبيق العامة

import os
from pathlib import Path

# المسارات الأساسية
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
ASSETS_DIR = BASE_DIR / "assets"
LOGS_DIR = BASE_DIR / "logs"

# إنشاء المجلدات إذا لم تكن موجودة
DATA_DIR.mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# قاعدة البيانات
DATABASE_PATH = DATA_DIR / "taj_al_itqan.db"

# إعدادات التطبيق
APP_NAME = "تاج الإتقان"
APP_VERSION = "1.0.0"
APP_TITLE = "تطبيق إدارة حلقات تحفيظ القرآن الكريم"

# إعدادات الواجهة
THEME_COLOR_PRIMARY = "Green"
THEME_STYLE = "Light"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

# إعدادات الطلاب
DEFAULT_INITIAL_POINTS = 100
POINTS_PER_SURAH = 10

# إعدادات الواتساب
WHATSAPP_MESSAGE_TEMPLATE = "السلام عليكم، هذه بطاقة الكيو أر الخاصة بالطالب {name} في حلقة تاج الإتقان."

# إعدادات البطاقات
QR_CARD_OUTPUT_DIR = ASSETS_DIR / "cards"
QR_CARD_SIZE_INCREASE = 80  # بكسل
QR_CARD_FONT_SIZE = 20

# إعدادات السور
TOTAL_SURAHS = 114

# المتغيرات البيئية
DEBUG_MODE = os.getenv("DEBUG", "False").lower() == "true"
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
