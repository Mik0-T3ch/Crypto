import os
import base64
from dotenv import load_dotenv

load_dotenv()


def get_master_key() -> bytes:
    key = os.getenv("MASTER_KEY")

    if not key:
        raise RuntimeError("MASTER_KEY no configurada en .env")

    return base64.urlsafe_b64decode(key)