import pandas as pd
from scipy.stats import kendalltau, spearmanr

def evaluate_rank_correlations(csv_path='../../data/processed/node_data.csv'):
    df = pd.read_csv(csv_path)

    cols = list(df.columns)
    remove = ["node", "community", "global_role", "local_role"]
    metrics = [m for m in cols if m not in remove]

    results = []

    for i, col_a in enumerate(metrics):
        for col_b in metrics[i+1:]:
            x = df[col_a]
            y = df[col_b]

            tau, _ = kendalltau(x, y)
            rho, _ = spearmanr(x, y)

            results.append({
                "metric_a": col_a,
                "metric_b": col_b,
                "kendall_tau": tau,
                "spearman_rho": rho
            })

    return pd.DataFrame(results)