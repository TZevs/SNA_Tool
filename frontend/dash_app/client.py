import requests

backend_url = "http://localhost:8000"

def fetch_global_metrics():
    try:
        return requests.get(f'{backend_url}/global/metrics').json()
    except Exception as ex:
        return {"status": "error", "message": str(ex)}

def fetch_global_recs():
    try:
        return requests.get(f'{backend_url}/global/recs').json()
    except Exception as ex:
        return {"status": "error", "message": str(ex)}


def fetch_community_ids():
    try:
        return requests.get(f'{backend_url}/community/ids').json()
    except Exception as ex:
        return {"status": "error", "message": str(ex)}

def fetch_community_nodes(comm_id):
    try:
        return requests.get(f'{backend_url}/community/{comm_id}').json()
    except Exception as ex:
        return {"status": "error", "message": str(ex)}

def fetch_community_metrics(comm_id):
    try:
        return requests.get(f'{backend_url}/community/metrics/{comm_id}').json()
    except Exception as ex:
        return {"status": "error", "message": str(ex)}

def fetch_community_recs():
    try:
        return requests.get(f'{backend_url}/community/recs').json()
    except Exception as ex:
        return {"status": "error", "message": str(ex)}