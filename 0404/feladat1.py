from os import system as ww

def feladat2(h):
    for i in range(10):
        print(f"{i+1}. fogási adat: {[(h[i][j]) for j in range(7)]}", end=" ")
        print("")

def feladat3(h):
    return len(h)

def feladat4(hf):
    print(f"\nA naplóban szereplő halfajok:",*hf)

def feladat5(h, a):
    datumok=[]
    for j in range(len(h)):
        if str(a) in str(h[j][0]):
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

def feladat6(h):
    tagok=[]
    for i in range(len(h)):
        tagok.append(h[i][0])
    #halmozás megszűntetése
    tagok=list(set(tagok))
    return len(tagok)

def feladat7(h):
    januar=[]
    
    for i in range(len(h)):
        if(h[i][1]==1):
            januar.append(h[i][0])

    return list(set(januar))

def feladat8(h, hf):
    legtobb=[]
    for i in range(3,7,1):
        legtobb.append(max([adat[i] for adat in h]))
    maxfogas=max(legtobb)
    maxfogassss=legtobb.index(maxfogas)
    print(f"\nLegnagyobb mennyiségű fogás: {[[break if(h[i][maxfogassss+1==maxfogas])]for i in range(len(h))]}")

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
    feladat4(halfajok)
    azonosito=int(input("Adjon meg egy horgász azonosítót:\n"))
    if(type(feladat5(halak, azonosito)) is str):
        print(feladat5(halak, azonosito))
    else:
        print("az alábbi napokon volt fogása:")
        print(*feladat5(halak,azonosito))
    print(f"Januárban halat fogó horgász azonosítók:\n{[*feladat7(halak)]}")

if __name__=='__main__':
    main()