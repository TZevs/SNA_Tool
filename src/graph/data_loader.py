import pandas as pd

def load_data(file_path):
    # Load the edges from the file in the path to a DataFrame
    df = pd.read_csv(file_path, sep=' ', names=['source', 'target'])

    # Remove duplicate edges (rows)
    df = df.drop_duplicates() 

    # Remove self-loops (edges where 'source' == 'target')
    # Using boolean indexing to filter out rows where 'source' == 'target'
    edge_df = df[df['source'] != df['target']]

    # Return the filtered DataFrame (edge list)
    return edge_df