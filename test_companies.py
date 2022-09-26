import requests
from test_login import login

SERVER = "http://localhost:8000"
END_POINT = "/api/v1.0/companies"

url = f"{SERVER}{END_POINT}"

uuid_str: str


def test_authentication():
    print("Testing Authentication on companies")
    print("Must be authenticated to query the companies")
    print("\n")
    page = requests.get(url)
    assert page.status_code == 401
    assert page.json() == {"detail": "Not authenticated"}


def test_create_company(seq):
    print("Testing creating a company")
    print("\n")

    json_data = {
        "ruc": f"test_ruc {seq}",
        "name": f"test_name {seq}",
        "employees": 5,
        "email": f"test_user{seq}@example.com",
        "password": "test123",
        "username": "test user"
    }
    data = requests.post(url, json=json_data)
    assert data.status_code == 201


def test_login_and_query(seq):
    print("Querying a company with login")
    print("\n")
    data = login(seq)
    header = {
        "Authorization": f"{data['token_type']} {data['access_token']}"
    }
    page = requests.get(url=url, headers=header)
    global uuid_str
    uuid_str = page.json()[0]['uuid']
    assert page.status_code == 200
    assert len(page.json()) == 1
    
def test_update(seq):
    print("Updating a company without login")
    print("\n")
    json_data = {
        'ruc': f'upd_test_ruc {seq}',
        'name': f'upd_test name {seq}',
        'employees': 10
    }
    page = requests.put(url=f"{url}/{uuid_str}", json=json_data)
    # Cannot update company info without being logged in
    assert page.status_code == 401
    print("Updating a company with login")
    print("\n")
    data = login(seq)
    header = {
        "Authorization": f"{data['token_type']} {data['access_token']}"
    }
    page = requests.get(url=url, headers=header, json=json_data)
    assert page.status_code == 200


def run_tests(seq):
    test_authentication()
    test_create_company(seq)
    test_login_and_query(seq)
    test_update(seq)
    print("companies tested, 7 assertion, 4 test passed")
