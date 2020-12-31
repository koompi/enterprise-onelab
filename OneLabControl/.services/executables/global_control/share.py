#!/usr/bin/python

import os

# Starting X11 server
os.system('x11vnc -display :0 -rfbport 5900&')

# Connecting all clients to x11 server 
to_connect = [3]

for i in to_connect:
	os.system('ssh admin@192.168.0.{} "export DISPLAY=:0 && cd /opt/.client-onelab && ./share.sh"'.format(i))
	continue
