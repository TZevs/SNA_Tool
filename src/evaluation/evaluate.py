import pandas as pd
from scipy.stats import kendalltau, spearmanr

def evaluate_rank_correlations(df):
    # Evaluate rank correlations between all centrality metrics

    # Remove the non-metric columns
    remove = ["node", "community", "global_role", "local_role"]
    metrics = [m for m in df.columns if m not in remove]

    # Store (kendall & Spearman) correlation values for each metric pair
    results = []

    # Loop through all unique metric pairs
    for i, col_a in enumerate(metrics):
        for col_b in metrics[i+1:]:
            # Extract 2 metrics to compare
            x = df[col_a]
            y = df[col_b]

            # Compute Kendall(tau): measures ordinal association based on concordant/discordant pairs
            tau, _ = kendalltau(x, y)

            # Compute Spearman(rho): measures monotonic relationships between ranked values
            rho, _ = spearmanr(x, y)

            # Append results for this metric pair
            results.append({
                "metric_a": col_a,
                "metric_b": col_b,
                "kendall_tau": tau,
                "spearman_rho": rho
            })

    # Return df with all metric pair correlation results
    return pd.DataFrame(results)