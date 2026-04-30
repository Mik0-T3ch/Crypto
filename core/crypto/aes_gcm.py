from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64
from core.security.key_manager import get_master_key

def encrypt(data: str) -> str:
    key = get_master_key()
    aesgcm = AESGCM(key)

    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, data.encode(), None)

    return base64.b64encode(nonce + ciphertext).decode()


def decrypt(token: str) -> str:
    key = get_master_key()
    aesgcm = AESGCM(key)

    decoded = base64.b64decode(token)

    nonce = decoded[:12]
    ciphertext = decoded[12:]

    decrypted = aesgcm.decrypt(nonce, ciphertext, None)

    return decrypted.decode()