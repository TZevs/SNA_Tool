import networkx as nx

# For an undirected graph
def undir_degree(G):
    # Computes degree centrality
    #   - calculates the number of connections each node has.
    #   - Returns a normalised value in the dictionary with the node id as key
    raw_metrics = nx.degree_centrality(G)

    # Sort the metrics dictionary by value into descending order
    sorted_dict = sorted(raw_metrics.items(), key=lambda d: d[1], reverse=True)

    # Return to be used in the ranking module
    return sorted_dict