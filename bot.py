import json
import logging
from fbchat import Client
from fbchat.models import Message

logger = logging.getLogger(__name__)


class MonsterBot(Client):
    """بوت مسنجر مونستر"""

    def __init__(self, config):
        """
        تهيئة البوت

        Args:
            config: كائن الإعدادات
        """
        self.config = config
        self.config.validate()

        # تحويل الكوكيز من JSON إذا لزم الأمر
        try:
            cookies = json.loads(self.config.COOKIES)
        except (json.JSONDecodeError, TypeError):
            cookies = self.config.COOKIES

        # استخراج c_user من الكوكيز لتعيين uid
        c_user = None
        if isinstance(cookies, dict):
            c_user = cookies.get("c_user")

        # تهيئة عميل Facebook مع البريد الإلكتروني وكلمة المرور
        super().__init__(
            email=self.config.EMAIL,
            password=self.config.PASSWORD,
            session_cookies=cookies,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )

        # تعيين uid من c_user إذا لم يُعيَّن بعد
        if c_user and not self.uid:
            self.uid = str(c_user)

        logger.info(f"✅ تم تهيئة {self.config.BOT_NAME} بنجاح")

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        """
        معالج الرسائل الواردة

        Args:
            author_id: معرف المرسل
            message_object: كائن الرسالة
            thread_id: معرف المحادثة
            thread_type: نوع المحادثة
        """
        try:
            # تجاهل رسائل البوت نفسه
            if author_id == self.uid:
                return

            message_text = message_object.text or ""
            logger.info(f"📨 رسالة من {author_id}: {message_text}")

            # معالجة الأوامر
            if message_text.startswith("/"):
                self.handle_command(message_text, thread_id, thread_type)
            else:
                # رد افتراضي
                self.send(
                    Message(text="👋 مرحباً! أنا بوت مونستر. اكتب /help للمساعدة"),
                    thread_id=thread_id,
                    thread_type=thread_type
                )

        except Exception as e:
            logger.error(f"❌ خطأ في معالجة الرسالة: {e}")

    def handle_command(self, command, thread_id, thread_type):
        """
        معالج الأوامر

        Args:
            command: الأمر المدخل
            thread_id: معرف المحادثة
            thread_type: نوع المحادثة
        """
        cmd = command.split()[0].lower()

        commands = {
            "/help": "📖 الأوامر المتاحة:\n/help - عرض المساعدة\n/ping - اختبار الاتصال\n/info - معلومات البوت",
            "/ping": "🏓 Pong!",
            "/info": f"🤖 {self.config.BOT_NAME} v{self.config.BOT_VERSION}",
        }

        response = commands.get(cmd, "❌ أمر غير معروف. اكتب /help للمساعدة")

        self.send(
            Message(text=response),
            thread_id=thread_id,
            thread_type=thread_type
        )

    def run(self):
        """تشغيل البوت"""
        logger.info("🚀 البوت جاهز للاستقبال...")
        self.listen()
