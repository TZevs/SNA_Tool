import pandas as pd

def recommend_local_roles():
    local_recs = {}

    local_recs['Local Provincial Hub'] = {
        'reason': 'Has many connections within the community.',
        'meaning': 'Acts as a local leader or anchor, a central user in the community.',
        'target': 'To coordinate the community.'
    }
    local_recs['Local Connector Hub'] = {
        'reason': 'Has many connections and connects several sub-groups within the community.',
        'meaning': 'Works like an internal bridge between the community sub-groups.',
        'target': "To improve the community's internal communication and information flow."
    }
    local_recs['Local Kinless Hub'] = {
        'reason': 'Has many connections to several communities outside of community.',
        'meaning': 'Acts as a hub across the connected communities.',
        'target': 'To improve cross-community connections and communication for better information flow.'
    }
    local_recs['Local Peripheral'] = {
        'reason': 'Has few internal connections and limited engagement within the community.',
        'meaning': 'Is locally isolated within the community.',
        'target': 'To support local inclusion and re-engagement.'
    }
    local_recs['Local Connector'] = {
        'reason': 'Links to different parts of the community.',
        'meaning': 'Acts as a local bridge that provides internal connections for better information flow.',
        'target': 'To improve internal information flow efficiency for the community.'
    }
    local_recs['Local Kinless'] = {
        'reason': 'Has weak internal links but has many cross-community connections.',
        'meaning': 'An outsider in the community but can reach many other communities.',
        'target': 'To build stronger links and bridges to other communities.'
    }

    df = pd.DataFrame.from_dict(local_recs, orient='index').reset_index()
    df = df.rename(columns={'index': 'role'})

    return df