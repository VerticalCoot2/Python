from os import system
import random
from math import pi

def afeladat(s1,s2):
    if(s1%2==0 and s2%2==0):
        if(s1>s2):
            sz = ((s1-s2)/s2)*100
            print(f"A nagyobbik {sz}%-al nagyobb sótartalmú")
        else:
            sz = ((s2-s1)/s1)*100
            print(f"A nagyobbik {sz}%-al nagyobb sótartalmú")
    else:
        h=s1/s2
        print(round(h),3)

system("cls")
def Main():
    so1= int(input("Kérem az 1. tenger sótartalmát"))
    so2= int(input("Kérem az 2. tenger sótartalmát"))
    afeladat(so1,so2)

if __name__=="__main__":
    Main()