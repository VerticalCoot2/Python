import os
def adatbevitel():
    global aoldal, boldal
    aoldal = int(input("A oldal: "))
    boldal = int(input("B oldal: "))
def kiszamol():
    terulet=aoldal*boldal
    print("a terület: ",terulet)
os.system("cls")
adatbevitel()
kiszamol()