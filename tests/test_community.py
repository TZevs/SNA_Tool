import pytest
import networkx as nx

from src.community import detect

def test_returns_two_dicts():
    G = nx.binomial_graph(n=10, p=0.5)

    node_comms, comms_dict = detect.detect_communities(G)

    assert isinstance(node_comms, dict)
    assert isinstance(comms_dict, dict)

def test_all_nodes_assigned():
    G = nx.binomial_graph(n=10, p=0.5)

    node_comms, _ = detect.detect_communities(G)

    assert set(node_comms.keys()) == set(G.nodes())

def test_communities_contain_nodes():
    G = nx.binomial_graph(n=10, p=0.5)

    _, comms_dict = detect.detect_communities(G)

    all_nodes = set()
    for nodes in comms_dict.values():
        all_nodes.update(nodes)

    assert all_nodes == set(G.nodes())

def test_comm_dict_and_node_comms_match():
    G = nx.binomial_graph(n=10, p=0.5)

    node_comms, comms_dict = detect.detect_communities(G)

    for node, com_id in node_comms.items():
        assert node in comms_dict[com_id]

def test_communities_empty_graph():
    G = nx.Graph()

    node_comms, comms_dict = detect.detect_communities(G)

    assert node_comms == {}
    assert comms_dict == {}

def test_communities_single_node_graph():
    G = nx.Graph()
    G.add_node(1)

    node_comms, comms_dict = detect.detect_communities(G)

    assert node_comms == {1: 'c0'}
    assert comms_dict == {'c0': [1]}

def test_invalid_input_non_graph():
    invalid_input = "not a graph"

    node_comms, comms_dict = detect.detect_communities(invalid_input)

    assert node_comms == {} or node_comms is None
    assert comms_dict == {} or comms_dict is None
