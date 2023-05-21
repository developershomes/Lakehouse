from deltalake import DeltaTable
from deltalake.writer import write_deltalake
import os
import json
import pandas as pd

delta_table_path = 'deltaTable/'
dt = DeltaTable(delta_table_path) 

# Read Data from Delta table
dt.to_pandas()

# Read Name and Eduction from the delta table 
dt.to_pandas(columns=["Name","Education"])

# Write Data to Delta table 
df = pd.DataFrame({'Name': ['Kalpan'], 'Age': [30], 'Education': 'Engineering'})
write_deltalake(dt, df, mode="append") 

# Read newly inserted Data from Delta table
dt.to_pandas()

# Check history 
dt.history()

# Check Schema of Delta table
dt.schema().json()

# Check files 
dt.files()

# Check versions 
dt.version()

# Load Specific version 
dt.load_version(0)