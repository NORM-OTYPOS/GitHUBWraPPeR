import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

# Sample data for testing
mock_user_data = {
    "login": "testuser",
    "name": "Test User",
    "bio": "This is a test user",
    "avatar_url": "https://example.com/avatar.jpg"
}

mock_repos_data = [
    {"name": "repo1", "language": "Python", "stargazers_count": 10, "forks_count": 5, "watchers_count": 3},
    {"name": "repo2", "language": "JavaScript", "stargazers_count": 20, "forks_count": 8, "watchers_count": 7},
    {"name": "repo3", "language": "Python", "stargazers_count": 15, "forks_count": 6, "watchers_count": 4},
]

@pytest.fixture
def mock_github_user(monkeypatch):
    def mock_fetch_github_user(username: str):
        return mock_user_data
    monkeypatch.setattr("app.utils.fetch_github_user", mock_fetch_github_user)

@pytest.fixture
def mock_github_repos(monkeypatch):
    def mock_fetch_github_repos(username: str):
        return mock_repos_data
    monkeypatch.setattr("app.utils.fetch_github_repos", mock_fetch_github_repos)

def test_get_report_route(mock_github_user, mock_github_repos):
    response = client.get("/report/testuser")
    assert response.status_code == 200
    json_response = response.json()
    
    # Check the presence of required fields in the response
    assert "username" in json_response
    assert json_response["username"] == "testuser"
    assert "tech_stack" in json_response
    assert "experience" in json_response
    assert "impact_score" in json_response

    # Validate the tech stack
    tech_stack = json_response["tech_stack"]
    assert tech_stack["Python"] == 2
    assert tech_stack["JavaScript"] == 1

    # Validate experience metrics
    experience = json_response["experience"]
    assert experience["total_repos"] == 3
    assert experience["total_stars"] == 45
    assert experience["total_forks"] == 19
    assert experience["total_watchers"] == 14

    # Validate the impact score
    impact_score = json_response["impact_score"]
    assert impact_score == (45 * 0.5) + (19 * 0.3) + (14 * 0.2)

def test_get_report_route_not_found():
    response = client.get("/report/nonexistentuser")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_invalid_username():
    response = client.get("/report/!@#$%^&*()")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid username format"}
