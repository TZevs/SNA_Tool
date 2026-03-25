def compute_local_thresholds(df):
    percentiles = [0.25, 0.50, 0.75, 0.90]

    local_df = df[['intra', 'inter', 'local_closeness', 'local_core_num', 'betweenness']]

    local_thresholds = local_df.groupby('community').quantile(percentiles, interpolation='nearest').unstack()

    return local_thresholds


def compute_global_thresholds(df):
    percentiles = [0.25, 0.50, 0.75, 0.90]

    global_df = df[['degree', 'global_closeness', 'global_core_num', 'betweenness', 'eigenvector', 'trussness']]

    global_thresholds = global_df.quantile(percentiles, interpolation='nearest')

    return global_thresholds