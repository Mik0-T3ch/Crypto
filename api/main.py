from fastapi import FastAPI
from dotenv import load_dotenv

from api.routes.crypto import router as crypto_router
from api.routes.password import router as password_router
from api.routes.methods import router as methods_router

load_dotenv()

app = FastAPI()

app.include_router(crypto_router)
app.include_router(password_router)
app.include_router(methods_router)