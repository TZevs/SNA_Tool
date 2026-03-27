import networkx as nx

def compute_betweenness(G):
    # Compute betweenness centrality

    # Calculate the number of times a node is used as a bridge on the shortest path between nodes.
    # Return normalised values in a dictionary for each node
    raw_metrics = nx.betweenness_centrality(G)

    # Sort the metrics dictionary by value into descending order
    sorted_dict = sorted(raw_metrics.items(), key=lambda d: d[1], reverse=True)

    # Return dictionary {node: normalised_betweenness_value}
    return dict(sorted_dict)