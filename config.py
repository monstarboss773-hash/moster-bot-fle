import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """إعدادات البوت"""
    
    # بيانات المصادقة
    EMAIL = os.getenv('EMAIL', '')
    PASSWORD = os.getenv('PASSWORD', '')
    APPSTAT = os.getenv('APPSTAT', '')
    COOKIES = os.getenv('COOKIES', '')
    
    # إعدادات البوت
    BOT_NAME = "Monster Bot"
    BOT_VERSION = "1.0.0"
    
    # إعدادات السجلات
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # التحقق من البيانات المطلوبة
    @classmethod
    def validate(cls):
        """التحقق من وجود جميع المتغيرات المطلوبة"""
        required = ['EMAIL', 'PASSWORD', 'APPSTAT', 'COOKIES']
        missing = [var for var in required if not getattr(cls, var)]
        
        if missing:
            raise ValueError(f"❌ متغيرات مفقودة: {', '.join(missing)}")
        
        return True
