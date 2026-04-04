from pathlib import Path
import pandas as pd

base_dir = Path(__file__).resolve().parents[2]
data_dir = base_dir / "data" / "processed"

def load_csv(filename: str) -> pd.DataFrame:
    file_path = data_dir / filename
    if not file_path.exists():
        return pd.DataFrame()
    return pd.read_csv(file_path)
