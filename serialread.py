import serial
import time

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"
ser.open()

while True:
   while True:
    data = str(ser.readline())# retrieve and cast data to a string
    data = data.replace("b","")
    data = data.replace("'", "")
    data = data.replace(" ", "")
    data = data.replace("\\r\\n", "")
    data = int(data)
    print(data)
    time.sleep(1)
ser.close
print(data)