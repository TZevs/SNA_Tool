import pandas as pd

def build_metrics_df(G, community_map, intra, inter, local_closeness, core, betweenness, global_closeness, degree, eigen, kcore, ktruss):
    rows = []

    for n in G.nodes():
        cid = community_map[n]

        rows.append({
            'node': n,
            'community': cid,
            'degree': degree[n],
            'intra': intra[cid].get(n, 0),
            'inter': inter[cid].get(n, 0),
            'local_closeness': local_closeness[cid].get(n, 0),
            'global_closeness': global_closeness[n],
            'local_core_num': core[cid].get(n, 0),
            'global_core_num': kcore[n],
            'betweenness': betweenness[n],
            'eigenvector': eigen[n],
            'trussness': ktruss[n]
        })

    return pd.DataFrame(rows)