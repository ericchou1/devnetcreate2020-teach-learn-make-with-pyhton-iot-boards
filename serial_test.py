#/usr/bin/env python3
import serial

serial = serial.Serial('/dev/cu.usbmodem1412201')
while True: 
    output = serial.readline().strip()
    output_string = output.decode("utf-8") 
    print('This is the serial output: ' + str(output_string))


