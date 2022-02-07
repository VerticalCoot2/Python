import os
import random
os.system("cls")
num=random.randrange(1,501)
lepes=1
print("Gondoltam egy számra 1-500 között...")
tipp=int(input("Tipp: "))
if(tipp==num):
    print("Grat, eltaláltad")
else:
    while(True):
        print("KÖZÖD!?")
