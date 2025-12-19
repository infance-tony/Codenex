import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the car sales dataset from online source
url = 'https://raw.githubusercontent.com/amankharwal/Website-data/master/car%20data.csv'
df = pd.read_csv(url)

# Display basic information
print("First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nDescriptive statistics:")
print(df.describe())

# Select numeric columns for correlation
numeric_df = df.select_dtypes(include=[np.number])

# Correlation matrix
print("\nCorrelation matrix:")
corr = numeric_df.corr()
print(corr)

# Heatmap for correlation
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Simple visualizations
plt.figure(figsize=(10, 6))
sns.histplot(df['Selling_Price'], bins=50, kde=True)
plt.title('Distribution of Selling Price')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='Kms_Driven', y='Selling_Price', data=df)
plt.title('Selling Price vs KM Driven')
plt.show()