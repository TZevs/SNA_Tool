import pandas as pd

def recommend_local_roles(local_roles):
    local_recs = {}

    for row in local_roles.itertuples():
        if row.local_role == 'Local Provincial Hub':
            local_recs[row.node] = {
                'reason': 'Has many connections within the ' + row.community + ' community.',
                'meaning': 'Acts as a local leader or anchor, a central user in the community.',
                'target': 'To coordinate the ' + row.community + ' community.'
            }
        elif row.local_role == 'Local Connector Hub':
            local_recs[row.node] = {
                'reason': 'Has many connections and connects several sub-groups within the ' + row.community + ' community.',
                'meaning': 'Works like an internal bridge between the ' + row.community + ' community sub-groups.',
                'target': "To improve " + row.community + "'s internal communication and information flow."
            }
        elif row.local_role == 'Local Kinless Hub':
            local_recs[row.node] = {
                'reason': 'Has many connections to several communities outside of ' + row.community + '.',
                'meaning': 'Acts as a hub across the connected communities.',
                'target': 'To improve cross-community connections and communication for better information flow.'
            }
        elif row.local_role == 'Local Peripheral' or row.local_role == 'Local Ultra-Peripheral':
            local_recs[row.node] = {
                'reason': 'Has few internal connections and limited engagement within ' + row.community + ' community.',
                'meaning': 'Is locally isolated within ' + row.community + ' community.',
                'target': 'To support local inclusion and re-engagement.'
            }
        elif row.local_role == 'Local Connector':
            local_recs[row.node] = {
                'reason': 'Links to different parts of the ' + row.community + ' community.',
                'meaning': 'Acts as a local bridge that provides internal connections for better information flow.',
                'target': 'To improve internal information flow efficiency for ' + row.community + ' community.'
            }
        elif row.local_role == 'Local Kinless':
            local_recs[row.node] = {
                'reason': 'Has weak internal links but has many cross-community connections.',
                'meaning': 'An outsider in the ' + row.community + ' community but can reach many other communities.',
                'target': 'To build stronger links and bridges to other communities.'
            }

    df = pd.DataFrame.from_dict(local_recs, orient='index').reset_index()
    df = df.rename(columns={'index': 'node'})

    return df