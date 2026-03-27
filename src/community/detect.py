import networkx as nx

def detect_communities(G):
    # Create copy of graph, so that changes are not made to the original
    H = G.copy()

    #

    # Returns a single list of node sets, 1 per community
    coms_list = nx.community.louvain_communities(H)

    # partition_mod = nx.community.modularity(coms_list)

    node_coms = {}
    for index, com in enumerate(coms_list):
        for n in com:
            node_coms[n] = f'c{index}'

    # Dictionary to store the communities and their metrics
    coms_dict = {}
    # Iterate through the list, use enumerate to get the set index's
    for index, com in enumerate(coms_list):
        # Assign an ID as a key to each community
        coms_dict[f'c{index}'] = list(com)

    return node_coms, coms_dict