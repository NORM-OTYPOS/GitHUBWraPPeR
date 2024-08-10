import pytest
from fastapi.testclient import TestClient

from app import app
from app.utils import (
    fetch_github_user, 
    fetch_github_repos, 
    evaluate_tech_stack, 
    evaluate_experience, 
    evaluate_repo_impact, 
    generate_report_data
)

client = TestClient(app)

# Mock data for testing
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

def test_fetch_github_user(mock_github_user):
    user_data = fetch_github_user("testuser")
    assert user_data["login"] == "testuser"
    assert user_data["name"] == "Test User"
    assert user_data["bio"] == "This is a test user"
    assert user_data["avatar_url"] == "https://example.com/avatar.jpg"

def test_fetch_github_repos(mock_github_repos):
    repos_data = fetch_github_repos("testuser")
    assert len(repos_data) == 3
    assert repos_data[0]["language"] == "Python"

def test_evaluate_tech_stack():
    tech_stack = evaluate_tech_stack(mock_repos_data)
    assert tech_stack["Python"] == 2
    assert tech_stack["JavaScript"] == 1

def test_evaluate_experience():
    experience = evaluate_experience(mock_repos_data)
    assert experience["total_repos"] == 3
    assert experience["total_stars"] == 45
    assert experience["total_forks"] == 19
    assert experience["total_watchers"] == 14

def test_evaluate_repo_impact():
    impact_score = evaluate_repo_impact(mock_repos_data)
    assert impact_score == (45 * 0.5) + (19 * 0.3) + (14 * 0.2)

def test_generate_report_data(mock_github_user, mock_github_repos):
    report_data = generate_report_data("testuser")
    assert report_data["username"] == "testuser"
    assert report_data["tech_stack"]["Python"] == 2
    assert report_data["experience"]["total_stars"] == 45
    assert report_data["impact_score"] == (45 * 0.5) + (19 * 0.3) + (14 * 0.2)

def test_get_report_route(mock_github_user, mock_github_repos):
    response = client.get("/report/testuser")
    assert response.status_code == 200
    json_response = response.json()
    assert json_response["username"] == "testuser"
    assert "tech_stack" in json_response
    assert "experience" in json_response
    assert "impact_score" in json_response
