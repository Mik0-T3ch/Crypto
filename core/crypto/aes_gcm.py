from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64
from core.security.key_manager import get_master_key


class AESCipher:
    def __init__(self):
        self.key = get_master_key()
        self.aesgcm = AESGCM(self.key)

    def encrypt(self, text: str) -> str:
        nonce = os.urandom(12)
        ciphertext = self.aesgcm.encrypt(nonce, text.encode(), None)
        token = base64.urlsafe_b64encode(nonce + ciphertext).decode()
        return token

    def decrypt(self, token: str) -> str:
        decoded = base64.urlsafe_b64decode(token)

        nonce = decoded[:12]
        ciphertext = decoded[12:]

        plaintext = self.aesgcm.decrypt(nonce, ciphertext, None)
        return plaintext.decode()