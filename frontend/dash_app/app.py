from dash import Dash, html, dcc
from callbacks import *

app = Dash(
    __name__,
    external_stylesheets=[
        dbc.themes.DARKLY,
        "https://cdn.jsdelivr.net/npm/ag-grid-community@32.3.3/styles/ag-grid.css",
        "https://cdn.jsdelivr.net/npm/ag-grid-community@32.3.3/styles/ag-theme-quartz.css",
        "https://cdn.jsdelivr.net/npm/ag-grid-community@32.3.3/styles/ag-theme-quartz-dark.css",
    ],
    suppress_callback_exceptions=True
)
server = app.server

# ── Stores ────────────────────────────────────────────────────────────────────
stores = html.Div([
    dcc.Store(id='global-store'),
    dcc.Store(id='community-id-store'),
    dcc.Store(id='community-store', data={}),
    dcc.Store(id='local-recs-store'),
    dcc.Store(id='local-stats-store'),
])

# ── Global (left) column ──────────────────────────────────────────────────────
global_col = dbc.Col([
    html.H3("Global Analysis"),
    html.Hr(),

    dbc.Card(dbc.CardBody([
        html.H5("Overview"),
        html.Div(id="global-overview"),
    ]), class_name="mb-3"),

    dbc.Card(dbc.CardBody([
        html.H5("Metrics Table"),
        html.Div(id="global-metrics"),
        html.Div(id='global-row-details'),
    ]), class_name="mb-3"),

    html.Hr(),
    html.H3('Data Visualisations'),
    dbc.Card(dbc.CardBody([
        html.H5("Bar Plot"),
        html.Div(id="global-roles-chart"),
    ]), class_name="mb-3"),

    dbc.Card(dbc.CardBody([
        html.H5("Histogram"),
        html.Div(id="degree-dist"),
    ]), class_name="mb-3"),

], xs=12, lg=6)

# ── Community (right) column ──────────────────────────────────────────────────
community_col = dbc.Col([
    html.H3("Community Analysis"),
    html.Hr(),

    dbc.Card(dbc.CardBody([
        html.H5("Select Community"),
        dcc.Dropdown(id="community-dropdown", placeholder="Choose a community…", style={"color": "Black"}),
    ]), class_name="mb-3"),

    dbc.Card(dbc.CardBody([
        html.H5("Overview"),
        html.Div(id="community-overview"),
    ]), class_name="mb-3"),

    dbc.Card(dbc.CardBody([
        html.H5("Community Graph"),
        html.Div(id="community-graph"),
    ]), class_name="mb-3"),

    dbc.Card(dbc.CardBody([
        html.H5("Metrics Table"),
        html.Div(id="community-metrics"),
        html.Div(id='community-row-details'),
    ]), class_name="mb-3"),

    dbc.Card(dbc.CardBody([
        html.H5("Bar Plot"),
        html.Div(id="community-roles-chart"),
    ]), class_name="mb-3"),

], xs=12, lg=6)

# ── Root layout ───────────────────────────────────────────────────────────────
app.layout = dbc.Container([
    stores,
    html.Br(),
    html.H2("Social Network & Influence Analysis", className="text-center"),
    html.Hr(),
    dbc.Row([global_col, community_col]),
], fluid=True)


if __name__ == "__main__":
    app.run(debug=True)
