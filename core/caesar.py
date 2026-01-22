from core.cipher import Cipher

class CaesarCipher(Cipher):

    name = "Caesar"

    def __init__(self, shift: int = 3):
        self.shift = shift

    def encrypt(self, text: str) -> str:
        result = ""

        for c in text:
            if c.isalpha():
                base = ord("A") if c.isupper() else ord("a")
                result += chr((ord(c) - base + self.shift) % 26 + base)
            else:
                result += c

        return result
