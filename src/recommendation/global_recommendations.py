import pandas as pd

def recommend_global_roles():
    global_recs = {}

    global_recs['Global Hub'] = {
        'reason': 'Has many direct links and is linked to other highly connected or influential nodes.',
        'meaning': 'Popular node, anchors global connectivity and acts as a central access point for information.',
        'target': 'To ensure information and or resources reach large sections of the network efficiently.'
    }
    global_recs['Global Broker'] = {
        'reason': 'Sits on many shortest paths between users.',
        'meaning': 'Acts as a bridge between otherwise disconnected sections of the network.',
        'target': 'To enable cross-community connection communication, reduce risk of network disconnection.'
    }
    global_recs['Global Core'] = {
        'reason': 'Is deeply embedded in the main structure of the network.',
        'meaning': 'Forms part of the structural spine that provides network stability.',
        'target': 'To support long-term influence over the network.'
    }
    global_recs['Global Spreader'] = {
        'reason': 'Sits within the high k-shells of the network.',
        'meaning': 'Provides efficient reach without being in the main core.',
        'target': 'To enable fast and wide spread of information and resources.'
    }
    global_recs['Global Peripheral'] = {
        'reason': 'Sits in the outer shells of the network.',
        'meaning': 'Weakly connected and isolated in the global structure, with limited access to information.',
        'target': 'For inclusion and re-engagement.'
    }
    df = pd.DataFrame.from_dict(global_recs, orient='index')
    df = df.rename(columns={'index': 'global_role'})

    return df