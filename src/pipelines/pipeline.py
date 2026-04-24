import time

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

def run_pipeline(file_path='../../data/raw/facebook_combined.txt', verbose=True):
    # Dictionary to store runtimes
    runtimes = {}
    start_pipeline = time.perf_counter()
    # ------------------------------------
    # Load/Clean Dataset + Graph Creation
    # ------------------------------------
    start_graph = time.perf_counter()
    edge_df = load_data(file_path)
    G = build_graph(edge_df)
    end_graph = time.perf_counter()
    runtimes["Data Load - Graph Creation"] = end_graph - start_graph
    if verbose:
        print(f"Data Load - Graph Creation: {end_graph - start_graph:.4f}s")

    # ------------------------------------
    # Global Metrics Pipeline
    # ------------------------------------
    start_global = time.perf_counter()
    bet, close, deg, eigen, core, truss, truss_elapsed = run_global_metrics_pipeline(G)
    end_global = time.perf_counter()
    runtimes["K-Truss"] = truss_elapsed
    runtimes["Compute Global Metrics"] = end_global - start_global
    if verbose:
        print(f"Compute Global Metrics: {end_global - start_global:.4f}s")

    # ------------------------------------
    # Detect Communities
    # ------------------------------------
    start_comm = time.perf_counter()
    node_comms, comms, mod = detect_communities(G)
    end_comm = time.perf_counter()
    runtimes["Community Detection"] = end_comm - start_comm
    if verbose:
        print(f"Community Detection: {end_comm - start_comm:.4f}s")

    # ------------------------------------
    # Local Metrics Pipeline
    # ------------------------------------
    start_local = time.perf_counter()
    z_score, part_eff = run_local_metrics_pipeline(G, node_comms, comms)
    end_local = time.perf_counter()
    runtimes["Compute Local Metrics"] = end_local - start_local
    if verbose:
        print(f"Compute Local Metrics: {end_local - start_local:.4f}s")

    # ------------------------------------
    # Compute Statistics (global & local)
    # ------------------------------------
    start_stats = time.perf_counter()
    compute_global_stats(G, mod)
    compute_community_stats(G, comms)
    end_stats = time.perf_counter()
    runtimes["Compute Stats"] = end_stats - start_stats
    if verbose:
        print(f"Compute Stats: {end_stats - start_stats:.4f}s")

    # Build DataFrame containing the global and local metrics for each node
    df = build_metrics_df(G, node_comms, bet, close, deg, eigen, core, truss, z_score, part_eff)

    # ------------------------------------
    # Compute Thresholds + Assign Roles (global & local)
    # ------------------------------------
    start_roles = time.perf_counter()

    # Get fixed local literature thresholds
    local_thresholds = get_local_thresholds()
    # Compute percentile-based global thresholds
    global_thresholds = compute_global_thresholds(df)

    # Assign global and local roles using the (global & local) thresholds
    local_roles_df = assign_local_roles(df, local_thresholds)
    global_roles_df = assign_global_roles(df, global_thresholds)

    # Merge the returned role assignment DF to the metric DF with the node column
    df = df.merge(local_roles_df, on='node', how='left')
    df = df.merge(global_roles_df, on='node', how='left')

    end_roles = time.perf_counter()
    runtimes["Compute Thresholds - Assign Roles"] = end_roles - start_roles
    if verbose:
        print(f"Compute Thresholds - Assign Roles: {end_roles - start_roles:.4f}s")

    # ------------------------------------
    # Perform Metric Evaluations
    # ------------------------------------
    start_eval = time.perf_counter()
    eval_df = evaluate_rank_correlations(df)
    end_eval = time.perf_counter()
    runtimes["Evaluation"] = end_eval - start_eval
    if verbose:
        print(f"Evaluation: {end_eval - start_eval:.4f}s")

    # ------------------------------------
    # CSV Outputs - CSV to persistent storage in the data directory
    # ------------------------------------
    start_out = time.perf_counter()
    eval_df.to_csv('../../data/processed/rank_corr_eval.csv', index=False)
    df.to_csv('../../data/processed/node_data.csv', index=False)
    edge_df.to_csv('../../data/processed/edge_data.csv', index=False)
    end_out = time.perf_counter()
    runtimes["Write Outputs"] = end_out - start_out
    if verbose:
        print(f"Write Outputs: {end_out - start_out:.4f}s")

    # End pipeline counter
    end_pipeline = time.perf_counter()
    runtimes["Pipeline"] = end_pipeline - start_pipeline

    # ------------------------------------
    # Runtime Table
    # ------------------------------------
    if verbose:
        print("\n=== Runtime Summary ===")
        for step, t in runtimes.items():
            print(f"{step:<35} {t:.4f}s")

    return df

run_pipeline()