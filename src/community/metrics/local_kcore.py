import networkx as nx

def compute_community_kcore(G, coms_dict):
    community_node_kcore = {}

    for cid, nodes in coms_dict.items():
        sub = G.subgraph(nodes)
        community_node_kcore[cid] = nx.core_number(sub)

    return community_node_kcore