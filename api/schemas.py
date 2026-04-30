from pydantic import BaseModel
from typing import Union, Dict

class EncryptRequest(BaseModel):
    text: str
    method: str

class DecryptRequest(BaseModel):
    text: Union[str, Dict]
    method: str