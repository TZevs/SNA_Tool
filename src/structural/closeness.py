import networkx as nx

def undir_closeness(G):
    # Compute closeness centrality
    #   - of a node u is the
    raw_metrics = nx.closeness_centrality(G)