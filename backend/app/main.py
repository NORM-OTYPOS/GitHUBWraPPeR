from fastapi import FastAPI
from fastapi import FastAPI, HTTPException
from app.models import UserRequest, Report
from app.routes import router as github_router

app = FastAPI()

@app.get("/report/{username}", response_model=Report)
async def get_user_report(username: str):
    # Example logic
    if username == "invalid":
        raise HTTPException(status_code=404, detail="User not found")
    report = generate_user_report(username)  # Your function to generate the report
    return report

app.include_router(github_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
