# import pandas as pd

# df = pd.read_parquet("tmp/data.parquet", engine="pyarrow")

import pyarrow.parquet as pq

table = pq.read_table("tmp/data.parquet")

df = table.to_pandas()

pass