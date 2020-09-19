import os

#All previous code is related to the UI the following code will be a means of comunicating with the host machine.

def ssh_initInteract():
    os.system("ssh hangsia@192.168.1.79")

def ssh_initPuasePlay():
    print("Hello I am connected successfully")

def ssh_initStopStart():
    print("Hello I am connected successfully")