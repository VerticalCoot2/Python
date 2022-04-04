import os
import random
import math
os.system("cls")
def main():
    letters = [0]*10
    price= int(input("Adja meg a borítéka árát: "))
    piece=0
    for i in range(0,len(letters), 1):
        piece = random.randrange(20,201)
        letters[i] = piece
#a
    print(*letters,"\n")
#b
    b=(letters[3]+letters[6])*price
    print(b,"FT Bevétele szármzott a 4. és a 7. napon\n")
#c
    for j in range(0,len(letters),1):
        if (60<letters[j]<110):
            print(f"(2x){letters[j]*2}", end=" ")
        else:
            print(f"(3x){letters[j]*3}", end=" ")
    print("\n")
#d
    stamps=[0]*10
    piece2=0
    for k in range(0,len(stamps),1):
        piece2=random.randrange(20,201)
        stamps[k]=piece2
    d=(letters[4]+letters[5]+letters[6]+letters[7]+letters[8]+letters[9])
    d2=(stamps[4]+stamps[5]+stamps[6]+stamps[7]+stamps[8]+stamps[9])
    if(d>d2):
        print(f"{d-d2}-vel/al adtak el több levelet\n")
    else:
        print(f"{d2-d}-vel/al adtak el több bélyeget\n")
#e
    e1=stamps[5]
    e2=letters[1]
    e3=((e1+e2)/2)%2
    if(e3==0):
        print("Páros. \n")
    else:
        print("Páratlan. \n")
#f
    osszeg=0
    osszeg2=0
    for t in range(0,len(letters),1):
        osszeg = osszeg + letters[t]
        osszeg = osszeg/len(letters)

    for l in range(0,len(stamps),1):
        osszeg2 = osszeg2 + stamps[l]
        osszeg2 = osszeg2/len(stamps)
    f=[osszeg, osszeg2]
    f2=max(f)-min(f)
    print(f"A külöönbség: {round(f2)} ")

    

    


if __name__ =='__main__':
    main()