from fastapi import APIRouter
from src.utils.file_loader import load_csv

router = APIRouter()

node_metrics = load_csv('node_data.csv')

@router.get('/nodes')
def get_metrics():
    if node_metrics.empty:
        return {"status": "missing data", "message": "data upload required"}
    return {
        "status": "success",
        "recs": node_metrics.to_dict(orient="records")
    }