import os
import random
import math
os.system("cls")

szam=int(input("írjon be egy számot: "))
checker=3%szam
checker2=2%szam
if(checker==0 and checker2!=0):
    print("A szám megfelelő")
else:
    print("A szám nem megfelelő")
    print("")
    print("")
    print("")

szam2=random.randrange(100,1001)
print("A termék ára: ", szam2)
if(szam2>700):
    print("A termék túl drága")
elif(szam2<400):
    print("A termék túl olcsó")
else:
    print("A termék ára optimális")
    print("")
    print("")
    print("")


szam3=(random.randrange(100,1001))
print("A termék ára: ", szam3)
if(szam3>700):
    szam3=szam3*1,1
    print("A termék túl drága")
elif(szam3<400):
    szam3=szam3*1,1
    print("A termék túl olcsó")
else:
    szam3=szam3*0,9
    print("A termék ára optimális")


