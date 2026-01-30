# utils/logger.py
# نظام تسجيل الأحداث (Logging)

import logging
import logging.handlers
from pathlib import Path
from config import LOGS_DIR, LOG_LEVEL, APP_NAME


def setup_logger(name="taj_al_itqan", level=LOG_LEVEL):
    """
    إعداد نظام التسجيل
    
    Args:
        name: اسم Logger
        level: مستوى التسجيل
    
    Returns:
        كائن Logger مهيأ
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level))
    
    # صيغة السجل
    formatter = logging.Formatter(
        '[%(asctime)s] %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # معالج الملف
    log_file = LOGS_DIR / f"{name}.log"
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=10485760,  # 10MB
        backupCount=5,
        encoding='utf-8'
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    # معالج وحدة التحكم (Console)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    return logger


# إنشاء Logger افتراضي
logger = setup_logger()
