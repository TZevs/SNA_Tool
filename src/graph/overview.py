import networkx as nx
import numpy as np
import json

def compute_global_stats(G, mod):
    # Compute structural statistics for the entire network
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    density = nx.density(G)
    diameter = nx.approximation.diameter(G)

    # Compute within community degree (not z-score)
    degrees = dict(G.degree)
    # Convert DegreeView into a list
    deg_ls = list(degrees.values())
    # Calculate the mean degree for the community
    avg_degree = np.mean(deg_ls)

    # Store statistics
    data = {
        "num_nodes": num_nodes,
        "num_edges": num_edges,
        "density": density,
        "modularity": mod,
        "avg_deg": avg_degree,
        "diameter": diameter,
    }

    # Write stats to JSON file in persistent storage
    with open('../../data/processed/global_stats.json', 'w') as file:
        json.dump(data, file, indent=2)

    return