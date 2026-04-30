import base64

class Base64Cipher:

    def encrypt(self, text: str) -> str:
        return base64.b64encode(text.encode()).decode()

    def decrypt(self, text: str) -> str:
        return base64.b64decode(text.encode()).decode()