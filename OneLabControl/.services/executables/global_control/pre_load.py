#!/usr/bin/python

import time
import sys
import os


# List containing the ping incrementation
pc_ip =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]

while True:

    for i in pc_ip:

        # This will send a request to each machine in a loop
         os.system("ping -c 1 192.168.0.{} -q -4  -W .001 && echo 'True' > /opt/.services/ip-ping/ping_{}.txt || echo 'False' > /opt/.services/ip-ping/ping_{}.txt".format(i, i, i))

         # Confirming it was sent
         print ("ping'd macine{}".format(i))

         # Declaring the variable for reading files
        
    continue
