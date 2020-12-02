#/usr/bin/env python

import subprocess

interface = "wlan0"

print ("[+] changing to a new MAC for" + interface)

# subprocess.call("ifconfig wlan0 down", shell=True)
# subprocess.call("macchanger -r eth0", shell=True)
# subprocess.call("ifconfig eth0 up", shell=True)
# subprocess.call("ifconfig", shell=True) 