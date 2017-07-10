#This is basic code to connect wipy to wifi network and disable HeartBeat led from blinking
import machine
import pycom
pycom.heartbeat(False)
from network import WLAN
from os import sd #import module thats needed to start microSD card if user have one
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
#code below mounts SD card thanks to one of imports
#  IMPORTANT: card must be FAT formatted BEFROE trying to use it!!!!!
sd = SD()
os.mount(sd, '/sd')
