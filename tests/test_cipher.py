from core.crypto.aes_gcm import AESCipher
import pytest

cipher = AESCipher()


def test_encrypt_decrypt():
    data = "hola mundo"
    encrypted = cipher.encrypt(data)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == data


def test_wrong_token():
    with pytest.raises(Exception):
        cipher.decrypt("esto no es valido")


def test_empty_string():
    data = ""
    encrypted = cipher.encrypt(data)
    decrypted = cipher.decrypt(encrypted)
    assert decrypted == data


def test_multiple_encryptions():
    data = "same text"

    e1 = cipher.encrypt(data)
    e2 = cipher.encrypt(data)

    assert e1 != e2