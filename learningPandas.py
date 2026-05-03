import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(df.head())
print(df.tail())
print(df.dtypes)
print(df.describe())

print(df[['Name', 'Sex', 'Age']])