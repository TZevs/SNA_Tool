import pandas as pd

# Flattening the dict to have a role and node per row, instead of a list.
# Needed for grouping later
def flatten_df_helper(role_dict, col):
    rows = [
        {'node': node, col: role}
        for node, role_list in role_dict.items()
        for role in role_list
    ]
    return pd.DataFrame.from_dict(rows)

def assign_global_roles(df, thresholds):
    roles = {node: [] for node in df['node']}

    for row in df.itertuples():
       # Identifying global hubs using the global threshold boundaries
        if (
            row.degree >= thresholds.loc[0.90, 'degree'] and
            row.global_closeness >= thresholds.loc[0.90, 'global_closeness'] and
            row.global_core_num >= thresholds.loc[0.75, 'global_core_num']
        ):
            roles[row.node].append('global_hub')

        # Identifying global brokers using the global thresholds boundaries
        if (
            row.betweenness >= thresholds.loc[0.90, 'betweenness'] and
            row.global_closeness >= thresholds.loc[0.90, 'global_closeness']
        ):
            roles[row.node].append('global_bridge')

        # Identifying core nodes within the network using the global thresholds.
        if (
            row.global_core_num >= thresholds.loc[0.90, 'global_core_num'] and
            row.trussness >= thresholds.loc[0.75, 'trussness']
        ):
            roles[row.node].append('global_core_node')

    return flatten_df_helper(roles, 'global_role')


def assign_local_roles(df, thresholds):
    roles = {node: [] for node in df['node']}

    communities = df.groupby('community')

    for community, comm in communities:
        comm_thresh = thresholds.loc[community]

        for row in comm.itertuples():
            # Identifying local hubs using the computed thresholds for this community
            if (
                row.intra >= comm_thresh[('intra', 0.90)] and
                row.local_closeness >= comm_thresh[('local_closeness', 0.50)] and
                row.local_core_num >= comm_thresh[('local_core_num', 0.50)]
            ):
                roles[row.node].append('local_hub')

            # Identifying local bridges using the computed thresholds for this community
            if (
                 row.inter >= comm_thresh[('inter', 0.90)] and
                 row.intra <= comm_thresh[('intra', 0.25)] and
                 row.betweenness >= comm_thresh[('betweenness', 0.75)]
            ):
                roles[row.node].append('local_bridge')

            # Identifying local leaders using the computed thresholds for this community
            if (
                row.local_closeness >= comm_thresh[('local_closeness', 0.90)] and
                row.local_core_num >= comm_thresh[('local_core_num', 0.50)] and
                row.intra >= comm_thresh[('intra', 0.50)]
            ):
                roles[row.node].append('local_leader')

    return flatten_df_helper(roles, 'local_role')
