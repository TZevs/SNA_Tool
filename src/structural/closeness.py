import networkx as nx

def compute_closeness(G):
    # Compute closeness centrality

    # Calculate the average distance a node has with all other nodes in the graph
    # Return normalised values in a dictionary for each node
    raw_metrics = nx.closeness_centrality(G)

    # Sort the metrics dictionary by value into descending order
    sorted_dict = sorted(raw_metrics.items(), key=lambda d: d[1], reverse=True)

    # Return dictionary {node: normalised_closeness_value}
    return dict(sorted_dict)