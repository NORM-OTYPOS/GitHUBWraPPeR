from pydantic import BaseModel, Field
from typing import List, Optional, Dict

class Repo(BaseModel):
    name: str
    language: str
    stargazers_count: int
    forks_count: int
    watchers_count: int

class User(BaseModel):
    login: str
    name: Optional[str] = None
    bio: Optional[str] = None
    avatar_url: Optional[str] = None

class TechStack(BaseModel):
    language: str
    count: int

class Experience(BaseModel):
    total_repos: int
    total_stars: int
    total_forks: int
    total_watchers: int

class Report(BaseModel):
    username: str
    name: Optional[str] = None
    bio: Optional[str] = None
    avatar_url: Optional[str] = None
    sentiment_analysis: Dict[str, float]
    advanced_analysis: str
    tech_stack: List[TechStack]
    experience: Experience
    impact_score: float

class UserRequest(BaseModel):
    username: str
