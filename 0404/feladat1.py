from os import system as ww
from turtle import st

def feladat2(h):
    for i in range(10):
        print(f"{i+1}. fogási adat: {[(h[i][j]) for j in range(7)]}", end=" ")
        print("")+

def feladat3(h):
    return len(h)

def feladat4(hf):
    print(f"\nA naplóban szereplő halfajok:",*hf)

def feladat5(h, a):
    datumok=[]
    if a in h:
        for i in range(len(h)):
            if h[i][0]==a:
                if h[i][1] < 10:
                    honap="0"+str(h[i][1])
                else:
                    honap=h[i][1]
                if h[i][2] < 10:
                    nap="0"+str(h[i][2])
                else:
                    nap=h[i][2]
                datumok.append(honap+"."+nap)
        return datumok
    else:
        return "Nincs ilyen horgász azonisító."
        

def main():
    ww("cls")
    halak=[]
    halfajok=["ponty","csuka","süllő","harcsa"]
    #1.) file beolvasása
    be=open("naplo.txt","r",encoding="utf-8")
    for sor in be:
        #adott sor átalakítása kislistává
        sor=sor.strip().split(" ")
        #elemek átlakítása int ill. float típussá
        for i in range(7):
            if("." in sor[i]):
                sor[i]=float(sor[i])
            else:
                sor[i]=int(sor[i])
        #sor elemei -> nagy 2d listába (halak)
        halak.append(sor)        
    be.close()
    #2.) feladat
    feladat2(halak)
    print(f"\nA fogási naplóban szereplő adatok száma: {feladat3(halak)}")
    azonosito=int(input("Adjon meg egy horgász azonosítót:\n"))
    if(type(feladat5(halak, azonosito)) is str):
        print(feladat5(halak, azonosito))
    else:
        print("az alábbi napokon volt fogása:")
        print(*feladat5(halak,azonosito))


if __name__=='__main__':
    main()