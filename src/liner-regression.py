# import pandas as pd;
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split


# pd.read_csv('/properties.csv')

import pandas as pd

# URL to the Auto MPG dataset (Check for the latest URL or availability on the UCI repository)
url = "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data"

# Column names based on the dataset description
column_names = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model_year', 'origin', 'car_name']

# Read the dataset from the URL
# Note: The dataset uses various delimiters and contains missing values denoted as '?'
df = pd.read_csv(
    url,
    sep=r'\s+',
    names=column_names,
    na_values='?',
    comment='\t'
)


# Display the first few rows of the dataframe
# df.head()
# print(df.head())
# df.info()
# df.discription()
# print((df.isnull().sum()/df.shape[0])*100)
print((df.isnull()))
