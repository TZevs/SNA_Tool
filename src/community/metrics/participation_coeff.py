from collections import defaultdict

def compute_participation_coefficient(G, node_comms):
    local_part = {}

    for node in G.nodes():
        deg = G.degree(node)
        if deg == 0:
            local_part[node] = 0
            continue

        edge_to_comm_count = defaultdict(int)
        for ngb in G.neighbors(node):
            edge_to_comm_count[node_comms[ngb]] += 1

        sum_sq = sum((k / deg) ** 2 for k in edge_to_comm_count.values())
        local_part[node] = 1 - sum_sq

    return local_part
