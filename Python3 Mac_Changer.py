#!/usr/bin/env python
# Python Mac-Changer
# print("Author: coding.s9 AKA MunYa")
# print("Disclaimer: I am not liable or responsible 4 your misuse of this video.")
# print("This video is 4 educational purposes only!")
print("Objective: Python3 Mac-Changer")

import subprocess
import optparse

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    # Use a list to prevent session or code hijacking
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

#Create Parser Object
parser = optparse.OptionParser()
#Teach the Child
parser.add_option("-i", "--interface", dest="interface", help="Interface to change it's MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
#Tell Child to parse arguments
(options, arguments) = parser.parse_args()

change_mac(options.interface, options.new_mac)

