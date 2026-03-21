import networkx as nx

def detect_communities(G):
    # Create copy of graph, so that changes are not made to the original
    H = G.copy()

    #

    # Returns a single list of node sets, 1 per community
    coms_list = nx.community.louvain_communities(H)

    # Compute the modularity of the partition
    mod = nx.community.modularity(G, coms_list)

    # Dictionary to store the communities in
    coms_dict = {}
    # Iterate through the list, use enumerate to get the set index's
    for index, com in enumerate(coms_list):
        # Assign an ID as a key to each community
        coms_dict[f'c{index}']['n'] = com

        com_subgraph = H.subgraph(com)

        # Compute general community metrics
        coms_dict[f'c{index}']['node_count'] = nx.number_of_nodes(com_subgraph)
        coms_dict[f'c{index}']['edge_count'] = nx.number_of_edges(com_subgraph)

        # Compute degree centrality for the community subgraphs (intra-community degree)
        coms_dict[f'c{index}']['intra_degree'] = nx.degree(com_subgraph)
