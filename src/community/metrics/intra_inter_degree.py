from collections import defaultdict

def compute_intra_inter_degree(G, node_comms):
    intra = defaultdict(lambda: defaultdict(int))
    inter = defaultdict(lambda: defaultdict(int))

    for u, v in G.edges():
        cu, cv = node_comms[u], node_comms[v]

        if cu == cv:
            intra[cu][u] += 1
            intra[cv][v] += 1
        else:
            inter[cu][u] += 1
            inter[cv][v] += 1

    return intra, inter