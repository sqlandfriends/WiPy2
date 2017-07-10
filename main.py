# main.py -- put your code here!
import machine
import pycom
pycom.heartbeat(False)
from network import WLAN
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
for net in nets:
    if net.ssid == 'Orange-F813':
        print('Network found!')
        wlan.connect('Orange-F813', auth=(WLAN.WPA2, '73044277'), timeout=5000)
       
    elif net.ssid == 'dlink':
        print('Network found!')
        wlan.connect('dlink', timeout=5000)
    elif net.ssid == 'VMD5BC68E':
        print('Network found!')
        wlan.connect('VMD5BC68E',auth=(WLAN.WPA2, 'Ge6nGnvszvhd'), timeout=5000)
    
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break
