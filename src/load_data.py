import pandas as pd

# Load dataset
df = pd.read_csv("data/properties.csv")

# Basic inspection
print("Shape of dataset:", df.shape)
print("\nColumn names:\n", df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nData info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())
