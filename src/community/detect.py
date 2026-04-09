import networkx as nx

def detect_communities(G):
    # Create copy of graph, so that changes are not made to the original
    H = G.copy()

    # Returns a single list of node sets, 1 per community
    comms_list = nx.community.louvain_communities(H)

    mod = nx.community.modularity(G, comms_list)

    node_comms = {}
    for index, com in enumerate(comms_list):
        for n in com:
            node_comms[n] = f'c{index}'

    # Dictionary to store the communities and their metrics
    comms = {}
    # Iterate through the list, use enumerate to get the set index's
    for index, comm in enumerate(comms_list):
        # Assign an ID as a key to each community
        comms[f'c{index}'] = list(comm)

    return node_comms, comms, mod