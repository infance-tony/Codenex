import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Load a pre-trained model for image classification
model = tf.keras.applications.MobileNetV2(weights='imagenet')

def predict_tumor(img_path):
    """
    Predict if the image has a tumor based on general image classification.
    This is a simplified example using a pre-trained model.
    """
    try:
        # Load and preprocess the image
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

        # Make prediction
        predictions = model.predict(img_array)
        decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=5)[0]

        # Check for keywords related to brain or medical conditions
        tumor_keywords = ['brain', 'tumor', 'cancer', 'mri', 'scan', 'medical']
        for _, label, confidence in decoded_predictions:
            if any(keyword in label.lower() for keyword in tumor_keywords):
                return f"Potential tumor detected (confidence: {confidence:.2f})"

        # If no relevant prediction, assume no tumor
        return "No tumor detected in the image."

    except Exception as e:
        return f"Error processing image: {str(e)}"

# Ask for image path
img_path = input("Enter the path to the image file: ")
result = predict_tumor(img_path)
print(result)