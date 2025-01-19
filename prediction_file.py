import tensorflow as tf
import cv2
import numpy as np
from picamera import PiCamera
from time import sleep

# Load the trained model
model = tf.keras.models.load_model('basil_lemon_model.h5')

# # Initialize the camera
camera = PiCamera()

# Function to capture an image
def capture_image():
    camera.start_preview()
    sleep(2)  # Give the camera time to adjust to the lighting
    camera.capture('/home/pi/plant_image.jpg')
    camera.stop_preview()

# Preprocess the image for prediction
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))  # Resize to model input size
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = img / 255.0  # Normalize image
    return img

# Function to predict the plant
def recognize_plant(image_path):
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    if prediction > 0.5:
        print("This is a Lemon plant!")
    else:
        print("This is a Basil plant!")

# Capture an image
capture_image()

# Predict the plant type
recognize_plant('./realimages/basilfinal.jpg')