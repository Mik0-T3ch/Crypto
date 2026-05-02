from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

API_KEY = "vP8sF3kL9XqR2zT7mN4yW6A1bC0dE5FgHiJkLmNo"


def test_encrypt_decrypt():
    res = client.post(
        "/crypto/encrypt",
        json={"text": "hola", "method": "aes"},
        headers={"x-api-key": API_KEY},
    )

    assert res.status_code == 200
    token = res.json()["result"]
    res = client.post(
        "/crypto/decrypt",
        json={"text": token, "method": "aes"},
        headers={"x-api-key": API_KEY},
    )

    assert res.status_code == 200
    assert res.json()["result"] == "hola"


def test_no_api_key():
    res = client.post(
        "/crypto/encrypt",
        json={"text": "hola", "method": "aes"},
    )

    assert res.status_code in [401, 422]


def test_wrong_api_key():
    res = client.post(
        "/crypto/encrypt",
        json={"text": "hola", "method": "aes"},
        headers={"x-api-key": "wrong_key"},
    )

    assert res.status_code == 401


def test_invalid_method():
    res = client.post(
        "/crypto/encrypt",
        json={"text": "hola", "method": "caesar"},
        headers={"x-api-key": API_KEY},
    )

    assert res.status_code == 400


def test_invalid_token():
    res = client.post(
        "/crypto/decrypt",
        json={"text": "basura", "method": "aes"},
        headers={"x-api-key": API_KEY},
    )

    assert res.status_code in [400, 500]


def test_password_hash_verify():
    res = client.post(
        "/password/hash",
        json={"password": "123456"},
    )

    assert res.status_code == 200
    hashed = res.json()["hash"]

    res = client.post(
        "/password/verify",
        json={"password": "123456", "hashed": hashed},
    )

    assert res.status_code == 200
    assert res.json()["valid"] is True


def test_encrypt_randomness():
    res1 = client.post(
        "/crypto/encrypt",
        json={"text": "hola", "method": "aes"},
        headers={"x-api-key": API_KEY},
    )

    res2 = client.post(
        "/crypto/encrypt",
        json={"text": "hola", "method": "aes"},
        headers={"x-api-key": API_KEY},
    )

    assert res1.json()["result"] != res2.json()["result"]