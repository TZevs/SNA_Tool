import networkx as nx
from collections import defaultdict

def compute_intra_inter_degree(G, community_map):
    intra = defaultdict(lambda: defaultdict(int))
    inter = defaultdict(lambda: defaultdict(int))

    for u, v in G.edges():
        cu, cv = community_map[u], community_map[v]

        if cu == cv:
            intra[cu][u] += 1
            intra[cv][v] += 1
        else:
            inter[cu][u] += 1
            inter[cv][v] += 1

    return intra, inter

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

def compute_community_closeness(G, coms_dict):
    community_closeness = {}

    for cid, nodes in coms_dict.items():
        subgraph = G.subgraph(nodes)
        community_closeness[cid] = nx.closeness_centrality(subgraph)

    return community_closeness

def compute_community_kcore(G, coms_dict):
    community_node_kcore = {}

    for cid, nodes in coms_dict.items():
        sub = G.subgraph(nodes)
        community_node_kcore[cid] = nx.core_number(sub)

    return community_node_kcore