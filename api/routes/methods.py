from fastapi import APIRouter
from core.registry import manager

router = APIRouter(
    prefix="/utils",
    tags=["utils"]
)

@router.get("/methods")
def methods():
    return manager.list_methods()