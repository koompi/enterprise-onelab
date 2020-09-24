import os

#All previous code is related to the UI the following code will be a means of comunicating with the host machine.
#21 - sep - 2020 Added individual buttons and linked drop down box. As well as completed ssh commands

#Backend for machine 1


def ssh_initInteract1():
    os.system("remote-viewer spice://172.16.1.1:5900")

def ssh_initStart1():
    os.system("sudo -S <<< 123 virsh start monitor-01")

def ssh_initStop1():
    print ("sudo -S <<< 123 virsh destroy monitor-01")

def ssh_initPlay1():
    print ("sudo -S <<< 123 virsh resume monitor-01")

def ssh_initPuase1():
    print ("sudo -S <<< 123 virsh suspend monitor-01")

def ssh_ss1():
    print ("sudo -S <<< 123 virsh screenshot monitor-01")


#Backend for machine 2

def ssh_initInteract2():
    print ("remote-viewer spice://172.16.1.1:5900")

def ssh_initStart2():
    print ("sudo -S <<< 123 virsh start monitor-02")

def ssh_initStop2():
    print ("sudo -S <<< 123 virsh resume monitor-02")

def ssh_initPlay2():
    print ("sudo -S <<< 123 virsh resume monitor-02")

def ssh_initPuase2():
    print ("sudo -S <<< 123 virsh suspend monitor-02")

def ssh_ss2():
    print ("sudo -S <<< 123 virsh screenshot monitor-02")

#Backend for machine 3

def ssh_initInteract3():
    print ("Interact with me Daddy")

def ssh_initStart3():
    print ("I am Start")

def ssh_initStop3():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay3():
    print ("GO GO GOOOOOOO")

def ssh_initPuase3():
    print ("Pause Pause Pause")

def ssh_ss3():
    print ("Camers sounds")

#Backend for machine 4


def ssh_initInteract4():
    print ("Interact with me Daddy")

def ssh_initStart4():
    print ("I am Start")

def ssh_initStop4():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay4():
    print ("GO GO GOOOOOOO")

def ssh_initPuase4():
    print ("Pause Pause Pause")

def ssh_ss4():
    print ("Camers sounds")

#Backend for machine 5

def ssh_initInteract5():
    print ("Interact with me Daddy")

def ssh_initStart5():
    print ("I am Start")

def ssh_initStop5():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay5():
    print ("GO GO GOOOOOOO")

def ssh_initPuase5():
    print ("Pause Pause Pause")

def ssh_ss5():
    print ("Camers sounds")

#Backend for machine 6

def ssh_initInteract6():
    print ("Interact with me Daddy")

def ssh_initStart6():
    print ("I am Start")

def ssh_initStop6():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay6():
    print ("GO GO GOOOOOOO")

def ssh_initPuase6():
    print ("Pause Pause Pause")

def ssh_ss6():
    print ("Camers sounds")

#Backend for machine 7


def ssh_initInteract7():
    print ("Interact with me Daddy")

def ssh_initStart7():
    print ("I am Start")

def ssh_initStop7():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay7():
    print ("GO GO GOOOOOOO")

def ssh_initPuase7():
    print ("Pause Pause Pause")

def ssh_ss7():
    print ("Camers sounds")
    

#Backend for machine 8

def ssh_initInteract8():
    print ("Interact with me Daddy")

def ssh_initStart8():
    print ("I am Start")

def ssh_initStop8():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay8():
    print ("GO GO GOOOOOOO")

def ssh_initPuase8():
    print ("Pause Pause Pause")

def ssh_ss8():
    print ("Camers sounds")

#Backend for machine 9

def ssh_initInteract9():
    print ("Interact with me Daddy")

def ssh_initStart9():
    print ("I am Start")

def ssh_initStop9():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay9():
    print ("GO GO GOOOOOOO")

def ssh_initPuase9():
    print ("Pause Pause Pause")

def ssh_ss9():
    print ("Camers sounds")

#Backend for machine 10


def ssh_initInteract10():
    print ("Interact with me Daddy")

def ssh_initStart10():
    print ("I am Start")

def ssh_initStop10():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay10():
    print ("GO GO GOOOOOOO")

def ssh_initPuase10():
    print ("Pause Pause Pause")

def ssh_ss10():
    print ("Camers sounds")

#Backend for machine 11

def ssh_initInteract11():
    print ("Interact with me Daddy")

def ssh_initStart11():
    print ("I am Start")

def ssh_initStop11():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay11():
    print ("GO GO GOOOOOOO")

