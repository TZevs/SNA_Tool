from client import fetch_global_metrics, fetch_global_recs, fetch_community_ids, fetch_community_nodes, fetch_community_metrics, fetch_community_recs

def load_global_data():
    metrics_raw = fetch_global_metrics()
    nodes = metrics_raw["nodes"].copy()

    global_roles = [node['global_role'] for node in nodes]
    cleaned_metrics = [
        {k: v for k, v in node.items() if k != 'global_role'}
        for node in nodes
    ]

    return {
        "metrics": cleaned_metrics,
        "global_roles": global_roles,
        "recs": fetch_global_recs()["recs"],
    }

def load_community_data(comm_id):
    community = fetch_community_nodes(comm_id)
    metrics = fetch_community_metrics(comm_id)['nodes']

    local_roles = [node['local_role'] for node in metrics]
    cleaned_metrics = [
        {k: v for k, v in node.items() if k != 'local_role' or k != 'community'}
        for node in metrics
    ]

    nodes = community["nodes"]
    edges = community["edges"]

    nodes = [
        {"data": {"id": (n["node"]), "label": (n["node"])}}
        for n in nodes
    ]
    edges = [
        {"data": {"source": (e["source"]), "target": (e["target"])}}
        for e in edges
    ]

    return {
        "nodes": nodes,
        "edges": edges,
        "metrics": cleaned_metrics,
        "local_roles": local_roles,
        "recs": fetch_community_recs(comm_id),
    }

def load_community_ids():
    ids = fetch_community_ids()
    return {
        "ids": ids['comm_ids'],
    }