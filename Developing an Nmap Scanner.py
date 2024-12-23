#!usr/bin/python3

import nmap

scanner = map.PortScanner()

print("welcome, this is a simple nmap automation tool")
print("<-------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")
print("The IP you entered is:", ip_addr)
type(ip_addr) 

rsep = input(""" \nplease enter the tpe of scan you want to run
             1)SYN ACK scan
             2)UDP SCAN
             3)Comprehensive Scan  """)
print("")