import pandas as pd

def get_local_thresholds():
    # Set fixed local thresholds based on literature (Guimerà & Nunes Amaral, 2005)
    local_thresholds = {
        # Non-Hub's (z < 2.5), Hub roles (z > 2.5)
        'z_hub': 2.50,
        'p_ultra_max': 0.05, # Ultra-Peripheral (P ≤ 0.05)
        # Peripheral (0.05 < P ≤ 0.62)
        'p_peripheral_max': 0.62,
        # Non-Hub Connectors (0.62 < P ≤ 0.80)
        'p_connector_max': 0.80, # Non-Hub Kinless (P > 0.80)
        'p_provincial_max': 0.30, # Provincial Hub (P ≤ 0.30)
        # Connector Hub (0.30 < P ≤ 0.75)
        'p_connector_hub_max': 0.75, # Kinless Hubs (P > 0.75)
    }
    # Return thresholds as a dict
    return local_thresholds

def compute_global_thresholds(df):
    # Compute thresholds for each global metric

    # If DF is empty, return an empty DF
    if len(df.index) == 0:
        return pd.DataFrame()

    # Percentile boundaries for thresholds (25%, 50%, 75%, 90%)
    percentiles = [0.25, 0.50, 0.75, 0.90]
    # Select only the global metrics relevant for thresholding
    global_df = df[['degree', 'global_closeness', 'global_core_num', 'betweenness', 'eigenvector', 'trussness']]

    # Compute percentile thresholds for each metric, returns the nearest value from the dataset
    global_thresholds = global_df.quantile(percentiles, interpolation='nearest')

    # Returns DF of rows = percentiles and columns = metrics
    return global_thresholds