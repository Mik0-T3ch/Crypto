from fastapi import APIRouter, HTTPException
from api.schemas import EncryptRequest, DecryptRequest
from core.cipher_manager import manager

router = APIRouter()


@router.get("/test")
def test():
    return {"msg": "API funcionando"}


@router.post("/encrypt")
def encrypt(data: EncryptRequest):
    try:
        result = manager.encrypt(data.method, data.text)
        return {"result": result}
    except Exception:
        raise HTTPException(status_code=400, detail="Cipher no encontrado")


@router.post("/decrypt")
def decrypt(data: DecryptRequest):
    try:
        result = manager.decrypt(data.method, data.text)
        return {"result": result}
    except Exception:
        raise HTTPException(status_code=400, detail="Cipher no encontrado")