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
        className="ag-theme-quartz-dark",
        rowData=data,
        columnDefs=column_defs,
        defaultColDef={
            "minWidth": 100,
        },
        style={"height": "400px", "width": "100%"},
        dashGridOptions={
            "theme": "legacy",
            "pagination": True,
            "paginationPageSize": 20,
            "rowSelection": {'mode': 'singleRow'},
        },
    )
