import pandas as pd

df = pd.read_csv("athlete_events.csv")
# Filter for female athletes only
female_athletes = df[df['Sex'] == 'F']
print('Females')
print(len(female_athletes.head()))

# Filter for athletes older than 35
older_athletes = df[df['Age'] > 35]
print("Older Athletes")
print(len(older_athletes[['Name', 'Age', 'Sport']].head()))