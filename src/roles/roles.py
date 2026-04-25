import pandas as pd

def assign_global_roles(df, thresholds):
    # Assign global structural roles to nodes based percentile thresholds of global metrics
    global_roles = {}

    # Iterate through df rows
    for row in df.itertuples():

       # Global Hub: high degree + high eigenvector (top 10% for both) -> globally influential nodes
        if (row.degree >= thresholds.loc[0.90, 'degree'] and
            row.eigenvector >= thresholds.loc[0.90, 'eigenvector']
        ):
            global_roles[row.node] ='Global Hub'
            continue

        # Global Broker: high betweenness + low cohesion metrics -> cross-community bridge (bottleneck)
        if (row.betweenness >= thresholds.loc[0.90, 'betweenness'] and
            row.global_closeness <= thresholds.loc[0.50, 'global_closeness'] and
            row.eigenvector <= thresholds.loc[0.50, 'eigenvector'] and
            row.degree <= thresholds.loc[0.50, 'degree']
        ):
            global_roles[row.node] = 'Global Broker'
            continue

        # Global Core: high k-core + high trussness (top 10% for both) -> structurally central
        if (row.global_core_num >= thresholds.loc[0.90, 'global_core_num'] and
            row.trussness >= thresholds.loc[0.90, 'trussness']
        ):
            global_roles[row.node] = 'Global Core'
            continue

        # Global Spreader: high-mid k-core + medium eigenvector + medium degree -> ideal information diffusion targets
        if (thresholds.loc[0.90, 'global_core_num'] >= row.global_core_num >= thresholds.loc[0.75, 'global_core_num'] and
            thresholds.loc[0.75, 'eigenvector'] >= row.eigenvector >= thresholds.loc[0.25, 'eigenvector'] and
            thresholds.loc[0.75, 'degree'] >= row.degree >= thresholds.loc[0.50, 'degree']
        ):
            global_roles[row.node] = 'Global Spreader'
            continue

        # Global Peripheral: low k-core (bottom 25%) -> nodes on the structural outskirts
        if row.global_core_num <= thresholds.loc[0.25, 'global_core_num']:
            global_roles[row.node] = 'Global Peripheral'
            continue

    # Convert role assignments to df; row=node, column=global_role
    df = pd.DataFrame(
        {'node': node,'global_role': role}
        for node, role in global_roles.items()
    )
    return df


def assign_local_roles(df, thresholds):
    # Assign local (within-community) roles using z-score and participation coefficient thresholds
    local_roles = {}

    # Assign roles per community
    communities = df.groupby('community')

    # Iterate through communities
    for community, comm in communities:
        # Iterate through rows in the community
        for row in comm.itertuples():
            # Get node participation coefficient value
            P = row.local_P
            z = row.local_zscore

            # Local Hubs: high zscore (z > 2.5)
            if z >= thresholds['z_hub']:

                # Provincial Hub: edges mostly stay inside the community
                if P <= thresholds['p_provincial_max']:
                    local_roles[row.node] = 'Local Provincial Hub'
                    continue

                # Connector Hub: edges spread across several communities
                elif P <= thresholds['p_connector_hub_max']:
                    local_roles[row.node] = 'Local Connector Hub'
                    continue

                # Kinless Hub: edges distributed almost equally across communities
                else:
                    local_roles[row.node] = 'Local Kinless Hub'
                    continue

            # Non-Hubs: low zscore (z < 2.5)
            elif z < thresholds['z_hub']:

                # Ultra‑Peripheral: almost all edges stay inside the community
                if P <= thresholds['p_ultra_max']:
                    local_roles[row.node] = 'Local Ultra-Peripheral'
                    continue

                # Peripheral: mostly internal edges, but some external
                elif P <= thresholds['p_peripheral_max']:
                    local_roles[row.node] = 'Local Peripheral'
                    continue

                # Connector: edges spread across multiple communities
                elif P <= thresholds['p_connector_max']:
                    local_roles[row.node] = 'Local Connector'
                    continue

                # Kinless: edges distributed widely across communities
                else:
                    local_roles[row.node] = 'Local Kinless'
                    continue

    # Convert role assignments to df; row=node, column=local_role
    df = pd.DataFrame(
        {'node': node, 'local_role': role}
        for node, role in local_roles.items()
    )
    return df
