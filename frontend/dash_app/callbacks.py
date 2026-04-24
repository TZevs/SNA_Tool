from dash import Input, Output, callback, html, State
import dash_bootstrap_components as dbc

from components.tables import metrics_table
from components.charts import role_bar_chart, community_graph, global_degree_hist, global_degree_hist_without_comm
from components.overview import overview_cards
from loaders import load_global_data, load_community_data, load_community_ids, load_local_recs, load_local_stats

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

@callback(
    Output("local-recs-store", "data"),
    Input("local-recs-store", "data")
)
def set_local_recs(data):
    if data is None:
        return load_local_recs()
    return data

@callback(
    Output("local-stats-store", "data"),
    Input("local-stats-store", "data"),
)
def set_local_stats(data):
    if data is None:
        return load_local_stats()
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

    return overview_cards(data['stats'], 'global-overview-content')

@callback(
    Output("global-metrics", "children"),
    Input("global-store", "data")
)
def render_global_metrics(data):
    if not data:
        return html.P("No global data available")



    return [
        metrics_table(data["metrics"], "global_metrics_table")
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
    Output("global-row-details", "children"),
    Input("global_metrics_table", "selectedRows"),
    State("global-store", "data")
)
def show_global_row_details(selected, store):
    if not selected:
        return [
            html.Br(),
            html.P("Select a row for further details.")
        ]

    row = selected[0]
    recs = store['recs']

    if row['global_role'] is None:
        return [
            html.Br(),
            dbc.CardHeader(f'Node: {row['node']} does not have a global role assigned.')
        ]

    return dbc.Card([
        dbc.CardHeader(f"Node: {row['node']}"),
        dbc.CardBody([
            html.Div([
                html.Div([
                    html.Strong("Role: "),
                    html.Span(row["global_role"]),
                    html.Br()
                ]),
                dbc.Card([
                    dbc.CardHeader(f"Recommendations"),
                    dbc.CardBody([
                        html.Div([
                            html.Strong("Why Target: "),
                            html.Span(recs[row['global_role']]['target']),
                            html.Br(),
                            html.Strong("Reason: "),
                            html.Span(recs[row['global_role']]['reason']),
                            html.Br(),
                            html.Strong("Meaning: "),
                            html.Span(recs[row['global_role']]['meaning']),
                        ]),
                    ])
                ])
            ], style={"lineHeight": "1.8"})
        ])
    ], style={"marginTop": "10px"})

@callback(
    Output("degree-dist", "children"),
    Input("global-store", "data")
)
def render_degree_dist(data):
    if not data:
        return html.P("No global data available")

    df = data['metrics']

    return [
        global_degree_hist(df),
        html.Br(),
        global_degree_hist_without_comm(df)
    ]

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
    Output("community-metrics", "children"),
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
        metrics_table(data["metrics"], "community_metrics_table")
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
        html.Div(id="node-info"),
        html.Br()
    ])

@callback(
    Output("node-info", "children"),
    Input("community-cyto", "tapNode"),
)
def show_local_node_info(node):
    if not node:
        return html.P("Click a node to see details")

    d = node['data']

    return dbc.Card([
        dbc.CardHeader(f'Node: {d.get('id')}'),
        dbc.CardBody([
            html.Div([
                html.Strong(f"Role: "),
                html.Span(d.get('role', 'No Role Assigned')),
                html.Br(),
                html.Strong(f"Z-Score: "),
                html.Span(d.get('local_zscore')),
                html.Br(),
                html.Strong(f"Participation Coefficient: "),
                html.Span(d.get('local_P')),
                html.Br()
            ])
        ])
    ])

@callback(
    Output("community-row-details", "children"),
    Input("community_metrics_table", "selectedRows"),
    State("local-recs-store", "data"),
)
def show_local_row_details(selected, store):
    if not selected:
        return [
            html.Br(),
            html.P("Select a row for further details.")
        ]

    row = selected[0]
    recs = store['recs']

    if row['local_role'] is None:
        return [
            html.Br(),
            dbc.CardHeader(f'Node: {row['node']} does not have a local role assigned.')
        ]

    return dbc.Card([
        dbc.CardHeader(f"Node: {row['node']}"),
        dbc.CardBody([
            html.Div([
                html.Div([
                    html.Strong("Role: "),
                    html.Span(row["local_role"]),
                    html.Br()
                ]),
                dbc.Card([
                    dbc.CardHeader(f"Recommendations"),
                    dbc.CardBody([
                        html.Div([
                            html.Strong("Why Target: "),
                            html.Span(recs[row['local_role']]['target']),
                            html.Br(),
                            html.Strong("Reason: "),
                            html.Span(recs[row['local_role']]['reason']),
                            html.Br(),
                            html.Strong("Meaning: "),
                            html.Span(recs[row['local_role']]['meaning']),
                        ]),
                    ])
                ])
            ], style={"lineHeight": "1.8"})
        ])
    ], style={"marginTop": "10px"})

@callback(
    Output("community-overview", "children"),
    Input("local-stats-store", "data"),
    Input("community-dropdown", "value")
)
def render_global_overview(data, comm_id):
    if not comm_id:
        return html.P("Select a Community")

    if not data:
        return html.P("No local data available")

    stats = data['stats']

    return overview_cards(stats[comm_id], 'local-overview-content')