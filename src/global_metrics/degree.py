import networkx as nx

# For an undirected graph
def compute_degree(G):
    # Computes degree centrality

    # Calculates the number of connections(edges) each node has
    # Returns normalised values in a dictionary for each node
    metric = nx.degree_centrality(G)

    # Return dictionary {node: normalised_degree_value}
    return metric