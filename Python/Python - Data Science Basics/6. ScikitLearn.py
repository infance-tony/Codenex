import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data: X (features), y (target)
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Make a prediction
prediction = model.predict([[6]])
print(f"Prediction for X=6: {prediction[0]}")