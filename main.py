import os
import json
from fbchat import Client
from fbchat.models import Message

# جلب بيانات الجلسة من متغيرات البيئة في Railway
appstate_raw = os.environ.get('APPSTATE_JSON')

class MessengerBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        # تجاهل الرسائل المرسلة من البوت نفسه
        if author_id != self.uid:
            self.send(Message(text="تم استلام رسالتك! البوت يعمل الآن بنجاح 🚀"), thread_id=thread_id, thread_type=thread_type)

if appstate_raw:
    try:
        # تحويل النص إلى قاموس (JSON)
        session_cookies = json.loads(appstate_raw)
        
        # تسجيل الدخول باستخدام الكوكيز فقط
        client = MessengerBot(' ', ' ', session_cookies=session_cookies)
        
        print("تم تسجيل الدخول بنجاح! البوت في حالة استماع...")
        client.listen()
    except Exception as e:
        print(f"حدث خطأ أثناء تسجيل الدخول: {e}")
else:
    print("خطأ: لم يتم العثور على APPSTATE_JSON في إعدادات Railway")
