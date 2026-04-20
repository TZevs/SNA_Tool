import pandas as pd

def assign_global_roles(df, thresholds):
    global_roles = {node: [] for node in df['node']}

    for row in df.itertuples():
       # Identifying global_metrics hubs using the global_metrics threshold boundaries
        if (row.degree >= thresholds.loc[0.90, 'degree'] and
            row.eigenvector >= thresholds.loc[0.90, 'eigenvector']
        ):
            global_roles[row.node].append('Global Hub')

        # Identifying global_metrics brokers using the global_metrics thresholds boundaries
        if (row.betweenness >= thresholds.loc[0.90, 'betweenness'] and
            row.global_closeness <= thresholds.loc[0.50, 'global_closeness'] and
            row.eigenvector <= thresholds.loc[0.50, 'eigenvector'] and
            row.degree <= thresholds.loc[0.50, 'degree']
        ):
            global_roles[row.node].append('Global Broker')

        # Identifying core nodes within the network using the global_metrics thresholds.
        if (row.global_core_num >= thresholds.loc[0.90, 'global_core_num'] and
            row.trussness >= thresholds.loc[0.90, 'trussness']
        ):
            global_roles[row.node].append('Global Core')

        if (thresholds.loc[0.90, 'global_core_num'] >= row.global_core_num >= thresholds.loc[0.75, 'global_core_num'] and
            thresholds.loc[0.75, 'eigenvector'] >= row.eigenvector >= thresholds.loc[0.25, 'eigenvector'] and
            thresholds.loc[0.75, 'degree'] >= row.degree >= thresholds.loc[0.50, 'degree']):
            global_roles[row.node].append('Global Spreader')

        if row.global_core_num <= thresholds.loc[0.25, 'global_core_num']:
            global_roles[row.node].append('Global Peripheral')

    df = pd.DataFrame(
        {'node': node,'global_role': role}
        for node, roles in global_roles.items()
        for role in roles
    )
    return df


def assign_local_roles(df, thresholds, node_comms):
    local_roles = {node: [] for node in df['node']}

    communities = df.groupby('community')

    for community, comm in communities:
        for row in comm.itertuples():
            P = row.local_P
            if row.local_zscore >= thresholds['z_hub']:
                if P <= thresholds['p_provincial_max']:
                    local_roles[row.node].append('Local Provincial Hub')
                elif P <= thresholds['p_connector_hub_max']:
                    local_roles[row.node].append('Local Connector Hub')
                else:
                    local_roles[row.node].append('Local Kinless Hub')
            elif row.local_zscore < thresholds['z_hub']:
                if P <= thresholds['p_ultra_max']:
                    local_roles[row.node].append('Local Ultra-Peripheral')
                elif P <= thresholds['p_peripheral_max']:
                    local_roles[row.node].append('Local Peripheral')
                elif P <= thresholds['p_connector_max']:
                    local_roles[row.node].append('Local Connector')
                else:
                    local_roles[row.node].append('Local Kinless')

    df = pd.DataFrame(
        {'node': node, 'community': node_comms[node], 'local_role': role}
        for node, roles in local_roles.items()
        for role in roles
    )
    return df
