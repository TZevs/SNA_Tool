import networkx as nx

# For an undirected graph
def undir_closeness(G):
    # Compute closeness centrality
    #   - calculates the average distance a node has with all other nodes in the graph.
    #   - Returns a normalised value in the dictionary with the node id as key
    raw_metrics = nx.closeness_centrality(G)

    # Sort the metrics dictionary by value into descending order
    sorted_dict = sorted(raw_metrics.items(), key=lambda d: d[1], reverse=True)

    # Return to be used in the ranking module
    return sorted_dict