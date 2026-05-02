class CipherManager:
    def __init__(self):
        self.ciphers = {}
        self.categories = {}

    def register(self, name, cipher, category):
        self.ciphers[name] = cipher
        self.categories[name] = category

    def encrypt(self, name, text):
        if name not in self.ciphers:
            raise ValueError("Método no encontrado")

        return self.ciphers[name].encrypt(text)

    def decrypt(self, name, text):
        if name not in self.ciphers:
            raise ValueError("Método no encontrado")

        return self.ciphers[name].decrypt(text)

    def list_methods(self):
        return [
            name for name, category in self.categories.items()
            if category == "secure"
        ]


from core.educational.caesar import CaesarCipher
from core.encoding.base64 import Base64Cipher
from core.crypto.aes_gcm import AESCipher

manager = CipherManager()

manager.register("caesar", CaesarCipher(3), "educational")
manager.register("base64", Base64Cipher(), "encoding")
manager.register("aes", AESCipher(), "secure")