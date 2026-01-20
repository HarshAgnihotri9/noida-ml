import pandas as pd

# Load dataset
df = pd.read_csv("data/messy_customer_sales_data.csv")

# print(df.info())
# print(df.describe())
# print(df.head(10))
# print(df.head())
# print(df.tail())

# print(df.shape)

# print(df.columns)
df['Gender'] = df['Gender'].str.strip().str.lower()
df['Gender'] = df['Gender'].replace({
    'm': 'Male',
    'male': 'Male',
    'f': 'Female',
    'female': 'Female'
})

gender_purchase = df.groupby("Gender")["Purchase_Amount"].sum()
gender_purchase2 = df.groupby("Gender")["Purchase_Amount"].value_counts()

print(gender_purchase)
print('the end')
print(gender_purchase2)




# print(df['Gender'])

# # print(df.head())
# print( df["Gender"].value_counts())




# print( df[df["Country"] == "India"])
# print(df[df["City"] == "CHENNAI"])


# print(df[df["Purchase_Amount"].isnull()])


# print(df[["sector", "society", "rate", "area"]])
# # Basic inspection
# print("Shape of dataset:", df.shape)
# print("\nColumn names:\n", df.columns.tolist())

# print("\nFirst 5 rows:")
# print(df.head())

# print("\nData info:")
# print(df.info())
# print((df['Gender']=='M').sum())

print("\nMissing values:")
# print(df.isnull().sum())

# print((df.isnull().sum()/df.shape[0])*100)
