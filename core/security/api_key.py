import os

VALID_KEYS = os.getenv("VAULT_API_KEYS", "").split(",")

def verify_api_key(key: str):
    if key not in VALID_KEYS:
        raise Exception("Unauthorized")