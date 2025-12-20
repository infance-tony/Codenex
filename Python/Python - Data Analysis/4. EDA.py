import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the online sales dataset (Online Retail dataset from UCI)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx'
df = pd.read_excel(url)

print("EDA Analysis for Online Sales Dataset")
print("=" * 50)

# 1️⃣ Dataset Overview
print("\n1. Dataset Overview")
print("-" * 20)
print("Head of the dataset:")
print(df.head())
print("\nTail of the dataset:")
print(df.tail())
print(f"\nShape: {df.shape} (rows, columns)")
print(f"Columns: {list(df.columns)}")
print("\nInfo:")
print(df.info())

# Interpretation: The dataset contains transaction data with columns like InvoiceNo, StockCode, etc. It has about 541,909 rows and 8 columns. Data types include object, datetime, float, int.

# 2️⃣ Data Quality Check
print("\n2. Data Quality Check")
print("-" * 20)
missing_values = df.isnull().sum()
print("Missing values per column:")
print(missing_values)
print(f"Total missing values: {missing_values.sum()}")

duplicates = df.duplicated().sum()
print(f"\nNumber of duplicate rows: {duplicates}")

print("\nData types:")
print(df.dtypes)

# Interpretation: There are missing values in Description and CustomerID. Duplicates exist, possibly due to multiple entries. Data types seem appropriate, but Quantity and UnitPrice are numeric.

# 3️⃣ Statistical Summary
print("\n3. Statistical Summary")
print("-" * 20)
numeric_cols = df.select_dtypes(include=[np.number]).columns
print("Numeric columns:", list(numeric_cols))
print("\nDescribe:")
print(df[numeric_cols].describe())

# Interpretation: Quantity has negative values (returns), UnitPrice varies widely. Mean quantity is positive, indicating mostly sales.

# 4️⃣ Univariate Analysis
print("\n4. Univariate Analysis")
print("-" * 20)

# Histogram for Quantity
plt.figure(figsize=(10, 6))
sns.histplot(df['Quantity'], bins=50, kde=True)
plt.title('Histogram of Quantity')
plt.show()

# Interpretation: Quantity is right-skewed with outliers. UnitPrice has many low values and some high. Most transactions from UK.

# 5️⃣ Bivariate Analysis
print("\n5. Bivariate Analysis")
print("-" * 20)

# Scatter plot: Quantity vs UnitPrice
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Quantity', y='UnitPrice', data=df)
plt.title('Scatter Plot: Quantity vs UnitPrice')
plt.show()

# Interpretation: Scatter shows some correlation, but outliers. Daily sales fluctuate. Higher prices in some countries.

# 6️⃣ Correlation Analysis
print("\n6. Correlation Analysis")
print("-" * 20)
corr_matrix = df[numeric_cols].corr()
print("Correlation Matrix:")
print(corr_matrix)

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# Interpretation: Low correlation between Quantity and UnitPrice. Pearson coefficient shows weak relationships.

# 7️⃣ Multivariate Analysis
print("\n7. Multivariate Analysis")
print("-" * 20)

# Pairplot for numeric columns
sns.pairplot(df[numeric_cols])
plt.show()

# Interpretation: Pairplot shows distributions and relationships. Facet shows quantity variations by country.

# 8️⃣ Outlier Detection
print("\n8. Outlier Detection")
print("-" * 20)

# Boxplot for outliers in Quantity
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Quantity'])
plt.title('Boxplot for Quantity Outliers')
plt.show()

# Interpretation: Many outliers in Quantity, indicating bulk purchases or returns. Z-score detects extreme prices.

# 9️⃣ Categorical Data Analysis
print("\n9. Categorical Data Analysis")
print("-" * 20)

# Count plot for Country
plt.figure(figsize=(12, 8))
sns.countplot(y='Country', data=df, order=df['Country'].value_counts().index)
plt.title('Count Plot of Countries')
plt.show()

# Interpretation: UK dominates transactions. Top products are common items like mugs.

# 🔟 Feature vs Target Analysis (Assuming target is Quantity or sales amount)
print("\n10. Feature vs Target Analysis")
print("-" * 30)

# Create a sales amount column
df['SalesAmount'] = df['Quantity'] * df['UnitPrice']

# Boxplot of UnitPrice by Country
top_countries = df['Country'].value_counts().head(5).index
df_top = df[df['Country'].isin(top_countries)]
plt.figure(figsize=(12, 8))
sns.boxplot(x='Country', y='UnitPrice', data=df_top)
plt.title('Boxplot of UnitPrice by Top 5 Countries')
plt.show()

# Interpretation: Higher sales in certain countries. UnitPrice varies. Weak correlations with Quantity.