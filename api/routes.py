from fastapi import APIRouter, HTTPException, Depends
from core.registry import manager
from api.schemas import EncryptRequest, DecryptRequest
from api.dependencies.auth import verify_api_key

router = APIRouter()


@router.post("/encrypt", dependencies=[Depends(verify_api_key)])
def encrypt(data: EncryptRequest):
    category = manager.categories.get(data.method)

    if category is None:
        raise HTTPException(status_code=400, detail="Método no encontrado")

    if category != "secure":
        raise HTTPException(status_code=400, detail="Método no seguro")

    try:
        result = manager.encrypt(data.method, data.text)
        return {"result": result}
    except Exception:
        raise HTTPException(status_code=500, detail="Error al encriptar")


@router.post("/decrypt", dependencies=[Depends(verify_api_key)])
def decrypt(data: DecryptRequest):
    category = manager.categories.get(data.method)

    if category is None:
        raise HTTPException(status_code=400, detail="Método no encontrado")

    if category != "secure":
        raise HTTPException(status_code=400, detail="Método no seguro")

    try:
        result = manager.decrypt(data.method, data.text)
        return {"result": result}
    except Exception:
        raise HTTPException(status_code=500, detail="Error al desencriptar")


@router.get("/methods")
def methods():
    return manager.list_methods()