from dash import Input, Output, callback, html, State, no_update
import dash_bootstrap_components as dbc

from components.cards import role_cards
from components.tables import metrics_table
from components.charts import role_bar_chart, community_graph
from loaders import load_global_data, load_community_data, load_community_ids

GLOBAL_DATA = load_global_data()

# Initialise Store Data
@callback(
    Output("global-store", "data"),
    Input("global-store", "data")
)
def set_global_store(data):
    if data is None:
        return GLOBAL_DATA
    return data

@callback(
    Output("community-id-store", "data"),
    Input("community-id-store", "data")
)
def set_community_ids(data):
    if data is None:
        return load_community_ids()
    return data

# ---------------------------------------------------------------
# Global Column Cards
# ---------------------------------------------------------------
@callback(
    Output("global-overview", "children"),
    Input("global-store", "data")
)
def render_global_overview(data):
    if not data:
        return html.P("No global data available")

    nodes = [n["node"] for n in data["metrics"]]
    deg = [d["degree"] for d in data["metrics"]]

    return [
        html.P(f"Number of Users: {len(nodes)}")
    ]

@callback(
    Output("global-metrics-table", "children"),
    Input("global-store", "data")
)
def render_global_metrics(data):
    if not data:
        return html.P("No global data available")

    return [
        metrics_table(data["metrics"])
    ]

@callback(
    Output("global-roles-chart", "children"),
    Input("global-store", "data")
)
def render_global_roles(data):
    if not data:
        return html.P("No global data available")

    return [
        role_bar_chart(data["global_roles"], 'global_role')
    ]

@callback(
    Output("global-recs", "children"),
    Input("global-store", "data")
)
def render_global_recs(data):
    if not data:
        return html.P("No global data available")

    recs = data['recs']

    return role_cards(recs)

# ---------------------------------------------------------------
# Community/Local Column Cards
# ---------------------------------------------------------------
@callback(
    Output("community-dropdown", "options"),
    Input("community-id-store", "data")
)
def populate_dropdown(data):
    if not data:
        return []
    return [{"label": f"Comm {cid}", "value": cid} for cid in data['ids']]

@callback(
    Output("community-store", "data"),
    Input("community-dropdown", "value"),
    State("community-store", "data")
)
def update_community_cache(comm_id, store):
    if not comm_id:
        return store

    if store is None:
        store = {}

    if comm_id not in store:
        store[comm_id] = load_community_data(comm_id)

    return store

@callback(
    Output("community-metrics-table", "children"),
    Input("community-dropdown", "value"),
    Input("community-store", "data")
)
def render_community_metrics(comm_id, store):
    if not comm_id:
        return html.P("Select a Community")

    if comm_id not in store:
        return "Loading..."

    data = store[comm_id]

    return [
        metrics_table(data["metrics"])
    ]

@callback(
    Output("community-roles-chart", "children"),
    Input("community-dropdown", "value"),
    Input("community-store", "data")
)
def render_local_roles(comm_id, store):
    if not comm_id:
        return html.P("Select a Community")

    if comm_id not in store:
        return "Loading..."

    data = store[comm_id]

    return [
        role_bar_chart(data["local_roles"], 'local_role')
    ]

@callback(
    Output("community-graph", "children"),
    Input("community-dropdown", "value"),
    Input("community-store", "data")
)
def render_community_graph(comm_id, store):
    if not comm_id:
        return html.P("Select a Community")

    if comm_id not in store:
        return "Loading..."

    data = store[comm_id]

    return html.Div([
        community_graph(data),
        html.Div(id="node-info")
    ])

@callback(
    Output("node-info", "children"),
    Input("community-cyto", "tapNode"),
    State("community-store", "data"),
    State("community-dropdown", "value"),
)
def show_local_node_info(node, store, comm_id):
    if not node:
        return html.P("Click a node to see details")

    node_id = node['data']['id']

    recs_container = store[comm_id]["recs"]
    recs_list = recs_container.get("recs", [])

    rec = next((r for r in recs_list if str(r['node']) == node_id), None)

    d = node['data']

    return html.Div([
        html.H6(f"Node {node_id}"),
        html.P(f"Role: {d.get('local_role')}"),
        html.P(f"Z-Score: {d.get('local_zscore')}"),
        html.P(f"Participation Coefficient: {d.get('local_P')}"),
        html.P(f"Betweenness: {d.get('betweenness')}"),
        html.P(f"Closeness: {d.get('local_closeness')}"),
        html.Div([
            html.P(f"{d.get('local_role')} Recommendations:"),
            html.P(f"Reason: {rec['reason'] if rec else 'N/A'}"),
            html.P(f"Meaning: {rec['meaning'] if rec else 'N/A'}"),
            html.P(f"Target: {rec['target'] if rec else 'N/A'}"),
        ])
    ])