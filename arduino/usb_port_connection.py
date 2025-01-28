import serial
import time

sdata = serial.Serial('/dev/ttyACM0', 9600, timeout=1.0)
time.sleep(2)
sdata.reset_input_buffer()
print("arduino connected")

# send data from arduino to raspberrypi
def receive_data_from_arduino():
    try:
        while sdata.in_waiting > 0:
            time.sleep(0.01)
            arduino_data = sdata.readline().decode('utf-8').rstrip()
            print("Uno: " + arduino_data)
    except KeyboardInterrupt:
        print("Serial Comms Closed")
        sdata.close()
        
# send data from raspberrypi to arduino
def send_data_from_raspberrypi():
    try:
        while True:
            time.sleep(1)
            data = "Raspberry PI \n"
            sdata.write(data.encode('utf-8'))
            print("PI: " + data)
            receive_data_from_arduino()

            
    except KeyboardInterrupt:
        print("Serial Comms Closed")
        sdata.close()
        
if __name__ == "__main__":
    send_data_from_raspberrypi()
    receive_data_from_arduino()

