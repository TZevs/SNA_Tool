import networkx as nx
import pandas as pd

def build_graph(df):
    # Create an empty undirected graph
    G = nx.Graph()

    # Add unweighted edges to the graph from the DataFrame
    G.add_edges_from(df.values)

    # Return the graph
    return G

def graph_statistics(G):
    # Calculate the number of edges and nodes in the graph
    num_edges = G.number_of_edges()
    num_nodes = G.number_of_nodes()

    # Compute the average node degree in the graph
    # Get the total number of degrees (every edge has 2 nodes) by doing number_of_edges * 2
    # Then divide by the number_of_nodes to get the average node degree
    avg_degree = (2 * num_edges) / num_nodes

    # Return a dictionary containing the statistics
    stats = {
        'num_edges': num_edges,
        'num_nodes': num_nodes,
        'avg_degree': avg_degree
    }
    return stats


# Consider adding a function to assign weights to edges based on the mutual edges nodes have.