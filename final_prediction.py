import tensorflow as tf
import cv2
import numpy as np
import subprocess
import os
from time import sleep
import board
import digitalio
import adafruit_character_lcd.character_lcd as characterlcd

# **1. Set Up the LCD Display**
# Adjust these pins and dimensions based on your LCD model
lcd_columns = 16
lcd_rows = 2
lcd_rs = digitalio.DigitalInOut(board.D26)  # Register select pin
lcd_en = digitalio.DigitalInOut(board.D19)  # Enable pin
lcd_d4 = digitalio.DigitalInOut(board.D13)  # Data pin D4
lcd_d5 = digitalio.DigitalInOut(board.D6)  # Data pin D5
lcd_d6 = digitalio.DigitalInOut(board.D5)  # Data pin D6
lcd_d7 = digitalio.DigitalInOut(board.D11)  # Data pin D7

lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows
)

# **2. Load the Trained Model**
model = tf.keras.models.load_model('/home/pi/leaf_classification/basil_lemon_model.h5')

# **3. Function to Capture an Image Using the Camera**
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

# **4. Preprocess the Image for Prediction**
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load the image at {image_path}.")
        return None
    img = cv2.resize(img, (224, 224))  # Resize to model input size
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    img = img / 255.0  # Normalize image
    return img

# **5. Function to Predict the Plant**
def recognize_plant(image_path):
    lcd.clear()
    lcd.message = "Processing...\nPlease wait"
    # img = preprocess_image(image_path)
    img = preprocess_image('/home/pi/leaf_classification/realimage/lemon.png')

    if img is None:
        lcd.clear()
        lcd.message = "Error: Image\nnot found!"
        return  # Exit if image could not be loaded or preprocessed

    prediction = model.predict(img)
    print(prediction)

    # Determine the plant type and display on LCD
    if prediction > 0.5:
        result = "Lemon"
    else:
        result = "Basil"

    print(f"This is a {result}!")
    lcd.clear()
    lcd.message = f"Plant Type:\n{result}"

# **6. Path to Save the Captured Image**
image_path = '/home/pi/Desktop/plant_image.jpg'

# **7. Main Script Execution**
lcd.clear()
lcd.message = "Plant Classifier\nReady!"

# Capture the image
if not capture_image(image_path):
    print("Exiting script due to image capture failure.")
    lcd.clear()
    lcd.message = "Capture Failed\nExiting..."
    exit(1)

# Predict the plant type
recognize_plant(image_path)

# Keep the message on LCD for a while before clearing it
sleep(10)
lcd.clear()
lcd.message = "Process Complete!"
