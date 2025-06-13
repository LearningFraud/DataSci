import pandas as pd 

df = pd.read_csv("athlete_events.csv")

# Count participants in each sport
sport_counts = df['Sport'].value_counts()
print(sport_counts.head())

# Count medals per team
medals_by_team = df[df['Medal'].notnull()].groupby('Team')['Medal'].count()
print(medals_by_team.sort_values(ascending=False).head())

female_participants_by_sport = df.groupby("Sport")["Sex" == "Female"].head(10)