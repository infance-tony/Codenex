import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Step 1: Load the dataset
# For demonstration, creating sample data
np.random.seed(42)
data = {
    'ApplicantIncome': np.random.randint(2000, 10000, 100),
    'CoapplicantIncome': np.random.randint(0, 5000, 100),
    'LoanAmount': np.random.randint(50, 500, 100),
    'Loan_Status': np.random.choice([0,1], 100),
    'Gender': np.random.choice(['Male', 'Female'], 100),
    'Married': np.random.choice(['Yes', 'No'], 100),
    'Education': np.random.choice(['Graduate', 'Not Graduate'], 100),
    'Self_Employed': np.random.choice(['Yes', 'No'], 100),
    'Property_Area': np.random.choice(['Urban', 'Semiurban', 'Rural'], 100),
    'Credit_History': np.random.choice([0,1], 100)
}
df = pd.DataFrame(data)

# Step 2: Understand the data structure
print("Step 2: Data Overview")
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# Step 3: Handle missing values
print("\nStep 3: Missing Values")
print(df.isnull().sum())
# Fill missing values (example: mean for numerical, mode for categorical)
for col in df.columns:
    if df[col].dtype == 'object':
        df[col].fillna(df[col].mode()[0], inplace=True)
    else:
        df[col].fillna(df[col].mean(), inplace=True)

# Step 4: Data types and encoding
print("\nStep 4: Data Types")
le = LabelEncoder()
for col in df.select_dtypes(include=['object']):
    df[col] = le.fit_transform(df[col])

# Step 5: Univariate Analysis
print("\nStep 5: Univariate Analysis")
for col in df.columns:
    if df[col].dtype != 'object':
        plt.figure(figsize=(6,4))
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.show()
        print(f"Interpretation: {col} has a mean of {df[col].mean():.2f} and std of {df[col].std():.2f}")

# Step 6: Bivariate Analysis
print("\nStep 6: Bivariate Analysis")
# Assuming target is 'Loan_Status' (0 or 1)
target = 'Loan_Status'  # Adjust if different
for col in df.columns:
    if col != target and df[col].dtype != 'object':
        plt.figure(figsize=(6,4))
        sns.boxplot(x=target, y=col, data=df)
        plt.title(f'{col} vs {target}')
        plt.show()
        print(f"Interpretation: Higher {col} seems associated with {target}")

# Step 7: Multivariate Analysis
print("\nStep 7: Multivariate Analysis")
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
print("Interpretation: Correlation shows relationships between features")

# Step 8: Outlier Detection
print("\nStep 8: Outlier Detection")
for col in df.select_dtypes(include=[np.number]):
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = ((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR))).sum()
    print(f"{col}: {outliers} outliers")

# Step 9: Feature Engineering
print("\nStep 9: Feature Engineering")
# Example: Create new feature
df['Total_Income'] = df['ApplicantIncome'] + df['CoapplicantIncome']  # Assuming columns exist
print("Added Total_Income feature")

# Step 10: Summary and Insights
print("\nStep 10: Summary")
print("EDA completed. Key insights: [Summarize based on visualizations]")
# Example: "Loan approval is higher for higher income groups."