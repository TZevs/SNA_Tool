import networkx as nx
from collections import deque

def compute_support(G):
    # Compute triangle support for every edge in the graph

    # Store every edge (u, v) common neighbours count
    support = {}
    # Iterate through edges in Graph
    for (u, v) in G.edges():
        # common_neighbors(G, u, v) returns nodes w that form triangles (u, v, w)
        support[(u, v)] = len(list(nx.common_neighbors(G, u, v)))

    # Return dictionary {(u, v): trangle_count}
    return support

def compute_ktruss(G):
    # Compute k-truss decomposition using iterative edge peeling

    # Copy of graph to keep the original graph G
    H = G.copy()

    # Store the truss level(-1) each edge is removed from
    removed_edge_truss = {}

    # Initial triangle support for all edges
    support = compute_support(H)

    k = 2
    # Continue peeling until no edges remain
    while H.number_of_edges() > 0:
        # Queue edges whose support is below the k-truss threshold (support < k - 2)
        queue = deque([e for e, s in support.items() if s < k - 2])

        # Iterate through edges in queue for removal
        while queue:
            # Get edge from queue
            u, v = queue.popleft()

            # Skip if edge was already removed
            if not H.has_edge(u, v):
                continue

            # Remove edge and store its truss level
            H.remove_edge(u, v)
            removed_edge_truss[(u, v)] = k - 1
            support.pop((u, v), None)

            # Update support for neighbouring edges in triangles (u, v, w)
            for w in nx.common_neighbors(H, u, v):
                for e in [(u, w), (v, w)]:
                    if e in support:
                        support[e] -= 1
                        # If support drops below threshold, add to queue for removal
                        if support[e] < k - 2:
                            queue.append(e)

        # Move onto the next truss level
        k += 1

    # Remaining edges belong to the highest truss level reached
    for (u, v) in H.edges():
        removed_edge_truss[(u, v)] = k - 1

    # Convert edge truss levels into node truss levels
    return compute_node_truss(removed_edge_truss)

def compute_node_truss(edge_truss):
    # Get node truss from edge truss level values

    # node_truss[node] = the maximum truss of the connected edges
    node_truss = {}
    # Iterate through edge_truss dictionary
    for (u, v), tr in edge_truss.items():
        # Assign highest truss level for each endpoint
        node_truss[u] = max(node_truss.get(u, 0), tr)
        node_truss[v] = max(node_truss.get(v, 0), tr)

    # Return dictionary {node: truss_lvl}
    return dict(node_truss)