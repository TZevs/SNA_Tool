import networkx as nx

def undir_degree(G):
    # Compute the degree centrality for the network nodes
    # Returns a dictionary of {nodeId : centrality_score(normalised)}
    deg_dict = nx.degree_centrality(G)

    # Sort the dictionary by value into descending order
    sorted_dict = sorted(deg_dict.items(), key=lambda d: d[1], reverse=True)

    # Return to be used in the ranking module
    return sorted_dict