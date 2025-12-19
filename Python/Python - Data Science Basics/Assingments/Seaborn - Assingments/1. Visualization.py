import seaborn as sns
import matplotlib.pyplot as plt

# Load sample dataset
df = sns.load_dataset('iris')

# 1. Scatter Plot (Relational)
plt.figure(figsize=(6,4))
sns.scatterplot(data=df, x='sepal_length', y='sepal_width', hue='species')
plt.title('Scatter Plot')
plt.show()

# 2. Line Plot (Relational)
plt.figure(figsize=(6,4))
sns.lineplot(data=df, x='sepal_length', y='sepal_width')
plt.title('Line Plot')
plt.show()

# 3. Bar Plot (Categorical)
plt.figure(figsize=(6,4))
sns.barplot(data=df, x='species', y='sepal_length')
plt.title('Bar Plot')
plt.show()

# 4. Box Plot (Categorical)
plt.figure(figsize=(6,4))
sns.boxplot(data=df, x='species', y='sepal_length')
plt.title('Box Plot')
plt.show()

# 5. Violin Plot (Categorical)
plt.figure(figsize=(6,4))
sns.violinplot(data=df, x='species', y='sepal_length')
plt.title('Violin Plot')
plt.show()

# 6. Histogram (Distribution)
plt.figure(figsize=(6,4))
sns.histplot(data=df, x='sepal_length', kde=True)
plt.title('Histogram')
plt.show()

# 7. KDE Plot (Distribution)
plt.figure(figsize=(6,4))
sns.kdeplot(data=df, x='sepal_length', hue='species')
plt.title('KDE Plot')
plt.show()

# 8. Heatmap (Matrix)
plt.figure(figsize=(6,4))
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heatmap')
plt.show()