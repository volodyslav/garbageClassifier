from tensorflow import keras
import tensorflow as tf

def model_load():
    """Load keras model for predictions"""
    model = keras.models.load_model("garbage_2.keras")
    return model

def load_image(img):
    """Transform the image for predictions"""
    data = tf.keras.preprocessing.image.ImageDataGenerator(
        rescale=1.0/255
    )