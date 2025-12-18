import tensorflow as tf
import numpy as np

# Simple TensorFlow example: Creating constants and performing basic operations
a = tf.constant(5.0)
b = tf.constant(3.0)
c = a + b

print("Result of a + b:", c.numpy())

# Example of a simple linear regression model

# Generate some sample data
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)  # y = 2*X

# Define a simple model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compile the model
model.compile(optimizer='sgd', loss='mean_squared_error')

# Train the model
model.fit(X, y, epochs=100, verbose=0)

# Make a prediction
prediction = model.predict([6])
print("Prediction for X=6:", prediction[0][0])