import pytest
import pandas as pd

from src.roles import thresholds

@pytest.fixture
def test_df():
    return pd.DataFrame({
        "community": ["c0", "c0", "c1", "c1"],
        "intra": [1, 2, 3, 4],
        "inter": [2, 3, 4, 5],
        "local_closeness": [1, 1, 2, 2],
        "local_core_num": [1, 2, 2, 3],
        "degree": [5, 6, 7, 8],
        "global_closeness": [2, 3, 4, 5],
        "global_core_num": [1, 1, 2, 2],
        "betweenness": [0.1, 0.2, 0.3, 0.4],
        "eigenvector": [0.5, 0.6, 0.7, 0.8],
        "trussness": [2, 2, 3, 3],
    })

def test_threshold_functions_return_dfs(test_df):
    glb = thresholds.compute_global_thresholds(test_df)
    lcl = thresholds.compute_local_thresholds(test_df)

    assert type(glb) == pd.DataFrame
    assert type(lcl) == pd.DataFrame

def test_local_returned_df(test_df):
    result = thresholds.compute_local_thresholds(test_df)

    assert list(result.index) == ['c0', 'c1']

    assert type(result.columns) == pd.MultiIndex

    # Check MultiIndex columns, 'intra' used as an example
    assert ('intra', 0.25) in result.columns
    assert ('intra', 0.50) in result.columns
    assert ('intra', 0.75) in result.columns
    assert ('intra', 0.90) in result.columns

def test_global_returned_df(test_df):
    result = thresholds.compute_global_thresholds(test_df)

    assert list(result.columns) == ['degree', 'global_closeness', 'global_core_num', 'betweenness', 'eigenvector', 'trussness']
    assert list(result.index) == [0.25, 0.50, 0.75, 0.90]

def test_thresholds_empty_df():
    df = pd.DataFrame(columns=[
        "community", "intra", "inter", "local_closeness", "local_core_num", "degree", "global_closeness", "global_core_num", "betweenness", "eigenvector","trussness"
    ])

    glb = thresholds.compute_global_thresholds(df)
    lcl = thresholds.compute_local_thresholds(df)

    assert glb.empty
    assert lcl.empty