import requests

SERVER = "http://localhost:8000"
END_POINT = "/api/v1.0/suppliers"


def test_authentication():
    print("Testing Authentication on suppliers")
    url = f"{SERVER}{END_POINT}"
    page = requests.get(url)
    assert page.status_code == 401
    assert page.json() == {"detail": "Not authenticated"}
    
def run_tests():
    test_authentication()
    print("suppliers tested, 2 assertion, 1 test passed")