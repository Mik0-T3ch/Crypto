from core.crypto.aes_gcm import encrypt, decrypt

def test_encrypt_decrypt():
    data = "hola mundo"

    encrypted = encrypt(data)
    decrypted = decrypt(encrypted)

    assert decrypted == data