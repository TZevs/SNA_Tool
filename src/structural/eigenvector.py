import networkx as nx

# For an undirected graph
def undir_eigenvector(G):
    # Compute Eigenvector centrality
    #   - calculates a score by summing the scores of a nodes' neighbours
    #   - Returns a normalised value in the dictionary with the node id as key
    raw_metrics = nx.eigenvector_centrality(G)

    # Sort the dictionary by value into descending order
    sorted_dict = sorted(raw_metrics.items(), key=lambda d: d[1], reverse=True)

    # Return to be used in the ranking module
    return sorted_dict