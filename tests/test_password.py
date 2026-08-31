from core.password import hash_password, verify_password


def test_password_hash():
    password = '123456'
    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed) is True
    assert verify_password('wrong', hashed) is False
