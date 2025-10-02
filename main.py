import pandas as pd
import json

# Dummy JSON data
data_json = '''
[
    {"name": "Alice", "age": 25, "city": "Pune"},
    {"name": "Bob", "age": 30, "city": "Mumbai"},
    {"name": "Charlie", "age": 28, "city": "Delhi"}
]
'''

# Convert JSON string to Python object
data = json.loads(data_json)

# Convert to DataFrame
df = pd.DataFrame(data)

# Append a new row (dummy entry)
df.loc[len(df)] = {"name": "David", "age": 35, "city": "Bangalore"}

# Print DataFrame
print(df)

# Save as CSV for DVC tracking
df.to_csv("people.csv", index=False)
