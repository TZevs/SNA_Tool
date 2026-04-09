import dash_ag_grid as dag

def metrics_table(data, table_id):
    if not data:
        return "No metrics available"

    hidden_cols = {"global_role", "local_role"}

    column_defs = [
        {
            "headerName": col.replace("_", " ").title(),
            "field": col,
            "sortable": True,
            "filter": True,
            "resizable": True,
        }
        for col in data[0].keys()
        if col not in hidden_cols
    ]

    return dag.AgGrid(
        id=table_id,
        rowData=data,
        columnDefs=column_defs,
        defaultColDef={
            "flex": 1,
            "minWidth": 120,
            "cellStyle": {
                "backgroundColor": "rgb(50, 50, 50)",
                "color": "white",
                "fontSize": "14px",
                "padding": "6px",
                "textAlign": "left",
            },
        },
        className="ag-theme-alpine-dark",
        style={"height": "400px", "width": "100%"},
        dashGridOptions={
            "pagination": True,
            "paginationPageSize": 10,
            "rowSelection": {'mode': 'singleRow'}
        },
    )
