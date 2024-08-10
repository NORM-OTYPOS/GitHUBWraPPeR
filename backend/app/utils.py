# utils.py
import requests
from typing import Any, Dict, List
from transformers import pipeline


GITHUB_API_URL = "https://api.github.com"


def fetch_github_user(username: str) -> Dict[str, Any]:
    """
    Fetches GitHub user data from the GitHub API.
    
    Parameters:
    - username (str): The GitHub username.
    
    Returns:
    - Dict[str, Any]: A dictionary containing user data.
    """
    url = f"{GITHUB_API_URL}/users/{username}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def fetch_github_repos(username: str) -> List[Dict[str, Any]]:
    """
    Fetches GitHub repositories for a given user.
    
    Parameters:
    - username (str): The GitHub username.
    
    Returns:
    - List[Dict[str, Any]]: A list of dictionaries, each containing data about a repository.
    """
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def evaluate_tech_stack(repos: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Evaluates the tech stack used across a user's repositories.
    
    Parameters:
    - repos (List[Dict[str, Any]]): A list of repositories data.
    
    Returns:
    - Dict[str, int]: A dictionary mapping programming languages to the number of repos using them.
    """
    tech_stack = {}
    for repo in repos:
        language = repo.get("language")
        if language:
            tech_stack[language] = tech_stack.get(language, 0) + 1
    return tech_stack


def evaluate_experience(repos: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Evaluates the experience of the user based on their repositories.
    
    Parameters:
    - repos (List[Dict[str, Any]]): A list of repositories data.
    
    Returns:
    - Dict[str, int]: A dictionary containing various experience metrics.
    """
    experience_metrics = {
        "total_repos": len(repos),
        "total_stars": sum(repo.get("stargazers_count", 0) for repo in repos),
        "total_forks": sum(repo.get("forks_count", 0) for repo in repos),
        "total_watchers": sum(repo.get("watchers_count", 0) for repo in repos),
    }
    return experience_metrics


def evaluate_repo_impact(repos: List[Dict[str, Any]]) -> float:
    """
    Evaluates the impact of the user's repositories.
    
    Parameters:
    - repos (List[Dict[str, Any]]): A list of repositories data.
    
    Returns:
    - float: A score representing the impact of the user's repositories.
    """
    total_stars = sum(repo.get("stargazers_count", 0) for repo in repos)
    total_forks = sum(repo.get("forks_count", 0) for repo in repos)
    total_watchers = sum(repo.get("watchers_count", 0) for repo in repos)
    
    # Simple formula for impact (this can be more complex as needed)
    impact_score = (total_stars * 0.5) + (total_forks * 0.3) + (total_watchers * 0.2)
    return impact_score


def generate_report_data(username: str) -> Dict[str, Any]:
    """
    Generates a comprehensive report for a GitHub user.
    
    Parameters:
    - username (str): The GitHub username.
    
    Returns:
    - Dict[str, Any]: A dictionary containing the report data.
    """
    user_data = fetch_github_user(username)
    repos_data = fetch_github_repos(username)
    
    report_data = {
        "username": user_data.get("login"),
        "name": user_data.get("name"),
        "bio": user_data.get("bio"),
        "avatar_url": user_data.get("avatar_url"),
        "tech_stack": evaluate_tech_stack(repos_data),
        "experience": evaluate_experience(repos_data),
        "impact_score": evaluate_repo_impact(repos_data),
    }
    
    return report_data

# Initialize the text-generation pipeline
text_generator = pipeline("text-generation", model="gpt-3")

def generate_text(prompt: str, max_length: int = 100) -> str:
    """
    Generate text based on the provided prompt using a Hugging Face LLM.
    """
    results = text_generator(prompt, max_length=max_length, num_return_sequences=1)
    return results[0]['generated_text']