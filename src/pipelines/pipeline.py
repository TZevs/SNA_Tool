from graph.graph_builder import build_graph
from graph.data_loader import load_data

from community.detect import detect_communities

from roles.thresholds import get_local_thresholds, compute_global_thresholds
from roles.roles import assign_global_roles, assign_local_roles

from utils.df_builder import build_metrics_df

from pipelines.metric_pipeline import run_global_metrics_pipeline, run_local_metrics_pipeline

from recommendation.global_recommendations import recommend_global_roles
from recommendation.local_recommendations import recommend_local_roles

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

    global_recs = recommend_global_roles()
    local_recs = recommend_local_roles(local_roles_df)

    df.to_csv('../../data/processed/metric_data.csv')

    local_roles_df.to_csv('../../data/processed/local_roles.csv')
    global_roles_df.to_csv('../../data/processed/global_roles.csv')

    global_recs.to_csv('../../data/processed/global_recs.csv')
    local_recs.to_csv('../../data/processed/local_recs.csv')

    return