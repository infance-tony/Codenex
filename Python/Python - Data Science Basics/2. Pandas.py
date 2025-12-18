import pandas as pd
import numpy as np

# Creating DataFrames
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': ['a', 'b', 'c', 'd'],
    'C': [1.1, 2.2, 3.3, 4.4]
})

# Reading data
# df = pd.read_csv('file.csv')  # Example for CSV
# df = pd.read_excel('file.xlsx')  # Example for Excel

# Basic operations
print(df.head())  # First 5 rows
print(df.tail())  # Last 5 rows
print(df.info())  # DataFrame info
print(df.describe())  # Statistical summary

# Selecting data
print(df['A'])  # Column selection
print(df.loc[0])  # Row by label
print(df.iloc[0])  # Row by index
print(df[df['A'] > 2])  # Filtering

# Data manipulation
df['D'] = df['A'] * 2  # Adding column
df = df.drop('B', axis=1)  # Dropping column
df = df.rename(columns={'A': 'Alpha'})  # Renaming columns
df = df.sort_values('Alpha')  # Sorting

# Handling missing data
df.loc[0, 'C'] = np.nan  # Introduce NaN
print(df.isnull())  # Check for NaN
df = df.fillna(0)  # Fill NaN
df = df.dropna()  # Drop NaN

# Grouping and aggregation
grouped = df.groupby('Alpha').sum()  # Group by and sum
print(grouped)

# Merging and joining
df2 = pd.DataFrame({'Alpha': [1, 2], 'E': [5, 6]})
merged = pd.merge(df, df2, on='Alpha')  # Merge
print(merged)

# Pivoting
pivot = df.pivot_table(values='C', index='Alpha', aggfunc='mean')  # Pivot table
print(pivot)

# Time series (if applicable)
# df['date'] = pd.to_datetime(df['date'])
# df.set_index('date', inplace=True)
# print(df.resample('M').mean())  # Resample

# Exporting data
# df.to_csv('output.csv', index=False)  # To CSV
# df.to_excel('output.xlsx', index=False)  # To Excel

# Other functions: apply, map, transform, etc. (examples)
df['F'] = df['Alpha'].apply(lambda x: x**2)  # Apply function
print(df)
