from fastapi import APIRouter
import numpy as np
from src.utils.file_loader import load_csv
import json

router = APIRouter(prefix="/community")

nodes = load_csv("node_data.csv")
edges = load_csv("edge_data.csv")
recs = load_csv("local_recs.csv")

@router.get("/ids")
def get_community_ids():
    if nodes.empty:
        return {"status": "missing data", "message": "data upload required"}

    ids = nodes['community'].unique().tolist()

    return {
        "status": "success",
        "comm_ids": ids
    }

@router.get("/recs")
def get_local_recs():
    if recs.empty:
        return {"status": "missing data", "message": "data upload required"}

    return {
        "status": "success",
        "recs": recs.to_dict(orient="records")
    }

@router.get("/stats")
def get_stats():
    with open("../../data/processed/community_stats.json", "r") as jsonfile:
        stats = json.load(jsonfile)

    return {
        "status": "success",
        "stats": stats,
    }

@router.get("/{comm_id}")
def get_community(comm_id):
    if nodes.empty or edges.empty:
        return {"status": "missing data", "message": "data upload required"}

    df = nodes.loc[nodes['community'] == comm_id]
    valid_nodes = set(df['node'].astype(str))

    ed_df = edges[
        edges['source'].astype(str).isin(valid_nodes) &
        edges['target'].astype(str).isin(valid_nodes)
    ]
    community = df.replace({np.nan: None}).astype(object).to_dict(orient="records")
    comm_edges = ed_df.replace({np.nan: None}).astype(object).to_dict(orient="records")

    return {
        "status": "success",
        "nodes": community,
        "edges": comm_edges,
    }

@router.get('/metrics/{comm_id}')
def get_metrics(comm_id):
    if nodes.empty or edges.empty:
        return {"status": "missing data", "message": "data upload required"}

    df = nodes[['node', 'community', 'local_closeness', 'local_core_num', 'betweenness', 'local_zscore', 'local_P', 'local_role']]
    metrics = df.loc[nodes['community'] == comm_id]
    metrics = metrics.replace({np.nan: None}).astype(object).to_dict(orient="records")

    return {
        "status": "success",
        "nodes": metrics
    }

