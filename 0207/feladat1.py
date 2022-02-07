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

def bfeladat(s1,s2):
    eredmeny=(s1%s2)%2
    if eredmeny==0:
        return"paros"
    else:
        return"Páratlan"


def dfeladat(solista):
    elteresek=[]
    for i in range(0,len(solista)):
        if solista[i]>35:
            elteresek.append(solista[i]+35)
        else:
            elteresek.append(35-solista[i])
    return elteresek

def efeladat(solista):
    solista=list(set(solista))
    solista.sort()
    for i in range(0,len(solista)):
        print(solista[i], end=", ")

def ffeladat(solista):
    for i in range(0, len(solista), 2):
        print(solista[i], end=" ")

def gfeladat(solista):
    seged=[]
    for i in range(0,len(solista),2):
        seged.append(solista[i])
    return seged


system("cls")
def Main():
    so1= int(input("Kérem az 1. tenger sótartalmát"))
    so2= int(input("Kérem az 2. tenger sótartalmát"))
    print("a.) feladat")
    afeladat(so1,so2)
    print("a.) feladat")
    print(bfeladat(so1,so2))
    print("c.) feladat")
    sotartalmak =[]
    for i in range(0,20):
        sotartalmak.append(random.randrange(30,41))
    print(*sotartalmak)
    print("d.)feladat")
    print(*dfeladat(sotartalmak))
    print("e.)feladat")
    efeladat(sotartalmak)
    print("f.)feladat")
    #eljárás
    ffeladat(sotartalmak)
    print("g.)feladat")
    #függvény
    gfeladat(sotartalmak)
if __name__=="__main__":
    Main()