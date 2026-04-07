import plotly.graph_objects as go
import plotly.express as px
from dash import dcc, html
import dash_cytoscape as cyto

# Role bar chart
def role_bar_chart(data, type):
    if not data:
        return html.P("No role data available")

    # Extract roles
    roles = [role for role in data]

    if not roles:
        return html.P("No role field found")

    fig = px.histogram(
        x=roles,
        color=roles,
        labels={"x": f'{type}', "count": "Count"},
        template="plotly_dark"
    )

    fig.update_layout(
        showlegend=False,
        margin=dict(l=20, r=20, t=40, b=20),
        height=300
    )
    return dcc.Graph(figure=fig)

palette = px.colors.qualitative.Set3
LOCAL_ROLE_COLOURS = {
    "Local Ultra-Peripheral": palette[0],
    "Local Peripheral": palette[7],
    "Local Connector": palette[2],
    "Local Kinless": palette[3],
    "Local Provincial Hub": palette[4],
    "Local Connector Hub": palette[5],
    "Local Kinless Hub": palette[6],
}

def community_graph(data):
    # Lookup metrics by id
    metrics_by_id = {
        m["node"]: m
        for m in data["metrics"]
    }
    node_data = []
    for n in data["nodes"]:
        node_id = n["data"]["id"]
        m = metrics_by_id[node_id]

        node_data.append({
            "data": {
                **n["data"],
                **m
            }
        })

    elements = node_data + data["edges"]

    return cyto.Cytoscape(
        id="community-cyto",
        elements=elements,
        style={"width": "100%", "height": "600px"},
        layout={
            "name": "grid",
            "avoidOverlap": True,
            "avoidOverlapPadding": 8,
        },
        minZoom=0.2,
        stylesheet=[
            {
                "selector": "node:selected",
                "style": {"color": "yellow"}
            },
            {
                "selector": "node",
                "style": {"label": "data(id)"}
            },
            *[
                {
                    "selector": f'[local_role = "{role}"]',
                    "style": {"backgroundColor": colour}
                }
                for role, colour in LOCAL_ROLE_COLOURS.items()
            ]
        ]
    )



