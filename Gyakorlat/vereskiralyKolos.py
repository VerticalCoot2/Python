import os
import random
import math
os.system("cls")

nap=random.randrange(1,31)
honap=random.randrange(1,13)

print("Nap: ",nap)
print("Hónap: ",honap)
print("")
print("")
print("")
napokban=((honap*30)+nap)
print("Napokban: ", napokban)
triplanap=napokban*3
print("Tripla nap: ",triplanap)
print(f"Tripla idő: {math.floor(triplanap/30)} hónap {triplanap%30} nap")

next=input("")
if(next==""):
    os.system("cls")
else:
    os.system("cls")
money=int(input("Kérem adja meg a költhető összeget... "))
spend=int(input("Milyen árú termékeket óhalyt venni?... "))
l=money%2
if(l==0):
    print(f"Marad: {money%spend} Ft")
else:
    k=money/spend
    print(f"Temékszám: {math.floor(k)} db")