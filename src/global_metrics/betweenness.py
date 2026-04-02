import networkx as nx

def compute_betweenness(G):
    # Compute betweenness centrality

    # Calculate the number of times a node is used as a bridge on the shortest path between nodes.
    # Return normalised values in a dictionary for each node
    metric = nx.betweenness_centrality(G, k=100, seed=42, normalized=True)

    # Return dictionary {node: normalised_betweenness_value}
    return metric