import networkx as nx

# For an undirected graph
def compute_degree(G):
    # Computes degree centrality

    # Calculates the number of connections(edges) each node has
    # Returns normalised values in a dictionary for each node
    raw_metrics = nx.degree_centrality(G)

    # Sort the metrics dictionary by value into descending order
    sorted_dict = sorted(raw_metrics.items(), key=lambda d: d[1], reverse=True)

    # Return dictionary {node: normalised_degree_value}
    return sorted_dict