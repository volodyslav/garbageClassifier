import tensorflow as tf
from tensorflow import keras
from PIL import Image, ImageOps
import numpy as np
import platform

image_size = (200, 200)
labels = ['battery','biological','cardboard','clothes','glass',
          'metal', 'paper','plastic','shoes', 'trash']

def preprocess_image(image_path):
    """Preprocessing of the image"""
    image = Image.open(image_path).convert("RGB")
    image = ImageOps.fit(image, image_size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = image_array.astype(np.float32) / 255.0
    data = np.ndarray(shape=(1, 200, 200, 3), dtype=np.float32)
    data[0] = normalized_image_array
    return data

def load_image(image_path):
    """Load the model and transform the image for predictions"""
    model = keras.models.load_model("garbage.h5")

    # Determine the platform
    preprocess = preprocess_image(image_path)
    prediction = model.predict(preprocess)
    label = labels[prediction[0].argmax()]
    print("Predictions:", labels[prediction[0].argmax()])
    print("Predictions:", prediction)
    return label
   