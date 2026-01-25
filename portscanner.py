#!/bin/python3
import socket
import sys
from datetime import datetime

# Define our target (We will scan ourselves first)
target = "scanme.nmap.org" 

# Add a nice banner
print("-" * 50)
print(f"Scanning Target: {target}")
print(f"Time started: {datetime.now()}")
print("-" * 50)

try:
    # Check ports from 1 to 1024
    for port in range(1, 1024):  
        
        # Create a socket object
        # AF_INET = IPv4
        # SOCK_STREAM = TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout (0.5 seconds) so we don't wait forever on closed ports
        socket.setdefaulttimeout(0.5)
        
        # connect_ex returns 0 if the connection was successful (Port is OPEN)
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port} is OPEN")
        
        # Always close the connection nicely
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()
