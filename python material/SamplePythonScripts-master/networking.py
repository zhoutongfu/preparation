#!/usr/bin/python

#Author: Suraj Patil
#Version: 1.0
#Date: 25th March 2014

'''uses scapy, you need to have scapy installed, gets the MAC address of the IP address you specify by sending and receiving
ARP request and response'''

from scapy.all import *
ip = raw_input('Enter IP address')

try:
  alive, dead = alive,dead=srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip), timeout=2, verbose=0)
  print "MAC  -  IP"
  print alive[0][1].hwsrc  # will print the MAC address of the IP address you specify in the ip
except:
  pass
