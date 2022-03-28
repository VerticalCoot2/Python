from os import system as s
from random import randrange as rand
import thirdparty as out
def harmasatlag(list):
    helper=0
    for i in range (4):
        helper=helper+list[2][i]
    return helper/len(list)
def main():
    tt=int(input("\n\n              Melyik feladatod szeretné megnyitni?\n"))
    if tt==1:
        Feladat1()
    elif tt==2:
        Feladat2()
def Feladat1():
    s("cls")
    print("3 személy életkora véletlen értékkel: \n")
    age1=rand(1,91)
    age2=rand(1,91)
    age3=rand(1,91)
    print(f" {age1}, {age2}, {age3} \n")
    print(f"Átlagéletkor: {out.atlag(age1,age2,age3)} év")
    print(f"Évtized: {out.evtized(age2)}")
    print(f"Az évtized {out.vizsgalat(age2).lower()}.")
def Feladat2():
    s("cls")
    tanulok=[[12,14,16,18], [11,13,15,17], [10,14,12,13]]
    print(f"tanulok eredményei")
    print(tanulok)
    print(*tanulok)
    print(f"\nTanulók eredményei(kölön sorokban)")
    for i in range(3):
        print(f"{i+1}, tanuló eredményei")
        for j in range(4):
            print(f"{tanulok[i][j]}", end=" ")
        print("")
    print(f"\n2.harmadik feladatának pontos száma: {tanulok[1][2]}\n\nHarmadik tanuló pontszámai: ")
    for j in range(4):
        print(tanulok[2][j] , end=" ")
    print("")
    print("\n2.feladat pontszamai: ")
    for i in range(3):
        print(tanulok[i][1])
    print("\n Pontszamok atlaga 2 tizedesre kerekítve")
    osszeg=0
    for i in range(3):
        for j in range(4):
            osszeg =osszeg+tanulok[i][j]
    atlag=round(osszeg/12,2)
    print(atlag)
        

if __name__=='__main__':
    main()