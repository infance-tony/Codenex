import seaborn as sns

import matplotlib.pyplot as plt

# Load a sample dataset
tips = sns.load_dataset("tips")

# Create a simple scatter plot
sns.scatterplot(data=tips, x="total_bill", y="tip")

# Display the plot
plt.show()