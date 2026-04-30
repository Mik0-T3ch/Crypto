from fastapi import APIRouter
from core.registry import manager
from api.schemas import EncryptRequest, DecryptRequest

router = APIRouter()

@router.post("/encrypt")
def encrypt(data: EncryptRequest):
    result = manager.encrypt(data.method, data.text)
    return {"result": result}

@router.post("/decrypt")
def decrypt(data: DecryptRequest):
    result = manager.decrypt(data.method, data.text)
    return {"result": result}