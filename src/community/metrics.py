import networkx as nx
from collections import defaultdict

def compute_intra_inter_degree(G, community_map):
    intra_deg = defaultdict(lambda: defaultdict(int))
    inter_deg = defaultdict(lambda: defaultdict(int))

    for u, v in G.edges():
        cu, cv = community_map[u], community_map[v]

        if cu == cv:
            intra_deg[cu][u] += 1
            intra_deg[cv][v] += 1
        else:
            inter_deg[cu][u] += 1
            inter_deg[cv][v] += 1

    sorted_intra = {
        comm_id: dict(sorted(nodes.items(), key=lambda item: item[1], reverse=True))
        for comm_id, nodes in intra_deg.items()
    }
    sorted_inter = {
        comm_id: dict(sorted(nodes.items(), key=lambda item: item[1], reverse=True))
        for comm_id, nodes in inter_deg.items()
    }

    return sorted_intra, sorted_inter

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