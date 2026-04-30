from pydantic import BaseModel

class EncryptRequest(BaseModel):
    text: str
    method: str

class DecryptRequest(BaseModel):
    text: str
    method: str

class HashRequest(BaseModel):
    text: str

class VerifyRequest(BaseModel):
    text: str
    hash: str