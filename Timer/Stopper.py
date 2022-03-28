from time import sleep
from os import system
sec=0
min=0
hour=0
day=0
system("cls")
input("START \n")
system("cls")
while(True):
    print(f"Days:{day}   Time:{hour}:{min}:{sec}")
    sec=sec+1
    if(sec==60):
        min=min+1
        sec=0
    if(min==60):
        min=0
        hour=hour+1
    if(hour==24):
        day=day+1
        hour=0
    sleep(1)
    system("cls")