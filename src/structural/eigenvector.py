import networkx as nx

def undir_eigenvector(G):
    # Compute Eigenvector centrality
    #   -
    raw_metrics = nx.eigenvector_centrality(G)