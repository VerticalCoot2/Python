import os

def beker():
    global szam1, szam2
    szam1 = int(input("Első szám"))
    szam2 = int(input("Második szám"))
    print("")
def muvelet():
    szam3=1
    szamitas= (szam1+szam2)-szam3
    print(szamitas)
os.system("cls")
beker()
muvelet()