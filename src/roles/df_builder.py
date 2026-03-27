import pandas as pd

def build_metrics_df(G, node_comms, intra, inter, l_close, l_core, bet, close, deg, eigen, core, truss):
    rows = []

    for n in G.nodes():
        cid = node_comms[n]

        rows.append({
            'node': n,
            'community': cid,
            'degree': deg[n],
            'intra': intra[cid].get(n, 0),
            'inter': inter[cid].get(n, 0),
            'local_closeness': l_close[cid].get(n, 0),
            'global_closeness': close[n],
            'local_core_num': l_core[cid].get(n, 0),
            'global_core_num': core[n],
            'betweenness': bet[n],
            'eigenvector': eigen[n],
            'trussness': truss[n]
        })

    return pd.DataFrame(rows)