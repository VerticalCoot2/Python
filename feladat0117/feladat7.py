import os

def beker():
    szam1=int(input("Első szám: "))
    szam2=int(input("Második szám: "))
    print("")
    return szam1, szam2
def muvelet():
    szamok=beker()
    szam3=1
    szamitas=(szamok[0]+szamok[1])-szam3

os.system("cls")
muvelet()