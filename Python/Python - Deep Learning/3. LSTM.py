import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout

# -------------------------------------------
# Load dataset
# -------------------------------------------
df = pd.read_csv("rain_data.csv")  # your CSV file

features = ["Temperature", "Humidity", "WindSpeed", "Pressure"]
target = "Rain"

X = df[features].values
y = df[target].values

# -------------------------------------------
# Normalize data
# -------------------------------------------
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# -------------------------------------------
# LSTM expects 3D Input → (samples, timesteps, features)
# Here we use timestep = 1
# -------------------------------------------
X_lstm = X_scaled.reshape((X_scaled.shape[0], 1, X_scaled.shape[1]))

# -------------------------------------------
# Train-Test Split
# -------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_lstm, y, test_size=0.2, random_state=42
)

# -------------------------------------------
# Build LSTM Model
# -------------------------------------------
model = Sequential([
    LSTM(64, return_sequences=False, input_shape=(1, len(features))),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(1, activation='sigmoid')    # binary output
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# -------------------------------------------
# Train
# -------------------------------------------
history = model.fit(
    X_train, y_train,
    epochs=30,
    batch_size=16,
    validation_split=0.2
)

# -------------------------------------------
# Evaluate
# -------------------------------------------
loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)

# -------------------------------------------
# Prediction Example
# -------------------------------------------
sample = np.array([[30, 80, 10, 1005]])  # temp, humidity, wind, pressure
sample_scaled = scaler.transform(sample)
sample_lstm = sample_scaled.reshape((1, 1, 4))

pred = model.predict(sample_lstm)
print("\nRain Probability:", pred[0][0])
print("Rain Prediction:", "Rain" if pred[0][0] > 0.5 else "No Rain")
