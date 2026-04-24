from fastapi import FastAPI
from .routers import global_, communities

# Initialise FastAPI app instance
app = FastAPI()

# Register API routers for global metrics and community data
app.include_router(global_.router)
app.include_router(communities.router)