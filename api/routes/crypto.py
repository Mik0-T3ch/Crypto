from fastapi import APIRouter, HTTPException, Depends
from core.registry import manager
from api.schemas import EncryptRequest, DecryptRequest
from api.dependencies.auth import verify_api_key_dependency

router = APIRouter(
    prefix="/crypto",
    tags=["crypto"],
    dependencies=[Depends(verify_api_key_dependency)]
)


@router.post("/encrypt")
def encrypt(data: EncryptRequest):
    category = manager.categories.get(data.method)

    if category is None:
        raise HTTPException(status_code=400, detail="Método no encontrado")

    if category != "secure":
        raise HTTPException(status_code=400, detail="Método no permitido")

    try:
        result = manager.encrypt(data.method, data.text)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Error interno")


@router.post("/decrypt")
def decrypt(data: DecryptRequest):
    category = manager.categories.get(data.method)

    if category is None:
        raise HTTPException(status_code=400, detail="Método no encontrado")

    if category != "secure":
        raise HTTPException(status_code=400, detail="Método no permitido")

    try:
        result = manager.decrypt(data.method, data.text)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Error interno")