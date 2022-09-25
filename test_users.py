import requests

SERVER = "http://localhost:8000"
END_POINT = "/api/v1.0/users"


def test_authentication():
    print("Testing Authentication on users")
    print("Must be authenticated to query the users")
    print("\n")
    url = f"{SERVER}{END_POINT}"
    page = requests.get(url)
    assert page.status_code == 401
    assert page.json() == {"detail": "Not authenticated"}
    
def run_tests():
    test_authentication()
    print("users tested, 2 assertion, 1 test passed")