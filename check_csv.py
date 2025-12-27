import pandas as pd

csv_url = "https://raw.githubusercontent.com/binorassocies/rimdata/refs/heads/main/data/results_elections_rim_2019-2024.csv"
df = pd.read_csv(csv_url)

print("COLUMNS:", list(df.columns))
print(df.head(2))
