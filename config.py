import os

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    def load_dotenv(*_args, **_kwargs):
        return False

load_dotenv()

class Config:
    APPSTAT = os.getenv('APPSTAT', '').strip()
    COOKIES = os.getenv('COOKIES', '').strip()

    EMAIL = os.getenv('EMAIL', '').strip()
    PASSWORD = os.getenv('PASSWORD', '').strip()

    BOT_NAME = "Monster Bot"
    BOT_VERSION = "1.0.0"

    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').strip()

    @classmethod
    def validate(cls):
        required = ['APPSTAT', 'COOKIES', 'EMAIL', 'PASSWORD']
        missing = [var for var in required if not getattr(cls, var, '')]

        if missing:
            raise ValueError(f"❌ متغيرات مفقودة: {', '.join(missing)}")

        return True
