import pandas as pd

df = pd.read_csv("athlete_events.csv")

# Female athletes over 30
combo_filter = df[(df['Sex'] == 'F') & (df['Age'] > 30)]
print("Female Athletes above 30")
print(combo_filter[['Name', 'Age', 'Sport']].head())

# Male athletes in Basketball
basketball_males = df[(df['Sex'] == 'M') & (df['Sport'] == 'Basketball')]
print("\n\nGuys who Play Basketball")
print(basketball_males.head())

# Aussie Swimmers
aussie_swimmers = df[(df['NOC'] == 'AUS') & (df['Sport'] == 'Swimming')]
print("\n\nAussie Swimmers")
print(aussie_swimmers.head())

