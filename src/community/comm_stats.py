import networkx as nx

def compute_density(G, coms_dict):
    community_density = {}

    for cid, nodes in coms_dict.items():
        sub = G.subgraph(nodes)
        community_density[cid] = nx.density(sub)

    return community_density

def compute_sizes(coms_dict):
    community_sizes = {}

    for cid, com in coms_dict.items():
        community_sizes[cid] = len(com)

    return community_sizes