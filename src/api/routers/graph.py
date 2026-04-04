from fastapi import APIRouter
from src.utils.file_loader import load_csv

router = APIRouter(prefix="/graph")

edge_df = load_csv("edge_data.csv")

@router.get("/edges")
def get_edges():
    if edge_df.empty:
        return {"status": "missing data", "message": "data upload required"}
    return {
        "status": "success",
        "recs": edge_df.to_dict(orient="records")
    }
