from pathlib import Path
import pandas as pd

# Set absolute file path - from current file to processed directory
base_dir = Path(__file__).resolve().parents[2]
data_dir = base_dir / "data" / "processed"

def load_csv(filename: str):
    # Load CSV file
    file_path = data_dir / filename

    # Return empty df if file does not exist
    if not file_path.exists():
        return pd.DataFrame()

    # Read CSV into a DataFrame
    return pd.read_csv(file_path)
