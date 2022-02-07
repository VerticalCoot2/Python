
import os
import math
os.system("cls")
szam=int(input("adja meg a számot: "))
print("")
print("E: szám harmada")
print("M: szám harmadának maradéke")
print("N: szám négyzete")
print("K: szám köbe")
print("G: szám gyöke")
valasz=input("Nyomja le a megfelelő billentryűt: ")
if(valasz=="E"):
    eredmeny=szam/3
    print("Az eredmény", eredmeny)
elif(valasz=="M"):
    eredmeny=3%szam
    print("Az eredmény: ", eredmeny)
elif(valasz=="N"):
    eredmeny=szam*szam
    print("AZ eredmény", eredmeny)
elif(valasz=="K"):
    eredmeny=szam*szam*szam
    print("Az eredmény: ", eredmeny)
elif(valasz=="G"):
    eredmeny=math.sqrt(szam)
    print("Az eredmény: ", round(eredmeny))
else:
    print("Tanul meg olvas!")