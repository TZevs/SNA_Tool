import networkx as nx

def undir_kcore_shell(G):
    H = G.copy()
    # Compute k-core decomposition
    #   - recursively removes the nodes with less than k-max degrees
    #   - computes the structure of the entire network, or the structure of nodes with at least (k+1) degrees
    #   - Returns the maximal k-core subgraph (the largets possible value of k)
    main_core = nx.k_core(H)

    core_nums = nx.core_number(H)

    # Compute k-core decomposition
    #   - the recursively removed nodes are stored in a bucket == kshell
    #   - computes the k
    #   - Returns k-shell nodes
    main_shell = nx.k_shell(H)