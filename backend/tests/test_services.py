import pytest
from app.services import (
    get_user_report,
    generate_pdf_report
)
from app.utils import (
    fetch_github_user,
    fetch_github_repos,
    evaluate_tech_stack,
    evaluate_experience,
    evaluate_repo_impact,
    generate_report_data
)

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
def mock_fetch_github_user(monkeypatch):
    def mock_fetch_github_user(username: str):
        return mock_user_data
    monkeypatch.setattr("app.utils.fetch_github_user", mock_fetch_github_user)

@pytest.fixture
def mock_fetch_github_repos(monkeypatch):
    def mock_fetch_github_repos(username: str):
        return mock_repos_data
    monkeypatch.setattr("app.utils.fetch_github_repos", mock_fetch_github_repos)

def test_get_user_report(mock_fetch_github_user, mock_fetch_github_repos):
    report_data = get_user_report("testuser")
    
    assert report_data["username"] == "testuser"
    assert report_data["name"] == "Test User"
    assert report_data["bio"] == "This is a test user"
    assert report_data["avatar_url"] == "https://example.com/avatar.jpg"
    
    tech_stack = report_data["tech_stack"]
    assert tech_stack["Python"] == 2
    assert tech_stack["JavaScript"] == 1
    
    experience = report_data["experience"]
    assert experience["total_repos"] == 3
    assert experience["total_stars"] == 45
    assert experience["total_forks"] == 19
    assert experience["total_watchers"] == 14
    
    impact_score = report_data["impact_score"]
    assert impact_score == (45 * 0.5) + (19 * 0.3) + (14 * 0.2)

def test_generate_pdf_report(mock_fetch_github_user, mock_fetch_github_repos):
    report_data = get_user_report("testuser")
    pdf_content = generate_pdf_report(report_data)
    
    # Check that the PDF content is not empty
    assert pdf_content is not None
    assert isinstance(pdf_content, bytes)


@pytest.fixture
def mock_generate_text(monkeypatch):
    def mock_generate_text(prompt: str, max_length: int = 100) -> str:
        return "This is a mocked advanced analysis based on the provided bio."
    monkeypatch.setattr("app.utils.generate_text", mock_generate_text)

def test_generate_user_report(mock_generate_text):
    report = generate_user_report("testuser")
    
    assert report["username"] == "testuser"
    assert report["name"] == "Test User"
    assert report["bio"] == "I am a passionate developer working on exciting projects."
    assert report["advanced_analysis"] == "This is a mocked advanced analysis based on the provided bio."
    
    tech_stack = report["tech_stack"]
    assert tech_stack["Python"] == 2
    assert tech_stack["JavaScript"] == 1
    
    experience = report["experience"]
    assert experience["total_repos"] == 3
    assert experience["total_stars"] == 45
    assert experience["total_forks"] == 19
    assert experience["total_watchers"] == 14
    
    impact_score = report["impact_score"]
    assert impact_score == (45 * 0.5) + (19 * 0.3) + (14 * 0.2)