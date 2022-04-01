from os import system

def aFeladat(aa):
    b=0
    for i in aa:
        if i==min(aa):
            print(f"A legkissebb érték a(z) {str(min(aa))}, és a(z) {str(i+1)}.-ik napon volt")
        else:
            b += 1

def bFeladat(bb):
    jutalek=[]
    for i in bb:
        jutalek.append(str(f"A váltó jutaléka a(z) {i+1}. napon {bb[i]/0.05} volt.\n"))
    return jutalek

def cFeladat(cc):
    pass

def dFeladat(dd):
    pass

def eFeladat(ee):
    pass


def main():
    system("cls")
    lp=int(input("hány napon keresztül szeretné megadni?\n"))
    arfolyam=[]
    for i in range(lp):
        adatok=input(f"Adja meg a(z) {i+1}. árat.\n")
        arfolyam.append(adatok)
    print("\n a.) feladat")
    aFeladat(arfolyam)
    print(f"\n b.) feladat \n{bFeladat(arfolyam)}\n\nc.)feladat")#imu62262995259225995295292595299529259
    arfolyamok=[299, 310, 297, 321, 318, 301, 285, 392]
    print(*arfolyamok, "\nd.) feladat")




if __name__=='__main__':
    main()