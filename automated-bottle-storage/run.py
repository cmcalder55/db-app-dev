# Importing Libraries
from pickle import FALSE
import serial
import time
on = True

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

while on == True:
    num = input("Enter a number: ") # Taking input from user
    print(num)
    if num == 24:
        on = False
    value = write_read(num)
    print(value) # printing the value