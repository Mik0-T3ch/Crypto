from core.security.api_key import verify_api_key

def auth_dependency(api_key: str):
    verify_api_key(api_key)