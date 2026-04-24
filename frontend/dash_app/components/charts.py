import plotly.graph_objects as go
import plotly.express as px
from dash import dcc, html
import dash_cytoscape as cyto
import pandas as pd

global_palette = {
    "Global Peripheral": "#0d6efd",
    "Global Core": "#00d4ff",
    "Global Spreader": "#2ecc71",
    "Global Hub": "#f1c40f",
    "Global Broker": "#e83e8c"
}

local_palette = {
    "Local Ultra-Peripheral": "#20c997",
    "Local Peripheral": "#6f42c1",
    "Local Connector": "#ff6b6b",
    "Local Kinless": "#4dabf7",
    "Local Provincial Hub": "#3ddc97",
    "Local Connector Hub": "#fd7e14",
    "Local Kinless Hub": "#adb5bd",
}

# Role bar chart
def role_bar_chart(data, type):
    if not data:
        return html.P("No role data available")

    # Extract roles
    roles = [role for role in data]

    if not roles:
        return html.P("No role field found")

    palette = global_palette if type == "global_role" else local_palette

    fig = px.histogram(
        x=roles,
        color=roles,
        #labels={"x": f'{type}', "count": "Count"},
        #template="plotly_dark",
        color_discrete_map=palette,
    )

    fig.update_layout(
        showlegend=False,
        margin=dict(l=20, r=20, t=40, b=20),
        height=300,
        title=f'Role Distribution ({type}s)',
        xaxis_title="Global Roles" if type == "global_role" else "Local Roles",
        yaxis_title='Count',
    )
    return dcc.Graph(figure=fig)

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
        layout={
            "name": "cose",
            "avoidOverlap": True,
            "avoidOverlapPadding": 20,
            "idealEdgeLength": 200,
            "nodeRepulsion": 500000,
            "gravity": 80,
        },
        stylesheet=[
            {
                "selector": "node",
                "style": {"content": "data(id)"}
            },
            {
                "selector": "edge",
                'style': {
                    'width': 0.3,        # ultra‑thin
                    'line-color': '#999',
                }
            },
            *[
                {
                    "selector": f'[local_role = "{role}"]',
                    "style": {"background-color": colour}
                }
                for role, colour in local_palette.items()
            ]
        ],
        style={"width": "100%", "height": "600px", "background-color": "white"},
        minZoom=0.2,

    )

def global_degree_hist(data):
    df = pd.DataFrame(data)

    fig = px.histogram(
        df,
        x='degree',
        color='community',
        barmode="overlay",
        opacity=0.65,
        height=400,
        color_discrete_sequence=px.colors.qualitative.Prism,
    )
    fig.update_layout(
        title='Normalised Degree Distribution By Community',
        xaxis_title='Normalised Degree (0-1)',
        yaxis_title='Count',
        legend_title='Community',
    )
    fig.update_xaxes(range=[0, 0.1])
    
    return dcc.Graph(figure=fig)


def global_degree_hist_without_comm(data):
    df = pd.DataFrame(data)

    fig = px.histogram(
        df,
        x='degree',
        color_discrete_sequence=px.colors.qualitative.Prism,
        height=400,
    )
    fig.update_layout(
        title='Normalised Degree Distribution',
        xaxis_title='Normalised Degree (0-1)',
        yaxis_title='Count',
    )
    fig.update_xaxes(range=[0, 0.1])

    return dcc.Graph(figure=fig)

