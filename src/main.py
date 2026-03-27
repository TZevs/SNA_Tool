from graph import data_loader, graph_builder
from community import detect
from roles import df_builder, thresholds, roles
from pipelines import metric_pipeline

def run_main_pipeline(file_path='../data/facebook_combined.txt'):
    edge_df = data_loader.load_data(file_path)
    edge_df = edge_df.head(2000)
    G = graph_builder.build_graph(edge_df)

    bet, close, deg, eigen, core, truss = metric_pipeline.run_global_metrics_pipeline(G)

    node_comms, comms = detect.detect_communities(G)
    intra, inter, l_close, l_core = metric_pipeline.run_local_metrics_pipeline(G, node_comms, comms)

    metric_df = df_builder.build_metrics_df(G, node_comms, intra, inter, l_close, l_core, bet, close, deg, eigen, core, truss)
    metric_df.to_csv('../data/bug_groupby.csv')

    l_thresh = thresholds.compute_local_thresholds(metric_df)
    g_thresh = thresholds.compute_global_thresholds(metric_df)

    local_roles = roles.assign_local_roles(metric_df, l_thresh)
    global_roles = roles.assign_global_roles(metric_df, g_thresh)

    df = metric_df.merge(local_roles, on='node')
    df = df.merge(global_roles, on='node')

    df.to_csv('../data/sna_result_data.csv')

    return

if __name__ == '__main__':
    run_main_pipeline()