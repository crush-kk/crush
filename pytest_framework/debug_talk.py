from commons.url_utils import  read_url


class DebugTalk:
    def env(self, key: str):
        return read_url()[key]
    def add(self, a, b):
        return a + b
    def password(self):
        return "123456"
