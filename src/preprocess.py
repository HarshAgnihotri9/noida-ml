import pandas as pd
import ast

# Load data
df = pd.read_csv("data/properties.csv")

# -------------------------
# BASIC CLEANING
# -------------------------

# Drop rows with very few missing critical values
df.dropna(subset=["sector", "address", "agePossession"], inplace=True)

# Fill categorical nulls
df["society"].fillna("Unknown", inplace=True)
df["additionalRoom"].fillna("None", inplace=True)

# Fill numeric nulls
df["floorNum"].fillna(df["floorNum"].median(), inplace=True)

# -------------------------
# FEATURE ENGINEERING
# -------------------------

# Convert sector to numeric (remove text like 'Sector ')
df["sector"] = df["sector"].astype(str)

# Age possession → numeric age
def extract_age(x):
    if isinstance(x, str):
        digits = "".join([c for c in x if c.isdigit()])
        return int(digits) if digits else 0
    return 0

df["property_age"] = df["agePossession"].apply(extract_age)

# Count nearby locations
def count_list_items(x):
    try:
        return len(ast.literal_eval(x))
    except:
        return 0

df["nearby_count"] = df["nearbyLocations"].apply(count_list_items)
df["furnish_count"] = df["furnishDetails"].apply(count_list_items)
df["feature_count"] = df["features"].apply(count_list_items)

# Drop high-noise columns
df.drop(
    columns=[
        "address",
        "agePossession",
        "nearbyLocations",
        "furnishDetails",
        "features"
    ],
    inplace=True
)

# -------------------------
# FINAL CHECK
# -------------------------

print("Final shape:", df.shape)
print(df.head())
print(df.isnull().sum())
