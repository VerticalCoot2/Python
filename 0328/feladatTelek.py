from os.path import exists as ex
from os import system as sis

def exist():
    file_exists = ex("H:\Python\0328\tulajok.txt")
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

def main():
    sis('cls')
    telkek=[]
    be=open("telek.txt","r", encoding="utf-8")
    for sor in be:
        sor=sor.strip().split(" ")
        sor[2]=int(sor[2])
        sor[3]=int(sor[3])
        telkek.append(sor)
    be.close