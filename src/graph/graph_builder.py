import networkx as nx
import pandas as pd

def build_graph(df):
    # Create an empty undirected graph
    G = nx.Graph()

    # Add unweighted edges to the graph from the DataFrame
    G.add_edges_from(df.values)

    # Return the graph
    return G