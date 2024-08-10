# __init__.py
from fastapi import FastAPI

from .routes import router

# Initialize FastAPI app
app = FastAPI(
    title="GitHub Wrapper",
    description="An API for generating comprehensive reports based on GitHub profiles.",
    version="1.0.0"
)

# Include routes from the routes module
app.include_router(router)

# Add any startup or shutdown events if needed
@app.on_event("startup")
async def startup_event():
    # Code to run on startup
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Code to run on shutdown
    pass
