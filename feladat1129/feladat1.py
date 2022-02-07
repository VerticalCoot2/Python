import os
import random
os.system("cls")

def main():
    autok=["Lamborghini", "Ferrari", "Lada"]
    for i in range(0,len(autok), 1):
        print(autok[i],)
    for i in range(0,len(autok), 1):
        print(autok[2])
    autok.append("Volga")
    print(autok[3])
    autok[3]="Nissan"
    print(autok[3])
    input()
    os.system("cls")
    Numbers()
def Numbers():
    szamok=[3,12,11,18,5,8,17,2,1,4]
    print(len(szamok))
    print(szamok.index(2)+1)
    del szamok[2]
    print(len(szamok))
    print(szamok)
    szamok.remove(12)
    print(szamok)
    szamok.sort()
    print(szamok)
    szamok.reverse()
    print(szamok)
    input()
    os.system("cls")
    numsII()
def numsII():
    szamok=[0]*6
    for i in range(0,len(szamok),1):
        szamok[i]=int((input("Adja meg az "+str(i+1)+" . számot")))
    for i in range(3, len(szamok),1):
        if(szamok[i]%2==0):
            print(szamok[i])
    input()
    os.system("cls")
    atlagMagassag()
def atlagMagassag():
    magassagok=[0]*16
    print("16 véletlen magasság érték: ")
    for i in range(0,len(magassagok,1)):
        magassagok[i]=random.randrange(170,185)
        print(magassagok[i], end=" ")
        #atlag
        osszeg = 0
        for i in range(0,len(magassagok),1):
            osszeg=osszeg+magassagok[i]
    print("")
    print(magassagok)
    atlag =osszeg/len(magassagok)+1

    print










if __name__ == "__main__":
    main()