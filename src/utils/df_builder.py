import pandas as pd

def build_metrics_df(G, node_comms, l_close, l_core, bet, close, deg, eigen, core, truss, zscore, part_eff):
    rows = []

    for n in G.nodes():
        cid = node_comms[n]

        rows.append({
            'node': n,
            'community': cid,
            'degree': deg[n],
            'local_closeness': l_close[cid].get(n, 0),
            'global_closeness': close[n],
            'local_core_num': l_core[cid].get(n, 0),
            'global_core_num': core[n],
            'betweenness': bet[n],
            'eigenvector': eigen[n],
            'trussness': truss[n],
            'local_zscore': zscore[n],
            'local_P': part_eff[n]
        })

    return pd.DataFrame(rows)