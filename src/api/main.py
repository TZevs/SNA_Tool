#from pipelines.pipeline import run_pipeline
from fastapi import FastAPI
from .routers import global_, graph, communities

app = FastAPI()

app.include_router(global_.router)
app.include_router(graph.router)
app.include_router(communities.router)

# if __name__ == '__main__':
#     run_pipeline()