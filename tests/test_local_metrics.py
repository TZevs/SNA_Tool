import pytest
import networkx as nx

from src.community.metrics import local_closeness, local_kcore, zscore, participation_coeff
from src.community import detect

@pytest.fixture
def mock_communities():
    G = nx.binomial_graph(n=100, p=1, seed=42)

    node_comms, comms_dict = detect.detect_communities(G)

    return G, node_comms, comms_dict

@pytest.mark.parametrize('centrality', [
    local_closeness.compute_community_closeness,
    local_kcore.compute_community_kcore,
    zscore.compute_local_zscore,
], ids=['Local Closeness Dict', 'Local K-core Dict', 'Local Z-score Dict'])
def test_returns_dict(centrality, mock_communities):
    G, _, comms_dict = mock_communities

    results = centrality(G, comms_dict)

    assert isinstance(results, dict)

def test_return_p_dict(mock_communities):
    G, node_comms, _ = mock_communities

    results = participation_coeff.compute_participation_coefficient(G, node_comms)

    assert isinstance(results, dict)
