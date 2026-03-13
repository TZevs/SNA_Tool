import networkx as nx

def undir_kcore(G):
    # Compute k-core decomposition centrality
    raw_metrics = nx.k_core(G)