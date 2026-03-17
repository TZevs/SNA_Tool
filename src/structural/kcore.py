import networkx as nx

def compute_kcore(G):
    """
    - Compute the core number for each node in the graph G
    - core_number = the largest value k of a k-core containing the node
    - Using core_number instead of k_core as that returns a subgraph, which is not needed for the analysis, other than for visualisation
    """
    core_nums = nx.core_number(G)

    # Returns dictionary {node: core_value}
    return core_nums