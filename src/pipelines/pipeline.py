from graph.graph_builder import build_graph
from graph.data_loader import load_data

from pipelines.metric_pipeline import run_global_metrics_pipeline, run_local_metrics_pipeline
from community.detect import detect_communities

from graph.overview import compute_global_stats
from community.comm_stats import compute_community_stats

from utils.df_builder import build_metrics_df

from roles.thresholds import get_local_thresholds, compute_global_thresholds
from roles.roles import assign_global_roles, assign_local_roles

from evaluation.evaluate import evaluate_rank_correlations

def run_pipeline(file_path='../../data/raw/facebook_combined.txt'):
    # Load and clean edge-list dataset
    edge_df = load_data(file_path)
    # Create graph with cleaned edge data
    G = build_graph(edge_df)

    # Run global metric pipeline
    bet, close, deg, eigen, core, truss = run_global_metrics_pipeline(G)

    # Detect communities
    node_comms, comms, mod = detect_communities(G)
    # Run local metric pipeline
    z_score, part_eff = run_local_metrics_pipeline(G, node_comms, comms)

    # Calculating network stats for global and communities, saved as JSON to persistent storage in the data directory
    compute_global_stats(G, mod)
    compute_community_stats(G, comms)

    # Build DataFrame containing the global and local metrics for each node
    df = build_metrics_df(G, node_comms, bet, close, deg, eigen, core, truss, z_score, part_eff)

    # Get fixed local thresholds
    local_thresholds = get_local_thresholds()
    # Compute global percentile thresholds using metric values
    global_thresholds = compute_global_thresholds(df)

    # Assign global and local roles using the (global & local) thresholds
    local_roles_df = assign_local_roles(df, local_thresholds, node_comms)
    global_roles_df = assign_global_roles(df, global_thresholds)

    # Merge the returned role assignment DF to the metric DF with the node column
    df = df.merge(local_roles_df, on='node', how='left')
    df = df.merge(global_roles_df, on='node', how='left')

    # Run evaluation methods on the metric data
    eval_df = evaluate_rank_correlations(df)
    # Output correlation DF as CSV to persistent storage in data directory
    eval_df.to_csv('../../data/processed/rank_corr_eval.csv', index=False)

    # Output metric DF as CSV to persistent storage in data directory
    df.to_csv('../../data/processed/node_data.csv', index=False)

    # Output edge-list DF as CSV to persistent storage for community graphs in frontend
    edge_df.to_csv('../../data/processed/edge_data.csv', index=False)

    # End of analysis pipeline
    return

run_pipeline()