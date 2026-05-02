import os

def verify_api_key(key: str) -> bool:
    expected = os.getenv("API_KEY")
    return key == expected