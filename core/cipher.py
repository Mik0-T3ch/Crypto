from abc import ABC, abstractmethod

class Cipher(ABC):

    @abstractmethod
    def encrypt(self, text: str) -> str:
        pass
