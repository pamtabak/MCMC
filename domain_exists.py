import os
import socket

try:
	socket.gethostbyname(i.strip())
	print(i + " exists")
except socket.gaierror:
	print "unable to get address for", i