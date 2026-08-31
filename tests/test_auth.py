from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_login():
    response = client.post(
        '/auth/login',
        params={
            'username': 'admin',
            'password': '123456'
        }
    )

    assert response.status_code == 200

    data = response.json()
    assert 'access_token' in data
    assert data['token_type'] == 'bearer'
