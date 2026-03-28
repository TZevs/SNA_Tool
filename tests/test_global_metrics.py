import pytest
import networkx as nx

from src.structural import betweenness, closeness, degree, eigenvector, kcore, ktruss

@pytest.mark.parametrize('centrality', [
    betweenness.compute_betweenness,
    closeness.compute_closeness,
    degree.compute_degree,
    eigenvector.compute_eigenvector,
    kcore.compute_kcore,
    ktruss.compute_ktruss,
], ids=['Betweenness Dict', 'Closeness Dict', 'Degree Dict', 'Eigenvector Dict', 'Kcore Dict', 'Ktruss Dict'])
def test_returns_dict(centrality):
    G = nx.binomial_graph(n=10, p=0.5)
    result = centrality(G)

    assert isinstance(result, dict)

@pytest.mark.parametrize('centrality', [
    betweenness.compute_betweenness,
    closeness.compute_closeness,
    degree.compute_degree,
    eigenvector.compute_eigenvector,
    kcore.compute_kcore,
    ktruss.compute_ktruss,
], ids=['Betweenness Keys=Nodes', 'Closeness Keys=Nodes', 'Degree Keys=Nodes', 'Eigenvector Keys=Nodes', 'Kcore Keys=Nodes', 'Ktruss Keys=Nodes'])
def test_keys_are_nodes(centrality):
    G = nx.binomial_graph(n=10, p=0.5)
    result = centrality(G)

    assert set(result.keys()) == set(G.nodes())

@pytest.mark.parametrize('centrality', [
    betweenness.compute_betweenness,
    closeness.compute_closeness,
    degree.compute_degree,
    eigenvector.compute_eigenvector,
], ids=['Betweenness Dict Order', 'Closeness Dict Order', 'Degree Dict Order', 'Eigenvector Dict Order'])
def test_dict_order(centrality):
    G = nx.binomial_graph(n=10, p=0.5)
    result = centrality(G)

    values = list(result.values())
    assert values == sorted(values, reverse=True)

@pytest.mark.parametrize('centrality', [
    betweenness.compute_betweenness,
    closeness.compute_closeness,
    degree.compute_degree,
    eigenvector.compute_eigenvector,
    kcore.compute_kcore,
    ktruss.compute_ktruss,
], ids=['Betweenness Dict Empty', 'Closeness Dict Empty', 'Degree Dict Empty', 'Eigenvector Dict Empty', 'Kcore Dict Empty', 'Ktruss Dict Empty'])
def test_empty_graph(centrality):
    G = nx.Graph()
    result = centrality(G)

    assert result == {}

@pytest.mark.parametrize('centrality, expected', [
    (betweenness.compute_betweenness, 0.0),
    (closeness.compute_closeness, 0.0),
    (degree.compute_degree, 1),
    (eigenvector.compute_eigenvector, 1.0),
    (kcore.compute_kcore, 0),
    (ktruss.compute_ktruss, 0),
], ids=['Betweenness Single Node', 'Closeness Single Node', 'Degree Single Node', 'Eigenvector Single Node', 'Kcore Single Node', 'Ktruss Single Node'])
def test_empty_graph(centrality, expected):
    G = nx.Graph()
    G.add_node(1)

    result = centrality(G)

    assert len(result) == 1
    assert result[1] == expected