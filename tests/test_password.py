from core.hashing.password import hash_password, verify_password

def test_password_hashing():
    password = "secure123"

    hashed = hash_password(password)

    assert verify_password(password, hashed) == True
    assert verify_password("wrong", hashed) == False