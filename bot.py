import logging
import json
from fbchat import Client
from fbchat.models import Message

logger = logging.getLogger(__name__)

class MonsterBot(Client):
    def __init__(self, config):
        self.config = config
        self.config.validate()

        try:
            cookies = json.loads(self.config.COOKIES)
        except json.JSONDecodeError:
            cookies = self.config.COOKIES

        super().__init__(
            self.config.EMAIL,
            self.config.PASSWORD,
            session_cookies=cookies,
            user_agent="Mozilla/5.0"
        )

        logger.info(f"تم تهيئة {self.config.BOT_NAME} بنجاح")

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        try:
            if author_id == self.uid:
                return

            message_text = message_object.text or ""
            logger.info(f"رسالة من {author_id}: {message_text}")

            if message_text.startswith("/"):
                self.handle_command(message_text, thread_id, thread_type)
            else:
                self.send(
                    Message(text="مرحباً! أنا بوت مونستر. اكتب /help للمساعدة"),
                    thread_id=thread_id,
                    thread_type=thread_type
                )
        except Exception as e:
            logger.error(f"خطأ في معالجة الرسالة: {e}")

    def handle_command(self, command, thread_id, thread_type):
        cmd = command.split()[0].lower()

        commands = {
            "/help": "الأوامر:\n/help\n/ping\n/info",
            "/ping": "Pong!",
            "/info": f"{self.config.BOT_NAME} v{self.config.BOT_VERSION}"
        }

        response = commands.get(cmd, "أمر غير معروف. اكتب /help")

        self.send(
            Message(text=response),
            thread_id=thread_id,
            thread_type=thread_type
        )

    def run(self):
        logger.info("البوت جاهز للاستقبال...")
        self.listen()
