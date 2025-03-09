import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)

table = pa.Table.from_pandas(df)

pq.write_table(table, "tmp/data-pa.parquet")

# df.to_parquet("tmp/data.parquet", engine="pyarrow", index=False)

print("Parquet file written successfully!")
