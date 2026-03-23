import pandas as pd
import networkx as nx

def build_metrics_df(G, community_map, intra, inter, closeness, core):
    rows = []

    for n in G.nodes():
        cid = community_map[n]

        rows.append({
            'node': n,
            'community': cid,
            'intra': intra[cid].get(n, 0),
            'inter': inter[cid].get(n, 0),
            'closeness': closeness[cid].get(n, 0),
            'core_num': core[cid].get(n, 0)
        })

    return pd.DataFrame(rows)