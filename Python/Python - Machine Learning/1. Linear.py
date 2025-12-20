import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
dataset = pd.read_csv("https://raw.githubusercontent.com/ybifoundation/Dataset/main/Salary%20Data.csv")

# Display the first few rows of the dataset
print("Dataset Preview:\n", dataset.head())

# Check for missing values
print("\nMissing Values:\n", dataset.isnull().sum())

# Assume dataset has 'YearsExperience' as feature and 'Salary' as target
X = dataset.iloc[:, :-1].values  # Independent variable (Years of Experience)
y = dataset.iloc[:, -1].values   # Dependent variable (Salary)

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict on the test set
y_pred = regressor.predict(X_test)
y1=regressor.predict([[60000]])
print(y1)


# Print model coefficients
print("\nModel Coefficients:")
print("Intercept:", regressor.intercept_)
print("Slope:", regressor.coef_[0])

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print("\nMean Squared Error:", mse)

# Visualizing the training set results
plt.scatter(X_train, y_train, color='red', label='Actual')
plt.plot(X_train, regressor.predict(X_train), color='blue', label='Regression Line')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()

# Visualizing the test set results
plt.scatter(X_test, y_test, color='green', label='Actual')
plt.plot(X_train, regressor.predict(X_train), color='blue', label='Regression Line')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.legend()
plt.show()
