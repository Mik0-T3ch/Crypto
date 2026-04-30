import os
import base64
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class AESCipher:
    def __init__(self, key: bytes | None = None):
        self.key = key or AESGCM.generate_key(bit_length=256)
        self.aesgcm = AESGCM(self.key)

    def encrypt(self, text: str) -> dict:
        nonce = os.urandom(12)
        ciphertext = self.aesgcm.encrypt(nonce, text.encode(), None)

        return {
            "ciphertext": base64.b64encode(ciphertext).decode(),
            "nonce": base64.b64encode(nonce).decode(),
            "key": base64.b64encode(self.key).decode()
        }

    def decrypt(self, data: dict) -> str:
        try:
            ciphertext = base64.b64decode(data["ciphertext"])
            nonce = base64.b64decode(data["nonce"])
            key = base64.b64decode(data["key"])

            aesgcm = AESGCM(key)
            plaintext = aesgcm.decrypt(nonce, ciphertext, None)

            return plaintext.decode()
        except Exception:
            raise ValueError("Error al desencriptar")