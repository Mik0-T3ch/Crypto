from core.crypto.aes_gcm import encrypt, decrypt
import pytest

def test_encrypt_decrypt():
    data = "hola mundo"
    encrypted = encrypt(data)
    decrypted = decrypt(encrypted)
    assert decrypted == data


def test_wrong_token():
    with pytest.raises(Exception):
        decrypt("esto no es valido")


def test_empty_string():
    data = ""
    encrypted = encrypt(data)
    decrypted = decrypt(encrypted)
    assert decrypted == data


def test_multiple_encryptions():
    data = "same text"
    
    e1 = encrypt(data)
    e2 = encrypt(data)

    assert e1 != e2