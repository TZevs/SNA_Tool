import networkx as nx

def undir_kshell(G):
    H = G.copy()
    # Compute k-core decomposition
    #   - computes the
    #   - identifies the main structure of the network, the nodes with at least k neighbours
    #   - Returns k-shell subgraphs of G
    main_shell = nx.k_shell(H)