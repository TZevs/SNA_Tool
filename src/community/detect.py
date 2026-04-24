import networkx as nx

def detect_communities(G):
    # Detect communities using the Louvain algorithm

    # Returns a list of node sets, each set represents 1 community
    comms_list = nx.community.louvain_communities(G)

    # Compute the modularity score for the community partitions
    mod = nx.community.modularity(G, comms_list)

    # Store community ID per node {node: comm_id}
    node_comms = {}
    for index, com in enumerate(comms_list):
        for n in com:
            # Set community ID per node
            node_comms[n] = f'c{index}'

    # Store community sets as dictionary
    comms = {}
    # Iterate through the list, use enumerate to get the set index's
    for index, comm in enumerate(comms_list):
        # Assign an ID as a key for each community
        comms[f'c{index}'] = list(comm)

    # Return {node: comm_id}, {comm_id: list(nodes)}, modularity score
    return node_comms, comms, mod