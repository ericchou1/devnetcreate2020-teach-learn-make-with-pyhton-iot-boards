# devnetcreate2020-teach-learn-make-with-pyhton-iot-boards
Cisco DevNet Create 2020 Talk: Teach, Learn, and Make with Python IoT Boards for Fun and Profit

This repository is provided as supplement for Cisco DevNet Create 2020 Virtual Talk

![Cisco DevNet Create 2020 1](/images/devnetcreate2020_1.png)
![Cisco DevNet Create 2020 2](/images/devnetcreate2020_2.png)


## Useful links: 

- [Adafruit CLUE Board](https://learn.adafruit.com/adafruit-clue/overview)
- [CircuitPython on CLUE](https://learn.adafruit.com/adafruit-clue/circuitpython)
- [CircuitPython CLUE Firmware Download](https://circuitpython.org/board/clue_nrf52840_express/)
- [CircuitPython Library](https://circuitpython.org/libraries)
- [Mu Editor](https://codewith.mu/)
- [Netmiko](https://pypi.org/project/netmiko/)

## Part 1: Overview of Adafruit CLUE Board

- Click image below for YouTube video

[![DevNet Create 2020 Part 1](/images/video_part1.png)](https://youtu.be/8rDgbaXD9-c)

## Part 2: Adafruiit CLUE sensors

- Click image below for YouTube video

[![DevNet Create 2020 Part 2](/images/video_part2.png)](https://youtu.be/IPlhbTFaFfE)

## Part 3: CircuitPython and Libraries

![Circuit Python Libraries](/images/CircuitPython_libraries.png)

- Click image below for YouTube video

[![DevNet Create 2020 Part 3](/images/video_part3.png)](https://youtu.be/EfLhfftXfZs)

## Part 4: Serial Output

```
#/usr/bin/env python3
import serial

serial = serial.Serial('/dev/cu.usbmodem1412201')
while True: 
    output = serial.readline().strip()
    output_string = output.decode("utf-8") 
    print('This is the serial output: ' + str(output_string))
```

- Click image below for YouTube video

[![DevNet Create 2020 Part 4](/images/video_part4.png)](https://youtu.be/ZN0ldc6aP1o)

## Part 5: Network Example

```
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
```

- Click image below for YouTube video

[![DevNet Create 2020 Part 5](/images/video_part5.png)](https://youtu.be/tA_CBOEB8Ek)






