import serial
import csv
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "142102"
ser.open()

#light = serial.write_line("" + str((input.light_level())))
while True:
    data = str(ser.readline())# retrieve and cast data to a string
    data = data.replace("b","")
    data = data.replace("'", "")
    data = data.replace(" ", "")
    data = data.replace("\\r\\n", "")
    if len(data) > 0:
        print(data)
        file = open("sensor.csv", "a")
        file.write(data+",")
        file.close()