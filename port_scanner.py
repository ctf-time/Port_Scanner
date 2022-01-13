#!/bin/python
import sys
import socket
from datetime import datetime

#Define our target 
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
	print("Invalid arguments")
	print("Syntax: python3 port_scanner.py <ip>") #syntax to run port scanner on specific IP


#Add banner
print( "-" * 50)
print("Scanning target: " +target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(50,85):                                      #runs one port at a time, we can also include all ports till  65535
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		print("Checking port {}".format(port))
		if result == 0:
			print("Port {} is open".format(port))
		s.close()

except KeyboardInterrupt:                         #exceptions may occurr through keyboard say for if we used ctrl + c
	print("\nExiting program.")

except socket.gaierror:	                          # to handle no hostname resolution
	print("Hostname could not be resolved")
	sys.exit()

except socket.error:                              #if we cann't connect to the IP address we specified
	print("Couldn't connect to server")
	sys.exit()


