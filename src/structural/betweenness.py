import networkx as nx

def undir_betweenness(G):
    # Compute betweenness centrality
    #   - node v is the sum of the fraction of all-pairs shortest paths that pass through v.
    raw_metrics = nx.betweenness_centrality(G)