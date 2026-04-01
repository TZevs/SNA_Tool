import networkx as nx
from collections import deque

def compute_support(G):
    # Dictionary storing edge triangle counts - {(u, v): count}
    support = {}
    # Iterate through edges in Graph
    for (u, v) in G.edges():
        # common_neighbors returns set of w(nodes) that are neighbors to u and v
        # len() returns the number of nodes in the set - the triangle count(support)
        # Assign the triangle count to the edge in the dictionary
        support[(u, v)] = len(list(nx.common_neighbors(G, u, v)))

    return support

def compute_ktruss(G):
    H = G.copy()

    removed_edge_truss = {}

    support = compute_support(H)

    k = 2
    while H.number_of_edges() > 0:

        queue = deque([e for e, s in support.items() if s < k - 2])

        while queue:
            u, v = queue.popleft()

            if not H.has_edge(u, v):
                continue

            H.remove_edge(u, v)
            removed_edge_truss[(u, v)] = k - 1
            support.pop((u, v), None)

            # Update neighbors
            for w in nx.common_neighbors(H, u, v):
                for e in [(u, w), (v, w)]:
                    if e in support:
                        support[e] -= 1
                        if support[e] < k - 2:
                            queue.append(e)

        k += 1

    for (u, v) in H.edges():
        removed_edge_truss[(u, v)] = k - 1

    return compute_node_truss(removed_edge_truss)

def compute_node_truss(edge_truss):
    # Dictionary storing edge truss level - {(u, v): max(edge_truss(connected to node))}
    node_truss = {}
    # Iterate through edge_truss dictionary
    for (u, v), tr in edge_truss.items():
        # node_truss = the maximum truss of the connected edges
        # Split the (u, v) edge into nodes u and v to assign truss value
        node_truss[u] = max(node_truss.get(u, 0), tr)
        node_truss[v] = max(node_truss.get(v, 0), tr)

    # Return dictionary {node: truss}
    return dict(node_truss)