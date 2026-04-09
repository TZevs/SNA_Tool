import networkx as nx
import numpy as np
import json

def compute_global_stats(G, mod):
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    density = nx.density(G)
    diameter = nx.diameter(G)

    degrees = dict(G.degree)
    deg_ls = list(degrees.values())
    avg_degree = np.mean(deg_ls)

    data = {
        "num_nodes": num_nodes,
        "num_edges": num_edges,
        "density": density,
        "modularity": mod,
        "avg_deg": avg_degree,
        "diameter": diameter,
    }

    with open('../../data/processed/global_stats.json', 'w') as file:
        json.dump(data, file, indent=2)

    return