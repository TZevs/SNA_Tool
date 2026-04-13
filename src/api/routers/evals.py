from fastapi import APIRouter
import pandas as pd

router = APIRouter()

@router.get('/evals')
def get_evals():
    eval_df = pd.read_csv('../../data/processed/rank_corr_eval.csv')

    return {
        "status": "success",
        "evals": eval_df.to_dict(orient='records'),
    }