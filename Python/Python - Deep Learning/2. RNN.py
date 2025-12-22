import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("sentiment_dataset.csv")  # contains text, label

texts = df['text'].astype(str).tolist()
labels = df['label'].tolist()

# Tokenization
tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# Padding
max_len = 20
padded = pad_sequences(sequences, maxlen=max_len, padding='post')

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    padded, labels, test_size=0.2, random_state=42
)

# Convert labels to numpy array (IMPORTANT)
y_train = np.array(y_train)
y_test = np.array(y_test)

# Build RNN Model
model = Sequential([
    Embedding(input_dim=5000, output_dim=64, input_length=max_len),
    SimpleRNN(64),
    Dense(1, activation='sigmoid')
])

model.compile(
    loss='binary_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
)

# Train model
model.fit(X_train, y_train, epochs=5, batch_size=4, validation_split=0.2)

# Evaluate
loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)
sentences = [
    "I really enjoyed this movie",
    "It was a horrible experience",
    "The service was excellent",
    "I am not happy with this product",
    "Absolutely wonderful and satisfying",
    "This is the worst thing ever",
    "I love the quality",
    "Totally not worth it",
    "Very impressive performance",
    "I will never recommend this"
]

# Convert to sequences
seqs = tokenizer.texts_to_sequences(sentences)
pads = pad_sequences(seqs, maxlen=max_len)

# Predict
preds = model.predict(pads)

print("\n===== Sentiment Predictions =====")
for sentence, pred in zip(sentences, preds):
    sentiment = "Positive 😊" if pred[0] > 0.5 else "Negative 😡"
    print(f"{sentence} --> {sentiment}  (score={pred[0]:.4f})")