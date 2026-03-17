import pandas as pd
import os

def load_data():
    base_dir = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base_dir, "data", "healthcare.csv")

    df = pd.read_csv(path)

    df.columns = df.columns.str.strip().str.replace(" ", "_")

    return df