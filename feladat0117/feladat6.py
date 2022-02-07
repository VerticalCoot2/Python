import os

def beker():
    global szam1, szam2
    szam1 = int(input("Első szám"))
    szam2 = int(input("Második szám"))
    print("")
def muvelet():
    szam3=1
    return (szam1+szam2)-szam3
os.system("cls")
beker()
print(muvelet())