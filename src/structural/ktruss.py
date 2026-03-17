import networkx as nx

def undir_ktruss(G):
    # Compute k-core decomposition
    #   -
    #   - Returns a k-truss subgraph
    raw_subgraphs = nx.k_truss(G)
