import networkx as nx

def compute_ktruss(G):
    # Compute k-truss decomposition - with static support (approx k-truss, not true decomposition)

    # Dictionary storing edge triangle counts - {(u, v): count}
    support = {}
    # Iterate through edges in Graph
    for (u, v) in G.edges():
        # common_neighbors returns set of w(nodes) that are neighbors to u and v
        # len() returns the number of nodes in the set - the triangle count(support)
        # Assign the triangle count to the edge in the dictionary
        support[(u, v)] = len(list(nx.common_neighbors(G, u, v)))

    # Dictionary storing edge truss level - {(u, v): truss_lvl}
    edge_truss = {}
    # Iterate through edges in Graph
    for (u, v) in G.edges():
        # Calculate truss level(k) = support(triangle count) + 2
        k = support[(u, v)] + 2
        # Assign k-truss to the edge in the dictionary
        edge_truss[(u, v)] = k

    # Dictionary storing edge truss level - {(u, v): max(edge_truss(connected to node))}
    node_truss = {}
    # Iterate through edge_truss dictionary
    for (u, v), truss_lvl in edge_truss.items():
        # node_truss = the maximum truss of the connected edges
        # Split the (u, v) edge into nodes u and v to assign truss value
        node_truss[u] = max(2, truss_lvl)
        node_truss[v] = max(2, truss_lvl)

    # Return dictionary {node: truss}
    return node_truss
