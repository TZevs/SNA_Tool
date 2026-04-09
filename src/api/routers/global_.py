from fastapi import APIRouter
from src.utils.file_loader import load_csv
import numpy as np
import json

router = APIRouter(prefix="/global")

node_metrics = load_csv('node_data.csv')
recs = load_csv('global_recs.csv')

@router.get('/metrics')
def get_metrics():
    if node_metrics.empty:
        return {"status": "missing data", "message": "data upload required"}

    metrics_df = node_metrics[['node', 'degree', 'global_closeness', 'global_core_num', 'betweenness', 'eigenvector', 'trussness', 'global_role']]
    metrics = metrics_df.replace({np.nan: None}).astype(object).to_dict(orient="records")

    return {
        "status": "success",
        "nodes": metrics
    }

@router.get("/recs")
def get_global_recs():
    if recs.empty:
        return {"status": "missing data", "message": "data upload required"}
    return {
        "status": "success",
        "recs": recs.to_dict(orient="records")
    }

@router.get("/stats")
def get_global_stats():
    with open("../../data/processed/global_stats.json", "r") as jsonfile:
        stats = json.load(jsonfile)

    return {
        "status": "success",
        "stats": stats,
    }