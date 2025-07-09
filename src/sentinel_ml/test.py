import pandas as pd
from pathlib import Path

current_file = Path(__file__).resolve()
project_root = current_file.parents[2]
df = pd.read_csv(f"{project_root}/data/HDFS_100k.log_structured.csv")

print(df.head())
