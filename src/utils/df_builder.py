import pandas as pd

def build_metrics_df(G, node_comms, bet, close, deg, eigen, core, truss, zscore, part_eff):
    # Store Series: row = node, columns = metrics
    rows = []

    # Iterate through nodes in the graph
    for n in G.nodes():
        # Get comm_id of the community the node is in
        cid = node_comms[n]

        # Append node row
        rows.append({
            'node': n,
            'community': cid,
            'degree': deg[n],
            'global_closeness': close[n],
            'global_core_num': core[n],
            'betweenness': bet[n],
            'eigenvector': eigen[n],
            'trussness': truss[n],
            'local_zscore': zscore[n],
            'local_P': part_eff[n]
        })

    # Return combined Series as a DF
    return pd.DataFrame(rows)