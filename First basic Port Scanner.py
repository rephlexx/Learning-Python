# Basic Port scanner

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) # ranslate hostname to IPv4

else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")

print("-" * 50)
print("Scanning target "+target)
print("Time started: " +str(datetime.now()))
print("-" * 50)

try:
    for port in range(130,140):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # try to connect for 1 second
        result = s.connect_ex((target,port))  # Returns an error indicator
        if result == 0:
                print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()
