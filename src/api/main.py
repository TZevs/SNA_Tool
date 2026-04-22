from fastapi import FastAPI
from .routers import global_, communities, evals

app = FastAPI()

app.include_router(global_.router)
app.include_router(communities.router)
app.include_router(evals.router)
