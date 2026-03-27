import pandas as pd

def load_data(file_path):
    # Load the edges from the file in the path to a DataFrame
    df = pd.read_csv(file_path, sep=' ', names=['first_node', 'last_node'])

    # Remove duplicate edges (rows)
    df = df.drop_duplicates() 

    # Remove self-loops (edges where 'first_node' == 'last_node')
    # Using boolean indexing to filter out rows where 'first_node' == 'last_node'
    filtered_df = df[df['first_node'] != df['last_node']]

    # Return the filtered DataFrame (edge list)
    return filtered_df