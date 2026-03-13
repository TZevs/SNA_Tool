import networkx as nx

def undir_degree(G):
    # Computes degree centrality
    # - calculates the fraction of nodes connected to a node.
    # Returns a dictionary of {nodeId : centrality_score(normalised(degree/n-1))}
    raw_metrics = nx.degree_centrality(G)

    # Sort the dictionary by value into descending order
    sorted_dict = sorted(raw_metrics.items(), key=lambda d: d[1], reverse=True)

    # Return to be used in the ranking module
    return sorted_dict