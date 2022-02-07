import os
import random

def main():
    os.system("cls")
    list=[]
    betuszam=random.randrange(1,101)
    print(betuszam)
    for i in range(0, betuszam):
        list.append(random.randrange(97,123))
        list[i]=chr(list[i])
    print(*list, end= " ")
    
    for j in range(1,11):
        csereindex=random.randrange(1,len(list)-1)
        if(csereindex%2!=0):
            list[csereindex]=" "
    print(list)
    for i in range(1,len(list),2):
        list[i]=list[i].upper()
    print(list)
    s="".join(list)
    print(s)
    print(s.split()[1])

def meh():
    print("Milyen műveletet szeretne gyakorolni?\n")
    print("\t1. Összeadás\n\t2.Kivonás\n\t3. Szorzás")
    valasz=int(input("valasztás (1-3): "))
    print("")
    db=0
    ok=0
    #   c==B
    while(ok<5):
        db = db+1
        a= random.randrange(1,11)
        b= random.randrange(1,11)
        if(valasz==1):
            print(str(a+"+"+str(b)+"=",end=' ' ))
            d=a+b
            c=int(input(""))
        elif(valasz==2):
            print(str(a+"-"+str(b)+"=",end=' ' ))
            d=a+b
            c=int(input(""))
        elif valasz==3:
            print(str(a+"+"+str(b)+"=",end=' ' ))
            d=a+b
            c=int(input(""))
        else:
            print("nope")
            meh()
        if(c==d):
            ok=ok+1
            print("helyes")
        else:
            print("                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          0,,,,,,,,,,,,,,,,,,,,hibas")


if __name__=='__main__':
    meh()