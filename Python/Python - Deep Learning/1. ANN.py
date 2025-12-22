# -------------------------------------------------
# ANN MODEL FOR MOBILE PRICE PREDICTION (CSV)
# -------------------------------------------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# -------------------------------------------------
# 1. Load CSV
# -------------------------------------------------
df = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/mobile_prices.csv")

print("Data Loaded Successfully!")
print(df.head())

# -------------------------------------------------
# 2. Split into Features & Labels
# -------------------------------------------------
X = df.drop("price", axis=1)
y = df["price"]

# -------------------------------------------------
# 3. Train-Test Split
# -------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------------------------
# 4. Feature Scaling (VERY IMPORTANT)
# -------------------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -------------------------------------------------
# 5. Build ANN Model
# -------------------------------------------------
model = Sequential([
    Dense(64, activation='relu', input_shape=(X_train_scaled.shape[1],)),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(1)   # Regression output
])

model.compile(optimizer='adam', loss='mse', metrics=['mae'])

model.summary()

# -------------------------------------------------
# 6. Train model
# -------------------------------------------------
history = model.fit(
    X_train_scaled, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2
)

# -------------------------------------------------
# 7. Evaluate
# -------------------------------------------------
loss, mae = model.evaluate(X_test_scaled, y_test)
print("MAE:", mae)

# -------------------------------------------------
# 8. Predict with new data
# -------------------------------------------------
sample = np.array([[1200, 6, 165, 64, 4, 800, 1500]])  # example input
sample_scaled = scaler.transform(sample)

pred_price = model.predict(sample_scaled)
print("Predicted Price:", pred_price[0][0])
