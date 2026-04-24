from global_metrics import betweenness, closeness, degree, eigenvector, kcore, ktruss
from community.metrics import zscore, participation_coeff

# Global metric pipeline
def run_global_metrics_pipeline(G):
    # Compute global centrality metrics for all nodes (betweenness, closeness, degree, eigenvector)
    bet = betweenness.compute_betweenness(G)
    close = closeness.compute_closeness(G)
    deg = degree.compute_degree(G)
    eigen = eigenvector.compute_eigenvector(G)

    # Compute decomposition methods (k-core, k-truss)
    core = kcore.compute_kcore(G)
    truss = ktruss.compute_ktruss(G)

    # Return global metrics
    return bet, close, deg, eigen, core, truss

def run_local_metrics_pipeline(G, node_comms, comms):
    # Compute local community-aware metrics (within-module degree (z-score), participation coefficient)
    z_score = zscore.compute_local_zscore(G, comms)
    part_eff = participation_coeff.compute_participation_coefficient(G, node_comms)

    # Return all local metrics
    return z_score, part_eff