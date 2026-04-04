from fastapi import APIRouter
import numpy as np
from src.utils.file_loader import load_csv

router = APIRouter(prefix="/communities")

nodes = load_csv("node_data.csv")
edges = load_csv("edge_data.csv")

@router.get("/{comm_id}")
def get_community(comm_id: str):
    if nodes.empty or edges.empty:
        return {"status": "missing data", "message": "data upload required"}

    df = nodes.loc[nodes['community'] == comm_id]
    ed_df = edges.loc[edges['source'].isin(df['node'])]

    community = df.replace({np.nan: None}).astype(object).to_dict(orient="records")
    comm_edges = ed_df.replace({np.nan: None}).astype(object).to_dict(orient="records")

    return {
        "status": "success",
        "community": community,
        "edges": comm_edges,
    }
