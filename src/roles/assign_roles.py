import pandas as pd

def assign_global_roles(df, thresholds):
    keys = df['node']
    roles = {key: [] for key in keys}

    for row in df.itertuples():
        if row.degree >= thresholds.loc['degree', 0.90]:
            roles[row.node].append('hub')

    return pd.DataFrame(roles)


def assign_local_roles(df, thresholds):
    keys = df['node']
    roles = {key: [] for key in keys}

    communities = df.groupby('community')

    for name, comm in communities:
        comm_thresh = thresholds.loc[name]
        for row in comm.itertuples():
            # Identifying local hubs using the computed thresholds for this community
            if (row.intra >= comm_thresh[('intra', 0.90)] and row.local_closeness >= comm_thresh[('local_closeness', 0.50)]
                    and row.local_core_num >= comm_thresh[('local_core_num', 0.50)]):
                roles[row.node].append('hub')

            # Identifying local bridges using the computed thresholds for this community
            if ((row.inter >= comm_thresh[('inter', 0.90)] or row.inter >= comm_thresh[('inter', 0.75)])
                    and (row.intra <= comm_thresh[('intra', 0.25)] or row.intra <= comm_thresh[('intra', 0.50)])
                    and row.betweenness >= comm_thresh[('betweenness', 0.75)]):
                roles[row.node].append('bridge')

            # Identifying local leaders using the computed thresholds for this community
            if (row.local_closeness >= comm_thresh[('local_closeness', 0.90)] and row.local_core_num >= comm_thresh[('local_core_num', 0.50)]
                    and row.intra >= comm_thresh[('intra', 0.50)]):
                roles[row.node].append('leader')

    return pd.DataFrame(roles)