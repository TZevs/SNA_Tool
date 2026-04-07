import dash_bootstrap_components as dbc
from dash import html
import plotly.express as px

palette = px.colors.qualitative.Light24
ROLE_COLOURS = {
    "Global Hub": palette[7],
    "Global Broker": palette[1],
    "Global Core": palette[2],
    "Global Spreader": palette[11],
    "Global Peripheral": palette[0],
}
def role_cards(recs):
    return dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(r["role"]),
                        dbc.CardBody(
                            [
                                html.P(f'Reason: {r["reason"]}'),
                                html.P(f'Meaning: {r["meaning"]}'),
                                html.P(f'Target: {r["target"]}')
                            ]
                        )
                    ],
                    style={
                        "borderTop": f"6px solid {ROLE_COLOURS.get(r['role'], '#999')}",
                        "backgroundColor": "rgb(50, 50, 50)",
                        "color": "white",
                        "marginBottom": "20px"
                    },
                    className="shadow-sm"
                ),
                xs=12, sm=12, md=6, lg=4, xl=4
            )
            for r in recs
        ],
        className="g-3"
    )

palette2 = px.colors.qualitative.Set3
LOCAL_ROLE_COLOURS = {
    "Local Ultra-Peripheral": palette2[0],
    "Local Peripheral": palette2[7],
    "Local Connector": palette2[2],
    "Local Kinless": palette2[3],
    "Local Provincial Hub": palette2[4],
    "Local Connector Hub": palette2[5],
    "Local Kinless Hub": palette2[6],
}
def local_role_cards(recs):
    return dbc.Row(
        [
            dbc.Col(
                dbc.Card(
                    [
                        dbc.CardHeader(r["role"]),
                        dbc.CardBody(
                            [
                                html.P(f'Reason: {r["reason"]}'),
                                html.P(f'Meaning: {r["meaning"]}'),
                                html.P(f'Target: {r["target"]}')
                            ]
                        )
                    ],
                    style={
                        "borderTop": f"6px solid {LOCAL_ROLE_COLOURS.get(r['role'], '#999')}",
                        "backgroundColor": "rgb(50, 50, 50)",
                        "color": "white",
                        "marginBottom": "20px"
                    },
                    className="shadow-sm"
                ),
                xs=12, sm=12, md=6, lg=4, xl=4
            )
            for r in recs
        ],
        className="g-3"
    )