def ssh_initPuase11():
    print ("Pause Pause Pause")

def ssh_ss11():
    print ("Camers sounds")

#Backend for machine 12

def ssh_initInteract12():
    print ("Interact with me Daddy")

def ssh_initStart12():
    print ("I am Start")

def ssh_initStop12():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay12():
    print ("GO GO GOOOOOOO")

def ssh_initPuase12():
    print ("Pause Pause Pause")

def ssh_ss12():
    print ("Camers sounds")

#Backend for machine 13

def ssh_initInteract13():
    print ("Interact with me Daddy")

def ssh_initStart13():
    print ("I am Start")

def ssh_initStop13():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay13():
    print ("GO GO GOOOOOOO")

def ssh_initPuase13():
    print ("Pause Pause Pause")

def ssh_ss13():
    print ("Camers sounds")


#Backend for machine 14

def ssh_initInteract14():
    print ("Interact with me Daddy")

def ssh_initStart14():
    print ("I am Start")

def ssh_initStop14():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay14():
    print ("GO GO GOOOOOOO")

def ssh_initPuase14():
    print ("Pause Pause Pause")

def ssh_ss14():
    print ("Camers sounds")

#Backend for machine 15

def ssh_initInteract15():
    print ("Interact with me Daddy")

def ssh_initStart15():
    print ("I am Start")

def ssh_initStop15():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay15():
    print ("GO GO GOOOOOOO")

def ssh_initPuase15():
    print ("Pause Pause Pause")

def ssh_ss15():
    print ("Camers sounds")

#Backend for machine 16


def ssh_initInteract16():
    print ("Interact with me Daddy")

def ssh_initStart16():
    print ("I am Start")

def ssh_initStop16():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay16():
    print ("GO GO GOOOOOOO")

def ssh_initPuase16():
    print ("Pause Pause Pause")

def ssh_ss16():
    print ("Camers sounds")

#Backend for machine 17

def ssh_initInteract17():
    print ("Interact with me Daddy")

def ssh_initStart17():
    print ("I am Start")

def ssh_initStop17():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay17():
    print ("GO GO GOOOOOOO")

def ssh_initPuase17():
    print ("Pause Pause Pause")

def ssh_ss17():
    print ("Camers sounds")

#Backend for machine 18

def ssh_initInteract18():
    print ("Interact with me Daddy")

def ssh_initStart18():
    print ("I am Start")

def ssh_initStop18():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay18():
    print ("GO GO GOOOOOOO")

def ssh_initPuase18():
    print ("Pause Pause Pause")

def ssh_ss18():
    print ("Camers sounds")

#Backend for machine 19


def ssh_initInteract19():
    print ("Interact with me Daddy")

def ssh_initStart19():
    print ("I am Start")

def ssh_initStop19():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay19():
    print ("GO GO GOOOOOOO")

def ssh_initPuase19():
    print ("Pause Pause Pause")

def ssh_ss19():
    print ("Camers sounds")
    

#Backend for machine 20

def ssh_initInteract20():
    print ("Interact with me Daddy")

def ssh_initStart20():
    print ("I am Start")

def ssh_initStop20():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay20():
    print ("GO GO GOOOOOOO")

def ssh_initPuase20():
    print ("Pause Pause Pause")

def ssh_ss20():
    print ("Camers sounds")

#Backend for machine 21

def ssh_initInteract21():
    print ("Interact with me Daddy")

def ssh_initStart21():
    print ("I am Start")

def ssh_initStop21():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay21():
    print ("GO GO GOOOOOOO")

def ssh_initPuase21():
    print ("Pause Pause Pause")

def ssh_ss21():
    print ("Camers sounds")

#Backend for machine 22


def ssh_initInteract22():
    print ("Interact with me Daddy")

def ssh_initStart22():
    print ("I am Start")

def ssh_initStop22():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay22():
    print ("GO GO GOOOOOOO")

def ssh_initPuase22():
    print ("Pause Pause Pause")

def ssh_ss22():
    print ("Camers sounds")

#Backend for machine 23

def ssh_initInteract23():
    print ("Interact with me Daddy")

def ssh_initStart23():
    print ("I am Start")

def ssh_initStop23():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay23():
    print ("GO GO GOOOOOOO")

def ssh_initPuase23():
    print ("Pause Pause Pause")

def ssh_ss23():
    print ("Camers sounds")

#Backend for machine 24

def ssh_initInteract24():
    print ("Interact with me Daddy")

def ssh_initStart24():
    print ("I am Start")

