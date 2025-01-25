import tensorflow as tf
import cv2
import numpy as np
import subprocess
import os
from time import sleep

# Load the trained model
model = tf.keras.models.load_model('/home/pi/leaf_classification/basil_lemon_model.h5')

# Function to capture an image using the camera
def capture_image(output_path):
    command = f"libcamera-jpeg -o {output_path} --width 1920 --height 1080"
    process = subprocess.run(command, shell=True)

    # Check if the image was captured successfully
    if process.returncode == 0 and os.path.exists(output_path):
        print(f"Image captured and saved to {output_path}.")
        return True
    else:
        print("Error: Failed to capture image.")
        return False

# Preprocess the image for prediction
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load the image at {image_path}.")
        return None
    img = cv2.resize(img, (224, 224))  # Resize to model input size
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = img / 255.0  # Normalize image
    return img

# Function to predict the plant
def recognize_plant(image_path):
	
    img = preprocess_image(image_path)
    # img = preprocess_image('/home/pi/leaf_classification/realimage/lemon.png')
    if img is None:
        return  # Exit if image could not be loaded or preprocessed
    prediction = model.predict(img)
    print(prediction)
    if prediction > 0.5:
        print("This is a Lemon plant!")
    else:
        print("This is a Basil plant!")

# Path to save the captured image
image_path = '/home/pi/Desktop/plant_image.jpg'

# Capture the image
if not capture_image(image_path):
    print("Exiting script due to image capture failure.")
    exit(1)

# Predict the plant type
recognize_plant(image_path)
