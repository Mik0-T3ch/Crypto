from core.educational.caesar import CaesarCipher
from core.encoding.base64 import Base64Cipher
from core.crypto.aes_gcm import AESCipher

class CipherManager:

    def __init__(self):
        self.ciphers = {}

    def register(self, name, cipher):
        self.ciphers[name] = cipher

    def encrypt(self, name, text):
        if name not in self.ciphers:
            raise ValueError("Cipher no encontrado")
        return self.ciphers[name].encrypt(text)

    def decrypt(self, name, text):
        if name not in self.ciphers:
            raise ValueError("Cipher no encontrado")
        return self.ciphers[name].decrypt(text)

manager = CipherManager()
manager.register("caesar", CaesarCipher(3))
manager.register("base64", Base64Cipher())
manager.register("aes", AESCipher())