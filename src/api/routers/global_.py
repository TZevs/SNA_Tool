from fastapi import APIRouter
from src.utils.file_loader import load_csv
import numpy as np
import json

# Global Data API
router = APIRouter(prefix="/global")

# Use helper to load CSV's, in persistent storage outputted by the analysis pipeline, as DFs
node_metrics = load_csv('node_data.csv')
recs = load_csv('global_recs.csv')

# GET all global metrics
@router.get('/metrics')
def get_metrics():
    if node_metrics.empty:
        return {"status": "missing data", "message": "data upload required"}

    # Select all but the local metrics and roles
    metrics_df = node_metrics[['node', 'degree', 'community', 'global_closeness', 'global_core_num', 'betweenness', 'eigenvector', 'trussness', 'global_role']]
    # Cleans data to remove numpy values, JSON does not support them
    metrics = metrics_df.replace({np.nan: None}).astype(object).to_dict(orient="records")

    return {
        "status": "success",
        "nodes": metrics
    }

# GET recommendations for global roles
@router.get("/recs")
def get_global_recs():
    if recs.empty:
        return {"status": "missing data", "message": "data upload required"}
    return {
        "status": "success",
        "recs": recs.to_dict(orient="records")
    }

# GET statistics for the network
@router.get("/stats")
def get_global_stats():
    # Read statistics from global_stats JSON in persistent storage
    with open("../../data/processed/global_stats.json", "r") as jsonfile:
        stats = json.load(jsonfile)

    return {
        "status": "success",
        "stats": stats,
    }