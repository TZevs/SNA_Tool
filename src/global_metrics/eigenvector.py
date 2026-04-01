import networkx as nx

def compute_eigenvector(G):
    # Compute Eigenvector centrality

    # Calculate a score by summing the scores of a nodes' neighbours
    # Returns normalised values in a dictionary for each node
    raw_metrics = nx.eigenvector_centrality(G)

    # Sort the dictionary by value into descending order
    sorted_dict = sorted(raw_metrics.items(), key=lambda d: d[1], reverse=True)

    # Return dictionary {node: normalised_eigenvector_value}
    return dict(sorted_dict)