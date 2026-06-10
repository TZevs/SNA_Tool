import networkx as nx

def compute_eigenvector(G):
    # Compute Eigenvector centrality

    # Calculate a score by summing the scores of a nodes' neighbours
    # Returns normalised values in a dictionary for each node
    metric = nx.eigenvector_centrality(G)

    # Return dictionary {node: normalised_eigenvector_value}
    return metric