from graph import data_loader, graph_builder
from community import detect
from roles import thresholds, roles
from utils import df_builder
from pipelines import metric_pipeline

def run_main_pipeline(file_path='../data/facebook_combined.txt'):
    edge_df = data_loader.load_data(file_path)
    G = graph_builder.build_graph(edge_df)

    bet, close, deg, eigen, core, truss = metric_pipeline.run_global_metrics_pipeline(G)

    node_comms, comms = detect.detect_communities(G)
    l_close, l_core, z_score, part_eff = metric_pipeline.run_local_metrics_pipeline(G, node_comms, comms)

    df = df_builder.build_metrics_df(G, node_comms, l_close, l_core, bet, close, deg, eigen, core, truss, z_score, part_eff)

    local_thresholds = thresholds.get_local_thresholds()
    global_thresholds = thresholds.compute_global_thresholds(df)

    local_roles_df = roles.assign_local_roles(df, local_thresholds, node_comms)
    global_roles_df = roles.assign_global_roles(df, global_thresholds)

    #df = metric_df.merge(local_roles, on='node', how='left')
    #df = df.merge(global_roles, on='node', how='left')

    df.to_csv('../data/sna_result_data.csv')
    local_roles_df.to_csv('../data/local_roles.csv')
    global_roles_df.to_csv('../data/global_roles.csv')

    return

if __name__ == '__main__':
    run_main_pipeline()