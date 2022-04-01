from os import system
from time import sleep
system("cls")
minutes=0
hour=0
days=0
secs=60
minutes=int(input("Count down minute: "))
minutes=abs(minutes)
minutes=minutes-1
system("cls")
while(True):
    abs(minutes)
    print(f"Minute: {minutes}\nSecond: {secs}")
    secs=secs-1
    if(minutes<0):
        minutes=59
        hour=hour-1
    if(secs<0):
        secs=59
        minutes=minutes-1
    sleep(1)
    system("cls")
    if(minutes<=0 and secs<=0):
        for i in range(3):
            print("Time Out!")
            system("msg * \"Time Out\"")
        break