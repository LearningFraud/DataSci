import pandas as pd

df = pd.read_csv("athlete_events.csv")

# Sort by age
sorted_by_height = df.sort_values(by='Height', ascending=False)

# Sort by weight
sorted_by_weight = sorted_by_height.sort_values(by='Weight', ascending=False)
print(sorted_by_weight[['Name', 'Weight', 'Sport']].head(10))