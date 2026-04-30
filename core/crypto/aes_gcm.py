from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64
from core.security.key_manager import get_master_key

def decrypt(token: str) -> str:
    key = get_master_key()
    aesgcm = AESGCM(key)

    try:
        decoded = base64.urlsafe_b64decode(token)
    except Exception:
        raise ValueError("Invalid or corrupted token")

    if len(decoded) < 12:
        raise ValueError("Invalid or corrupted token")

    nonce = decoded[:12]
    ciphertext = decoded[12:]

    try:
        decrypted = aesgcm.decrypt(nonce, ciphertext, None)
    except Exception:
        raise ValueError("Invalid or corrupted token")

    return decrypted.decode()