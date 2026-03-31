import numpy as np

def compute_local_zscore(G, comms_dict):
    local_zscore = {}

    for cid, nodes in comms_dict.items():
        S = G.subgraph(nodes)

        intra = S.degree()
        mean = np.mean(list(intra))
        std = np.std(list(intra))

        for n in nodes:
            if std > 0:
                local_zscore[n] = (intra[n] - mean) / std
            else:
                local_zscore[n] = 0.0

    return local_zscore