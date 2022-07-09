import json
import os
import pandas as pd
with open(os.path.join("assets/ventas.json")) as file:
        data = json.load(file)

df = pd.DataFrame(data)
df['date_closed'] = pd.to_datetime(df['date_closed'], format='%Y-%m-%d %H:%M:%S').dt.to_period('W').dt.to_timestamp()
print(df.head())