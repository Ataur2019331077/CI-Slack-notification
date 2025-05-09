from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI"}

def test_check():
    response = client.get("/check")
    assert response.status_code == 200
    assert response.json() == {"message": "Check endpoint is working"}

def test_new_endpoint():
    response = client.get("/new-endpoint")
    assert response.status_code == 200
    assert response.json() == {"message": "This is a new endpoint!"}

def test_branch_created():
    response = client.get("/branch-created")
    assert response.status_code == 200
    assert response.json() == {"message": "This is from new branch"}


def test_branch_created_2():
    response = client.get("/branch-created-2")
    assert response.status_code == 200
    assert response.json() == {"message": "This is from new branch 2"}