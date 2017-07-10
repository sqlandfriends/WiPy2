# main.py -- put your code here!
import machine
import pycom
pycom.heartbeat(False)
from network import WLAN
wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
for net in nets:
   
    elif net.ssid == 'Net Name': #where Net Name is Your network name
        print('Network found!')
        wlan.connect('Net Name',auth=(WLAN.WPA2, 'Pass'), timeout=5000)#Pass = Password for Your network
    
        while not wlan.isconnected():
            machine.idle() # save power while waiting
        print('WLAN connection succeeded!')
        break
