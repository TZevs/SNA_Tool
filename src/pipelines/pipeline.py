from graph.graph_builder import build_graph
from graph.data_loader import load_data

from community.detect import detect_communities

from roles.thresholds import get_local_thresholds, compute_global_thresholds
from roles.roles import assign_global_roles, assign_local_roles

from utils.df_builder import build_metrics_df

from pipelines.metric_pipeline import run_global_metrics_pipeline, run_local_metrics_pipeline

def run_pipeline(file_path='../../data/raw/facebook_combined.txt'):
    edge_df = load_data(file_path)
    G = build_graph(edge_df)

    bet, close, deg, eigen, core, truss = run_global_metrics_pipeline(G)

    node_comms, comms = detect_communities(G)
    l_close, l_core, z_score, part_eff = run_local_metrics_pipeline(G, node_comms, comms)

    df = build_metrics_df(G, node_comms, l_close, l_core, bet, close, deg, eigen, core, truss, z_score,
                                     part_eff)

    local_thresholds = get_local_thresholds()
    global_thresholds = compute_global_thresholds(df)

    local_roles_df = assign_local_roles(df, local_thresholds, node_comms)
    global_roles_df = assign_global_roles(df, global_thresholds)

    local_roles_df = local_roles_df.drop('community', axis=1)
    df = df.merge(local_roles_df, on='node', how='left')
    df = df.merge(global_roles_df, on='node', how='left')

    df.to_csv('../../data/processed/node_data.csv')
    edge_df.to_csv('../../data/processed/edge_data.csv')

    return