import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Iris dataset from online source
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
df = pd.read_csv(url, header=None, names=column_names)

# Basic Exploratory Data Analysis
print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nStatistical summary:")
print(df.describe())

# Pairplot to visualize relationships
sns.pairplot(df, hue='species')
plt.title('Pairplot of Iris Dataset')
plt.show()

# Boxplot for each feature by species
df.boxplot(by='species', figsize=(10, 6))
plt.suptitle('Boxplot of Features by Species')
plt.show()

# Correlation heatmap for bivariate analysis
corr = df.drop('species', axis=1).corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Numerical Features')
plt.show()

# Summary of what the code has done:
# This script performs basic Exploratory Data Analysis (EDA) on the Iris dataset.
# It loads the dataset from an online source using pandas, assigns column names, and displays initial information.
# Then, it generates a pairplot to visualize relationships between features colored by species using seaborn.
# Next, it creates boxplots for each feature grouped by species to show distributions and outliers.
# Additionally, it displays a correlation heatmap to show bivariate correlations between numerical features.
# How it's been done:
# - Imported necessary libraries: pandas for data handling, matplotlib and seaborn for plotting.
# - Loaded CSV data from URL with specified column names.
# - Used print statements to output dataset head, info, and descriptive statistics.
# - Utilized sns.pairplot for pairwise feature comparisons with hue for species differentiation.
# - Employed pandas boxplot method to create boxplots by species category.
# - Computed correlation matrix for numerical features and visualized it with a heatmap.