import pandas as pd

df = pd.read_csv("data.csv")

print("branch version")
print(df.describe())