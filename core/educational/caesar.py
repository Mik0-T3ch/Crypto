class CaesarCipher:

    def __init__(self, shift: int):
        self.shift = shift

    def encrypt(self, text: str) -> str:
        result = ""
        for char in text:
            if char.isalpha():
                shift_base = 65 if char.isupper() else 97
                result += chr((ord(char) - shift_base + self.shift) % 26 + shift_base)
            else:
                result += char
        return result

    def decrypt(self, text: str) -> str:
        return CaesarCipher(-self.shift).encrypt(text)