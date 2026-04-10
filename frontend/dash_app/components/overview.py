import dash_bootstrap_components as dbc
from dash import html

def overview_cards(data, id):
    is_local = True if id == "local-overview-content" else False

    return dbc.Row(
        [
            dbc.Col(stat_card(data["num_nodes"], "Nodes"), xs=12, sm=6, md=4),
            dbc.Col(stat_card(data["num_edges"], "Edges"), xs=12, sm=6, md=4),
            dbc.Col(stat_card(f'{data["density"]:.5f}', "Density"), xs=12, sm=6, md=4),
            dbc.Col(stat_card(f'{data["avg_deg"]:.3f}', "Average Degree"), xs=12, sm=6, md=4),
            dbc.Col(stat_card(data["diameter"], "Diameter"), xs=12, sm=6, md=4),
            None if is_local else dbc.Col(stat_card(f'{data["modularity"]:.3f}', "Modularity"), xs=12, sm=6, md=4),
        ], className="g-3"
    )

def stat_card(value, label):
    return dbc.Card(
        style={
            "backgroundColor": "#3a3a3a",
            "padding": "18px",
            "borderRadius": "10px",
            "boxShadow": "0 2px 6px rgba(0,0,0,0.35)",
            "height": "100%",
        },
        children=[
            html.Div([
                html.H6(value, style={"fontSize": "1.6rem", "fontWeight": "bold"}),
                html.P(label, style={"fontSize": "1.2rem"})
            ],
            style={"textAlign": "center"},
            )
        ]
    )