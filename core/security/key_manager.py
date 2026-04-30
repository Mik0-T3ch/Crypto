import os
import base64

def get_master_key() -> bytes:
    key = os.getenv("VAULT_MASTER_KEY")

    if not key:
        raise Exception("VAULT_MASTER_KEY not set")

    try:
        return base64.b64decode(key)
    except Exception:
        raise Exception("Invalid base64 key")