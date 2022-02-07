import os
import math
import random
#import colorama

os.system("cls")
print("Mit szeretne csinálni:")
print("")
print("A - kerekíteni")
print("B - bért számolni")
print("C - színezni")
print("D - Armstrong szám test")
print("E - piacvetélkedő")
choos=input("válasszon: ")
if choos =="A":
    elso=float(input("Kérem az első számot: "))
    masodik=float(input("Kérem az második számot: "))
    print("{0:>19}{1:>20}{2:>20}".format("3 ill. 2 tizedesen",round(elso,3), round(masodik,2)))
    print("{0:>19}{1:>20}{2:>20}".format("csonkítva",math.floor(elso), math.floor(masodik)))
    print("{0:>19}{1:>20}{2:>20}".format("felfele kerekitve:",math.ceil(elso),math.ceil(masodik)))
    print("{0:>19}{1:>20}{2:>20}".format("egészek köbe",math.ceil(elso) **3, math.ceil(masodik) **3))
elif choos =="B":
    jegyek=random.randrange(200,501)
    print("Az eladott jegyek száma: ", jegyek, "db/n")
    bevetel=jegyek*320
    print("A pénztár bevétele: ", bevetel, "Ft")
    if(bevetel>112000 and bevetel<150000):
        ber=120000+(bevetel*0.01)
        print("Pénztáros fizetése: ", ber,"Ft")
    else:
        ber=120000*0.99
        print("Pénztáros fizetése: ",ber,"Ft")
elif choos =="C":
    os.system("color f1")
    #print(colorama.Fore.BLUE)
    szam1=random.randrange(100,150)
    szam2=random.randrange(20,81)
    print("Az első véletlenszám: ", szam1)
    print("Az második véletlenszám: ", szam2, "/n")
    egesz=szam1//szam2
    maradek=szam1%szam2
    print("Az osztás egész része: ",egesz)
    print("Az osztás egész része: ",maradek)
elif choos =="D":
    szam=int(input("Kérek egy három jegyű pozitív egész számot: "))
    if(szam>99 and szam<1000):
        szazasok=szam//100
        tizesek=(szam%100)//10
        egyesek=(szam%100)%10
        kobosszeg =(szazasok**3)+(tizesek**3)+(egyesek**3)
        if(szam == kobosszeg):
            print("A megadott szám Armstrong szám")
        else:
            print("A megadott nem szám Armstrong szám")
    else:
        print("learn to OLVAS!")
elif choos =="E":
    kispest= random.randrange(150,201)
    fenyUtca= random.randrange(201,251)
    print("kispest: ", round(kispest, 2))
    print("Fény utca: ", round(fenyUtca, 2))
    print("")
else:
    print("error 404")