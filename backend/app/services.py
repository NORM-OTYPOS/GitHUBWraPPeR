import requests
from app.pdf_generator import create_pdf
from app.utils import generate_text

def fetch_github_profile(url: str) -> dict:
    username = url.split("/")[-1]
    response = requests.get(f"https://api.github.com/users/{username}")
    if response.status_code == 200:
        return response.json()
    return None

def generate_pdf_report(profile_data: dict) -> str:
    pdf_path = f"reports/{profile_data['login']}_report.pdf"
    create_pdf(profile_data, pdf_path)
    return pdf_path

def generate_user_report(username: str) -> dict:
    """
    Generate a comprehensive report for a GitHub user, including advanced analysis using an LLM.
    """
    # Fetch user data and repositories (assuming these functions are defined elsewhere)
    user_data = fetch_github_user(username)
    repos_data = fetch_github_repos(username)
    
    # Generate enhanced analysis based on user's bio
    prompt = f"Analyze the following GitHub bio and provide a summary: {user_data.get('bio', '')}"
    advanced_analysis = generate_text(prompt)
    
    # Generate tech stack, experience, and impact score (assuming these functions are defined elsewhere)
    tech_stack = evaluate_tech_stack(repos_data)
    experience = evaluate_experience(repos_data)
    impact_score = evaluate_repo_impact(repos_data)
    
    # Compile the report
    report = {
        "username": user_data.get("login"),
        "name": user_data.get("name"),
        "bio": user_data.get("bio"),
        "avatar_url": user_data.get("avatar_url"),
        "advanced_analysis": advanced_analysis,
        "tech_stack": tech_stack,
        "experience": experience,
        "impact_score": impact_score
    }
    
    return report
