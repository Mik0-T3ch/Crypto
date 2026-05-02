from fastapi import Header, HTTPException
from core.security.api_key import verify_api_key


def verify_api_key_dependency(x_api_key: str = Header(...)):
    if not verify_api_key(x_api_key):
        raise HTTPException(status_code=401, detail="Unauthorized")