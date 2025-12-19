import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import zipfile
import urllib.request
import io

# Load the dataset (Student Performance from UCI)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00320/student.zip'
response = urllib.request.urlopen(url)
with zipfile.ZipFile(io.BytesIO(response.read())) as zf:
    with zf.open('student-mat.csv') as f:
        df = pd.read_csv(f, sep=';')

# 1️⃣ Dataset Overview
print("Head:")
print(df.head())
print("\nTail:")
print(df.tail())
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nInfo:")
print(df.info())

# 2️⃣ Data Quality Check
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())
print("\nData types:")
print(df.dtypes)

# 3️⃣ Statistical Summary
print("\nStatistical Summary:")
print(df.describe())
# For specific: mean, median, std, etc. are in describe()

# 4️⃣ Univariate Analysis
# Histograms for numerical columns
numerical_cols = df.select_dtypes(include=[np.number]).columns
for col in numerical_cols:
    plt.figure()
    df[col].hist()
    plt.title(f'Histogram of {col}')
    plt.show()

# Boxplots
for col in numerical_cols:
    plt.figure()
    sns.boxplot(df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()

# Value counts for categorical
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts())

# 5️⃣ Bivariate Analysis
# Scatter plot (example: age vs G3)
plt.figure()
sns.scatterplot(x='age', y='G3', data=df)
plt.title('Scatter plot: Age vs Final Grade')
plt.show()

# Line plot (if applicable, e.g., sorted by age)
plt.figure()
df.sort_values('age')['G3'].plot()
plt.title('Line plot: G3 by Age')
plt.show()

# Group-by comparison (e.g., mean G3 by sex)
print("\nGroup-by mean G3 by sex:")
print(df.groupby('sex')['G3'].mean())

# 6️⃣ Correlation Analysis
corr_matrix = df[numerical_cols].corr()
print("\nCorrelation Matrix:")
print(corr_matrix)
# Heatmap
plt.figure(figsize=(10,8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 7️⃣ Multivariate Analysis
# Pairplot for numerical
sns.pairplot(df[numerical_cols])
plt.show()

# 8️⃣ Outlier Detection
# Boxplots already done
# IQR method
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))]
    print(f"\nOutliers in {col}: {len(outliers)}")

# Z-score
from scipy import stats
for col in numerical_cols:
    z_scores = np.abs(stats.zscore(df[col]))
    outliers_z = df[z_scores > 3]
    print(f"Outliers in {col} (Z>3): {len(outliers_z)}")

# 9️⃣ Categorical Data Analysis
for col in categorical_cols:
    plt.figure()
    sns.countplot(df[col])
    plt.title(f'Count plot of {col}')
    plt.show()

# 🔟 Feature vs Target Analysis
target = 'G3'
# GroupBy mean
print("\nGroupBy mean by categorical features:")
for col in categorical_cols:
    print(f"\n{col}:")
    print(df.groupby(col)[target].mean())

# Boxplot by target (e.g., by sex)
plt.figure()
sns.boxplot(x='sex', y=target, data=df)
plt.title(f'Boxplot of {target} by sex')
plt.show()

# Correlation with target
print("\nCorrelation with target:")
print(df.corr()[target].sort_values(ascending=False))