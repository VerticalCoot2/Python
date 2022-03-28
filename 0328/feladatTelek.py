from inspect import _void
from os.path import exists as ex
from os import system as sis

def exist():
    file_exists = ex("H:\Python\\0328\\negyzet.txt")
    return file_exists

def feladat1(t):
    for i in range(len(t)):
        print(f"{t[i][0]} {t[i][1]}:{t[i][2]} x {t[i][3]} méter", sep="")

def feladat2(t):
    for i in range(len(t)):
        print(f"{i+1} \t {t[i][2]} x {t[i][3]}", sep="")

def feladat3(t):
    meretek=[]
    for i in range(len(t)):
        meretek.append(t[i][2]*t[i][3])
    legnagyobb=max(meretek)
    hanyadik=meretek.index(legnagyobb)
    print(f"\nLegnagyobb Méretű telek: {legnagyobb} m2")
    print(f"{t[hanyadik][0]} {t[hanyadik][1]} tulajdonna")

def feladat4(t):
    if(exist()):
        ki=open("negyzet.txt","a",encoding="utf-8")
        db=0
        for i in range(t):
            if(t[i][2]==t[i][2]):
                db += 1
        if db==0:
            print("\nNincs négyzet alakú telek!")
            print("Négyzet alakú telek!", file=ki)
        else:
            print(f"\n{db}db négyzet alakú telek van")
            print(f"{db}db négyzet alakú telek van", file=ki)
        ki.close()
    else:
        ki=open("negyzet.txt","w",encoding="utf-8")
        db=0
        for i in range(t):
            if(t[i][2]==t[i][2]):
                db += 1
        if db==0:
            print("\nNincs négyzet alakú telek!")
            print("Négyzet alakú telek!", file=ki)
        else:
            print(f"\n{db}db négyzet alakú telek van")
            print(f"{db}db négyzet alakú telek van", file=ki)
        ki.close()
def feladat5(t):
    pass

def main() -> _void:
    sis('cls')
    print("TELEK feladat")
    telkek=[]
    be=open("telek.txt","r", encoding="utf-8")
    for sor in be:
        sor=sor.strip().split(" ")
        sor[2]=int(sor[2])
        sor[3]=int(sor[3])
        telkek.append(sor)
    be.close

if __name__=='__main__':
    main()