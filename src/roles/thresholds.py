import pandas as pd

def get_local_thresholds():
    local_thresholds = {
        'z_hub': 2.50,
        'p_ultra_max': 0.05,
        'p_peripheral_max': 0.62,
        'p_connector_max': 0.80,
        'p_provincial_max': 0.30,
        'p_connector_hub_max': 0.75,
    }
    return local_thresholds


def compute_global_thresholds(df):
    if len(df.index) == 0:
        return pd.DataFrame()

    percentiles = [0.25, 0.50, 0.75, 0.90]

    global_df = df[['degree', 'global_closeness', 'global_core_num', 'betweenness', 'eigenvector', 'trussness']]

    global_thresholds = global_df.quantile(percentiles, interpolation='nearest')

    return global_thresholds