import pytest
import networkx as nx

from src.community.metrics import zscore, participation_coeff
from src.community import detect

@pytest.fixture
def mock_communities():
    G = nx.binomial_graph(n=100, p=1, seed=42)

    node_comms, comms_dict = detect.detect_communities(G)

    return G, node_comms, comms_dict

def test_returns_dict(mock_communities):
    G, _, comms_dict = mock_communities

    results = zscore.compute_local_zscore(G, comms_dict)

    assert isinstance(results, dict)

def test_return_p_dict(mock_communities):
    G, node_comms, _ = mock_communities

    results = participation_coeff.compute_participation_coefficient(G, node_comms)

    assert isinstance(results, dict)