def ssh_initStop24():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay24():
    print ("GO GO GOOOOOOO")

def ssh_initPuase24():
    print ("Pause Pause Pause")

def ssh_ss24():
    print ("Camers sounds")

#Backend for machine 25

def ssh_initInteract25():
    print ("Interact with me Daddy")

def ssh_initStart25():
    print ("I am Start")

def ssh_initStop25():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay25():
    print ("GO GO GOOOOOOO")

def ssh_initPuase25():
    print ("Pause Pause Pause")

def ssh_ss25():
    print ("Camers sounds")

#Backend for machine 26

def ssh_initInteract26():
    print ("Interact with me Daddy")

def ssh_initStart26():
    print ("I am Start")

def ssh_initStop26():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay26():
    print ("GO GO GOOOOOOO")

def ssh_initPuase26():
    print ("Pause Pause Pause")

def ssh_ss26():
    print ("Camers sounds")


#Backend for machine 27

def ssh_initInteract27():
    print ("Interact with me Daddy")

def ssh_initStart27():
    print ("I am Start")

def ssh_initStop27():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay27():
    print ("GO GO GOOOOOOO")

def ssh_initPuase27():
    print ("Pause Pause Pause")

def ssh_ss27():
    print ("Camers sounds")

#Backend for machine 28

def ssh_initInteract28():
    print ("Interact with me Daddy")

def ssh_initStart28():
    print ("I am Start")

def ssh_initStop28():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay28():
    print ("GO GO GOOOOOOO")

def ssh_initPuase28():
    print ("Pause Pause Pause")

def ssh_ss28():
    print ("Camers sounds")

#Backend for machine 29


def ssh_initInteract29():
    print ("Interact with me Daddy")

def ssh_initStart29():
    print ("I am Start")

def ssh_initStop29():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay29():
    print ("GO GO GOOOOOOO")

def ssh_initPuase29():
    print ("Pause Pause Pause")

def ssh_ss29():
    print ("Camers sounds")

#Backend for machine 30

def ssh_initInteract30():
    print ("Interact with me Daddy")

def ssh_initStart30():
    print ("I am Start")

def ssh_initStop30():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay30():
    print ("GO GO GOOOOOOO")

def ssh_initPuase30():
    print ("Pause Pause Pause")

def ssh_ss30():
    print ("Camers sounds")

#Backend for machine 31


def ssh_initInteract31():
    print ("Interact with me Daddy")

def ssh_initStart31():
    print ("I am Start")

def ssh_initStop31():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay31():
    print ("GO GO GOOOOOOO")

def ssh_initPuase31():
    print ("Pause Pause Pause")

def ssh_ss31():
    print ("Camers sounds")
    

#Backend for machine 32

def ssh_initInteract32():
    print ("Interact with me Daddy")

def ssh_initStart32():
    print ("I am Start")

def ssh_initStop32():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay32():
    print ("GO GO GOOOOOOO")

def ssh_initPuase32():
    print ("Pause Pause Pause")

def ssh_ss32():
    print ("Camers sounds")

#Backend for machine 33

def ssh_initInteract33():
    print ("Interact with me Daddy")

def ssh_initStart33():
    print ("I am Start")

def ssh_initStop33():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay33():
    print ("GO GO GOOOOOOO")

def ssh_initPuase33():
    print ("Pause Pause Pause")

def ssh_ss33():
    print ("Camers sounds")

#Backend for machine 34


def ssh_initInteract34():
    print ("Interact with me Daddy")

def ssh_initStart34():
    print ("I am Start")

def ssh_initStop34():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay34():
    print ("GO GO GOOOOOOO")

def ssh_initPuase34():
    print ("Pause Pause Pause")

def ssh_ss34():
    print ("Camers sounds")

#Backend for machine 35

def ssh_initInteract35():
    print ("Interact with me Daddy")

def ssh_initStart35():
    print ("I am Start")

def ssh_initStop35():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay35():
    print ("GO GO GOOOOOOO")

def ssh_initPuase35():
    print ("Pause Pause Pause")

def ssh_ss35():
    print ("Camers sounds")

#Backend for machine 36

def ssh_initInteract36():
    print ("Interact with me Daddy")

def ssh_initStart36():
    print ("I am Start")

def ssh_initStop36():
    print ("STOPPPPEEEDDD!")

def ssh_initPlay36():
    print ("GO GO GOOOOOOO")

def ssh_initPuase36():
    print ("Pause Pause Pause")

def ssh_ss36():
    print ("Camers sounds")