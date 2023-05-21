from deltalake import DeltaTable
from deltalake.writer import write_deltalake
import os
import json
import pandas as pd

delta_table_path = 'sampleTable1/'
dt = DeltaTable(delta_table_path) 

# Read Data from Delta table
dt.to_pandas(columns=["Id","SourceSystemMessageId"])

# Write Data to Delta table 
df = pd.DataFrame({'Id': ['3'], 'SourceSystemMessageId': ['1234']})
write_deltalake(dt, df, mode="append") 

# Read Data from Delta table
dt.to_pandas(columns=["TrainStepId","SourceSystemMessageId"])

# Check history 
dt.history()

# Check files 
dt.files()

# Check versions 
dt.version()

# Check Schema of Delta table
dt.schema().json()

# Load Specific version 
dt.load_version(0)