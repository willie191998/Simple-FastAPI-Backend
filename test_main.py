from fastapi.testclient import TestClient
from main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
import os
import pytest

# Set up the testing database URL
SQLALCHEMY_DATABASE_URL = os.getenv('TEST_DATABASE_URL')

# Create a new engine instance
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Create a new session local for the test
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency to use the test database
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Use the FastAPI TestClient to send requests
app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Create a test user in the test database (optional)
@pytest.fixture(scope="module")

def test_get_all_users(create_test_user):
    response = client.get("/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_user_not_found():
    response = client.get("/nonexistent_id")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_get_all_users_not_found():
    # Clear the test database or set up to have no users
    response = client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "No users found"}
