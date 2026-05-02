from core.crypto.aes_gcm import AESCipher

cipher = AESCipher()


def test_encrypt_decrypt():
    data = "hola mundo"
    encrypted = cipher.encrypt(data)
    decrypted = cipher.decrypt(encrypted)

    assert decrypted == data