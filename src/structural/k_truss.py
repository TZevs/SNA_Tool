import networkx as nx

def undir_ktruss(G):
    # Compute k-core decomposition centrality
    #   -
    # Returns a k-truss subgraph
    raw_metrics = nx.k_truss(G)