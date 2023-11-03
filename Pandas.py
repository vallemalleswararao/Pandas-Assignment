import pandas as pd

# Import the dataset
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users = pd.read_csv(url, sep='|', index_col='user_id')

# Number of observations and columns
print("Number of Observations:", users.shape[0])
print("Number of Columns:", users.shape[1])

# Column names
print("Columns:", users.columns)

# Index type
print("Index:", users.index)

# Data types of columns
print("Data types:\n", users.dtypes)

# Print only the 'occupation' column
print(users['occupation'])

# Number of different occupations
print("Number of different occupations:", users['occupation'].nunique())

# Most frequent occupation
print("Most frequent occupation:\n", users['occupation'].mode())

# DataFrame info
print(users.info())

# Describe all the columns
print(users.describe())

# Summarize only the 'occupation' column
print(users['occupation'].value_counts())

# Mean age of users
print("Mean age of users:", users['age'].mean())

# Age with least occurrence
print("Age with least occurrence:", users['age'].value_counts().idxmin())
