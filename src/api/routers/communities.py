from fastapi import APIRouter
import numpy as np
from src.utils.file_loader import load_csv
import json

# Community API
router = APIRouter(prefix="/community")

# Use helper to load CSV's, in persistent storage outputted by the analysis pipeline, as DFs
nodes = load_csv("node_data.csv")
edges = load_csv("edge_data.csv")
recs = load_csv("local_recs.csv")

# GET all unique community IDs
@router.get("/ids")
def get_community_ids():
    if nodes.empty:
        return {"status": "missing data", "message": "data upload required"}

    ids = nodes['community'].unique().tolist()

    return {
        "status": "success",
        "comm_ids": ids
    }

# GET local role recommendations
@router.get("/recs")
def get_local_recs():
    if recs.empty:
        return {"status": "missing data", "message": "data upload required"}

    return {
        "status": "success",
        "recs": recs.to_dict(orient="records")
    }

# GET all statistics for each community
@router.get("/stats")
def get_stats():
    # Read statistics from community_stats JSON in persistent storage
    with open("../../data/processed/community_stats.json", "r") as jsonfile:
        stats = json.load(jsonfile)

    return {
        "status": "success",
        "stats": stats,
    }

# GET comm_id node and edges
@router.get("/{comm_id}")
def get_community(comm_id):
    if nodes.empty or edges.empty:
        return {"status": "missing data", "message": "data upload required"}

    # Get nodes with comm_id
    df = nodes.loc[nodes['community'] == comm_id]
    # Extract the node 'id' from df into a set
    valid_nodes = set(df['node'].astype(str))

    # Filters edges where both endpoints are within the community(valid_nodes)
    ed_df = edges[
        edges['source'].astype(str).isin(valid_nodes) &
        edges['target'].astype(str).isin(valid_nodes)
    ]

    # Cleans data to remove numpy values, JSON does not support them
    community = df.replace({np.nan: None}).astype(object).to_dict(orient="records")
    comm_edges = ed_df.replace({np.nan: None}).astype(object).to_dict(orient="records")

    return {
        "status": "success",
        "nodes": community,
        "edges": comm_edges,
    }

# GET metrics for {comm_id} community
@router.get('/metrics/{comm_id}')
def get_metrics(comm_id):
    if nodes.empty or edges.empty:
        return {"status": "missing data", "message": "data upload required"}

    # Select local data from node CSV
    df = nodes[['node', 'community', 'local_zscore', 'local_P', 'local_role']]
    # Get nodes with comm_id
    metrics = df.loc[nodes['community'] == comm_id]

    # Round long values to 5 decimal places
    cols_to_round = ['local_zscore', 'local_P']
    metrics[cols_to_round] = metrics[cols_to_round].round(5)

    # Cleans data to remove numpy values, JSON does not support them
    metrics = metrics.replace({np.nan: None}).astype(object).to_dict(orient="records")

    return {
        "status": "success",
        "nodes": metrics
    }

