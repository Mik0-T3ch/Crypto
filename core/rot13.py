import codecs
from core.cipher import Cipher

class Rot13Cipher(Cipher):

    name = "ROT13"

    def encrypt(self, text: str) -> str:
        return codecs.encode(text, "rot_13")
