import requests

SERVER = "http://localhost:8000"
END_POINT = "/login"

url = f"{SERVER}{END_POINT}"


def login(seq):
    print("Loging in")
    login_data = {
        "username": f"test_user{seq}@example.com",
        "password": "test123"
    }

    res = requests.post(url=url, data=login_data)

    assert res.status_code == 200
    return res.json()
