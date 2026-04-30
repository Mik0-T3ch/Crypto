import hashlib

def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()

def verify_hash(text: str, hash_value: str) -> bool:
    return hash_text(text) == hash_value