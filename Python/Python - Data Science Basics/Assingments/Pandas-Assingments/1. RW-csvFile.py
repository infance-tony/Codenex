import pandas as pd
# Reading a CSV file
df = pd.read_csv('input.csv')  # Replace 'input.csv' with your actual file path
# Display the first few rows
print(df.head())
# Writing to a CSV file
df.to_csv('output.csv', index=False)  # This will create 'output.csv' without the index column