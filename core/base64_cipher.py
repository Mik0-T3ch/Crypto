import base64
from core.cipher import Cipher

class Base64Cipher(Cipher):

    name = "Base64"

    def encrypt(self, text: str) -> str:
        return base64.b64encode(text.encode()).decode()
