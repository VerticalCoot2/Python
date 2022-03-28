from os import system

def aFeladat(aa):
    min_ = aa[0]
    mini = 0
    for i in range(len(aa)):
        if aa[i] < min_:
            min_ = aa[i]
            mini = i + 1

    print(f"A legkissebb érték a(z) {min_}, és a(z) {mini}.-ik napon volt")
def bFeladat(bb):
    jutalek=[]
    for i in range(len(bb)):
        jutalek.append(str(f"A váltó jutaléka a(z) {i+1}. napon {bb[i]/0.05} volt."))
    return jutalek

def dFeladat(dd):
    newlist = []

    for i in range(len(dd)):
        if(190<dd[i]<315):
            newlist.append(dd[i]*3)

    return newlist

def eFeladat(ee):
    harom=0
    ketto=0
    for i in range(1,len(ee),2):
        if(ee[i]%3==0):
            harom+=1
    if(len(ee)==harom):
        print("Nincs ilyen")
    else:
        for i in range(len(ee/2)):
            print(ee[i])
            


def main():
    system("cls")
    lp=int(input("hány napon keresztül szeretné megadni?\n"))
    arfolyam=[]
    for i in range(lp):
        adatok=int(input(f"Adja meg a(z) {i+1}. árat.\n"))
        arfolyam.append(adatok)
    print("\n a.) feladat")
    aFeladat(arfolyam)
    print(f"\n b.) feladat \n{'\n'.join(bFeladat(arfolyam))}\n\nc.)feladat")#imu62262995259225995295292595299529259
    arfolyamok=[299, 310, 297, 321, 318, 301, 285, 392]
    print(*arfolyamok, "\nd.) feladat")
    dFeladat(arfolyam)


if __name__=='__main__':
    main()