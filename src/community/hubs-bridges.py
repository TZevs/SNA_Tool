import networkx as nx
from collections import defaultdict
import math

def identify_community_hubs(intra_deg, community_kcore, community_size):
    community_hubs = defaultdict(list)

    top_10_pc_intra_deg = {}
    top_10_pc_kcore = {}

    for cid, nodes in intra_deg.items():
        node_ls = list(nodes)
        size = community_size[cid]

        top_count = math.ceil(size * 0.10)
        top_nodes = node_ls[:top_count]

        top_10_pc_intra_deg[cid] = top_nodes

    for cid, nodes in community_kcore.items():
        node_ls = list(nodes)
        size = community_size[cid]

        top_count = math.ceil(size * 0.10)
        top_nodes = node_ls[:top_count]

        top_10_pc_kcore[cid] = top_nodes

    for cid, nodes in top_10_pc_intra_deg.items():
        for n in list(nodes):
            if top_10_pc_kcore[cid].contains(n):
                community_hubs[cid].append(n)

    return community_hubs

def identify_community_bridges(intra_deg, inter_deg, betweenness):


    return

def identify_community_leaders():

    return
