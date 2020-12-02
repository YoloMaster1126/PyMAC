#/usr/bin/env python

import subprocess

interface = input ("interface >")
New_Mac = input("New Mac >")

print("[+] changing to a new MAC for" + interface + "to" + New_Mac)

subprocess.call("ifconfig" + interface + "down", shell=True)
subprocess.call("ifconfig" + interface + "hw ether", shell=True)
subprocess.call("ifconfig" + interface + "up", shell=True)
subprocess.call("ifconfig", shell=True) 