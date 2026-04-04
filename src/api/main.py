#from pipelines.pipeline import run_pipeline
from fastapi import FastAPI
from .routers import node_metrics, recommendations, graph, communities

app = FastAPI()

app.include_router(node_metrics.router)
app.include_router(graph.router)
app.include_router(recommendations.router)
app.include_router(communities.router)

# if __name__ == '__main__':
#     run_pipeline()