import serial
import time
import csv

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
    #data = int(data)
    print(data)
    time.sleep(2)
    if len(data) > 0:
        print(data)
        file = open("sensor.csv", "a")
        file.write(data+",")
        file.close()

ser.close