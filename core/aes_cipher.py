from cryptography.fernet import Fernet

class AESCipher:
    def __init__(self, key=None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, text: str) -> str:
        return self.cipher.encrypt(text.encode()).decode()

    def decrypt(self, text: str) -> str:
        return self.cipher.decrypt(text.encode()).decode()