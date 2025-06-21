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

def test_adding_subbranch():
    response = client.get("/adding-subbranch")
    assert response.status_code == 200
    assert response.json() == {"message": "This is a new subbranch!"}