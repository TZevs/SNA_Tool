from collections import defaultdict

def compute_participation_coefficient(G, node_comms):
    # Compute participation coefficient for each node
    '''
    Formula from literature (Guimerà & Nunes Amaral, 2005):
        P_i = 1 - Σ_c (K_ic / K_i)^2
        where:
            K_ic = number of edges from node i to community c
            K_i = total degree of node i

    Translated for code:
        - Count edges from node i to each community (K_ic)
        - Compute total degree of node i (K_i)
        - Compute (K_ic / K_i) for all communities
        P = 1 - sum(K_ic / K_i)**2
    '''

    # Store values
    local_part = {}

    # Iterate through nodes in the graph
    for node in G.nodes():
        # Compute node degree
        deg = G.degree(node)

        # If node has no edges, P = 0
        if deg == 0:
            local_part[node] = 0
            continue

        # Count how many edges node i has to each community c
        # Store {comm_id: count}
        edge_to_comm_count = defaultdict(int)
        for ngb in G.neighbors(node):
            # Add to count key=(comm_id of the connected node)
            edge_to_comm_count[node_comms[ngb]] += 1

        # Apply the participation coefficient formula to each node
        sum_sq = sum((k / deg) ** 2 for k in edge_to_comm_count.values())
        local_part[node] = 1 - sum_sq

    # Return dictionary {node: participation_coefficient}
    return local_part
