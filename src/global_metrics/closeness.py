import networkx as nx

def compute_closeness(G):
    # Compute closeness centrality

    # Calculate the average distance a node has with all other nodes in the graph
    # Return normalised values in a dictionary for each node
    metric = nx.closeness_centrality(G)

    # Return dictionary {node: normalised_closeness_value}
    return metric