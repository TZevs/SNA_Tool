

def recommend_global_roles(df, global_roles):
    global_recs = {}

    for row in global_roles.itertuples():
        node_recs = []

        if row.global_role == 'Global Hub':
            node_recs.append({

            })
        elif row.global_role == 'Global Broker':
            node_recs.append({

            })
        elif row.global_role == 'Global Core':
            node_recs.append({

            })
        elif row.global_role == 'Global Spreader':
            node_recs.append({

            })
        elif row.global_role == 'Global Peripheral':
            node_recs.append({

            })

    return global_recs

def recommend_local_roles(df, local_roles):
    local_recs = {}

    for row in local_roles.itertuples():
        node_recs = []

        if row.local_role == 'Local Provincial Hub':
            node_recs.append({

            })
        elif row.local_role == 'Local Connector Hub':
            node_recs.append({

            })
        elif row.local_role == 'Local Kinless Hub':
            node_recs.append({

            })
        elif row.local_role == 'Local Peripheral' or row.local_role == 'Local Ultra-Peripheral':
            node_recs.append({

            })
        elif row.local_role == 'Local Connector':
            node_recs.append({

            })
        elif row.local_role == 'Local Kinless':
            node_recs.append({

            })

    return local_recs