from tensorflow import keras
import tensorflow as tf
import numpy as np
from PIL import Image

image_size = (150, 150)

def preprocess_image(image_path):
    """Preprocessing of the image"""
    img = Image.open(image_path)
    img = img.resize(image_size)
    img_array = np.asarray(img)
    img_array = img_array / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

def load_image(image_path):
    """Load the model and transform the image for predictions"""
    model = keras.models.load_model("garbage_2.keras")
    preprocess = preprocess_image(image_path)
    prediction = model.predict(preprocess)
    print("Predictions:", prediction)
    print(".........")
   