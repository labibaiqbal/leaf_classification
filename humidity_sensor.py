# -*- coding: utf-8 -*-
import adafruit_dht
import board
import time

# Initialize the DHT sensor
dht_sensor = adafruit_dht.DHT11(board.D4)  # Use DHT22 if needed

# Threshold for significant change
TEMP_THRESHOLD = 1.0  # Temperature change in °C
HUMIDITY_THRESHOLD = 5.0  # Humidity change in %

# Variables to store the last recorded values
last_temperature = None
last_humidity = None

while True:
    try:
        temperature = dht_sensor.temperature  # Temperature in Celsius
        humidity = dht_sensor.humidity        # Humidity as a percentage

        if temperature is not None and humidity is not None:
            # Check if this is the first reading or if values have changed significantly
            if (
                last_temperature is None or last_humidity is None or
                abs(temperature - last_temperature) >= TEMP_THRESHOLD or
                abs(humidity - last_humidity) >= HUMIDITY_THRESHOLD
            ):
                print(f"Temp={temperature:0.1f}C Humidity={humidity:0.1f}%")
                last_temperature = temperature
                last_humidity = humidity
        else:
            print("Sensor failure. Check wiring.")
    except RuntimeError as error:
        # Ignore intermittent errors
        print(f"Error: {error.args[0]}")
    except Exception as error:
        dht_sensor.exit()
        raise error

    time.sleep(3)
