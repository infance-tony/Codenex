import pandas as pd

# Create a sample DataFrame
marksUT= {'Name':['Raman','Raman','Raman','Zuhaire','Zuhaire','Zuhaire', 'Ashravy','Ashravy','Ashravy','Mishti','Mishti','Mishti'],
            'UT':[1,2,3,1,2,3,1,2,3,1,2,3],
            'Maths':[22,21,14,20,23,22,23,24,12,15,18,17],
            'Science':[21,20,19,17,15,18,19,22,25,22,21,18],
            'S.St':[18,17,15,22,21,19,20,24,19,25,25,20],
            'Hindi':[20,22,24,24,25,23,15,17,21,22,24,25],
            'Eng':[21,24,23,19,15,13,22,21,23,22,23,20] }
df = pd.DataFrame(marksUT)

# Statistical operations
print("DataFrame:")
print(df)
print("\nMean:")
print(df.mean(numeric_only=True))
print("\nRow Mean:")
print(df.select_dtypes(include='number').mean(axis=1))
print("\nRow Sum:")
print(df.select_dtypes(include='number').sum(axis=1))
print("\nSum:")
print(df.sum(numeric_only=True))
print("\nRow Mode:")
print(df.mode(axis=1))
print("\nMode:")
print(df.mode(numeric_only=True))
print("\nRow Median:")
print(df.median(axis=1))
print("\nRow Standard Deviation:")
print(df.std(axis=1))
print("\nMedian:")
print(df.median(numeric_only=True))
print("\nRow Variance:")
print(df.var(axis=1))
print("\nStandard Deviation:")
print(df.std(numeric_only=True))
print("\nRow Min:")
print(df.min(axis=1))
print("\nRow Max:")
print(df.max(axis=1))
print("\nVariance:")
print(df.var(numeric_only=True))
print("\nMin:")
print(df.min(numeric_only=True))
print("\nMax:")
print(df.max(numeric_only=True))
print("\nDescribe:")
print(df.describe(include='number'))
print("\nInfo:")
print(df.info())

# Handling missing values
# Introduce some missing values for demonstration
import numpy as np
df.loc[0, 'Maths'] = np.nan
df.loc[1, 'Science'] = np.nan

print("\nDataFrame with missing values:")
print(df)

# Check for missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# Drop rows with missing values
df_dropped = df.dropna()
print("\nDataFrame after dropping missing values:")
print(df_dropped)

# Fill missing values with mean
df_filled = df.fillna(df.mean(numeric_only=True))
print("\nDataFrame after filling missing values with mean:")
print(df_filled)