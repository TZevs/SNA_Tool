from client import (fetch_global_metrics, fetch_global_recs,
                    fetch_community_ids, fetch_community_nodes,
                    fetch_community_metrics, fetch_community_recs,
                    fetch_community_stats, fetch_global_stats)

def load_global_data():
    metrics = fetch_global_metrics()
    nodes = metrics["nodes"].copy()

    global_roles = [node['global_role'] for node in nodes]

    rec_dict = {
        item["role"]: {
            "reason": item["reason"],
            "meaning": item["meaning"],
            "target": item["target"]
        }
        for item in fetch_global_recs()["recs"]
    }

    return {
        "metrics": metrics['nodes'],
        "global_roles": global_roles,
        "recs": rec_dict,
        "stats": fetch_global_stats()['stats']
    }

def load_community_data(comm_id):
    community = fetch_community_nodes(comm_id)
    metrics = fetch_community_metrics(comm_id)['nodes']

    local_roles = [node['local_role'] for node in metrics]
    cleaned_metrics = [
        {k: v for k, v in node.items() if k != 'community'}
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
    }

def load_community_ids():
    ids = fetch_community_ids()
    return {
        "ids": ids['comm_ids'],
    }

def load_local_recs():
    data = fetch_community_recs()['recs']
    rec_lookup = {item['role']: item for item in data}
    return {
        "recs": rec_lookup,
    }

def load_local_stats():
    return {
        'stats': fetch_community_stats()['stats']
    }