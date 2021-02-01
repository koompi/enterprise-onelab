#!/usr/bin/python 

import time
import os

os.system("xinput --list | grep -E '(Keyboard | Mouse)' | egrep -iv 'virtual|video|button|bus' | egrep -o 'id=[0-9]+' | egrep -o '[0-9]+' > data.txt")

time.sleep(2)

list_of_lists = []

with open("/home/admin/koompi-onelab-status/Master_UI/data.txt", "r") as a_file:
    
    for line in a_file:
        stripped_line = line.strip()
        list_of_lists.append(stripped_line)

    a_file.close()

print (list_of_lists)

for i in list_of_lists:

    os.system('xinput float {}'.format(i))

    continue


