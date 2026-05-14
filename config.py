import os

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    def load_dotenv(*_args, **_kwargs):
        return False

load_dotenv()


class Config:
    def __init__(self):
        self.APPSTAT = os.getenv("APPSTAT", "").strip()
        self.COOKIES = os.getenv("COOKIES", "").strip()

        self.EMAIL = os.getenv("EMAIL", "").strip()
        self.PASSWORD = os.getenv("PASSWORD", "").strip()

        self.BOT_NAME = "Monster Bot"
        self.BOT_VERSION = "1.0.0"

        self.LOG_LEVEL = (os.getenv("LOG_LEVEL", "INFO") or "INFO").strip()

    def validate(self):
        required = ["EMAIL", "PASSWORD", "COOKIES"]
        missing = [var for var in required if not getattr(self, var, "")]
        if missing:
            raise ValueError(f"متغيرات مفقودة: {', '.join(missing)}")
        return True
