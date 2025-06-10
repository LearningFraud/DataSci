import pandas as pd
df = pd.read_csv("athele_events.csv")
# Assuming your DataFrame is named 'df'
count_x = df['Sports'].value_counts()['x']
  
print(count_x)