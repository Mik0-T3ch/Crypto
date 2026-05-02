from fastapi import APIRouter
from core.hashing.password import hash_password, verify_password
from api.schemas import PasswordHashRequest, PasswordVerifyRequest

router = APIRouter(
    prefix="/password",
    tags=["password"]
)


@router.post("/hash")
def password_hash(data: PasswordHashRequest):
    return {"hash": hash_password(data.password)}


@router.post("/verify")
def password_verify(data: PasswordVerifyRequest):
    return {"valid": verify_password(data.password, data.hashed)}