from core.hashing.password import hash_password, verify_password


def test_hash_and_verify():
    password = "123456"
    hashed = hash_password(password)

    assert verify_password(password, hashed) is True


def test_wrong_password():
    password = "123456"
    hashed = hash_password(password)

    assert verify_password("wrong", hashed) is False