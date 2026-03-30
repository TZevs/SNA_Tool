import pytest
import pandas as pd

from src.roles import roles

@pytest.fixture
def test_global_df():
    return pd.DataFrame({
        'node': ['A', 'B'],
        'degree': [10, 2],
        'global_closeness': [0.3, 0.9],
        'global_core_num': [5, 0],
        'betweenness': [0.04, 0.25],
        'trussness': [0.8, 0.2],
    })
@pytest.fixture
def global_thresholds():
    return pd.DataFrame({
        0.90: {
            'degree': 5,
            'global_core_num': 3,
            'global_closeness': 0.8,
            'betweenness': 0.2,
            'trussness': 0.7,
        },
        0.75: {
            'degree': 4,
            'global_core_num': 2,
            'global_closeness': 0.6,
            'betweenness': 0.15,
            'trussness': 0.6,
        },
        0.50: {
            'degree': 3,
            'global_core_num': 1,
            'global_closeness': 0.4,
            'betweenness': 0.1,
            'trussness': 0.5,
        },
        0.25: {
            'degree': 1,
            'global_core_num': 0,
            'global_closeness': 0.2,
            'betweenness': 0.05,
            'trussness': 0.3,
        },
    })

def test_global_roles_returns_df(test_global_df, global_thresholds):
    result = roles.assign_global_roles(test_global_df, global_thresholds)

    assert 'node' in result.columns
    assert 'global_role' in result.columns
    assert isinstance(result, pd.DataFrame)

def test_global_access_to_roles_by_index(test_global_df, global_thresholds):
    result = roles.assign_global_roles(test_global_df, global_thresholds)

    first_row = result.iloc[0]
    third_row = result.iloc[1]

    assert first_row['node'] == 'A'
    assert first_row['global_role'] == 'global_core_node'

    assert third_row['node'] == 'B'
    assert third_row['global_role'] == 'global_bridge'

def test_global_grouping_by_role(test_global_df, global_thresholds):
    result = roles.assign_global_roles(test_global_df, global_thresholds)

    counts = result.groupby('global_role').size().to_dict()

    assert counts == {'global_bridge': 1, 'global_core_node': 1}

