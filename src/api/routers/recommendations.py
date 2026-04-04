from fastapi import APIRouter
from src.utils.file_loader import load_csv

router = APIRouter(prefix="/recommendations")

local_rec_df = load_csv("local_recs.csv")
global_rec_df = load_csv("global_recs.csv")

@router.get("/local")
def get_local_recs():
    if local_rec_df.empty:
        return {"status": "missing data", "message": "data upload required"}
    return {
        "status": "success",
        "recs": local_rec_df.to_dict(orient="records")
    }

# @router.get("/local/{comm_id}")
# def get_community_recs(comm_id):
#     df = local_rec_df.loc[local_rec_df['community'] == comm_id]
#     return convert_types(df).to_dict(orient="records")

@router.get("/global")
def get_global_recs():
    if global_rec_df.empty:
        return {"status": "missing data", "message": "data upload required"}
    return {
        "status": "success",
        "recs": global_rec_df.to_dict(orient="records")
    }
