"""
Append data to an existing Parquet file.
"""

import pyarrow.parquet as pq
import pyarrow as pa

existing_table = pq.read_table('tmp/data.parquet')

new_data = pd.DataFrame({
    "Name": ["David", "Emma"],
    "Age": [40, 28],
    "City": ["San Francisco", "Seattle"]
})

new_table = pa.Table.from_pandas(new_data)

