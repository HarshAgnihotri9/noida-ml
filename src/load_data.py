import pandas as pd

# Load dataset
df = pd.read_csv("data/properties.csv")

# print(df.info())
# print(df.describe())
# print(df.head(10))
# print(df.head())
# print(df.tail())

# print(df.shape)

print(df.columns)

print(df.info())

print(df[["sector", "society", "rate", "area"]])
# # Basic inspection
# print("Shape of dataset:", df.shape)
# print("\nColumn names:\n", df.columns.tolist())

# print("\nFirst 5 rows:")
# print(df.head())

# print("\nData info:")
# print(df.info())

print("\nMissing values:")
# print(df.isnull().sum())

# print((df.isnull().sum()/df.shape[0])*100)
