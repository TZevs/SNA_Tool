import networkx as nx

def compute_kcore(G):
    # Compute the core number for each node in the graph G

    # core_number = the largest value k of a k-core containing the node
    # Not using the k_core method as it returns a subgraph, which is not useful for this analysis
    core_nums = nx.core_number(G)

    # Returns dictionary {node: core_value}
    return core_nums