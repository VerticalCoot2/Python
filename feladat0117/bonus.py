import os
def adat():
    a=int(input("Num 1: "))
    b=int(input("Num 2: "))
    return a, b
def calc():
    c=adat()
    if(c[0]>c[1]):
        print(f"A {c[0]} nagyobb szám")
    elif(c[0]<c[1]):
        print(f"A(z) {c[1]} nagyobb szám")
    else:
        print("a két szám egyenlő")
os.system("cls")
calc()