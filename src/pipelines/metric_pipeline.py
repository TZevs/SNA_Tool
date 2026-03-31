from structural import betweenness, closeness, degree, eigenvector, kcore, ktruss
from community.metrics import intra_inter_degree, local_closeness, local_kcore, zscore, participation_coeff

def run_global_metrics_pipeline(G):
    bet = betweenness.compute_betweenness(G)
    close = closeness.compute_closeness(G)
    deg = degree.compute_degree(G)
    eigen = eigenvector.compute_eigenvector(G)
    core = kcore.compute_kcore(G)
    truss = ktruss.compute_ktruss(G)

    return bet, close, deg, eigen, core, truss

def run_local_metrics_pipeline(G, node_comms, comms):
    #intra, inter = intra_inter_degree.compute_intra_inter_degree(G, node_comms)
    l_close = local_closeness.compute_community_closeness(G, comms)
    l_core = local_kcore.compute_community_kcore(G, comms)
    z_score = zscore.compute_local_zscore(G, comms)
    part_eff = participation_coeff.compute_participation_coefficient(G, node_comms)

    return l_close, l_core, z_score, part_eff