import networkx as nx
import numpy as np
import json

def compute_community_stats(G, comms):
    # Compute structural statistics per community

    # Store statistics for all communities {comm_id: stats{}}
    community_stats = {}

    # Iterate through comms dictionary {comms_id: list(nodes)}
    for cid, nodes in comms.items():
        # Create subgraph of community nodes
        sub = G.subgraph(nodes)

        # Created nested dictionary
        community_stats[cid] = {}

        # Compute stats with NetworkX methods
        community_stats[cid]['num_nodes'] = sub.number_of_nodes()
        community_stats[cid]['num_edges'] = sub.number_of_edges()
        community_stats[cid]['density'] = nx.density(sub)
        community_stats[cid]['diameter'] = nx.diameter(sub)

        # Compute within community degree (not z-score)
        degrees = dict(sub.degree)
        # Convert DegreeView into a list
        deg_ls = list(degrees.values())
        # Calculate the mean degree for the community
        community_stats[cid]['avg_deg'] = np.mean(deg_ls)

    # Write stats to JSON file in persistent storage
    with open('../../data/processed/community_stats.json', 'w') as file:
        json.dump(community_stats, file, indent=2)

    return


