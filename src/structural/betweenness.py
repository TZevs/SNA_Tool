import networkx as nx

# For an undirected graph
def undir_betweenness(G):
    # Compute betweenness centrality
    #   - calculates the number of times a node is used as a bridge on the shortest path between nodes.
    #   - Returns a normalised value in the dictionary with the node id as key
    raw_metrics = nx.betweenness_centrality(G)

    # Sort the metrics dictionary by value into descending order
    sorted_dict = sorted(raw_metrics.items(), key=lambda d: d[1], reverse=True)

    # Return to be used in the ranking module
    return sorted_dict