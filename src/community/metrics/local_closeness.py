import networkx as nx

def compute_community_closeness(G, coms_dict):
    community_closeness = {}

    for cid, nodes in coms_dict.items():
        subgraph = G.subgraph(nodes)
        community_closeness[cid] = nx.closeness_centrality(subgraph)

    return community_closeness