import time

from global_metrics import betweenness, closeness, degree, eigenvector, kcore, ktruss
from community.metrics import zscore, participation_coeff

# Global metric pipeline
def run_global_metrics_pipeline(G, verbose=True):
    # Compute global centrality metrics for all nodes (betweenness, closeness, degree, eigenvector)
    bet = betweenness.compute_betweenness(G)
    close = closeness.compute_closeness(G)
    deg = degree.compute_degree(G)
    eigen = eigenvector.compute_eigenvector(G)

    # Compute decomposition methods (k-core, k-truss)
    core = kcore.compute_kcore(G)
    start_truss = time.perf_counter()
    truss = ktruss.compute_ktruss(G)
    end_truss = time.perf_counter()
    truss_elapsed = end_truss - start_truss
    if verbose:
        print(f'K-Truss: {truss_elapsed:.4f}s')

    # Return global metrics
    return bet, close, deg, eigen, core, truss, truss_elapsed

def run_local_metrics_pipeline(G, node_comms, comms):
    # Compute local community-aware metrics (within-module degree (z-score), participation coefficient)
    z_score = zscore.compute_local_zscore(G, comms)
    part_eff = participation_coeff.compute_participation_coefficient(G, node_comms)

    # Return all local metrics
    return z_score, part_eff