import networkx as nx
import numpy as np
import json

def compute_community_stats(G, comms):
    community_stats = {}

    for cid, nodes in comms.items():
        sub = G.subgraph(nodes)

        community_stats[cid] = {}

        community_stats[cid]['num_nodes'] = sub.number_of_nodes()
        community_stats[cid]['num_edges'] = sub.number_of_edges()
        community_stats[cid]['density'] = nx.density(sub)
        community_stats[cid]['diameter'] = nx.diameter(sub)

        degrees = dict(sub.degree)
        deg_ls = list(degrees.values())
        community_stats[cid]['avg_deg'] = np.mean(deg_ls)

    with open('../../data/processed/community_stats.json', 'w') as file:
        json.dump(community_stats, file, indent=2)

    return


