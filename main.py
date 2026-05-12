import os
import logging
from dotenv import load_dotenv
from fbchat import Client
from fbchat.models import Message
from config import Config
from bot import MonsterBot

# تحميل متغيرات البيئة
load_dotenv()

# إعداد السجلات
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def main():
    """تشغيل بوت مونستر"""
    try:
        config = Config()
        bot = MonsterBot(config)
        logger.info("🤖 بوت مونستر يعمل الآن...")
        bot.run()
    except Exception as e:
        logger.error(f"❌ خطأ في تشغيل البوت: {e}")
        raise

if __name__ == "__main__":
    main()
