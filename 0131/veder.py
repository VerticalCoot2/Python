import os
import math
import tyutyu
def felulet(sugar,magassag):
    return (2*math.pow(sugar,2)*math.pi)+(magassag*2*sugar*math.pi)

os.system("cls")
r=float(input("Vödör alapkörének sugara(cm): "))
m=float(input("Vödör magasságát(cm): "))
print("")
print("A vödör felülete",round(felulet(r,m),3),"cm2")
