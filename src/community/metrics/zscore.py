import numpy as np

def compute_local_zscore(G, comms_dict):
    # Compute within-community degree z-score for each node
    '''
    Formula from literature (Guimerà & Nunes Amaral, 2005):
        Z_i = (K_i - K_s_i) / std(K_s_i)
        where:
            K_i = node i degree within community
            K_s_i = average community degree

    Translated for code:
        - Compute node i degree (K_i)
        - Compute average community degree (K_s_i)
        - Compute standard deviation of community degree
        Z = (intra_degree - avg_intra_degree) / std(intra_degrees)
    '''

    # Store values
    local_zscore = {}

    # Iterate through communities
    for cid, nodes in comms_dict.items():
        # Create subgraph for the community
        sub = G.subgraph(nodes)

        # Compute intra-community degrees (K_i) for all nodes in sub
        intra = sub.degree()
        # Calculate average(mean) of intra degrees
        mean = np.mean(list(intra))
        # Calculate the standard deviation of the intra degrees
        std = np.std(list(intra))

        # Apply z-score formula to each node
        for n in nodes:
            if std > 0:
                local_zscore[n] = (intra[n] - mean) / std
            else:
                # If std = 0, set node zscore to 0 -> Z_i = 0
                local_zscore[n] = 0.0

    # Return dictionary {node: zscore}
    return local_zscore