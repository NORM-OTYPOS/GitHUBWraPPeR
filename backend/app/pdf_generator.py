from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(profile_data: dict, path: str):
    c = canvas.Canvas(path, pagesize=letter)
    c.drawString(100, 750, f"GitHub Profile Report for {profile_data['login']}")
    c.drawString(100, 730, f"Name: {profile_data.get('name', 'N/A')}")
    c.drawString(100, 710, f"Public Repos: {profile_data['public_repos']}")
    # Add more details from profile_data as needed
    c.save()
