#!/usr/bin/env python3
import netmiko
import serial
from netmiko import ConnectHandler
import pprint
import time

# Defined IOSv1 credentials
ios_v1 = {'device_type': 'cisco_ios',
          'host': '192.168.2.250',
          'username': 'cisco',
          'password': 'cisco'}
iosv1_connect = ConnectHandler(**ios_v1)

# Start serial monitor for temperature
serial = serial.Serial('/dev/cu.usbmodem1412201')
while True:
    output = serial.readline().strip()
    output_string = output.decode("utf-8")
    print('Current Temperature: ' + str(output_string))
    show_int = iosv1_connect.send_command('show ip interface brief')
    g0_1_status = show_int.split()[16]

    if float(output_string) > 31:
        if g0_1_status == 'up':
            print('Too hot! Shutting down interface')
            output = iosv1_connect.send_config_set(['interface GigabitEthernet0/1',
                                                    'shut'
                                                   ])
            pprint.pprint(output)
    else:
        if g0_1_status == 'administratively':
            print('Temperature normal, Unshut interface')
            output = iosv1_connect.send_config_set(['interface GigabitEthernet0/1',
                                                    'no shut'
                                                  ])
            pprint.pprint(output)


