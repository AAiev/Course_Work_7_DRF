import requests

from config.settings import TELEGRAM_API_TOKEN, TELEGRAM_URL


class TelegramBotService:
    TOKEN = TELEGRAM_API_TOKEN
    URL = TELEGRAM_URL

    def __init__(self, chat_id, text):
        self.chat_id = chat_id
        self.text = text

    def send_message_tg(self):
        url = f"{self.URL}{self.TOKEN}/sendMessage"
        r = requests.post(url, data={"chat_id": self.chat_id, "text": self.text})

        if r.status_code != 200:
            raise Exception("post_text error")
